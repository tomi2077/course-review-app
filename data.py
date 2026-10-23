courses = [
    {"name": "python", "title": "Python Fundamentals", "students": 1200},
    {"name": "flask", "title": "Flask Web Development", "students": 800},
    {"name": "pandas", "title": "Data Analysis with Pandas", "students": 950},
    {"name": "docker", "title": "Docker Essentials", "students": 600}
]

reviews = [
    {"course_name": "python", "rating": 4.8, "comment": "Great introduction"},
    {"course_name": "python", "rating": 4.2, "comment": "A bit fast in places"},
    {"course_name": "python", "rating": 4.6, "comment": "Clear explanations throughout"},
    {"course_name": "flask", "rating": 4.0, "comment": "Solid but dated"},
    {"course_name": "flask", "rating": 4.4, "comment": "Good practical examples"},
    {"course_name": "pandas", "rating": 4.9, "comment": "Best course on the topic"},
]

def average_rating(course_name):
    course_review_list = [review for review in reviews if review["course_name"] == course_name]
    if len(course_review_list) == 0:
        return None
    total_rating_value = sum(review["rating"] for review in course_review_list)
    average_rating_value = total_rating_value / len(course_review_list)
    return round(average_rating_value, 1)
