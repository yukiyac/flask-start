from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/hiraizumi")
def hello_hiraizumi():
    return "Hello Hiraizumiヽ(*´∀｀*)ﾉ"


@app.route("/user/<name>")
def heyName(name):
    return name
# http://127.0.0.1:5001/user/Yukiya


@app.route("/user/age/<age>")
def heyAge(age):
    return age
# http://127.0.0.1:5001/age/Age


@app.route("/user/<name>/<age>")
def heyNage(name, age):
    return name + age
# http://127.0.0.1:5001/Name/Age


# from flask import render_template
@app.route("/html")
def html():
    # return "<h1>Hello HTMLです</h1>"
    return render_template("index.html")


# @app.route("/html/<name>")
# def htmlName(name):
    # return render_template("name.html", name=name)


@app.route("/html/<aaa>")
def htmlName(aaa):
    return render_template("name.html", bbb=aaa)


@app.route("/html/age/<age>")
def htmlAge(age):
    return render_template("age.html", htmlAge=age)


# @app.route("/query")
# def query():
    # search_text = request.args.get("search_text")
    # if search_text is not None:
    #   return search_text
    # else:
    #   return ""


@app.route("/query")
def query():
    BBB = request.args.get("AAA")
    if AAA is not None:
        return BBB
    else:
        return ""
# http://127.0.0.1:5001/query?AAA=XXX


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
