import json
from ast import literal_eval
data = json.load(open('data.json'))

def change_quantity(data, value):
    for k in data.keys():
        if 'quantity' in str(data[k]):
            dict2 = data[k]
            if type(dict2) == list and 'quantity' in str(dict2):
                for i in range(len(dict2)):
                    change_quantity(dict2[i], value)
            else:
                if 'quantity' in dict2.keys():
                    dict2['quantity'] = value*dict2['quantity']/100
                else:
                    change_quantity(dict2, value)
            # print(dict2)
            # print('-----------')
    return None

for value in [23, 50, 260]:
    data = json.load(open('data.json'))
    change_quantity(data, value)
    data = literal_eval(str(data).replace('100gm', str(value)+'gm'))
    with open('data'+ str(value) +'.json', 'w') as outfile:
        json.dump(data, outfile)