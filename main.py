from flask import Flask, redirect, render_template, request

app = Flask(__name__)

data = dict()

@app.route("/")
def main():
    return render_template("main.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        student = dict()
        student["name"] = request.form.get("name")
        student["studentNumber"] = int(request.form.get("studentNumber"))
        student["major"] = request.form.get("major")
        student["email"] = request.form.get("email_id") + request.form.get("email_addr")
        student["gender"] = request.form.get("gender")
        student["language"] = ", ".join(
            request.form.getlist("language")
        )
        data[student["studentNumber"]] = student
        result = [data[key] for key in sorted(data)]
        return render_template("result.html", result=result)
    result = [data[key] for key in sorted(data)]
    return render_template("result.html", result=result)


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


@app.route("/reset", methods=["POST"])
def reset():
    if request.method == "POST":
        data.clear()
        return redirect("/")
    return redirect("/result")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
