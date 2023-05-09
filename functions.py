
def hello_world():
    print("Hello, world!")

def hello_world_name(first_name):
    print(f"Hello,{first_name}!")


def hello_world_args(*args):
    firts_name = args [0]
    second_name = args[1]
    third_name = args [2]
   
    print (f"Hello, {firts_name}/ {second_name}/ {third_name} !")
    
def hello_worlds_keywords_args(FP,SP):
    print((f"hello,{FP}/{SP}"))

 
 
def hello_world_arbitary_keyword_args(**kwargs):
    print(kwargs)     
    print(kwargs.get('SP'))
    print(kwargs.get('FP'))
    if kwargs.get('SP') is None:
        print('No hay una segunda persona')
    else:
        print(f"Hello, {kwargs['FP']}/{kwargs['SP']}!")
    print(type(kwargs))



    #print ("Hello, come here!")
    
#hello_world()
#hello_world_name("Bianka")
#hello_world_args("J", "F", "M")
#hello_worlds_keywords_args(FP= "J", SP="F"){#para no estar adivinado con los argumentos anteriores}
#hello_world_arbitary_keyword_args(FP= "J")
#hello_world_arbitary_keyword_args(FP= "J", SP= "F")