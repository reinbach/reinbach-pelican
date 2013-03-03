Title: JagVest
Date: 2006-06-28
Tags: design
Slug: jagvest
Author: Greg Reinbach

A tool to help identify good investment properties.

Good investment properties are identified as those that are able to be rented out at a certain rate of return over and above the mortage of the propery in relation to the amount of money invested.

For example;
 - Down Payment $20,000
 - Property Cost $100,000
 - Mortgage $600
 - Rent $800

Rate of return is calculated as follows;
 (Rent - Mortgage) / Down Payment
 (800 - 600) / 20000 = 0.01
 Annualized it would be 12%

Will be using the following source for mortgage calculations as they are very well layout out and explained. <a href='http://www.hughchou.org/calc/formula.html'>http://www.hughchou.org/calc/formula.html</a>

<h2>Functionality</h2>
<ul>
<li>
<strong>Calculations</strong>
Want to be able to run various calculations/scenarios

- mortgage calculations
- future values
</li>

<li>
<strong>Searches</strong>
So the tool is going to need to determine what the going rental rates are in a specific region and then be able to run searches in that region to see if it is able to find properties that may be good investments.

The tool will need to be given a number of critieria in order to be able to run its searches. These criteria are identified as follows;
 - region (zip code(s))
 - desired percent return
 - down payment
 - percent of property cost down payment to equal
</li>

<li>
<strong>Track</strong>
Want to be able to store any properties that are found and track them. Provide the ability to set up various alerts.

A couple of possible alerts;
 - when the property is no longer available 
 - change in price of property
</li>

<li>
<strong>Manage</strong>
If the property is bought want to be able to manage the property, this is down the line and not important right now. Will be added on at a later date
</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>
<strong>Property Source</strong>
Need a source in which to search for properties that are for sale

Best option would be MLS, but need to get access to all the various MLS listings around the country, could be expensive and lots of programming for each one

Another option is to just scrap off realtor. Not all properties are listed here though, but may be able to be used to identify good regions
</li>

<li>
<strong>Rental Source</strong>
Need a source that provides rental information on a specific region
</li>
</ul>
