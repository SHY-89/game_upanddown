import random

print("Up Down GAME START")
print("---- GAME RULE ----")
print("1. 입력은 1~100까지의 숫자 중 하나만 입력이 가능합니다.")
print("2. 게임을 포기 하시려면 END를 입력해 주시면 강제로 종료합니다.")
print("-------------------")


def check_choice():
    choice = int(input("숫자를 입력 하세요:"))
    while choice < 1 or choice > 100:
        print("GAME RULE 1번을 위배 하였습니다. 다시입력 하세요.")
        choice = int(input("숫자를 입력 하세요:"))
    return choice

def check_game():
    user_select = check_choice()
    result = random.randint(1, 100)
    game_count = 1
    while user_select != result:

        if user_select > result:
            print("DOWN")
        elif user_select < result:
            print("UP")
        user_select = check_choice()
        game_count += 1
    return game_count


count = check_game()
print(f"시도 횟수 : {count} 입니다.")
#check_roof = input("다시 게임을 시작 하시겠 습니까?(y/n)")
