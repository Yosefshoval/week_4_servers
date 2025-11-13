import re
from fastapi import FastAPI
import uvicorn
import json



app = FastAPI()



@app.get('/test')
def test():
    return { 'msg': 'hi from test'}




@app.get('/test/{name}')
def save_name(name : str):


    return {'msg': 'saved user'}



@app.post('/caesar')
def Caesar_cipher(body : dict):
    # body like this: Body:{ "text": string, "offset": int, "mode": "encrypt"/”decrypt” }
    if not body.get('mode'):
        pass


    
    if body['mode'] == 'enencrypt':
        return { "encrypted_text": "..." }
    

    elif body['mode'] == 'decrypt':
        return { "decrypted_text": "..." }




@app.get('/fence/encrypt/')
def encrypt(text : str):

    return { "encrypted_text": "..." }




@app.post('/fence/decrypt')
def decrypt(body : dict):

    return { "decrypted": "..." }



@app.get('/endp_data/')
def summery(general : bool = True, url : str | None = None):
    pass






#endpoint data:
[{"url": "/atbash", "method": "POST", "stats": {"total_requests_received": 12, "avg_handling_time": 10.4}}]



#summery data:
{"highest_requests": { "name": "atbash POST", "number": 17 },
"lowest_requests": { "name": "fence GET", "number": 3 },
"highest_handeling_time": { "name": "caesar POST", "number": 21.7 },
"lowest": { "name": "atbash POST", "number": 7.9 }}



abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def enc(txt : str, offset : int, abc):
    if not re.match('^[a-zA-Z ]+$', txt):
        return False
    
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(len(abc))
    new = ''

    for i in range(len(txt)):
        
        
        if txt[i] == ' ':
            ch = txt[i]
        else:
            indx = abc.index(txt[i])
            ch = abc[(indx + offset) % len(abc)]

        new += ch
    
    return new


def decp(txt : str, offset : int, abc):
    if not re.match('^[a-zA-Z ]+$', txt):
        return False

    new = ''
    for i in range(len(txt)):
        if txt[i] == ' ':
            new += ' '
        else:
            new += abc[abc.index(txt[i]) - offset]
    
    return new





    

def rail_fence_cipher(txt : str):
    if not re.match('^[a-zA-Z ]+$', txt):
            return False

    txt = txt.replace(' ', '')
    evens = ''
    odd = ''
    
    for i in range(len(txt)):
        if i % 2 == 0:
            evens += txt[i]
        else:
            odd += txt[i]
        
    enced = evens + odd

    return enced



def de_rail_fence_cipher(txt : str):
    if not re.match('^[a-zA-Z ]+$', txt):
            return False
    
    decrypted = ''

    l = len(txt)
    
    evens = txt[:l // 2]
    print('even: ',evens)
    
    odd = txt[l // 2:]
    print('odd: ',odd)

    for chars in range(len(evens)):
        decrypted += evens[chars] + odd[chars]
    
    print(decrypted)
    

    return decrypted


# 'abcd' = 5
# 4 // 2 == 2 === 'ab'
# 4 + 1 // 2 == 2 === 'de'


# e = rail_fence_cipher('let us meet todayy')
# print('e:', e)
# d = de_rail_fence_cipher(e)
# print('d:', d)

