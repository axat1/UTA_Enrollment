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

    - `git clone https://github.com/axat1/UTA_Enrollment.git`

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

## Home Page
  ![HomePage](https://user-images.githubusercontent.com/55522031/119269737-dabc2d80-bc16-11eb-904a-e21e956a20f2.JPG)

## Login Page
  ![login](https://user-images.githubusercontent.com/55522031/119269775-05a68180-bc17-11eb-81b6-72c98d14547c.JPG)

## User Home Page
  ![Home_Page](https://user-images.githubusercontent.com/55522031/119269787-19ea7e80-bc17-11eb-8780-0c835269b1ea.JPG)

## Register Page
  ![register](https://user-images.githubusercontent.com/55522031/119269798-253daa00-bc17-11eb-99ce-4214f0aca065.JPG)

## Courses Page
  ![courses](https://user-images.githubusercontent.com/55522031/119269808-31c20280-bc17-11eb-89c6-9e5c96dfcc09.JPG)

## Enrollment Page
  ![enrollment](https://user-images.githubusercontent.com/55522031/119269816-3f778800-bc17-11eb-9524-723b2f79db1a.JPG)


  
### Some errors might occur
  - There might be version conflict between `flask_restplus` and `flask` so change some imports in different files of your environment if error occurs :

      > from werkzeug import cached_property -> from werkzeug.utils import cached_property

      > import flask.scaffold
      >flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
 
