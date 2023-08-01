# Chatbot README.md

This README.md file provides an overview and explanation of the Chatbot code created by Harsh Gupta (Desparete Enuf). The code is written in Python using the tkinter library to create a simple graphical user interface (GUI) for a basic chatbot.

## Getting Started

### Prerequisites

To run the Chatbot code, you need to have Python installed on your system.

### Running the Chatbot

1. Clone or download the repository containing the Chatbot code.
2. Ensure you have Python installed on your system.
3. Run the Python script, and a graphical window will appear, displaying the chatbot interface.
4. Type a message in the input box and press the "Sent" button to send the message to the chatbot.
5. The chatbot will respond based on the message you sent. It supports a few simple predefined responses.

## Code Description

The Chatbot code uses the tkinter library for GUI development and implements a basic chatbot functionality. Here's a breakdown of the key components:

1. `from tkinter import *`: This line imports the tkinter module, which is used for creating GUI applications.

2. `root = Tk()`: This line creates the main root window for the GUI.

3. `def sent()`: This function is called when the user clicks the "Sent" button. It reads the user's message from the input box, processes the input, and generates an appropriate response from the chatbot.

4. `text = Text(root, bg='blue', fg='white')`: This creates a Text widget to display the conversation between the user and the chatbot. The widget is set to have a blue background and white text color.

5. `e = Entry(root, width=80)`: This creates an Entry widget, which serves as an input box for the user to type messages.

6. `send = Button(root, text='Sent', bg='deeppink', fg='white', width=20, command=sent)`: This creates a button labeled "Sent" that triggers the `sent()` function when clicked.

7. The code uses conditional statements (if-elif-else) to handle different user inputs and generate corresponding responses from the chatbot.

8. The mainloop function (`root.mainloop()`) starts the GUI event loop, enabling user interaction with the chatbot.

## Functionality

The Chatbot code provides basic conversational interactions. The chatbot can respond to the following user messages:

- User: "hi" -> Chatbot: "hello"
- User: "hello" -> Chatbot: "hi"
- User: "how are you" -> Chatbot: "i'm fine and you?"
- User: "i'm fine too" -> Chatbot: "nice to hear that"
- Other messages -> Chatbot: "Sorry I didn't get it."

The chat history is displayed in a blue window with white text, and the user can type messages in the input box to interact with the chatbot.

## Acknowledgments

The Chatbot code was created by Harsh Gupta (Desparete Enuf). It demonstrates basic GUI development using the tkinter library in Python. The code is a simple example of a rule-based chatbot, which generates responses based on predefined conditions.

## License

This project is open-source and licensed under the [MIT License](LICENSE). You are free to modify and distribute the code, but please provide proper attribution to the original creator, Harsh Gupta (Desparete Enuf).
