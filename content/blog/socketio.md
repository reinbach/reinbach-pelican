Title: socket.io
Date: 2012-06-30
Tags: javascript, python
Slug: socketio
Author: Greg Reinbach

There are times when you need to communicate between the browser and the server without having to reload the page. That just saves a bunch of bandwidth, improves the user experience and is generally termed as AJAX. But now and then it is helpful to keep this connection between the browser and server open for a more extended time frame. This saves in some processing from opening/closing connections. In the past this has been considered long polling.

Now with "real time" apps or apps that have a more "desktop" like experience you want to be improve the connection/speed between the client/browser and the server, so keeping a connection open and streaming the relevant data to the browser really helps with this. It's a lot better than having to refresh the page continuously and provides the impression that the web app is more responsive.

This is where [socket.io](http://socket.io/) comes into play. It handles most of the issues with keeping this connection open, and especially handles the nuances of each browser. It will make use of websockets where possible and gracefully fail down to using flash for those older browsers.

Now seeing that I make use of Python for more programming fix, thankfully there is the nice package for this called [gevent-socketio](https://github.com/abourget/gevent-socketio) that makes things simpler.

So with that I have created a few simple examples with it to get a feel for using it;

- [gevent-socketio-example](https://github.com/reinbach/gevent-socketio-example)
- [gevent-zmq-socketio-example](https://github.com/reinbach/gevent-zmq-socketio-example)

Really nice and this opens a lot of possibilities which I hope to play with now.
