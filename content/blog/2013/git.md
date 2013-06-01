Title: Git
Date: 2013-06-01
Tags: general
Slug: git
Author: Greg Reinbach

At my new job we use [Git](http://git-scm.com/) exclusively, while previously I had been using [Mecurial](http://mercurial.selenic.com/). Even though I'd used Git for my projects hosted on Github.com, those are mainly personal projects, which did not require much collaboration with other developers. So the Git add/commit/push commands pretty much sufficed most of the time.

But after a few weeks of using Git extensively at WFP where we make use of the [Git Flow](https://github.com/nvie/gitflow) process, I must say I am really enjoying Git and grasping the branching aspect of things a lot better. I would still not classify myself as a expert of Git by any stretch of the imagination, but I do feel like I have moved past the crawling stage.

As I've mentioned, we make use of Git Flow, so installing that helps things a little. It's not really needed as the Git commands are simple enough, it does help with streamlining/automating a few tasks though.

See [Git Flow installation instructions](https://github.com/nvie/gitflow/wiki/Installation) if you want to make use of it.


General
-------

My daily Git routine generally revolves around the following commands;

    # list of branches
    git branch

    # work on a particular branch
    git checkout <branch>

    # see status of changes
    git status

    # see changes for particular file
    git diff <file>

    # remove changes made to the file
    git checkout <file>

    # add a file to the list of files to be commited
    git add <file>

    # committing changes, -m if I want to add a comment inline with the command
    git commit [-m]

    # when merging, the Git commit message is pretty decent, so add to it, rather than overwriting it
    git merge <branch>

    # pull changes from remote to your branch
    git pull <remote> <branch>

    # push your changes to the remote server
    git push <remote> <branch>

    # delete remote branch, this command is slightly weird. Note colon, that's needed
    git push <remote> :<remote_branch>

    # delete a branch locally
    # -D if there are changes in the branch you don't care about
    git branch -d <branch>

See [Git Documentation](http://git-scm.com/documentation) for more complete information.


Stashing
--------

If I need to "park" my changes so I can do a pull/push or some action that needs the branch(es) to be 'clean', making use of stash is really helpful.

    # show the list of currently stashed items
    git stash list

    # create a stash of the changes in branch
    git stash

    # apply the stashed item to the current branch
    # this applies the stash to the current branch and leaves it in the stash list
    # it applies the first stash item if none provided
    git stash apply [<stash>]

    # if you want to apply the first stash and remove it from the stash list
    git stash pop

    # to remove a stash item from the stash list
    git stash drop [<stash>]

    # to see the stash changes in greater detail
    git stash show -p [<stash>]

See [Git Tools - Stashing](http://git-scm.com/book/en/Git-Tools-Stashing) for more information on stashing.


Branching with Git Flow
-----------------------

Git Flow makes use of the following "types" of branches. Featrure/Release/Hotfix and each of those are handled in the same manner. So you just need to replace the command with the relevant type of branch you are dealing with.

    # start a new branch
    git flow <branch_type> start <name>

    # to merge and remove the branch
    git flow <branch_type> finish <name>

These are the commands I mainly use with Git Flow, there are a bunch of others, but I find the Git commands are simple enough to use. See [Git Flow](https://github.com/nvie/gitflow) for more information of the other commands.


Undo
----

Oops, need to undo a commit

    git reset HEAD~1

See [Git-Reset](http://git-scm.com/docs/git-reset) for detail information on resetting.
