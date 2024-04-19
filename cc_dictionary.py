inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snowfall():
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    return total_inches

thursday_snow = input("How many inches of snow fell on thursday?: ")
inches_snow["Thursday"] = int(thursday_snow)

print(f"The total snowfall was {print_total_snowfall()} inches.")

