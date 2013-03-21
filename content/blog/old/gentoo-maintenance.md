Title: Gentoo Maintenance
Date: 2006-07-27
Tags: gentoo
Slug: gentoo-maintenance
Author: Greg Reinbach

I'm running Gentoo boxes and the following commands help to keep the packages in order and clean.

I have added the following cron to my crontab to perform a sync on a regular basis so that I keep up to date.
<code>
# sync gentoo updates
# min[0-59] hour[0-23] day-of-month[1-31] month[1-12] day-of-week[0-6]
15 3 * * 1,3,5  root    emerge --sync
</code>

This cron will run Monday, Wednesday and Friday at 3:15am. This saves me having to perform a sync manually.

Then I can perform an update when ever I want to knowing that the portage list is pretty much up to date, with out having to wait for a sync to happen.
<code>
# emerge world -uva
</code>

The '-va' options displays in verbose fashion all the USE flags that will be used for each package as well as prompting you to perform this emerge or not.

Then periodically I run the following commands to keep the system clean.
<code>
# emerge --update --deep --newuse world -va
# emerge --depclean
# revdep-rebuild
</code>

See the <a href='http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?part=2&chap=1'>Portage Introduction</a> doc for complete information on portage.

Or for all <a href='http://www.gentoo.org/doc/en/index.xml'>Gentoo Docs</a>


