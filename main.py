from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Name(BaseModel):
    name: str

# Sample data for demonstration
marks_data = {
    "X": 10,
    "Y": 20,
    "Z": 30
}

@app.get("/api")
def get_marks(names: List[str]):
    marks = [marks_data.get(name, 0) for name in names]
    return {"marks": marks}

