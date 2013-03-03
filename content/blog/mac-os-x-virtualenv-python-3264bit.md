Title: mac os x virtualenv python 32/64bit
Date: 2011-02-22
Tags: python
Slug: mac-os-x-virtualenv-python-3264bit
Author: Greg Reinbach

I've been using virutalenv for a long time now for development purposes and it works extremely well.

Although lately I have run into some issues with trying to work with trying to run python as 32bit in one environment and 64bit in another. I must say it is all completely crazy trying to keep this all together, especially when you need to have other applications running at a specific architecture as well.

I had MySQL installed at 64bit with MySQL-python and all was working well with the virtualenv that had python at 64bit. But now I had to change python to 32bit, and that required me to "downgrade" MySQL to 32bit instead.

On a Mac (10.6) it is simple enough to switch between 32 and 64it and visa versa with the following commands

    For 64bit
    defaults write com.apple.versioner.python Prefer-32-Bit -bool no 

    For 32bit
    defaults write com.apple.versioner.python Prefer-32-Bit -bool yes

But sadly those do not affect the virtualenv, in order to modify the virtualenv python you need to do the following;

    $ lipo -info /Users/cogg/.virtualenvs/tweakeats/bin/python
    Architectures in the fat file: /Users/cogg/.virtualenvs/tweakeats/bin/python are: x86_64 i386 ppc7400
    $ mv /Users/cogg/.virtualenvs/tweakeats/bin/python /Users/cogg/.virtualenvs/tweakeats/bin/python.old
    $ lipo -remove x86_64 /Users/cogg/.virtualenvs/tweakeats/bin/python.old -output /Users/cogg/.virtualenvs/tweakeats/bin/python
    $ python
    [...]
    >>> import sys
    >>> sys.maxint
    2147483647

That was found on [stackoverflow](http://stackoverflow.com/questions/2088569/how-do-i-force-python-to-be-32-bit-on-snow-leopard-and-other-32-bit-64-bit-questi)
