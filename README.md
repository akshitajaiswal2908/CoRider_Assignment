# Flask CRUD Application

### Introduction

This is a basic Flask application that demonstrates CRUD (Create, Read, Update, Delete) operations using MongoDB for data storage.

### Features

- **Create**: Add new users to the database.
- **Read**: View existing users.
- **Update**: Modify user details.
- **Delete**: Remove users from the database.

### Prerequisites

- Python 3.x
- MongoDB

### Installation and Running

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_name>

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

3. **Run MongoDB (if not using Docker):**

    Start MongoDB on your local machine using the command:

    ```bash
    mongod

    Alternatively,if you want to run MongoDB using Docker, use the following command:

    ```bash
    docker run --name mongodb -d -p 27017:27017 mongo

4. ***Run the application:***

    Set the environment variable and run the Flask application:

    ```bash

    set FLASK_APP=run.py
    set FLASK_DEBUG=True 
    flask run

    If using Docker, you can run your Flask application in a Docker container as follows:

    ```bash

    docker build -t flask-crud-app .
    docker run -d -p 5000:5000 --link mongodb:mongo flask-crud-app

5. ***Open a browser and navigate to:***


    ```http://127.0.0.1:5000