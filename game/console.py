import random


class Console:
    """The console gets text or numerical input and displays them out to the terminal. The three main functions, are to read input from the user, read each letter of the chosen word, and displays the text.

    Attributes:
        input prompt string
    """

    def read(self, prompt):
        """Prompts user to enter text and returns the input.

        Args: 
            prompt the user to enter a string

        Returns:
            a string, which is the user's input
        """
        return input(prompt)

    def read_letter(self, prompt):
        """Reads an alpha character from the user's input.

        Args: 
            Character from the user's input of the prompt.

        Returns:
            returns the user's input as a float
        """
        return float(input(prompt))

    def write(self, text):
        """prints the text

        Args: 
            the text
        """
        print(text)
