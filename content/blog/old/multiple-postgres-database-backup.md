Title: multiple postgres database backup
Date: 2012-03-07
Tags: postgresql, python
Slug: multiple-postgres-database-backup
Author: Greg Reinbach

I have a number of small databases on a PostgreSQL server, and wanted a simple script to backup these databases and store them locally for each day of the week.

So I created a python script to do the work for me, it will handle any new databases that are added, so I don't have to worry about setting up a backup script each time I create a new database.

You can find the script at [https://gist.github.com/90b45a8259ad0b906554](https://gist.github.com/90b45a8259ad0b906554)

The script makes use of the .pgpass file, so you need to setup a .pgpass file for the user running the script, that stores the access params to psql so that the pg_dump call will work. See [see http://www.postgresql.org/docs/8.4/static/libpq-pgpass.html](see http://www.postgresql.org/docs/8.4/static/libpq-pgpass.html)

The script is something to get started with and will only work with small databases that have low traffic.

Setup up a crontab to run the script.

    0 3 * * * * root /etc/cron.daily/psql_backup.py

Then there is a separate rsync script to pull the database instances off the server to another location/data center.
