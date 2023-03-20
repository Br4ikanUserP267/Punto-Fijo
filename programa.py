import tkinter as tk
import matplotlib.pyplot as plt

class IteracionPuntoFijo:
    def __init__(self):
        self.funcion = None
        self.valorInicial = None
        self.tolerancia = None
    
    def ingresarValores(self, funcion, valorInicial, tolerancia):
        self.funcion = funcion
        self.valorInicial = float(valorInicial)
        self.tolerancia = float(tolerancia)
    

    
    def realizarIteracion(self):
        valorAnterior = self.valorInicial
        try:
            valorActual = eval(self.funcion.replace('x', str(valorAnterior)))
        except (SyntaxError, TypeError, NameError):
            print("Error: Invalid expression entered for function")
            return []
        valoresIteracion = [valorAnterior, valorActual]

        while abs(valorActual - valorAnterior) > self.tolerancia:
            valorAnterior = valorActual
            try:
                valorActual = eval(self.funcion.replace('x', str(valorAnterior)))
            except (SyntaxError, TypeError, NameError):
                print("Error: Invalid expression entered for function")
                return valoresIteracion
            valoresIteracion.append(valorActual)

        return valoresIteracion
        
    def graficarIteracion(self, valoresIteracion):
        x = range(len(valoresIteracion))
        y = valoresIteracion
        
        plt.plot(x, y, 'ro-')
        plt.xlabel('Iteraciones')
        plt.ylabel('Valores')
        plt.title('Iteración con Punto Fijo')
        plt.show()
class VentanaIteracion:
    def __init__(self, root):
        self.root = root
        self.iteracion = IteracionPuntoFijo()
        self.ventana = tk.Frame(self.root)
        self.ventana.pack()
        
        # Etiquetas y cuadros de entrada para la función, el valor inicial y la tolerancia
        self.etiquetaFuncion = tk.Label(self.ventana, text="Función:")
        self.etiquetaFuncion.grid(row=0, column=0, padx=10, pady=10)
        self.cuadroFuncion = tk.Entry(self.ventana, width=30)
        self.cuadroFuncion.grid(row=0, column=1, padx=10, pady=10)
        
        self.etiquetaValorInicial = tk.Label(self.ventana, text="Valor Inicial:")
        self.etiquetaValorInicial.grid(row=1, column=0, padx=10, pady=10)
        self.cuadroValorInicial = tk.Entry(self.ventana, width=30)
        self.cuadroValorInicial.grid(row=1, column=1, padx=10, pady=10)
        
        self.etiquetaTolerancia = tk.Label(self.ventana, text="Tolerancia:")
        self.etiquetaTolerancia.grid(row=2, column=0, padx=10, pady=10)
        self.cuadroTolerancia = tk.Entry(self.ventana, width=30)
        self.cuadroTolerancia.grid(row=2, column=1, padx=10, pady=10)
        
        # Botón para realizar la iteración y mostrar la gráfica
        self.botonIterar = tk.Button(self.ventana, text="Realizar Iteración", command=self.realizarIteracion)
        self.botonIterar.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
    
    def realizarIteracion(self):
        # Get function, initial value and tolerance from the input fields
        funcion = self.cuadroFuncion.get()
        valorInicial = float(self.cuadroValorInicial.get())
        tolerancia = float(self.cuadroTolerancia.get())
        
        self.iteracion.ingresarValores(funcion, valorInicial, tolerancia)
    
        # Perform iteration
        valoresIteracion = self.iteracion.realizarIteracion()
    
    # Display results and graph
        self.iteracion.graficarIteracion(valoresIteracion)
if __name__ == '__main__':
    root = tk.Tk()
    ventana_iteracion = VentanaIteracion(root)
    root.mainloop()