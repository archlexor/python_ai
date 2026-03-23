n = int(input("Enter your number: "))
i = 1
q = int(input(f'Enter the number upto which you want multiple of {i}: '))
while(i <= q):
    result = n * i 
    print(f'{n} * {i} = {result}')
    i = i + 1