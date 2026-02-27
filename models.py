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
    api_key: str = "dial-u10g43vnsunzhpkde182z738jli"
    api_url: str = "https://ai-proxy.lab.epam.com/openai/deployments/gpt-4o-mini-2024-07-18/chat/completions?api-version=2024-02-01"

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