# Flask CRUD Application

### Introduction

This is a basic Flask application that demonstrates CRUD (Create, Read, Update, Delete) operations using MongoDB for data storage.

### Features

- **Create**: Add new users to the database.
  - **POST /users**: Creates a new user with the specified data.
  
- **Read**: View existing users.
  - **GET /users**: Returns a list of all users.
  - **GET /users/<id>**: Returns the user with the specified ID.
  
- **Update**: Modify user details.
  - **PUT /users/<id>**: Updates the user with the specified ID with the new data.
  
- **Delete**: Remove users from the database.
  - **DELETE /users/<id>**: Deletes the user with the specified ID.

### Prerequisites

- Python 3.x
- MongoDB

### Installation and Running

1. **Clone the repository:**

   ```
   git clone git@github.com:akshitajaiswal2908/CoRider_Assignment.git
   cd CoRider_Assignment

2. **Install dependencies:**

    ```
    pip install -r requirements.txt

3. **Run MongoDB (if not using Docker):**

    Start MongoDB on your local machine using the command:

    ```
    mongod
    ```
    Alternatively,if you want to run MongoDB using Docker, use the following command:

    ```
    docker run --name mongodb -d -p 27017:27017 mongo

4. ***Run the application:***

    Set the environment variable and run the Flask application:

    ```

    set FLASK_APP=run.py
    set FLASK_DEBUG=True 
    flask run

    ```
    
    If using Docker, you can run your Flask application in a Docker container as follows:

    ```

    docker build -t flask-crud-app .
    docker run -d -p 5000:5000 --link mongodb:mongo flask-crud-app

5. ***Open a browser and navigate to:***


    ```
    http://127.0.0.1:5000

6. ***When you're done working with your Flask application and MongoDB, you can close them using the following steps:***
   ```

   docker stop flask-crud-app
   docker stop mongodb
