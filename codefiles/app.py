from flask import Flask, render_template, request

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/generate")
def generate():
    user = {
        "name": request.form.get("name", ""),
        "goal": request.form.get("goal", ""),
        "intensity": request.form.get("intensity", ""),
        "age": request.form.get("age", ""),
        "weight": request.form.get("weight", ""),
    }
    return render_template("result.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)