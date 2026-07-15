#1
def create_profile(name,age=18,city="Unknown"):
    return {
        "name":name,
        "age":age,
        "city":city
    }

print(create_profile("Anna"))
print(create_profile("Tom", 25))
print(create_profile(city="Haifa", name="Maria"))
print()

#2
def sum_even_numbers(*numbers):
    even_numbers = filter(lambda n: n % 2 == 0, numbers)
    return sum(even_numbers)

print(sum_even_numbers(1, 2, 3, 4, 5, 6))
print(sum_even_numbers(7, 9))
print(sum_even_numbers())
print()

#3
def print_pet_info(name, **info):
    print(f"Name: {name}")
    if len(info) > 0:
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
       print("No additional information")

print_pet_info("Lucky", age=4, color="White", breed="Spitz")
print_pet_info("Lucky")
print()

#4
def merge_lists(*lists):
    combined_list = []
    for lst in lists:
        combined_list = combined_list + lst
    return combined_list

print(merge_lists([1,2],[3],[4,5],[]))
print(merge_lists())


