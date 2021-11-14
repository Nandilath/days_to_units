calculation_to_units = 24
name_of_units = "hours"


def days_to_units (num_of_days,custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units} ")
    print(custom_message)

days_to_units(35, "Looks great")
days_to_units(58, "Mind blowing")