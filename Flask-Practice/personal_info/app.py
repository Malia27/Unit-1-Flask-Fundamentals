from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
 return '''<h1>Welcome to the Simple Personal Info app!</h1>
<ul>
    <li><a href="/grade/11">/grade/11</a></li>
    <li><a href="/subject/biology">/subject/science</a></li>
    <li><a href="/schedule?day=friday">/schedule?day=friday</a></li>
</ul>
 '''

@app.route('/grade/<int:year>')
def grade_year(year):
 return f'''
        <ul>
            <li>current grade: {year}</li>
            <li>Science Class:</li>
            <li>Average grade:</li>
            <li>Total # of students:</li>
        </ul>
'''
@app.route('/subject/<subjectname>')
def subject(subjectname):
    return f"Student is currently taking: {subjectname}"

if __name__ == '__main__':
 app.run(debug=True)