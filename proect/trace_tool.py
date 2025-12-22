import subprocess
import platform
import sys

def trace_route(destination: str) -> None:
  """
  Выполняет трассировку маршрута до указанного адреса, используя
  системную команду traceroute/tracert.

  Args:
    destination (str): IP-адрес или доменное имя, до которого нужно выполнить трассировку.
  """
  os_name = platform.system()
  command = []

  if os_name == "Windows":
    command = ["tracert", destination]
  elif os_name in ["Linux", "Darwin"]:  # Darwin - это macOS
    command = ["traceroute", destination]
  else:
    print(f"Платформа '{os_name}' не поддерживается для трассировки.")
    return

  print(f"Выполняем трассировку до {destination} на платформе {os_name}...")
  print("-" * 50)

  try:
    # Запускаем системную команду
    # capture_output=True, чтобы получить вывод
    # text=True, чтобы вывод был в виде строк, а не байтов
    # check=False, чтобы не генерировать исключение, если команда завершилась с ошибкой (например, хост недоступен)
    process = subprocess.run(command, capture_output=True, text=True, check=False, encoding='utf-8', errors='replace')

    if process.returncode == 0:
      print(process.stdout)
    else:
      print(f"Команда трассировки завершилась с ошибкой (код: {process.returncode}).")
      if process.stdout:
        print("Стандартный вывод:")
        print(process.stdout)
      if process.stderr:
        print("Стандартная ошибка:")
        print(process.stderr)

  except FileNotFoundError:
    print(f"Ошибка: Команда '{command[0]}' не найдена.")
    print("Убедитесь, что 'tracert' (для Windows) или 'traceroute' (для Linux/macOS) установлен и доступен в PATH.")
  except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

  print("-" * 50)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    target_host = sys.argv[1]
  else:
    target_host = input("Введите IP-адрес или доменное имя для трассировки (например, google.com или 8.8.8.8): ")

  if target_host:
    trace_route(target_host)
  else:
    print("Целевой адрес не указан.")