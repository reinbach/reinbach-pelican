Title: icinga
Date: 2012-02-24
Tags: server
Slug: icinga
Author: Greg Reinbach

It was about time I put together some monitoring system for the  servers I have running on rackspace. I decided to make use of [Icinga](https://www.icinga.org/), which is a fork of [Nagios](http://www.nagios.org/) and meant to be more actively developed. The web interface looks a lot nicer and it makes use of all the nagios plugins.

I followed the [quickstart guide](http://docs.icinga.org/latest/en/quickstart.html).

I have a server outside of rackspace and decided to make use of that to monitor the rackspace servers, sadly though this server runs CentOS and did not have the latest versions of PCRE (> 7.6) version  available in order to run the new web interface available for Icinga, so had to resort back to the classic interface.

Seeing that I was monitoring a couple of remote servers and hopefully the number of them will grow over time, I decided to make use of [Nagios NRPE plugin](http://exchange.nagios.org/directory/Addons/Monitoring-Agents/NRPE--2D-Nagios-Remote-Plugin-Executor/details) for the remote monitoring. This is meant to be a less resource intensive manner in monitoring although a little less secure than using SSH.

This required setting up the Nagios nrpe plugin on the remote servers as well as the [Nagios plugins](http://nagiosplugins.org/). I made use of both the nagios setup and the [Icinga NRPE](http://docs.icinga.org/latest/en/nrpe.html) instructions for the remote servers. The extra step was to create a user/group for nagios, otherwise the make install would not work.

When making changes to your configuration, it's a good idea to run one of the following before reloading or restarting the Icinga daemon;

    /usr/local/icinga/bin/icinga -v /usr/local/icinga/etc/icinga.cfg  
    /etc/init.d/icinga checkconfig
    /etc/init.d/icinga show-errors



