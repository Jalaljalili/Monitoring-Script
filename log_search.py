log_file_path = "/path/to/logfile.log"
search_term = "error"

try:
    # Open the log file
    with open(log_file_path, "r") as f:
        # Read the entire file and count the number of occurrences of the search term
        num_occurrences = f.read().count(search_term)
    
    # Print the number of occurrences
    print(f"Number of occurrences of '{search_term}' in '{log_file_path}': {num_occurrences}")
    
except FileNotFoundError:
    print(f"Log file not found: {log_file_path}")
