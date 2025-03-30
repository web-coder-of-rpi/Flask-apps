# import Flask
from flask import Flask

#define app varible
app = Flask(__name__)

# index
@app.route("/hello/<name>")# route /hello/<name> means that <name> is a varible
def hello(name):#function hello
    return f'Hello, {name}'# return Hello name

#run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
    #go to 127.0.0.1/hello/YOUR_NAME