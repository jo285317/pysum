import time
def  main():
    numbers = input()
    array = numbers.split(' ')
    _sum = 0
    time.sleep(25)
    for num in array:
        _sum += int(num)
    print(_sum, end='')

main()
