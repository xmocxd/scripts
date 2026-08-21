import sys
import re

def extract_numbers(filename):
    """Reads a file and extracts all numbers into a set."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading '{filename}': {e}", file=sys.stderr)
        sys.exit(1)

    # Extract all numbers (integers and floats) using regex
    tokens = re.findall(r'-?\d+(?:\.\d+)?', content)
    
    # Convert tokens to float or int for accurate numerical comparison
    return {float(t) if '.' in t else int(t) for t in tokens}

def main():
    # Expecting two file arguments: python compare_lists.py file1.txt file2.txt
    if len(sys.argv) != 3:
        print("Usage: python compare_lists.py <file1> <file2>")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    # Extract numbers from both files into sets
    set1 = extract_numbers(file1_path)
    set2 = extract_numbers(file2_path)

    print(f"File 1 unique numbers count: {len(set1)}")
    print(f"File 2 unique numbers count: {len(set2)}")
    print("-" * 40)

    # Compare the two sets
    if set1 == set2:
        print("Result: MATCH! Both lists contain the exact same numbers.")
    else:
        print("Result: NO MATCH. The lists contain different numbers.")
        
        # Optional: Show what is unique to each list
        only_in_1 = set1 - set2
        only_in_2 = set2 - set1
        
        if only_in_1:
            print(f"Numbers only in {file1_path}: {sorted(list(only_in_1))}")
        if only_in_2:
            print(f"Numbers only in {file2_path}: {sorted(list(only_in_2))}")

if __name__ == "__main__":
    main()
