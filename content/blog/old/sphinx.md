Title: sphinx
Date: 2011-10-07
Tags: general
Slug: sphinx
Author: Greg Reinbach

In an effort to improve the documenting of my code and some of my projects, I have been looking at the various tools/projects out there that help with this sort of thing. One of them being [Sphinx](http://sphinx.pocoo.org/).

So the idea is that I want to really have a single source for the documentation, and ideally it would be driven by the code. But alas that is really hard to do, so the idea is to add docstrings to your code. These can be read by the sphinx code during a build to help generate the necessary documentation.
The markup/down makes use of [reStructured Text](http://docutils.sourceforge.net/) which is simple to learn and make use of.

I ran a test build against a project I had just started and was very impressed with the results. I actually got a fair amount of information from my code that I told the sphinx build to include. The code had very little dostrings in it at the time, so that was nice to see. 

There is a sphinx-quickstart script that helps to generate the conf.py file and there are a large number of available settings/options you can choose. One being the creation of a makefile, which makes it very easy to rebuild the documentation, with 

    make html

And you have HTML files created of your documentation. You can switch out the "html" option/argument for Latex and various others.

This is just a scratch of what Sphinx is capable of, but I have the basics down and will continue using it and growing/developing my documentation of my codes and projects.

There is a very cool documentation hosting tool out there called [Read the Docs](http://readthedocs.org/) and that can import your Sphinx generated docs. 
