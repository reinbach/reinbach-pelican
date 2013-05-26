Title: Rackspace Arch Linux Server
Date: 2013-05-26
Tags: server
Slug: rackspace-arch-server
Author: Greg Reinbach

This is how I setup my servers on Rackspace. My preferred Linux distro is [Arch Linux](https://www.archlinux.org/), so when setting up the server on [Rackspace](https://www.rackspace.com/) that is the distro I select and the rest of the instructions are applicable to that distro.

Once the server has been created and is up and running. These are the steps I go through to get the base system in place.

update system
-------------

    pacman -Syu

convert to systemd
------------------

Currently Arch Linux still makes use of rc.d for running it's daemons, but is in the process of changing to systemd. So we are going to move to systemd now, which should make things easier in the long run. Make use of the [systemd installation instructions](https://wiki.archlinux.org/index.php/Systemd) to do this;

    pacman -S systemd

Edit your grub boot file and have the system boot into using systemd. Add the following snippet `init=/usr/lib/systemd/systemd` to the end of the `kernel` line, so it looks like `kernel /boot/vmlinuz-linux root=/dev/xvda1 ro console=hvc0 init=/usr/lib/systemd/systemd`. Then reboot the system.

    vi /boot/grub/menu.lst
    # update kernel line
    reboot

After system has rebooted, you can confirm that systemd is running with the following;

    car /proc/1/comm

Which should return the string `systemd`

Now we want to convert the relevant process to systemd;

    systemctl enable sshd
    systemctl enable syslog-ng

The final steps are to set the hostname and to clean up old packages and reset grub boot file;

    hostnamectl set-hostname <your_hostname>
    pacman -R sysvinit
    pacman -S systemd-sysvcompat
    vi /boot/grub/menu.lst
    # reset kernel line
    reboot

Once this is complete we now have a base system that we can save a server image of and then use this server image to create other servers from. We can now create Webservers or Database servers from this base server.

If you make use of Nagios/Icinga to monitor your servers, you can then [setup NRPE on the remote servers](|filename|nagios-nrpe-arch-linux.md).