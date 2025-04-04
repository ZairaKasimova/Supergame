import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class Supergame:
    def __init__(self, master: tk.Tk, words: iter, tasks: iter):
        self.master = master
        self.words = words
        self.tasks = tasks
        master.title('Игра по мотивам суперигры "Поле Чудес"')

        self.secret_word = ""
        self.guessed_letters = set()
        self.attempts_left = 5
        self.current_word_index = 0
        self.word_states = []
        self.loss_flag = False

        self.label_introduction = tk.Label(master, text="Приветствую нового игрока! Введите своё имя:")
        self.label_introduction.pack()

        self.entry_name = tk.Entry(font=("Arial", 16))
        self.entry_name.pack()

        self.start_button = tk.Button(text='Начать игру', font='Arial', fg='white', bg='green', command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        '''Start the game.'''
        if not self.loss_flag:
            self.player_name = self.entry_name.get() or "Инкогнито"

            self.label_introduction.destroy()
            self.entry_name.destroy()
            self.start_button.destroy()

            self.label_author = tk.Label(self.master, text="Автор кода к игре: Касимова Заира Габибовна.")
            self.label_author.pack(pady=15)  
        else:
            self.loss_flag = False
            self.start_over_button.destroy()

        self.label_instruction = tk.Label(self.master, 
                                          text="Угадайте слово или словосочетание по одному символу "
                                          "(необязательно вводить символы по порядку).",
                                          wraplength=350)
        self.label_instruction.pack(pady=10)

        self.task_label = tk.Label(text="", wraplength=350)
        self.task_label.pack(pady=10)

        self.word_label = tk.Label(self.master, text="", font=("Times", 22), fg='white', bg='blue')
        self.word_label.pack(pady=5)

        self.attempts_label = tk.Label(self.master, text=f"Попыток: {self.attempts_left}")
        self.attempts_label.pack()

        self.entry_character = tk.Entry(self.master, width=5)
        self.entry_character.pack()

        self.guess_button = tk.Button(self.master, text="Проверить", command=self.check_guess, font='Arial', bg='green', fg='white')
        self.guess_button.pack(pady=10)

        self.next_word()

    def next_word(self):
        '''Start guessing a new word or phrase.'''
        if self.current_word_index < len(self.words):
            self.task_label.config(text=self.tasks[self.current_word_index])
            self.secret_word = self.words[self.current_word_index]
            self.guessed_letters = set()
            self.attempts_left = 5
            self.word_states = ["_"] * len(self.secret_word)
            self.update_word_label()
            self.attempts_label.config(text=f"Попыток: {self.attempts_left}")
        else:
            messagebox.showinfo("Поздравляем!", f"{self.player_name}, Вы победили! Молодец!")
            self.master.destroy()

    def update_word_label(self):
        '''Update the display of the guessed word (or part of it).'''
        self.word_label.config(text=" ".join(self.word_states))

    def check_guess(self):
        '''Check the entered character.'''
        guess = self.entry_character.get().lower()
        self.entry_character.delete(0, tk.END)

        if len(guess) != 1:
            messagebox.showinfo("Ошибка", "Введите один символ!")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Сообщение", "Вы уже пробовали этот символ!")
            return

        self.guessed_letters.add(guess)
        correct_guess = False

        for i, letter in enumerate(self.secret_word):
            if letter == guess:
                self.word_states[i] = guess
                correct_guess = True

        self.update_word_label()

        if correct_guess:
            messagebox.showinfo("Сообщение", f"{self.player_name}, молодец! Это правильный ответ!")
        else:
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Попыток: {self.attempts_left}")
            messagebox.showinfo("Сообщение", "Это неправильный ответ!")

        if "_" not in self.word_states:
            if ' ' in self.secret_word:
                messagebox.showinfo("Поздравляем!", 
                                    f"{self.player_name}, так держать! Вы верно назвали словосочетание: {self.secret_word}!")
                self.current_word_index += 1
                self.next_word()
            else:
                messagebox.showinfo("Поздравляем!", 
                                    f"{self.player_name}, так держать! Вы верно назвали слово: {self.secret_word}!")
                self.current_word_index += 1
                self.next_word()

        if self.attempts_left == 0:
            messagebox.showinfo("Игра окончена", f"Вы проиграли! Загаданное слово: {self.secret_word}")
            self.play_after_losing()

    def play_after_losing(self):
        '''Resume the game after a loss.'''
        self.label_instruction.destroy()
        self.entry_character.destroy()
        self.word_label.destroy()
        self.guess_button.destroy()
        self.attempts_label.destroy()
        self.task_label.destroy()
        self.current_word_index = 0
        self.loss_flag = True
        self.start_over_button = tk.Button(self.master, text="Играть ещё раз", command=self.start_game, font='Arial', bg='green', fg='white')
        self.start_over_button.pack(pady=20)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x300')
    img = ImageTk.PhotoImage(Image.open('supergame.gif'))  
    image_label = tk.Label(image=img)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    game = Supergame(root, ["прямая", "парабола", "кубическая парабола", "гипербола"], ["Название графика функции y=x:", "Название графика функции y=x^2:", "Название графика функции y=x^3:", "Название графика функции y=k/x:"])
    root.mainloop()
