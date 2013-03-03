Title: kid vm
Date: 2011-04-14
Tags: appengine
Slug: kid-vm
Author: Greg Reinbach

Just pushed out a new appengine application. I needed a way to track the kids allowances as I never have cash on me. So I put together [Kid VM](http://kidvm-app.appspot.com), which allows you to;


- add kids
- add allowances for the kids
- add transactions


The system will automatically track/calculate the balance. A cron runs daily and creates a transaction for those allowances that are due that day.

Still a little rough, need to add some pretty graphs and clean up the app in a general sense. But it is working and now I can track the kids allowances.

I made use of tipfy for the framework and did a bunch of unit testing on the models. Very happy with the framework and will continue using it for appengine applications. 
