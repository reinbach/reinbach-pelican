Title: Postgres Auditing
Date: 2008-06-01
Tags: postgresql
Slug: postgres_auditing
Author: Greg Reinbach

Working on a new project called Bayete, it has been long time coming, but that is another story. For this project I wanted to have some low level auditing and so decided to make use of Postgres with it's functions/trigger options. The idea is that when there is any INSERT/UPDATE/DELETE action on a table it is recorded in an auditing table. The idea was inspired by Tony Mays, a work colleague.

PL/PGSQL is the language I used to program these functions and triggers. I was looking at PL/Python but decided on PL/PGSQL as it is more 'embedded' in Postgres and you have access to more information, while with another Language like PL/Python I would need to make more calls.

One gotchas is that one needs to look out for is the NULL value. It can really wreck havoc on your functions/triggers. If you have a NULL value for any var in your statement you're ending up with a NULL result!!

To really make the auditing work well you need to know who is taking the action and for that I required a change in the normal login query, now instead of just checking that the user exists in the database I now create a temporary 'session' table that holds the username of the user and so when an auditing action is invoked this 'session' table is queried for the username, if it does not exist the complete query will fail. Which could be considered another layer of security at the database level, albeit a very very weak layer that is easily circumvented by just manually creating the 'session' table.

The auditing record is tied back to the original record by the table's primary key and this is where one is required to make a slight modification in the table structures so that there is always only one primary key. This just makes things simpler for the auditing record and connecting it back to the record. I have not run into any issues with this at the moment. For those tables that had primary keys made up of more than 1 field, I changed by adding a system primary key to the table and making a constraint requiring the previous primary keys to be unique together.

So the auditing table is made up as follows;
- trx_type: the type of transaction that occurred (INSERT/UPDATE/DELETE)
- trx_table: the table that the transaction occurred in
- trx_key: the primary key of the table/record
- trx_time: time the transaction occurred
- trx_user: the user responsible for the transaction
- trx_desc: an xml string of the values affected

To provide a clear indication of what happened I make up a XML string showing the new/old values for each of the fields being affected. This allows easy parsing in the future to provide a clear history of the record.

In order to make life easier for me I have created a simple script that generates the function/trigger. I just pass in the table name and the primary key and it queries the database for the table information and then creates a file that holds the function/trigger. The reason for putting it in the file is that I just need to run the script once to generate the file and then I have another script that regenerates the database for me, making use of all these files that hold the functions/triggers plus a few other files that hold the data structure and default data (I'll post this in another posting). This allows for rapid rebuilding of the database as well as being able to create multiple instances of the database which I do for unit testing purposes. Just make sure not to add a trigger to any type of ids table that is used by the auditing table, otherwise you're in a nasty loop. Yes I did that, and it took me a little while to work out what the heck was going on.

Well that is a simple overview of the auditing that I have implemented. Granted it is still early days for this and it will more than likely go through some growing pains.
