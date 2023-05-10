#사용자 정의 함수부
def buy(lst):
    print('[구입]')
    product = input('상품명은? ')
    if product == '':
        return False
    else:
        quantity = int(input('수량은? '))
        lst[product] = quantity
        print(f'장바구니에 {product} {quantity}개가 담겼습니다.')
        print()

def show(lst):
    print(f'\n>>> 장바구니 보기: {lst}')
    print()

def find(lst):
    print('[검색]')
    search = input('장바구니에서 찾고자 하는 상품은? ')
    if search in lst:
        print(f'{search}은(는) {lst[search]}개 담겨있습니다.')
    else:
        print(f'장바구니에 {search}은(는) 없습니다.')
    

#주 프로그램부
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)





