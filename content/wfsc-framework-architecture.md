Title: MATLAB Framework for WFSC Simulation and Analysis - Part 1: Architecture
Date: 2015-06-30
Modified: 2015-06-30
Category: dev
Slug: wfsc-framework-architecture
Status: draft

As computer simulations increase in complexity and scope, it becomes increasingly important to manage and control the underlying models, algorithms, scripts, and resulting data. If left unattended, implementation becomes inconsistent and the simulation becomes difficult to maintain and update. This effect is particularly pronounced when a simulation is developed by a team of people.

The creation and maintenance of large-scale optical system simulations presents a substantial software development challenge for the following reasons:

* __Very large/complex simulations__ for active/adaptive optical systems may consist of hundreds of MATLAB functions and thousands of lines of code.

* __Ongoing development and design changes__ must be reflected in system models as they are made.

* __Distributed development__ exposes coding style differences and makes integration difficult.

## Managing the complexity
The ultimate goal is to develop an integrated environment to simulate, implement, and test complex systems. The introduction of an architectural simulation and analysis framework provides the tools necessary to realize this goal. The architectural framework provides:

* __Centralized development__ on a common simulation baseline

* A __simulation structure__ that is easy to navigate while providing a __separation of concerns__

* Well documented __model interface__

### Centralized Development
Maintaining a centralized simulation baseline for all team members to use and contribute to eliminates duplicate code, exposes bugs, and enhances general understanding of the simulation's design and features. The use of a common baseline also enables the use of version control (as needed) and facilitates unit and end-to-end testing.

### Separation of Model Logic from Simulation
When simulations and analysis are performed during the design phase of a project, a high-fidelity model of the (undeveloped) system must be used as a stand in for the real system. For many reasons, it is desirable to maintain complete separation between the model configuration/logic and any simulation or analysis code. If this approach is taken, there is minimal impact when design changes (which require model updates) occur and much less rework is required to integrate real system data when it becomes available.

A simplified approach to architecting and integrating a model with external simulations and core algorithms is shown below:

##### Model Folder Structure
The model should contain all of the model parameters (in this case, scripts which define MATLAB structures) and functions necessary to stimulate the system model. For an arbitrary active or adaptive optical system, the `telescope` portion of the model contains all of the scripts necessary to simulate the full telescope system in a vaccuum, so to speak. The `environment` portion of the model contains all of the scripts necessary to simulate the model in a real world environment. Finally, the `init` portion of the model contains a number of "quick launch" initialization scripts which are used to select a model for use in a simulation. 

    |-- model
        |-- environment
            |-- photometry
            |-- timeseries
        |-- init
        |-- telescope
            |-- image_chain
            |-- optics
            |-- sensitivities
            |-- sim

##### Interacting with the Model
Interactions with the model are simplified by the use of the init scripts. After the model is on the MATLAB path, an init script is called to load the desired model. Once loaded, the model may be exercised by calling any of its related methods:

    :::matlab
    addpath(genpath('/path/to/model'));
    init_model_july_2015;
    
    opd = gen_opd();
    psf = gen_psf();
    
Sometimes it is desirable to modify a small number of model parameters without developing a completely separate init script. This is easily accomplished by directly overriding model parameters after the init script is called:

    :::matlab
    addpath(genpath('/path/to/model'));
    init_model_july_2015;
    
    % we'd like to change the telescope's focal length from its default value
    telescope.focal_length = 14;
    
    opd = gen_opd();
    psf = gen_psf();


### Simulation Structure
In the short term, simulation structure doesn't matter too much but as the code base grows in size and complexity, unstructured simulations become difficult to update and maintain. An ideal simulation structure should be modularized into very specific functions. Take a look at a sample directory structure below:

    |-- algo
        |-- dfs
        |-- ipo
        |-- mgs
        |-- wfc
        |-- ...
        
    |-- model
        |-- environment
            |-- photometry
            |-- timeseries
        |-- init
        |-- telescope
            |-- image_chain
            |-- optics
            |-- sensitivities
            |-- sim
    
    |-- sim
        |-- commissioning
        |-- dfs
        |-- ipo
        |-- mgs
        |-- time_domain
        |-- ...
    
    |-- util
    
#### Model Folder
The model folder contains all of the model parameters (structures) and functions necessary to stimulate the system model. The configurations folder contains a number of scripts which may be called to instantiate a model in a user's workspace.  In essence, this is akin to creating an instance of a `Model` class, if one existed.

#### Algo Folfer
The algo folder contains core algorithms used for WFSC. These algorithms should not be model-specific.

#### Sim folder
The sim folder contains all of the simulations developed in order to exercise and analyze the model and core algorithms. 

#### Util Folder
The util folder contains a collection of commonly used WFSC MATLAB functions (like `MakeBroadbandPSF.m`, `v2m.m`, `zernike_compose.m`, etc.) These functions provide essential functionality used by the models, simulations, and angorithms.


## Model as a class?
There are several benefits to using a MATLAB class to represent an optical system model:

* Classes are very easy to reuse. Once a class is defined, it is easily extended with subclasses that add new properties.
* Classes can validate individual field values at assignment.
* Classes can restric access to fields, for example, allowing a particular field to be read only.
* Multiple instances of the same class may be loaded at once without running in to variable naming collisions. Try that with a struct!

Interactions are very similar to the approach detailed above. First, we add the Model class to the MATLAB path. Next, we call an init script to create an instance of the model we need. , Once created, the model may be exercised by calling any of its member functions:

    :::matlab
    addpath(genpath('/path/to/model_class_def'));
    
    mo = init_model('init_model_july_2015.m');
    
    base_opd = mo.gen_opd();
    psf = mo.gen_psf();
    
Modifying default parameters is also very similar:

    :::matlab
    addpath(genpath('/path/to/model_class_def'));
    
    mo = init_model('init_model_july_2015.m');
    
    base_opd = mo.gen_opd();
    psf = mo.gen_psf();
    
    % we'd like to change the telescope's focal length from its default value
    mo.focal_length = 14;
    
    opd = mo.gen_opd();
    psf = mo.gen_psf();

## Benefits of a Model-Based, Modularized Approach

#### Code Maintainability
A modularized approach logically compartmentalizes models and simulation scripts and will make it easier to locate and edit the codebase.

#### Scaling
Modular code is much easier to scale. Adding new features or refining existing models should not impact simulation code. It will also be easier to test new functionality.


#### Debugging
Debugging code will be much easier with a modularized approach to development. It will be easier to find offending pieces of code and fix them.

#### Testing
Writing test scripts and testing modular code is a whole lot easier then on non-modularized code.

#### Simple Integration
Because the model interface is standardized and designed to look like the true system interface, real data (when it becomes available) can be integrated into existing simulations with relative ease.
