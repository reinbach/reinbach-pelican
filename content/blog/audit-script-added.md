Title: audit script added
Date: 2009-01-26
Tags: postgresql
Slug: audit-script-added
Author: Greg Reinbach

I just updated the auditing article, with a python script that generates the necessary function and trigger to work with the <a href="http://python.reinbach.com/cms/auditing/">Postgres auditing example</a>. 

Not only does this help mimimize the mistakes I make, but it definitely makes life a lot easier just running the script whenever a change is made to a table that needs auditing. So that is a win win.

The idea would be to create a number of other scripts that allows the database to be re-created competely, this is for development purposes and allows for changes to the database to happen rapidly and with minimal mistakes. But that is for another posting.

