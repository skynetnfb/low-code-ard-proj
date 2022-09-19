
# Python program to demonstrate
# Conversion of JSON data to
# dictionary
 
 
# importing the module
import json
import re

def json_reader(file_name='json_test.txt'):
# Opening JSON file
    with open(file_name) as f:
        data = f.read().replace("\\","/").replace('""','"')
    print("Data type before reconstruction : ", type(data))
    # reconstructing the data as a dictionary
    js = json.loads(data,strict=False)
  
    print("Data type after reconstruction : ", type(js))
    print(js)



json_reader('json_test.txt')