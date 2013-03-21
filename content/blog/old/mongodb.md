Title: mongoDB
Date: 2011-09-02
Tags: mongodb
Slug: mongodb
Author: Greg Reinbach

At CashStar we have make use of MySQL, and for a number of our applications we have some sort of configuration method/system. Sadly due to the rapid development we have been doing, these various applications each have their own method/system of implementing configuration options for the application.

Lately I have been thinking of various ways to have a central configuration system for all our applications. A couple of the developers are working on a configuration service and are mainly looking at solving the requirements of the buy system first. They are going with the default key/value relationship and shouldn't have much of an issue with that. This is an improvement to what the buy system had before, which did not scale well. But they are sticking with MySQL and I don't think they are even thinking of other db options.

I like the idea of databases like [MongoDB](http://www.mongodb.org/) and how they store the data in a sort of document manner per key. I'm probably describing that badly. But the point being in old relationship terms, is that you can have any fields/columns for each record. So you don't have migration issues when a new field is needing to be added.

The other way you can go and I think the developers are heading this way is to go with a straight key/value relationship, but that does not seem like it will be clean, especially when you go to multiple levels in the key/value relationships. Anyway this is a long way of me saying that I started looking at MongoDB, as I have heard a good amount about it and have always been wanting to try it out and see if it would work as I expected/hoped.

First impressions are good with it in that it was an absolute breeze to setup and get going with it. Granted just been using the javascript terminal to run the usual simple queries and get a feel for it. But man oh man, 

* download
* untar
* create dir (/data/db)
* run mongod

and mongo db instance is running and waiting for connections. Granted this is locally and no replication etc etc happening as yet. Still need to work my way through all that to understand it better. But so far am liking it and thinking this may be a good start.   

Next I want to setup up a simple web application and connect with it and maybe work on a simple configuration type app.
