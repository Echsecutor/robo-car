import subprocess
from urllib import request
from flask import Flask, render_template, url_for, redirect, request
from motor import car

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('controls.html')


@app.route("/reboot")
def reboot():
    subprocess.Popen(["sudo", "reboot", "now"])
    return "Rebooting..."


@app.route("/poweroff")
def poweroff():
    subprocess.Popen(["sudo", "poweroff", "now"])
    return "Shutting Down..."


@app.route("/set_motor", methods=['POST'])
def set_motor():
    instructions = request.get_json()

    if not instructions:
        return "No instructions given"
    if "position" not in instructions.keys():
        return "No position given"
    position = instructions["position"]

    if "side" not in instructions.keys():
        return "No side given"
    side = instructions["side"]

    if position not in car.structured_motors().keys():
        return "invalid position: " + position

    if side not in car.structured_motors()[position].keys():
        return "invalid side: " + side

    motor = car.structured_motors()[position][side]

    if "action" not in instructions.keys():
        return "No action given"
    action = instructions["action"]

    if action == "forward":
        motor.forward()
    elif action == "backward":
        motor.backward()
    elif action == "stop":
        motor.stop()
    else:
        return "Unknown action"

    return "Setting motor " + position + " " + side + " to " + action
