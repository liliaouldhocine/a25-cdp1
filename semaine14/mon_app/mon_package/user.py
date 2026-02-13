class User():
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def greetings(self):
        return f"Bonjour {self.name}"
    
    def get_address(self):
        return f"{self.address.city}, {self.address.country}"