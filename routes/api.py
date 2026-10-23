from flask import Blueprint, jsonify, request
from data import courses, reviews, average_rating

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/courses")
def course_full_list():
    return jsonify([{**c, "rating": average_rating(c["name"])} for c in courses])

@api.route("/courses/count")
def api_count():
    return {"count": len(courses)}

@api.route("/courses/top")
def api_top():
    top = []
    for c in courses:
        avg = average_rating(c["name"])
        if avg is not None and avg > 4.0:
            top.append({**c, "rating": avg})
    return jsonify(top)

@api.route("/course/<name>")
def course_detail(name):
    for course in courses:
        if course["name"] == name:
            return jsonify({**course, "rating": average_rating(name)})
    return jsonify({"error": "Course not found"}), 404

@api.route("/course/<name>/rating")
def course_rating(name):
    for course in courses:
        if course["name"] == name:
            return jsonify({"name":course["name"], "rating": average_rating(name)})
            
    return jsonify({"error": "Course not found"}), 404

@api.route("/courses/search")
def search_courses():
    min_rating = request.args.get("min_rating", type=float)
    max_students = request.args.get("max_students", type=int)
    q = request.args.get("q", type=str)

    results = [{**c, "rating": average_rating(c["name"])} for c in courses]

    if min_rating is not None:
        results = [c for c in results if c["rating"] is not None and c["rating"] >= min_rating]
    if max_students is not None:
        results = [c for c in results if c["students"] <= max_students]
    if q is not None:
        results = [c for c in results if q.lower() in c["title"].lower()]

    return jsonify(results)

@api.route("/courses/<name>/reviews")
def course_reviews(name):
    if not any(c["name"] == name for c in courses):
        return jsonify({"error": "Course not found"}), 404
    course_review = [review for review in reviews if review["course_name"] == name]
    return jsonify(course_review)