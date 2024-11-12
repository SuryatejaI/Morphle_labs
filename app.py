import subprocess
from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    name = "Your Full Name"

    # System username
    username = os.getenv('USER', 'unknown')

    # Server time in IST
    server_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')

    # Get the output of the top command
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        top_output = f"Error retrieving top output: {e}"

    # Create the response
    response = f"""
        <h1>System Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <p><strong>Top Output:</strong></p>
        <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
