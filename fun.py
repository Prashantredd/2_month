def argss(name="hello"):
    print(f"name is {name}")
argss("joker")       # default values
def arf(*ars):  # here the name we can assign
    return sum(ars)
print(arf(1,2,3,4,5,6))
def k_ar(**kwarg):  # here the name we can assign key values both in this
    for i,j in kwarg.items():
        print(j)
k_ar(name="hello",age="43")        
import math
import random
print(math.sqrt(36))
print(random.randint(1,20))
def auto():
    print("world!@")
if __name__=="__main__":
    auto()
        


        