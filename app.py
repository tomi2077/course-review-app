from flask import Flask, jsonify, request

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
    return {"count": len(courses)}

@app.route("/api/courses/top")
def api_top():
    return [c for c in courses if c["rating"] > 4.0]

@app.route("/course/<name>")
def course_detail(name):
    for course in courses:
        if course["name"] == name:
            return jsonify(course)
    return jsonify({"error": "Course not found"}), 404

@app.route("/course/<name>/rating")
def course_rating(name):
    for course in courses:
        if course["name"] == name:
            return jsonify({"name":course["name"], "rating":course["rating"]})
            
    return jsonify({"error": "Course not found"}), 404

@app.route("/api/courses/search")
def search_courses():
    min_rating = request.args.get("min_rating", type=float)
    max_students = request.args.get("max_students", type=int)
    q = request.args.get("q", type=str)
    results = courses
    if min_rating is not None:
        results = [c for c in results if c["rating"] >= min_rating]
    if max_students is not None:
        results = [c for c in results if c["students"] <= max_students]
    if q is not None:
        results = [c for c in results if q.lower() in c["title"].lower()]
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    