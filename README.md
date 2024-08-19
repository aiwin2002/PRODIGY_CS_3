# SentinelPass

**SentinelPass** is a Python tool designed to evaluate the strength of a password and provide suggestions for improvement. This tool is essential for anyone looking to enhance their password security by ensuring it meets common criteria for strength.

## Features

- **Criteria Evaluation**: Checks password against five criteria:
  - Minimum length of 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character (e.g., !@#$%^&*)
- **Strength Levels**: Categorizes the password strength as:
  - Very Strong
  - Strong
  - Moderate
  - Weak
  - Very Weak
- **Feedback and Suggestions**: Provides actionable suggestions to improve the password if it does not meet all criteria.

## Usage

1. **Clone the repository:**


    ```bash
    
    git clone https://github.com/aiwin2002/PRODIGY_CS_3.git
    
    ```

1. Navigate to the project directory:
   
    ```bash
    cd PRODIGY_CS_3
    ```

2. Run the script:
   
    ```bash
    python SentinelPass.py
    ```

3. Follow the prompts to enter your password. SentinelPass will display the strength of your password and suggest improvements if necessary.

## Example

```plaintext
Enter your password (or type 'exit' to quit): Test@123
Password Strength: Very Strong

Enter your password (or type 'exit' to quit): test
Password Strength: Very Weak
Suggestions to improve your password:
 - Increase the password length to at least 8 characters.
 - Include at least one uppercase letter.
 - Include at least one digit.
 - Include at least one special character (e.g., !@#$%^&*).
