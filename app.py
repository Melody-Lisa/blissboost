import os
from flask import (
    Flask, flash, render_template,
     redirect, request, session, url_for, send_from_directory, abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import (
    generate_password_hash, check_password_hash)
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("profile", user=session["user"]))
    else:
        return render_template('index.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        # check if passwords match
        if request.form.get("password") != request.form.get("confirm_password"):
            flash("Passwords do not match")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", user=session["user"]))
            else:
                # invalid password match
                flash("Invalid username or password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Invalid username or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<user>", methods={"GET", "POST"})
def profile(user):
    # grab session user's username from the db
    user_data = mongo.db.users.find_one(
        {"username": session["user"]})

    if user_data:
        return render_template("profile.html", user=user_data)

    return redirect("login")


def is_valid_image_url(url):
    # List of common image file extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    # Check if the URL ends with a known image file extension
    for extension in image_extensions:
        if url.lower().endswith(extension):
            return True
    
    return False


@app.route("/pics", methods=["POST"])
def pics():
    if 'user' in session:
        user = session['user']
        profile_pic_url = request.form.get('profile_pic_url')

        # Check if the provided URL is not empty and is a valid image URL
        if profile_pic_url:
            # Save the URL to the user's profile
            mongo.db.users.update_one({'username': user}, {"$set": {'profile_pic_url': profile_pic_url}})
            return redirect(url_for("profile", user=user))
        else:
            flash("Please provide a valid image URL")
            return redirect(url_for("profile", user=user))
    else:
        flash("You can't edit this page, please log in.")
        return redirect(url_for("login"))


@app.route('/file/<filename>')
def file(filename):
    if filename:
        file_data = mongo.send_file(filename)
        if file_data:
            return file_data
        else:
            abort(404)  # File not found
    else:
        abort(400)  # Bad request (missing filename)


@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/edit_profile/<user>", methods=["GET", "POST"])
def edit_profile(user):
    # grab session user's username from the db
    logged_in_username = session.get("user")
    
    if logged_in_username:
        if logged_in_username == user:
            if request.method == "POST":
                # Update user details
                edit_data = {
                    "name": request.form.get("name").capitalize(),
                    "dob": request.form.get("dob"),
                    "about": request.form.get("about"),
                }

                # Perform the update operation
                mongo.db.users.update_one({"username": user}, {"$set": edit_data})

                flash("User details updated successfully")
                return redirect(url_for("profile", user=user))

            edit = mongo.db.users.find_one({"username": user})
            if edit:
                return render_template("edit_profile.html", user=edit)
            else:
                flash("User not found")
                return redirect(url_for("home"))
        else:
            flash("You are not authorized to edit this profile")
            return redirect(url_for("home"))
    else:
        flash("You are not signed in")
        return redirect(url_for("login"))


@app.route("/posts")
def posts():
    posts = mongo.db.posts.find()
    return render_template(
        'posts.html', posts=posts)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)