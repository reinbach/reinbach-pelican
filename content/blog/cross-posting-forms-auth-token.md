Title: Cross Posting Forms with Auth Token
Date: 2013-02-16
Tags: flask
Slug: cross-posting-forms-auth-token
Author: Greg Reinbach

On a follow up to [Cross Posting Forms)]http://www.reinbach.com/blog/cross-posting-forms) I wanted to be able to authenticate the user and decided to make use of an auth token, which would then be set client side and the client would supply it in each subsequent request.

Well that was added simply enough on the client side, but it took me a while to realize why it was not working on the server side of things.

I finally realized that when adding new headers to the requests, I need to add them to the headers list in the crossdomain decorator so that they pass through;

    @app.route("/login", methods=['POST')
    @crossdomain(origin='*', headers='origin, x-requested-with, content-type, accept, authtoken')
    def login():
        ...<snip>...

Otherwise it would be stripped out of the headers and I would end up constantly asking the client to authenticate and get no where.
