import json
from pathlib import Path


STATE = [{"url": str, "method": str, "stats": {"total_requests_received": 0, "avg_handling_time": 0}}]

#summery data:
SUMMERY = {"highest_requests": { "name": str, "number": int },
"lowest_requests": { "name": str, "number": int },
"highest_handeling_time": { "name": str, "number": int },
"lowest": { "name": str, "number": int }}


file = Path(__file__)

def save_name(name : str, file_name : str):
    try:
        with open(f'{file.parent.parent}/{file_name}', 'a') as f:
            f.write(f'{name}\n')
        return {'status' : True}
    
    except Exception as e:
        return {'status' : str(e)}


def read_file(file_name : str):
    try:
        with open(f'{file.parent}/data/{file_name}', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {'status' : e}




def save_data(data : list, file_name : str):
    try:
        with open(f'{file.parent}/data/{file_name}', 'w') as f:
            json_data = json.dumps(data, indent=3)
            f.write(json_data)
    
        return {'status' : True}
    
    except Exception as e:
        return {'status' : e}
