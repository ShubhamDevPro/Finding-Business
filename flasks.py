import subprocess
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    subprocess.Popen(["python", "mainpg.py"])
    return "Tkinter application is running!"
if __name__ == "__main__":
    app.run(debug=True,port=2004)

