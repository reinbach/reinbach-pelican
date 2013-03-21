Title: Server for AngularJS App
Date: 2013-01-24
Tags: python
Slug: server-for-angularjs-app
Author: Greg Reinbach

Working on my [Finance App](https://github.com/reinbach/finance) I wanted the website to be a standalone JS application for which I am using [AngularJS](http://angularjs.org/). To make that happen I needed a simple server to deliver the necessary javascript, css and html files that make up the javascript application to the client (browser).

So I decided to make use of [Werkzeug](http://werkzeug.pocoo.org/) and ended up with the following straight forward [python code](https://gist.github.com/4623828) to deliver the application code.

I wanted to stick with the angular-seed application format/layout of code and so the static files are delivered via the SharedDataMiddleware with the relevant paths defined there.

HTML files are delivered in the normal manner. A couple of improvements could be to only allow .html files and robots.txt files. It's still early days in the development of this project, so things may change as I learn more.
