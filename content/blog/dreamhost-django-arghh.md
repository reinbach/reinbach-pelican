Title: dreamhost django arghh
Date: 2009-01-03
Tags: server
Slug: dreamhost-django-arghh
Author: Greg Reinbach

Something that you learn the hard way and that makes you feel powerless is when you make use of a hosting provider and give up certain controls of the server.

The issue I just ran into was with me making a tweak on a django installation and modified the urls.py file, but in doing so I mispelt a module it needed to import, and alas the site is currently failing to import this module now and errors out. Well the problem is correcting that mistake is easy enough, but the web server is not re-reading that file until after a certain number of requests on the site.

Normally if you have control of the web server you can reload/restart it, but here I have to let it run its course and with time and enough requests it will correct itself.

Anyway it is back to normal now, so no need to worry anymore. Just have to be more careful in future. 

Normally this would not be an issue as the dev environment would match the production environment and these issues would be sorted out in the dev region where you have absolute control and then the release process would minimize the human element as much as possible and this sort of error would not occur.

At the moment I make use of mod_python in the dev environment and have all requests re-reading the files. While on the pyton.reinbach.com site I am making use of Fast CGI and a slightly different setup.
