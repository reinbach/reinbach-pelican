Title: code base
Date: 2008-06-09
Tags: design, mysql, php
Slug: code-base
Author: Greg Reinbach

Whenever I start a new project I generally make use of a base set of code. This code base has been growing slowly, ever so slowly, but I think it is a reasonable starting base. Nothing fancy, nice and simple and allows me to go in any direction I like.

When I have finished a project or have time during a project, I try to remember to move any improvements back into the base, I really ought to do this more often, but alas. The improvements are limited to the functionality that the base has, I do not want to have a bloated base to start with, I much prefer a very simple clean code base to start with and prefer to add rather than take away.

Currently the base has the following;
- MVC Framework
- DB Abstracted Layer
- User management
- Content
- Test Scripts

I am quite tempted to remove the Content piece, but so far it has managed to survive where it is at the moment.

Currently the DB Abstracted layer is MySQL specific, but I have been working on a side project that makes use of PostgreSQL heavily and I have extended this layer to handle both DB Sources. Something I need to move back into the base.

The Test Scripts are individual unit tests run through PHPUnit and test individual functionality, I need to get together a Test Suite that runs the whole bang shoot together.

So at the moment, this is just a blog entry to get things moving along. But plan to create a space here to better share my code and scripts.

Finally the code base can be found at <a href='http://www.reinbach.com/code.tgz'>http://www.reinbach.com/code.tgz</a> any feedback would be interesting.


