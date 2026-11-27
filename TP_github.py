from tkinter import *
from tkinter import messagebox

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

def mostrar_productos():
    lista.delete(0, END)
    for producto in lista_productos:
        lista.insert(END, producto)

def eliminar_productos():
    posicion= lista.curselection()[0]
    lista.delete(posicion)


def buscar_producto():
    if entrada_busqueda.get().strip() in lista_productos:
        messagebox.showwarning("Buscar producto", "El producto se encuentra en la lista.")
    else:
        messagebox.showwarning("Buscar producto", "El producto no se encuentra en la lista.")

def cantidad_productos():
    messagebox.showwarning("Cantidad de productos",f"Hay {len(lista_productos)} productos almacenados.")

def limpiar_producto():
    producto.set("")

etiqueta_titulo= Label(root, text="Getion de productos", font= "Arial 16")
etiqueta_titulo.place(x=250, y=20)

etiqueta_producto= Label(root, text="Ingrese un producto:", font= "Arial 12")
etiqueta_producto.place(x=20, y= 70)

etiqueta_nombre= Entry(root, textvariable= producto) 
etiqueta_nombre.place(x=30, y=100)

etiqueta_bonton= Button(root , text="agregar producto" ,command=agregar_productos)
etiqueta_bonton.place(x=40, y=130)

boton_mostrar = Button(root, text="Mostrar productos", command=mostrar_productos)
boton_mostrar.place(x=200, y=130)

boton_eliminar= Button(root , text="eliminar producto" ,command= eliminar_productos)
boton_eliminar.place(x=200, y=80)

etiqueta_busqueda = Label(root, text="Buscar producto:", font="Arial 12")
etiqueta_busqueda.place(x=350, y=70)

entrada_busqueda = Entry(root)
entrada_busqueda.place(x=350, y=100)

boton_buscar = Button(root, text="Buscar", command=buscar_producto)
boton_buscar.place(x=385, y=130)

boton_cantidad = Button(root, text="Cantidad de productos", command=cantidad_productos)
boton_cantidad.place(x=490, y=130)

boton_limpiar = Button(root, text="Limpiar", command=limpiar_producto)
boton_limpiar.place(x=40, y=165)

lista = Listbox(root, width=75, height=16)
lista.place(x=120, y=210)

root.mainloop()