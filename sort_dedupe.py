import sys
import re

def process_numbers():
    # Check if input is being piped or redirected
    if not sys.stdin.isatty():
        raw_input = sys.stdin.read()
    else:
        print("Enter your numbers (separated by spaces, commas, or newlines):")
        raw_input = input()

    # Use regex to find all numbers (handles integers and decimals)
    tokens = re.findall(r'-?\d+(?:\.\d+)?', raw_input)
    
    if not tokens:
        print("No valid numbers found in the input.")
        return

    # Convert string tokens to float or int
    numbers = [float(t) if '.' in t else int(t) for t in tokens]

    # Sort the list from low to high
    numbers.sort()

    # Check for duplicates and track what was removed
    seen = set()
    duplicates = set()
    
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    if duplicates:
        print(f"\nDuplicates found and removed: {sorted(list(duplicates))}")
    else:
        print("\nNo duplicates found.")

    # Remove duplicates while preserving the sorted order
    final_list = sorted(list(seen))

    # Print out the final list
    print(f"Final sorted list without duplicates: {final_list}")

if __name__ == "__main__":
    process_numbers()
