Title: uwsgi+nginx+flask virtualenv mac os x
Date: 2011-09-05
Tags: uwsgi, nginx
Slug: uwsgi-nginx-flask-virtualenv-mac-os-x
Author: Greg Reinbach

Ok the title is a little misleading, I did not manage to get everything happening within the virtualenv. The only part not there is nginx. I have nginx setup system wide.

There was plenty of resources out there in setting up a [virtualenv](http://pypi.python.org/pypi/virtualenv), so it is assumed that you have that as well as having [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) and [pip](http://pypi.python.org/pypi/pip) installed.

Create VirtualEnv
===========

    mkvirtualenv --no-site-packages sample


uWSGI
====

Install uwsgi making use of pip, makes life nice and easy;

    pip install http://projects.unbit.it/downloads/uwsgi-latest.tar.gz


nginx
====

Now we need to break out our compiling chops to install [nginx](http://nginx.org/). You can find the latest version on the [download page](http://nginx.org/en/download.html)
I downloaded version 1.1.2 and untar'd it all through the browser. Next thing is in the terminal head on over to the untar'd dir

    cd ~/Downloads/nginx-1.1.2
    ./configure --prefix=/usr/local/ --with-http_ssl_module
    make
    sudo make install

I added the --with-http_ssl_module config option as I am expecting to do some SSL work on my projects. This sample does not make use of it at all. You no longer have to add the --add-module=../uwsgi/nginx/ config option as nginx automatically includes that now.

Next you need to configure the nginx config files. I made use of the sites-available sites-enabled dir structure to manage the various configured local sites.

    cd /usr/local
    make nginx
    cd  nginx
    mkdir sites-available sites-enabled
    touch sites-available/sample
    ln -s sites-available sites-enabled/sample

We need to tell nginx to make use of the config files placed in these directories and we do that by adding the following line;

    include /usr/local/nginx/sites-enabled/*;

Right before the last } in the /usr/local/conf/nginx.conf file.

Now we can add the various nginx config files per website/project. You can use the following template as a starting point. It should get you up and running at least. Add this to the sites-available/sample file.

    server {
        listen 5001;
        server_name localhost;
        set $home /virtualenv/sample/hello;
        access_log /virtualenv/sample/hello/logs/nginx/access.log;
        error_log /virtualenv/sample/hello/logs/nginx/error.log;
     
        rewrite ^/(.*)/favicon.ico$ /static/images/favicon.ico last;
     
        location / {
            uwsgi_pass localhost:3031;
            include uwsgi_params;
            uwsgi_param USWGI_CHDIR $home/deploy;
            uwsgi_param USWGI_INI deploy;
            root $home;
        }
        location /static/ {
            root $home;
            autoindex on;
            error_page 404 = "404";
        }
    }

The "hello" part is our expected sample flask project we are going to create. And "deploy" refers to dir/files we are going to create in the "hello" project. I also added the rewrite rule as that helps prevent the logging of 404 attempts on the favicon which is always asked for by modern browsers nowadays.


Flask
===

Head back to your virtulenv and keep the love going with pip to install Flask;

    workon sample
    pip install flask

We now create the hello world sample project

    mkdir hello
    cd hello
    touch deploy/deploy.ini

Now edit the deploy.ini file and add the following to it.

    [uwsgi]
    socket = 127.0.0.1:3031
    processes = 2
    virtualenv = /virtualenv/sample/
    module = myapp
    callable = app
    touch-reload = /virtualenv/sample/hello/

The touch-reload option is nice for dev, but not a good idea for production systems. In that anytime a file is touched with in the hello dir uwsgi will reload the changes. Saves you having to restart the uwsgi service.
The "myapp" module and "app" callable relates to the app we are yet to create. 

Ok finally to the creating of the sample app. Create a myapp.py file in the hello dir and add the simple hello world flask example;

    from flask import Flask
    app = Flask(__name__)
     
    @app.route('/')
    def hello_world():
        return "Hello World!"
     
    if __name__ == '__main__':
        app.run()
 
We should now be all set to start up the processes and test it out.

    uwsgi --ini deploy/deploy.ini 
    /usr/local/sbin/nginx

Fire up the browser and point it to http://localhost:5001. Hopefully you get the "hello world!" message in your browser.

If you need to stop nginx or reload changes you can do the following;

    /usr/local/sbin/nginx -s reload
    /usr/local/sbin/nginx -s stop


