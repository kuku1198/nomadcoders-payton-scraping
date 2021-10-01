from flask import Flask

app = Flask("SuperScrapper")


@app.route("/")
def home():
    return "Hello World!"


@app.route("/contact")
def contact():
    return "Contact Me!"


app.run()
