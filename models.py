# from pydantic import BaseModel
# from typing import List, Optional

# class UserStory(BaseModel):
#     id: str
#     title: str
#     type: str  # feature / bug / task
#     acceptance_criteria: str

# class AnalyzeRequest(BaseModel):
#     user_stories: List[UserStory]
#     transcript: str
#     api_key: str = "AIzaSyDGHap6LzPRKVWxR_qjUVnVw5Let8KG5M8"
#     api_url: str = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

# class MappedFeedback(BaseModel):
#     story_id: str
#     story_title: str
#     type: str
#     feedback_points: List[str]
#     suggested_solution: str
#     ai_suggestion: str
#     priority: str

# class MoMActionItem(BaseModel):
#     action: str
#     owner: str
#     story_id: Optional[str] = None

# class MinutesOfMeeting(BaseModel):
#     date: str
#     attendees: List[str]
#     summary: str
#     decisions: List[str]
#     action_items: List[MoMActionItem]

# class AnalyzeResponse(BaseModel):
#     mapped_feedback: List[MappedFeedback]
#     unmapped_feedback: List[str]
#     minutes_of_meeting: MinutesOfMeeting
#     sequence_diagram: str

import os
from pydantic import BaseModel
from typing import List, Optional

class UserStory(BaseModel):
    id: str
    title: str
    type: str  # feature / bug / task
    acceptance_criteria: str

class AnalyzeRequest(BaseModel):
    user_stories: List[UserStory]
    transcript: str
    api_key: str = os.environ.get("GEMINI_API_KEY", "")
    api_url: str = os.environ.get("GEMINI_API_URL", "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent")

class MappedFeedback(BaseModel):
    story_id: str
    story_title: str
    type: str
    feedback_points: List[str]
    suggested_solution: str
    ai_suggestion: str
    priority: str

class MoMActionItem(BaseModel):
    action: str
    owner: str
    story_id: Optional[str] = None

class MinutesOfMeeting(BaseModel):
    date: str
    attendees: List[str]
    summary: str
    decisions: List[str]
    action_items: List[MoMActionItem]

class AnalyzeResponse(BaseModel):
    mapped_feedback: List[MappedFeedback]
    unmapped_feedback: List[str]
    minutes_of_meeting: MinutesOfMeeting
    sequence_diagram: str