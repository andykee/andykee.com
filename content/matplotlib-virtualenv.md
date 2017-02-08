Title: Using matplotlib inside a virtualenv on macOS 
Date: 2016-06-24
Category:
Tags: python, osx
Slug: matplotlib-virtualenv
Authors: AK

The GUI frameworks that matplotlib uses to display interactive figures don't play nicely with virtualenvs. Specifically, the default framework that is used on macOS breaks inside a virtualenv. To fix this, we need to tell matplotlib to use a different framework that works in a virtualenv. Thankfully, this is fairly straightforward. After installing matplotlib inside a virtualenv,

    :::bash
    cd ~/.virtualenvs/<name>/lib/python3.5/site-packages/matplotlib/mpl-data

Open `matplotlibrc` and change

    :::bash
    backend : macosx

to

    :::bash
    backend : TkAgg

