import os
from flask import Flask, render_template

app = Flask(__name__, static_folder=".", static_url_path="/static", template_folder=".")


@app.route("/")
def inicio():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
