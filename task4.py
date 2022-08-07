# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

num = int(input("Please enter value: "))
max_num = 0
while num != 0:
    num_el = num % 10
    if max_num < num_el:
        max_num = num_el
    num = num // 10
print(f"Max digit in value {max_num}")
