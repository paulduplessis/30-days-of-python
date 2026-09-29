x_int = 10
x_float = 10.4
x_str = "Hello"
x_bool = True
x_complex = 3 + 2j
x_none = None
x_list = [1, 2, 3, 3, 4]
x_tuple = (1, 2, 3, 3, 4)
x_set = {1, 2, 3, 3, 4}
x_dict = {"name": "Paul", "surname": "Du Plessis"}

print(x_int, type(x_int))
print(x_float, type(x_float))
print(x_str, type(x_str))
print(x_bool, type(x_bool))
print(x_complex, type(x_complex))
print(x_none, type(x_none))
print(x_list, type(x_list))
print(x_tuple, type(x_tuple))
print(x_set, type(x_set))   # Should print {1, 2, 3, 4} because duplicates are removed
print(x_dict, type(x_dict))