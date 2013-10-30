from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)
    
@app.route("/signup", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        request.form.get("age")
        request.form.get("gender")
        request.form.get("zipcode")
        request.form.get("email")
        request.form.get("password")

if __name__ == "__main__":
    app.run(debug = True)