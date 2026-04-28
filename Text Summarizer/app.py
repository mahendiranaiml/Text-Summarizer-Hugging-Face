from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import summarize_dialogue
from fastapi.responses import FileResponse

app = FastAPI()
class InputData(BaseModel):
    dialogue: str

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/summarize")
def summarize_api(data: InputData):
    summary = summarize_dialogue(data.dialogue)

    return {
        "summary": summary
    }