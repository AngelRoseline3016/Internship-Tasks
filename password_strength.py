#!/usr/bin/env python3
"""
Password Strength Assessment Tool
"""

def assess_password_strength(password):
    """Evaluate password strength based on various criteria"""
    
    # Initialize strength score
    strength = 0
    
    # Criteria checks
    if len(password) >= 8:
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(not c.isalnum() for c in password):
        strength += 1
    
    # Provide feedback based on score
    if strength == 0:
        return "Very Weak: Password is too short and lacks variety."
    elif strength == 1:
        return "Weak: Password is too short or lacks variety."
    elif strength == 2:
        return "Moderate: Password has some variety but is still weak."
    elif strength == 3:
        return "Good: Password has good variety but could be stronger."
    elif strength == 4:
        return "Strong: Password has excellent variety."
    elif strength == 5:
        return "Excellent: Password meets all criteria."

def main():
    # Get password input
    password = input("Enter your password: ")
    
    # Assess strength
    result = assess_password_strength(password)
    
    # Output result
    print(result)

if __name__ == "__main__":
    main()
