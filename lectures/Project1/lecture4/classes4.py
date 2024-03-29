class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

        # Keep track of this flight's id, then increment (for next created Flight)
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of this flight's passengers.
        self.passengers = []

        # Details about this flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f'\nFlight origin: {self.origin}')
        print(f'Flight destination: {self.destination}')
        print(f'Flight duration: {self.duration}')
        print(f'Flight id: {self.id}')

        print('\nPassengers:')
        for passenger in self.passengers:
            print(f'{passenger.name}')

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:

    def __init__(self, name):
        self.name = name

def main():

    # Create flight.
    flight = Flight(origin='New York', destination='Paris', duration=540)

    # Create passengers.
    alice = Passenger(name='Alice')
    bob = Passenger(name='Bob')

    # Add passengers.
    flight.add_passenger(alice)
    flight.add_passenger(bob)
    flight.add_passenger(Passenger(name='Charlie'))

    # Print flight information.
    flight.print_info()

    flight2 = Flight(origin="Boston", destination="Las Vegas", duration = 1200)
    flight2.add_passenger(alice)
    flight2.add_passenger(bob)
    flight2.add_passenger(Passenger(name='Chris'))

    flight2.print_info()

if __name__ == '__main__':
    main()
