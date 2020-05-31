import random

#begin = float(input("Введите первое число\n"))
#end = float(input("Введите второе число\n"))

begin = 7.0  #Начало. Можно изменить
end = 8.0  #Конец. Можно изменить

print("""#include <stdio.h>
#include <limits.h>
#include "ft_printf.h"
#include <float.h>

int main(void)
{""")


while begin < end:
    begin += 0.01  # Здесь можно изменять шаг
    p = random.randint(0, 1000)  # Точность - рандомное число от 0 до 1000, можно менять
    w = random.randint(0, 1000)  # Ширина - рандомное число от 0 до 1000, можно менять
    begin = float("{:.2f}".format(begin))  # Здесь можно указать точность, если закомментировать эту строку, будет 16
    print(f'ft_printf("%{p}.{w}f\\n", {begin});')

print('}')
