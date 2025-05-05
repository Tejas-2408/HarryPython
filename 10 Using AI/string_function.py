import re

def convert_to_dash_format(text):
    # Replace any sequence of non-alphanumeric characters with a single dash
    dashed = re.sub(r'[^a-zA-Z0-9]+', '-', text)
    # Remove leading and trailing dashes, if any
    return dashed.strip('-')

# Test cases
test_strings = [
    "hey how are you",
    "hello@world!",
    " multiple   spaces ",
    "Python_is#awesome!",
    "clean-this_up--please",
    "UPPER and lower CASE",
]

# Run and print results
for s in test_strings:
    print(f"Original: {s!r} -> Converted: {convert_to_dash_format(s)}")