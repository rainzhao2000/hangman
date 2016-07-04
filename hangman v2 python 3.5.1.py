import random
import tkinter as tk


class Category(object):
    def __init__(self, name, words):
        self.name = name
        self.words = words

    def random_word(self):
        return random.choice(self.words)


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Hangman v2 by Rain Zhao")
        self.geometry('600x600')
        self.menu()
        self.mainloop()

    def menu(self):
        self.app_frame = tk.Frame(self, width=600, height=600)
        self.app_frame.pack(fill='both', expand=True)
        self.main_title = tk.Label(self.app_frame,
                                   text="Welcome to Hangman, made by Rain Zhao",
                                   font=('Calibri', 16, 'bold'))
        self.main_title.pack()
        self.main_photo = tk.PhotoImage(file='main.png')
        self.main_photo_label = tk.Label(self.app_frame, image=self.main_photo)
        self.main_photo_label.image = self.main_photo
        self.main_photo_label.pack()
        self.start_label = tk.Label(self.app_frame,
                                    text="Would you like to start?",
                                    font=('Calibri', 16))
        self.start_label.place(relx=0.5, y=470, anchor=tk.CENTER)
        self.yes = tk.Button(self.app_frame, text='YES', font=('Calibri', 16,
                                                              'bold'),
                             fg='green', bg='white', command=self.select)
        self.yes.place(x=75, y=530, width=200, anchor=tk.W)
        self.no = tk.Button(self.app_frame, text='NO', font=('Calibri', 16,
                                                             'bold'),
                            fg='red', bg='white', command=self.destroy)
        self.no.place(x=325, y=530, width=200, anchor=tk.W)

    def select(self):
        for widget in self.app_frame.winfo_children():
            widget.destroy()
        self.canvas = tk.Canvas(self.app_frame, width=600, height=600)
        self.canvas.pack()
        self.countries = Category('countries', ['canada','russia','china',
                                                'vietnam','germany','france',
                                                'mexico','india'])
        self.animals = Category('animals', ['eagle','lion','crocodile','tiger',
                                            'chicken','sheep','moose','elephant'])
        self.colours = Category('colours', ['blue','green','yellow','red',
                                            'orange','violet','cyan','magenta'])
        self.fruits = Category('fruits', ['apple','banana','orange','mango',
                                          'watermelon','kiwi','peach','pineapple'])
        self.select_title = tk.Label(self.app_frame, text="""Please select one of
the following categories to begin""", font=('Calibri', 20, 'bold'))
        self.select_title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.countries_button = tk.Button(self.app_frame, text='COUNTRIES',
                                          font=('Calibri', 16, 'bold'),
                                          bg='white', command=lambda
                                          cat=self.countries:
                                          self.loading(cat))
        self.countries_button.place(width=200, x=75, y=200)
        self.animals_button = tk.Button(self.app_frame, text='ANIMALS',
                                        font=('Calibri', 16, 'bold'),
                                        bg='white', command=lambda
                                        cat=self.animals:
                                        self.loading(cat))
        self.animals_button.place(width=200, x=325, y=200)
        self.colours_button = tk.Button(self.app_frame, text='COLOURS',
                                        font=('Calibri', 16, 'bold'),
                                        bg='white', command=lambda
                                        cat=self.colours:
                                        self.loading(cat))
        self.colours_button.place(width=200, x=75, y=300)
        self.fruits_button = tk.Button(self.app_frame, text='FRUITS',
                                       font=('Calibri', 16, 'bold'),
                                       bg='white', command=lambda
                                       cat=self.fruits:
                                       self.loading(cat))
        self.fruits_button.place(width=200, x=325, y=300)
        self.return_method()

    def return_method(self):
        self.return_button = tk.Button(self.app_frame, text="Return to menu",
                                       font=('Calibri', 12), fg='white',
                                       bg='#3b757a', command=self.menu_buffer)
        self.return_button.place(x=20, y=575, anchor=tk.SW)
        self.canvas.create_line(0, 500, 600, 500)

    def menu_buffer(self):
        self.app_frame.destroy()
        self.menu()

    def loading(self, cat):
        for widget in self.app_frame.winfo_children():
            widget.destroy()
        self.word = cat.random_word()
        self.loading_label = tk.Label(self.app_frame, text="""Generating a word
. . .""", font=('Calibri', 20))
        self.loading_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.after(2000, self.hangman, cat)

    def hangman(self, cat):
        for widget in self.app_frame.winfo_children():
            widget.destroy()
        self.canvas = tk.Canvas(self.app_frame, width=600, height=600)
        self.canvas.pack()
        print(cat.name, self.word)
        self.hangman_title = tk.Label(self.app_frame, text="""Guess a letter or try
and guess the whole word""", font=('Calibri', 20, 'bold'))
        self.hangman_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.picture_frame = tk.Frame(self)
        self.picture_frame.place(x=50, y=250, anchor=tk.W)
        self.progress_frame = tk.Frame(self, width=350, height=50)
        self.progress_frame.place(x=220, y=250, anchor=tk.W)
        self.record_frame = tk.Frame(self, width=350, height=40)
        self.record_frame.place(x=220, y=300, anchor=tk.W)
        self.tries = 6
        self.record = []
        self.dash = '_'
        self.length = len(self.word)
        self.blanks = []
        for num in range(0, self.length):
            self.blanks.append(self.dash)
        self.blanks = ' '.join(self.blanks)
        self.blanks_label = tk.Label(self.progress_frame, text=self.blanks,
                                     font=('Calibri', 20))
        self.blanks_label.pack()
        self.picture()
        self.entry()
        self.cat_label = tk.Label(self.app_frame, text="The category is %s"
                                  % (cat.name), font=('Calibri', 16))
        self.cat_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        self.return_method()

    def picture(self):
        for widget in self.picture_frame.winfo_children():      
            widget.destroy()

        self.empty = tk.Label(self.picture_frame, text=""" ______
 |    |
 |    
 |
 |
 |
==========""", font=('Calibri', 14), justify=tk.LEFT)
        self.five = tk.Label(self.picture_frame, text=""" ______
 |    |
 |    O
 |
 |
 |
==========""", font=('Calibri', 14), justify=tk.LEFT)
        self.four = tk.Label(self.picture_frame, text=""" ______
 |    |
 |    O
 |    |
 |
 |
==========""", font=('Calibri', 14), justify=tk.LEFT)
        self.three = tk.Label(self.picture_frame, text=""" ______
 |    |
 |    O
 |   /|
 |
 |
==========""", font=('Calibri', 14), justify=tk.LEFT)
        self.two = tk.Label(self.picture_frame, text=""" ______
 |    |
 |    O
 |   /|\\
 |
 |
==========""", font=('Calibri', 14), justify=tk.LEFT)
        self.one = tk.Label(self.picture_frame, text=""" ______
 |    |
 |    O
 |   /|\\
 |   /
 |
==========""", font=('Calibri', 14), justify=tk.LEFT)
        self.end = tk.Label(self.picture_frame, text=""" ______
 |    |
 |    O
 |   /|\\
 |   / \\
 |
==========""", font=('Calibri', 14), justify=tk.LEFT)
        if self.tries == 6:
            self.empty.pack()
        elif self.tries == 5:
            self.five.pack()
        elif self.tries == 4:
            self.four.pack()
        elif self.tries == 3:
            self.three.pack()
        elif self.tries == 2:
            self.two.pack()
        elif self.tries == 1:
            self.one.pack()
        elif self.tries == 0:
            self.end.pack()

    def entry(self):
        self.ent = tk.StringVar()
        self.entry_label = tk.Label(self.app_frame, text='Input:',
                                    font=('Calibri', 14))
        self.entry_label.place(x=50, y=400, anchor=tk.W)
        self.entry_box = tk.Entry(self.app_frame, textvariable=self.ent)
        self.entry_box.place(x=150, y=400, width=350, anchor=tk.W)
        self.entry_box.bind('<Return>', self.check)

    def check(self, event):
        self.display = []
        self.guess = self.ent.get()
        self.guess = self.guess.lower()
        print('user input:', self.guess)
        if all(letter in "abcdefghijklmnopqrstuvwxyz" for letter in self.guess):
            if self.guess == self.word:
                self.correct_display()
                self.show_word()
                self.after(1000, self.win)
            elif len(self.guess) > 1:
                self.tries -= 1
                self.picture()
                self.wrong1_label = tk.Label(self.app_frame,
                                             text="""The guessed word doesn't   
match""", font=('Calibri', 12), justify=tk.LEFT)
                self.wrong1_label.place(x=200, y=120, anchor=tk.NW)
                self.tries_display()
                if self.tries == 0:
                    self.dead_display()
                    self.after(2000, self.show_word)
                else:
                    self.progress_display()
                    self.record_display()
                    self.entry()
            elif self.guess in self.record:
                self.label = tk.Label(self.app_frame,
                                      text="\nYou already used this letter        ",
                                      font=('Calibri', 12))
                self.label.place(x=200, y=120, anchor=tk.NW)
                self.entry()
            elif self.guess in self.word:
                self.progress_display()
                self.record_display()
                self.entry()
            else:
                self.record.append(self.guess)
                self.tries -= 1
                self.picture()
                self.wrong2_label = tk.Label(self.app_frame,
                                             text="""The guessed letter is not in
the word""", font=('Calibri', 12), justify=tk.LEFT)
                self.wrong2_label.place(x=200, y=120, anchor=tk.NW)
                self.tries_display()
                if self.tries == 0:
                    self.dead_display()
                    self.after(2000, self.show_word)
                else:
                    self.progress_display()
                    self.record_display()
                    self.entry()
        else:
            self.label = tk.Label(self.app_frame,
                                  text="\nUse letters only please        ",
                                  font=('Calibri', 12))
            self.label.place(x=200, y=120, anchor=tk.NW)
            self.entry()

    def correct_display(self):
        self.correct_label = tk.Label(self.app_frame,
                                       text="You've guessed the word!",
                                       font=('Calibri', 14, 'bold'))
        self.correct_label.place(x=220, y=350, anchor=tk.W)

    def tries_display(self):
        self.tries_label = tk.Label(self.app_frame,
                                    text="Tries left: %d" % (self.tries),
                                    font=('Calibri', 12), justify=tk.LEFT)
        self.tries_label.place(x=200, y=180, anchor=tk.NW)

    def dead_display(self):
        self.dead_label = tk.Label(self.app_frame,
                                  text="You ran out of lives",
                                  font=('Calibri', 14, 'bold'))
        self.dead_label.place(x=220, y=350, anchor=tk.W)

    def progress_display(self):
        for widget in self.progress_frame.winfo_children():
            widget.destroy()
        for letter in self.word:
            if letter in self.record:
                self.display.append(letter)
            elif self.guess == letter:
                self.display.append(letter)
                self.record.append(letter)
            else:
                self.display.append(self.dash)
        self.progress = ' '.join(self.display)
        print(self.progress)
        self.progress_label = tk.Label(self.progress_frame, text=self.progress,
                                       font=('Calibri', 20))
        self.progress_label.pack()
        if ''.join(self.display) == self.word:
            self.correct_display()
            self.after(1000, self.win)

    def record_display(self):
        for widget in self.record_frame.winfo_children():
            widget.destroy()
        self.letters_used = ', '.join(self.record)
        print(self.record)
        self.used_label = tk.Label(self.record_frame,
                                   text="Letters used: %s" % (self.letters_used),
                                   font=('Calibri', 12))
        self.used_label.pack()

    def show_word(self):
        for widget in self.progress_frame.winfo_children():
            widget.destroy()
        for letter in self.word:
            self.display.append(letter)
        self.show = ' '.join(self.display)
        print(self.show)
        self.show_label = tk.Label(self.progress_frame, text=self.show,
                                   font=('Calibri', 20))
        self.show_label.pack()
        if self.tries == 0:
            self.word_label = tk.Label(self.app_frame,
                                       text="The word was %s    " % (self.word),
                                       font=('Calibri', 20, 'bold'))
            self.word_label.place(x=220, y=350, anchor=tk.W)
            self.after(1000, self.lose)

    def win(self):
        win_gui = AppEnd(self, "You Win!", '450x550', 550, 'win.png', 430, 500,
                         'win')

    def lose(self):
        lose_gui = AppEnd(self, "You Lose :(", '450x500', 500, 'lose.png', 380,
                          450, 'lose')

class AppEnd(tk.Toplevel):
    def __init__(self, master, end_title, end_geometry, canvas_height, end_pic,
                 restart_label_y, button_y, state):
        tk.Toplevel.__init__(self)
        self.master = master
        self.end_title = end_title
        self.title(self.end_title)
        self.end_geometry = end_geometry
        self.geometry(end_geometry)
        self.canvas_height = canvas_height
        self.end_pic = end_pic
        self.end_photo = tk.PhotoImage(file=self.end_pic)
        self.end_photo_label = tk.Label(self, image=self.end_photo)
        self.end_photo_label.image = self.end_photo
        self.end_photo_label.pack()
        self.restart_label = tk.Label(self, text="Do you want to play again?",
                                      font=('Calibri', 16))
        self.restart_label_y = restart_label_y
        self.restart_label.place(relx=0.5, y=self.restart_label_y,
                                 anchor=tk.CENTER)
        self.end_yes = tk.Button(self, text='YES', font=('Calibri', 14, 'bold'),
                                 fg='green', bg='white', command=self.restart)
        self.button_y = button_y
        self.end_yes.place(x=75, y=self.button_y, width=150, anchor=tk.W)
        self.end_no = tk.Button(self, text='NO', font=('Calibri', 14, 'bold'),
                                 fg='red', bg='white', command=self.end_destroy)
        self.end_no.place(x=225, y=self.button_y, width=150, anchor=tk.W)
        self.state = state
        print(self.state)

    def restart(self):
        self.destroy()
        self.master.destroy()
        root = MainApp()
        print('restart')

    def end_destroy(self):
        self.destroy()
        self.master.destroy()
        print('exit')


root = MainApp()
