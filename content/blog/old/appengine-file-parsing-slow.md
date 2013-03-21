Title: appengine file parsing slow?
Date: 2011-08-13
Tags: appengine, postgresql, python
Slug: appengine-file-parsing-slow
Author: Greg Reinbach

I am working on a web application project that needs to handle an xls file that has a little over 8 thousand products in it. I started off developing this project on the app engine platform making use of webapp2 for the framework.

But when I got to the part of uploading the file and having to parse it, making use of xlrd to read the file etc, everything just seemed incredibly slow. So first thoughts were that I was doing something wrong, that my code was bad and needed to be optimized. Even though this was code that I had used in a very similar scenario to parse thousand line files and dump the data in a database.

This is not a very large dataset at all. So after digging around and looking for all the dos and dont's, making use of batch querying etc. I still was not having much luck with speed. So this has me a little concerned about the app engine platform. Not wanting to spend too much time trying to optimize this like crazy at such an early point of the development cycle. I really just want to get this web app up and running as a prototype, I jumped back to using my good ol faithful postgres.

The main difference in the way/manner I was working with the file on the app engine platform was to pass the contents to the xlrd reader, instead of usually passing in the filename/path and letting it open the file. The file was only 3.7MB, so that may have been an issue. Also I could have made use of the BlogStore, maybe that would have been a better angle on handling the file upload/parsing.

I'm sure there is something I can do better on the app engine platform to make this a lot speedier, will just need to hunt down what that is. For now I'm plugging away and happy as a clam with postgres.
