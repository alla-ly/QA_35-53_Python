#1
def print_list_reverse(lst):
    if lst is None or type(lst) is not list or len(lst) == 0:
        print("Wrong list")
    else:
        print(lst[::-1])

print_list_reverse([1, 2, 3, 4, 5])
print_list_reverse([])
print_list_reverse("not a list")
print_list_reverse(None)
print()

#2
def is_valid_point(point):
    if point is None or point == ():
        return None

    if type(point) is not tuple or len(point) != 2:
        return False

    x_type = type(point[0])
    y_type = type(point[1])

    if (x_type is int or x_type is float) and (y_type is int or y_type is float):
        return True
    else:
        return False

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))
print()

#3
def print_sublist_reverse(lst, start, finish):
    if lst is None or type(lst) is not list or len(lst) == 0:
        print("Wrong args")
        return

    if type(start) is not int or type(finish) is not int:
        print("Wrong args")
        return

    if start < 0 or finish < 0 or start >= len(lst) or finish >= len(lst) or start > finish:
        print("Wrong args")
        return

    result = lst[:start] + lst[start:finish + 1][::-1] + lst[finish + 1:]

    print(result)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print_sublist_reverse([1, 2, 3], "0", 2)
print_sublist_reverse([1, 2, 3], 0, 5)
print_sublist_reverse([1, 2, 3], 2, 1)

#4
def get_students_by_grade(students):
    if students is None or not isinstance(students, dict) or len(students) == 0:
       return {}

    result = {}

    for student in students:
        grade = students[student]

        if grade not in result:
            result[grade] = []

        result[grade].append(student)

    return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))

print(get_students_by_grade({}))
print(get_students_by_grade(None))
print(get_students_by_grade([1, 2, 3]))