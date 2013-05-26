Title: Nagios NRPE on Arch Linux
Date: 2013-05-26
Tags: server
Slug: nagios-nrpe-arch-linux
Author: Greg Reinbach

Lately I have been setting up a number of servers running Arch Linux and have wanted to monitor them from a central Nagios/Icinga server and these are the steps I take to set these servers up as remote servers that Nagios/Icinga can check via NRPE.

Thankfully things have gotten a lot simpler overtime and there are decent AUR packages that one can make use of. I've already converted these servers to be making use of systemd. See [previous article on setting up a base server using systemd](|filename|rackspace-server-arch.md)

On the remote servers do the following;

    # required libs
    pacman -S base-devel openssl

    # Nagios NRPE
    cd /opt/
    wget  https://aur.archlinux.org/packages/na/nagios-nrpe/nagios-nrpe.tar.gz
    tar -zxvf nagios-nrpe.tar.gz
    cd nagios-nrpe
    makepkg --asroot
    pacman -U nagios-nrpe-*.pkg.tar.xz
    systemctl enable nrpe
    systemctl start nrpe

    # Nagios Plugins
    cd /opt/
    wget https://aur.archlinux.org/packages/na/nagios-plugins/nagios-plugins.tar.gz
    tar -zxvf nagios-plugins.tar.gz
    cd nagios-plugins
    pacman -S net-snmp
    makepkg --asroot
    pacman -U nagios-plugins-*.pkg.tar.xz


Lastly the NRPE config file needs to be tweaked, to allow requests from the Nagios/Icinga central server, update the location of the conf.d file, and to uncomment the commands you want to allow;

    vi /etc/nrpe/nrpe.cfg

    # set allowed_hosts to nagios server's IP (72.47.237.156)
    allowed_hosts=<ip_address_of_nagios_server>

    # update include_dir to absolute path for conf.d dir
    include_dir=/etc/nrpe/conf.d/

    # uncomment the commands you want to allow being called

    # restart nrpe daemon to pick up changes
    systemctl restart nrpe

NOTE: With this setup the NRPE is configured to not accept parameters on the requests. So you cannot make use of `$ARG1$` etc in your commands. This is for security purposes. So you have to hardcode the relevant commands in the NRPE config file, or tweak the config file to allow parameters to be accepted.

You should now be all set to define the relevant services on the Nagios/Icinga server to check the remote server.