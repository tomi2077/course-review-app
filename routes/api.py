from flask import Blueprint, jsonify, request
from data import courses

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/courses")
def course_full_list():
    return jsonify(courses)

@api.route("/courses/count")
def api_count():
    return {"count": len(courses)}

@api.route("/courses/top")
def api_top():
    return jsonify([c for c in courses if c["rating"] > 4.0])

@api.route("/course/<name>")
def course_detail(name):
    for course in courses:
        if course["name"] == name:
            return jsonify(course)
    return jsonify({"error": "Course not found"}), 404

@api.route("/course/<name>/rating")
def course_rating(name):
    for course in courses:
        if course["name"] == name:
            return jsonify({"name":course["name"], "rating":course["rating"]})
            
    return jsonify({"error": "Course not found"}), 404

@api.route("/courses/search")
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
