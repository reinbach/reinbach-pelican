Title: Mountain Lion Setup
Date: 2012-08-31
Tags: general
Slug: mountain-lion-setup
Author: Greg Reinbach

Most of my development is with Python, Django, Gevent, ZeroMQ and mainly with Web Applications. With that in mind I just upgraded to the latest mac osx "Mountain Lion" and did the following to get myself setup.

First things first get XCode and install the Command Line Tools package, and make sure it is up to date. Or you can make use of the stand alone CLI package.

Next install "homebrew", can't leave home without it.

With most of my development making use of Python, I make use of virtualenv and virtualenvwrapper to separate the various projects.

    brew install virtualenv
    brew install virtualenvwrapper

I like to make use of Gevent in a lot of projects, but to be able to installed gevent in the various virtualenv, libevent needs to be installed globally for gevent to build against.

    brew install libevent

MySQL is used as the database for some projects. Grabbed the  and ran into an issue with the lib not being found, so created a symbolic link for it;

    sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib

Less is used for css styling and that is compressed as well. So needed node.js and relevant less package;

    brew install node.js
    curl https://npmjs.org/install.sh | sh
    npm install --global less

This pretty much gets me to the state that I like to have as a development machine. Hopefully I remembered everything here.
   

