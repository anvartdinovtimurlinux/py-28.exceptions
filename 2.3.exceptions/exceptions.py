print('Программа реализует польскую нотацию для двух положительных чисел')
print('Введиnе выражение по образцу: * 13 10')
print('Числа должны быть положительными, а ар. операции +, -, *, /')

while True:

    try:
        op, a, b = input('\nВведите ваше выражение: ').strip().split()
        assert op in ('+', '-', '*', '/')
        a, b = int(a), int(b)

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b
    except AssertionError:
        print('Введена недопустимая операция, попробуйте заново')
    except ZeroDivisionError:
        print('На ноль делить нельзя, попробуйте заново')
    except:
        print('Введите выражение в правильном формате, например: / 9 3')
    else:
        print(f'Ответ: {result}')
        break
