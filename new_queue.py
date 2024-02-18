from queue import Queue


#Обробник команд користувача
def parse_input(user_input):
    cmd = user_input
    cmd = cmd.strip().lower()
    return cmd

#Черга заявок
queue = Queue()

#Створити чергу заявок
def generate_request():
    for i in range(1, 101):
        queue.put(f'Client -> {i}')
        print(f'Додано заявку клієнта: Client -> {i}')

#Обробити заявки в черзі
def rocess_request():
    while not queue.empty():
        current_client = queue.get()
        print(f'Обслуговуємо клієнта: {current_client}')
    else:
        print(f'Наразі черга заявок порожня!\n')

#Керувати програмою
def main():
    print(f'Вітаємо у черзі обслуговування клієнтів!')

    while True:
        user_input = input("Бажаєте створити нову чергу? 'так' або 'ні': ")
        command = parse_input(user_input)
    
        if command  == "ні":
            print("\nДо побачення!")
            break
        elif command  == "так":        
            generate_request()
            rocess_request()
        else:
            print("Не коректне введення!")




if __name__ == "__main__":
    main()