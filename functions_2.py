def add(a, b, c):
    res = a + b + c
    return res


def addition(*nums):
    """
    returns sum of all the numbers passed as arguments
    parameters:
    integers or floats or a mix of integers and floats
    returns:
    integer or float
    """
    total = sum(nums)
    return total
addition(1,2,3)

def build_profile(**kwargs):
    for k,w in kwargs.items():
        print(k,w)



# build_profile(expirience="35",name="jane",age="19",yob="1994")

def fancy(name,*nums,**kwargs):
    print(name)
    print(nums)
    print(kwargs)

# call your function
# print(add(7,9,5))
# print(addition(4,5,8,9,10,3,2,7,9))


# anonymus/lamda functions
# def square(num):
#     return num*num
#
# result=square(5)
# print(result)

square=lambda num:num*num

print(square(5))
res=square(7)
print(res)
surface_area=lambda r,h:22/7*r**2*2+22/7*r*h

print(surface_area(9,14))

people=[
    {"name":"alex","age":35},
    {"name":"maria","age":30},
    {"name":"charlie","age":40},
]
# lambda x:x ['age']
sorted_by_age=sorted(people, key=lambda x:x["age"],reverse=True)
print(sorted_by_age)
