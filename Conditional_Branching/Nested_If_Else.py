age = int(input('Please enter your age. '))
membership = input('Please enter you have membership or not.(Yes/No) ')

isMember = True if membership.lower() == 'yes' else False

if age >= 60:
    if isMember:
        print(r'30% senior member discount.')
    else: print(r'20% senior non member discount.')
else: print('Not elegible for discount.')