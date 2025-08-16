def argss(name="hello"):
    print(f"name is {name}")
argss("joker")       # default values
def arf(*ars):
    return sum(ars)
print(arf(1,2,3,4,5,6))
def k_ar(**kwarg):
    for i,j in kwarg.items():
        print(j)
k_ar(name="hello",age="43")        
        