#%% imports
import json
import os
import pandas as pd
import random

#%% Read the .csv file
for file in os.listdir():
    if file.endswith(".csv"):
        df = pd.read_csv(file)
        # Create a jsonl file with the same name as the .csv file
        jsonl_file = file.split(".")[0] + ".jsonl"
        with open(jsonl_file, "w") as f:
            # Iterate over the rows of the dataframe
            for index, row in df.iterrows():
                dict = {}
                # The first 2 columns are the Question
                dict["stem"]=[row[0],row[1]]
                # The next 2 columns are the correct answer
                dict["answer"]=[row[2],row[3]]
                # The rest of the columns are the distractors
                dict["choice"]=[]
                for i in range(2,df.shape[1],2):
                    dict["choice"].append([row[i],row[i+1]])
                # Shuffle the list
                random.shuffle(dict["choice"])
                # Add a parameter to the dictionary describing the source file
                dict["prefix"] = file.split(".")[0]
                # Add the dictionary to the jsonl file in a new line
                json.dump(dict, f)
                f.write("\n")

# %%
