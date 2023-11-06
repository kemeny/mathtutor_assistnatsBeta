
# Math Tutor Assistant

## Introduction
The Math Tutor Assistant is a web-based application designed to help users with their math questions by leveraging the power of OpenAI's GPT-4. Built with Streamlit, this app offers a friendly chat interface where users can input their math problems and receive step-by-step assistance.

## Features
- **Interactive Chat Interface**: Engage in a conversational manner with the Math Tutor Assistant.
- **Powered by OpenAI GPT-4**: Utilize the advanced capabilities of GPT-4 for solving mathematical problems.
- **Session State Memory**: Keeps track of your questions and answers during the session.
- **Error Handling**: Informs users if there is an issue with the OpenAI API connection.

## Installation

Before running the application, make sure you have the following prerequisites installed:

- Python 3.6+
- Streamlit
- OpenAI Python library
- `python-dotenv` library for environment management

Follow these steps to set up the application:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/math-tutor-assistant.git
   cd math-tutor-assistant
   ```

2. **Install dependencies:**
   ```sh
   pip install streamlit openai python-dotenv
   ```

3. **Environment Variables:**
   Create a `.env` file in the root of your project directory and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY='your_api_key_here'
   ```

## Running the Application
To start the application, use the following command:
```sh
streamlit run app.py
```
The app will be served locally and can be accessed through a web browser.

## How to Use
1. Enter your math question in the provided chat input.
2. Submit your question to receive a response from the Math Tutor Assistant.
3. View the step-by-step guidance provided by the GPT-4 powered assistant.

## Important Notes
- Ensure that you have a valid OpenAI API key with access to the GPT-4 model.
- The application needs to be connected to the internet to interact with the OpenAI API.

## Troubleshooting
If the application encounters any errors, such as an invalid API key or loss of internet connectivity, it will prompt you with a message to check your settings or connection.

## Support
For questions, issues, or feature requests, please file an issue through the GitHub repository issue tracker.

## License
Include your license information here.

---

Enjoy using the Math Tutor Assistant to enhance your math learning and problem-solving experience!
