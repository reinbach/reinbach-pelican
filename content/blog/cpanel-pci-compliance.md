Title: cPanel and PCI Compliance
Date: 2013-03-11
Tags: server
Slug: cpanel-pci-compliance
Author: Greg Reinbach

These are the steps I went through to lock down a cPanel instance running on CentOS for PCI Compliance.

Lately I have been setting up a number of [cPanel](https://cpanel.net/) instances for a client and that is a pretty straightforward process. cPanel have decent [installation instructions](http://docs.cpanel.net/twiki/bin/view/AllDocumentation/InstallationGuide/WebHome) on how to do this and their script pretty much does most of the work.

One of the cPanel instances required to be PCI compliant and that wasn't as clear compared to the installation instructions. The steps you will need to take to be PCI Compliant will depend on the company running the scan, the website you are scanning and what they identify as issues. In my instance it was SecurityMetrics who ran the scan and I ended up taking the following steps to become PCI Compliant;

__CGI scipts__, especially the guestbook.cgi script was a big no no. The quickest and most effective way to disable these scripts was to make use of an .htaccess file. This only works if you don't want to make use of the guestbook.cgi script.

    # /usr/local/cpanel/cgi-sys/.htaccess
    RewriteEngine On
    RewriteRule ^guestbook.cgi$ [G,L]


__Packages with Security Issues__. OpenSSL and BIND versions failed the CPI scan, but a quick check of the CVE values in the changelog of these packages indicated that the relevant issue had been resolved. <CVE-string> is the CVE value that the PCI scan indicates that is failing. The step works for any package that is marked as having a security hole, if your system is already up to date.

    rpm -q --changelog openssl | grep <CVE-string>
    rpm -q --changelog bind | grep <CVE-string>

If the results show in the changelog that the CVE value has been fixed you can then inform the entity doing the PCI scan.


__Apache Configuration__. In the cPanel interface under Sevice Configuration > Apache Configuration > Global Configuration. There are PCI Recommendations for some of the settings. Follow these recommendations. Don't forget to rebuild the apache configuration and restart it, otherwise the changes will not take effect.


__Firewall__. Finally install [ConfigServer Security & Firewall (CSF)](http://www.configserver.com/cp/csf.html). The installation is pretty straightforward and once that is done, you can config and run tests via the cPanel interface. This resolved most of the issues, once I had installed it and followed most of the suggestions provided when running it's test.


Resources
---------

 * [CGI Script](http://serverfault.com/questions/322489/how-do-i-properly-disable-cgi-scripts-e-g-guestbook-cgi-on-whm)
 * [CVE Checks](http://bobcares.com/blog/?p=911)
 * [PCI Compliance in cPanel](http://www.hosting.com/support/cpanelvps/pci-compliance-in-cpanel)
 * [Moving Towards PCI Compliance with cPanel](http://www.v-nessa.net/2008/04/14/moving-towards-pci-compliance-with-cpanel)
 * [CSF](http://www.configserver.com/cp/csf.html)
