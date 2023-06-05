The Django Post

The Django Post
===============

Features
--------

*   User Registration and Authentication:

*   Users can register an account to create and manage their blog posts.
*   User authentication is implemented to ensure secure access to the platform.

*   Blog Creation and Management:

*   Users can create new blog posts by providing a title and content.
*   Existing blog posts can be edited or deleted by the author.
*   Each blog post includes the author's username and the date it was posted.

*   Commenting System:

*   Users can leave comments on blog posts to engage in discussions.
*   Comments include the author's username and the date it was posted.

*   Admin Panel:

*   Administrators have access to an admin panel for managing users, blogs, and comments.
*   Admins can export user data, including mail id, password, designation, age, gender, and registration date.
*   Admins can also export user data and blogs based on specific criteria.
*   Additionally, admins have the ability to export all user records except for the blogs.

Installation
------------

1.  Clone the repository: `git clone https://github.com/ZicsX/The-Django-Post.git`
2.  Navigate to the project directory: `cd The-Django-Post`
3.  Create a virtual environment: `python -m venv env`
4.  Activate the virtual environment:
    *   For Windows: `.\env\Scripts\activate`
    *   For macOS/Linux: `source env/bin/activate`
5.  Install the required dependencies: `pip install -r requirements.txt`
6.  Apply database migrations: `python manage.py migrate`
7.  Start the development server: `python manage.py runserver`

The application should now be running locally at [http://localhost:8000/](http://localhost:8000/).

Technologies Used
-----------------

*   Django: A powerful Python web framework used for building the backend of the application.
*   Django REST Framework: An extension for Django that enables the creation of RESTful APIs.
*   Bootstrap: A popular CSS framework for responsive and mobile-first web design.

Contributing
------------

Contributions to "The Django Post" are welcome! If you have any ideas, improvements, or bug fixes, please open an issue or submit a pull request.

License
-------

"The Django Post" is open source and released under the [MIT License](https://opensource.org/licenses/MIT).
