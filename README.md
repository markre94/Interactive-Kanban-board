### Interactive personal Kanban Board with Python and Flask.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [File structure](#file-structure)


## General info

This project was mainly developed to increase productivity by visualization of the workflow of the user. The Web application is based on the Kanban Board as on one of the most frequently used tool of the whole kanban system. 

The kanban_board application serves as an fully interactive personal task board. It handles multiple users, has implemented a login and registration system.

## Technologies
Project is created with:
* Python: 3.8.3
* Flask: 1.1.2
* Bootstrap 4
* sqlite.db


## File structure
The Kanban Board consist the following files:
- run.py _runs an application_
- requirements.txt _contains the required packages for the project._
- flask_app/ _configuration of the aplication along with all backend._

- flask_app/static/ _css file to fix the view and the positioning of the web application
- flask_app/templates _the html file interacting with the backend web application functions inside the views.py

- flask_app/forms.py _a file containing all of the used forms that are used as the main functionalty of the login and registration module of the kanban_app
- flask_app/models.py _file that constructs two models as a foundations of the sqlite database applied int the kanban_app
- flask_app/views.py - main backend fuctions providing of all of the application functionaly




### Additional challenges

- [ ] upgrade the users profile with the jquery/matpoplotlib to visualize the weekly progress and workflow of the logged user
- [ ] write end2end tests with Selenium, and more integration tests via pytest
- [ ] construct a fully operational test environment



