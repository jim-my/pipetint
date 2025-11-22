"""Color Removal Examples - Stripping ANSI codes from text.

Demonstrates how to remove colors from text using pipetint's remove_color functionality.
"""

import tempfile

from pipetint import Colorize, ColorizedString

print("=" * 60)
print("Color Removal Examples")
print("=" * 60)
print()

# Example 1: Remove colors using Colorize
print("1. Remove colors using Colorize class")
print("-" * 60)
colorizer = Colorize()

# Simulate colored text from terminal
colored_text = "\033[31mERROR\033[0m: Connection failed at \033[34m10:30:45\033[0m"
print(f"Original: {colored_text}")

clean_text = colorizer.remove_color(colored_text)
print(f"Cleaned:  {clean_text}")
print()

# Example 2: Remove colors using ColorizedString
print("2. Remove colors using ColorizedString")
print("-" * 60)
cs = ColorizedString("Log processing started").highlight(
    r"processing", ["green", "bold"]
)
print(f"Colored:  {cs}")

clean = cs.remove_color()
print(f"Cleaned:  {clean}")
print()

# Example 3: Pipeline processing - colorize then clean
print("3. Pipeline: Colorize for display, then extract plain text")
print("-" * 60)

log_lines = [
    "INFO: Server started successfully",
    "WARN: High memory usage detected",
    "ERROR: Database connection failed",
]

for line in log_lines:
    # Create colored version for display
    colored = ColorizedString(line)

    if "ERROR" in line:
        colored = colored.highlight(r"ERROR", ["red", "bold"])
    elif "WARN" in line:
        colored = colored.highlight(r"WARN", ["yellow"])
    elif "INFO" in line:
        colored = colored.highlight(r"INFO", ["blue"])

    # Display colored version
    print(f"Display: {colored}")

    # Extract plain text for logging/storage
    plain = str(colored.remove_color())
    print(f"Store:   {plain}")
    print()

# Example 4: Processing colored terminal output
print("4. Extract data from colored terminal output")
print("-" * 60)

# Simulate output from a tool that uses colors
terminal_output = [
    "\033[32m[PASS]\033[0m test_authentication.py",
    "\033[31m[FAIL]\033[0m test_database.py",
    "\033[32m[PASS]\033[0m test_api.py",
]

# Count failures by stripping colors first
failures = []
for line in terminal_output:
    clean_line = colorizer.remove_color(line)
    if "[FAIL]" in clean_line:
        # Extract filename
        filename = clean_line.split()[1]
        failures.append(filename)

print("Failed tests:")
for f in failures:
    print(f"  - {f}")
print()

# Example 5: Save colored output to file (plain text)
print("5. Save plain text version")
print("-" * 60)

# Create colored status message
status = ColorizedString("Deployment completed successfully!")
status = status.highlight(r"successfully", ["green", "bold"])

print(f"Display to user: {status}")

# Save to file without colors using tempfile for security
with tempfile.NamedTemporaryFile(
    mode="w", delete=False, suffix=".txt", encoding="utf-8"
) as f:
    f.write(str(status.remove_color()))
    temp_path = f.name

print(f"Saved plain text to: {temp_path}")
print()

print("=" * 60)
print("✅ Color removal examples completed!")
print("=" * 60)
