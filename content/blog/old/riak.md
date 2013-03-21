Title: riak
Date: 2012-01-12
Tags: riak
Slug: riak
Author: Greg Reinbach

I've been playing around with [Riak](http://basho.com/products/riak-overview/) lately and wanted to make use of the [python client](https://github.com/basho/riak-python-client). Ran into a small issue setting it all up in virtualenv. My system is Arch Linux.

After making sure protobuf was installed system wide, currently the latest version is 2.4.1.
In my virtualenv I did the following to get it all sorted out;

    wget http://protobuf.googlecode.com/files/protobuf-2.4.1.tar.bz2
    tar -jxvf protobuf-2.4.1.tar.bz2
    cd protobuf-2.4.1/python/
    python setup.py install
    pip install riak

Make sure you download the protobuf version that matches what you installed system wide. See [download page](http://code.google.com/p/protobuf/downloads/list)

Running "pip install riak" first and it was attempting to pull in a protobuf library from basho and for some reason it was failing. So did the above and things look good.

