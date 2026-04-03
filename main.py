import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import analyze_feedback
import uvicorn
from fastapi.responses import HTMLResponse
import pathlib
import traceback
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Customer Feedback Intelligence Agent API")

# Path to the templates directory
TEMPLATES_DIR = pathlib.Path(__file__).parent / "templates"

class FeedbackRequest(BaseModel):
    review: str

class FeedbackResponse(BaseModel):
    response: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    index_path = TEMPLATES_DIR / "index.html"
    if index_path.exists():
        return index_path.read_text()
    return "<h1>Customer Feedback Agent API is active</h1><p>Visit /analyze to use the agent.</p>"

@app.post("/analyze", response_model=FeedbackResponse)
async def analyze_sentiment(request: FeedbackRequest):
    try:
        logger.info(f"Received analysis request for: {request.review[:50]}...")
        # Pass the message to our ADK agent via helper
        agent_response = await analyze_feedback(request.review)
        logger.info("Agent analysis successful.")
        return FeedbackResponse(response=str(agent_response))
    except Exception as e:
        error_trace = traceback.format_exc()
        logger.error(f"Agent analysis failed: {str(e)}\n{error_trace}")
        raise HTTPException(status_code=500, detail=f"Agent analysis failed: {str(e)}")

if __name__ == "__main__":
    # Get port from environment variable for Cloud Run deployment, default to 8080
    port = int(os.environ.get("PORT", 8080))
    # Note: Use 0.0.0.0 for Cloud Run
    uvicorn.run(app, host="0.0.0.0", port=port)
