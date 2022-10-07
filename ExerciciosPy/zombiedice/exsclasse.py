# =============================================================================
# class Casa():
#     def __init__(self, area: int, rua, cor, proprietario = None):
#         self.area = area
#         self.rua = rua
#         self.cor = cor
#         self.proprietario = proprietario
#         
#     def __str__(self):
#         return f"Nome do proprietário: {self.proprietario}\nÁrea: {self.area} m²\nRua: {self.rua}\nCor: {self.cor}"
#     
#     
# class Carro:
#     def __init__(self, marca: str, ano: int, modelo: str, motor: str, cor: str, portaMala: int):
#         self._marca = marca
#         self._ano = ano
#         self._modelo = modelo
#         self._motor = motor
#         self._cor = cor
#         self._portaMala = portaMala
#         self._ligado = False
#         
#     def __str__(self):
#         return f"{self._marca} {self._modelo} {self._ano}\nFicha Técnica:\nMotorização: {self._motor}\nCor: {self._cor}\nVolume do porta-malas: {self._portaMala}L"
#     
#     def isLigado(self):
#         if self._ligado:
#             return 'Motor ligado'
#         else:
#             return 'Motor desligado'
#         
#     def ligar(self):
#         self._ligado = True
#         
#     def desligar(self):
#         self._ligado = False
#     
# 
# jetta = Carro('Volkswagen', 2014, 'Jetta Highline TSI', '2.0 TSI 211cv', 'branco', 465)
# jetta.ligar()
# print(jetta)
# print(jetta.isLigado())
# 
# goleta = Carro('Volkswagen', 2011, 'Gol G5 Trend', '1.0', 'branco', 250)
# print(goleta)
# 
# =============================================================================

class Calculadora:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
    
    def setNum(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def somar(self):
        return self.n1 + self.n2
    
    def subtrair(self):
        return self.n1 - self.n2
    
    def multiplicar(self):
        return self.n1 * self.n2
    
    def dividir(self):
        try:
            return self.n1 / self.n2
        except:
            print('Erro: divisão por zero')
    
class CalculadoraCientifica(Calculadora):
    def __init(self):
        super().__init__()
        
    def quadrado(self):
        return self.n1**2, self.n2**2

calc = CalculadoraCientifica()
calc.setNum(10, 20)

