Title: Setting up OSX for Python Development 
Date: 2015-12-15 10:30
Modified: 2015-12-15 11:00
Category: dev
Tags: python, osx
Summary: This is how I set up my Python development environment on OSX.
Slug: setting-up-osx-for-python-development
Authors: AK


This is how I set up my Python development environment on OSX. I had a few goals in mind that led me to this configuration:

* Support development using both Python 2 and Python 3
* Manage Python projects with virtualenvs
* Easily switch between projects and their respective (Python 2 and 3) environments

Previously I had been doing all of my development in Python 3 with virtualenv/virtualenvwrapper and had created aliases to redefine `python=python3` and `pip=pip3`. This worked great for a while, but I inevitably ran in to some Python 2 dependencies and knew I needed a more robust solution for managing development in both Python 2 and 3.

The community seems to like managing multiple versions of Python with [pyenv](https://github.com/yyuu/pyenv) and then using [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv) to manage virtualenvs. I really liked pyenv, but couldn't get pyenv-virtualenv to work for me. Coming from virtualenvwrapper it was very clunky and had some frustrating bugs. 

Instead, I arrived at a solution that uses only virtualenv and virtualenvwrapper to manage different versions of Python installed using [Homebrew](http://brew.sh). It turns out that virtualenv already has the tools necessary to manage multiple versions of Python and I can continue using my familiar workflows thanks to virtualenvwrapper.

## Clean up
If not starting with a fresh system, there may be some lingering installations of Python and its related tools. We need to uninstall these. First, remove old versions of Python (and any other Python-related detritus in `/usr/local/Cellar` with

    :::bash
    brew uninstall <package>

We also need to remove `pip`, `virtualenv`, and `virtualenvwrapper` if they were previously installed (either with a Homebrew version of Python or with the version of Python that ships with OSX). Delete all mentions of these packages that appear in `/usr/local/bin` and `/Library/Python/2.7/site-packages`. 


## Install Homebrew
Installing Python is best accomplished by [Homebrew](http://brew.sh). If it isn't already installed, install it by running

    :::bash
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

If the Command Line Tools for Xcode aren't already installed, the Homebrew installation will fail. These can be installed with

    :::bash
    xcode-select --install

We need to make sure the system looks to the Homebrew-installed packages before searcing the rest of the PATH. To accomplish this, we add the following line to our `.bash_profile`:

    :::bash
    export PATH=/usr/local/bin:/usr/local/sbin:$PATH

### Having permissions ussues with OSX El Cap and Homebrew
OSX 10.11/El Capitan introduced some security changes that prevent you from writing to many system directories including `/usr`, `/System`, and `/bin`. Apple left `/usr/local` open, so Homebrew can still be used. Despite this, there still appears to be a permissions issue when trying to install packages with Homebrew. 

If `/usr/local` exists already, resolve this by running

    :::bash
    sudo chown -R $(whoami):admin /usr/local

If `/usr/local` doesn't exist, the resolution is a bit more involved. See the [Homebrew documentation](https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/El_Capitan_and_Homebrew.md) for the fix.

## Install Python
Now we can install the various versions of Python we need with Homebrew:

    :::bash
    brew install python
    brew install python3

## Install virtualenv/virtualenvwrapper
Next, we'll install virtualenv and virtualenvwrapper:
 
    :::bash
    pip install virtualenv
    pip install virtualenvwrapper

## Configure virtualenvwrapper
Finally, we need to configure virtualenvwrapper. I store my virtualenvs in `~/.virtualenvs` and my development projects in `~/Dev`. We'll point virtualenvwrapper to these directories in `.bash_profile`:

    :::bash
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Dev
    source /usr/local/bin/virtualenvwrapper.sh

We're going to make two small additions to our `.bash_profile` to enhance the way virtualenv works. First, we want virtualenv to `cd` into our project directory when issuing a `workon` command:

    :::bash
    CMD='proj_name=$(basename $VIRTUAL_ENV); cd $PROJECT_HOME/$proj_name'
    FILE=$WORKON_HOME/postactivate
    grep -q -F "$CMD" "$FILE" || echo "$CMD" >> "$FILE"

We're also going to set things up so that virtualenvwrapper will issue a `workon` command when we `cd` into a virtulenv directory and `deactivate` when we leave. Again in `.bash_profile`:

https://gist.github.com/gibatronic/de66e3841b981798e6c1
https://gist.github.com/cjerdonek/7583644 
https://gist.github.com/clneagu/7990272


## Configure pip
Usually we want to restrict the usage of pip to when we are inside a virtual environment. To do this, add the following line to `.bash_profile`:

    :::bash
    export PIP_REQUIRE_VIRTUALENV=true

Sometimes we still need to install things globally though, so we'll create a new command to allow global pip installs with `gpip`. Again in `.bash_profile`:

    :::bash
    gpip(){ PIP_REQUIRE_VIRTUALENV="" pip "$@" }






Here's what we're left with:
when not in a virtualenv
    
    python <script> will run a script in python 2
    python3 <script> will run a script in python 3

pip and pip3 work the same way

when inside a virtualenv, just call `python <script>` and whatever version used to make the virtualenv will be used.

When making new virtualenvs, `mkvirtualenv -p python3 <name>` for python 3.x virtual env





