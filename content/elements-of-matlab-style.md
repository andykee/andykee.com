Title: The Elements of MATLAB Style 
Date: 2016-01-03 19:49
Modified: 2016-01-04 16:18
Category: dev
Tags: matlab
Summary: The following guide gives coding conventions for what I consider to be great MATLAB style. It includes details on syntax, layout, naming, basic patterns, project organization, and architecture. This style guide will evolve over time as I continue to collect and discover best practices.  
Slug: elements-of-matlab-style
Authors: AK

I used to write a lot of Python code. At my new job, we work mostly in MATLAB. I enjoy using both languages and am probably equally capabile in both (within their own limitations). That being said, both languages have their issues (just google ["python2 vs python3"](https://www.google.com/search?q=python2+vs+python3) or ["MATLAB plotting"](https://www.google.com/search?q=matlab+plotting)).

One place that I feel Python really shines while MATLAB falls relatively short is in defining a coding style. Python has [PEP8](https://www.python.org/dev/peps/pep-0008/) which gives a fairly comprehensive set of style guidelines. The closest thing I could find from MathWorks is a short document on [Techniques to Improve Performance](http://www.mathworks.com/help/matlab/matlab_prog/techniques-for-improving-performance.html). Not a bad start, but we can do better.

The following guide gives coding conventions for what I consider to be great MATLAB style. It includes details on syntax, layout, naming, basic patterns, project organization, and architecture. While its organization may be similar to PEP8, its content is all MATLAB. This style guide will evolve over time as I continue to collect and discover best practices. 


## Contents
* [Code layout](#code-layout)
    * Indentation
    * Maximum Line Length
    * Blank Lines
    * Encoding
* Comments
    * Documentation strings
    * Block comments
    * Inline comments
* Naming Conventions
    * Function Names
    * Variable Names
    * Constants
    * Configurations and Options
    * Class Names
* Patterns
    * Functions
    * Try/catch
    * Warnings
* Project organization



## <a name="code-layout"></a>Code layout  
 
