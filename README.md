# Flask Enrollment Project

## Description
UTA_Enrollment is the web application created using flask REST API.

API request is made using Postman.

- UTA_Enrollment project is the website that used to enroll users to different courses that are provided by the site itself.
- This project uses MongoDB non relational database to perform CRUD operations on the data.
- This project can provide advance functionalities such as
  - Login/Logout
  - Session & cookie management
  - Flask-security
  - Flask-WTF -> WTForms
  - Flask_restplus



## Tech Stack
- python > 3.5
- Flask
- Flask-WTF
- Python-dotenv
- flask_restplus
- Black(for code formatting)
- MongoDB(As per the system requirements)

## Project Set-Up

  - ### Clone this repository using following command

    - `git clone https://`

  - ### Download all the requirements from requirements.txt file
    - `pip install -r requirements.txt`

  - ### Activate virtual environment
    - For Windows user
          venv\Scripts\activate
    - For Linux and MAC user
          source venv\Scripts\activate

  - ### Start application
    - `flask run`

## Endpoints
- GET
  - /api
  - /api/<idx>
- POST
  - /api
- PUT
  - /api/<idx>
- DELETE
  - /api/<idx>

### Some errors might occur
  - There might be version conflict between `flask_restplus` and `flask` so change some imports in different files of your environment if error occurs :

      > from werkzeug import cached_property -> from werkzeug.utils import cached_property

      > import flask.scaffold
      >flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
