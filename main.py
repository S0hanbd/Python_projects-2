import json
import os
from Contact import Contact
class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.filename = "contacts.json"
        self.load_from_file()





    def load_from_file(self):
        ...