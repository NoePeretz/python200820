d = {}
print('Welcome')

while True:
    print('1')
    print('2')
    print('3')
    print('4')
    print('5')
    print('6')
    
    option = input('')
    
    if option == '6'  :
        break
    elif option == '1':
        while True:
            voc = input('')
        while True:
                    voc = input('')
                    if voc == '0':
                        break
                    if voc not in d:
                        voc_ch = input('')
                        d[voc] = voc_ch
                    else:
                        print('')
    elif option == '2':
        s = sorted(d)
        print(s)
        for i in s:
            print(i,':',d[i])
    elif option == '3':
        while True:
            voc == input('')
            if voc in d:
                print('')
