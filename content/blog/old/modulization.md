Title: Modulization!
Date: 2006-02-06
Tags: design
Slug: modulization
Author: Greg Reinbach

Sweet, looks like I have finally worked out a way, that I am happy with, to modularize.

Been working on JaG CMS of late and have a nice code base there from which to start most projects. So spent the last week working out the best way to extend this code base, and ideally that would be through modules.

I had a couple of requirements for the modules that I wanted to achieve, which were;

1. minimal impact on the code base. meaning I did not want to have to update the code base whenever a module was installed. The code base needed to exist as it was. I didn't mind making changes to the code base to handle modules, but that was to be a change for modules as a whole to make use of the code base.

2. 1 location of module files. This would lead to easy management and maintenance of each module

So spent the week creating a catalog module and have most of that achieved with the requirements above. Just need to complete the coding of the module, which should not take much longer, but the module code is sitting in a separate directory from the code base, and is interacting with the code base as needed.

Will be spending this week completing it and then creating some sort of managment interface to modules. After that I will be working on plugins, how to create those and have them interact with the code base.
