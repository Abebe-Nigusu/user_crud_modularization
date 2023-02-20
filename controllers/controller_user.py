from flask_app.models.model_user import User
from flask import render_template, request, redirect, session

from flask_app import app
from flask_app.models.model_user import User

@app.route("/")
def index():
    all_users = User.get_all()
    return render_template("index.html", all_users=all_users)

@app.route('/users/new')
def display_form():
    return render_template("display_form.html")


@app.route('/users/create', methods=["POST"])
def create():
    user = User.create(request.form)
    return redirect("/")


@app.route('/users/get_one/<int:id>')
def get_one(id):
    data = {
        "id": id
    }
    return render_template("show_user.html", user=User.get_one(data))


@app.route('/users/update/<int:id>', methods=["POST"])
def update(id):
    User.update(request.form)
    # return redirect('/')
    return redirect("/")


@app.route('/users/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user=User.get_one(data))


@app.route('/users/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)





























