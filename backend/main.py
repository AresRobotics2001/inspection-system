from fastapi import FastAPI, UploadFile, File
from vision.detector import analyze_image

app = FastAPI(title="Inspection System API")

@app.get("/")
def home():
    return {"message": "API funcionando correctamente"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    result = analyze_image(contents)
    return {"result": result}
