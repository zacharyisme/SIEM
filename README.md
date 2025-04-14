# Classify API Service

This FastAPI project provides an endpoint to classify Jira tickets using OpenAI GPT-4.

## Endpoint

**POST** `/classify_ticket`

### Request Body
```json
{
  "summary": "User cannot access VPN",
  "description": "The VPN client throws error 807 when trying to connect from home."
}
```

### Response
```json
{
  "category": "Network Issue"
}
```

## Usage

1. Set your OpenAI API key in the environment:
   ```bash
   export OPENAI_API_KEY=your_api_key
   ```

2. Run locally:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Or use Docker:
   ```bash
   docker build -t classify-api .
   docker run -e OPENAI_API_KEY=your_api_key -p 8000:8000 classify-api
   ```

## Notes
- Make sure to use `model=gpt-4` in production for best results.
- The prompt logic is modular in `app/prompt.py`.
