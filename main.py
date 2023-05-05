from flask import Flask, redirect, render_template, request

app = Flask(__name__)

data = dict()


@app.route("/delete", methods=["POST", "GET"])
def delete():
    if request.method == "POST":
        studentNumber = request.form.getlist("studentNumber")
        for studentNumber in studentNumber:
            del data[int(studentNumber)]
        result = [data[key] for key in sorted(data)]
        return render_template("result.html", result=result)
    return redirect("/result")


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        return redirect("/")
    return redirect("/result")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
