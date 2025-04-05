import pandas as pd
import os
import yaml

path = "params.yaml"
params=yaml.safe_load(open(path))['preprocess']
print("loading YAML",path)

candidate_colums = ["skills","degree_names","professional_company_names",
            "related_skils_in_job",'start_dates', 'end_dates'
               ]

req_colums=["skills_required","educationaL_requirements",
            "experiencere_requirement"]

data = pd.read_csv(params["input"])
data = data.sample(n=500, random_state=42) 
data.to_csv(params['input'])
print("preprocessing data")
candidates = data[candidate_colums]
candidates= candidates[0:20]
reqs = data[req_colums]
reqs = reqs[0:20]
candidates.to_csv(params['outputcandidate'])
reqs.to_csv(params['outputreq'])
print("----data preprocesse sucessfully----")