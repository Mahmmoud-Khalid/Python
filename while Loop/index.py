""" 
    ============================================================
        By Solo_Learn <3
    ============================================================
    You are making a game! The player tries to shoot an object and can hit or miss it.
    The player starts with 100 points, with a hit adding 10 points to the player's score,
    and a miss deducting 20 points.

    Your program needs to take 4 action results as input ("hit" or "miss"),
    calculate and output the player's remaining points.

    Sample Input
    hit
    hit
    miss
    hit

    Sample Output
    110

    Explanation: 3 hits add 30 points, one miss deducts 20, making the total points equal to 110.

"""

health = 100
n_actions = 0

while n_actions <= 3:

    score = input("")
    if score == "hit":
        health += 10
    elif score == "miss":
        health -= 20
    else:
        continue
    n_actions += 1
    
print(health)