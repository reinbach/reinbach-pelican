Title: more socket.io and zeromq fun
Date: 2012-07-08
Tags: gevent, zeromq, javascript, python, socket.io
Slug: more-socketio-and-zeromq-fun
Author: Greg Reinbach

Playing around with socket.io and zeromq and put together a little triage app. The app has a producer that randoming creates events, which are picked up by the app and tracks them. If any users are connected to the app, the event is send to them. The user can update the event's status, category and/or add comments to the event. These changes are automatically sent to any other user viewing the app at the same time.

[https://github.com/reinbach/mini-triage](https://github.com/reinbach/mini-triage)
