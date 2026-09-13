from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_file = Path("templates/index.html")
    return html_file.read_text(encoding="utf-8")