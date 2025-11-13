
#endpoint data:
import json
from pathlib import Path


[{"url": "/atbash", "method": "POST", "stats": {"total_requests_received": 12, "avg_handling_time": 10.4}}]



#summery data:
{"highest_requests": { "name": "atbash POST", "number": 17 },
"lowest_requests": { "name": "fence GET", "number": 3 },
"highest_handeling_time": { "name": "caesar POST", "number": 21.7 },
"lowest": { "name": "atbash POST", "number": 7.9 }}


file = Path(__file__)

def save_name(name : str, file_name : str):
    try:
        with open(f'{file.parent}/{file_name}' 'a') as f:
            f.write(f'{name}\n')
        return {'status' : True}
    
    except Exception as e:
        return {'status' : e}


def read_file(file_name : str):
    try:
        with open(f'{file.parent}/{file_name}', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {'status' : e}




def save_data(data : dict, file_name : str):
    try:
        with open(f'{file.parent}/{file_name}', 'w') as f:
            json_data = json.dumps(data, indent=3)
            f.write(json_data)
    
        return {'status' : True}
    
    except Exception as e:
        return {'status' : e}
