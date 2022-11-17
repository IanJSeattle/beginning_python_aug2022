question = 'how old are you? '

invalid = True

while invalid:
    result = input(question)
    if result.isnumeric():
        if int(result) < 0 or int(result) > 120:
            print('please enter a value between 0 and 120!')
            invalid = True
            continue
        elif 
        else:
            invalid = False

