import tkinter
import random

# Function for switching between different screens of the program.
# Destroys widgets of current screen and then loads the next.
def switch_screens (widgets_list, screen):
    # Destory all objects of the previous screen
    for i in widgets_list:
        i.destroy ()
    
    # Call function to load next screen depending on argument
    if (screen == "rules"):
        rules_screen ()
    elif (screen == "colours"):
        colours_screen ()
    elif (screen == "main"):
        main_menu_screen ()
    elif (screen == "easy"):
        game_screen ("easy")
    elif (screen == "medium"):
        game_screen ("medium")
    elif (screen == "hard"):
        game_screen ("hard")

# Function for loading the main menu screen which leads to other screens.
def main_menu_screen ():
    # Initializing variables
    global name_label, rules_button, colours_button, easy_button, medium_button, hard_button
    main_menu_widgets = []
    
    # Hex colour code of the medium button's colour
    medium_button_colour = "#fdff75"

    # Title of the main menu
    name_label = tkinter.Label (main_window, bg= "black", text = "Colour Memory Game",
                                font = ("Calibri", 45), width = 22, height = 2, fg = "white")
    name_label.grid (row = 0, column = 0, padx = 280, pady = 15)
    
    # Button to switch to the rules and information screen
    rules_button = tkinter.Button (main_window, text = "Rules and Information",
                                   width = 20, height = 5, bg = "plum2", 
                                   command = lambda: switch_screens (main_menu_widgets, "rules"))
    rules_button.grid (row = 1, column = 0, pady = 7)

    # Button to switch to the colours screen
    colours_button = tkinter.Button (main_window, text = "Colours",
                                     width = 20, height = 5, bg = "light blue",
                                     command = lambda: switch_screens (main_menu_widgets,
                                     "colours"))
    colours_button.grid (row = 2, column = 0, pady = 7)

    # Button to begin the game at the easy difficulty
    easy_button = tkinter.Button (main_window, text = "Easy Mode",
                                  width = 20, height = 5, bg = "light green",
                                  command = lambda: switch_screens (main_menu_widgets, "easy"))
    easy_button.grid (row = 3, column = 0, pady = 7)

    # Button to begin the game at the medium difficulty
    medium_button = tkinter.Button (main_window, text = "Medium Mode",
                                    width = 20, height = 5, bg = medium_button_colour,
                                    command = lambda: switch_screens (main_menu_widgets, "medium"))
    medium_button.grid (row = 4, column = 0, pady = 7)

    # Button to begin the game at the hard difficulty 
    hard_button = tkinter.Button (main_window,text = "Hard Mode",
                                  width = 20, height = 5, bg = "pink",
                                  command = lambda: switch_screens (main_menu_widgets, "hard"))
    hard_button.grid (row = 5, column = 0, pady = 7)
    
    # List of Tkinter widgets on the main menu screen
    main_menu_widgets = [name_label, rules_button, colours_button,
                         easy_button, medium_button, hard_button]

# Function that loads the rule screen
def rules_screen ():
    # Initializing variables
    global rules_label, return_to_menu, game_description_label, game_description_title
    global colour_description_title, colour_description_label
    rules_screen_widgets = []
                              
    # Explanation of how to play the game
    game_description = ("This is a memory game. When playing a series of colours will flash one "
                        "after another,\nafterwards you must remember the order and enter them. "
                        "Score is determined by the\nnumber of correct guesses and the difficulty. "
                        "At the main menu you choose between\n3 difficulties to play the game at. "
                        "After choosing the difficulty the game will begin\nafter a countdown. The"
                        " random set of colours will begin to flash one after another.\nAfter the "
                        "colours finish flashing you are provided a text box to input your guesses."
                        "\nOnce you are done, press the submit button and you will be presented "
                        "with your score.")

    # Explanation of the colours in the game and the colours screen
    colour_description = ("At higher difficulties there will be harder colours. At the colours menu"
                          " you may view \nthe colours in the game or enter your own custom "
                          "colours. When entering a colour\nprovide a valid hex code, name of the"
                          " colour and its difficulty.")

    # Title of the rules and information screen
    rules_label = tkinter.Label (main_window, bg = "black", text = "Rules and Information",
                                 font = ("Calibri", 30), width = 30, height = 4, fg = "white")
    rules_label.grid (row = 0, column = 0, padx = 345, pady = 20)
    
    # Title of the game explanation
    game_description_title = tkinter.Label (main_window, bg = "light green", text = "How to Play",
                                 font = "Gothis", width = 25, height = 1)
    game_description_title.grid (row = 1, column = 0, pady = 10)

    # Label containing an explanation of how to play the game
    game_description_label = tkinter.Label (main_window,
                                text = game_description,
                                font = ("Gothis", 11), width = 70, height = 9)
    game_description_label.grid (row = 2, column = 0, pady = 5)
    
    # Title of the colour explanation
    colour_description_title = tkinter.Label (main_window,bg = "light green", text = "Colours",
                                 font = "Gothis", width = 25, height = 1)
    colour_description_title.grid (row = 3, column = 0, pady = 10)

    # Label containing an explanation of the colours in the game and the colours screen
    colour_description_label = tkinter.Label (main_window,
                                text = colour_description,
                                font = ("Gothis", 11), width = 70, height = 4)
    colour_description_label.grid (row = 4, column = 0, pady = 5)

    # Button to return to the main menu
    return_to_menu = tkinter.Button (main_window, text = "Back to Main Menu",
                                   width = 20, height = 2, bg = "light blue", 
                                   command = lambda: switch_screens(rules_screen_widgets, "main"))
    return_to_menu.grid (row = 5, column = 0, pady = 5)

    # List of all Tkinter widgets of the rule screen
    rules_screen_widgets = [rules_label, return_to_menu, game_description_label,
                            game_description_title, colour_description_title,
                            colour_description_label]

# Function that loads the colours screen in which the user can view colours
# and submit custom colours.
def colours_screen ():
    # Initializing variables
    global colours_title_label, colours_to_menu, colour_preview_display, next_colour_button
    global previous_colour_button, colours_to_menu, colour_name, colours_to_menu, submit_colour
    global colour_input_entry, hex_input_entry, custom_colour_difficulty
    colour_screen_widgets = []
    all_colours = get_colours("all")

    # Custom colour difficulty StringVar 
    custom_colour_difficulty = tkinter.StringVar ()
    
    # Title of the colours screen
    colours_title_label = tkinter.Label (main_window, bg = "black", text = "Colours",
                                         font = ("Calibri", 30), width = 30, height = 2, 
                                         fg = "white")
    colours_title_label.grid (row = 0, column = 0, pady = 20, padx = 345)

    # Label that acts as the display for the current colour
    colour_preview_display = tkinter.Label (main_window, bg = "light grey", 
                                            text = "", font = "Gothis", width = 40, height = 15)
    colour_preview_display.grid (row = 1, column = 0)
    colour_preview_display.configure (bg = f"{all_colours[0][0]}")

    # Frame for colour scrolling related buttons and labels
    colour_scroll_frame = tkinter.Frame (main_window)
    colour_scroll_frame.grid (row = 2, column = 0, pady = 10)

    # Button to switch to the previous colour
    previous_colour_button = tkinter.Button (colour_scroll_frame, text = "<<<",
                                             command = lambda: colour_screen_switch(get_colours(
                                                 "all"), colour_name['text'], "left"))
    previous_colour_button.grid (row = 0, column = 0)

    # Label that displays current colour
    colour_name = tkinter.Label (colour_scroll_frame, text = "",
                                 bg = 'light grey', font= ("Gothis", 11), width = 20, height = 1)
    colour_name.grid (row = 0, column = 1)
    colour_name.configure (text = f"{all_colours[1][0]}")

    # Button to switch to the next colour
    next_colour_button = tkinter.Button (colour_scroll_frame, text = ">>>",
                                         command = lambda: colour_screen_switch(get_colours(
                                                           "all"), colour_name['text'], "right"))
    next_colour_button.grid (row = 0, column = 2)

    custom_colour_input ()

    # Button for returning to the main menu
    colours_to_menu = tkinter.Button (main_window, text = "Back to Main Menu", width = 20,
                                      height = 2, bg = "light blue", 
                                      command = lambda: switch_screens (colour_screen_widgets, "main"))
    colours_to_menu.grid (row = 8, column = 0, pady = 15)

    # List of Tkinter widgets on the colour screen
    colour_screen_widgets = [
        colours_title_label, colours_to_menu, colour_preview_display, next_colour_button, 
        previous_colour_button, colours_to_menu, colour_name, colours_to_menu, colour_input_entry,
        hex_input_entry, colour_level_hard, colour_level_medium, colour_level_easy, 
        input_colour_title, input_name_label, input_hex_label, submit_colour, submission_status
        ]

    colour_level_easy.invoke ()

def custom_colour_input ():
    global colour_input_entry, hex_input_entry, colour_level_hard, colour_level_medium
    global colour_level_easy, input_colour_title, input_name_label, input_hex_label
    global submit_colour, submission_status

    # Frame for widgets for custom colour input
    custom_colour_frame = tkinter.Frame (main_window)
    custom_colour_frame.grid (row = 4, column = 0)

    # Custom colour input section label
    input_colour_title = tkinter.Label (main_window,
                                        text = "Input Custom Colour", bg = 'light grey',
                                        font= ("Gothis", 14), width = 20, height = 1)
    input_colour_title.grid (row = 3, column = 0, pady = 5)

    # Label for colour name entry box
    input_name_label = tkinter.Label (custom_colour_frame, text = "Colour Name",
                                      bg = 'light grey', font= ("Gothis", 11), width = 10,
                                      height = 1)
    input_name_label.grid (row = 1, column = 0)

    # Label for hex code entry box
    input_hex_label = tkinter.Label (custom_colour_frame,
                                     text = "Hex Code", bg = 'light grey', font = ("Gothis", 11),
                                     width = 10, height = 1)
    input_hex_label.grid (row = 1, column = 1)

    # Entry box for custom colour name
    colour_input_entry = tkinter.Entry (custom_colour_frame, font = ("Calibri", 12))
    colour_input_entry.grid (row = 2, column = 0)

    # Entry box for custom colour hex code
    hex_input_entry = tkinter.Entry (custom_colour_frame, font = ("Calibri", 12))
    hex_input_entry.grid (row = 2, column = 1)

    # Frame for custom colour difficulty radiobuttons 
    custom_colour_difficulty_frame = tkinter.Frame (main_window)
    custom_colour_difficulty_frame.grid (row = 5, column = 0)

    # Radiobuttons for custom colour difficulty 
    colour_level_easy = tkinter.Radiobutton (custom_colour_difficulty_frame, text = "Easy",
                                       variable = custom_colour_difficulty, value = "easy")
    colour_level_easy.grid (row = 0, column = 0)

    colour_level_medium = tkinter.Radiobutton (custom_colour_difficulty_frame, text = "Medium",
                                         variable = custom_colour_difficulty, value = "medium")
    colour_level_medium.grid (row = 0, column = 1)

    colour_level_hard = tkinter.Radiobutton (custom_colour_difficulty_frame, text = "Hard",
                                       variable = custom_colour_difficulty, value = "hard")
    colour_level_hard.grid (row = 0, column = 2)

    # Status of custom colour submission (invalid input, duplicate, success)
    submission_status = tkinter.Label (main_window, width = 18, height = 1, bg = "black")
    submission_status.grid (row = 6, column = 0, pady = 5)

    # Button for submitting custom colour
    submit_colour = tkinter.Button (main_window, text = "Submit", width = 10, height = 1,
                                    bg = "light blue",
                                    command = lambda: submit_custom_colour (get_colours("all")))
    submit_colour.grid (row = 7, column = 0, pady = 5)

# Function that loads the game screen
def game_screen (difficulty):
    global colour_display

    # Label which acts as a display for colours.
    colour_display = tkinter.Label (main_window, bg = "light grey", 
                                    text = "", font = "Gothis", width = 60, height = 20)
    colour_display.grid (row = 0, column = 0, padx = 370, pady = 150)
    
    # Get colour list based on difficulty 
    colours = get_colours (difficulty)
    
    # Generate list of 5 random numbers ranging from 0 to the number of colours
    colour_order = random_numbers_generator (0, len(colours[0]), 5)

    # Call change_colour function to begin game
    change_colour (colours, colour_order, difficulty)
 
# Loads guessing phase portion of game screen where users can submit their guesses
def guessing_phase (ordered_colours, difficulty):
    global first_colour_guess_label, second_colour_guess_label, third_colour_guess_label
    global fourth_colour_guess_label, fifth_colour_guess_label, first_colour_guess_entry
    global second_colour_guess_entry, third_colour_guess_entry, fourth_colour_guess_entry
    global fifth_colour_guess_entry, submit_colour

    # Frame for guessing phase widgets
    guess_frame = tkinter.Frame (main_window)
    guess_frame.grid (row = 1, column = 0, pady = 20)

    # Change colour display location and configure for guessing phase
    colour_display.grid (row = 0, column = 0, padx = 370, pady = 10)
    colour_display.configure (bg = "black", text = "Guessing Phase", fg = 'white')

    # Label for the entry box of each guess
    first_colour_guess_label = tkinter.Label (guess_frame,
                                              text = "Guess #1", bg = 'light grey',
                                              font= ("Gothis", 11), width = 10, height = 1)
    first_colour_guess_label.grid (row = 0, column = 0)

    second_colour_guess_label = tkinter.Label (guess_frame,
                                               text = "Guess #2", bg = 'light grey',
                                               font= ("Gothis", 11), width = 10, height = 1)
    second_colour_guess_label.grid (row = 0, column = 1)

    third_colour_guess_label = tkinter.Label (guess_frame,
                                              text = "Guess #3", bg = 'light grey',
                                              font= ("Gothis", 11), width = 10, height = 1)
    third_colour_guess_label.grid (row = 0, column = 2)

    fourth_colour_guess_label = tkinter.Label (guess_frame,
                                               text = "Guess #4", bg = 'light grey',
                                               font= ("Gothis", 11), width = 10, height = 1)
    fourth_colour_guess_label.grid (row = 0, column = 3)

    fifth_colour_guess_label = tkinter.Label (guess_frame,
                                              text = "Guess #5", bg = 'light grey',
                                              font= ("Gothis", 11), width = 10, height = 1)
    fifth_colour_guess_label.grid (row = 0, column = 4)

    # Entry boxes for each guess
    first_colour_guess_entry = tkinter.Entry (guess_frame, font = ("Calibri", 12))
    first_colour_guess_entry.grid (row = 1, column = 0)

    second_colour_guess_entry = tkinter.Entry (guess_frame, font = ("Calibri", 12))
    second_colour_guess_entry.grid (row = 1, column = 1)

    third_colour_guess_entry = tkinter.Entry (guess_frame, font = ("Calibri", 12))
    third_colour_guess_entry.grid (row = 1, column = 2)

    fourth_colour_guess_entry = tkinter.Entry (guess_frame, font = ("Calibri", 12))
    fourth_colour_guess_entry.grid (row = 1, column = 3)

    fifth_colour_guess_entry = tkinter.Entry (guess_frame, font = ("Calibri", 12))
    fifth_colour_guess_entry.grid (row = 1, column = 4)

    # Button for submitting guesses, calls a function to load score
    submit_colour = tkinter.Button (main_window, text = "Submit",
                                    width = 10, height = 1, bg = "light blue",
                                    command = lambda: load_score (ordered_colours, difficulty))
    submit_colour.grid (row = 2, column = 0)

# Function that loads the results of the game after the user finishes guessing
def load_score (ordered_colours, difficulty):
    # Destroy submit button
    submit_colour.destroy ()

    results = calculate_score (ordered_colours, difficulty)

    # Label that displays the score the user achieved
    score_label = tkinter.Label (main_window, justify = "left", 
                                 text = f"Your score is {results[0]}", bg = 'light green',
                                 font= ("Gothis", 11), width = 40, height = 1)
    score_label.grid (row = 3, column = 0)

    # Label that displays the number of correct guesses the user achieved
    correct_guesses_label = tkinter.Label (main_window, justify = "left", 
                                           text = f"You guessed {results[1]} correctly!",
                                           bg = 'light green', font= ("Gothis", 11), 
                                           width = 40, height = 1)
    correct_guesses_label.grid (row = 4, column = 0)

    # Button to restart the game and send the user back to the main menu
    restart_button = tkinter.Button (main_window, text = "Back to main menu",
                                     width = 15, height = 1, bg = "light blue",
                                     command = restart_game)
    restart_button.grid (row = 5, column = 0)

# Function that calculates the score when the user finishes playing the game
def calculate_score (ordered_colours_list, difficulty):
    # Initialzing variables
    total_score = 0
    correct_guesses = 0

    # Get user guesses input, convert to lowercase and remove excess whitespace
    first_guess = first_colour_guess_entry.get ().lower ().strip ()
    second_guess = second_colour_guess_entry.get ().lower ().strip ()
    third_guess = third_colour_guess_entry.get ().lower ().strip ()
    fourth_guess = fourth_colour_guess_entry.get ().lower ().strip ()
    fifth_guess = fifth_colour_guess_entry.get ().lower ().strip ()

    # If corrent guess, add 10 to the score and increment counter
    if (first_guess == ordered_colours_list[0]) :
        total_score += 10
        correct_guesses += 1

    if (second_guess == ordered_colours_list[1]) :
        total_score += 10
        correct_guesses += 1

    if (third_guess == ordered_colours_list[2]) :
        total_score += 10
        correct_guesses += 1

    if (fourth_guess == ordered_colours_list[3]) :
        total_score += 10
        correct_guesses += 1

    if (fifth_guess == ordered_colours_list[4]) :
        total_score += 10
        correct_guesses += 1

    # Multiply the score depending on the difficulty
    if (difficulty == "medium") :
        total_score *= 1.5
        
    elif (difficulty == "hard") :
        total_score *= 2

    return [total_score, correct_guesses]

# Changes the colour of the game colour screen at a certain speed depending on difficulty.
def change_colour (colours_list, order, difficulty):
    # Initializing variables
    ordered_hex = []
    ordered_names = []
    time = 1500

    # List of ordered colour hex codes based on the random order
    ordered_hex = [colours_list[0][order[0]], colours_list[0][order[1]], 
                   colours_list[0][order[2]], colours_list[0][order[3]],
                   colours_list[0][order[4]]]
    # List of ordered colour names based on the random order
    ordered_names = [colours_list[1][order[0]], colours_list[1][order[1]], 
                     colours_list[1][order[2]], colours_list[1][order[3]], 
                     colours_list[1][order[4]]]           

    # Changing timing based on difficulty 
    if (difficulty == "medium"):
        time = round (time / 1.5)
    elif (difficulty == "hard"):
        time = round (time / 2)

    # Start countdown
    colour_display.after (0, lambda: colour_display.configure(text = "Ready"))
    colour_display.after (time * 1, lambda: colour_display.configure (text = "Set"))
    colour_display.after (time * 2, lambda: colour_display.configure (text = "Go!"))
    colour_display.after (time * 3, lambda: colour_display.configure (text = ""))

    # Flash colours on the colour display
    colour_display.after (time * 3, lambda: colour_display.configure (bg=f"{ordered_hex[0]}"))
    colour_display.after (time * 4, lambda: colour_display.configure (bg=f"{ordered_hex[1]}"))
    colour_display.after (time * 5, lambda: colour_display.configure (bg=f"{ordered_hex[2]}"))
    colour_display.after (time * 6, lambda: colour_display.configure (bg=f"{ordered_hex[3]}"))
    colour_display.after (time * 7, lambda: colour_display.configure (bg=f"{ordered_hex[4]}"))
    
    # Start the guessing phase
    colour_display.after (time * 8, lambda: guessing_phase (ordered_names, difficulty))

# Function that returns a list of colour names and hex codes 
# depending on the difficulty argument.
def get_colours (colour_difficulty):
    # Initializing variables
    colour_codes = []
    colour_names = []
    saved_colour_file_name = "colours.txt"
    read_file = open (saved_colour_file_name, "r")
    line_read = []

    # Read the first line of the colours file
    line_read = read_file.readline ().strip ("\n").split (" ")

    # 2D lists of predefined colours of different difficulties.
    # The first list contains the colour's hex code. The second list contains the colour's names
    easy_colours = [
        ['#FF0000', '#0000FF', '#00FF00', '#FFC0CB', '#FFA500', '#800080', '#A52A2A', '#FFFF00'], 
        ['red', 'blue', 'green', 'pink', 'orange', 'purple', 'brown', 'yellow']
    ]
    medium_colours = [
        ['#20B2AA', '#F08080', '#EE1289', '#800000', '#FFD700', '#FA8072', '#000080', '#9ACD32'], 
        ['sea green', 'coral', 'deep pink', 'maroon', 'gold', 'salmon', 'navy', 'yellow green']
    ]
    hard_colours = [
        ['#2F4F4F', '#8B3A62', '#A2CD5A', '#EEDFCC', '#FFD39B', '#6E7B8B', '#8B6914', '#FFA54F'], 
        ['dark gray', 'hot pink', 'olive green', 'off white', 'beige', 'gray blue', 'dark gold',
         'tan']
    ]

    # Adding custom colours to the list of colours
    # While the current line read is not empty
    while line_read != ['']:
        # If the colour is an easy colour add it to the easy list
        if (line_read[2] == "easy"):
            easy_colours[0].append (line_read[0])
            easy_colours[1].append (line_read[1])
        # If the colour is a medium colour add it to the medium list
        elif (line_read[2] == "medium"):
            medium_colours[0].append (line_read[0])
            medium_colours[1].append (line_read[1])
        # If the colour is a hard colour add it to the hard list
        else:
            hard_colours[0].append (line_read[0])
            hard_colours[1].append (line_read[1])
        # Read the next line of the file
        line_read = read_file.readline ().strip ("\n").split (" ")

    # If the function argument is easy, the easy difficulity colours will be returned.
    if (colour_difficulty == "easy") :
        colour_codes = easy_colours[0]
        colour_names = easy_colours[1]

    # If the function argument is medium, the medium difficulity colours will be returned.
    elif (colour_difficulty == "medium") :
        colour_codes = medium_colours[0]
        colour_names = medium_colours[1]

    # If the function argument is hard, the hard difficulity colours will be returned.
    elif (colour_difficulty == "hard") :
        colour_codes = hard_colours[0]
        colour_names = hard_colours[1]

    else:
        # Create a master list of all colour names and hex codes
        # Add each colour hex code to the first list within "all_colours"
        for i in easy_colours[0]: #codes
            colour_codes.append (i)
        for i in medium_colours[0]: #codes
            colour_codes.append (i)
        for i in hard_colours[0]: #codes
            colour_codes.append (i)

        # Add each colour's name to the second list within "all_colours"
            for i in easy_colours[1]: #codes
                colour_names.append (i)
            for i in medium_colours[1]: #codes
                colour_names.append (i)
            for i in hard_colours[1]: #codes
                colour_names.append (i)

    return [colour_codes, colour_names]

# Function for submitting a custom colour on the colours screen.
# First validates if the hex code of the colour is valid. Then 
# checks if the colour is a duplicate of the colours that are
# already saved. If it is not, it is saved. 
def submit_custom_colour (predefined_colours):
    # Initalizing variables
    valid_hex_letters = ["A", "B", "C", "D", "E", "F"]
    valid_hex_colour = True
    upper_hex_colour = ""
    duplicate = False
    current_colour = []

    # Getting user input
    name = colour_input_entry.get (). lower ()
    hex_code = hex_input_entry.get ()
    difficulty = custom_colour_difficulty.get ()

    # Initialzing file manipulation
    file_name = "colours.txt"
    file_read = open (file_name, 'r')
    file_append = open (file_name, 'a')

    current_colour = file_read.readline ().strip ("\n").split(" ")

    # Hex code validation
    # Check if the inputted hex code begins with "#" and is 7 characters long
    if (len (hex_code) == 7 and hex_code[0] == "#"):
        # Check each character after the "#"
        for i in range (1, len(hex_code)):
            # Check if the character is a letter or number
            if (not ((hex_code[i].isdigit()) or (hex_code[i].upper() in valid_hex_letters))):
                # If it is not a number or letter, it is not valid
                submission_status.configure (text = "Invalid Input!", fg = "red")
                valid_hex_colour = False

    # If it does not begin with "#" or is 7 charecters long it is not valid
    else:
        submission_status.configure (text = "Invalid Input!", fg = "red")
        valid_hex_colour = False
    
    # If the hex code is valid change all the letters in to uppercase
    if (valid_hex_colour):
        upper_hex_colour = hex_code.upper()

    # If the hex code or colour name is already in the program, it is a duplicate 
    if ((upper_hex_colour in predefined_colours[0]) or (name in predefined_colours[1])):
        duplicate = True
        submission_status.configure (text = "Duplicate!", fg = "red")

    # If the hex code is already saved in the file it is a duplicate.
    while current_colour != ['']:
        if (upper_hex_colour == current_colour[0]) or (name == current_colour[1]):
            duplicate = True
            submission_status.configure (text = "Duplicate!", fg = "red")
        current_colour = file_read.readline ().strip ("\n").split(" ")
    
    is_not_black = (upper_hex_colour != "#000000") and (name != "black")
    is_not_light_grey = (upper_hex_colour != "#D3D3D3") and (name != "light grey")
    not_blank = (len(name) > 0)

    # If the hex code is not a duplicate add it to the colours file
    # If the colour is black or light grey do not add it as it is used 
    # in the guessing phase and may confuse players.
    if (duplicate == False) and (valid_hex_colour == True):
        if (is_not_black and is_not_light_grey and not_blank):
            submission_status.configure (text = "Success!", fg = "light green")
            file_append.write(f"{upper_hex_colour} {name} {difficulty}\n")
        else:
            submission_status.configure (text = "Error!", fg = "red")
    
# Creates a list of random numbers of a certain length and from a certain range.
def random_numbers_generator (start, end, length):
    # Initializing variables
    random_numbers = []
    random_integer = 0

    # While the list of random numbers is less than requested
    while (len(random_numbers) < length) :
        # Generate a random number within the range
        random_integer = random.randrange (start, end)

        # If the number has not already been generated, add it to the list
        if (random_integer not in random_numbers) :
            random_numbers.append (random_integer)

    return random_numbers

# Colour preview screen buttons functionality. Allows user to go through avaliable colours.
def colour_screen_switch (colours, current, direction):
    # Intializing variables
    index = 0

    # Find position of current colour in the list of colours
    for i in range(0, len(colours[0])):
        if (colours[1][i] == current):
            index = i
    
    # If the user wants to switch to the previous colour on the left
    if (direction == "left"):
        # If the user is on the first colour
        if (index == 0):
            # Find the length of the list and set the index to the last colour
            index = len(colours[0])-1
            # Set colour preview display to the colour and change the label to the colour's name
            colour_preview_display.configure (bg = f"{colours[0][index]}")
            colour_name.configure (text = f"{colours[1][index]}")
        else:
            # Set the position to the previous colour's index
            index -= 1
            # Set colour preview display to the colour and change the label to the colour's name
            colour_preview_display.configure (bg = f"{colours[0][index]}")
            colour_name.configure (text = f"{colours[1][index]}")

    # If the user wants to switch to the next colour on the right
    elif (direction == "right"):
        # If the user is on the last colour
        if (index == len(colours[0])-1):
            # Loop around and set the index to the first colour
            index = 0
            # Set colour preview display to the colour and change the label to the colour's name
            colour_preview_display.configure (bg = f"{colours[0][index]}")
            colour_name.configure (text = f"{colours[1][index]}")
        else:
            # Set the position to the next colour's index
            index += 1
            # Set colour preview display to the colour and change the label to the colour's name
            colour_preview_display.configure (bg = f"{colours[0][index]}")
            colour_name.configure (text = f"{colours[1][index]}")

# Function that restarts the game
def restart_game ():
    # Destorys the window
    main_window.destroy ()

    # Calls main function
    main ()

def main ():
    global main_window
    
    # Creates main window
    main_window = tkinter.Tk ()
    main_window.geometry ("1280x720")
    main_window.title ("Colour Memory Game")

    # Calls main menu function which loads the main menu
    main_menu_screen ()

    main_window.mainloop ()

main ()
