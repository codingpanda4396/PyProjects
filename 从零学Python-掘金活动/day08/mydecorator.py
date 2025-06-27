import functools
def decorator_prime(func_name):
    
    @functools.wraps(func_name)
    def before(num):
        """前置输出信息"""
        print("%s是不是素数？"%num)
        return func_name(num)
    return before



@decorator_prime
def is_prime(num):
    if num<2:
        return False
    isPrime=True
    center=int(num/2)
    i=2
    while i<=center:
        if num%i==0:
            isPrime=False
            break
        i+=1
    return isPrime 

if __name__=="__main__":
    while True:
        # 接收一个整数
        input_number = input('请输入一个整数（输入q退出）：')
        if input_number == 'q':
            break
        # 素数判断结果
        result = is_prime(int(input_number))
        # 打印输出
        if result:
            print(input_number + '是素数')
        else:
            print(input_number + '不是素数')