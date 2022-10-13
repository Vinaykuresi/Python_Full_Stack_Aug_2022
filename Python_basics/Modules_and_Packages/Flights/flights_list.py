flight_seats = 5

def increase_seats(no_of_seats):
    global flight_seats
    flight_seats += no_of_seats
    return flight_seats

def get_no_of_flight_seats():
    return flight_seats