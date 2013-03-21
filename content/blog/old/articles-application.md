Title: articles application
Date: 2009-01-16
Tags: python
Slug: articles-application
Author: Greg Reinbach

This blog system was not working out well for me, especially for those long ramblings of mine, so I have created an <a href="http://python.reinbach.com/cms/">articles app</a> in django and now I can ramble on forever.

I wanted something that would be able to display code snippets more intuitively and effectively. The article app includes an extra field for the html content that takes the text/body of the article and converts it into an html structure.

The conversion process makes use of <a href="http://daringfireball.net/projects/markdown/">markdown</a> and <a href="http://www.freewisdom.org/projects/python-markdown/CodeHilite">codehilite</a> and the processing is done on the server side of things and only has to be done when I add/update the article, instead of at the client side each and everytime the article is viewed.
