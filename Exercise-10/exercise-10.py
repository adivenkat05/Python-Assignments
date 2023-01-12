def mergeList(list1, list2):
    resultList = []
    for i in list1:
        if(i % 2 != 0):
            resultList.append(i)

    for i in list2:
        if(i % 2 == 0):
            resultList.append(i)
    
    return f"Result list: {resultList}"


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print(mergeList(list1, list2))
    
