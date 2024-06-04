import tkinter as tk


class Flashcard:
    def __init__(self, root):
        self.root = root
        self.root.title('flashcard app')

        self.flashcards = [('rusia','moscow'),('paises bajos','amsterdam'),('suecia','estocolmo')]
        self.current_index = 0

        self.card_frame = tk.Frame(self.root)
        self.card_frame.grid(row = 0, column = 0,pady = 20)

        self.card_label = tk.Label(self.card_frame, text = ' ',font=('Arial',24),width= 15,height=5)
        self.card_label.grid(row=1,column=0)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=1,column=0)

        self.show_button = tk.Button(self.button_frame,text='show answer',command=self.flip_card)
        self.show_button.grid(row=2,column=0)

        self.next_button = tk.Button(self.button_frame,text = 'next card',command=self.next_card)
        self.next_button.grid(row=3,column=0)

        self.show_card()
    def show_card(self):
        self.show_answer = False
        self.card_label.config(text=self.flashcards[self.current_index][0])
        self.show_button.config(text='show answer')
    def flip_card(self):
        if self.show_answer:
            self.card_label.config(text=self.flashcards[self.current_index][0])
            self.show_button.config(text='show answer')
        else:
            self.card_label.config(text=self.flashcards[self.current_index][1])
            self.show_button.config(text='show question')
        self.show_answer = not self.show_answer
    def next_card(self):
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.show_card()
if __name__ == "__main__":
    root = tk.Tk()
    app = Flashcard(root)
    root.mainloop()