shopping_bag = {}
print('[구입]')

while True:
    item = input('상품명? ')
    if item == '':
        break
    quantity = int(input('수량은? '))
    shopping_bag[item] = quantity
    
    print(f'장바구니에 {item} {quantity}개가 담겼습니다.')
    print()
   
print(f'\n>>> 장바구니 보기: {shopping_bag}')
print('\n[검색]')

while True:
    search_item = input('장바구니에서 확인하고자하는 상품은? ')
    if search_item in shopping_bag:
        print(f'{search_item}은(는) {shopping_bag[search_item]}개 담겨있습니다.')
        break
    else:
        print('해당 상품은 존재하지 않습니다.')
