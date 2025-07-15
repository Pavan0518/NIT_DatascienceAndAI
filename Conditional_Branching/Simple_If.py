def friends_in_trouble(j_angry, s_angry):
    return (j_angry & s_angry) | ((not j_angry) & (not s_angry))

print(friends_in_trouble(True, True))
print(friends_in_trouble(True, False))
print(friends_in_trouble(False, True))
print(friends_in_trouble(False, False))