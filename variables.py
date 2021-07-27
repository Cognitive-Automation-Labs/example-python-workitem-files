from RPA.Tables import Tables
from RPA.Robocloud.Items import Items
import os
import json

tables = Tables()
items = Items()
workitem_filename = "data.csv"

with open("./devdata/env.json") as env_in:
    env_file = json.load(env_in)
    for key in env_file:
        os.environ[key] = env_file[key]
