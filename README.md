
# Backend of a Social media app using FastAPI
This is a backend implementation of a social media app built using FastAPI. The app allows users to register, login, create posts, like posts, and read others posts. The backend is built using Python, FastAPI, and SQLAlchemy, and the database is PostgreSQL. The app is deployed on Render.

## Live Deployed
The service is deployed on https://test-e3xf.onrender.com and a documented at https://test-e3xf.onrender.com/docs.


## Problem Statement
Design and develop a backend for a social media application using FastAPI that can be deployed on any web hosting service. The application should allow users to register, login, create posts, like and vote on posts, and get posts. 

## Description
The backend uses Postgres as its database and SQLAlchemy as its ORM to interact with the database. The backend has implement JWT authentication to protect certain routes and limit access to only logged-in users. Alembic has been used as the database migration tool to manage schema changes.

## Tech Stack
    Python 3
    FastAPI
    Pydantic
    SQL databases (PostgreSQL)
    SQLAlchemy
    Alembic (for database migrations)
    Git and GitHub
    Render (for deployment)
    Postman & Thunder Client (for testing API endpoints)

## API endpoints
This API consists of four distinct routes:

    1. The "Post" route: This route is responsible for the creation, deletion, updating, and retrieval of posts.

    2. The "Users" route: This route is designed to handle user creation and user search by ID.
    3. The "Auth" route: This route facilitates user authentication and login.
    4. The "Vote" route: This route handles voting and liking functionality, including upvotes and downvotes. However, note that the current implementation does not include logic for downvotes.

| 	Endpoint	 | 	HTTP Method	 | 	Description	 | 
| 	:-----:	 | 	:-----:	 | 	:-----:	 | 
| /users	| POST	 | Creates a new user with the provided user data in the request body. Returns the newly created user data in the response. If a user with the same email already exists, returns a 208 Already Reported HTTP error.|
|/users/{id} |	GET	| Retrieves the user data for the user with the specified id parameter. If the user is found, returns the user data in the response. If the user is not found, returns a 404 Not Found HTTP error.|

| 	Endpoint	 | 	HTTP Method	 | 	Description	 |
| 	:-----:	 | 	:-----:	 | 	:-----:	 | 
| /login	|POST|	Authenticates the user by checking if the email and password provided in the user_cred parameter match those stored in the database. If they match, an access token is generated using oauth2.create_access_token and returned as a response. If they do not match, an HTTPException with status code 403 is raised, indicating that the credentials are invalid.|

| 	Endpoint	 | 	HTTP Method	 | 	Description	 |
| 	:-----:	 | 	:-----:	 | 	:-----:	 | 
|/posts |	GET	| Returns a list of all posts, including the count of votes for each post. Supports search query to filter posts by title.|
|/posts |	POST	| Creates a new post with the provided title, content, and published status. The logged-in user's ID is automatically assigned as the post's user_id. Returns the newly created post.|
|/posts/{id} |	GET	| Returns a specific post by ID, including the count of votes for the post. Raises a 404 error if the post with the given ID does not exist, or if the requesting user is not the author of the post.|
|/posts/{id} |	DELETE	| Deletes a specific post by ID. Raises a 404 error if the post with the given ID does not exist, or if the requesting user is not the author of the post. Returns a 204 status code on successful deletion.|
|/posts/{id} |	PUT	| Updates a specific post by ID with the provided title, content, and published status. Raises a 404 error if the post with the given ID does not exist, or if the requesting user is not the author of the post. Returns the updated post.|

| 	Endpoint	 | 	HTTP Method	 | 	Description	 |
| 	:-----:	 | 	:-----:	 | 	:-----:	 | 
|/votes	| POST |	This endpoint is used to vote on a post. It takes a JSON payload in the request body containing the ID of the post to be voted on and the direction of the vote (up or down). The user making the vote is authenticated via an access token. If the user has already voted on the post, a 208 Already Reported status code is returned. If the post does not exist, a 404 Not Found status code is returned. If the vote is successfully added to the database, a 201 Created status code is returned along with the newly created vote object in JSON format.|


## Installation
1. Clone the repository: git clone https://github.com/Devanshchowdhury2212/RestAPI.git
2. Change directory into the project: cd RestAPI
3. Create a virtual environment: python -m venv env
4. Activate the virtual environment:
- Windows: env\Scripts\activate
- Linux/Mac: source env/bin/activate
5. Install the dependencies: pip install -r requirements.txt

## Configuration 
The app requires some environment variables to be set. These can be set using a .env file in the root of the project.
    
    -DATABASE_HOSTNAME=${DATABASE_HOSTNAME}
    -database_port=${database_port}
    -database_password=${database_password} 
    -database_name=${database_name}
    -database_username=${database_username}
    -secret_key=${secret_key}
    -algorithm=${algorithm}
    -ACCESS_TOKEN_EXPIRE_MINUTES=${ACCESS_TOKEN_EXPIRE_MINUTES}
    -SQLALCHEMY_DB_URL=${SQLALCHEMY_DB_URL} 
- SQLALCHEMY_DB_URL: the URL to your PostgreSQL database. Replace user, password, and dbname with your database credentials.
- SECRET_KEY: a secret key used for encrypting and decrypting JSON Web Tokens (JWTs).

## Running the App
To start the app, run:

uvicorn app.main:app --reload

This will start the app at http://localhost:8000.

