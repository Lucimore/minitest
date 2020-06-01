import random

#begin = float(input("Введите первое число\n"))
#end = float(input("Введите второе число\n"))

begin = -10000.0  #Начало. Можно изменить
end = 10000.0  #Конец. Можно изменить

print("""#include <stdio.h>
#include <limits.h>
#include "ft_printf.h"
#include <float.h>

int main(void)
{""")


while begin < end:
#    begin += 0.001
    begin += random.uniform(0.0, 100.0)  # Здесь можно изменять шаг
    p = random.randint(0, 15)  # Точность - рандомное число от 0 до 1000, можно>
    w = random.randint(0, 100)  # Ширина - рандомное число от 0 до 1000, можно >
    begin = float("{:.1f}".format(begin))  # Здесь можно указать точность, если>
#    print(f'ft_printf("%{p}.{w}f\\n", {begin});')
    print(f'ft_printf("%{p}.{w}Lf\\n", (long double){begin});')  # Тест для Lf

print('}')
