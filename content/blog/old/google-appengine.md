Title: Google AppEngine
Date: 2010-04-12
Tags: python
Slug: google-appengine
Author: Greg Reinbach

Lately I have been playing around with the Google AppEngine, and seeing how that works. 

I really like the idea of the system being placed in Google's Dataservers and leveraging their infrastructure. On top of that the hosting is free if your quotas are low and so only if your site becomes popular or is heavily used do you need to pony up with the cash.

To try out AppEngine I decided to write a simple Critic's website and decided to use the "raw" AppEngine code/infrastructure. You can make use of 3rd party frameworks (eg: Django). The reason for that was just to get a good understanding of the basics and also to try something new.

Well it was simple enough and had some interesting way of doing things. For example when fetching a result set you always have to put in the number of entries you want back. I can see the reason for that, and so had to change the thinking/logic in the code in regards to that.

When creating/setting up an AppEngine application you need to create an app.yaml file that pretty much configures the site, and there are a number of options that are available to you. I really liked this as you are able to quickly and easily require that certain files/paths require authenticated users. You also map the paths to the necessary files in one location. This worked fine in a small application, so not sure how easy it would be to maintain it, if you had a very large application.

I sure have grown use to having all the bells and whistles that comes with using the Django framework, so will definitely be using that in the next applications/projects. It appears that the only part you really cannot make use of is the ORM that comes with Django, as you are using the proprietary storage mechanism that AppEngine is based on. Setting up the models was not that much different from Django.

The parts that I really missed in this application was the urls conf functionality. I like being able to change the url mapping in once place, which can be easily changed at anytime with out having to update the code everywhere. The other part was the handling of posted forms. I have grown lazy.

Well all that I have left to do on this project is to template it and it should be all good to go. A very basic site, but it allowed me to play with the AppEngine functionality and go through the complete cycle.
