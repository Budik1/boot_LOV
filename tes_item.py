kv = 0
raid = 1
if kv or raid:
    if kv:
        if raid:
            print('test ok,kv and raid')
        else:
            print('test ok, kv')
    elif raid:
        print('test ok, raid')

else:
    if kv:
        print('kv')
    elif raid:
        print('raid')
    else:
        print('Test No')

veles_collect = 250 * 8 + 200 * 11 + 100 * 16 + 50 * 19
print(veles_collect)
