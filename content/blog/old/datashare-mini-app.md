Title: datashare mini app
Date: 2012-04-09
Tags: flask, gevent, javascript, python
Slug: datashare-mini-app
Author: Greg Reinbach

Playing around with gevent and "real time" updating of the data between browsers viewing/working on the same data.

So I created a mini app that pushes updates/additions to data in the browser to all users viewing that data.

[https://github.com/reinbach/datashare](https://github.com/reinbach/datashare)

In this mini app the data in the browser is a table with each cell being editable and with the ability to add a new line to the table. As changes are made in each of these cells or a row is added, any of the users viewing this data will see these changes in their browser instantly.

