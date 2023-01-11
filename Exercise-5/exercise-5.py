def first_last_same(list):
    print(f"Given list: {list}")

    if (list[0] == list[-1]):
        return "The result is TRUE."

    else :
        return "The result is FALSE."


list1 = [10, 20, 30, 10]
print(first_last_same(list1))

list2 = [10, 20, 30, 40]
print(first_last_same(list2))
