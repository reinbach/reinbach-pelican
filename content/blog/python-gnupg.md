Title: python-gnupg
Date: 2011-09-13
Tags: python
Slug: python-gnupg
Author: Greg Reinbach

At CashStar I had to implement some interactions with files being sent to us and needing to decrypt them on the fly. [GPG](http://www.gnupg.org/) was the encryption we were using and I decided to make use of python-gnupg for my side of the code. GnuPrivacyGuard needs to be installed as python-gnupg is a wrapper to that.

Developing on a mac I found that installing [GPGTools](http://www.gpgtools.org/installer/index.html) was the easiest route in doing that. On the servers we would do the normal compiling of the relevant source code to install. There are currently 2 versions of GPG out there 1.41 and 2.018. GPGTools installs both and a bunch of other goodies.

To install python-gnupg, the ever faithful pip does the trick

    pip install python-gnupg

Now you can do everything you need to do through python. If you run into any issues, a good resource is either the [docs](http://packages.python.org/python-gnupg/) or to actually go and [download the source](http://code.google.com/p/python-gnupg/downloads/list) and there is a file there called test_gnupg.py that gives you all the example code you need.


