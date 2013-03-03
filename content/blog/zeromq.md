Title: zeromq
Date: 2011-09-03
Tags: zeromq
Slug: zeromq
Author: Greg Reinbach

[ZeroMQ](http://www.zeromq.org/) is a messaging layer that is blazingly fast. There is a great [intro to zeromq](http://nichol.as/zeromq-an-introduction) by [Nicholas Piël](http://nichol.as/).

I've been needing to get some decent messaging layer in place and so I decided to try zeromq out.

Grabbed the latest version (currently [2.1.9](http://download.zeromq.org/zeromq-2.1.9.tar.gz))

    cd /path/to/downloaded/zeromq-2.1.9
    ./configure --prefix=/usr/local
    make
    sudo make install

Then because I make use of virtualenv, I wanted to install the pyzmq libs in the specific virtualenv I was working on. First I downloaded the pyzmq lib (currently [2.1.9](https://github.com/zeromq/pyzmq/downloads/pyzmq-2.1.9.tar.gz)

    source /path/to/virtualenv/bin/activate
    cd /path/to/downloaded/pyzmq-2.1.9
    python setup.py  configure --zmq=/usr/local
    python setup.py install

And just to confirm that all is well, you can do the following;

    python -c "import zmq"

If you get no errors you're golden.

Now onto the  [ZeroMQ Guide](http://zguide.zeromq.org/page:all). It is a pretty lengthy endeavor, but there are loads of great sample code in many different languages. The [guide and sample code](https://github.com/imatix/zguide), can also be accessed from GitHub. 
