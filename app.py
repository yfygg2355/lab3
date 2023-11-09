import os
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

my_skills = [
    "HTML",
    "CSS",
    "JavaScript",
    "Python",
    "Flask",
    "Bootstrap",
]
@app.route('/')
def index():
    current_time = datetime.now()
    return render_template('base.html', os=os, request=request, current_time=current_time)
@app.route('/page1')
def page1():
    current_time = datetime.now()
    return render_template('page1.html', os=os, request=request, current_time=current_time)

@app.route('/page2')
def page2():
    current_time = datetime.now()
    return render_template('page2.html', os=os, request=request, current_time=current_time)

@app.route('/page3')
def page3():
    current_time = datetime.now()
    return render_template('page3.html', os=os, request=request, current_time=current_time)

# Динамічний маршрут для навичок
@app.route('/skills/<int:id>')
def show_skill(id):
    if 0 <= id < len(my_skills):
        skill = my_skills[id]
        return f"Skill {id}: {skill}"
    return "Skill not found"

@app.route('/skills')
def show_all_skills():
    total_skills = len(my_skills)
    skills_list = "<ul>"
    for id, skill in enumerate(my_skills):
        skills_list += f"<li>Skill {id}: {skill}</li>"
    skills_list += "</ul>"
    return f"Total Skills: {total_skills}<br>{skills_list}"

if __name__ == '__main__':
    app.run(debug=True)
