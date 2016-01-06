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
    * [Indentation](#indentation)
    * [Maximum line length](#maximum-line-length)
    * [Blank lines](#blank-lines)
    * [Whitespace](#whitespace)
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

Logic block (if/else, while/end) and try/catch statements should always have their content indented four spaces. 

All functions, including nested functions, should be indented.

Good:

    :::matlab
    function foo
        disp('indent all functions');

        if True
            nestedfunction;
        end

        function nestedfunction
            if doSomething
                disp('we did something');
            end
        end

    end

Bad:

    :::matlab
    function foo
    disp('classic indenting');
    
    if True
        nestedfunction;
    end

        function nestedfunction
        if doSomething
            disp('we did something');
        end
        end
    end

If you're using the MATLAB Editor, it has smart indenting built in. The smart indenting options are configurable in **Preferences -> Editor/Debugger -> Language**, select **MATLAB** as the language, and see **Function indenting format**.

### <a name="maximum-line-length"></a>Maximum line length

90%+ of your lines should be limited to 75 characters. "Flat is better than nested."

### <a name="blank-lines"></a>Blank lines

### <a name="whitespace"></a>Whitespace

Avoid extraneous whitespace in the following situations:

SEE PEP8

## <a name="comments"></a>Comments

### <a name="documentation-strings"></a>Documentation strings


### <a name="block-comments"></a>Block comments


### <a name="inline-comments"></a>Inline comments

An inline comment is a comment on the same line as a statement. Use them sparingly. When necessary, they should be separated by at least two spaces from the end of they statement. They should start with a `%` and a single space.

## <a name="naming-conventions"></a>Naming Conventions 

### <a name="variables"></a>Variables

### <a name="functions"></a>Functions

Function names should be in `lowercase`, with underlines used sparingly to improve readability. Function names should match their filenames.

### <a name="constants"></a>Constants

Constants should be named in `ALL_CAPS_WITH_UNDERSCORES`.

### <a name="configuration-and-options"></a>Configuration and options

Script configurations and options are commonly stored in strucutre arrays. Field names should use `UpperCamel` and values should be in `lowercase`:

    :::matlab
    config = struct( ...
        'Algorithm', 'levenberg-marquardt', ...
        'Crop', 'off', ...
        'DispIter', True, ...
        'PlotIter', True, ...
        'DispFinal', False, ...
        'MaxIter', 30 ...
    );

### <a name="classes"></a>Classes

Class names should use `UpperCamel` with capitalized acronyms: `HTTPWriter`, not `HttpWriter`.


## <a name="speed"></a>Speed

### <a name="vectorize"></a>Vectorize



### <a name="structures-of-arrays"></a>Structures of arrays vs arrays of structures

When working with large amounts of data, structures of arrays are preferable to arrays of structures as they require significantly less memory and come with a speed benefit when reading/writing.

    :::matlab
    % Structure of arrays
    data.x = linspace(0,2*pi);
    data.y = sin(data.x);

    % Array of structures
    people(1).name = 'doug';
    people(1).job = 'retired';
    
    people(2).name = 'andy';
    people(2).job = 'engineer';


### <a name="pre-allocation"></a>Pre-allocation

## <a name="patterns"></a>Patterns

### <a name="functions"></a>Functions
### <a name="error-handling"></a>Error handling
try/catch

### <a name="warnings"></a>Warnings

