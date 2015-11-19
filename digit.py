"""Diginity problem"""
def change_digit():
    """change num to digit"""
    while True:
        num, ans = input(), 0
        if num == '0':
            break
        while int(num) >= 10:
            for i in num:
                ans += int(i)
            num = str(ans)
            ans = 0
        print(num)
change_digit()
