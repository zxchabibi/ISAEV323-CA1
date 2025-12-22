def calc_avg(numbers: list) -> float:
    if not numbers:
        return 0.0  
    return sum(numbers) / len(numbers)
print(calc_avg([10, 20, 30, 40]))
def fmt_fio(parts: list, capitalize: bool = True) -> str:
    fio = " ".join(parts)
    if capitalize:
        return fio.title()
    return fio
print(fmt_fio(["петров", "иван", "сергеевич"]))
print(fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False))
def filter_scores(data_dict: dict, min_value: int) -> dict:

    result = {}
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value         
    return result
scores = {"math": 95, "history": 78, "english": 88, "art": 92}
print(filter_scores(scores, 90))