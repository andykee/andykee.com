Title: Python Ref 
Date: 2015-12-01 11:00
Modified: 2015-12-01 11:00
Category: ref
Tags: python
Summary:
Slug: python 
Authors: Andy Kee

### Setting up new projects for github with virtualenv
    
    cd ~/dev
    mkdir project
    mkvirtualenv project
    cd project
    git init
    
### Using requirements.txt with pip

After installing a bunch of stuff with pip:

    pip freeze > requirements.txt

After cloning a new git repo or pulling down new changes to an existing one:

    pip install -r path/to/requirements.txt


