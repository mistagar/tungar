from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Homepage</h1>"

'''@app.route("/posts/<int:id>")
def posts(id):
    return "This is post :" + str(id)'''

@app.route("/posts", methods = ["GET"])
def post():
    return "All posts"

@app.route("/posts/create", methods = ["POST"])
def create():
    return "Post created"

@app.route("/posts/updated/<int:id>", methods = ["PUT"])
def updated(id):
    return f"Post number {id} has been updated!"

@app.route("/posts/delete/<int:id>", methods = ["DELETE"])
def delete(id):
    return f"Post number {id} has been deleted"




if __name__=="__main__":
    app.run(debug = true)