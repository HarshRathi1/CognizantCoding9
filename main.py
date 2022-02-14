'''Chaman planned to choose a four digit lucky number for his car. His lucky numbers are 3,5 and 7. Help him find the number, whose sum is divisible by  3 or 5 or 7. Provide a valid car number, Fails to provide a valid input then display that number is not a valid car number.

Note : The input other than 4 digit positive number[includes negative and 0] is considered as invalid.'''
n=1234
temp=n
sum=0
if n<1000 or n>9999:
    print(n,"is not a valid car number")
else:
    while temp>0:
        sum+=temp%10
        temp=temp//10
    if sum%3==0 or sum%5==0 or sum%7==0:
        print("Lucky number")
    else:
        print("Sorry its not my lucky number")
