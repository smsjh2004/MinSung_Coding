import random
import time

w=["League OF Legends", "Hearthstone", "Teamfight Tactics", "Eternal Return", "GTFO", "BACK 4 BLOOD", "Overwatch", "Minecraft", "Tom Clancy's Rainbow Six Siege", "Don't Starve Together", "STARCRAFT", "DLMAX RESPECT", "SuddenAttack"]
n=1
print("[타자 게임] 준비되면 Enter")
input()
start = time.time()

q=random.choice(w)
while n <=5:
    print("--문제", n, "--")
    print(q)
    x=input()
    if q == x:
        print("성공")
        n=n+1
        q=random.choice(w)
    else:
        print("그걸 틀리네 ㅋㅋ")

end = time.time()
et = end - start
et = format(et, ".2f")
print("타자 시간: ",et,"초")
