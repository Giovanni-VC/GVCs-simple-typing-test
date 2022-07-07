# Import tkinter library
from tkinter import *
from tkinter import messagebox


def start(count=60):
    """
    Countdown for 60 seconds and show a message box
    Arguments:
        count=60
    Returns:
        None
    """

    if count == 60:
        entry.delete(0, 'end')

    if count > 0:
        # call countdown again after 1000ms (1s)
        win.after(1000, start, count - 1)

    if count == 0:
        text_words = word_extractor(text)
        input_text_string = input_text.get()
        input_text_string_words = word_extractor(input_text_string)
        n_correct_words, n_wrong_words = correct_words(input_text_string_words, text_words)
        messagebox.showinfo("Results", f"Your score is {n_correct_words} WPM. \n In reality you typed "
                                       f"{n_correct_words + n_wrong_words}, but you made {n_wrong_words}"
                                       f" mistakes"
                            )


def word_extractor(text):
    """
    Extract the words of a text delimited by space
    Arguments:
        text: a string
    Returns:
        list of words
    """
    text_words = text.split(" ")
    return text_words


def correct_words(input_words, correct_words):
    """
    Counts how many words in a list are correct, based on a list of correct words
    Arguments:
        input_words: a list
        correct_words: a list
    Returns:
        Number of correct words and wrong words
    """

    number_of_correct_words = 0
    wrong_words = 0

    for i in range(0, len(input_words)):

        if input_words[i] == correct_words[i]:
            number_of_correct_words += 1
        else:
            wrong_words += 1
    return [number_of_correct_words, wrong_words]


# Create a variable for the text

text = "A disaster is a hazard resulting in an event of substantial extent causing significant " \
       "physical damage or destruction, loss of life, or drastic change to the environment. " \
       "Disasters fall into two major categories. These include man made and natural disasters. " \
       "Man-made disasters are disasters due to result of of human intent, negligence or involving a " \
       "failure of a man-made system that leads to human suffering and environmental damage. Man-made " \
       "disasters are the consequence of technological or human hazards. Fires, transport accidents, " \
       "industrial accidents, oil spills and nuclear explosions/ radiation are some examples " \
       "resulting the human hazards. Man has cut forests recklessly to clear the land for " \
       "cultivation and along with this environmental degradation has taken place, which " \
       "also affects human life. Man-made hazards or disasters are sometimes referred to " \
       "as anthropogenic. Man-made disasters can be divided into different categories. " \
       "As with natural hazards, man-made hazards are events that have not happened, " \
       "for instance terrorism. Man-made disasters are examples of specific cases where " \
       "man-made hazards have become reality in an event. The rising population has " \
       "resulted in high fuel consumption and reduction of natural resources. " \
       "Over population also affects our social environment. Another type of disaster that " \
       "falls in this category is nuclear bomb. Other types of man made disasters which are " \
       "just as catastrophic include chemical spill, oil spill, arson and terrorism."

# Create an instance of frame
win = Tk()

# Set title
win.title("GVC's simple typing test speed")

# Set geometry
win.geometry("1000x600")

# Create a text Label
label = Label(win, padx=20, text=text, wraplength=1000, font=('Poppins bold', 15)).pack(pady=20)
input_text = StringVar()

# Create an entry widget
entry = Entry(win, textvariable=input_text)
entry.pack(fill='x', expand=True, padx=45, pady=45)
entry.focus()

# Add a placeholder in the entry Widget
entry.insert(0, "Click the button to start and type the words shown above")

# Add a button to start or reset

button = Button(text="Start/Restart", command=start, width=45)
button.pack(side="bottom", pady=40)

win.mainloop()

# TODO 1: Build an interface in Tkinter

# TODO 2: Display a text for the user to write

# TODO 3: Trigger the timer and crash when it hits 60s

# TODO 4: Show stats
