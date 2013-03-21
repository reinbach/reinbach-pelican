Title: Dual Monitor Setup
Date: 2006-06-16
Tags: general
Slug: dual-monitor-setup
Author: Greg Reinbach

At work I have a Sony Vaio [FS950] running Debian and an external 19'' Monitor that I wanted to connect to expand my desktop. Below is an extract from my xorg.conf file with some explanations about the changes.

I used the following resources for help;
 - <a href='http://gentoo-wiki.com/HOWTO_Dual_Monitors'>http://gentoo-wiki.com/HOWTO_Dual_Monitors</a>

So after much tweaking and playing around below is the part of the xorg.conf file that setup the monitors the way I wanted them.

<strong>Laptop</strong>
<code>
--- snip ---

Section 'Device'
&nbsp;&nbsp;&nbsp;      Identifier&nbsp;&nbsp;&nbsp;'video0'
&nbsp;&nbsp;&nbsp;        Driver&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;BusID&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;Screen&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;itorLayout'&nbsp;&nbsp;&nbsp; 'CRT,LFP'
&nbsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;e'&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;Info'&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;ce'&nbsp;&nbsp;&nbsp;'false'
&nbsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;dSection

Section 'Monitor'
&nbsp;&nbsp;&nbsp;Identifier&nbsp;&nbsp;&nbsp;'Laptop Monitor'
&nbsp;&nbsp;&nbsp;Modeline&nbsp;&nbsp;&nbsp;'1280x800@60' 83.91 1280 1312 1624 1656 800 816 824 841
&nbsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;dSection

Section 'Screen'
&nbsp;&nbsp;&nbsp;Identifier&nbsp;&nbsp;&nbsp;'screen0'
&nbsp;&nbsp;&nbsp;Device&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;Monitor&nbsp;&nbsp;&nbsp;Monitor'
&nbsp;&nbsp;&nbsp;DefaultDepth&nbsp;&nbsp;&nbsp;24
&nbsp;&nbsp;&nbsp;SubSection&nbsp;&nbsp;&nbsp; 'Display'
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;'1024x800' '800x600' '640x480'
&nbsp;&nbsp;&nbsp;EndSubSection
EndSection

--- snip ---
</code>

The default xorg.conf file had 'vesa' as the driver and I changed that to i810' (I just had to change the text here to 'i810', and it worked for me)
'Clone' is set to false as I did not want a duplicate copy of the desktop on my external monitor, but rather to extend it.

<strong>External Monitor</strong>
<code>
--- snip ---

Section 'Device'
&nbsp;&nbsp;&nbsp;Identifier&nbsp;&nbsp;&nbsp;'video1'
&nbsp;&nbsp;&nbsp;Driver&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;BusID&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;Screen&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;itorLayout'&nbsp;&nbsp;&nbsp; 'CRT,LFP'
#        Option          'MetaModes' '1600x1200'
EndSection

Section 'Monitor'
&nbsp;&nbsp;&nbsp;Identifier&nbsp;&nbsp;&nbsp;'NEC Monitor'
&nbsp;&nbsp;&nbsp;HorizSync&nbsp;&nbsp;&nbsp;31-81
&nbsp;&nbsp;&nbsp;VertRefresh&nbsp;&nbsp;&nbsp;56-75
&nbsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;dSection

Section 'Screen'
&nbsp;&nbsp;&nbsp;Identifier&nbsp;&nbsp;&nbsp;'screen1'
&nbsp;&nbsp;&nbsp;Device&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;Monitor&nbsp;&nbsp;&nbsp;EC Monitor'
&nbsp;&nbsp;&nbsp;DefaultDepth&nbsp;&nbsp;&nbsp;24
&nbsp;&nbsp;&nbsp;SubSection&nbsp;&nbsp;&nbsp; 'Display'
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                Viewport&nbsp;&nbsp;&nbsp;        0 0
&nbsp;&nbsp;&nbsp;EndSubSection
EndSection

--- snip ---
</code>

Here I added the external monitor's settings. You ned to know/determine the HorizSync and VertRefresh that is specific to your monitor, a quick way is to boot up a Gnoppix CD and see what it sets for your monitor or look at the specs for the external monitor.

For the external monitor I needed to make sure that the 'DefaultDepth' value had a matching 'SubSection' with a 'Depth' that matched it.

Once I had everything setup I ran into the issue that the external monitor's desktop would scroll, so that it appeared that I had this really large desktop but only a portion of it would show on the monitor and moving the mouse to the edge of the monitor would result in the desktop scrolling in that direction. I did not like that and so that is what the 'Viewport 0 0' line does it. it stops the scrolling.

<strong>Monitor Layout</strong>
<code>
--- snip ---

Section 'ServerFlags'
&nbsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;'Xinerama'&nbsp;&nbsp;&nbsp;'on'
&nbsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;'RandR'&nbsp;&nbsp;&nbsp;'on'
EndSection

Section 'ServerLayout'
&nbsp;&nbsp;&nbsp;Identifier&nbsp;&nbsp;&nbsp;'Default Layout'
&nbsp;&nbsp;&nbsp;Screen&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;'screen0' 0 0
&nbsp;&nbsp;&nbsp;Screen&nbsp;&nbsp;&nbsp;bsp;&nbsp;&nbsp;'screen1' RightOf 'screen0'
&nbsp;&nbsp;&nbsp;InputDevice&nbsp;&nbsp;&nbsp;'Generic Keyboard'
&nbsp;&nbsp;&nbsp;InputDevice&nbsp;&nbsp;&nbsp;'Configured Mouse'
&nbsp;&nbsp;&nbsp;InputDevice&nbsp;&nbsp;&nbsp;'Synaptics Touchpad'
&nbsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;erama''on'
EndSection

--- snip ---
</code>

The last section pretty much determines how the monitors play together. So that is it, with these settings for the monitors in your xorg.conf file you should be all set with dual monitors.
