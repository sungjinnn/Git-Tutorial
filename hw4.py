def rep_char(c,n) :
    print(c*n)

def draw_line_string():
    name = input('input his/her name: ')
    msg1 = f' Hello {name}, '
    msg2 = ' Welcome to seoul. '
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr)
    print(msg1)
    print(msg2)
    rep_char('-',nstr)

draw_line_string()

