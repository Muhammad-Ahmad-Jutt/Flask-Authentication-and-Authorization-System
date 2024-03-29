
# Flask Authentication and Authorization System Demonstration

This project demonstrates a basic authentication and authorization system using Flask, JWT (JSON Web Tokens), and SQLAlchemy. It provides endpoints for user login, user creation, retrieving user information, listing items, and logging out.

## Purpose

The main purpose of this project is to learn how the login and logout sessions work in a web application. Additionally, it demonstrates password hashing for secure storage in a database.

## Prerequisites

- Python 3.x
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- MySQL server (or another compatible database server)
- Hashlib(for converting password to hash)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
2. Navigate to the project directory:

   ```bash
   cd 'your repo'
   ```
3. Install dependencies:
   ``` bash
   pip install -r requirements.txt
   ```
4. Set up the MySQL database:

   * Create a database named `users`.
   * Adjust the database URI in `app.config['SQLALCHEMY_DATABASE_URI']` in `app.py` if necessary.

## Usage

1. Run the Flask application:
   ``` bash
   python app.py
   ```
2. Access the application in your browser at `http://localhost:5000`.

### API Endpoints

* **POST /login** : Endpoint to authenticate users and generate a JWT token.
* **POST /create_user** : Endpoint to create a new user.
* **GET /user_info** : Endpoint to retrieve user information.
* **GET /items** : Endpoint to retrieve a list of items (requires authentication).
* **POST /logout** : Endpoint to log out users.

### HTML Pages

* **index.html** : Provides a simple interface for user login, sign out, and checking status.

### JavaScript Code

* **index.js** : Handles user interactions such as signing in, signing out, and checking status.

## Contributing
s
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE]() file for details.
