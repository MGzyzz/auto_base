import json
from abc import ABC, abstractmethod


class TruckState(ABC):
    @abstractmethod
    def change_driver(self, new_driver):
        pass

    @abstractmethod
    def start_run(self):
        pass

    @abstractmethod
    def start_repair(self):
        pass

class BaseState(TruckState):
    name = "На базе"
    def change_driver(self, new_driver):
        return "Водитель успешно изменен на " + new_driver
    def start_run(self):
        return "Грузовик выехал в путь"
    def start_repair(self):
        return "Грузовик отправлен в ремонт"


class RunState(TruckState):
    name = "На маршруте"
    def change_driver(self, new_driver):
        return "Нельзя менять водителя в пути"
    def start_run(self):
        return "Грузовик уже находится в пути"
    def start_repair(self):
        return "Грузовик отправлен в ремонт"


class RepairState(TruckState):
    name = "В ремонте"
    def change_driver(self, new_driver):
        return "Водитель успешно изменен на " + new_driver
    def start_run(self):
        return "Грузовик случайным образом отправлен в путь или на базу"
    def start_repair(self):
        return "Грузовик уже находится в ремонте"

class Truck:
    def __init__(self, id, name, driver, state_name):
        self.id = id
        self.name = name
        self.driver = driver
        self.state_name = state_name


class TruckManagement:
    def __init__(self):
        self.trucks = []
        self.states = {
            "base": BaseState(),
            "run": RunState(),
            "repair": RepairState()
        }
        self.load_data()

    def load_data(self):
        try:
            with open("dump.json", "r") as file:
                data = json.load(file)
                for item in data:
                    truck = Truck(item["id"], item["name"], item["driver"], item["state_name"])
                    self.trucks.append(truck)
        except FileNotFoundError:
            print("Файл не найден. Создайте файл trucks.json с данными.")


    def show_truck_info(self, truck):
        print(f"{'='*15}\n{truck.id}| {truck.name}| {truck.driver} | {truck.state_name}\n{'='*15}")

    def save_data(self):
        with open("dump.json", "w") as file:
            data = [{"id": truck.id, "name": truck.name, "driver": truck.driver, "state_name": truck.state_name}
                    for truck in self.trucks]
            json.dump(data, file, indent=4)

    def main_menu(self):
        while True:
            print("Меню:\n1\tОтобразить текущее состояние грузовиков\n2\tПоказать данные грузовика по id\n3\tОбновить состояние грузовика\n4\tЗавершить программу и выгрузить все данные")
            choice = input("Выберите действие: ")

            match choice:
                case '1':
                    print('№ | Грузовик| Водитель  | Состояние ')
                    for truck in self.trucks:
                        self.show_truck_info(truck)
                case '2':
                    truck_id = int(input("Введите номер грузовика: "))
                    truck = next((t for t in self.trucks if t.id == truck_id), None)
                    if truck:
                        self.show_truck_info(truck)
                    else:
                        print("Грузовик с таким номером не найден.")
                case '3':
                    truck_id, new_state_name = input("Укажите номер грузовика и состояние через пробел: ").split()
                    truck = next((t for t in self.trucks if t.id == int(truck_id)), None)
                    if truck:
                        truck.state_name = new_state_name
                        state = self.states.get(new_state_name)
                        if state:
                            print(f"Грузовик \"{truck.name}\" - {state.name}")
                        else:
                            print("Некорректное состояние.")
                case '4':
                    self.save_data()
                    break





if __name__ == "__main__":
    truck_management = TruckManagement()
    truck_management.main_menu()
