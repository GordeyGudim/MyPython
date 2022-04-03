import random
def orel_reshka(vibros = random.choice(range(1,3))):
    n = int(input())
    if n == vibros:
        return 'you win'
    else:
        print('You not win')
        return orel_reshka()
print(orel_reshka())