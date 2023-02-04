def kill_monsters(health, monsters, damage):
    hits = (monsters - 1) // 3
    health_a = health - hits * damage
    return f'hits: {hits}, damage: {hits * damage}, health: {health_a}' if health_a > 0 else "hero died"


print(kill_monsters(100, 4, 33))
#hits: 1, damage: 33, health: 67

'''Description
You are Saitama (a.k.a One Punch Man), and you are fighting against the monsters!
You are strong enough to kill them with one punch, but after you punch 3 times, 
one of the remaining monsters will hit you once.
Your health is health; number of monsters is monsters, damage that monster can give you is damage.

Task
Write a function that will calculate:
how many hits you received, how much damage you received and your remaining health.
if your health is <= 0, you die and function should return "hero died".'''
