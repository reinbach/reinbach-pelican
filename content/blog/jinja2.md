Title: Jinja2
Date: 2011-08-12
Tags: jinja2, python
Slug: jinja2
Author: Greg Reinbach

[Jinja2](http://jinja.pocoo.org/) is now my template engine of choice. I have been using django templates with django for a couple of years now and am very comfortable with them, but have been missing a few things with it more and more. Just not powerful enough. Well missing somethings that would be cool and helpful. 

Jinja2 has solved some of these issues for me. Definitely have not had the chance to use it as much as I would like. Still on Django templates at CashStar, but everything else I am now using Jinja2. Slowly prepping CashStar to move to Jinja2. Probably the main issues in that it would probably be the most time consuming part of the transition is the use of '-' within blocknames.

    {% block page-js %}

works fine in Django, but is an issue in Jinja2, so have slowly been updating our templates to make use of '_' rather.

A couple of the neat and helpful features in Jinja2 is being able to set a variable in the child template, which is then available in the parent template. The template you are extending. Actually there are quite a few neat things, besides the more powerful features of it. Best thing is to have a look at their [documentation](http://jinja.pocoo.org/docs/)


