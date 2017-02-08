Title: Using Sphinx to Create MATLAB Documentation
Date: 04-23-2016
Category: 
Tags: matlab
Summary: 
Slug: sphinx-matlab
Authors: AK
Status: draft

##1. Install and configure Sphinx
Install Sphinx, either from a distribution package or with `pip`

    :::bash
    pip install Sphinx

Set up Sphinx by running `sphinx-quickstart` with the follwoing options:

    :::bash
    > Root path for the documentation: <project_root>/doc
    > Separate source and build directories: n
    > Name prefix for templates and static dir: _
    > Project name:
    > Author name(s):
    > Project version: 
    > Project release:
    > Project language: en
    > Source file suffix: .rst
    > Name of your master document: index
    > Do you want to use the epub builder: n
    
    > autodoc: automatically insert docstrings from modules: y
    > doctest: automatically test code snippets in doctest blocks: n
    > intersphinx: link between Sphinx documentation of ditfferetn projects: n
    > todo: write "todo" entries that can be shown or hidden on build: n
    > coverage: checks for documentation coverage: n
    > imgmath: include math, rendered as PNG or SVG images: n
    > mathjax: include math, rendered in the browser by MathJax: y
    > ifconfig: conditional inclusion of content based on config values: n
    > viewcode: include links to the source code of documented Python objects: n
    > githubpages: create .nojekyll file to publish the document on GitHub pages: n
    
    > Create Makefile?: y
    > Create Windows command file?: n

##2. Install and Configure `matlabdomain` Extension 

    :::bash
    pip install sphinxcontrib-matlabdomain

Configure `matlabdomain` in Sphinx's `conf.py` file

    :::python
    extensions = [
        'sphinxcontrib.matlab'
    ]

    matlab_src_dir = '/absolute/path/to/matlab/src'
    default_domain = 'mat'

##3. 




