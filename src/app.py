import subprocess
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('controls.html')


@app.route("/reboot")
def reboot():
    subprocess.Popen(["sudo", "reboot", "now"])
    return "Rebooting..."
    #return redirect(url_for("index"), 307)