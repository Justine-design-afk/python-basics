# import functions_2
# from builtins import function
import math

import my_package
# import functions_2

# f2.my_function(100, 22.2)
# import functions_2 as f2

# import math
# math.pow(2,2)
# print(math.pow(2,2))

# from oop4 import Employee,PermanentEmployee,ContractEmployee

from my_package import shapes
print(shapes.triangle_area(3,4,5))

from my_package.shapes import triangle_area
print(triangle_area(3,4,5))

print(dir(math))
print(dir(my_package))



