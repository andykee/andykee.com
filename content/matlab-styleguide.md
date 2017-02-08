Title: MATLAB Styleguide
Date: 2016-03-21
Category: 
Tags: matlab
Slug: matlab-styleguide
Authors: AK
Status: draft


## Contents
1. [Code Layout](#code-layout)
    * [Indentation](#indentation)
    * [Maximum Line Length](#maximum-line-length)
    * [Whitespace](#whitespace)
2. [Comments](#comments)
    * [Header](#header)
    * [Block Comments](#block-comments)
    * [Inline Comments](#inline-comments)
3. [Naming Conventions](#naming-conventions)
    * [Variables](#variables)
    * [Constants](#constants)
    * [Structures and Cell Arrays](#structures-cell-arrays)
    * [Functions](#functions)
    * [Classes](#classes)
4. [Programming Recommendations](#programming-recommendations)



## <a name="code-layout"></a>1. Code Layout

### <a name="indentation"></a>Indentation


*Indent consistently with the MATLAB editor.* Functions and nested functions should always have their content indented. Logical blocks (`if`/`else`, `while`/`end`) and `try`/`catch` statements should also have their content indented.

*Don't mix tabs and spaces.* The most popular way of intenting is with spaces only. This mode is configured in the MATLAB editor by selecting the option "Tab key inserts spaces" in the Preferences menu.


### <a name="maximum-line-length"></a>Maximum Line Length

*Limit lines to 80 characters in length.* This greatly enhances readability and matches the standard column dimension for many editors, terminal emulators, printers, and debuggers. For long flowing blocks of text (documentation headers and block comments), limiting the length to 72 characters is recommended for readability.

*Split long lines at graceful points.* Long lines due to complicated expressions should be simplified and rewritten on multiple lines. The preferred way of wrapping long lines is by using MATLAB's implied line continuation operator `...`. In general, break after a comma, right parenthesis, string terminator, or space. 


### <a name="whitespace"></a>Whitespace

*Avoid extraneous whitespace*, particularly in the following situations:

* Immediately inside parentheses, brackets, or braces.

    Yes:

        :::matlab
        pow(arg1, arg2)
 
    No:  

        :::matlab
        pow( arg1, arg2 )

* Immediately before a comma or semicolon:

    Yes:
        
        :::matlab
        val = pow(arg1, arg2);
        
    No:

        :::matlab
        val = pow(arg1 , arg2) ;

* On either side of a colon:

    Yes:
        
        :::matlab
        x = y[1:4, :];
        
    No:
        
        :::matlab
        x = y[1 : 4, : ];

* Immediately before the open parenthesis of a function definition or call:

    Yes:

        :::matlab
        function pow(arg1, arg2)
        
        pow(x, y)
        
    No:  
        
        :::matlab
        function pow (arg1, arg2)
        pow (x, y)

* Immediately before the open bracket that starts an indexing or slicing:

    Yes:

        :::matlab
        x[1:5] = y[6:10];
    
    No:  

        :::matlab
        x [1:5] = y [6:10];

* More than one space around an assignment to align it with another:

    Yes:

        :::matlab
        x = 1;
        y = 2;
        variable = 3;

    No:

        :::matlab
        x        = 1;
        y        = 2;
        variable = 3;   

Avoid trailing whitespace anywhere. It's usually invisible and can be confusing.

Always surround binary operators with a single space on either side: assignment (`=`), comparisons (`==`, `~=`, `<`, `>`, `<=`, `>=`), and Booleans (`&`, `|`, `&&`, `||`).


Compound commands (multiple commands on the same line) are generally discouraged. While sometimes it's desirable to put an if/for/while with a small body on the same line, never do this for a multi-clause commands.

Yes:

    :::matlab
    if x > 0
        do_the_thing();
    end

Rather not:

    :::matlab
    if x > 0, do_the_thing(); end

Definitely not:

    :::matlab
    if x > 0, do the thing(); else, do_the_other_thing(); end

Separate functions and major code blocks with two blank lines. Use a single blank line to indicate logical sections within functions and major code blocks


## <a name="comments"></a>2. Comments

All comments should be formatted using MATLAB markup. This makes publication of documentation using `publish` a breeze. A basic syntax guide follows: 

    :::matlab
    %% SECTION TITLE
    % DESCRIPTIVE TEXT
    % 
    %%% SECTION TITLE WITHOUT SECTION BREAK
    %
    % _ITALIC TEXT_
    %
    % *BOLD TEXT*
    %
    % |MONOSPACED TEXT|
    %
    % BULLETED LIST:
    % * ITEM 1
    % * ITEM 2
    %
    % NUMBERED LIST:
    % # ITEM 1
    % # ITEM 2
    %
    % PREPEND SOURCE CODE WITH THREE SPACES:
    %   for i = 1:10
    %       disp(x)
    %   end
    %
    % INCLUDE EXTERNAL FILE CONTENT:
    % <include>filename.m</include>
    %
    % INCLUDE IMAGES:
    % <<filename.png>>
    %
    % HYPERLINKS:
    % <http://www.jpl.nasa.gov>
    % <matlab:FUNCTION DISPLAYED_TEXT>
    %
    % INLINE LATEX EQUATIONS:
    % $e^{\pi i} = -1$
    %
    % BLOCK LATEX EQUATIONS:
    % $$e^{\pi i} = -1$$
    %
    % LATEX MARKUP:
    % <latex>
    % ...
    % </latex>


### <a name="header"></a>Header

Write header comments for all functions and classes. Header comments should incude a sample function call, function description, inputs, and outputs. Notes, references, and examples are optional. 

Header comments should be located above the `function` or `class` statement. 

Full header comments are not necessary for scripts, but you should begin the script with a comment listing author, date, and a short description of the script.

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


### <a name="block-comments"></a>Block Comments

Block comments provide descriptions of code sequences, algorithms, data structures, etc. They provide a convenient place to describe a code block and any special processing that is used. Block comments should be indented to the same level as the code they describe.   

Place a blank line before and after block comments. Paragraphs inside a block comment should be separated by  blank comment line (a line containing a single `%`).


### <a name="inline-comments"></a>Inline Comments

Inline comments describe short implementation details and should be used sparingly. They should be separated by two spaces from the statement they describe. They should start with a `%` and a single space.


## <a name="naming-conventions"></a>3. Naming Conventions

### <a name="variables"></a>Variables
Use `lowercase` for simple variable names and `lowerCamelCase` for compound variable names. 

Prefix variable names that store a count of things with "n" or "m":

    :::matlab
    [nRows,nCols] = size(array);

Prefix variable names that are incremented in a loop with "i" (or "j", "k", ...) to make it clear what the loop is indexing through:

    :::matlab
    for iRow = 1:nRows
        ...

Use "is" as a prefix for variables representing logical states:

    :::matlab
    isPositive = data > 0;


### <a name="constants"></a>Constants
Use `UPPERCASE` for constant names. If the constant has a compound name, use an underscore as a separator.


### <a name="structures-cell-arrays"></a>Structures and Cell Arrays
Use `UpperCamelCase` for structure names. Structure fields should follow the naming convention for variables.

Cell arrays should follow the convention for variables.


### <a name="functions"></a>Functions
Functions should have short, all `lowercase` names. They should be named for what they do and function names should match their filenames. Underscores may be used sparingly to improve readability. 


### <a name="classes"></a>Classes
Use `UpperCamelCase` for class and object names. Class names should be nouns. 

Class properties should be named like structure fields or variables. Class methods should be named like functions.


## <a name="programming-recommendations"></a>4. Programming Recommendations

* Minimize the use of global variables. Their use makes the code more difficult to read, understand, and debug. 

* Avoid the use of `eval`. Statements that use `eval` tend to be harder to read and write, more difficult to debug, and slower to execute than alternatives. Consider using structures or cell arrays coupled with dynamic field referencing or cell indexing as an alternative. 

* Avoid the conditional expression `if 0`. Use block comments to temporarily bypass a block of code instead. Never release software containing `if 0`.

* Use an options structure when a function requires many input parameters. A structure is easier to parse than a long list of parameter-value pairs. 

* When working with large amounts of data, structures of arrays are preferable to arrays of structures as they require significantly less memory and come with a speed benefit when reading/writing.

        :::matlab
        % Structure of arrays
        Data.x = linspace(0,2*pi);
        Data.y = sin(Data.x);

        % Array of structures
        Img(1).nRows = 256;
        Img(1).nCols = 256;
        Img(2).nRows = 1000;
        Img(2).nCols = 1000;
        
* Profile the code. It helps identify bottlenecks in execution speed and identifies opportunities for optimization.

* Pay attention to messages from the Code Analyzer. Implemnent the suggested changes when they make sense and don't significantly impact redability.

* Use logical indexing instead of `find`. Logical indexing is almost always faster.

* Provide some form of input validity checking for functions. Checking the type and range of numerical inputs and the validity of character strings greatly improves the reliability of a function. The `inputParser` function coupled with `assert()` is very helpful for input validity checking.

