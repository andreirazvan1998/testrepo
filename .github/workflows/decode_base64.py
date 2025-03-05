import base64
import json
import sys
import os

def decode_base64(input_str):
    # Add padding if necessary
    padding_needed = len(input_str) % 4
    if padding_needed:
        input_str += '=' * (4 - padding_needed)

    try:
        # Decode the Base64 content
        decoded_bytes = base64.b64decode(input_str)
        decoded_str = decoded_bytes.decode('utf-8')  # Assuming UTF-8 encoded string
        return decoded_str
    except Exception as e:
        return f"Error decoding: {e}"

def get_test_result(pr_number, base64_content):
    # Decode the Base64 content
    decoded_content = decode_base64(base64_content)

    # Output the decoded content in a format that GitHub Actions can read
    print(f"Decoded content for PR {pr_number}: {decoded_content}")
    return decoded_content

if __name__ == '__main__':
    # Get PR number and base64 content from environment variables
    pr_number = sys.argv[1]  # PR number passed as the first argument
    base64_content = sys.argv[2]  # Base64 content passed as the second argument
    
    result = get_test_result(pr_number, base64_content)
    # Output result to stdout so GitHub Actions can capture it
    print(result)
