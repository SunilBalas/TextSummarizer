# app.py
from flask import Flask, request, Response, render_template, jsonify
from TextSummarizer.constants import TRAIN_COMMAND
from TextSummarizer.pipeline.prediction import PredictionPipeline
from TextSummarizer.logging import logger
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/train", methods=["GET"])
def train():
    try:
        os.system(TRAIN_COMMAND)
        return Response("Training Successful !!")
    except Exception as ex:
        return Response(f"Error Occurred: {ex}")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        text = request.form.get("text")
        logger.info(f"Requested Text: {text}")
        obj = PredictionPipeline()
        result = obj.predict(text)
        result = str(result).replace('<n>', '')
        logger.info(f"Summarized Text: {result}")
        return jsonify({"text": result})
    except Exception as ex:
        return jsonify(str(ex))

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=8080, 
        debug=True
    )
