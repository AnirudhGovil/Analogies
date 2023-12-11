# Concatenate all the json files into one
#%% imports
import os

#%% Create a jsonl file called "merged.jsonl"
with open("merged.jsonl", "w") as f:
    # Iterate over the files in the current directory
    for file in os.listdir():
        # If the file is a jsonl file except the merged.jsonl file
        if file.endswith(".jsonl") and file != "merged.jsonl":
            # Open the file
            with open(file, "r") as f2:
                # Iterate over the lines of the file
                for line in f2:
                    # Write the line to the merged.jsonl file
                    f.write(line)


# %%
