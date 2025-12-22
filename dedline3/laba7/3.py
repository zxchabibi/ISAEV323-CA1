class StringUtils:
    @staticmethod
    def invert(string):
        return string[::-1]
    @staticmethod
    def normalize(string):
        return string.strip().lower()
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    @classmethod
    def from_string(cls, data_string):
        name, role = data_string.split(";")
        return cls(name, role)
print(StringUtils.invert("Hello"))  
print(StringUtils.normalize(" DATA "))  
user = User.from_string("Alice;Admin")
print(user.name)  
print(user.role)  