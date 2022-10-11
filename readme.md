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
    
    
    
