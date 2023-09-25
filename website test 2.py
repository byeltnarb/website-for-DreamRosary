from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", active_page='home')

@app.route("/rosaries")
def rosaries():
    return render_template("rosaries.html", active_page='rosaries')

@app.route("/baby_pins")
def baby_pins():
    return render_template("baby_pins.html", active_page='baby_pins')

@app.route("/contact")
def contact():
    return render_template("contact.html", active_page='contact')

if __name__ == "__main__":
    app.run(debug=True)