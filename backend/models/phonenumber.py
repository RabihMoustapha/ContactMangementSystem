class PhoneNumber:
    def __init__(self, number, id, country_code):
        self.number = number
        self.id = id
        self.country_code = country_code

        def __str__(self):
            return f"PhoneNumber(number={self.number}, id={self.id}, country_code={self.country_code})"

        def get_number(self):
            return self.number

        def get_id(self):
            return self.id

        def get_country_code(self):
            return self.country_code