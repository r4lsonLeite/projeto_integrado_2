from user import User


class Address():
    def __init__(self, user: User, street: str, city: str, country: str, zip_code: int,):
        
        self.user = user
        self.street = street
        self.city = city
        self.coutry = country
        self.zip_code = zip_code
        
        def __str__(self):
            return f"{self.street}, {self.city} - {self.country} ({self.zip_code})"
    
    pass
    