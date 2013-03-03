Title: Cross Posting Forms
Date: 2013-01-25
Tags: flask, javascript
Slug: cross-posting-forms
Author: Greg Reinbach

My application has 2 different components. An API written in Flask and a JS Application using AngularJS and these are served from different locations/domains. So the API needed to implement [HTTP Access Controls CORS](https://developer.mozilla.org/en-US/docs/HTTP/Access_control_CORS) to allow the requests from different domains.

For the API, I used the following [view decorator](http://flask.pocoo.org/snippets/56/) and I also added

    f.required_methods = ['OPTIONS']

to the decorator function as suggested in the comments. I then implemented the decorator in the following manner;

    @app.route("/login", methods=['POST')
    @crossdomain(origin='*', headers='origin, x-requested-with, content-type, accept')
    def login():
        ...<snip>...

Once that was done the calls from the JS Applicatin worked.

To improve things, I'll probably move the headers param into the decorator function and make it a default rather than having to type it every time.
