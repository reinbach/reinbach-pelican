Title: rhel to centos
Date: 2008-06-15
Tags: server
Slug: rhel-to-centos
Author: Greg Reinbach

A project I am currently working on requires me moving a website between servers. The client has just purchased a new server from Dell with RHEL5 installed on it. Everything was going well till I needed to install a file, but alas we were not able to mount the CDRom drive anymore, and we do not have an RHN subscription. I am doing this all remotely and not into having to pay for a subscription to get updates etc. I decided to move from RHEL to CentOS and these are the steps I took.

It actually was not hard at all, just had to do a little googling and everything panned out for me. So below are the steps I took.

<strong>Step 1:</strong>
remove dependency on RHN for updates/upgrades etc. To make use of these repos you need a subscription and I am just not into that.
<code>
rpm -e yum-rhn-plugin
rpm -e redhat-release-notes-5Server redhat-release-5Server --nodeps
</code>

<strong>Step 2:</strong>
get the centos release and notes rpms that get things going for you in moving from RHEL to CentOS. You need to know what platform you are running on 32bit or 64bit

A quick command to find that information out is;
<code>uname -a</code>

<strong>i386 (32bit)</strong>
<code>
wget http://mirror.centos.org/centos-5/5/os/i386/CentOS/centos-release-5-1.0.el5.centos.1.i386.rpm
wget http://mirror.centos.org/centos-5/5/os/i386/CentOS/centos-release-notes-5.1.0-2.i386.rpm
</code>

<strong>x86_64 (64bit)</strong>
<code>
wget http://mirror.centos.org/centos-5/5/os/x86_64/CentOS/centos-release-5-1.0.el5.centos.1.x86_64.rpm
wget http://mirror.centos.org/centos-5/5/os/x86_64/CentOS/centos-release-notes-5.1.0-2.x86_64.rpm
</code>

<strong>Step 3:</strong>
run the rpms, this will setup your system to make use of CentOS and actually updates you repos list (/etc/yum.repos.d/)
<code>
rpm -Uvh centos-release*.rpm --test
rpm -Uvh centos-release*.rpm
</code>

run the test first to make sure you do not have any dependencies, if you did you will need to get hold those files to fulfill the dependencies. I did not have any issues so I just continued. Good luck if you did have dependency issues : )

<strong>Step 4: (optional)</strong>
update the name of the system. The previous command will result in this file being updated, it really is up to you. I went and changed mine back to 'RedHat Enterprises Linux Server release 5 (Tikanga)'
<code>nano /etc/issue</code>

<strong>Step 5:</strong>
lastly I went ahead and did an upgrade:
<code>yum upgrade</code>

That resulted in 334 packages needed to be downloaded and installed. After that was complete, everything worked fine for me and I was able to install the necessary files that I wanted without any issues. Thank goodness. Now I do not have to worry about mounting the CDRom and I have no problems using yum accessing open repos.

<strong>Resources:</strong>
- <a href='http://jyrxs.blogspot.com/2008/02/using-centos-5-repos-in-rhel5-server.html'>http://jyrxs.blogspot.com/2008/02/using-centos-5-repos-in-rhel5-server.html</a>
