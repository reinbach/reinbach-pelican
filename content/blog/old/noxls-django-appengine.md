Title: Noxls - Django Appengine
Date: 2011-02-06
Tags: django, appengine
Slug: noxls-django-appengine
Author: Greg Reinbach

Developed a base system/framework that makes use of Django on AppEngine. The system integrates with CheddarGetter for payment gateway. The nice part about the framework is that it is a base for a Saas System. I do not need to worry about getting the base in place each time, I can started on the meat of the Saas system, and not have to redo the base each time.

The base system handles has the following features;

- Ties up with the account/product levels created on CheddarGetter
- Account Management
- Handle Upgrading/Degrading account levels
- News
- Contact
- About
- Plan and Pricing
- Signup

There are a number of features and probably a few bugs that still need to be sorted out. It is a start and hopefully it will grow from here. Currently this base is being used on the [http://www.noxls.com](http://www.noxls.com) site
