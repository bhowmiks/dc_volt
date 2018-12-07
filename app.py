from flask import Flask, request, jsonify, json, abort,session,render_template,flash,redirect, url_for, send_from_directory, send_file
import numpy as np
import pandas as pd
import os



app = Flask(__name__)
app.secret_key = os.urandom(12)
new_data = False

@app.route('/')
def home():

    return "Hello I-jet"







# run the application
if __name__ == "__main__":

    #app.config['SESSION_TYPE'] = 'filesystem'
    print(app.secret_key)
    app.run(debug=True)

