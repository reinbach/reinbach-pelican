Title: maintenance page
Date: 2012-03-07
Tags: server
Slug: maintenance-page
Author: Greg Reinbach

I had to move servers for a client and made use of a simple maintenance page to stop data being added to the both the servers as I moved the latest data across.

The servers had a normal apache instance running, without nginx etc. So I made use of .htaccess and a html page to handle this.

I put in place a maintenance.html file on the server that looked like this;

    <html>
    <head>
        <title>Pearl Izumi</title>
        <script type="text/javascript">
        function delayer() {
            window.location = "/";
        }
        </script>
    </head>
    <body style="text-align: center;" onLoad="setTimeout('delayer()', 5000)">
        <h3>Currently in maintenance mode</h3>

        <p>We're making this a better place.</p>
    </body>
    </html>

The javascript is in there to redirect the use back to the home page every 5s to help them keep checking, also to redirect them away from the maintenance.html page. Otherwise when we updated the .htaccess file, and the user tries to reload the site, they may still end up at the maintenance page. Also this does not work well if a user has javascript turned off. So there are a number of things that need to be tweaked to improve this.

The .htaccess file redirects all requests to the maintenance page and is done with the following;

    RewriteEngine On
    RewriteCond %{REQUEST_URI} !/maintenance.html$
    RewriteCond %{REMOTE_HOST} !^67\.255\.207\.160
    RewriteRule $ /maintenance.html [R=307,L]

If you need to open the site up to other IP addresses, you can add extra "REMOTE_HOST" lines with the relevant IP address.
In this instance all requests are sent to the maintenance.html page, so that makes it tricky to add images and styling to your maintenance page. To do that in this case, you would need to link to images/css files off this server at another server.

So that was it. To turn the maintenance page on and off, just un/comment the rewrite rules in the .htaccess page. You probably also want to rename the maintenance page to something else, that is not accessible by the webserver, to prevent people accidentally accessing it.

I now also make use of this maintenance page when doing updates to the site.
