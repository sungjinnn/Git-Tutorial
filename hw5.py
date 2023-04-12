def read_single_digit(num):
    digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return digits[num]

def read_number(num):
    read_num = str(num)
    digit = [read_single_digit(int(read_num[0])),read_single_digit(int(read_num[1])),read_single_digit(int(read_num[2]))]
    return ' '.join(digit)

num = input('세자리 정수 입력: ')

if len(num) == 3:
    print(read_number(num))
else:
    print('세자리 정수가 아닙니다.')
