import tkinter as tk
from sympy import symbols, lambdify, SympifyError
from sympy.parsing.sympy_parser import parse_expr
import math
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



class VentanaPuntoFijo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Punto Fijo")

        # Crear los widgets
        self.funcion_label = tk.Label(self, text="Función f(x)")
        self.funcion_g_label = tk.Label(self, text="Función g(x)")
        self.valor_inicial_label = tk.Label(self, text="Valor inicial")
        self.tolerancia_label = tk.Label(self, text="Tolerancia")
        self.iteraciones_maximas_label = tk.Label(self, text="Iteraciones máximas")
        self.funcion_entry = tk.Entry(self)
        self.funcion_g_entry = tk.Entry(self)
        self.valor_inicial_entry = tk.Entry(self)
        self.tolerancia_entry = tk.Entry(self)
        self.iteraciones_maximas_entry = tk.Entry(self)
        self.resolver_button = tk.Button(self, text="Resolver", command=self.resolver)
        self.graficar_button = tk.Button(self, text="Graficar", command=self.graficar)
        self.graficar_button.grid(row=6, column=2)

     

        # Crear el Treeview para mostrar los resultados
        self.resultados_tree = ttk.Treeview(self, columns=("iteracion", "x_i", "x_siguiente", "error"), show="headings")
        self.resultados_tree.heading("iteracion", text="Iteración")
        self.resultados_tree.heading("x_i", text="x_i")
        self.resultados_tree.heading("x_siguiente", text="x_siguiente")
        self.resultados_tree.heading("error", text="Error")

        # Posicionar los widgets en la ventana
        self.funcion_label.grid(row=0, column=0)
        self.funcion_entry.grid(row=0, column=1)
        self.funcion_g_label.grid(row=1, column=0)
        self.funcion_g_entry.grid(row=1, column=1)
        self.valor_inicial_label.grid(row=2, column=0)
        self.valor_inicial_entry.grid(row=2, column=1)
        self.tolerancia_label.grid(row=3, column=0)
        self.tolerancia_entry.grid(row=3, column=1)
        self.iteraciones_maximas_label.grid(row=4, column=0)
        self.iteraciones_maximas_entry.grid(row=4, column=1)
        self.resolver_button.grid(row=5, column=0, columnspan=2)
        self.resultados_tree.grid(row=6, column=0, columnspan=2)

    def resolver(self):
        # Limpiar los resultados anteriores
        self.resultados_tree.delete(*self.resultados_tree.get_children())

        funcion = self.funcion_entry.get()
        funcion_g = self.funcion_g_entry.get()
        valor_inicial = float(self.valor_inicial_entry.get())
        tolerancia = float(self.tolerancia_entry.get())
        iteraciones_maximas = int(self.iteraciones_maximas_entry.get())

        try:
            # Verificar que las funciones ingresadas sean válidas
            x = symbols('x')
            parse_expr(funcion)
            parse_expr(funcion_g)
            f = lambdify(x, funcion)
            g = lambdify(x, funcion_g) # Assign the result of lambdify to the variable g
            if math.isnan(valor_inicial):
              raise ValueError("El valor inicial debe ser un número.")
            if tolerancia <= 0:
             raise ValueError("La tolerancia debe ser un número positivo.")

        # Verificar que el número máximo de iteraciones sea válido
            if iteraciones_maximas <= 0:
                raise ValueError("El número máximo de iteraciones debe ser un número positivo.")

            # Resolver el problema del punto fijo
            iteracion_actual = 0
            x_i = valor_inicial
            error = float('inf')

            while error > tolerancia and iteracion_actual < iteraciones_maximas:
                x_siguiente = g(x_i)
                error = abs(x_siguiente - x_i)
                iteracion_actual += 1
                x_i = x_siguiente

                # Agregar los resultados a la tabla
                self.resultados_tree.insert("", "end", values=(iteracion_actual, x_i, x_siguiente, error))

        except SympifyError:
            tk.messagebox.showerror("Error", "Las funciones ingresadas no son válidas.")
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def graficar(self):
        # Obtener la función ingresada
        funcion = self.funcion_entry.get()

        try:
            # Verificar que la función ingresada sea válida
            x = symbols('x')
            parse_expr(funcion)
            f = lambdify(x, funcion)

            # Crear la figura y el eje
            figura = Figure(figsize=(5, 4), dpi=100)
            eje = figura.add_subplot(111)

            # Calcular los valores de x y f(x) para graficar
            x_valores = list(range(-10, 11))
            y_valores = [f(x) for x in x_valores]

            # Graficar la función
            eje.plot(x_valores, y_valores)
            eje.axhline(0, color="black")
            eje.axvline(0, color="black")
            eje.set_xlabel('x')
            eje.set_ylabel('f(x)')

            # Mostrar la figura en la ventana
            canvas = FigureCanvasTkAgg(figura, master=self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)

        except SympifyError:
            tk.messagebox.showerror("Error", "La función ingresada no es válida.")


if __name__ == '__main__':
    ventana_iteracion = VentanaPuntoFijo()
    ventana_iteracion.mainloop()
