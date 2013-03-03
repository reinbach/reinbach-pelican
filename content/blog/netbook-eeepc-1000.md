Title: netbook eeepc 1000
Date: 2009-02-26
Tags: general
Slug: netbook-eeepc-1000
Author: Greg Reinbach

Just bought myself a eeepC 1000 linux netbook as I am going to be travelling a bit lately and want to keep working during that time.

I was planning on putting Gentoo onto it, but decided against that as it was suggested that compiling every package will be a bit resource intensive on the netbook so I decided on <a href="http://www.eeebuntu.org/">eeebuntu remix</a>

The reason I decided to install a different Linux distr was to give me more flexibility and the desired environment for me. The default Xandros distro actually looked pretty decent and I could see anyone being able to use this with no problems. The interface was very good and intuitive. But I need to do some development on the machine and needed something more.

Well the only issue I had was booting from the USB Drive in that I kept getting a flashing cursor in the top left corner. The solution was that the USB stick's boot partition needed to be fixed with the command

    lilo -M /dev/sdd

After that it was pretty much plain sailing. The next part I'm working on is getting <a href="http://www.virtualbox.org">virtualbox</a> setup, which is done, but really getting Windows installed within virtualbox and the trick is intalling Windows without a CD Drive.

<strong>Resources:</strong>
<a herf="http://www.debuntu.org/how-to-install-ubuntu-linux-on-usb-bar">Installing Ubuntu on USB Stick</a>
