from solutions.F_object_class.entities.transport import Vehicle

def create_fleet() -> list[Vehicle]:
    '''
    Creates a new list of hard-coded Vehicle objects spread across different makes and models
    Returns:
        A new list of 11 vehicles
    '''
    vehicle1 = Vehicle("Honda", "Grey", 5)
    vehicle2 = Vehicle("BYD", "Blue", 5)
    vehicle3 = Vehicle("Ford", "Grey", 3)
    vehicle4 = Vehicle("Toyota", "Black", 5)
    vehicle5 = Vehicle("Volkswagen", "Red", 7)
    vehicle6 = Vehicle("Opal", "White", 7)
    vehicle7 = Vehicle("Toyota", "Blue", 4)
    vehicle8 = Vehicle("Cupra", "Black", 6)
    vehicle9 = Vehicle("BYD", "Blue", 5)
    vehicle10 = Vehicle("Volkswagen", "Red", 7)
    vehicle11 = Vehicle("Ford", "Grey", 3)

    return [vehicle1, vehicle2, vehicle3, vehicle4, vehicle5, vehicle6, vehicle7, vehicle8, vehicle9, vehicle10, vehicle11]


def display_vehicles(vehicles_list: list[Vehicle]) -> None:
    '''
    Displays all vehicles in a supplied list
    Args:
        vehicles_list (list[Vehicle]): the list of vehicles to be displayed
    '''
    for vehicle in vehicles_list:
        print(vehicle)

def tech_display_vehicles(vehicles_list: list[Vehicle]) -> None:
    '''
    Displays the repr representation of all vehicles in a supplied list
    Args:
        vehicles_list (list[Vehicle]): the list of vehicles to be displayed
    '''
    for vehicle in vehicles_list:
        print(repr(vehicle))


def find_duplicates(vehicle_list: list[Vehicle]) -> list[Vehicle]:
    '''
    Identify all duplicates in a supplied list of Vehicles
    Args:
        vehicle_list (list[Vehicle]): The list of vehicles to be processed

    Returns:
        A list containing a single instance of each vehicle
        appearing more than once in the supplied list
    '''
    duplicates = []
    if not vehicle_list:
        return duplicates

    for vehicle in vehicle_list:
        if vehicle_list.count(vehicle) > 1 and vehicle not in duplicates:
            duplicates.append(vehicle)

    return duplicates


def find_uniques(vehicle_list: list[Vehicle]) -> list[Vehicle]:
    '''
    Identify all unique vehicles in a supplied list
    Args:
        vehicle_list (list[Vehicle]): The list of vehicles to be processed

    Returns:
        A list containing all unique vehicles found in the supplied list
    '''
    uniques = []
    if not vehicle_list:
        return uniques

    for vehicle in vehicle_list:
        if vehicle_list.count(vehicle) == 1:
            uniques.append(vehicle)

    return uniques


def write_vehicles_to_file(vehicle_list: list[Vehicle], filename: str) -> None:
    '''
    Write the content of a supplied list of vehicles to the specified file.
    Vehicles are written out using Vehicle's file format as provided by format():file
    Args:
        vehicle_list (list[Vehicle]): The list of vehicles to be written to the file
        filename (str): The filename to write to. This must include the path and file extension.
    '''
    if not filename:
        return

    with open(filename, "a") as file:
        for vehicle in vehicle_list:
            file.write(f"{vehicle:file}\n")


if __name__ == "__main__":
    vehicles = create_fleet()

    print("Fleet details:")
    display_vehicles(vehicles)
    print("-"*20)

    print("Technical details:")
    tech_display_vehicles(vehicles)
    print("-"*20)

    duplicates = find_duplicates(vehicles)
    print("Duplicate vehicles:")
    display_vehicles(duplicates)
    print("-"*20)

    uniques = find_uniques(vehicles)
    print("Unique vehicles:")
    display_vehicles(uniques)
    print("-"*20)

    write_vehicles_to_file(vehicles, "fleet_details.txt")