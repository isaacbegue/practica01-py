def segment_display(str):
    l1 =''
    l2 =''
    l3 =''
    l4 =''
    l5 =''
    ch1 = '#   '
    ch2 = '  # '
    ch3 = '# # '
    ch4 = '### '
    for n in str:
        if n == '1':
            l1 += ch2
            l2 += ch2
            l3 += ch2
            l4 += ch2
            l5 += ch2
        elif n in ['2','3','5','6','7','8','9','0']:
            l1 += ch4
            if n in ['2','3','7']:
                l2 += ch2
            elif n in ['5','6']:
                l2 += ch1
            else:
                l2 += ch3
            if n == '7':
                l3 += ch2
            elif n == '0':
                l3 += ch3
            else:
                l3 += ch4
            if n in ['3','5','7','9']:
                l4 += ch2
            elif n == '2':
                l4 += ch1
            elif n in ['0','6','8']:
                l4 += ch3
            else:
                l4 += ch2
            if n == '7':
                l5 += ch2
            else:
                l5 += ch4
        elif n == '4':
            l1 += ch3
            l2 += ch3
            l3 += ch4
            l4 += ch2
            l5 += ch2
        else:
            print('Favor de ingresar un número natural.')
            return
    print(l1,l2,l3,l4,l5,sep='\n',end='')
    
str = input('Ingresa un número natural: ')
segment_display(str)