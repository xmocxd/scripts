import sys
import re

def extract_numbers(text):
    """Extracts all numbers (integers and floats) into a set for comparison."""
    tokens = re.findall(r'-?\d+(?:\.\d+)?', text)
    return {float(t) if '.' in t else int(t) for t in tokens}

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

    # 2. Clean text: Strip out non-numeric, non-whitespace, non-return, non-comma text
    cleaned_text = re.sub(r'[^0-9.\-\s,]', '', raw_input)

    # 3. Parse numbers from the cleaned text, sort, and find duplicates
    tokens = re.findall(r'-?\d+(?:\.\d+)?', cleaned_text)
    
    if not tokens:
        print("No valid numbers found in the input after cleaning.")
        return

    numbers = [float(t) if '.' in t else int(t) for t in tokens]
    
    # Sort numbers from low to high
    numbers.sort()

    # Track duplicates
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    # Final sorted unique list
    final_sorted_unique = sorted(list(seen))

    # 4. Compare original input file numbers vs final sorted/deduplicated numbers
    original_set = extract_numbers(raw_input)
    final_set = set(final_sorted_unique)

    # --- Output Results to stdout ---
    sys.stdout.write("=== PIPELINE RESULTS ===\n")
    
    if duplicates:
        sys.stdout.write(f"Duplicates found and removed: {sorted(list(duplicates))}\n")
    else:
        sys.stdout.write("No duplicates found.\n")


    sys.stdout.write("-" * 40 + "\n")
    sys.stdout.write("Comparison Check (Original File vs. Final Unique List):\n")
    
    if original_set == final_set:
        sys.stdout.write("Result: MATCH! Both represent the exact same set of unique numbers.\n")
    else:
        sys.stdout.write("Result: NO MATCH.\n")
        only_in_orig = original_set - final_set
        only_in_final = final_set - original_set
        if only_in_orig:
            sys.stdout.write(f"Numbers only in original: {sorted(list(only_in_orig))}\n")
        if only_in_final:
            sys.stdout.write(f"Numbers only in final: {sorted(list(only_in_final))}\n")
            

    sys.stdout.write(f"Final sorted unique list: {final_sorted_unique}\n")
    

if __name__ == "__main__":
    main()
