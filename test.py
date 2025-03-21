first_number = 12
second_number = 7

# result = first_number + second_number
# result = first_number - second_number
# result = first_number * second_number
# result = first_number / second_number
# result = first_number ** second_number
result = first_number % second_number

# print(first_number + second_number)
# print(result)
# print(type(result))
# print(round(result, 2))
print("{:,}".format(result).replace("," , "."))

# operando con strings (cadenas)

first_str = "Hola"
second_str = " "
third_str = "mundo"

print(first_str + second_str + third_str)
print(third_str[0:3]*5)

odd_numbers = [1,3,5,7,9]
even_numbers = [2,4,6,8,10]

# result = zip(odd_numbers, even_numbers)
# result = map(sum, zip(odd_numbers, even_numbers))
result = list(map(sum, zip(odd_numbers, even_numbers)))

for element in result:
    print(element)

print(result)