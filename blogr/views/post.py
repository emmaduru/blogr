from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_required, current_user
from blogr import db
from blogr.forms.post import PostCreationForm, PostEditForm
from blogr.forms.comment import CommentCreationForm
from blogr.models.post import Post
from blogr.models.comment import Comment

post = Blueprint("post", __name__)

@post.route("/create", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostCreationForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("post/create_post.html", form=form)

@post.route("/<int:post_id>", methods=["GET"])
def post_detail(post_id):
    form = CommentCreationForm()
    post = Post.query.filter_by(id=post_id).first_or_404()
    return render_template("post/post_detail.html", post=post, form=form)

@post.route("/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    form = PostEditForm()
    post = Post.query.filter_by(id=post_id).first_or_404()
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("index"))
    form.title.data = post.title
    form.body.data = post.body
    return render_template("post/edit_post.html", form=form)

@post.route("/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("index")) 

@post.route("/<int:post_id>/comment", methods=["POST"])
@login_required
def create_comment(post_id):
    form = CommentCreationForm()
    if form.validate_on_submit():
        post = Post.query.filter_by(id=post_id).first_or_404()
        comment = Comment(body=form.body.data, post_id=post.id, author_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for("post.post_detail", post_id=post_id))

@post.route("/<int:post_id>/comment/<int:comment_id>", methods=["POST"])
@login_required
def delete_comment(post_id, comment_id):
    comment = Comment.query.filter_by(id=comment_id).first_or_404()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("post.post_detail", post_id=post_id))