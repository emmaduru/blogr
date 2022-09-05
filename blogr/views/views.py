from flask import render_template
from blogr.models.post import Post
from blogr import app

@app.route("/", methods=["GET"])
@app.route("/posts", methods=["GET"])
def index():
    posts = Post.query.all()
    return render_template("post/index.html", posts=posts)

