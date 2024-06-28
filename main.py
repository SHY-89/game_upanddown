import random

print("Up Down GAME START")
print("---- GAME RULE ----")
print("1. 입력은 1~100까지의 숫자 중 하나만 입력이 가능합니다.")
print("2. 게임을 포기 하시 려면 10000를 입력해 주시면 강제로 종료합니다.")
print("-------------------")
game_status = True
game_total_count = None


def check_choice():
    global game_status
    choice = int(input("숫자를 입력 하세요:"))
    while choice < 1 or choice > 100:
        if choice == 10000:
            game_status = False
            return choice
        print("GAME RULE 1번을 위배 하였습니다. 다시입력 하세요.")
        choice = int(input("숫자를 입력 하세요:"))
    return choice

def check_game():
    global game_status
    user_select = check_choice()
    result = random.randint(1, 100)
    game_count = 1
    while user_select != result:
        if not game_status:
            return 0
        if user_select > result:
            print("DOWN")
        elif user_select < result:
            print("UP")
        user_select = check_choice()
        game_count += 1
    return game_count


while game_status:
    if game_total_count is not None:
        print(f"게임 진행 중 가장 빠르게 맞춘 횟수는 {game_total_count} 입니다.")
    count = check_game()
    if count == 0:
        break
    print(f"시도 횟수 : {count} 입니다.")
    check_roof = input("다시 게임을 시작 하시겠 습니까?(y/n)")
    if check_roof == "n" or check_roof == "N": game_status = False
    if game_total_count is None:
        game_total_count = count
    elif game_total_count > count:
        game_total_count = count
