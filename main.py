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
def show_rules():
    print()
    print("=== ПРАВИЛА ИГРЫ ===")
    print("Код состоит из 3 цифр")
    print("У вас есть 5 попыток")
    print("После каждой попытки показывается кол-во цифр на своих местах")
    print("3 совпадения - победа, после 5 неудач поражение")