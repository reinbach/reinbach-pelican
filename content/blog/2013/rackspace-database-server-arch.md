Title: Rackspace Arch Linux Database Server
Date: 2013-05-27
Tags: server
Slug: rackspace-arch-databaseserver
Author: Greg Reinbach

This is how I setup my database servers on Rackspace. I make use of PostgreSQL.

My preferred Linux distro is [Arch Linux](https://www.archlinux.org/), so when setting up the server on [Rackspace](https://www.rackspace.com/) that is the distro I select and the rest of the instructions are applicable to that distro.

Once the server has been created and is up and running, I update the system. See [previous article](|filename|rackspace-server-arch.md) on the steps I take to do that.


Setup PostgreSQL
----------------

    pacman -S postgresql (Y)
    systemd-tmpfiles --create postgresql.conf
    mkdir /var/lib/postgres/data
    chown -c -R postgres:postgres /var/lib/postgres
    su - postgres
    initdb -D '/var/lib/postgres/data'
    systemctl start postgresql
    systemctl enable postgresql

    vi /var/lib/postgres/data/postgresql.conf
    # set listen_address variable
    set listen_addresses = '*'

    # set password for postgres user
    passwd postgres
    su - postgres
    psql -c "alter user postgres with password '<password>'" -d template1

    # setup relevant connection parameters that you want to allow to have access
    vi /var/lib/postgres/data/pg_hba.conf
    # IPv4 local connections:
    host   all   all   <your_desired_ip_address>/32   md5
    # change the local users not be trusted by require a password
    local   all         all    md5

    # restart postgres to pick up changes
    systemctl restart postgresql


Setup backup script
-------------------

I have a simple database backup script that runs daily and makes a backup of each database.

    # need steps to setup backup scripts
    mkdir -p /opt/backup/database
    chown -R postgres:postgres /opt/backup/database/

    # move backup script into place
    mv database_backup.py /etc/cron.daily/
    chmod 700 /etc/cron.daily/database_backup.py

    # update crontabs to run script daily
    # add following to cron
    MAILTO=<email_address>
    0 3 * * * * root /etc/cron.daily/database_backup.py

    # add .pgpass so script can access database
    vi ~/.pgpass
    *:*:*:postgres:<password>

    # set decent permissions for file
    chmod 600 ~/.pgpass

    # install relevant database libraries so script actually works
    pacman -S python-psycopg2
