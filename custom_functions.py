# def greet():
#     print("skrrrr!")



# def greeting(name):
#     print(f"hello {name}")

# greeting('justine')
# greeting('juma')

# def volume_cylinder(radius,height):
#    v=22/7*radius**2*height
#    print(round(v,2))
#
# volume_cylinder(12,21   )
# volume_cylinder(10,14)
#
# def volume_cylinder_better(radius,height):
#     v=22/7*radius**2*height
#     return v
# result=volume_cylinder_better(12,21 )
# print(result)
#
# with open("volume.txt","w") as file:
#     file.write(str(result))

# def volume_surface(radius,height):
#     v=22/7*radius**2*height
#     a=22/7*radius**2*2 +22/7*radius*2*height
#     return v,a
# volume,area=volume_surface(7,17)
# print(f"volume is{volume} area is{area}")
#
#  # name
# v,a=volume_surface(21,12)

def divide(a,b,should_round:bool=False):
    res= a/b
    if should_round== True:
        return round(res,2)
    else:
        return res


print(divide(9,5,True))










 #calling our functions == use no arguments / parameters == data
