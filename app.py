from flask import Flask, jsonify

courses = [
    {"name": "python", "title": "Python Fundamentals", "rating": 4.5, "students": 1200},
    {"name": "flask", "title": "Flask Web Development", "rating": 4.2, "students": 800},
    {"name": "pandas", "title": "Data Analysis with Pandas", "rating": 4.7, "students": 950},
    {"name": "docker", "title": "Docker Essentials", "rating": 3.9, "students": 600},
]

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, welcome to the course</h1>"

@app.route("/about")
def about():
    return "You are Welcome"

@app.route("/courses")
def course_list():
    return """<ul>
                <li> Mathematics </li>
                <li> Physics </li>
                <li> Structures</li>
            </ul>"""

@app.route("/api/courses")
def course_full_list():
    return jsonify(courses)

@app.route("/api/courses/count")
def api_count():
    
    course_count = {}

    for course in courses:
        name = course["name"]
        course_count[name] = course_count.get(name, 0) + 1

    return jsonify(course_count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    