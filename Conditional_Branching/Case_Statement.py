num = int(input('Please enter a number. '))

match num:
    case 1 : print('You entered the number {}'.format(num))
    case 2 : print('You entered the number {}'.format(num))
    case 3 : print('You entered the number {}'.format(num))
    case _ : print('You entered the number other than 1, 2 and 3.')