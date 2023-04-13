from tkinter import *

class main:

    def __init__(self):
        
        self.janela = Tk()
        self.janela.title("Gerador de Folha Salarial")
        #usei minsize e maxsize como gambiarra pro resultado do calculo não esticar a janela infinitamente
        self.janela.minsize(width="300", height="600")
        self.janela.maxsize(width="300", height="600")
        self.janela.resizable(0,0)
        self.janela.config(bg="BLACK")

        self.labelHoras = Label(self.janela, font='arial 10 bold', bg="BLACK", fg="#68228B", text="DIGITE AS HORAS TRABALHADAS!")
        self.labelHoras.pack()

        #usei Spinbox para receber os valores de Horas e Salario
        #não usei Entry pois não consegui converter os valores de str para tipos numéricos
        #aceito dicas para melhorar
        #  
        self.spinHoras = Spinbox(self.janela, from_="0", to="999", font='arial 20 bold', bg="WHITE", fg="BLACK")
        self.spinHoras.pack()

        self.labelSalario = Label(self.janela, font='arial 10 bold', bg="BLACK", fg="WHITE", text="DIGITE SEU SALÁRIO POR HORA!")
        self.labelSalario.pack()

        self.spinSalario = Spinbox(self.janela, from_="0", to="999", font='arial 20 bold', bg="WHITE", fg="BLACK")
        self.spinSalario.pack()

        self.botaoCalcula = Button(self.janela, font='arial 12 bold', bg="BLACK", fg="WHITE", text="Calcular", command=lambda: self.calculo())
        self.botaoCalcula.pack(fill=X)
        
        self.janela.mainloop()

        self.SalarioBruto = float
        self.Ir = float
        self.SalarioLiquido = float
        self.DescFgts = float
        self.DescIr = float
        self.DescInss = float
        self.DescTotal = float

    def calculo(self):
        self.Inss = [0.10, "10%"]
        self.Fgts = [0.11, "11%"]
        self.Horas = self.spinHoras.get()
        self.Salario = self.spinSalario.get()
        self.SalarioBruto = float(self.Horas)*float(self.Salario)

        if self.SalarioBruto <= 900:
            self.Ir = [0.0, "0%"]
            
        elif self.SalarioBruto in range(901, 1500):
            self.Ir = [0.05, "5%"]
        
        elif self.SalarioBruto in range(1501, 2500):
            self.Ir = [0.10, "10%"]
            
        elif self.SalarioBruto > 2500:
            self.Ir = [0.20, "20"]

        self.DescFgts = self.SalarioBruto * self.Fgts[0]
        self.DescIr = self.SalarioBruto * self.Ir[0]
        self.DescInss = self.SalarioBruto * self.Inss[0]
        self.DescTotal = self.DescIr + self.DescInss
        self.SalarioLiquido = self.SalarioBruto - self.DescTotal 

        #criei esse Text dentro da função calculo pois não sei como chama-lo de fora da função
        #ele recebe .pack sempre que a função é chamada, então ele é gerado infinitamente e fica esticando a janela
        #usei o after como gambiarra pra ele aparecer sempre em cima do anterior, se não ele aparece em baixo e some
        #não consegui usar o pack_forget pra apagar o anterior a cada vez que é gerado um novo
        
        self.folhaSalario = Text(self.janela, font='arial 12 bold', bg="WHITE", fg="BLACK", width="36")
        self.folhaSalario.insert("1.0",f"SALÁRIO BRUTO: R$ {self.SalarioBruto}\nSALÁRIO LÍQUIDO: R${self.SalarioLiquido}\nFGTS: R$ {self.DescFgts}\nINSS: R$ {self.DescInss}\nIR: R$ {self.DescIr}\nDESCONTOS TOTAIS: R$ {self.DescTotal}")
        self.folhaSalario.pack(after=self.botaoCalcula)
    
main()