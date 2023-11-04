import sqlite3



def get_work_experience_id_by_company(company):
    conn = sqlite3.connect('resume.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM work_experience WHERE company = ?', (company,))
    data = cursor.fetchone()
    print(data)

    conn.close()
    
    if data:
        return data[0]

    else:
        return None

def insert_responsibility(company, responsibility, details):
    work_experience_id = get_work_experience_id_by_company(company)

    if work_experience_id is not None:
        conn = sqlite3.connect('resume.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO responsibilities (work_experience_id, responsibility, details) VALUES (?, ?, ?)', (work_experience_id, responsibility, details))

        conn.commit()
        conn.close()

def insert_achievement(company, achievement):
    work_experience_id = get_work_experience_id_by_company(company)

    if work_experience_id is not None:
        conn = sqlite3.connect('resume.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO key_achievements (work_experience_id, achievement) VALUES (?, ?)', (work_experience_id, achievement))

        conn.commit()
        conn.close()


def create_database():
    conn = sqlite3.connect('resume.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS work_experience (
            id INTEGER PRIMARY KEY,
            company TEXT,
            title TEXT,
            skills TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responsibilities (
            id INTEGER PRIMARY KEY,
            work_experience_id INTEGER,
            responsibility TEXT,
            details TEXT,
            FOREIGN KEY (work_experience_id) REFERENCES work_experience (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS key_achievements (
            id INTEGER PRIMARY KEY,
            work_experience_id INTEGER,
            achievement TEXT,
            FOREIGN KEY (work_experience_id) REFERENCES work_experience (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS education (
            id INTEGER PRIMARY KEY,
            university TEXT,
            degree TEXT,
            specialization TEXT,
            year_of_graduation TEXT,
            score TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY,
            achievement TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO work_experience (company, title, skills)
        VALUES (?, ?, ?)
    ''', ('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'SYSTEMS ENGINEER', 'Database Management (MSSQL), PLSQL, Python Programming, Kafka, Data Integration, Cross-Functional Collaboration, Agile Project Management (Azure DevOps), Data Quality Assurance'))

    conn.commit()
    insert_responsibility('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Data Masking for GDPR Compliance', 'Led the development of a Data Masking Application to ensure GDPR compliance, overseeing intricate MSSQL servers, schemas, procedures, indexes, and views. Implemented data masking strategies to protect sensitive information while maintaining data usability. Created Power BI reports to monitor performance and activity related to the masked data to analyse correctness and precision of masking applied to data and to analyse correctness and precision of masking applied to data.')

    insert_responsibility('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Kafka Consumer Solution', 'Engineered a Kafka Consumer solution, through integration with Mainframe data storage. Streamlined data ingestion processes, enhancing data availability and real-time analytics capabilities.')
    insert_responsibility('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Data Preparation and Integration', 'Utilized Python to optimize data preparation tasks, ensuring seamless integration with Datacebo and improving overall data quality. Implemented data wrangling techniques to create clean and structured datasets for analysis. Python backend development to connect to application database and frontend screens. Designed user-friendly APIs for test data provisioning and usage statistics, enhancing usability and efficiency for project teams. Facilitated efficient data access and reporting for testing purposes.')

    insert_responsibility('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Azure DevOps and Agile Project Management', 'Managed Azure DevOps repositories and pipelines, leveraging Azure Boards for agile project management. Implemented efficient development processes, enabling improved project tracking and collaboration.')

    insert_responsibility('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Cross-Functional Collaboration', 'Collaborated cross-functionally with various teams, including data engineers, business analysts, and project managers, to ensure the seamless flow of data and the successful execution of projects. Fostered effective communication and cooperation to achieve project goals.')

    insert_achievement('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Successfully developed and deployed a Data Masking Application for GDPR compliance, safeguarding sensitive data while maintaining usability.')

    insert_achievement('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Engineered a Kafka Consumer solution, reducing data provisioning time by 50%, resulting in substantial operational efficiency gains.')
    insert_achievement('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Collaborated cross-functionally to ensure the seamless flow of data, contributing to the success of multiple projects.')

    insert_achievement('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Developed Power BI reports for real-time performance and activity monitoring of masked data, contributing to data governance.')
    insert_achievement('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Optimized data preparation with Python, improving data quality and integration capabilities for Datacebo.')
    insert_achievement('TATA CONSULTANCY SERVICES (BFSI Domain, Belgium)', 'Collaborated cross-functionally to ensure the seamless flow of data, contributing to the success of multiple projects.')

    cursor.execute('''
        INSERT INTO achievements (achievement)
        VALUES (?)
    ''', ('Microsoft Certified: Power BI Data Analyst',))

    cursor.execute('''
        INSERT INTO achievements (achievement)
        VALUES (?)
    ''', ('Microsoft Certified: Azure Fundamentals and Azure Data Fundamentals',))

    cursor.execute('''
        INSERT INTO achievements (achievement)
        VALUES (?)
    ''', ('Completed Machine Learning course from Stanford University - Coursera',))

    cursor.execute('''
        INSERT INTO achievements (achievement)
        VALUES (?)
    ''', ('NPTEL Elite + Gold Certified in Database Management System',))

    cursor.execute('''
        INSERT INTO achievements (achievement)
        VALUES (?)
    ''', ('Completed Python Specialization from University of Michigan - Coursera',))

    cursor.execute('''
        INSERT INTO achievements (achievement)
        VALUES (?)
    ''', ('Presented "Personality Assessment Using Social Media for Hiring Candidates" at the 2020 3rd International Conference on Communication System, Computing and IT Applications (CSCITA)',))

    cursor.execute('''
        INSERT INTO education (university, degree, specialization, year_of_graduation, score)
        VALUES (?, ?, ?, ?, ?)
    ''', ('St. Francis Institute of Technology', 'Bachelor of Engineering', 'Computer Science', '2020', '9.62 CGPA'))

    

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
