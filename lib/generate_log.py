from datetime import datetime


def generate_log(log_data):
    """
    Generate a log file with timestamped filename containing log entries.
    
    Args:
        log_data: A list of log entries (strings)
    
    Returns:
        str: The filename of the created log file
    
    Raises:
        ValueError: If log_data is not a list
    
    Example:
        >>> generate_log(["User logged in", "User updated profile"])
        Log written to log_20240610.txt
        'log_20240610.txt'
    """
    # Validate input is a list
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")
    
    # Create timestamped filename in format log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # Write log entries to file
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    
    # Print confirmation message with filename
    print(f"Log written to {filename}")
    
    return filename