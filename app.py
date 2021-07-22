import base64
from fer.fer import top_emotion
from flask import Flask, json, request
from fer import FER
import cv2
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_jsonpify import jsonify, jsonpify
import numpy as np
import numpy as np



app = Flask(__name__)
api = Api(app)
CORS(app)


class head(Resource):
    def get(self):
     return jsonify({"Reply:" : "YEEEEEET"})

class getEmotion(Resource):
    def get(self,url):
        try:
            
            detector = FER()
            img = cv2.imread(url)

            result = detector.detect_emotions(img)
            toReturn = str(result).split('\'emotions\':',1)[1].replace('{','').replace('}','').replace(']','')
            
            
            return jsonify({"Results:": toReturn})
        except Exception as e:
            print(e)
            return jsonify({"result": "No Face Detected"})

api.add_resource(head, '/')
api.add_resource(getEmotion, '/getEmotion/<path:url>')



if __name__ == "__main__":
    app.run(debug=True)

