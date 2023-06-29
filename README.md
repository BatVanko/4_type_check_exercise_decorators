# 4_type_check_exercise_decorators
Create a decorator called type_check. It should receive a type (int/float/str/…), and it should check if the parameter passed to the decorated function is of the type given to the decorator. If it is, execute the function and return the result, otherwise return "Bad Type".

Test Code
@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

Output
4
Bad Type

