from pydantic import BaseModel,ValidationError

class MyRequirments(BaseModel):
    skills: list
    experience:list
    education:list
    keywords:list

class Candidate(BaseModel):
    skills: list
    experience:list
    education:list
    company:list

class Selection(BaseModel):
    candidate:Candidate