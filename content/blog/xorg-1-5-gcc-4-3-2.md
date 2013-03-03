Title: Xorg 1.5/gcc 4.3.2
Date: 2009-04-06
Tags: gentoo
Slug: xorg-1-5-gcc-4-3-2
Author: Greg Reinbach

Gentoo is the distribution I use for my desktop and I just performed an extensive upgrade/update this weekend which had me moving to gcc 4.3.2. That required me to do a system and world reinstall and that involves a number of packages (system: 120, world: +/-798)

Each morning I do a world update on my system and I did not notice a few critical updates and I ended up with my apps not starting up cause they could not link to libstdc++.so.6. After a bit of searching I realized that I had actually upgraded gcc to 4.3.2 and this required that I do the system/world reinstall after setting up my current gcc version.

Well after the reinstall, which ran overnight, I re-synced and did my usual world upgrade/update and upgraded to xorg 1.5 which is a major change from the norm. Did I read the instructions completely, nope, I just went ahead and did the upgrade and low and behold my window manager was not fully operational to put it mildly. Anyway I went back to the instructions, which required that I update my INPUT_DEVICES and reinstall xorg server. I must say I was very thankful afterwards that I was required to run the eselect news command before the system would allow an update as that pointed me to the instructions.

Now me and my machine are happy campers.
