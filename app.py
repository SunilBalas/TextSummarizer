from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from TextSummarizer.constants import TRAIN_COMMAND
from TextSummarizer.pipeline.prediction import PredictionPipeline

import uvicorn
import sys
import os

text: str = "What is Text Summarization ?"

app = FastAPI()

@app.get("/", tags=["authorization"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train():
    try:
        os.system(TRAIN_COMMAND)
        return Response("Training Successful !!")
    except Exception as ex:
        return Response(f"Error Occurred: {ex}")

@app.post("/predict")
async def predict(text):
    try:
        obj = PredictionPipeline()
        result = obj.predict(text)
        return result
    except Exception as ex:
        raise ex

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8080
    )