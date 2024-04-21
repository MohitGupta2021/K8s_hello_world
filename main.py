# # # from flask import Flask, request, jsonify
# # # import requests

# # # app = Flask(__name__)

# # # # Define the endpoint to receive HTTP requests
# # # @app.route('/forward', methods=['GET', 'POST'])
# # # def forward_request():
# # #     # Get the data from the incoming request
# # #     data = request.data
# # #     headers = dict(request.headers)
# # #     method = request.method

# # #     # Forward the request to the external service
# # #     external_url = 'http://192.168.49.2:30476'  # Replace with your external URL
# # #     response = requests.request(method, external_url, headers=headers, data=data)

# # #     # Return the response from the external service
# # #     return jsonify(
# # #         status=response.status_code,
# # #         headers=dict(response.headers),
# # #         content=response.text
# # #     )

# # # # Run the Flask application
# # # if __name__ == '__main__':
# # #     app.run(host='0.0.0.0', port=5000)
# # from flask import Flask, render_template

# # app = Flask(__name__)

# # # Route to render the HTML content
# # @app.route('/')
# # def render_html():
# #     # HTML content from the JSON response
# #     html_content = """
# #         <html>
# #         <head>
# #             <meta charset="utf-8">
# #             <meta http-equiv="X-UA-Compatible" content="IE=edge">
# #             <meta name="description" content="A simple docker helloworld example.">
# #             <meta name="author" content="Karthik Gaekwad">
# #             <meta name="viewport" content="width=device-width, initial-scale=1">

# #             <!-- Latest compiled and minified CSS -->
# #             <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

# #             <script type="text/javascript">
# #                 function init() {
# #                     timeDisplay = document.createTextNode("");
# #                     document.getElementById("clock").appendChild(timeDisplay);
# #                 }

# #                 function updateVisit() {
# #                     visitDisplay = document.createTextNode("");
# #                     document.getElementById("visits").appendChild(visitDisplay);

# #                     var counter = Cookies.get('counter');
# #                     if (counter == null) {
# #                         counter = 1;
# #                     } else {
# #                         counter = Number(counter) + 1;
# #                     }
# #                     Cookies.set('counter', counter);
# #                     document.getElementById("visits").firstChild.nodeValue = counter;
# #                 }

# #                 function updateClock() {
# #                     var currentTime = new Date();

# #                     var currentHours = currentTime.getHours();
# #                     var currentMinutes = currentTime.getMinutes();
# #                     var currentSeconds = currentTime.getSeconds();

# #                     // Pad the minutes and seconds with leading zeros, if required
# #                     currentMinutes = (currentMinutes < 10 ? "0" : "") + currentMinutes;
# #                     currentSeconds = (currentSeconds < 10 ? "0" : "") + currentSeconds;

# #                     // Choose either "AM" or "PM" as appropriate
# #                     var timeOfDay = (currentHours < 12) ? "AM" : "PM";

# #                     // Convert the hours component to 12-hour format if needed
# #                     currentHours = (currentHours > 12) ? currentHours - 12 : currentHours;

# #                     // Convert an hours component of "0" to "12"
# #                     currentHours = (currentHours == 0) ? 12 : currentHours;

# #                     // Compose the string for display
# #                     var currentTimeString = currentHours + ":" + currentMinutes + ":" + currentSeconds + " " + timeOfDay;

# #                     // Update the time display
# #                     document.getElementById("clock").firstChild.nodeValue = currentTimeString;
# #                 }
# #             </script>
# #         </head>
# #         <body onload="updateVisit(); updateClock(); setInterval('updateClock()', 1000 )">
# #             <!-- Fixed navbar -->
# #             <nav class="navbar navbar-inverse navbar-fixed-top">
# #                 <div class="container">
# #                     <div class="navbar-header">
# #                         <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
# #                             <span class="sr-only">Toggle navigation</span>
# #                             <span class="icon-bar"></span>
# #                             <span class="icon-bar"></span>
# #                             <span class="icon-bar"></span>
# #                         </button>
# #                         <a class="navbar-brand" href="#">Docker Helloworld</a>
# #                     </div>
# #                     <div id="navbar" class="navbar-collapse collapse">
# #                         <ul class="nav navbar-nav">
# #                             <li class="active"><a href="#">Home</a></li>
# #                             <li><a href="https://github.com/karthequian/docker-helloworld">About</a></li>
# #                             <li><a href="https://twitter.com/iteration1">Contact</a></li>
# #                         </ul>
# #                     </div><!--/.nav-collapse -->
# #                 </div>
# #             </nav>

# #             <div class="container theme-showcase" role="main">

# #                 <!-- Main jumbotron for a primary marketing message or call to action -->
# #                 <div class="jumbotron">
# #                     <h1>Hello</h1>
# #                     <p>Is it me you're looking for?</p>
# #                 </div>
# #                 <hr/>
# #                 <div class="footer">
# #                     <p>2021 Karthik Gaekwad, Visits: <span id="visits"></span>, <span id="clock"></span></p>
# #                     <div title="The container ID is the ID of the container (or host) that is the helloworld application.">Container ID: helloworld-5d6cdd4b4f-zk26s
# #                     </div>
# #                 </div>
# #             </div> <!-- /container -->
# #         </div>
# #         <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
# #         <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
# #         <script src="https://cdnjs.cloudflare.com/ajax/libs/js-cookie/2.1.1/js.cookie.min.js"></script>
# #         <!-- Latest compiled and minified JavaScript -->
# #         <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
# #         </body>
# #         </html>
# #     """

# #     return html_content

# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=5000)



# from flask import Flask, render_template
# import requests

# app = Flask(__name__)

# # Function to fetch content from external service and render it
# # Function to fetch content from external service and render it
# def get_external_content():
#     external_url = 'http://192.168.49.2:30476'  # Replace with your external URL
#     response = requests.get(external_url)
    
#     # Check if the response is successful
#     if response.ok:
#         try:
#             content = response.json()
#         except json.decoder.JSONDecodeError:
#             # If JSON parsing fails, return the raw text content
#             content = {
#                 "status": response.status_code,
#                 "headers": dict(response.headers),
#                 "content": response.text
#             }
#     else:
#         # If the response is not successful, return an empty content
#         content = {
#             "status": response.status_code,
#             "headers": dict(response.headers),
#             "content": ""
#         }

#     return content

# # Route to render HTML page with external content
# @app.route('/')
# def render_external_content():
#     content = get_external_content()

#     return render_template('external_content.html', content=content)

# # Run the Flask application
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

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
    external_url = 'http://192.168.49.2:30862'  # Replace with your external URL
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
    app.run(host='0.0.0.0', port=5001)
