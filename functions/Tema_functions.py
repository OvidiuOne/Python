# #Exercitiu 1:



#
# def sum_num(*args, **kwargs):
#     sum = 0
#     for arg in args:
#         if type(arg) in [int, float]:
#             sum += arg
#     for value in kwargs.items():
#         if type(value) in [int, float]:
#             sum += value
#     print(f"The sum of the numbers is {sum}")
#     return sum
#
# sum_num (1, 5, -3, 'abc', [12, 56, 'cad'])
# sum_num ()
# sum_num (2, 4, 'abc', param_1=2)



# #Exercitiu 2:
#
# def n_sum(n, all_nums=[], even_nums=[], odd_nums=[]):
#     if n == 0:
#         all_sum = sum(all_nums)
#         even_sum = sum(even_nums)
#         odd_sum = sum(odd_nums)
#         return (all_sum, even_sum, odd_sum)
#     else:
#         all_nums.append(n)
#         if n % 2 == 0:
#             even_nums.append(n)
#         else:
#             odd_nums.append(n)
#         return n_sum(n-1, all_nums, even_nums, odd_nums)
#
# n = 10
# all_sum, even_sum, odd_sum = n_sum(n)
# print("Sum of all numbers from 0 to 10:", all_sum)
# print("Sum of even numbers from 0 to 10:", even_sum)
# print("Sum of odd numbers from 0 to 10:", odd_sum)



# # Exercitiu 3:

# # Varianta 1

# def read_integer_from_keyboard():
#     try:
#         value = int(input("Enter an integer value: "))
#         return value
#     except ValueError:
#         return 0
#
# print("The number is::", read_integer_from_keyboard())

## Varianta 2


# def read_integer_from_keyboard():
#     while True:
#         try:
#             value = int(input("Enter an integer value: "))
#             print(f"The number is: {value}")
#         except ValueError:
#             print("0")
#
# read_integer_from_keyboard()
