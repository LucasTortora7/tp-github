from tkinter import *

root= Tk()
root.title("Mi App")
root.geometry("700x501")
root.resizable(0,0)
root.config(bg="#F59556")

lista_productos = []
producto = StringVar()

def agregar_productos():
    produc = producto.get().strip()
    if not produc:
           return
   
    lista_productos.append(produc)
    producto.set("")
   

etiqueta_titulo= Label(root, text="Getion de productos", font= "Arial 16")
etiqueta_titulo.place(x=250, y=20)

etiqueta_producto= Label(root, text="Ingrese un producto:", font= "Arial 12")
etiqueta_producto.place(x=20, y= 70)

etiqueta_nombre= Entry(root, textvariable= producto) 
etiqueta_nombre.place(x=30, y=100)

etiqueta_bonton= Button(root , text="agregar producto" ,command=agregar_productos)
etiqueta_bonton.place(x=40, y=130)

lista = Listbox(root, width=75, height=16)
lista.place(x=30, y=180)

root.mainloop()