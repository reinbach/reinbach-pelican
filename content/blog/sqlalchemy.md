Title: sqlalchemy
Date: 2011-09-26
Tags: sqlalchemy
Slug: sqlalchemy
Author: Greg Reinbach

Working on a web application using the Flask and so made use of [SQLAlchemy](http://www.sqlalchemy.org/) for the database abstraction layer on a PostgreSQL database instance.

My first impressions is that this is very sweet. I am very used to the ORM in Django and have hit a number of limitations with the way it works. I have not enjoyed having to jump Q object to start making use of AND and OR statements. Also the Aggregate and Annotate options are a bit quirky. The Django ORM does the basics and it does it well. But as you need to do more and more complex queries you start to run into limitations, and things start to feel like there is a fair amount of patching.

I've just finished the guide on SQLAlchemy and it appears to provide a very well rounded database abstraction layer. So am very keen to get using it in my project.

Obviously in both options you can always resort to raw sql, but then that kinda defeats the purpose of making use of an ORM. And yes you can insert SQLAlchemy into Django if you like, but I already prefer Jinja2 and pulling up the Django ORM, then there is a lot of patching happening on a framework from the get go and that is not always a good thing.
