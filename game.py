def main():
    while True:
        print()
        print("=== МЕНЮ ===")
        print("1-Начать")
        print("2-Правила")
        print("0-Выход")
        choice=read_choice("Выберите пункт: ",["0", "1", "2"])
        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "0":
            print("Выход из программы")
            break
def read_choice(prompt, allowed):
    while True:
        choice=input(prompt)
        if choice in allowed:
            return choice
        else:
            print("Ошибка. Выберите один из доступных вариантов")
            return choice
def show_rules():
    print()
    print("=== ПРАВИЛА ИГРЫ ===")
    print("Код состоит из 3 цифр")
    print("У вас есть 5 попыток")
    print("После каждой попытки показывается кол-во цифр на своих местах")
    print("3 совпадения - победа, после 5 неудач поражение")
def read_code():
    while True:
        code=input("Введите код из 3 цифр: ")
        if len(code)==3 and code.isdigit():
            return code
        print("Код должен быть из 3 цифр")
def count_matches(secret,guess):
    matches=0
    for i in range(3):
        if secret[i]==guess[i]:
            matches+=1
    return matches
def is_open(matches):
    if matches==3:
        return True
    else:
        return False
def play_game():
    secret="427"
    attempts=5
    print()
    print("=== СЕЙФ ЕКЕБ ===")
    print("Попробуйте открыть сейф")
    for attempt in range(1,attempts+1):
        print()
        print("Попытка", attempt, "из", attempts)
        guess=read_code()
        matches=count_matches(secret,guess)
        print("Совпадений:", matches)
        if is_open(matches):
            print("ПОБЕДА!")
            return
    print("ПОРАЖЕНИЕ!")
main()