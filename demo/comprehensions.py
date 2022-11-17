some_list = [1,2,3,4,5,6]

things = {}
for item in some_list:
    things[item] = item ** 2

things = {item: item ** 2 for item in some_list}

print(things)
