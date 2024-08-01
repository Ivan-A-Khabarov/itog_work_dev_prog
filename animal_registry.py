from animals import Dogs, Cats, Hamsters, Horses, Donkeys

class AnimalRegistry:
    def __init__(self):
        self.animals = []
    
    def register_new_animal(self, animal):
        self.animals.append(animal)
    
    def determine_class(self, animal):
        if isinstance(animal, Dogs):
            return "Собаки"
        elif isinstance(animal, Cats):
            return "Кошки"
        elif isinstance(animal, Hamsters):
            return "Хомяки"
        elif isinstance(animal, Horses):
            return "Лошади"
        elif isinstance(animal, Donkeys):
            return "Ослы"
        else:
            return "Неизвестный класс"
    
    def list_commands(self, animal):
        return animal.get_commands()
    
    def train_new_commands(self, animal, new_command):
        commands = animal.get_commands()
        commands.append(new_command)
        animal.set_commands(commands)

    def menu(self):
        while True:
            print("1. Зарегистрировать новое животное")
            print("2. Определить класс животного")
            print("3. Показать команды животного")
            print("4. Обучить животное новой команде")
            print("5. Выйти")
            choice = input("Выберите опцию меню: ")
            if choice == '1':
                name = input("Введите имя животного: ")
                commands = input("Введите команды животного (разделенные запятыми): ").split(',')
                birth_date = input("Введите дату рождения животного (ГГГГ-ММ-ДД): ")
                animal_class = input("Введите класс животного (Собаки, Кошки, Хомяки, Лошади, Ослы): ")
                if animal_class == "Собаки":
                    animal = Dogs(name, commands, birth_date)
                elif animal_class == "Кошки":
                    animal = Cats(name, commands, birth_date)
                elif animal_class == "Хомяки":
                    animal = Hamsters(name, commands, birth_date)
                elif animal_class == "Лошади":
                    animal = Horses(name, commands, birth_date)
                elif animal_class == "Ослы":
                    animal = Donkeys(name, commands, birth_date)
                else:
                    print("Неверный класс животного")
                    continue
                self.register_new_animal(animal)
                print("Животное зарегистрировано")
            elif choice == '2':
                name = input("Введите имя животного: ")
                for animal in self.animals:
                    if animal.get_name() == name:
                        print("Класс животного:", self.determine_class(animal))
                        break
                else:
                    print("Животное не найдено")
            elif choice == '3':
                name = input("Введите имя животного: ")
                for animal in self.animals:
                    if animal.get_name() == name:
                        print("Команды животного:", ', '.join(self.list_commands(animal)))
                        break
                else:
                    print("Животное не найдено")
            elif choice == '4':
                name = input("Введите имя животного: ")
                new_command = input("Введите новую команду: ")
                for animal in self.animals:
                    if animal.get_name() == name:
                        self.train_new_commands(animal, new_command)
                        print("Животное обучено новой команде")
                        break
                else:
                    print("Животное не найдено")
            elif choice == '5':
                break
            else:
                print("Неверный выбор, попробуйте еще раз")

if __name__ == "__main__":
    registry = AnimalRegistry()
    registry.menu()