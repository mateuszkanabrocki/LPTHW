from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello", methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")


if __name__ == "__main__":
    app.run()














# from flask import Flask
# from flask import render_template
# from flask import request

# app = Flask(__name__)

# @app.route("/hello")
# def index():
#     # if there were no default 'Nobody'
#     # and no name given then name = None
#     name = request.args.get('name', 'Nobody')
#     greet = request.args.get('greet', 'Hello')

#     if name:
#         greeting = f"{greet}, {name}"
#     else:
#         greeting = "Hello World"

#     return render_template("index.html", greeting=greeting)

# if __name__ == "__main__":
#     app.run()


# from flask import Flask
# from flask import render_template
# from flask import request

# app = Flask(__name__)

# @app.route("/hello", methods=['POST', 'GET'])
# def index():
#     greeting = "Hello World"

#     if request.method == "POST":
#         name = request.form['name']
#         greet = request.form['greet']
#         greeting = f"{greet}, {name}"
#         return render_template("index.html", greeting=greeting)
#     else:
#         return render_template("hello_form.html")


# if __name__ == "__main__":
#     app.run()
