def make_card():
    '''
    Ask for name, birth year and favourite foods, then print a formatted profile card.
    '''
    full_name = input("Full name: ")
    birth_year = int(input("Birth Year: "))
    foods = input("Favourite foods, comma-separated: ")

    # Clean name once: split() drops extra spaces, join puts single spaces back
    parts = full_name.split()
    name = " ".join(parts).title()
    parts = name.split()

    age = 2026 - birth_year

    # Assumes exactly 3 foods (no loops yet)
    food_list = foods.split(",")
    food_1 = food_list[0].strip()
    food_2 = food_list[1].strip()
    food_3 = food_list[2].strip()

    border = "=" * 30

    print(border)
    print(f"{'Name':<12}: {name}")
    print(f"{'Initials':<12}: {parts[0][0]}.{parts[1][0]}.")
    print(f"{'Reversed':<12}: {name[::-1]}")
    print(f"{'Age in 2026':<12}: {age}")
    print(f"{'Adult?':<12}: {age >= 18}")
    print(f"{'Even age?':<12}: {age % 2 == 0}")
    print(f"{'Name length':<12}: {len(name)}")
    has_a_label = "Has 'a'?"
    print(f"{has_a_label:<12}: {'a' in name}")
    print(f"{'Foods':<12}: {' | '.join([food_1, food_2, food_3])}")
    print(f"{'First food':<12}: {food_1.upper()}")
    print(border)


make_card()
