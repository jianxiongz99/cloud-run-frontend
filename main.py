from flask import Flask, request, jsonify, render_template
import requests
import os, socket
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_request', methods=['POST'])
def send_request():
    form_data = request.form
    print("Received form data:", form_data)
    parsed_url = urlparse(form_data.get('url', ''))
    host = parsed_url.hostname
    port = parsed_url.port
    host_info = socket.getaddrinfo(host=host, 
                                   port=port)
    lines = []
    
    lines.append(f"DNS lookup for {host}: " + repr([info[4][0] for info in host_info]))
    print(lines[-1])
    resp = requests.get(parsed_url.geturl(),
                 timeout=5)
    lines.append("---- response from backend ----")
    lines.append(f"Status Code: {resp.status_code}")
    lines.append(f"Response Headers: {resp.headers}")
    lines.append(f"Response Text: {resp.text}...")
    lines.append("---- end of response ----")
    return jsonify({'lines': lines})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 8080))