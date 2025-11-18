from typing import List, Union, Dict

def calc_avg(numbers: List[Union[int, float]]) -> float:
  if not numbers:
    return 0.0
  return sum(numbers) / len(numbers)

def fmt_fio(parts: List[str], capitalize: bool = True) -> str:
  fio = " ".join(parts)
  if capitalize:
    return fio.title()
  return fio

def filter_scores(data_dict: Dict[str, Union[int, float]], min_value: Union[int, float]) -> Dict[str, Union[int, float]]:
  result = {}
  for key, value in data_dict.items():
    if value >= min_value:
      result[key] = value
  return result

print("--- Функция 1: calc_avg ---")
print(f"Среднее для [10, 20, 30, 40]: {calc_avg([10, 20, 30, 40])}")
print(f"Среднее для []: {calc_avg([])}")
print(f"Среднее для [5, 10, 15]: {calc_avg([5, 10, 15])}")
print(f"Среднее для [1.5, 2.5, 3.0]: {calc_avg([1.5, 2.5, 3.0])}")
print("-" * 30)

print("--- Функция 2: fmt_fio ---")
print(f"ФИО с капитализацией: {fmt_fio(['петров', 'иван', 'сергеевич'])}")
print(f"ФИО без капитализации: {fmt_fio(['сидорова', 'анна', 'валериевна'], capitalize=False)}")
print(f"ФИО с капитализацией (имена с произвольным регистром): {fmt_fio(['иВаН', 'пЕтРоВ'])}")
print("-" * 30)

print("--- Функция 3: filter_scores ---")
scores = {"math": 95, "history": 78, "english": 88, "art": 92, "chemistry": 60}
print(f"Исходные оценки: {scores}")
print(f"Оценки >= 90: {filter_scores(scores, 90)}")
print(f"Оценки >= 80: {filter_scores(scores, 80)}")
print(f"Оценки >= 100: {filter_scores(scores, 100)}")
print("-" * 30)
