# %%
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import config, utils
import subprocess

ventana = tk.Tk()
ventana.title("Tablero Central de Ejecuciones")
ventana.geometry("700x400")

def mostrar_opcion():
    opcion_seleccionada = Lista_desplegable_opciones.get()  # Obtener la opción seleccionada
    print(text=f"Opción seleccionada: {opcion_seleccionada}")  # Mostrar el resultado

def ejecutar_consulta():
    lista = capturar_datos()
    credenciales = utils.Lectura_json(config.credenciales)
    consulta = utils.lectura_planos(config.Consulta)

    consulta = consulta.replace("_Fecha_",lista[-1])
    consulta = consulta.replace("_codigo_cliente_",lista[0])
    consulta = consulta.replace("_codigo_producto_",lista[1])

    df = utils.conexion_base_de_datos(
        credenciales["SQLSERVER"]["Servidor"],
        credenciales["SQLSERVER"]["Usuario"],
        credenciales["SQLSERVER"]["Password"],
        credenciales["SQLSERVER"]["Database"],
        consulta
    )

    df.to_csv('Salida_Tabla_parametros.txt', sep='|', index=False)
    messagebox.showinfo("Resultado", "Salida Exitosa")
    ventana.destroy()


def ejecutar_script(nombre_script):
    try:
        subprocess.run(["python", nombre_script], check=True)
        messagebox.showinfo("Resultado", "Salida Exitosa")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script: {e}")

def seleccionar_archivo():
    # Abre el explorador de archivos para seleccionar un archivo
    archivo = filedialog.askopenfilename(
        title="Seleccionar un archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    
    # Si el usuario selecciona un archivo, se imprime la ruta
    if archivo:
        print(f"Archivo seleccionado: {archivo}")

def actualizar_estado_campos(event):
    # Obtener la opción seleccionada del Combobox
    seleccion = Lista_desplegable_opciones.get()
    
    if seleccion == "Masiva":
        # Deshabilitar todos los campos de entrada en la lista
        for entry in lista_Datos_entrada:
            entry.config(state="disabled")
        # Habilitar el botón de explorar
        boton_explorar.config(state="normal")
    else:
        # Habilitar todos los campos de entrada en la lista
        for entry in lista_Datos_entrada:
            entry.config(state="normal")
        # Deshabilitar el botón de explorar
        boton_explorar.config(state="disabled")


def capturar_datos():
    # Recorre la lista de widgets y guarda los datos en una lista
    datos = [widget.get() for widget in lista_Datos_entrada]
    return datos  # Muestra los datos capturados en la consola

#Marco Botones Ejecutables
Marco_Ejecutables = tk.LabelFrame(ventana,
                      text="Ejecutables", 
                      padx=25, 
                      pady=25)
Marco_Ejecutables.grid(
    row=0,
    column=0,
    padx=10, 
    pady=10,
    sticky="nsew"
)

Marco_otros = tk.LabelFrame(
    ventana,
    text='Canales Contable',
    padx=11,
    pady=20
)

Marco_otros.grid(
    row=0,
    column=1,
    padx=10, 
    pady=10,
    sticky="nsew"
)

lista_Datos_entrada = []

# Crear varias etiquetas y entradas (Entry)
etiquetas = ["Codigo Cliente", "Codigo Producto"]

for i, etiqueta_texto in enumerate(etiquetas):
    etiqueta = tk.Label(Marco_otros, text=etiqueta_texto + ":")
    etiqueta.grid(row=i+1, column=0, padx=10, pady=5)
    
    # Crear un Entry para cada etiqueta
    entry = tk.Entry(Marco_otros, width=30)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    
    # Agregar el Entry a la lista
    lista_Datos_entrada.append(entry)

# Etiqueta para la fecha
etiqueta_fecha = tk.Label(Marco_otros, text="Selecciona una fecha:")
etiqueta_fecha.grid(row=7,column=0)

# Widget DateEntry
calendario = DateEntry(Marco_otros, width=20, background='darkblue', foreground='white', borderwidth=2,date_pattern='dd-mm-yyyy')
calendario.grid(row=7,column=1)

lista_Datos_entrada.append(calendario)
#lista_opciones
opciones = ["Masiva", "individual"]

#Etiqueta de la lista desplegable
Etiqueta_lista_des = tk.Label(Marco_otros, text="Selecciona Tipo:")
Etiqueta_lista_des.grid(row=0, column=0, padx=10, pady=10)

#lista desplegalbel
Lista_desplegable_opciones = ttk.Combobox(Marco_otros, values=opciones)
Lista_desplegable_opciones.grid(row=0, column=1,padx=10, pady=5)
Lista_desplegable_opciones.current(1)  # Seleccionar la primera opción por defecto

# Asignar la función de actualización del estado de los campos
Lista_desplegable_opciones.bind("<<ComboboxSelected>>", actualizar_estado_campos)

# Botón para abrir el explorador de archivos
boton_explorar = tk.Button(Marco_otros, text="Seleccionar Archivo", command=seleccionar_archivo,state="disabled")
boton_explorar.grid(row = 8, column=1,columnspan=2, pady=1)


boton_capturar = tk.Button(Marco_otros, text="Enviar Datos", command=ejecutar_consulta)
boton_capturar.grid(row=len(etiquetas) + 2, column=0, columnspan=2, pady=10)

# Inicializar el estado de los campos de entrada según la opción por defecto
actualizar_estado_campos(None)  # Llamar a la función para establecer el estado correcto

# Botones para cada script
boton_1 = tk.Button(Marco_Ejecutables, #ubicacion del boton, siempre debe estar en la ventana ya definida
                       text="Script 1", #texto que lleva el boton
                       command=lambda :ejecutar_script("script1.py"),#funcionalidad del Boton
                       width=12,#ancho del boton
                       height=1,#largo del boton
                       font=('Comic Sans MS',12),#fuente de la letra del boton
                       wraplength=100) #justifica el texto en el boton
boton_1.grid(row=3, column=0, padx=10, pady=10)

boton_2 = tk.Button(Marco_Ejecutables, 
                       text="Script 2", 
                       command=lambda :ejecutar_script("script2.py"),
                       width=12,
                       height=1,
                       font=('Comic Sans MS',12),
                       wraplength=100)
boton_2.grid(row=4, column=0, padx=10, pady=10)

boton_3 = tk.Button(Marco_Ejecutables, 
                       text="Script 3", 
                       command=lambda :ejecutar_script("script3.py"),
                       width=12,
                       height=1,
                       font=('Comic Sans MS',12),
                       wraplength=150)
boton_3.grid(row=5, column=0, padx=10, pady=10)



ventana.mainloop()



