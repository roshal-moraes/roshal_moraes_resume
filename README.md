Detailed step-by-step guide to creating a Flask project with an SQLite database and using Bootstrap for styling. We'll set up a virtual environment as well.

# Step 1: Set Up Your Project

Create  directory portfolio for  project and navigate to it in the terminal.

#Step 2: Create a Virtual Environment

`pip install virtualenv`
`virtualenv portfolio`

# Step 3: Activate the virtual environment:

On Windows:
`venv\Scripts\activate`


# Step 4: Install Flask and SQLite

Install Flask and SQLite:
`pip install flask`

# Step 5: Set Up Your Flask Application and Database
Refer app.py as for application apis.
Refer database.py for database setup.

# Step 6: Create HTML Templates

Create HTML template for resume(refer index.html). This template will be used in app.py to display the resume information


# Step 7: Custom CSS
To store CSS files in a separate folder and use them in your HTML files, you can follow these steps:

Create a Folder for Your CSS Files:

Create a folder in your project directory to store your CSS files. For example, you can create a folder named "static" or "css."

Move CSS Files:
Move your CSS files (e.g., styles.css) to the "static" or "css" folder you created.

Update Your HTML to Link CSS:
In your HTML file (e.g., index.html), you'll need to link to the CSS files in the "static" folder using the url_for function provided by Flask.

Tell Flask About the Static Folder:
In your Flask application, you need to tell Flask where to find the static files. This is done by specifying the static_folder parameter when creating the Flask app.
`app = Flask(__name__, static_folder='static')
`

# To Run Application in Local: 
`python app.py`
Access your Flask application in your web browser at http://localhost:5000 by default.


When you're done working on your project, deactivate the virtual environment:
`deactivate`

# Final output
The Resume Webpage is printed and attached as resume.pdf for reference.


