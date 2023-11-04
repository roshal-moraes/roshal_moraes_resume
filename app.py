from flask import Flask, render_template, jsonify
import sqlite3
#from database import create_database

app = Flask(__name__)

#create_database()



# Define your API endpoints
@app.route('/experience')
def get_experience():
    conn = sqlite3.connect('resume.db')
    cursor = conn.cursor()
     # Fetch all work experiences
    cursor.execute("SELECT * FROM work_experience")
    work_experience_data = cursor.fetchall()

    work_experiences = []

    for work_experience in work_experience_data:
        work_experience_id = work_experience[0]

        # Fetch responsibilities associated with each work experience
        cursor.execute("SELECT responsibility, details FROM responsibilities WHERE work_experience_id = ?", (work_experience_id,))
        responsibilities_data = cursor.fetchall()
        responsibilities = [{"responsibility": item[0], "details": item[1]} for item in responsibilities_data]
        print(responsibilities)


        # Fetch achievements associated with each work experience
        cursor.execute("SELECT achievement FROM key_achievements WHERE work_experience_id = ?", (work_experience_id,))
        key_achievements_data = cursor.fetchall()
        key_achievements = [item[0] for item in key_achievements_data]
        print(key_achievements)
        response = {
            'company': work_experience[1],
            'title': work_experience[2],
            'responsibilities': responsibilities,
            'achievements': key_achievements,
            'skills_used': work_experience[3].split(', ')
        }
        print(response)
        work_experiences.append(response)

    conn.close()
    print(work_experiences)
    return work_experiences
    # Pass the work experiences to the template
   


def get_education():
    conn = sqlite3.connect('resume.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM education')
    data = cursor.fetchone()
    conn.close()
    response = {
        "university": data[1],
        "degree": data[2],
        "specialization": data[3],
        "year_of_graduation": data[4],
        "score": data[5]
    }
    return response

@app.route('/achievements')
def get_achievements():
    conn = sqlite3.connect('resume.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM achievements')
    achievements_data = cursor.fetchall()
    achievements = [achievement[1] for achievement in achievements_data]
    conn.close()
    return achievements

# Render the HTML templates
@app.route('/')
def index():
    print(get_experience())
    return render_template('index.html',  static_folder='static', experience_data_set=get_experience(), education = get_education(), achievements =  get_achievements())
if __name__ == '__main__':
    app.run(debug=True)