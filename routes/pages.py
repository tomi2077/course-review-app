from flask import Blueprint, render_template, request, redirect, url_for
import requests
from data import courses, reviews, average_rating

pages = Blueprint("pages", __name__)

@pages.route("/")
def home():
    return render_template("home.html")

@pages.route("/courses")
def course_list():
    rows = [{**c, "rating": average_rating(c["name"])} for c in courses]
    return render_template("courses.html", courses=rows)

@pages.route("/course-page/<name>")
def course_page(name):
    for course in courses:
        if course["name"] == name:
            course_reviews = [review for review in reviews if review["course_name"] == name]
            average_rating_value = average_rating(name)
            return render_template("course.html", course=course, reviews=course_reviews, av_rating=average_rating_value)
    return render_template("404.html"), 404

@pages.route("/tip")
def learning_tip():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke",timeout=5)
        response.raise_for_status()
        data = response.json()
        return render_template("tip.html", tip=data)
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Joke API failed: {e}")
        return render_template("error.html"), 503

@pages.route("/add-review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        name = request.form.get("course_name")
        rating = request.form.get("rating", type=float)
        comment = request.form.get("comment")
        if not comment:
            return render_template("add_review.html", error="Comment is required"), 400
        if not any(c["name"] == name for c in courses):
            return render_template("add_review.html", error="No course with that name"), 404
        if rating is None:
            return render_template("add_review.html", error="Rating must be a number"), 400
        reviews.append({"course_name": name, "rating": rating, "comment": comment})
        return redirect(url_for("pages.course_list"))
    return render_template("add_review.html")