from collections import deque


#Обробник команд користувача
def parse_input(user_input):
    cmd = user_input
    cmd = cmd.strip().lower()
    return cmd

#Функція перевірки на паліндромність
def is_palindrome(check_string: str):
    formatted_string = ''.join(check_string.split()).lower()   # Перетворення рядка: видалення пробілів і переведення в нижній регістр
    char_deque = deque(formatted_string)   # Створення двосторонньої черги з символів рядка

    # Порівняння символів з обох кінців, поки черга не стане порожньою або поки не буде знайдено відмінності
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
        return True

#Керувати програмою
def main():
    print(f'Вітаю у додатку з перевірки паліндромів!')

    while True:
        user_input = input("Бажаєте почати превірку на паліндромність? ('так' або 'ні'): ")
        command = parse_input(user_input)
    
        if command  == "ні":
            print("\nДо побачення!")
            break
        elif command  == "так":
            check_input = input("Введіть текст для превірки: ")
            print(f"Чи є текст '{check_input}' паліндромом: '{is_palindrome(check_input)}'")
        else:
            print("Не коректне введення!")





if __name__ == "__main__":
    main()