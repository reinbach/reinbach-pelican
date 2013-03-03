Title: Fabric nice and soft
Date: 2010-03-14
Tags: python
Slug: fabric-nice-and-soft
Author: Greg Reinbach

Finally I got tired of the way I was doing my releases. Which involved me exporting the relevant release from the versioning system and then copying across the files to their respective places, making sure that I was placing them in the correct place. This was all done manually.

Well after reading a bit about [Fabric](http://fabfile.org), I decided to give it a try and am very ecstatic with it. All you need to do is create a simple fab file and call away.
The [Tutorial](http://docs.fabfile.org/0.9.0/tutorial.html) provided by them is straight forward.

I did end up modifying my sites in order to further simplify the releasing of code. I was using mod_python with Apache and had the media files located in the Web Document directory, but have now implemented WSGI and now the code released is all together and there is no need to keep the media files in a different location.

At the moment things are a lot simpler and it is now really easy to make a release. Further enhancements that I need to do is to add auto testing of the code base and ensure all tests pass, adding checks that code is all checked in. Maybe forcing a push to the main Repo etc.

I also want to add Nginx to the server setup as that is meant to be a much better setup. That will probably be the next step I take in regards to the server.
