Title: crap memory issues
Date: 2011-09-06
Tags: server
Slug: crap-memory-issues
Author: Greg Reinbach

Looks like my server is running out of ram... yikes!! I think I am going to move this site to AWS. I have a number of systems running on this server and it is about time I split things up. Also gives me an excuse to make use of AWS.  

So if you have issues or start getting 505 errors. It's due to memory issues!

**[updated]**  It appears there was a conflict in the apache config files dealing with SSL certs. Able to remove these conflicts and things to be a lot stabler of late. The interesting thing is that this is a VPS Server and I am meant to be limited to 512MB or so, but if I run

    free -m
                     total       used       free     shared    buffers     cached
    Mem:           894        416        478          0          0          0
    -/+ buffers/cache:        416        478
    Swap:            0          0          0

It was showing a total of 894 MB and that I still had 150MB free, and whenever it got to that point services were being stopped. It appears that PostgreSQL was the first service to go, meaning this site would go down. So that is something to change in regards to monitoring.
