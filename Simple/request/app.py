from flask import Flask, render_template, request #import all

app = Flask(__name__)#flask class

#main route
@app.route("/", methods=["GET", "POST"])#index route methods are get and post
def index():
    if request.method == "POST":#if the user made a post form
        name = request.form['name']#get the contents if the html form
        return f'Hello, {name}!!!<a href="/">Reload</a>'#return the users name
    return render_template("index.html")#else, return the main page
if __name__ == "__main__":
    app.run(debug=True)#run the app