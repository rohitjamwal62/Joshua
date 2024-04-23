listb = [['pair:$band/usdt', 'entry:1.4612-1.54-1.605'], ['pair:$jack/usdt', 'entry:5.4612-5.54-5.605'], ['pair:$mask/usdt', 'entry:5-5.2-5.32']]
lista = ['pair:$mask/usdt', 'entry:5-5.2-5.32']

def match_lists(lista, listb):
    for sublist in listb:
        if sublist == lista:
            return True
    return False

result = match_lists(lista, listb)
print("Matching sublist found:", result)
