#ejercicio 1
# codigo
class CuentaBancaria:
    def __init__(self, numero, titular, saldo_inicial):
        assert type(numero)== int and numero >0, ' debe ingresar un numero entero positivo'
        assert type(titular) == str and len(titular)>0, ' debe ingresar una cadena de caracteres positiva'
        assert isinstance(saldo_inicial, (int, float)) and saldo_inicial >=0, ' debe ingresar un numero mayor o igual a cero'

        self.__numero = numero
        self.__titular = titular
        self._saldo_inicial = saldo_inicial

    def get_numero(self):
        return self.__numero
    def get_titular(self):
        return self.__titular
    def get_saldo(self):
        return self._saldo_inicial
    def depositar(self, monto:float):
        assert isinstance(monto, (int, float)) and monto > 0, ' debe ingresar un monto positivo'
        self._saldo_inicial += monto
    
    def extraer(self, monto):
        assert isinstance(monto, (int, float)) and monto > 0 , ' no hay saldo suficiente'
        self._saldo_inicial -= monto

    def __str__(self):
        return f"Cuenta: {self.__numero}| Titular: {self.__titular}| Saldo: {self._saldo_inicial}"
    
#Tests
c = CuentaBancaria(1001, "Ana Pérez", 1000)

assert c.get_numero() == 1001
assert c.get_titular() == "Ana Pérez"
assert c.get_saldo() == 1000

c.depositar(500)
assert c.get_saldo() == 1500

c.extraer(300)
assert c.get_saldo() == 1200

print(c)