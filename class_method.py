class Event:
    def __init__(self, name, date, location, attendees):
        self.name = name
        self.date = date
        self.location = location
        self.attendees = attendees

    @classmethod
    def from_string(cls, data_string):
        """
        Class method to simplify object creation from a single string.
        Splits the string by commas and passes the values to the constructor.
        
        Example usage:
            data_string = "Conference,2023-12-25,New York,500"
            event = Event.from_string(data_string)
        
        This avoids manually splitting the string and calling the constructor.
        """
        data = data_string.split(',')
        return cls(data[0], data[1], data[2], int(data[3]))
        
    def __str__(self):
        return f"Event[name={self.name}, date={self.date}, location={self.location}, attendees={self.attendees}]"


def main():
    # Example usage of the class method to simplify instantiation
    data_string = "Conference,2023-12-25,New York,500"
    event = Event.from_string(data_string)
    print(event)


if __name__ == "__main__":
    main()
