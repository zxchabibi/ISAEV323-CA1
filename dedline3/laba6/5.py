class SmartList(list):
    def __getitem__(self, index):
        if isinstance(index, int) and index < 0:
            index = -index - 1
        return super().__getitem__(index)
s1 = SmartList([10, 20, 30])
print(s1[0])    
print(s1[-1])  
print(s1[-2])   