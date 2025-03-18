import base64
import json
import sys

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

    try:
        # Parse the decoded content as JSON
        data = json.loads(decoded_content)

        # Search for the PR number in the JSON and get the corresponding test result
        pr_data = data.get(pr_number, None)
        if pr_data:
            return pr_data.get("test_result", "Test result not found.")
        else:
            return f"PR number {pr_number} not found in the decoded content."
    except json.JSONDecodeError:
        return "Error decoding JSON content."

if __name__ == '__main__':
    # Get PR number and base64 content from command-line arguments
    pr_number = sys.argv[1]  # PR number passed as the first argument
    base64_content = sys.argv[2]  # Base64 content passed as the second argument
    
    # Get the test result for the given PR number
    result = get_test_result(pr_number, base64_content)

    # Output result to stdout so GitHub Actions can capture it
    print(result)
