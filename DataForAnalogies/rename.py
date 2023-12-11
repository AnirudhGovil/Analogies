# Rename a bunch of ,csv files
#%%
import glob
import os

for file in glob.glob("*.csv"):
    # Only keep the part after Education2.xlsx -
    # this is the part that will be used to name the jsonl file
    new_name = file.split("Education2.xlsx - ")[1]
    # Save the file under the new name
    os.rename(file, new_name)
# %%
