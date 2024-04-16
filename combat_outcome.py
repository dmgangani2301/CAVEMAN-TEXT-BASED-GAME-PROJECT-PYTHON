import random
def combat_outcome (difficulty, bonus):
    combat_score = random.randint (1, 10)
    weapon_score = combat_score + bonus
    if weapon_score > difficulty: 
        return True
    else: return False

print (combat_outcome(5, 2))