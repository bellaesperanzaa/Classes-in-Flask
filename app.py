from flask import Flask, render_template, request,url_for
app = Flask(__name__)

# A dictionary of UserProfiles
# key: username
user_dictionary = {}

#TODO: Add lname to the UserProfile class. Include it in the constructor!
class UserProfile:
    def __init__(self, fname, lname, email, age):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.age = age

    def __str__(self):
        return "I am " + self.fname


@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        age = request.form["age"]
        email = request.form["email"]
        phone = request.form["phone"]
        user = UserProfile(fname, lname, email, age)
        user_dictionary[username]= user
        #etc.
         
        # TODO: Create a UserProfile for the user
        # and store them in the user_dictionary
        # be sure to use the username as the key
        # and the UserProfile as the value

    return render_template("create_profile.html", 
                           users = user_dictionary,
                           url=url_for("signup"))


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=80)