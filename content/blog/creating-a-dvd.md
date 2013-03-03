Title: Creating a DVD
Date: 2006-06-17
Tags: general
Slug: creating-a-dvd
Author: Greg Reinbach

This is a shortcut of what I need to do in order to create my dvds. For a superb full explanation on creating dvd's see this resource;
 - <a href='http://forums.gentoo.org/viewtopic-t-117709.html'>http://forums.gentoo.org/viewtopic-t-117709.html</a>

Note: <code>FILENAME</code> - is the name of the dvd you are creating

<strong>Step 1 - Transcode</strong>

Transocde AVI file into dvd friendly format.
<code>
$ transcode -i FILENAME.avi -y ffmpeg --export_prof dvd-ntsc --export_asr 3 -o FILENAME -D0 -b224 -N 0x2000 -s2 -m FILENAME.ac3 -J modfps=clonetype=3 --export_fps 29.97 
</code>

The above script is for a 16:9 aspect ratio, if you need that to be 4:3 aspect ratio then change the following
<code>
--export_asr 3 => --export_asr 2
</code>

This results in 2 files, once for the video and the other for the sound

<strong>Step 2 - Combine</strong>

Need to combine the video and sound file together
<code>
$ mplex -f 8 -o FILENAME_dvd.mpg FILENAME.m2v FILENAME.ac3 
</code>

<strong>Step 3 - Menu</strong>

Create an xml file (this is one without a menu)
<code>
&lt;dvdauthor dest='DVD'&gt;
&nbsp;&nbsp;&nbsp;  &lt;vmgm /&gt;
&nbsp;&nbsp;&nbsp;   &lt;titleset&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     &lt;titles&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       &lt;video widescreen='nopanscan' /&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       &lt;pgc&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         &lt;vob file='FILENAME_dvd.mpg' chapters='0,0:30,1:00,1:30,2:30,3:00,3:30,4:00'/&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       &lt;/pgc&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     &lt;/titles&gt;
&nbsp;&nbsp;&nbsp;   &lt;/titleset&gt;
 &lt;/dvdauthor&gt;
</code>

<strong>Step 4 - Author</strong>

This run the xml file through dvdauthor
<code>
$ dvdauthor -x dvdauthor.xml
</code>

<strong>Step 5 - Burn</strong>

Create DVD image that will be used to burn DVD
<code>
$ growisofs -Z /dev/dvd -dvd-video DVD/
</code>

That is is. Except that I should create some scripts for all this and maybe package it into a simple program
