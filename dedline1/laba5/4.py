numbers = []
for i in range(5):
  try:
    numbers.append(float(input(f"Число {i+1}: ")))
  except:
    print("Ошибка")
if numbers:
  print(f"Мин: {min(numbers)}")
  print(f"Макс: {max(numbers)}")
else:
  print("Нет чисел")