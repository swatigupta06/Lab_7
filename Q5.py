
sting=str(input("Enter a string: "))
alphabets=0
digits=0
special=0
upp=0
low=0

s=len(sting)
for i in range(s):
    if sting[i].isalpha():
        alphabets=alphabets+1
        if sting[i].isupper():
            upp=upp+1
        elif sting[i].islower():
            low=low+1
    elif sting[i].isdigit():
        digits=digits+1
    elif sting[i]==" " or sting[i]=="\n" or sting[i]=="\t":
        special=special+1
print(f'Alphabets:{alphabets}')
print(f'Digits:{digits}')
print(f'Special Characters:{special}')
print(f'Upper Case:{upp}')
print(f'Lower Case:{low}')