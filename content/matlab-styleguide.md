Title: MATLAB Styleguide
Date: 2016-03-21
Category: dev
Tags: matlab
Slug: matlab-styleguide
Authors: AK


# MATLAB Styleguide


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



## 1. Code Layout

### Indentation

Indent consistently with the MATLAB editor. Functions and nested functions should always have their content indented. Logical blocks (`if`/`else`, `while`/`end`) and `try`/`catch` statements should also have their content indented.

Don't mix tabs and spaces. The most popular way of intenting is with spaces only. This mode is configured in the MATLAB editor by selecting the option "Tab key inserts spaces" in the Preferences menu.


### Maximum Line Length

Limit lines to 80 characters in length. This greatly enhances readability and matches the standard column dimension for many editors, terminal emulators, printers, and debuggers. For long flowing blocks of text (documentation headers and block comments), limiting the length to 72 characters is recommended for readability.

Split long lines at graceful points. Long lines due to complicated expressions should be simplified and rewritten on multiple lines. The preferred way of wrapping long lines is by using MATLAB's implied line continuation operator `...`. In general, break after a comma, right parenthesis, string terminator, or space. 


### Whitespace

Avoid extraneous whitespace in the following situations:

* Immediately inside parentheses, brackets, or braces.

    Yes: spam(ham[1], {eggs: 2})
    No:  spam( ham[ 1 ], { eggs: 2 } )

* Immediately before a comma, semicolon, or colon:

* On either side of a colon. Because it acts like a 

More here from MATLAB book and pep8



Avoid trailing whitespace anywhere. It's usually invisible and can be confusing.

Always surround binary operators with a single space on either side: assignment (`=`), comparisons (`==`, `~=`, `<`, `>`, `<=`, `>=`), and Booleans (`&`, `|`, `&&`, `||`).


Compound commands (multiple commands on the same line) are generally discouraged. While sometimes it's desirable to put an if/for/while with a small body on the same line, never do this for a multi-clause commands.

Rather not:

    pep8 example

Definitely not:

    pep8 example

Separate functions and major code blocks with two blank lines. Use a single blank line to indicate logical sections within functions and major code blocks


## 2. Comments

All comments should be formatted 

### Header

Write header comments for all functions and classes. Header comments should use the following format:
 





Header comments should be located above the `function` or `class` statement. 

Full header comments are not necessary for scripts, but you should begin the script with a comment listing author, date, and a short description of the script.




12. Format header comments for easy publishing as documentation
short syntax guide for matlab publishing here - google MATLAB publishing markup

13. Write documentation headers for all functions and classes
Sample function call, description, inputs, and outputs are required (as defined), notes, references, and examples are optional.

    :::matlab
    % function name
    % 
    % Function description
    %
    % Inputs
    % ------
    % input1 : description 
    % inputn : description 
    %
    % Outputs
    % -------
    % output1 : description  
    % outputn : description
    % 
    % Notes
    % -----
    % This is an example of a note. It may cite a reference [1] as needed.
    %
    % References
    % ----------
    % [1] Reference 1
    % [2] Reference 2
    % 
    % Examples
    % --------
    % >> blah
    %
    
    % Author: 
    % Date: 
    % Version: 

14. Syntax discussion (see elements of matlab style 118)


### Block Comments

Block comments provide descriptions of code sequences, algorithms, data structures, etc. They provide a convenient place to describe a code block and any special processing that is used. Block comments should be indented to the same level as the code they describe.   

Place a blank line before and after block comments. Paragraphs inside a block comment should be separated by  blank comment line (a line containing a single `%`).


### Inline Comments

Inline comments describe short implementation details and should be used sparingly. They should be separated by two spaces from the statement they describe. They should start with a ~%~ and a single space.


## 3. Naming Conventions

### Variables
Use lowercase for simple variable names and lowerCamelCase for compound variable names. 


### Constants
Use all uppercase for constant names. If the constant has a compound name, use an underscore as a separator.


### Structures and Cell Arrays
Use UpperCamelCase for structure names. Structure fields should follow the naming convention for variables.

Cell arrays should follow the convention for variables.


### Functions
Functions should have short, all lowercase names. Underlines may be used sparingly to improve readability. They should be named for what they do and function names should match their filenames.


### Classes
Use nouns when naming classes. Use UpperCamelCase for class and object names. 

Class properties should be named like structure fields or variables. Class methods should be named like functions.


### Data Files and Directories


## 4. Programming Recommendations

Use block comments to temporarily bypass a block of code
    not `if 0`


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


