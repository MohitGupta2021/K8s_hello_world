
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Function to fetch content from external service and render it
def get_external_content():
    # Get the data from the incoming request
    data = request.data
    headers = dict(request.headers)
    method = request.method

    # Forward the request to the external service
    external_url = 'http://192.168.49.2:30082'  # Replace with your external URL
    response = requests.request(method, external_url, headers=headers, data=data)

    # Prepare the response data
    content = {
        "status": response.status_code,
        "headers": dict(response.headers),
        "content": response.text
    }

    return content

# Route to render HTML page with external content
@app.route('/')
def render_external_content():
    content = get_external_content()
    # for key,val in content.items():
    #     print("key= ",key )
    #     print("\n")
    # val=content['content']
    # print(val)

    return render_template('external_content.html', content=content)
@app.route('/page')
def render_html():
    content = get_external_content()
    val=content['content']
# #     # HTML content from the JSON response
    html_content = f"""{val}"""
    return html_content
# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
