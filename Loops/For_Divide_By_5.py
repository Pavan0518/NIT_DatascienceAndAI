for i in range(1, 51):
    if i % 5 == 0:
        print(i, 'can divide by 5.')
    else:
        print(i, 'cannot divide by 5.')
        
print('----------------------------------')
        
for i in range(1, 31):
    if i % 3 == 0:
        print(i, 'can divide by 3.')
    else:
        print(i, 'cannot divide by 3.')
        
print('----------------------------------')
        
for i in range(1, 31):
    if i % 3 != 0:
        print(i, 'cannot divide by 3.')
        

print('----------------------------------')
       
for i in range(1, 31):
    if i % 5 != 0:
        print(i, 'cannot divide by 5.')
        
        
print('----------------------------------')

for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
    
print('----------------------------------')

for i in range(1, 11):
    if i == 6:
        break
    print(i)
    
print('----------------------------------')

for i in range(1, 11):
    if i == 6:
        continue
    print(i)