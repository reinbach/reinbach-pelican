Title: nginx + uWSGI - Emperor
Date: 2013-05-11
Tags: server, nginx, uwsgi
Slug: nginx-uwsgi-emperor
Author: Greg Reinbach

I upgraded my rackspace server to the new generation version and made some slight changes to the nginx and uwsgi setup. The websites now make use of a slightly different nginx and uWSGI configuration setup.

The main change is with the [uWSGI](https://projects.unbit.it/uwsgi/) files and I am making use of the [Emperor](http://uwsgi-docs.readthedocs.org/en/latest/Emperor.html) configuration rather. This is the suggested method if one has a number of apps on a single server.

This change required me tweaking the nginx config file and setting up a uwsgi configuration file for the websites. I modified the main nginx config file by adding `include /opt/nginx/conf/sites/*;` to it so each of the websites separate nginx conf files would be read and implemented.

Then for each website the following config files would be setup;


nginx config
------------

    server {
        listen 80;
        server_name *.example.com;
        error_log /var/log/nginx/example-error.log;
        access_log /var/log/nginx/example-access.log;

        location / {
            uwsgi_pass 127.0.0.1:9001;
            include uwsgi_params;
        }
    }

This is a very simple example, the main part is the `location` section where I pass in the Port number that the uWSGI instance will be running on and the default `include uwsgi_params`.


uwsgi config
------------

    [uwsgi]
    chdir = /opt/sites/example/
    master = true
    threads = 20
    socket = 127.0.0.1:9001
    callable = app
    module = uwsgi_app
    logto = /var/log/uwsgi/example.log
    virtualenv = /opt/sites/example/
    processes = 4

I make use of the `ini` config style and each website will have one of these. The `socket` value needs to match up with the `uwsgi_pass` value used in the nginx config file.

I make use of virtualenv to manage/handle the website instances and so the `virtualenv` option is included.

`module` points to the wsgi file in the website and that file will depend on the framework (Django, Flask etc. in my instance) being used for the website.

`callable` value needs to match the param that the wsgi file is using to set the website instance to.

Then depending on the framework used for the web site their would be a wsgi file setup to instantiate the website.

Django wsgi file sample
-----------------------

    import sys
    import os

    sys.path.append(os.path.abspath("{0}/{1}".format(
        os.path.dirname(__file__),
        "example"
    )))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

    import django.core.handlers.wsgi

    app = django.core.handlers.wsgi.WSGIHandler()

Note the `app` param is what needs to match what the `callable` value is in the uWSGI config file.

Flask wsgi file sample
----------------------

    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    from example import app

    if __name__ == '__main__':
        app.run()
