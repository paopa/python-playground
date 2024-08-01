import copy

a = [1, [2, 3]]

a_eq = a
a_scp = a.copy()
a_dcp = copy.deepcopy(a)

# change the first element of the list
a_eq[0] = 2
a_eq[1][0] = 4


print(f"a: {a}, id: {id(a)}, id[1]: {id(a[1])}")
print(f"a_eq: {a_eq}, id: {id(a_eq)}, id[1]: {id(a_eq[1])}")
# shallow copy copies the reference of the nested list, so the nested list is still the same object
# it means that if you change the nested list, it will change in both lists
print(f"a_cp: {a_scp}, id: {id(a_scp)}, id[1]: {id(a_scp[1])}")
# deep copy copies the nested list, so the nested list is a new object
# it means that if you change the nested list, it won't change in the original list
print(f"a_dcp: {a_dcp}, id: {id(a_dcp)}, id[1]: {id(a_dcp[1])}")
