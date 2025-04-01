#import Flask and render_template
from flask import Flask, render_template

#define flask app
app = Flask(__name__)

#index route
@app.route("/")
def index():
    return render_template('index.html')#return the template index.html

if __name__ == '__main__':
    app.run(debug=True)#run the app
#go to 127.0.0.1:5000/