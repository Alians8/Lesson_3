
#Task_1________________________________________________________________________________________________________________________________________

def f(x_1, x_2):
    try:
        x_1, x_2 = int(x_1), int(x_2)
        f_num = x_1 / x_2
    except ValueError:
        return "Ошибка! Нужно ввести именно цифру"
    except ZeroDivisionError:
        return "На ноль делить нельзя! Введите цифру, отличную от нуля"
    return round(f_num, 4)


print(f(input("Введите первую цифру:"), input("Введите вторую цифру")))

#Task_2________________________________________________________________________________________________________________________________________


def people(**kwargs):
    return " ".join(kwargs.values())


print(people(n=input('Введите имя:'), s= input('Теперь введите фамилию:'), b=input('Введите дату рождения:'), c=input('Введите город:'), email=input('Введите адрес эл.почты'), t=input('Введите сотовый телефон:')))




#Task_3________________________________________________________________________________________________________________________________________


def f(n_1, n_2, n_3):
    list = [n_1, n_2, n_3]
    try:
        list.remove(min(list))
        return sum(list)
    except TypeError:
        return "Можно ввести только integer. Повторите попытку."


print(f(117, 34, [6]))











#Task_5__________________________________________________________________________________________________________________



def sum_n():
    s = 0
    while True:
        v_list = input("Введите число, введите 'E' для выхода").split()
        for n in v_list:
            if n == 'E':
                return s
            else:
                try:
                    s+= int(n)
                except ValueError:
                    print('Чтобы выйти, нажмите "E" ')
        print(f"Сумма чисел равна {s}")


print(sum_n())





#Task_4_________________________________________________________________________________________________________________


def f(a, b):
    try:
        x = a ** b
    except TypeError:
        return "Ввести второе число со знаком минус"
    return x


print(f(2, [5]))




#Task_6_________________________________________________________________________________________________________________


def f():
    for word in input('Вести слова на анг-м в нижнем регистре:\n').split():
        x = 0
        for c in word:
            if 97 <= ord(c) <= 122:
                x += 1
        print(word.title() if x == len(word) else f"{word} - маленькими буквами")


f()
