def type_check(type_of):
    def decorator(func):
        def wrapper(num):
            if not isinstance(num, type_of):
                return "Bad Type"
            return func(num)
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

