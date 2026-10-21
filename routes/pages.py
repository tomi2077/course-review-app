from flask import Blueprint, render_template, request, redirect, url_for
import requests
from data import courses

pages = Blueprint("pages", __name__)

@pages.route("/")
def home():
    return render_template("home.html")
@pages.route ("/courses")
def course_list():
    return render_template("courses.html", courses=courses)

@pages.route("/course-page/<name>")
def course_page(name):
    for course in courses:
        if course["name"] == name:
            return render_template("course.html", course=course)
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

        for course in courses:
            if course["name"] == name:
                course["rating"] = rating
                return redirect(url_for("pages.course_list"))

        return render_template("add_review.html", error="No course with that name"), 404

    return render_template("add_review.html")