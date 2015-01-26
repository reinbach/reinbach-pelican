Title: Block SSH attacks
Date: 2014-03-01
Tags: server
Slug: iptables
Author: Greg Reinbach

Periodically one of my servers gets hit by SSH brute force attacks, and I finally got tired of manually dealing with it.

Previously I would go through the following flow;

- Get a notification that my server load was increasing
- Log into the sever
- Check/confirm that it was the usual issue, by looking at the logs
- Check where the offending IP address is originating from.
- Add an iptables rule to block the offending IP address `iptables -I INPUT -s <OFFENDING_IP> -j DROP`
- Watch as the load returned to normal

So after a little research, with the goal of not wanting anything fancy or crazy to install and/or setup. I decided to go with a few more iptable rules to try and mitigate the issue, as per [Rainer Wichmann](http://la-samhna.de/library/brutessh.html#3). It is an old posting, but looks exactly like the kind of rules I'm looking for;

    iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set \
    --name SSH -j ACCEPT
    iptables -A INPUT -p tcp --dport 22 -m recent --update --seconds 60 --hitcount 4 \
    --rttl --name SSH -j LOG --log-prefix "SSH_brute_force "
    iptables -A INPUT -p tcp --dport 22 -m recent --update --seconds 60 --hitcount 4 \
    --rttl --name SSH -j DROP

There is also a whitelisting option, but seeing that I have a dynamic IP address, I didn't see that as being exactly helpful.