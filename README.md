# AI Hackathon Agent: Customer Feedback Intelligence

This agent is built using the **Google Agent Development Kit (ADK)** and **Gemini 1.5 Flash**. It analyzes customer reviews, determines sentiment, provides a summary, and suggests a professional response.

## Quick Start (Local)

1.  **Install dependencies**:
    ```bash
    uv sync
    ```
2.  **Set Environment Variables**:
    Create a `.env` file with:
    ```env
    GOOGLE_CLOUD_PROJECT=prismatic-smoke-405207
    ```
3.  **Run the service**:
    ```bash
    uv run python main.py
    ```
4.  **Test the endpoint**:
    ```bash
    curl -X POST http://localhost:8080/analyze \
         -H "Content-Type: application/json" \
         -d '{"review": "The product is amazing, but the customer service was a bit slow."}'
    ```

## Cloud Run Deployment

To deploy this agent to Google Cloud Run, run the following command in your terminal:

```bash
gcloud run deploy hackathon-feedback-agent \
    --source . \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars GOOGLE_CLOUD_PROJECT=prismatic-smoke-405207
```

## How it works

The agent uses the ADK `Agent` class wrapper around `gemini-1.5-flash`. The logic is defined in `agent.py` and served via a FastAPI API in `main.py`.
The Dockerfile uses `uv` for efficient dependency management and lightweight container build.
