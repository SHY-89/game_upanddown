import random

print("Up Down GAME START")
print("---- GAME RULE ----")
print("1. 입력은 1~100까지의 숫자 중 하나만 입력이 가능합니다.")
print("-------------------")

choice = int(input("숫자를 입력 하세요:"))
result = random.randint(1, 100)
game_count = 1
while choice != result:

    if choice > result:
        print("DOWN")
    elif choice < result:
        print("UP")
    choice = int(input("숫자를 입력 하세요:"))
    game_count += 1

print(f"시도 횟수 : {game_count} 입니다.")