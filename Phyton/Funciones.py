hp = 100
def take_damage (damage):
    global hp
    hp = hp - damage
    print (f"hp: {hp}")
    return hp 

take_damage(20)


