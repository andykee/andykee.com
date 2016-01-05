Title: The Elements of MATLAB Style 
Date: 2016-01-03 19:49
Modified: 2016-01-04 16:18
Category: dev
Tags: matlab
Summary: The following guide gives coding conventions for what I consider to be great MATLAB style. It includes details on syntax, layout, naming, basic patterns, project organization, and architecture. This style guide will evolve over time as I continue to collect and discover best practices.  
Slug: elements-of-matlab-style
Authors: AK

I used to write a lot of Python code. At my new job, we work mostly in MATLAB. I enjoy using both languages and am probably equally capabile in both (within their own limitations). That being said, both languages have their issues (just google ["python2 vs python3"](https://www.google.com/search?q=python2+vs+python3) or ["MATLAB plotting"](https://www.google.com/search?q=matlab+plotting)).

One place that I feel Python really shines while MATLAB falls relatively short is in defining a coding style. Python has [PEP8](https://www.python.org/dev/peps/pep-0008/) which gives a fairly comprehensive set of style guidelines. The closest thing I could find from MathWorks is a short document on [Techniques to Improve Performance](http://www.mathworks.com/help/matlab/matlab_prog/techniques-for-improving-performance.html). Not a bad start, but we can do better. Several unofficial MATLAB style guides exist, although I was surprised to find very few of them conform to the style MathWorks uses to write its functions - especially with respect to comments and naming conventions.

The following guide gives coding conventions for what I consider to be great MATLAB style. It includes details on syntax, layout, naming, basic patterns, project organization, and architecture. While its organization may be similar to PEP8, its content is all MATLAB. This style guide will evolve over time as I continue to collect and discover best practices. 


## Contents
* [Code Layout](#code-layout)
    * [Indentation](#intentation)
    * [Maximum line length](#maximum-line-length)
    * [Blank lines](#blank-lines)
* [Comments](#comments)
    * [Documentation strings](#documentation-strings)
    * [Block comments](#block-comments)
    * [Inline comments](#inline-comments)
* [Naming Conventions](#naming-conventions)
    * [Variables](#variables)
    * [Functions](#functions)
    * [Constants](#constants)
    * [Configurations and options](#configuration-and-options)
    * [Classes](#classes)
* [Speed](#speed)
    * [Vectorize](#vectorize)
    * [Structures of arrays](#structures-of-arrays)
    * [Pre-allocation](#pre-allocation)
* [Patterns](#patterns)
    * [Functions](#functions)
    * [Error handling](#error-handling)
    * [Warnings](#warnings)



## <a name="code-layout"></a>Code Layout  

### <a name="indentation"></a>Indentation


### <a name="maximum-line-length"></a>Maximum line length


### <a name="blank-lines"></a>Blank lines


## <a name="comments"></a>Comments

### <a name="documentation-strings"></a>Documentation strings


### <a name="block-comments"></a>Block comments


### <a name="inline-comments"></a>Inline comments


## <a name="naming-conventions"></a>Naming Conventions 

### <a name="variables"></a>Variables
### <a name="functions"></a>Functions
### <a name="constants"></a>Constants
### <a name="configuration-and-options"></a>Configuration and options
### <a name="classes"></a>Classes

## <a name="speed"></a>Speed

### <a name="vectorize"></a>Vectorize
### <a name="structures-of-arrays"></a>Structures of arrays
### <a name="pre-allocation"></a>Pre-allocation

## <a name="patterns"></a>Patterns

### <a name="functions"></a>Functions
### <a name="error-handling"></a>Error handling
try/catch

### <a name="warnings"></a>Warnings

