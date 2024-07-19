import re

# List of common SQL injection patterns
patterns = [
    r"\'\s*--",   # Single quote followed by comment
    r"\"\\s*--",  # Double quote followed by comment
    r"\bOR\b",    # OR keyword
    r"\bAND\b",   # AND keyword
    r"\bSELECT\b",# SELECT keyword
    r"\bUNION\b", # UNION keyword
    r"\bDROP\b",  # DROP keyword
    r"\bINSERT\b",# INSERT keyword
    r"\bUPDATE\b",# UPDATE keyword
    r"\bDELETE\b",# DELETE keyword
]

def check_for_sql_injection(user_input):
    for pattern in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return True
    return False

def main():
    user_input = input("Enter a query or input to check: ")
    
    if check_for_sql_injection(user_input):
        print("Warning: Potential SQL injection detected.")
    else:
        print("No SQL injection patterns detected.")

if __name__ == "__main__":
    main()
