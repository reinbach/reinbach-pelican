Title: webpy
Date: 2011-08-16
Tags: webpy, python
Slug: webpy
Author: Greg Reinbach

Still on my whirl wind tour of python web frameworks, picking a few that catch my eye and playing around with them. Mainly trying out their tutorials that they have and if it interests me, going ahead and developing an actual web application for them.

The latest one I am playing around with at the moment is [web.py](http://webpy.org/). It appears simple enough, but crikey does it pack a lot. Webpy is capable of handling decent loads (used by reddit.com) and generally you would expect it to be bare bones. But not webpy you get form handling, it almost builds APIs for you out of the box and on top of it all it has a templating engine as well called Templetor. 

Granted the templating is completely different to what I am used to. Mainly used to Django, Jinja2 which are both very similar to each other and Cheetah or ZPL which are XML based structure. You also have the option of using another templating engine and there are simple hooks in place already to make use of Jinja2 and others.

I've just gone through the documentation and it appears that it hits all the necessary points. Obviously using it in a complete web application would give a clearer idea.  

The few things that I see lacking; 

- Is a messaging wrapper, and this is just me being really lazy. It would be simple enough to write as a sessions storage mechanism is available.  

- Is reverse lookup of routes. I am used to other frameworks that allow you to name the url path , and can then use the name instead of "hardcoding" the path in templates or reverse lookup the name to get the actual url path. Makes for easy development, but may not be good philosophically.


I also like that the documentation mainly goes about explaining how to solve issues.
