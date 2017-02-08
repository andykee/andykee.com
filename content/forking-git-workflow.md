Title: The Forking Git Workflow 
Date: 2016-05-10 
Category: 
Tags: git
Summary: 
Slug: forking-git-workflow
Authors: AK
Status: draft

The forking workflow is the way that most open source projects operate. It provides a workflow that allows for developers to contribute to their own server-side repos, and specify which features should be included in the official project repo (via a pull request). 

### 0. Setup
Create the official repository on a server accessible by all team members. Typically, this repository will also serve as the public repo of the project maintainer. Because the official repo is public, it should be created as bare. Create it with:

    :::bash
    ssh user@host
    git init --bare [/path/to/repo.git]

Most repo hosting services also provide a GUI alternative for creating a new repo. It is harder to screw up, so opt for this method when it is available.

With the repo set up on the server, we set up our local version:

    :::bash
    mkdir [project]
    cd [project]
    git init
    git remote add origin [repo-url]
    touch README.md
    git add README.md
    git commit -m "Initial commit"
    git push origin master -u

Because `master` should always be in a *production-ready* state, we'll need a `dev` branch where we can integrate and test new features before they're ready for prime time. Let's make that now:

    :::bash
    git checkout -b dev
    git push origin dev -u

At this porint, developers can fork the repo and start hacking.

### 1. Fork and clone
Before we can start contributing to the project, we need to fork its repository. Forking basically makes a copy of the repository with a link back to the original. Find the official repository on GitHub (or Bitbucket, GitLab, ...) and click **Fork**. That's it!

![Fork!]({filename}/img/github-fork.jpg)

Now we have our own copy of the official repository on the remote server. Make a clone on your local machine:

    :::bash
    git clone [forked-repo-url]

We'll need a pointer back to the official repository so we can keep our repo in sync with the official one. Whereas `origin` points to the forked repo on the remote server, `upstream` will point to the official repository on the remote server. Make it with:

    :::bash
    git remote add upstream [official-repo-url]

### 2. Hack
All development should occur on a branch. A new branch should be created for new features, changes, or bug fixes. Branch naming is straightforward: prepend feature branches with `feature-` and change or fix branches with `fix-`. Before we make a new branch, let's make sure we're starting with the most recent version of the code:

    :::bash
    git checkout dev
    git pull upstream dev

Now we can create a new branch:

    :::bash
    git checkout -b [branch-name]

Hack away on this new branch. Make commits. Break things, then unbreak them. Do whatever needs to be done. Sometime between creating the branch and finishing up development, you'll need to push this branch to your remote:

    :::bash
    git push origin [branch-name]

It's worth noting that when we're pushing our code, we can add the `-u` flag, which will point our local branch to the remote one. This let's us use a shortened version of the push command (simply `git push`), without specifying the repo name or branch name and git will know where to send things. This would be a useful thing to do at this point if you see yourself pushing changes over time to this branch on the server. Otherwise, it's just unnecessary keystrokes. 

### 3. Publish
Once a new feature/fix is done, it's time to present the code to the rest of the team and incorporate it into the official repo. Head back to the browser and navigate to your forked repo. Click on **New pull request** and complete the pull request, identifying `dev` as the ??? branch and your `[branch-name]` branch as the ???..

![Pull request]({filename}/img/github-pull.png)

Once the code checks out, it can be merged into the repository by the project maintainer. If, however, issues are discovered, they will need to be fixed on the branch you created the pull request from. Do this in your own repository:

    :::bash
    git checkout [branch-name]

       (fix things)

    git commit -m "Commit message"
    git push origin [branch-name]

The new commit will be automatically added to the current pull request. Magic!

### 4. Clean
After your code has been incorporated into the official repo, you don't need your branch anymore. Delete it locally by:

    :::bash
    git branch -d [branch-name]

Remove the remote branch:

    :::bash
    git push origin :[branch-name]

Finally, pull down a fresh copy of the offical dev branch (which now includes your new code):

    :::bash
    git pull upstream dev




### Advanced hacking with friends

contributing to other developers forks from x-team document 

