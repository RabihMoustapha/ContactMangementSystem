import phonenumber

class Contact:
    phone_number = None

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.firstname = first_name
        self.lastname = last_name
        self.phone_number = []

    def __str__(self):
        return f"Contact(id={self.id}, firstname={self.firstname}, lastname={self.lastname}, phone_number={self.phone_number})"

    def get_id(self):
        return self.id

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_phone_number(self):
        return self.phone_number

    def add_phone_number(self, phone_number, id, country_code):
        self.phone_number.append(phonenumber.PhoneNumber(phone_number, id, country_code))