#!/bin/bash
# Color Removal CLI Examples
# Demonstrates how to use --remove-color and --output-format flags

echo "======================================================================"
echo "Color Removal CLI Examples"
echo "======================================================================"
echo ""

# Example 1: Strip colors from colored text
echo "1. Strip ANSI colors from text"
echo "----------------------------------------------------------------------"
echo "Input: Colored ERROR message"
echo -e "\033[31mERROR\033[0m: Connection failed" | tee /dev/tty | pipetint --remove-color
echo ""

# Example 2: Clean up log files
echo "2. Clean up log files (remove colors before saving)"
echo "----------------------------------------------------------------------"
echo "Simulating colored log output..."
(
    echo -e "\033[32mINFO\033[0m: Server started"
    echo -e "\033[33mWARN\033[0m: High memory usage"
    echo -e "\033[31mERROR\033[0m: Connection failed"
) > /tmp/colored.log

echo "Original (with colors):"
cat /tmp/colored.log

echo ""
echo "Cleaned (colors removed):"
cat /tmp/colored.log | pipetint --remove-color
echo ""

# Example 3: Pipeline - colorize then strip for processing
echo "3. Pipeline: Colorize for display, strip for data processing"
echo "----------------------------------------------------------------------"
echo "Count ERROR lines (without color codes interfering):"

cat /tmp/colored.log | \
    pipetint 'ERROR' red | \
    tee >(echo "Display:"; cat) | \
    pipetint --remove-color | \
    grep -c ERROR | \
    xargs -I {} echo "Error count: {}"
echo ""

# Example 4: Output format - plain
echo "4. Using --output-format=plain"
echo "----------------------------------------------------------------------"
echo "Same as --remove-color:"
cat /tmp/colored.log | pipetint --output-format=plain
echo ""

# Example 5: Output format - HTML
echo "5. Convert to HTML format (with inline styles)"
echo "----------------------------------------------------------------------"
echo "Creating HTML output..."
echo "SUCCESS: Deployment complete" | pipetint 'SUCCESS' green --output-format=html > /tmp/output.html
echo "Saved to /tmp/output.html:"
cat /tmp/output.html
echo ""

# Example 6: Real-world use case - Extract plain text from test results
echo "6. Real-world: Extract plain test results"
echo "----------------------------------------------------------------------"

# Simulate test output with colors
(
    echo -e "\033[32m✓\033[0m test_auth passed"
    echo -e "\033[31m✗\033[0m test_db failed"
    echo -e "\033[32m✓\033[0m test_api passed"
) > /tmp/test_results.txt

echo "Test results (colored):"
cat /tmp/test_results.txt

echo ""
echo "Extracting failed tests (plain text):"
cat /tmp/test_results.txt | \
    pipetint --remove-color | \
    grep failed
echo ""

# Cleanup
rm -f /tmp/colored.log /tmp/output.html /tmp/test_results.txt

echo "======================================================================"
echo "✅ Color removal CLI examples completed!"
echo "======================================================================"
