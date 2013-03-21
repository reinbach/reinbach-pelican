Title: gevent
Date: 2011-09-02
Tags: gevent, python
Slug: gevent
Author: Greg Reinbach

Playing around with [gevents](http://www.gevent.org/). Easily enough installed/setup. First you need the [libevent](http://monkey.org/~provos/libevent/) requirements installed. I downloaded 2.0.13 and did the following;
    
    ./configure --prefix=/usr/local
    make
    sudo make install

There after you can use pip to finish up installing the rest of the requirements and gevent itself

    pip install greenlet
    pip install gevent

A quick test to make sure you're all set;

    python
    import gevent

That's it. You're ready to play.
