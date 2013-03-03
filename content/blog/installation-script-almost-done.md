Title: Installation Script almost done
Date: 2006-01-19
Tags: php
Slug: installation-script-almost-done
Author: Greg Reinbach

Been working on the installation script for JaG CMS and am about half way through it, should be another day or two and be able to release the code.

Been interesting in working out how to handle the transistion from no libraries available at the beginning of the installation to a gradual addition of libraries of the code base as parts are set up.

For example have no templating engine available to handle the presentation logic, but after the first step this is available. The step after that will add the db abstraction layer, as the parameters of the db are provided.

So have found that interest in solving. But now that I have the design it is flowing easily together.
