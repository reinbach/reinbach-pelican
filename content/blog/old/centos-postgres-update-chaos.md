Title: centos postgres update chaos
Date: 2009-06-03
Tags: postgresql, server
Slug: centos-postgres-update-chaos
Author: Greg Reinbach

The other day I updated a centos server and postgres was updated in the process. I rebooted the server for all the new libraries to take effect etc, just to make sure. Well when the server rebooted all my postgres databases disppeared. Postgres started up perfectly, but not one database was there, just the default postgres databases.

That freaked me out, and had me hopping for a while, trying to work out what happened. It all boiled down to the data dir changing locations!

The quick fix was to just copy the old data dir into the new data dir location and restart postgres. All the databases reappeared, much to my relief. It is prudent to stop postgres completely before you move the data dir.
