Title: my stack a changing
Date: 2011-09-15
Tags: python
Slug: my-stack-a-changing
Author: Greg Reinbach

Currently I make use of the following simple stack;

* Jinja2
* Django
* MySQL / Postgres
* nginx
* Apache

And based on some of the tasks I have been needing to do (queueing) and handling huge load issues that I have started to encounter. I have started to re-look at this stack.

I definitely need to get some decent queueing mechanism in place, we have started to make use of [Celery](http://celeryproject.org/) at work. But [ZeroMQ](http://www.zeromq.org/) sounds really interesting to me, so want to have a look at that some more. Would like to try it out on some projects soon. So some queueing/messaging layer needs to be added to the stack. 

I just read the great article on [benchmarking python wsgi servers](http://nichol.as/benchmark-of-python-web-servers) by [Nicholas Piël](http://nichol.as/). Based on the results of all the benchmarking he did and what I am seeing/reading about what others are using in their stack I think I am going to try out [gevent](http://www.gevent.org/) and [uwsgi](http://projects.unbit.it/uwsgi/). 

I have also started seeing people making use of different types of databases based on the specific need. This varying from graph databases like [neo4j](http://neo4j.org/) to key-value store like [redis](http://redis.io/) to document orientated databases like [mongoDB](http://www.mongodb.org/). 

For the last few years I have been using Django for my framework and this works extremely well. As you get everything that you would need when developing full featured web applications. There is a great community around it and a huge amount of information out there. But since I started doing some Google AppEngine work, Django did not work very well for that, it is not engineered to and there are better frameworks to do this (since then django-nosql has been developed). It got me thinking about other python frameworks and the possibility that they are better in certain instances. 

So I have been playing with a few of those and expect that some of them will become part of the stack based on the need. In a similar way that various database instances/types are applicable in certain instances. The main ones that I have looked at are [webapp2](http://webapp-improved.appspot.com/), [webpy](http://webpy.org/) and [Flask](http://flask.pocoo.org/)

On the client side of things, HTML5 is gathering a lot of steam and a number of interesting projects are cropping up around Javascript and CSS. Well when I say cropping up, it is relative to what I am only starting to learn about. May have been around for a while, but I am only just now starting to find out about them.

As the use of javascript has grown, fairly large applications have started to be built in javascript and so some straight Javascript frameworks have been created like [Knockout](http://knockoutjs.com/), [SproutCore](http://www.sproutcore.com/), and [backbone.js](http://documentcloud.github.com/backbone/). There is also [CoffeScript](http://jashkenas.github.com/coffee-script/) which is a new language that compiles into Javascript. 

While for CSS you have pre-processors being developed that help with the creation and maintenance of stylesheets like [Less](http://lesscss.org/), [Sass](http://sass-lang.com/) and [OO Css](http://oocss.org/)

Lastly an interesting area that growing in popularity is opening a connection between the client (talking the browser here) and server allowing messages to be sent along this connection. [Websockets](http://websocket.org/) and [socket.io](http://socket.io/) appear to be the most interesting in this area at this point.

So loads of new cool technologies to wrap my head around and learn about. Hopefully implement them in a project soon to get a real feel about them. My stack is starting to expand and that is a great feeling as it makes it a lot more robust and scalable. I'm also able to handle and apply better and proper tools to the required solution/application.
