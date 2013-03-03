Title: diptoe
Date: 2011-09-20
Tags: flask
Slug: diptoe
Author: Greg Reinbach

I wanted to have a basic site that can be used to gauge the level of interest in an idea. 

So I created a simple web app called [DipToe](https://github.com/reinbach/diptoe) that accepts and stores email addresses in a flat file. Made use of the [Flask](http://flask.pocoo.org/) framework and in about 70 lines of code, excluding the html and css, have the site complete. It prompts for an email address and stores this in a flat text file. 

There is validation on the email address, which I pulled out of the Django framework. It also very loosely checks whether the user has entered the email address already and doesn't save it again.

The layout of the page has a large "splash" area on the home page and an about page as well. It is easy enough to add more pages if needed.

I made use of the [twitter/bootstrap](https://github.com/twitter/bootstrap) for most of the css.
