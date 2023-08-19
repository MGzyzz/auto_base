import json


class Truck:
    def __init__(self, id, name, driver, state_name):
        self.id = id
        self.name = name
        self.driver = driver
        self.state_name = state_name


class TruckManagement:
    def __init__(self):
        self.trucks = []
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


    def main_menu(self):
        while True:
            print("Меню:\n1\tОтобразить текущее состояние грузовиков\n2\tПоказать данные грузовика по id")
            choice = input("Выберите действие: ")

            if choice == "1":
                print('№ | Грузовик| Водитель  | Состояние ')
                for truck in self.trucks:
                    self.show_truck_info(truck)
            elif choice == "2":
                truck_id = int(input("Введите номер грузовика: "))
                truck = next((t for t in self.trucks if t.id == truck_id), None)
                if truck:
                    self.show_truck_info(truck)
                else:
                    print("Грузовик с таким номером не найден.")




TruckManagement().main_menu()