class DatabaseConfig:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    def __init__(self, db_name=None, user=None, password=None):
        if not self._initialized:
            self.db_name = db_name
            self.user = user
            self.password = password
            self._initialized = True
conf1 = DatabaseConfig("shop_db", "admin", "123")
conf2 = DatabaseConfig("users_db", "root", "000")  
print(conf1 is conf2)  
print(conf2.db_name)  
print(conf2.user)      
print(conf2.password)  