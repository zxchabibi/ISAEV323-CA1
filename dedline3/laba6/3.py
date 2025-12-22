class мультиплеер:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, number):
        return self.factor * number
by_5 = мультиплеер(5)
print(by_5(10)) 
print(by_5(2))   