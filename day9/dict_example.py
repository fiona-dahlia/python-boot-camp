example_dictionary = {
    "Fio": 10,
    "Jerri": 14,
}
print(example_dictionary["Fio"])

# add new element
example_dictionary["Jino"] = 38

# overwriting value
example_dictionary["Fio"] = 11
print(example_dictionary)

# looping through dictionary
for key in example_dictionary:
    print(f"key: {key} value: {example_dictionary[key]}")


