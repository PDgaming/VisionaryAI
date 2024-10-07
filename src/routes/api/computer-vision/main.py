
# # A very simple Flask Hello World app for you to get started with...

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import base64
# from io import BytesIO
# from PIL import Image
# import requests

# app = Flask(__name__)
# cors = CORS(app)

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#     return response

# @app.route('/')
# def hello():
#     return 'Hello, this a simple python sever made using flask that is running on the web. This server was made to be used as an API, so please use the API.'
# @app.route("/computer-vision", methods=["GET", "POST"])
# def computer_vision():
#     if request.method == "POST":
#         data = request.get_json()
#         image_data = data.get("Image", "")

#         if not image_data:
#             return jsonify({"error": "No image data provided"}), 400

#         # Remove the data URL prefix if present
#         if image_data.startswith('data:image'):
#             image_data = image_data.split(",", 1)[1]

#         # Attempt to decode the base64 data
#         try:
#             image_bytes = base64.b64decode(image_data)
#         except Exception as e:
#                 return jsonify({"error": f"Failed to decode base64 data: {str(e)}"}), 400

#         image = Image.open(BytesIO(image_bytes))

#     else:
#         return jsonify({"Message": "This endpoint only supports POST methods"})


# if __name__ == "__main__":
#     app.run(debug=True)
