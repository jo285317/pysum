def  main():
    numbers = input()
    array = numbers.split(' ')
    _sum = 0
    for num in array:
        _sum += int(num)
    print(_sum)

main()
