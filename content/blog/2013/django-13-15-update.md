Title: django 1.3 to 1.5 update
Date: 2013-02-28
Tags: django
Slug: django-13-15-update
Author: Greg Reinbach

Just updated this site from Django 1.3 to 1.5 and hit the following nuances

Generic view changes
---------------------

This has changed a bit, and I was only using it to generate the robots.txt file. So I just moved it to a simple view. So no longer use generic views.

Syndication contrib changes
---------------------------

I just needed to change the import path and tweak the url settings file a bit. Actually a lot simpler now. See the [syndication page](https://docs.djangoproject.com/en/1.5/ref/contrib/syndication/) for more information.

ALLOWED_HOSTS
-------------

Due to potential CSRF issues this setting is now needed in the settings.

    ALLOWED_HOSTS = ['.reinbach.com']

The dot allows any subdomain to work as well.

Admin static files
------------------

The path location changed, it is now. So I just needed to change my nginx.conf file to have the /static/admin path point to the new location, which is;

    django/contrib/admin/static/admin/

That was pretty much all I needed to do, now I'm at the latest and greatest. Granted this site is really basic with not much functionality within it. So no major tweaks needed. But still nice when it is quick and simple to jump up to a new release.
