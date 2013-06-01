Title: Rackspace Arch Linux WebServer
Date: 2013-05-27
Tags: server
Slug: rackspace-arch-webserver
Author: Greg Reinbach

This is how I setup my web servers on Rackspace. I make use of nginx and uWSGI where the websites make use of a few different frameworks, mainly Django, Flask, and plain static HTML sites.

My preferred Linux distro is [Arch Linux](https://www.archlinux.org/), so when setting up the server on [Rackspace](https://www.rackspace.com/) that is the distro I select and the rest of the instructions are applicable to that distro.

Once the server has been created and is up and running, I update the system. See [previous article](|filename|rackspace-server-arch.md) on the steps I take to do that.


Setup nginx
-----------

    # install nginx
    pacman -S nginx

    # setup nginx to start when server starts
    systemctl enable nginx
    systemctl start nginx

    # update nginx.conf (/etc/nginx/nginx.conf) file
    vi /etc/nginx/nginx.conf

    # comment out server settings
    # and add the following to the bottom of the file;
    include /opt/nginx/conf/sites/*;

I place the various sites nginx config files in `/opt/nginx/conf/sites/` so need to create the directory.

    mkdir -p /opt/nginx/conf/sites/


Setup uWSGI
-----------

    # install uWSGI
    cd /opt/
    wget https://aur.archlinux.org/packages/uw/uwsgi/uwsgi.tar.gz
    tar -zxvf uwsgi.tar.gz
    cd /opt/uwsgi
    makepkg --asroot
    pacman -U uwsgi*.pkg.*
    cp emperor.uwsgi.service  /etc/systemd/system/uwsgi.service

    # setup uwsgi user and log files
    useradd -c 'uwsgi user'  --system --no-create-home uwsgi
    mkdir -p /var/log/uwsgi
    chown -R uwsgi /var/log/uwsgi

    # update emperor.ini file
    vi /etc/uwsgi/emperor.ini

    # emperor.ini contents
    [uwsgi]
    uid = <uwsgi_uid> # <- get this from the /etc/passwd file
    logto = /var/log/uwsgi/uwsgi.log
    emperor = /etc/uwsgi/apps
    master = 1

    # start up uwsgi
    systemctl enable uwsgi
    systemctl start uwsgi


Setup VirtualEnv
----------------

I setup each of the websites in it's own virtual environment.

    pacman -S python-virtualenvwrapper

    # create/update ~/.bashrc and add relevant virtualenv wrapper details
    vi ~/.bashrc

    # add virtualenv wrapper details to .bashrc file
    export WORKON_HOME=~/env
    source /usr/bin/virtualenvwrapper.sh


Various other required libs
---------------------------

Install the relevant repo clients you make use of. For me that is Git and Mecurial.

    pacman -S git


Depending on which databases you make use of you may need the relevant database libs. I make use of PostgreSQL for my database needs most of the time and the sites require psycopg2, which in turn needs the postgresql libs.

    pacman -S  postgresql-libs

And that is it, I'm now all set to ran my fabric scripts, which setup and/or update the relevant site.