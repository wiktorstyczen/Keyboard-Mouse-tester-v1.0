import tkinter

window = tkinter.Tk()

window.title("Sprawdzanie działania przycisków myszy oraz klawiszy na klawiaturze.")

def left_click(event):
 tkinter.Label(window, text = "Lewy przycisk działa!").pack()
def middle_click(event):
 tkinter.Label(window, text = "Kółko myszy działa!").pack()
def right_click(event):
 tkinter.Label(window, text = "Prawy przycisk działa!").pack()
def key_a(event):
 tkinter.Label(window, text = "Klawisz A działa!").pack()
def key_w(event):
 tkinter.Label(window, text = "Klawisz W działa!").pack()
def key_r(event):
 tkinter.Label(window, text = "Klawisz R działa!").pack()
def key_q(event):
 tkinter.Label(window, text = "Klawisz Q działa!").pack()
def key_e(event):
 tkinter.Label(window, text = "Klawisz E działa!").pack()
def key_s(event):
 tkinter.Label(window, text = "Klawisz S działa!").pack()
def key_t(event):
 tkinter.Label(window, text = "Klaiwsz T działa!").pack()
def key_y(event):
 tkinter.Label(window, text = "Klawisz Y działa!").pack()
def key_u(event):
 tkinter.Label(window, text = "Klawisz U działa!").pack()
def key_i(event):
 tkinter.Label(window, text = "Klawisz I działa!").pack()
def key_o(event):
 tkinter.Label(window, text = "Klawisz O działa!").pack()
def key_p(event):
 tkinter.Label(window, text = "Klawisz P działa!").pack()
def key_d(event):
 tkinter.Label(window, text = "Klawisz D działa!").pack()
def key_f(event):
 tkinter.Label(window, text = "Klawisz F działa!").pack()
def key_g(event):
 tkinter.Label(window, text = "Klawisz G działa!").pack()
def key_h(event):
 tkinter.Label(window, text = "Klawisz H działa!").pack()
 
window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)
window.bind("<a>", key_a)
window.bind("<w>", key_w)
window.bind("<r>", key_r)
window.bind("<q>", key_q)
window.bind("<e>", key_e)
window.bind("<s>", key_s)
window.bind("<t>", key_t)
window.bind("<y>", key_y)
window.bind("<u>", key_u)
window.bind("<i>", key_i)
window.bind("<o>", key_o)
window.bind("<p>", key_p)
window.bind("<d>", key_d)
window.bind("<f>", key_f)
window.bind("<g>", key_g)
window.bind("<h>", key_h)

window.mainloop()