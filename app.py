from flask import Flask,render_template,jsonify,request,redirect,url_for
app=Flask(__name__)


@app.route("/form",methods=['GET','POST'])
def form():
    return render_template("form.html")


@app.route("/",methods=['GET'])
def home():
    return "Devesh Working shit"


@app.route("/ok",methods=['GET'])
def ok():
    return "Devesh Working ok"


if __name__  == "__main__":
    app.run(port=4001,debug =True)