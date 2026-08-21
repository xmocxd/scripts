import sys
import re

def main():
    # Read everything from stdin (piped input)
    raw_input = sys.stdin.read()
    
    if not raw_input:
        return

    # Regex explanation:
    # Keeps digits (\d), periods (.) for decimals, minus signs (-) for negative numbers,
    # spaces, tabs (\t), newlines (\n, \r), and commas (,).
    # Anything else is stripped out.
    cleaned_output = re.sub(r'[^0-9.\-\s,]', '', raw_input)

    # Output the cleaned text directly to stdout
    sys.stdout.write(cleaned_output)

if __name__ == "__main__":
    main()
