
def my_split(string, char=" "):
    res = []
    current_string = []
    for c in string:
        if c != char: 
            current_string.append(c)
        else:
            res.append(''.join(current_string))
            current_string = []
    res.append(''.join(current_string))

    return res

def presentation(name):
    return f"Je me présente, {name} à votre service !"