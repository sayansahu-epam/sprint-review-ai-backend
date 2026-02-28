from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import AnalyzeRequest, AnalyzeResponse
from analyzer import analyze_transcript
from mangum import Mangum

app = FastAPI(title="Sprint Review AI Backend", description="AI-powered sprint review analysis API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    
    return {"status": "ok", "message": "Sprint Review AI Backend - v2.0 Deployed via CI/CD!"}




@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    try:
        result = await analyze_transcript(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
handler = Mangum(app)