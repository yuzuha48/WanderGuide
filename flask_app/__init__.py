from flask import Flask 
import os

app = Flask(__name__) 
app.secret_key = "secret"

# Define where we're going to store our uploaded files
app.config["UPLOAD_DIR"] = os.path.join(app.instance_path, "uploads")

# Make sure that the upload path exist
os.makedirs(app.config["UPLOAD_DIR"], exist_ok=True)