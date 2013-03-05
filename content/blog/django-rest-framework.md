Title: Django REST Framework
Date: 2013-03-05
Tags: django, python
Slug: django-rest-framework
Author: Greg Reinbach

A look at [Django REST Framework](http://django-rest-framework.org/) for developing nice RESTful Web APIs.

We are very much a Django shop at the company I work at and have moved to a Service Orientated Architecture (SOA). Well there are some legacy applications that are in the process of being moved into this sort of artchiture. A number of libraries have been used to help with the various APIs developed, these have mainly been [Piston](https://bitbucket.org/jespern/django-piston/wiki/Home) and [TastyPie]().

There are great [discussions and comparisons](http://stackoverflow.com/questions/8430579/django-restful-api-django-piston-vs-django-tastypie) out on the Tubes about these various libraries. But I must say version 2 of [Django REST Framework](http://django-rest-framework.org/) is looking great.

Django REST Framework feels like it handles a lot more possibilities, that you are not limited or forced down a particular path. You have the Serialization shim, but other than that you can structure your WEB Api code the way that most suites you.

You can make use of functional or class views, but if you have a general model and setup and no need to get fancy there are the relevant helper classes that do that necessary magic for you. Actually it appears there are helper functions/classes at all levels no matter which direction you can with structuring your WEB Api. There are even mixins you can make use of if you make use of classes for your views and want a little help with some functionality.

Their [tutorial](http://django-rest-framework.org/tutorial/1-serialization.html) is great and covers all these areas. The added bonus of this library is the Web Interface that pops up, it really helps with creating data and interacting with the WEB Api a lot simpler.