Title: Docker VPN
Date: 2014-05-19
Tags: docker
Slug: docker-vpn
Author: Greg Reinbach

Work requires use of VPN, and with making use of containers for development, releases etc. I need to access our repos from within these containers. These are the steps I take to ensure I can connect to resources within the VPN.

When running the docker instance, ensure we have `--privileged` as one of the options otherwise you will end up with the following error;

    TUNSETIFF failed: Operation not permitted

So start your docker container with the following command;

    sudo docker run -i -t --privileged centos bash

This will bring up a CentOS base instance and continuing with a CentOS base, run the following commands to install OpenConnect VPN;

    wget http://mirror-fpt-telecom.fpt.net/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm
    yum install -y epel-release-6-8.noarch.rpm
    yum install -y NetworkManager-openconnect which

You will actually need the `which` command, as this is used in the `/etc/vpnc/vpnc-script` script and appears to not be a requirement of `NetworkManager-openconnect`

To connect via VPN, the usual command;

    openconnect <URL> -u <username>

You should be all set to access your resources via VPN.