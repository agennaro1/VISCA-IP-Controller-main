
# Python program to update
# JSON
 
 
import json
#preset_levels = dict()

f = open("ptz_settings.json")
data = json.load(f)

for i in data["CAMERAS"]:
    print(i)

f.close()



# function to add to JSON
def write_json(new_data, filename='ptz_sttings.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["CAMERAS"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
 
#read_ptz_set()