import re

def check_password_strength(password):
    # Define rules
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Count total errors
    errors = sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    # Strength levels
    if errors == 0:
        return "✅ Strong Password"
    elif errors <= 2:
        return "⚠️ Medium Password"
    else:
        return "❌ Weak Password"

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    print(check_password_strength(password))
