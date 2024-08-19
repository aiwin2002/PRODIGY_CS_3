import re

def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate score based on criteria met
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Strength levels
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback and suggestions
    suggestions = []
    if not length_criteria:
        suggestions.append("Increase the password length to at least 8 characters.")
    if not uppercase_criteria:
        suggestions.append("Include at least one uppercase letter.")
    if not lowercase_criteria:
        suggestions.append("Include at least one lowercase letter.")
    if not digit_criteria:
        suggestions.append("Include at least one digit.")
    if not special_char_criteria:
        suggestions.append("Include at least one special character (e.g., !@#$%^&*).")

    return {
        'strength': strength,
        'suggestions': suggestions
    }

def main():
    while True:
        # Get user input
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Exiting the password strength checker. Stay secure!")
            break

        result = check_password_strength(password)
        print(f"Password Strength: {result['strength']}")
        if result['suggestions']:
            print("Suggestions to improve your password:")
            for suggestion in result['suggestions']:
                print(f" - {suggestion}")

if __name__ == "__main__":
    main()
