# import Flask
from flask import Flask

# define the app with the Flask() class
app = Flask(__name__)

# index route
@app.route("/")
# index function
def index():
    return 'Hello world!!!'# return text 'Hello World!!!'

if __name__ == '__main__':
    app.run()# run the app
#go to 127.0.0.1