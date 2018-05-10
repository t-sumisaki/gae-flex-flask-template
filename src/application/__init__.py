from flask import Flask, render_template


app = Flask('application')



@app.route('/')
def root():
    return render_template('default.html')