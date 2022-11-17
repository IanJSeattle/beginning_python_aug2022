bread = True
eggs = False

if bread:
    msg = 'i got a loaf of bread'
    print(msg)
    if eggs:
        print('\n'.join([msg for i in range(11)]))
