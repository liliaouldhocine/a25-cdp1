# assert express, expression 

def add(a, b):
    assert isinstance(a, int) and isinstance(b, int), 'A et/ou B ne sont pas un int'
    return a + b

print(add(1, "2"))