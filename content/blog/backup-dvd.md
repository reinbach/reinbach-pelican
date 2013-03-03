Title: Backup DVD
Date: 2006-07-05
Tags: general
Slug: backup-dvd
Author: Greg Reinbach

A great resource on backing up a DVD can be found at
<a href='http://gentoo-wiki.com/HOWTO_Backup_a_DVD'>http://gentoo-wiki.com/HOWTO_Backup_a_DVD</a>

The rest of this page is the steps I take to backup a DVD. At the moment there are a couple of types of DVDs out there which range in size the normal DVD is about 4.7Gig and I believe this is a single layer DVD and then there is the double layer DVD which provides you with about 8Gigs of space. So if you are backing up a DVD make sure you have DVDs that can hold the DVD you are going to backup.

<strong>Step 1 - Copy DVD</strong>
<code>
$ vobcopy -m
</code>

This copies the DVD onto your sytstem and creates a dir with the name of the DVD all in ippercase. So make sure you run this command from the dir you want the backup dir to be placed in.

<strong>Step 2 - Create Image</strong>
<code>
$ mkisofs -dvd-video -o dvd.img DVD_DIR/
</code>

DVD_DIR/ is the directory that was created by the previous step.
It's good to perform this step as it helps shrink the file size to be able to fit on the DVD and makes for a faster burn.

<strong>Step 3 - Burn It</strong>
<code>
$ growisofs -dvd-compat -Z /dev/dvdrw=dvd.img
</code>

And that should be it, with you now having a nice backup of your DVD
