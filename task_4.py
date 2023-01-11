from random import randint as r


def formu(k):
    operator = ['-', '+']
    with open('in_1.txt', 'a', encoding='utf-8') as in_1:
        for i in range(k):
            coef = r(0, 10)
            oprIndx = r(0, 1)
            pow = k - i
            skip = False
            if coef != 0:
                in_1.write(str(coef))
                if pow > 1:
                    in_1.write('*x^' + str(pow))
                if pow == 1:
                    in_1.write('*x')
            if coef == 1:
                if pow > 1:
                    in_1.write('x^' + str(pow))
                if pow == 1:
                    in_1.write('x')
            if coef == 0:
                skip = True
            if not skip:
                in_1.write(str(operator[oprIndx]))
        in_1.write(str(r(0, 10)) + '=0\n')


for i in range(2, 9):
    formu(i)