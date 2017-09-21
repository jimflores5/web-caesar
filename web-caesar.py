import string

def alphabet_position(letter):
    start_value = letter.lower()
    alpha_lower = string.ascii_lowercase
    position = alpha_lower.index(start_value)
    return position

def rotate_character(char,rot):
    alpha_lower = string.ascii_lowercase 
    alpha_upper = string.ascii_uppercase

    if char not in alpha_lower and char not in alpha_upper:
        new_letter = char
    elif char in alpha_lower:
        new_letter = alpha_lower[(alphabet_position(char)+rot)%26]
    else:
        temp_letter = alpha_upper[(alphabet_position(char)+rot)%26]
        new_letter = temp_letter.upper()
    return new_letter

def encrypt(text,rot):
    new_text = ""

    for char in text:
        new_text += rotate_character(char,rot)

    return new_text

def main():
    message = input("Enter a message to encrypt:")
    shift = int(input("Shift by:"))
    print(encrypt(message,shift))

if __name__ == "__main__":
    main()