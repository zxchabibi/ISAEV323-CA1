def format_report(report_title, *data, **properties):
  print(f"--- Отчет: {report_title} ---")

  if data:
    print("Данные:")
    for item in data:
      print(f"- {item}")

  if properties:
    print("Свойства:")
    for key, value in properties.items():
      print(f"- {key}: {value}")

  print("----------------------------")

format_report(
    "Ежедневный отчет",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    author="Сидоров А.В.",
    date="2025-11-04"
)
