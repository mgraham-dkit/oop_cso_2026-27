# import required classes from modules
from datetime import date, time, datetime
from types import NotImplementedType


class Screening:
    # Spec states that the date and time fields should be optional, so defaults are provided
    # These are None so that the validation can pick them up and set them appropriately
    # Putting the values into the signature will set them to the value created when the class was loaded into the system
    # (like how we have to set lists and dicts to None instead of [] or {} - we want a new value for every instance
    def __init__(self, screening_id: str, movie_title: str, screening_date: date = None, screening_time: time = None):
        # Handle screening ID validation
        prefix = "S_"
        default_id = prefix + "DEFAULT"

        # If no screening ID provided
        if not screening_id:
            print(f"NO ID PROVIDED - SETTING TO DEFAULT ({default_id})")
            screening_id = default_id

        # If it doesn't start with the prefix
        if not screening_id.upper().startswith(prefix):
            screening_id = prefix + screening_id
            print(f"Screening ID must start with standard prefix ({prefix}). ID updated to {screening_id}")

        # Handle movie title validation
        default_title = "DEFAULT_TITLE"
        if not movie_title:
            print(f"NO TITLE PROVIDED - SETTING TO DEFAULT ({default_title})")
            movie_title = default_title

        # Handle validating movie date
        today = date.today()

        # If it's not a date
        if not isinstance(screening_date, date):
            print(f"DATE OBJECT NOT PROVIDED FOR SCREENING DATE - SETTING TO TODAY ({today})")
            screening_date = today


        # If it's not a time
        if not isinstance(screening_time, time):
            default_time = time(20, 0, 0, 0)
            print(f"TIME OBJECT NOT PROVIDED FOR SCREENING TIME - SETTING TO {default_time})")
            screening_time = default_time

        # VALIDATION COMPLETE - NOW STORE INFORMATION

        # Screening ID has rules about its format, and should not be changed after creation. Therefore, it is encapsulated
        self._screening_id = screening_id

        # Screening title cannot be empty, so encapsulate (this is less important than screening ID as there's no
        # required format, but still useful for consistency later
        self._movie_title = movie_title

        # Screening date and time must be present and must be those types. Therefore, these should be encapsulated
        self._screening_date = screening_date
        self._screening_time = screening_time

    # Type-hinting to indicate it returns a string. No type-hinting needed on self
    def __str__(self) -> str:
        # str is for users, and users doesn't need screening ID so we can leave it out
        return f"{self._movie_title} is on at {self._screening_time} on {self._screening_date}"

    def __repr__(self) -> str:
        # repr is for developers, include all fields and their names
        return f"Screening{{_screening_id={self._screening_id}, _movie_title={self._movie_title}, _screening_date={self._screening_date}, _screening_time={self._screening_time}}}"

    # To cover possibility of returning True/False OR returning NotImplemented, type-hinting has to include both types
    def __eq__(self, other: object) -> bool | NotImplementedType:
        # eq returns true/false where the parameter is the correct type (Screening)
        # It returns NotImplemented where the type is wrong
        if not isinstance(other, Screening):
            return NotImplemented

        # Spec states two Screenings are the same if their ids match (and the case doesn't matter)
        if self._screening_id.lower() != other._screening_id.lower():
            return False

        # As the id is the only value that has to match for them to be equal, if this matches then we can return true
        return True

    def __hash__(self) -> int:
        # Whatever is used as the equality comparison for eq is what we use for hash
        # As eq used only the screening_id, we only pass that into the hash calculation process
        return hash(self._screening_id.lower())

    # We want access to the screening details for the Booking to be able to display it, so we need to create getters:
    def get_screening_time(self) -> time:
        return self._screening_time

    def get_screening_date(self) -> date:
        return self._screening_date

    def get_movie_title(self) -> str:
        return self._movie_title

    def get_screening_id(self) -> str:
        return self._screening_id


class Booking:
    # Spec states a static variable is used to track how many Bookings have been made
    # As this has a specific logic to how it is updated, it should be encapsulated to be protected from random change
    _booking_count = 0

    def __init__(self, screening: Screening, customer_name: str, booking_date: datetime = None):
        # Handle Screening validation
        if not isinstance(screening, Screening):
            print("ALL BOOKED SCREENINGS MUST CONTAIN SCREENING OBJECTS. STORING DEFAULT SCREENING.")
            # Creating a screening just containing Nones will trigger Screening's validation to store the default information
            screening = Screening(None, None)

        # Handle customer name validation
        if not customer_name:
            default_name = "DEFAULT CUSTOMER"
            print(f"ALL CUSTOMERS MUST BE NAMED. SETTING TO DEFAULT CUSTOMER NAME ({default_name})")

        # Handle booking date validation
        # If it's not a date
        if not isinstance(booking_date, datetime):
            now = datetime.now()
            print(f"DATE OBJECT NOT PROVIDED FOR BOOKING DAT - SETTING TO NOW ({now})")
            booking_date = now

        # VALIDATION COMPLETE - Begin storing date
        Booking._booking_count += 1
        self._booking_id = Booking._booking_count
        self._screening = screening
        self._customer_name = customer_name
        self._booking_date = booking_date

    def __str__(self) -> str:
        # Spec states it must be in a user-friendly manner, so the information is formatted as a clear sentence.
        return f"{self._booking_id}: {self._customer_name} booked to see {self._screening.get_movie_title()} at {self._screening.get_screening_time()} on {self._screening.get_screening_date()}"

    def __format__(self, format_spec: str) -> str:
        # If no format (i.e. None) was specified, return str() output
        if not format_spec:
            return str(self)

        # To avoid case sensitivity, convert to lowercase
        match(format_spec.lower()):
            case "brief":
                # Spec states that the brief format should include id, customer name, movie title and scheduling information,
                # so those are included. As these are the same as str output, reuse that!
                return str(self)
            case "complete":
                # Spec states that the complete format should include all information, so every field is included.
                # Spec states it must be in a user-friendly manner, so the information is formatted as a clear sentence.
                return f"{self._booking_id}, {self._booking_date}: {self._customer_name} booked a ticket for {self._screening.get_movie_title()} at {self._screening.get_screening_time()} on {self._screening.get_screening_date()} (screening {self._screening.get_screening_id()})"
            case _:
                # Use str as the default response - this could have been anything and str is convenient because it already exists
                return str(self)


    # To cover possibility of returning True/False OR returning NotImplemented, type-hinting has to include both types
    def __eq__(self, other: object) -> bool | NotImplementedType:
        # eq returns true/false where the parameter is the correct type (Screening)
        # It returns NotImplemented where the type is wrong
        if not isinstance(other, Booking):
            return NotImplemented

        # Spec states two Bookings are the same if their ids match (no need for case neutralisation as the ids are numbers)
        if self._booking_id != other._booking_id:
            return False

        # As the id is the only value that has to match for them to be equal, if this matches then we can return true
        return True

    # Create getter methods for our encapsulated instance variables
    def get_booking_id(self) -> int:
        return self._booking_id

    def get_booking_date(self) -> datetime:
        return self._booking_date

    def get_customer_name(self) -> str:
        return self._customer_name

    def get_screening(self) -> Screening:
        return self._screening

print(Screening(None, None) == Screening("None", None))