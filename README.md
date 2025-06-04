# Python Firebase Project

This is a basic Python project setup with Firebase integration.

## Setup Instructions

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up Firebase:
   - Go to the [Firebase Console](https://console.firebase.google.com/)
   - Create a new project or select an existing one
   - Go to Project Settings > Service Accounts
   - Generate a new private key (this will download a JSON file)
   - Rename the downloaded file to `serviceAccountKey.json` and place it in the project root

3. Run the project:
   ```
   python main.py
   ```

## Project Structure
- `main.py`: Main application file with Firebase initialization
- `requirements.txt`: Project dependencies
- `serviceAccountKey.json`: Firebase credentials (you need to add this)

## Security Note
- Never commit your `serviceAccountKey.json` to version control
- Consider using environment variables for sensitive information 