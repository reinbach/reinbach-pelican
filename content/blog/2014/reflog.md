Title: Git reflog
Date: 2014-03-15
Tags: general
Slug: reflog
Author: Greg Reinbach

Git reflog just saved my bacon.

Last week my commit message referenced the wrong ticket and in attempting to fix the commit message I accidentally reset our develop branch of the project to the master branch. In short, I wiped out all our changes in the project! A few months of work gone, poof!
Well, Git is a distributed repo system so everyone still had the original correct repo, but to top things off I had also pushed these changes to our our central repo server. Awesome!

Anyway a quick chat with a team mate, who informed me about [reflog in git](http://git-scm.com/docs/git-reflog), I was back to the races. A couple of deletes using reflog I was back to normal and breathing easy again.

    git reflog delete master@{X}

With `X` being the reference number of the entry to remove.

So while `git log` will show you the current logs for the branch, `git reflog` records the updates on the branch tips.

So if you appear to have reset your branch to the beginning of time and you need to get back to the present. `git reflog` may be the tool for you to do that.