Title: Pelican
Date: 2013-03-04
Tags: python
Slug: pelican
Author: Greg Reinbach

Blog changed to use [Pelican](http://docs.getpelican.com) and my thoughts on it.

Well that escalated quickly! I was wanting to update the look and feel of this blog, felt it needed a little touch up.

I had read and heard about various blog systems that were very static, with the relevant files being pre-generated and pushed to the server. The benefit being that this simplified things on the server side, server would be able to handle large loads etc. Also the blog entries could be versioned stored in a repo easily enough.

So it appears things lined up this past week. I ran across a blurb saying that [kernel.org](http://kernel.org) just updated their site to make use of [Pelican](http://docs.getpelican.com), and I decided to take a look at it. Well that quickly turned into me trying out the tutorial, then moving onto the rest of the documentation and working on developing a theme and before I knew it, I had just redone my site.

I created a quick python script to pull my blog entries and generate the relevant markdown files. Luckily my blog makes use of markdown, so that was simple enough.

A quick nginx conf change, which included adding a rewrite rule for old links and voila things are up and running with a new theme etc.

So I'm extremely impressed with [Pelican](http://docs.getpelican.com), they have done a fantastic job and it's very easy to use. The packaged commands with it make it a breeze doing the various tasks you need to do. I really like making use of my normal editor (Emacs) to write articles and the bonus is that the articles are now stored in the repo as well.
