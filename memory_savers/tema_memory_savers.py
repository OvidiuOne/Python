from car_list import cars

# Categorize by horsepower


# slow_cars = []
# fast_cars = []
# sport_cars = []
#
# for car in cars:
#     if car["hp"] < 120:
#         slow_cars.append(car)
#     elif car["hp"] < 180:
#         fast_cars.append(car)
#     else:
#         sport_cars.append(car)
#
# print("slow_cars", slow_cars)
# print("fast_cars", fast_cars)
# print("sport_cars", sport_cars)

slow_cars = [cars["brand"] for cars in cars if cars.get("hp", 0) < 120]
fast_cars = [cars["brand"] for cars in cars if cars.get("hp", 0) >= 120 and cars.get("hp", 0) < 180]
sport_cars = [cars["brand"] for cars in cars if cars.get("hp", 0) >= 180]

print("slow_cars :", slow_cars)
print("fast_cars :", fast_cars)
print("sport_cars :", sport_cars)


# # Categorize by price
#
# cheap_cars = []
# medium_cars = []
# expensive_cars = []
#
# for car in cars:
#     if car["price"] < 1000:
#         cheap_cars.append(car)
#     elif car["price"] < 5000:
#         medium_cars.append(car)
#     else:
#         expensive_cars.append(car)
#
# print("cheap_cars", cheap_cars)
# print("medium_cars", medium_cars)
# print("expensive_cars", expensive_cars)

cheap_cars = [cars["brand"] for cars in cars if cars.get("price", 0) < 1000]
medium_cars = [cars["brand"] for cars in cars if cars.get("price", 0) >= 1000 and cars.get("price", 0) < 5000]
expensive_cars = [cars["brand"] for cars in cars if cars.get("price", 0) >= 5000]

print("cheap_cars :", cheap_cars)
print("medium_cars :", medium_cars)
print("expensive_cars :", expensive_cars)