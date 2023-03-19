def get_integer(prompt):
    res = int(input(prompt))
    return res

def exchange(money):
    FH = money // 500
    money %= 500
    OH = money // 100
    money %= 100
    FT = money // 50
    money %= 50
    T = money // 10
    print('500원 동전의 개수: ', FH)
    print('100원 동전의 개수: ', OH)
    print('50원 동전의 개수: ', FT)
    print('10원 동전의 개수: ', T)

money = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(money)
