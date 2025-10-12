"""
Isaac Henderson - PE#6
COP2373 
Regular Expression Validation Program

This program validates phone numbers, social security numbers, and zip codes
using regular expressions.
"""

import re


def validate_phone_number(phone):
    # Pattern allows for optional parentheses around area code,
    # various separators (space, dash, dot), and optional spaces
    pattern = r'^(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})$'
    return bool(re.match(pattern, phone.strip()))


def validate_ssn(ssn):
   
    # Pattern for SSN: 3 digits, optional dash, 2 digits,
    # optional dash, 4 digits
    pattern = r'^\d{3}-?\d{2}-?\d{4}$'
    return bool(re.match(pattern, ssn.strip()))


def validate_zip_code(zip_code):
    
    # Pattern for ZIP: 5 digits, optionally followed by dash and 4 more digits
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code.strip()))


def get_user_input():
    
    while True:
        print("\nEnter the following information to validate:")
        
        # Get phone number
        phone = input("Phone Number: ").strip()
        phone_valid = validate_phone_number(phone)
        status = 'VALID' if phone_valid else 'INVALID'
        print(f"Phone Number '{phone}' is {status}")
        
        # Get SSN
        ssn = input("Social Security Number: ").strip()
        ssn_valid = validate_ssn(ssn)
        print(f"SSN '{ssn}' is {'VALID' if ssn_valid else 'INVALID'}")
        
        # Get ZIP code
        zip_code = input("ZIP Code: ").strip()
        zip_valid = validate_zip_code(zip_code)
        status = 'VALID' if zip_valid else 'INVALID'
        print(f"ZIP Code '{zip_code}' is {status}")
        
        # Summary
        print("\nSUMMARY:")
        print(f"Phone Number: {'✓' if phone_valid else '✗'}")
        print(f"SSN:          {'✓' if ssn_valid else '✗'}")
        print(f"ZIP Code:     {'✓' if zip_valid else '✗'}")
        
        if phone_valid and ssn_valid and zip_valid:
            print("🎉 All entries are valid!")
        else:
            print("❌ Some entries need correction.")
        
        # Ask if user wants to continue
        continue_choice = input("\nWould you like to validate another "
                                "set? (y/n): ").strip().lower()
        if continue_choice not in ['y', 'yes']:
            break


def main():
    """
    Main function to run the validation program.
    """


print("Regular Expression Validation Program")

# Get user input for validation
get_user_input()

print("\nThank you for using the validation program!")


if __name__ == "__main__":
    main()
