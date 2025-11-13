import re


ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypter(txt : str, offset : int, abc : list):
    if not re.match('^[a-zA-Z ]+$', txt):
        return False
    
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


def decrypter(txt : str, offset : int, abc : list):
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

    l = len(txt) - 1
    
    evens = txt[:(l // 2) + 1]
    
    odd = txt[(l // 2) + 1:]

    for chars in range(len(odd)):
        decrypted += evens[chars] + odd[chars]
    
    if len(odd) < len(evens):
        decrypted += evens[-1]  

    return decrypted

