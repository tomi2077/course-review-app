from flask import Flask, jsonify, request, render_template
from routes.pages import pages
from routes.api import api

app = Flask(__name__)
app.register_blueprint(pages)
app.register_blueprint(api)

@app.errorhandler(404)
def not_found(e):
    if request.path.startswith("/api/"):
        return jsonify({"error": "Not found"}), 404
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    