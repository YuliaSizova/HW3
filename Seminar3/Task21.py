list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": "S005"},
          {" V ": "S009"}, {" VIII ": "S007"}]


my_set = set()

for item in list_1:
    for key in item.keys():
        my_set.add(item.get(key))

print(my_set)
