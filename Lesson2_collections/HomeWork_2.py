#1
def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst)==0:
        print("Wrong list")
        return
    reversed_lst = lst[::-1]
    print(reversed_lst)

print_list_reverse([1, 2, 3, 4, 5])
print()

#2
def is_valid_point(point):
    if point is None:
        return None
    if isinstance(point, tuple) and len(point)==0:
        return None
    if not isinstance(point,tuple):
        return False
    if len(point)!=2:
        return False
    x,y = point
    if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
        return False
    return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))
print()

#3
def print_sublist_reverse(lst, start, finish):
    if lst is None or not isinstance(lst,list) or len(lst)==0:
        print("Wrong args")
        return
    if (
        not isinstance(start,int) or isinstance(start,bool)
        or not isinstance(finish,int) or isinstance(finish,bool)
    ):
        print("Wrong args")
        return
    if start<0 or finish >=len(lst) or start>finish:
        print("Wrong args")
        return
    beginning = lst[:start]
    middle_reversed = lst[start:finish+1]
    ending = lst[finish+1]
    print(beginning+middle_reversed+ending)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print_sublist_reverse([1, 2, 3], "0", 2)
print_sublist_reverse([1, 2, 3], 0, 5)
print_sublist_reverse([1, 2, 3], 2, 1)

#4
def get_students_by_grade(students):
    if students is None or not isinstance(students,dict) or len(students)==0:
        return {}
    result = {}
    for name,grade in students.items():
        result.setdefault(grade, [].append(name))
        return
    
print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))











