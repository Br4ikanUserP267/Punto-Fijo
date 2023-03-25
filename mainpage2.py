# Importar librerías
import subprocess
import tkinter as tk

# Definir una función para abrir un script de Python
def open_programa():
    subprocess.Popen(["python", "programa.py"])

# Crear una ventana raíz Tkinter y establecer su título a "Punto Fijo".
root = tk.Tk()
root.title("Punto Fijo")

# Título y definición del tema
fixed_point = "PUNTO FIJO"
fixed_point_definition = """
Un punto fijo es un punto de una función en el que el valor de salida no cambia 
cuando el valor de entrada se utiliza como valor de salida. Los puntos fijos tienen muchas 
aplicaciones, como la resolución de ecuaciones y la simulación de sistemas dinámicos.
"""
# Crear una etiqueta para la definición y explicación de punto fijo
fixed_point_label = tk.Label(root, text=fixed_point, font=("Times New Roman", 20))
fixed_point_label.pack()
fixed_point_label = tk.Label(root, text=fixed_point_definition, padx=10, pady=5, font=("Times New Roman", 13))
fixed_point_label.pack()

# Muestra la función del programa
input_data_title = "Función del programa"
input_data = """
Este programa calcula el punto fijo de una función mediante el método iterativo 
iterativo. El usuario necesita introducir una función, su derivada, la toleracia, una estimación inicial para el punto fijo 
y el número máximo de iteraciones a realizar.
"""
input_data_title_label = tk.Label(root, text=input_data_title, font=("Times New Roman", 16))
input_data_title_label.pack()
input_data_label = tk.Label(root, text=input_data, padx=10, pady=5, font=("Times New Roman", 13))
input_data_label.pack()

# Botón que accede a el programa
button = tk.Button(root, text="Acceder a la aplicación", font=("Times New Roman", 13) , command=open_programa)
button.pack()

# Corre el programa
root.mainloop()
