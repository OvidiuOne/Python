import csv
import json
import os
import shutil

##OUTPUT_DIR = "output_data"

if __name__ == "__main__":
    shutil.rmtree("output_data", ignore_errors=True)
    # if os.path.exists("output_data")
    #     shutil.rmtree("output_data")  ##
    with open("input.csv", "r") as f:
        dict_reader = csv.DictReader(f)
        cars = list(dict_reader)

    slow_cars = [car for car in cars if int(car.get("hp", 0)) < 120]
    fast_cars = [car for car in cars if 120 <= int(car.get("hp", 0)) < 180]
    sport_cars = [car for car in cars if int(car.get("hp", 0)) >= 180]
    cheap_cars = [car for car in cars if int(car.get("price", 0)) < 1000]
    medium_cars = [car for car in cars if 1000 <= int(car.get("price", 0)) < 5000]
    expensive_cars = [car for car in cars if int(car.get("price", 0)) >= 5000]

    if not os.path.exists("output_data"):
        os.makedirs("output_data")

    with open("output_data/slow_cars.json", "w") as f1, open("output_data/fast_cars.json", "w") as f2, \
            open("output_data/sport_cars.json", "w") as f3, open("output_data/cheap_cars.json", "w") as f4, \
            open("output_data/medium_cars.json", "w") as f5, open("output_data/expensive_cars.json", "w") as f6:
        json.dump(slow_cars, f1, indent=2)
        json.dump(fast_cars, f2, indent=2)
        json.dump(sport_cars, f3, indent=2)
        json.dump(sport_cars, f4, indent=2)
        json.dump(sport_cars, f5, indent=2)
        json.dump(sport_cars, f6, indent=2)

    # with open("output_data/slow_cars.json", "w") as f:
    #     json.dump(slow_cars, f, indent=2)
    # with open("output_data/fast_cars.json", "w") as f:
    #     json.dump(fast_cars, f, indent=2)
    # with open("output_data/sport_cars.json", "w") as f:
    #     json.dump(sport_cars, f, indent=2)
    # with open("output_data/cheap_cars.json", "w") as f:
    #     json.dump(cheap_cars, f, indent=2)
    # with open("output_data/medium_cars.json", "w") as f:
    #     json.dump(medium_cars, f, indent=2)
    # with open("output_data/expensive_cars.json", "w") as f:
    #     json.dump(expensive_cars, f, indent=2)

    audi = [car for car in cars if car.get("brand", 0) == "Audi"]
    with open("output_data/audi.json", "w") as f:
        json.dump(audi, f, indent=2)

    bmw = [car for car in cars if car.get("brand", 0) == "BMW"]
    with open("output_data/bmw.json", "w") as f:
        json.dump(bmw, f, indent=2)

    dacia = [car for car in cars if car.get("brand", 0) == "Dacia"]
    with open("output_data/dacia.json", "w") as f:
        json.dump(dacia, f, indent=2)

    honda = [car for car in cars if car.get("brand", 0) == "Honda"]
    with open("output_data/honda.json", "w") as f:
        json.dump(honda, f, indent=2)

    mercedes = [car for car in cars if car.get("brand", 0) == "Mercedes"]
    with open("output_data/mercedes.json", "w") as f:
        json.dump(mercedes, f, indent=2)

    toyota = [car for car in cars if car.get("brand", 0) == "Toyota"]
    with open("output_data/toyota.json", "w") as f:
        json.dump(toyota, f, indent=2)





    # print("slow_cars :", slow_cars)
    # print("fast_cars :", fast_cars)
    # print("sport_cars :", sport_cars)
    # print("cheap_cars :", cheap_cars)
    # print("medium_cars :", medium_cars)
    # print("expensive_cars :", expensive_cars)