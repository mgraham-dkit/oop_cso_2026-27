from types import NotImplementedType


class Vehicle:
    def __init__(self, make: str, colour: str, num_seats: int):
        '''
        Initialises a new Vehicle object with supplied parameters
        Args:
            make (str): The make of the vehicle
            colour (str): The colour of the vehicle
            num_seats (int): The number of seats within the vehicle
        '''

        self.make = make
        self.colour = colour
        self.num_seats = num_seats

    def __str__(self) -> str:
        '''
        Generates a text representation of the vehicle
        Returns:
            A formatted string representing the vehicle's information
        '''

        return f"{self.num_seats} seater {self.make.capitalize()} in {self.colour.casefold()}"

    def __repr__(self) -> str:
        '''
        Generates a text representation of the object suitable for logging
        Returns:
            A formatted string containing all fields and their values as key value pairs.
        '''

        return f"Vehicle{{make={self.make}, colour={self.colour}, num_seats={self.num_seats}}}"

    def __format__(self, format_spec) -> str:
        '''
        Generates a text representation of the vehicle in one of the following formats:
            short:  Only the make and colour are included
            long:   The make, colour and number of seats is included.
            file:   All components are included, separated by a delimiter ("%%")
            All other options will default to the str() output
        Args:
            format_spec (str): The format to be employed. Options include short, long and file.
            All other options will default to the str() output. Options are not case-sensitive.

        Returns:
            A string formatted according to the specified format supplied as a parameter
        '''
        if not format_spec:
            return str(self)

        match format_spec.lower():
            case "short":
                return f"{self.make} in {self.colour}"
            case "long":
                return str(self)
            case "file":
                return f"{self.make}%%{self.colour}%%{self.num_seats}"
            case _:
                return str(self)

    def __eq__(self, other: object) -> bool | NotImplementedType:
        '''
        Checks if the supplied Vehicle is equal to this Vehicle.
        Two Vehicles are considered equal if all attributes are equal, and these comparisons
        are case-insensitive.
        Args:
            other (object): The Vehicle to compare to

        Returns:
            NotImplemented if the supplied object is not a Vehicle,
            False if any attribute does not match, True otherwise.
        '''
        if not isinstance(other, Vehicle):
            return NotImplemented

        if self.make.lower() != other.make.lower():
            return False

        if self.colour.lower() != other.colour.lower():
            return False

        if self.num_seats != other.num_seats:
            return False

        return True

    def __ne__(self, other: object) -> bool | NotImplementedType:
        '''
        Checks if the supplied Vehicle is not equal to this Vehicle.
        Two Vehicles are considered not equal if any attribute pair are not equal, and these comparisons
        are case-insensitive.
        Args:
            other (object): The Vehicle to compare to

        Returns:
            NotImplemented if the supplied object is not a Vehicle,
            True if any attribute does not match, False if all attributes match.
        '''
        return not self == other

    def __hash__(self) -> int:
        '''
        Generates an identity value (hash) of this Vehicle. This calculation is based on
        all attributes in the Vehicle.
        Returns:
            The hash value of this object (based on all attributes)
        '''
        return hash((self.make, self.colour, self.num_seats))


class Fleet:
    def __init__(self, fleet_name: str):
        '''
        Initialises a new Fleet object with a specified name and a blank list of _vehicles
        Args:
            fleet_name (str): The name of the new Fleet object
        '''

        self._fleet_name = fleet_name
        self._vehicles = []

    def get_vehicles(self) -> list[Vehicle]:
        '''
        Retrieve the list of all vehicles in the fleet.
        This will return a copy of the vehicle list, maintaining encapsulation
        Returns:
            A copy of the list of vehicles
        '''
        return list(self._vehicles)

    def add_vehicle(self, vehicle: Vehicle) -> bool:
        '''
        Adds a supplied vehicle to the fleet's vehicle list
        Args:
            vehicle (Vehicle): The vehicle to be added

        Returns:
            True if the vehicle could be added, False otherwise (if the vehicle does not exist)
        '''
        if not vehicle:
            return False

        self._vehicles.append(vehicle)
        return True

    def remove_vehicle(self, vehicle: Vehicle) -> bool:
        '''
        Removes a supplied vehicle from the fleet's vehicle list
        Args:
            vehicle (Vehicle): The vehicle to be removed

        Returns:
            True if the vehicle could be removed, False otherwise
            (if the vehicle does not exist or was not found)
        '''

        if not vehicle:
            return False

        if vehicle in self._vehicles:
            self._vehicles.remove(vehicle)
            return True

        return False

    def get_vehicle_count(self) -> int:
        '''
        Counts the number of _vehicles in the fleet
        Returns:
            The number of _vehicles in the fleet
        '''

        return len(self._vehicles)

    def get_vehicles_by_make(self, make: str) -> list[Vehicle]:
        '''
        Identifies all _vehicles matching the supplied make (case-insensitive)
        Args:
            make (str): The make to search for

        Returns:
            A list of all _vehicles matching the specified make
        '''
        matches = []

        if not make:
            return matches

        make = make.lower()
        for vehicle in self._vehicles:
            if vehicle.make.lower() == make:
                matches.append(vehicle)

        return matches

    def __str__(self) -> str:
        '''
        Generates a text representation of the fleet
        Returns:
            A formatted string representing the fleet's information
        '''

        return f"{self._fleet_name} contains {len(self._vehicles)} _vehicles."

    def __repr__(self) -> str:
        '''
        Generates a text representation of the object suitable for logging
        Returns:
            A formatted string containing all fields and their values as key value pairs.
        '''

        return f"Fleet{{_fleet_name={self._fleet_name}, _vehicles={self._vehicles}}}"

    def __format__(self, format_spec) -> str:
        '''
        Generates a text representation of the fleet in one of the following formats:
            short:  Only the fleet name is included
            long:   The fleet name and details of each vehicle (make, colour and number of seats) is included.
            file:   Fleet name##{vehicle:file},{vehicle:file},...,{vehicle:file}
            All other options will default to the str() output
        Args:
            format_spec (str): The format to be employed. Options include short, long and file.
            All other options will default to the str() output. Options are not case-sensitive.

        Returns:
            A string formatted according to the specified format supplied as a parameter
        '''
        if not format_spec:
            return str(self)

        match format_spec.lower():
            case "short":
                return f"{self._fleet_name}"
            case "long":
                vehicle_text = ""
                for i, vehicle in enumerate(self._vehicles):
                    vehicle_text += vehicle
                    if i < len(self._vehicles)-1:
                        vehicle_text += ", "

                return f"{self._fleet_name}: {vehicle_text}"
            case "file":
                vehicle_text = ""
                for i, vehicle in enumerate(self._vehicles):
                    vehicle_text += format(vehicle, "file")
                    if i < len(self._vehicles)-1:
                        vehicle_text += ","
                return f"{self._fleet_name}##{vehicle_text}"
            case _:
                return str(self)

    def __eq__(self, other: object) -> bool | NotImplementedType:
        '''
        Checks if the supplied Fleet is equal to this Fleet.
        Two Fleets are considered equal if all attributes are equal, and these comparisons
        are case-insensitive.
        Args:
            other (object): The Fleet to compare to

        Returns:
            NotImplemented if the supplied object is not a Fleet,
            False if any attribute does not match, True otherwise.
        '''
        if not isinstance(other, Fleet):
            return NotImplemented

        if self._fleet_name.lower() != other._fleet_name.lower():
            return False

        return True

    def __ne__(self, other: object) -> bool | NotImplementedType:
        '''
        Checks if the supplied Fleet is not equal to this Vehicle.
        Two Fleet are considered not equal if their names are not the same (case-insensitive).
        Args:
            other (object): The Fleet to compare to

        Returns:
            NotImplemented if the supplied object is not a Fleet,
            True if the fleet names do not match, False if they do match.
        '''
        return not self == other

    def find_duplicates(self) -> list[Vehicle]:
        '''
        Identify all duplicate Vehicles within the Fleet

        Returns:
            A list containing a single instance of each vehicle
            appearing more than once in the fleet
        '''
        duplicates = []
        for vehicle in self._vehicles:
            if self._vehicles.count(vehicle) > 1 and vehicle not in duplicates:
                duplicates.append(vehicle)

        return duplicates

    def find_uniques(self) -> list[Vehicle]:
        '''
        Identify all unique _vehicles in the fleet
        Returns:
            A list containing all unique _vehicles found in the fleet
        '''
        uniques = []
        for vehicle in self._vehicles:
            if self._vehicles.count(vehicle) == 1:
                uniques.append(vehicle)

        return uniques

    def write_vehicles_to_file(self, filename: str) -> None:
        '''
        Write the content of the fleet vehicle list to the specified file.
        Vehicles are written out using Vehicle's file format as provided by format():file
        Args:
            filename (str): The filename to write to. This must include the path and file extension.
        '''
        if not filename:
            return

        with open(filename, "a") as file:
            for vehicle in self._vehicles:
                file.write(f"{vehicle:file}\n")