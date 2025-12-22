def filter_logs(log_list, keyword):
    for log in log_list:
        if keyword in log:
            yield log
logs = [
    "INFO: Server started",
    "ERROR: Database connection failed",
    "INFO: User logged in",
    "ERROR: File not found"]
for error in filter_logs(logs, "ERROR"):
    print(error)