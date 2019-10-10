num1 = input('请输入第一个数字')

try:
    num1 = int(num1)
except ValueError:
    print('您输入的不是数字')
else:
    num2 = input('请输入第二个数字')
    try:
        num2 = int(num2)
    except ValueError:
        print('您输入的不是数字')
    else:
        num = num1 + num2
        print('和是' + str(num))
