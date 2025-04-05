from src.AI_AGENT_RESUME_SELECTOR.components.entity import projectEntity

import os
import yaml
from agno.agent import Agent, RunResponse
from agno.models.groq import Groq
import json
import re
#api_key = os.environ.get("GROQ_API_KEY")
api_key = os.environ.get("GROQ_API_KEY")
print("-------key",api_key)
path = "params.yaml"
params=yaml.safe_load(open(path))['preprocess']
print("loading YAML",path)

def load_jd(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

agent = Agent(
    name="jobprocessing agent",
    model= Groq(
        id="llama-3.1-8b-instant", 
        api_key = api_key
    ),
    role="loads job requirment",
    description='''You are a recruitment assistant. From a given job description, extract and return a structured JSON like this:

{
  "skills": [...],
  "experience": [...],
  "education": [...],
  "keywords": [...]
}

Do not wrap the response in code blocks or Python variables.
Only return valid JSON.
    ''',
    instructions=["return in json form"
                    ],
    response_model=projectEntity.MyRequirments,
)

txt = load_jd(params['inputJobreq'])
response = agent.run(txt)
print(">>>>>> here is respone >>>",f"data{response.content}")
op = json.loads(response.content)

with open(params['jsonJobReq'], "w") as f:
    print("------",params['jsonJobReq'])
    json.dump(op, f, indent=4)

