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
            with open("dumps.json", "r") as file:
                data = json.load(file)
                for item in data:
                    truck = Truck(item["id"], item["name"], item["driver"], item["state_name"])
                    self.trucks.append(truck)
        except FileNotFoundError:
            print("Файл не найден. Создайте файл trucks.json с данными.")



class Main:
    while True:
        if TruckManagement:
            TruckManagement().load_data()
            print('Work')
            break