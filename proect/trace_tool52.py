
import subprocess
import platform
import sys
import os # Для os.path.join, если понадобится более сложная обработка пути
import logging # Для модуля логирования

def trace_route(destination: str, output_filename: str = None, use_logging: bool = False) -> None:
  """
  Выполняет трассировку маршрута до указанного адреса, используя
  системную команду traceroute/tracert.
  Выводит трассировку построчно и может записывать результат в файл.

  Args:
    destination (str): IP-адрес или доменное имя, до которого нужно выполнить трассировку.
    output_filename (str, optional): Имя файла для записи вывода трассировки. Если None, вывод в файл не производится.
    use_logging (bool, optional): Если True, использует модуль logging для записи в файл, иначе -
                                 обычную запись в файл. При use_logging=True, output_filename
                                 становится лог-файлом.
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

  file_handle = None
  logger = None

  if output_filename:
    if use_logging:
      # Настройка логирования
      logger = logging.getLogger("traceroute_logger")
      logger.setLevel(logging.INFO)
      
      # Очищаем существующие хэндлеры, чтобы избежать дублирования при повторных вызовах
      if logger.hasHandlers():
        logger.handlers.clear()

      try:
        file_handler = logging.FileHandler(output_filename, encoding='utf-8', errors='replace')
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        print(f"Результат трассировки будет записан в лог-файл: {output_filename}")
      except IOError as e:
        print(f"Ошибка: Не удалось открыть лог-файл {output_filename}: {e}")
        logger = None # Отключаем логирование, если файл недоступен
    else:
      try:
        file_handle = open(output_filename, 'w', encoding='utf-8', errors='replace')
        print(f"Результат трассировки будет записан в файл: {output_filename}")
      except IOError as e:
        print(f"Ошибка: Не удалось открыть файл {output_filename} для записи: {e}")
        return

  try:
    # Используем Popen для построчного вывода.
    # encoding='utf-8', errors='replace' позволяет Popen автоматически декодировать
    # байтовый вывод в строки, заменяя невалидные символы.
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', errors='replace')

    # Читаем и выводим stdout построчно
    for line in process.stdout:
      sys.stdout.write(line) # Используем sys.stdout.write, чтобы сохранить оригинальные переводы строк
      if file_handle:
        file_handle.write(line)
      if logger:
        logger.info(line.strip()) # .strip() убирает переводы строк, т.к. logging добавляет свои

    # Ждем завершения процесса и получаем код возврата
    process.wait()

    if process.returncode == 0:
      pass # Успешно, stdout уже выведен
    else:
      # Если команда завершилась с ошибкой, выводим stderr
      print(f"Команда трассировки завершилась с ошибкой (код: {process.returncode}).")
      stderr_output = process.stderr.read() # Читаем весь stderr
      if stderr_output:
        print("Стандартная ошибка:")
        sys.stderr.write(stderr_output)
        if file_handle:
          file_handle.write("\n--- Стандартная ошибка ---\n")
          file_handle.write(stderr_output)
        if logger:
          logger.error("\n--- Стандартная ошибка ---")
          logger.error(stderr_output.strip())

  except FileNotFoundError:
    error_msg = f"Ошибка: Команда '{command[0]}' не найдена.\n" \
                "Убедитесь, что 'tracert' (для Windows) или 'traceroute' (для Linux/macOS) установлен и доступен в PATH."
    print(error_msg)
    if file_handle:
      file_handle.write(error_msg + "\n")
    if logger:
      logger.error(error_msg)
  except Exception as e:
    error_msg = f"Произошла непредвиденная ошибка: {e}"
    print(error_msg)
    if file_handle:
      file_handle.write(error_msg + "\n")
    if logger:
      logger.error(error_msg)
  finally:
    # Закрываем файловый хэндл, если он был открыт
    if file_handle:
      file_handle.close()
    # Логгеру не требуется явное закрытие здесь, FileHandler закроется сам при завершении программы
    # или при очистке хэндлеров.
    if logger:
        # Убедимся, что все хэндлеры закрыты и удалены для этого логгера
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)

  print("-" * 50)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    target_host = sys.argv[1]
  else:
    target_host = input("Введите IP-адрес или доменное имя для трассировки (например, google.com или 8.8.8.8): ")

  if not target_host:
    print("Целевой адрес не указан.")
  else:
    output_file = None
    output_choice = input("Записать результат трассировки в файл? (y/n, по умолчанию 'n'): ").lower()
    if output_choice == 'y':
      output_file = input("Введите имя файла для записи (например, traceroute_result.txt): ")
      if not output_file:
        print("Имя файла не указано, запись в файл отменена.")
        output_file = None

    use_logging_option = False
    if output_file: # Предлагаем использовать logging только если пользователь выбрал запись в файл
      logging_choice = input("Использовать модуль 'logging' для записи в файл? (y/n, по умолчанию 'n'): ").lower()
      if logging_choice == 'y':
        use_logging_option = True

    trace_route(target_host, output_file, use_logging_option)
