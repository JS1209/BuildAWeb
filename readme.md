Build A Web
---

backend of a website constructor app.

current folder structure:
- builtSites/   //whole folder created by running the app
    - user/
        - constructed files for user's website
        - config file (now a txt file, could be json later)

- program/
    - sourceFiles/
        - backend/
            - all files/features that are offered in the Build A Web app
        - frontend/
            - all files/features that are offered in the Build A Web app
    - src/ 
        - functions/
            - checks.py
            - functionCopying.py //this copy pastes from sourcefiles into the user's folder
            - UI_functions.py //alters the config file and adds or removes a specified feature to/from the user's folder
        - BuildAWeb.py
    - readme.md
    
    ---
    
    
    proposed folder structure:
- builtSites/   //whole folder created by running the app
    - user/
        - constructed files for user's website
        - config file (now a txt file, could be json later)

- program/
    - sourceFiles/
        - backend/
            - all files/features that are offered in the Build A Web app
        - frontend/
            - all files/features that are offered in the Build A Web app
    
    - src/ 
        - functions/
            - global-vars/ 
                - houses any global variable like user's name
            - dialogs/
                - give user insight to what is happening using print(), each section of the app will need its own dialogs that can be inserted into BuildAWeb.py when needed. e.g. welcome screen, success/error messages.
            - checks/
                - when running the app, user folder, user inputs, app folder contents all have to be checked to prevent conflicts, duplicates, unhandled inputs, etc. these checks may be separated into files according to usage.
            - installers/
                - takes input from user and installs or removes features in user folder
                - feature_builders.py
                - feature_removers.py
        - BuildAWeb.py //strictly combines functionality and manages the flow of the app in an organised way, should avoid having logic of itself.
- readme.md
    
    
   -----------------___________________------------------------______________________-------------------____________________----------------____-------
   
PROPOSED BY JS1209

- BuildAWebWebsite/ -> When the program works good enough, maybe try to make a website out of the program (frontend react and such, backend python3)
- builtSites/ -> Same as above
- program/
    - sourceFiles/ -> Same as above
    - src/
        - BuildAWeb.py - Houses global variables, is the start up application and thus the binder of all functions
        - functions/
            - dialogs/      
                - Dialogs for the menu's
     
            - menus.py
                - Main menu
                - Feature menu
                - Any other menu
                - Responsible for basic changes in tasks.txt (or ofcourse json)
                            
            - writers.py
                - Puts together the files and directories
                - Can copy whole files/directories
                - Can place code in the right place(s) in the right file(s)
                - Calls checkers to check if peace of code/feature is present in source files
                - Calls checkers to check if peace of code/feature is already present in end product (for when feature_builders/removers are
                               used here)                       
                        
            - checkers.py
                - Checks if directories/files exist.
                - Checks if functions exist in sourceFiles (so this scans the .js files for certain functions)
                - Additional checks that are needed throughout the process
                - return 0 if found, return 1 if not found (return 0 because "zero errors have been encountered")
                            
            - feature_builders.py   -> Only for inserting ONE feature (multiple functions due to multiple placements of code)
            - feature_removers.py   -> Only for deleting ONE feature (multiple functions due to multiple deletions of code)
            
            - db_management.py -> for database management when changing models/migrations. Only necessary when everything else works
                            
    BUILDAWEB CALLS MENU'S, WHICH CALL WRITERS, WHICH CALL CHECKERS
