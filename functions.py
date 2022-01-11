# parametro por defecto: person 

def hello(name = "person"):
    print('hello world')

def add(one, two):
    return one + two

print(add(1+2))

hello()

# funciones lambda 

subs = lambda one, two : one - two
print(subs(1+2))
