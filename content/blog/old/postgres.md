Title: Postgres
Date: 2006-03-15
Tags: postgresql
Slug: postgres
Author: Greg Reinbach

Well I took it upon myself to have a look at Postgres (<a href="http://www.postgres.com">www.postgres.com</a>) . So I set up postgres on my dev box and played around with it a bit. It definitely has a few more features than MySQL and is a lot more concerned about rights and permissions. Some nice features are the sequences for primary keys are automatically setup up/managed by the system and there is no need to manually handle this as in MySQL.

I then decided to see what it would take to port JaG CMS from MySQL to Postgres, and was really impressed with how little it took. I did actually find a couple of little things as well as bug or two in my sql queries. But it really did not take much time at all, less than an hour I would say. Most of it trouble shooting my bugs and working out that Postgres does not like integer statements in the where clause (eg: WHERE 1) but rather that it needs to be a boolean statement (eg: WHERE 1 = 1)

So all in all I was impressed with Postgres and hope that I willmake more use of it in the future.

I realize that MySQL is/has developed a lot of the functionality that Postgres already has, like Stored Procedures, Triggers etc. but I don't think it hurts to know a number of databases really well.
