import re
from fastapi import FastAPI
import uvicorn
import json
import encryption_area.encrypt as cpt
import file_handling.read_and_save as ras





app = FastAPI()



@app.get('/test')
def test():
    return { 'msg': 'hi from test'}




@app.get('/test/name')
def save_name(name : str):
    result = ras.save_name(name, 'names.txt')
    if result['status'] == True:
        return {'msg': 'saved user'}
    return result



@app.post('/caesar')
def Caesar_cipher(body : dict):
    # body like this: Body:{ "text": string, "offset": int, "mode": "encrypt"/”decrypt” }
    if not body.get('mode') or not body.get('offset') or not body.get('text'):
        print('problam')
        return {'problam' : 'not mode, offset or text are given.'}

    if body['mode'] == 'encrypt':
        print('en')
        encrypted_txt = cpt.encrypter(body['text'], body['offset'], cpt.ABC)   

        return { "encrypted_text": encrypted_txt }
    

    elif body['mode'] == 'decrypt':
        decrypted_txt = cpt.decrypter(body['text'], body['offset'], cpt.ABC)

        return { "decrypted_text": decrypted_txt }




@app.get('/fence/encrypt/{text}')
def encrypt(text : str):
    encypted_text = cpt.rail_fence_cipher(text)

    return { "encrypted_text": encypted_text }




@app.post('/fence/decrypt')
def decrypt(body : dict):
    if not body.get('text'):
        return {'problam' : 'not text given.'}
    
    decrypted_text = cpt.de_rail_fence_cipher(body['text'])

    return { "decrypted": decrypted_text }



@app.get('/get_data/')
def summery(general : bool = True, url : str | None = None):
    pass



if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)