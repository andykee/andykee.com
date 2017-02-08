Title: Using matplotlib inside a virtualenv on macOS 
Date: 2016-06-24
Category: dev
Tags: python, osx
Slug: matplotlib-virtualenvs
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

Supposedly this change can also be made inside a python script by doing 

    :::python
    import matplotlib.pyplot as plt
    plt.use('TkAgg')

but I haven't tried this yet.

