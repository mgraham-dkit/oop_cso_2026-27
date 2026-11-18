from solutions._LabExams.A_Sem1Exam.entities.tickets import Screening, Booking
import datetime


def create_screening_list() -> list[Screening]:
    screening1 = Screening("S_00001", "Movie 1", datetime.date(2026, 11, 10), datetime.time(12, 0, 0, 0))
    screening2 = Screening("S_00002", "Movie 2", datetime.date(2026, 11, 10), datetime.time(12, 35, 0, 0))
    screening3 = Screening("S_00003", "Movie 3", datetime.date(2026, 11, 10), datetime.time(13, 10, 0, 0))
    screening4 = Screening("S_00004", "Movie 1", datetime.date(2026, 11, 10), datetime.time(14, 30, 0, 0))
    screening5 = Screening("S_00001", "Movie 1", datetime.date(2026, 11, 10), datetime.time(12, 0, 0, 0))
    screening6 = Screening("S_00006", "Movie 3", datetime.date(2026, 11, 10), datetime.time(16, 0, 0, 0))
    screening7 = Screening("S_00007", "Movie 4", datetime.date(2026, 11, 10), datetime.time(18, 30, 0, 0))
    screening8 = Screening("S_00008", "Movie 2", datetime.date(2026, 11, 10), datetime.time(18, 50, 0, 0))
    screening9 = Screening("S_00009", "Movie 3", datetime.date(2026, 11, 10), datetime.time(19, 10, 0, 0))
    screening10 = Screening("S_00001", "Movie 1", datetime.date(2026, 11, 10), datetime.time(12, 0, 0, 0))

    screening_list = [screening1, screening2, screening3, screening4, screening5, screening6, screening7, screening8, screening9, screening10]

    return screening_list


def get_distinct_titles(screening_list: list[Screening]) -> list[str]:
    # Display list of all movie titles for screenings on record - track results in a list
    movie_titles = []
    # Check each screening currently on record, i.e. in our list of screenings
    for screening in screenings:
        # Find out the title (in lowercase so we don't need to worry about sensitivity) of this screening
        current_title = screening.get_movie_title().lower()
        # If we haven't already added it to our list
        # (Remember, each title should be shown only once, so we can't allow duplicates)
        if current_title not in movie_titles:
            # Add it to the list
            movie_titles.append(current_title)

    # Return the final list back so it can be displayed somewhere else
    return movie_titles


def search_screenings(screening_list: list[Screening], target_screening: Screening) -> list[Screening]:
    # Create somewhere to store all screenings with this title
    matches = []
    # Loop through all the screenings
    for screening in screening_list:
        # If this screening is the one we're looking for
        if screening == target_screening:
            # Add it to our list
            matches.append(screening)

    # Return the list of matching screenings
    return matches


def display_technical_details(screening_list: list[Screening]) -> None:
    print("Screening technical details:")
    # Loop through each screening and print out repr version
    for screening in screening_list:
        print(repr(screening))

def display_brief_bookings(booking_dict: dict[int, Booking]) -> None:
    print("Screening technical details:")
    # Loop through each booking in the dictionary (pulling from values) and display with brief format
    for booking in booking_dict.values():
        print(format(booking, "brief"))

if __name__ == "__main__":
    # 1) Set up list of screenings
    # Use a function so the main program is easier to read (and so we could easily change how the list is made later)
    screenings: list[Screening] = create_screening_list()
    bookings: dict[int, Booking] = {}

    # 2) Create three hard-coded bookings and store in the dictionary
    booking_now = Booking(screenings[0], "Theodore", datetime.datetime.now())
    bookings[booking_now.get_booking_id()] = booking_now

    booking_yesterday = Booking(screenings[0], "Alvin", datetime.datetime(2026, 10, 17, 14, 20, 0, 0))
    bookings[booking_yesterday.get_booking_id()] = booking_yesterday

    booking_tomorrow = Booking(screenings[1], "Simon", datetime.datetime(2026, 10, 19, 18, 20, 0, 0))
    bookings[booking_tomorrow.get_booking_id()] = booking_tomorrow

    # 3) Display technical details of all screenings
    display_technical_details(screenings)

    # 4) Display all bookings in brief format
    display_brief_bookings(bookings)

    # 5) Get all distinct movie titles from screenings currently on record
    distinct_titles = get_distinct_titles(screenings)
    print("Movies currently screening:")
    for title in distinct_titles:
        print(title.capitalize())

    # 6) Count how many times an object matching screening1 appears in the list
    # Find all matching screenings
    matching_screenings = search_screenings(screenings, screenings[0])
    # Count and display the count
    count_matches = len(matching_screenings)
    print(f"Number of screenings matching {screenings[0]} = {count_matches}")