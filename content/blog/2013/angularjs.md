Title: AngularJS
Date: 2013-01-20
Tags: javascript
Slug: angularjs
Author: Greg Reinbach

A while back at work I started using backbone.js for the UI part of the project. It was interesting and sadly I did not spend much time on the project before being pulled off to work on other tasks.

This week I wanted to get back to working on JS frameworks/application as I need one for my [Finance App](http://www.reinbach.com/blog/finance-app). For the browser UI application portion of the app, I wanted to make a purely JS application and I decided to try out [AngularJS](http://angularjs.org/) after reading some good things about it.

I've since gone through their [Tutorial](http://docs.angularjs.org/tutorial) and was introduced to [Testacular](http://vojtajina.github.com/testacular/) for running unit tests and [Jasmine](http://pivotal.github.com/jasmine/) for the end 2 end testing. In the past I've not done much in the way of testing for JS code and these look fantastic, and hopefully I will get a lot better with testing JS code. I plan to do a lot for this application.

At the moment, I've cloned the [angular-seed](https://github.com/angular/angular-seed) project and starting to setup my application, while I work my way through the [Guide](http://docs.angularjs.org/guide). The examples and the testing make use of node.js, which is fine for unit testing. But my production servers make use of nginx and uWSGI for the webserver, so I'm needing to sort out that aspect of things before progressing too much.

