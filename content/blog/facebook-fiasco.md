Title: Facebook Fiasco
Date: 2010-11-29
Tags: general
Slug: facebook-fiasco
Author: Greg Reinbach

At work I had to extend our eGift Card purchasing process to handle Facebook Connect, which was to allow the purchaser to select the recipient of the eGift Card from their list of friends on Facebook and then to deliver the eGift Card to the friend via a Facebook wall posting.

Well the whole exercise was very interesting to say the least. The whole Facebook development framework leaves a lot to be desired. There are a couple of issues that we just could not get around, mainly to do with SSL and Facebook really not handling that environment very well. The support is limited and misleading in places. No need to analyze this to death as it has been done plenty elsewhere by more informed people.

The cherry on the cake for me, was that the day we went live with our updated process, Facebook tanked and was out for a few hours. So that provided some exciting moments there. We now have a system wide kill switch for Facebook, which allows us to turn off any interaction we have with Facebook from the Connect functionality to the Like buttons.

Sadly they are the 800 lb gorilla and you have to work with what they give you. I ended up using a few of their APIs in implementing this all, which included the Javascript API, their new Graph API and the old Rest API. It would just be nice if they really tightened up their APIs.

