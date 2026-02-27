import httpx
import json
from models import AnalyzeRequest

async def analyze_transcript(request: AnalyzeRequest) -> dict:
    
    # Build user stories text
    stories_text = ""
    for story in request.user_stories:
        stories_text += f"""
        - ID: {story.id}
          Title: {story.title}
          Type: {story.type}
          Acceptance Criteria: {story.acceptance_criteria}
        """

    prompt = f"""
You are a sprint review analyst. Analyze the transcript and map feedback to user stories.

USER STORIES:
{stories_text}

TRANSCRIPT:
{request.transcript}

Return ONLY a valid JSON object with NO extra text, NO markdown, NO backticks. Just raw JSON like this:
{{
  "mapped_feedback": [
    {{
      "story_id": "US-101",
      "story_title": "Dark Mode Toggle",
      "type": "feature",
      "feedback_points": ["toggle is hidden in settings", "flicker when switching themes"],
      "suggested_solution": "Move toggle to nav bar and fix flicker",
      "ai_suggestion": "Use CSS transitions to avoid flicker",
      "priority": "medium"
    }}
  ],
  "unmapped_feedback": [
    "Footer shows wrong copyright year",
    "Page transitions feel abrupt"
  ],
  "minutes_of_meeting": {{
    "date": "2024-01-01",
    "attendees": ["Scrum Master", "Developer", "Client"],
    "summary": "Sprint review covering 3 user stories with feedback on dark mode, payment retry, and dashboard performance",
    "decisions": ["Retry button added", "Lazy loading implemented"],
    "action_items": [
      {{
        "action": "Move dark mode toggle to nav bar",
        "owner": "Developer",
        "story_id": "US-101"
      }}
    ]
  }},
  "sequence_diagram": "sequenceDiagram\\n  User->>App: Opens settings\\n  App->>Backend: Fetch preferences\\n  Backend-->>App: Return theme\\n  App-->>User: Apply theme"
}}

Map ALL feedback from the transcript to the correct user story. 
Anything that does not belong to any user story goes into unmapped_feedback.
"""

    headers = {
        "Api-Key": request.api_key,
        "Content-Type": "application/json"
    }

    body = {
        "temperature": 0,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(request.api_url, headers=headers, json=body)
        response.raise_for_status()
        
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        
        return json.loads(content)
      
        
        
        
        
    #     parsed = json.loads(content)
    
    # # Fix: force type from original user stories
    #     story_type_map = {s.id: s.type for s in request.user_stories}
    #     for item in parsed.get("mapped_feedback", []):
    #         if item["story_id"] in story_type_map:
    #             item["type"] = story_type_map[item["story_id"]]
    
    #     return parsed