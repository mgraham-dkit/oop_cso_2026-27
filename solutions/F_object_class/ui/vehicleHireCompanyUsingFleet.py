from solutions.F_object_class.entities.transport import Vehicle
from solutions.F_object_class.entities.transport import Fleet

def create_fleet(fleet_name: str) -> Fleet:
    '''
    Creates a new Fleet containing 11 hard-coded Vehicle objects spread across different makes and models
    Args:
        fleet_name(str): the name for the new fleet
    Returns:
        A new Fleet with the specified name, containing 11 vehicles
    '''
    new_fleet = Fleet(fleet_name)
    new_fleet.add_vehicle(Vehicle("Honda", "Grey", 5))
    new_fleet.add_vehicle(Vehicle("BYD", "Blue", 5))
    new_fleet.add_vehicle(Vehicle("Ford", "Grey", 3))
    new_fleet.add_vehicle(Vehicle("Toyota", "Black", 5))
    new_fleet.add_vehicle(Vehicle("Volkswagen", "Red", 7))
    new_fleet.add_vehicle(Vehicle("Opal", "White", 7))
    new_fleet.add_vehicle(Vehicle("Toyota", "Blue", 4))
    new_fleet.add_vehicle(Vehicle("Cupra", "Black", 6))
    new_fleet.add_vehicle(Vehicle("BYD", "Blue", 5))
    new_fleet.add_vehicle(Vehicle("Volkswagen", "Red", 7))
    new_fleet.add_vehicle(Vehicle("Ford", "Grey", 3))

    return new_fleet


def display_vehicles(vehicles_list: list[Vehicle]) -> None:
    '''
    Displays all vehicles in a supplied list
    Args:
        vehicles_list: the list of vehicles to be displayed
    '''
    for vehicle in vehicles_list:
        print(vehicle)

def tech_display_vehicles(vehicles_list: list[Vehicle]) -> None:
    '''
    Displays the repr representation of all vehicles in a supplied list
    Args:
        vehicles_list: the list of vehicles to be displayed
    '''
    for vehicle in vehicles_list:
        print(repr(vehicle))


if __name__ == "__main__":
    fleet = create_fleet("My fleet")

    print("Fleet details:")
    display_vehicles(fleet.get_vehicles())
    print("-"*20)

    print("Technical details:")
    tech_display_vehicles(fleet.get_vehicles())
    print("-"*20)

    duplicates = fleet.find_duplicates()
    print("Duplicate vehicles:")
    display_vehicles(duplicates)
    print("-"*20)

    uniques = fleet.find_uniques()
    print("Unique vehicles:")
    display_vehicles(uniques)
    print("-"*20)

    fleet.write_vehicles_to_file("fleet_details.txt")
    print(f"{fleet:file}")