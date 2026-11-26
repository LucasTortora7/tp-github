from tkinter import *
from tkinter import messagebox

root= Tk()
root.title("Mi App")
root.geometry("700x501")
root.resizable(0,0)
root.config(bg="#F59556")

lista_productos = []

etiqueta_titulo= Label(root, text="Getion de productos", font= "Arial 16")
etiqueta_titulo.place(x=250, y=20)

etiqueta_producto= Label(root, text="Ingrese un producto:", font= "Arial 12")
etiqueta_producto.place(x=20, y= 70)

etiqueta_nombre= Entry(root, textvariable= lista_productos) 
etiqueta_nombre.place(x=30, y=100)

root.mainloop()