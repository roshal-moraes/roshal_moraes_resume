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

Create HTML templates for your work experience and education sections. Don't forget to include Bootstrap for styling.

To keep your HTML files in a separate folder and still be able to serve them using Flask, you can make use of the render_template function provided by Flask. This function allows you to render HTML templates located in a separate folder. Here's how you can do it:

Create a folder for your HTML templates. For example, you can create a folder named "templates" in your project directory.

Move your HTML files to the "templates" folder. You can place your index.html and any other HTML templates you want to use in this folder.

Modify your Flask application to use the render_template function to render these HTML templates. You need to specify the template name (without the file extension) when rendering the template.

The render_template function is used to render the index.html template. The index.html file should be located in the "templates" folder.


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


#Step 8: With the virtual environment active, navigate to your project directory and run your Flask application:

bash
Copy code
python app.py
Access your Flask application in your web browser at http://localhost:5000 by default.

Step 8: Deactivate the Virtual Environment

When you're done working on your project, deactivate the virtual environment:
bash
Copy code
deactivate
By following these steps, you can create a Flask project with an SQLite database, populate data from the database, and style it using Bootstrap. This approach allows you to build a resume website with dynamic content.



Flask Routes:

We create a Flask web application using the Flask class and define three routes:
/experience: This route simulates fetching work experience data from a database. In reality, you would replace this with code to query your database and return the appropriate data.
/education: This route simulates fetching education data.
/: The root route for rendering the HTML template.
API Endpoints:

The /experience route returns JSON data containing simulated work experience data. In a real application, you would query a database and return the actual work experience data.
The /education route returns JSON data containing simulated education data.
HTML Template (index.html):

In your HTML template, you structure your resume as you normally would, using HTML and CSS for styling. However, you use Flask's template syntax to insert dynamic data where needed.
In the "Work Experience" section, you have placeholders for the company name, responsibilities, and achievements.
You use Flask's template syntax to populate these placeholders with data fetched from the /experience API endpoint:
{{ experience_data.company }} inserts the company name.
{% for responsibility in experience_data.responsibilities %} and {% for achievement in experience_data.achievements %} are loops that iterate through the lists of responsibilities and achievements and insert them into the HTML list items.
The same template logic applies to the "Education" section to insert data from the /education API endpoint.
Flask Rendering:

In the index route, you use Flask's render_template function to render the index.html template.
When the template is rendered, Flask substitutes the placeholders with the data obtained from the API endpoints, creating a dynamic resume page.
By structuring your Flask application in this way, you can easily update your resume data by modifying the API endpoint logic and leave the HTML structure and rendering process intact. This approach separates data from presentation, making it more maintainable and scalable.