from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret-key"

users=[]

@app.route("/")
def index():
    return redirect(url_for("signup"))

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        confirm=request.form["confirm"]
        if password!=confirm:
            flash("Passwords do not match!")
            return redirect(url_for("signup"))
        users.append({"name":name,"email":email})
        flash("Signup successful!")
        return render_template("success.html", user=name)
    return render_template("signup.html")

if __name__=="__main__":
    app.run(debug=True)
