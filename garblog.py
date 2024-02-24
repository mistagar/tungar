from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Homepage</h1>"

@app.route("/posts")
def post():
    posts ={
        "1": "First Post",
        "2": "Second Post",
        "3": "Third Posts"
    }
    return jsonify(posts)


@app.route("/posts/<int:id>", methods=["GET"])
def posts(id):
    return "This is post :" + str(id)

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