import sys
import re

def extract_number_and_text(line):
    """Extracts number and associated non-numeric text from a line.
    Returns a tuple of (number, original_line_text) or None if no number found."""
    match = re.search(r'-?\d+(?:\.\d+)?', line)
    if match:
        number = float(match.group()) if '.' in match.group() else int(match.group())
        return (number, line)
    return None

def main():
    # Ensure an input file argument is provided
    if len(sys.argv) != 2:
        print("Usage: python number_pipeline.py <input_file>", file=sys.stderr)
        sys.exit(1)

    input_file_path = sys.argv[1]

    # 1. Read the original input file
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            raw_input = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading '{input_file_path}': {e}", file=sys.stderr)
        sys.exit(1)

    if not raw_input:
        print("The input file is empty.")
        return

    # 2. Process each line: extract number and preserve associated text
    lines = raw_input.split('\n')
    number_line_pairs = []
    duplicates = {}  # Track which numbers are duplicated
    
    for line in lines:
        if line.strip():  # Skip empty lines
            result = extract_number_and_text(line)
            if result:
                number, original_text = result
                number_line_pairs.append((number, original_text))
                # Track duplicates
                if number in duplicates:
                    duplicates[number] += 1
                else:
                    duplicates[number] = 1

    if not number_line_pairs:
        print("No valid numbers found in the input.")
        return

    # 3. Sort by number (keeping original text attached)
    number_line_pairs.sort(key=lambda x: x[0])

    # Identify which numbers are duplicates
    duplicate_numbers = {num for num, count in duplicates.items() if count > 1}

    # 4. Output Results
    sys.stdout.write("=== PIPELINE RESULTS ===\n")
    
    if duplicate_numbers:
        sys.stdout.write(f"Duplicates found: {sorted(list(duplicate_numbers))}\n")
    else:
        sys.stdout.write("No duplicates found.\n")

    sys.stdout.write("-" * 40 + "\n")
    sys.stdout.write("Sorted Output (with preserved text):\n")
    sys.stdout.write("-" * 40 + "\n")

    for number, original_text in number_line_pairs:
        sys.stdout.write(f"{original_text}\n")
    

if __name__ == "__main__":
    main()
