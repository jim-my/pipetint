from pipetint import BG_WHITE, BLUE, BOLD, DIM, RED, YELLOW, colored

print(colored("SYSTEM ALERT") | RED | BOLD | BG_WHITE)
print(str(colored("DEBUG") | DIM) + " - Application started")
print(str(colored("INFO") | BLUE) + " - User logged in")
print(str(colored("WARNING") | YELLOW | BOLD) + " - Memory usage high")
print(str(colored("ERROR") | RED | BOLD) + " - Database connection failed")
