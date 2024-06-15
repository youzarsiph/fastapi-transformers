""" FastAPI Microservice """

from fastapi import FastAPI
from transformers import pipeline


# App
app = FastAPI()

# Phi3 Mini 128K Instruct model
model = pipeline(
    task="text-generation",
    model="microsoft/Phi-3-mini-128k-instruct",
    trust_remote_code=True,
)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint"""

    return {"details": "Phi3 FastAPI AI microservice using HuggingFace Transformers"}
