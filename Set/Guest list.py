guest_set = set(map(int, input("Name of the guist devided by comma: ").split(',')))

print(f"Current guest list: {guest_set}")

while True:
    name_to_find = input("\nEnter a name to search (or type 'exit' to quit): ")
    if name_to_find.lower() == 'exit':
        break

    if name_to_find in guest_set:
        print(f"'{name_to_find}' is on the guest list. Welcome!")
    else:
        print(f"Sorry, '{name_to_find}' is not on the guest list.")