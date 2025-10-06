tasks = []

def list_tasks():
    """Показує список завдань."""
    if not tasks:
        return "Список порожній."
    return "\n".join([f"{i+1}. {task['title']} - [{'x' if task['done'] else '[ ]'}]" for i, task in enumerate(tasks)])

def add_task(title):
    """Додає нове завдання до списку."""
    tasks.append({"title": title, "done": False})

def remove_task(user_index):
    if user_index < 1 or user_index > len(tasks):
        return "ERR01"
    tasks.pop(user_index - 1)
    return "OK"

def mark_done(user_index):
    if user_index < 1 or user_index > len(tasks):
        return "ERR01"
    tasks[user_index - 1]["done"] = True
    return "OK"

def edit_task(user_index, new_title):
    if user_index < 1 or user_index > len(tasks):
        return "ERR01"
    tasks[user_index - 1] = {"title": new_title, "done": tasks[user_index - 1]["done"]}
    return "OK"

def print_menu():
    """Формує текст меню для взаємодії з користувачем."""
    return """--- Меню To-Do ---
1) Додати завдання
0) Вихід"""
def main():
    """Основна функція для взаємодії з користувачем."""
    print("Ласкаво просимо до списку завдань To-Do!")
    while True:
        print(print_menu())
        choice = input("Оберіть пункт: ")

        if choice == "1":
            title = input("Введіть назву завдання: ")
            add_task(title)
            print("Завдання додано!")
        elif choice == "2":
            try:
                idx = int(input("Номер завдання для видалення: "))
                print(remove_task(idx))
            except ValueError:
                print("ERR01")
        elif choice == "3":
            try:
                idx = int(input("Номер виконаного завдання: "))
                print(mark_done(idx))
            except ValueError:
                print("ERR01")
        elif choice == "4":
            print(list_tasks())
        elif choice == "5":
            try:
                idx = int(input("Номер завдання для редагування: "))
                new_t = input("Нова назва завдання: ")
                print(edit_task(idx, new_t))
            except ValueError:
                print("ERR01")
        elif choice == "0":
            print("До зустрічі!")
            break
        else:
            print("ERR01")

if __name__ == "__main__":
    main()
