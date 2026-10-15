import contact

class Group:
    contacts = None

    def __init__(self, name, id, description):
        self.name = name
        self.id = id
        self.description = description
        self.contacts = []

        def __str__(self):
            return f"Group(name={self.name}, id={self.id}, description={self.description})"

        def get_id(self):
            return self.id

        def get_name(self):
            return self.name

        def get_description(self):
            return self.description

        def get_contacts(self):
            return self.contacts

        def add_contact(self, id, first_name, last_name):
            self.contacts.append(contact.Contact(id, first_name, last_name))