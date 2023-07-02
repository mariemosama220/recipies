import sys
from pyngrok import ngrok
from flask import Flask, request, jsonify
import os
import project_source

from flask import Flask, request, render_template
import requests, os, time
# from azure.cognitiveservices.vision.computervision import ComputerVisionClient
# from msrest.authentication import CognitiveServicesCredentials
# from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
# from dotenv import load_dotenv

# load_dotenv()
# run the imported file
from project_source import *
from project_source import get_similar_recipe
app = Flask(__name__)
# make app config "ENV" = "development" to make the app run in development mode
app.config["ENV"] = "development"
app.config["USE_NGROK"] = True


key = os.getenv("COG_SERVICE_KEY")
region = os.getenv("COG_SERVICE_REGION")
endpoint = os.getenv("ENDPOINT")
COG_endpoint = os.getenv("COG_SERVICE_ENDPOINT")

@app.route('/get-recipe', methods=['POST'])
def get_recipe():


        # Load the values from .env

    json_data = request.get_json()  # Get the JSON data from the request
    print(json_data)

    # test_input = json_data['test_input']  # Extract the required input from the JSON
    # print(test_input)
    result = get_similar_recipe(json_data).to_json()  # Call your function with the input
    print("result", jsonify(result)  )
    return jsonify(result)  # Return the result as a JSON response

if __name__ == '__main__':
    app.run()
