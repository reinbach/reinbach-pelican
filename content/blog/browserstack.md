Title: browserstack
Date: 2011-10-09
Tags: css, design, html
Slug: browserstack
Author: Greg Reinbach

Being a web developer I am constantly needing to test/debug web applications against the various browsers and I have always found the IE family to be a pain. Ignoring the non-standard issues of these browsers etc. My main issue is having to load up Windows to be able to get to them, this has usually required me having virtual environments running or having dual booting machines. On top the extra steps etc to get Windows up and running there is also the requirement of having to have a license for Windows just to test their browsers. 

Today I tried out [BrowserStack](http://www.browserstack.com/). I had to debug a site in IE9, and after a quick signup, I was at the dashboard and able to load up the site in IE9 and troubleshoot my issue. I was given 60min of free time, which is nice, as it allowed me to try out the service and get comfortable with it.

The neat thing about BrowserStack is that they provide a number of debug tools, eg: Firebug Lite, in the browser that they start up. You don't have to install these, all you have to worry about is the issue you are dealing with.

A couple of caveats came up;


* I tried to do Local Testing and that crashed on me. It makes use of a Java applet and that is what appeared to crash on me. I was running Chrome for this and did not try other browsers, as I just moved to a URL that was accessible outside of my dev environment. A troubleshooting ticket was automatically sent to them, so hopefully that will get sorted out.

* There is a little latency when using the service, but with what is actually happening that is expected. It was not horrendous and I was still able to be productive. Not something I would like to spend a lot of time in, but fine for troubleshooting and quick testing.


So overall I'm happy with the service, makes me excited to think that I can blow away my VM Window instances and no longer have to worry about dual booting etc.

*[update 2/23/2012]* After using this service some more, I've run into issues with it being very slow and painful to use at times. I was not as productive as it was initially. So I'm heading back to the good 'ol VMs.
