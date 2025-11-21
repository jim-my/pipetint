from pipetint import BLUE, BOLD, GREEN, RED, YELLOW, colored

print(colored("Success") | GREEN | BOLD)
print(colored("Warning") | YELLOW)
print(colored("Error") | RED | BOLD)
print(colored("Info") | BLUE)
