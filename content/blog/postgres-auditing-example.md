Title: postgres auditing example
Date: 2009-01-13
Tags: postgresql
Slug: postgres-auditing-example
Author: Greg Reinbach

A while ago I wrote in general terms about putting together a low level auditing system for postgres, well this post is about one way I went about doing this.

I have written a short article on it that can be found <a href="http://python.reinbach.com/cms/auditing/">here</a>

The auditing steps are implemented in the database layer through functions and triggers making use of PL/SQL, it includes a login function that creates a session table that is used to ensure that the user is logged in and that the auditing function has access to the users information.

