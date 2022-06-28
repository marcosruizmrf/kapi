from cgitb import text

from setuptools import Command


menu_inicial = Tk()
menu_inicial.title("Titulo")
menu_inicial.geometry("500x300")

cmd = Button(menu_inicial, text="Executar", command=cmd_Click)
cmd.pack()
