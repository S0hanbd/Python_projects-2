class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
    @staticmethod
    def from_dict(contact_dict):
        return Contact(contact_dict["name"], contact_dict["phone"], contact_dict["email"])
    