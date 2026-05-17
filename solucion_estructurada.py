"""
Solución estructurada: Clientes y cuentas bancarias usando diccionarios.

Representación:
  - Un cliente es un diccionario con las claves:
        "dni"      : int   — identificador único
        "nombre"   : str
        "apellido" : str
        "cuentas"  : list[dict] — lista de cuentas bancarias del cliente

  - Una cuenta bancaria es un diccionario con las claves:
        "numero"  : int   — número de cuenta (único globalmente)
        "tipo"    : str   — "caja_ahorro" o "cuenta_corriente"
        "saldo"   : float — saldo actual (>= 0)

Nota: todas las funciones reciben y devuelven estas estructuras directamente.
No existe ningún mecanismo que impida acceder o modificar cualquier campo desde
afuera; la consistencia depende enteramente de que se usen siempre las funciones
definidas aquí.
"""

# ---------------------------------------------------------------------------
# Constructores (funciones que crean las estructuras)
# ---------------------------------------------------------------------------

def crear_cliente(dni: int, nombre: str, apellido: str) -> dict:
    """
    Crea y devuelve un nuevo cliente sin cuentas.

    Precondiciones:
        - dni es un entero de 7 u 8 dígitos
        - nombre y apellido son strings no vacíos

    >>> c = crear_cliente(12345678, "Juan", "Pérez")
    >>> c["dni"]
    12345678
    >>> c["cuentas"]
    []
    """
    assert isinstance(dni, int) and 1_000_000 <= dni <= 99_999_999, \
        "El DNI debe tener 7 u 8 dígitos"
    assert isinstance(nombre, str) and nombre.strip() != "", \
        "El nombre no puede estar vacío"
    assert isinstance(apellido, str) and apellido.strip() != "", \
        "El apellido no puede estar vacío"

    return {
        "dni": dni,
        "nombre": nombre.strip(),
        "apellido": apellido.strip(),
        "cuentas": [],
    }


def crear_cuenta(numero: int, tipo: str, saldo_inicial: float = 0.0) -> dict:
    """
    Crea y devuelve una nueva cuenta bancaria.

    Precondiciones:
        - numero es un entero positivo
        - tipo es "caja_ahorro" o "cuenta_corriente"
        - saldo_inicial >= 0

    >>> cc = crear_cuenta(1001, "caja_ahorro", 500.0)
    >>> cc["saldo"]
    500.0
    """
    tipos_validos = {"caja_ahorro", "cuenta_corriente"}
    assert isinstance(numero, int) and numero > 0, \
        "El número de cuenta debe ser un entero positivo"
    assert tipo in tipos_validos, \
        f"El tipo debe ser uno de: {tipos_validos}"
    assert isinstance(saldo_inicial, (int, float)) and saldo_inicial >= 0, \
        "El saldo inicial no puede ser negativo"

    return {
        "numero": numero,
        "tipo": tipo,
        "saldo": float(saldo_inicial),
    }


# ---------------------------------------------------------------------------
# Operaciones sobre un cliente y sus cuentas
# ---------------------------------------------------------------------------

def agregar_cuenta(cliente: dict, cuenta: dict) -> None:
    """
    Agrega una cuenta bancaria al cliente.

    Precondiciones:
        - cliente fue creado con crear_cliente
        - cuenta fue creada con crear_cuenta
        - el número de la cuenta no existe ya en el cliente

    La función modifica cliente en el lugar (efecto secundario).
    """
    numeros_existentes = {c["numero"] for c in cliente["cuentas"]}
    assert cuenta["numero"] not in numeros_existentes, \
        f"El cliente ya tiene una cuenta con número {cuenta['numero']}"

    cliente["cuentas"].append(cuenta)


def depositar(cliente: dict, numero_cuenta: int, monto: float) -> None:
    """
    Deposita monto en la cuenta indicada del cliente.

    Precondiciones:
        - monto > 0
        - el número de cuenta existe en el cliente
    """
    assert isinstance(monto, (int, float)) and monto > 0, \
        "El monto a depositar debe ser positivo"

    cuenta = _buscar_cuenta(cliente, numero_cuenta)
    assert cuenta is not None, \
        f"El cliente no tiene una cuenta con número {numero_cuenta}"

    cuenta["saldo"] += monto


def extraer(cliente: dict, numero_cuenta: int, monto: float) -> None:
    """
    Extrae monto de la cuenta indicada del cliente.

    Precondiciones:
        - monto > 0
        - el número de cuenta existe en el cliente
        - el saldo resultante no queda negativo
    """
    assert isinstance(monto, (int, float)) and monto > 0, \
        "El monto a extraer debe ser positivo"

    cuenta = _buscar_cuenta(cliente, numero_cuenta)
    assert cuenta is not None, \
        f"El cliente no tiene una cuenta con número {numero_cuenta}"
    assert cuenta["saldo"] >= monto, \
        "Saldo insuficiente"

    cuenta["saldo"] -= monto


def saldo_total(cliente: dict) -> float:
    """
    Devuelve la suma de saldos de todas las cuentas del cliente.

    >>> c = crear_cliente(12345678, "Ana", "López")
    >>> agregar_cuenta(c, crear_cuenta(1, "caja_ahorro", 100.0))
    >>> agregar_cuenta(c, crear_cuenta(2, "cuenta_corriente", 250.0))
    >>> saldo_total(c)
    350.0
    """
    return sum(c["saldo"] for c in cliente["cuentas"])


def nombre_completo(cliente: dict) -> str:
    """
    Devuelve el nombre completo del cliente en formato 'Nombre Apellido'.
    """
    return f"{cliente['nombre']} {cliente['apellido']}"


# ---------------------------------------------------------------------------
# Operaciones sobre el conjunto de clientes
# ---------------------------------------------------------------------------

def cliente_mas_rico(clientes: list[dict]) -> dict:
    """
    Devuelve el cliente con mayor saldo total entre todos los clientes.

    Precondiciones:
        - clientes es una lista no vacía de clientes creados con crear_cliente

    En caso de empate devuelve el primero encontrado.
    """
    assert len(clientes) > 0, "La lista de clientes no puede estar vacía"

    mejor = clientes[0]
    for cliente in clientes[1:]:
        if saldo_total(cliente) > saldo_total(mejor):
            mejor = cliente
    return mejor


def clientes_con_saldo_minimo(clientes: list[dict], minimo: float) -> list[dict]:
    """
    Devuelve la lista de clientes cuyo saldo total es mayor o igual a minimo.

    Precondiciones:
        - minimo >= 0
    """
    assert minimo >= 0, "El monto mínimo no puede ser negativo"
    return [c for c in clientes if saldo_total(c) >= minimo]


def resumen_clientes(clientes: list[dict]) -> None:
    """
    Imprime por pantalla un resumen de cada cliente: nombre, cantidad de
    cuentas y saldo total.
    """
    for cliente in clientes:
        n_cuentas = len(cliente["cuentas"])
        total = saldo_total(cliente)
        print(
            f"{nombre_completo(cliente)}"
            f" | DNI: {cliente['dni']}"
            f" | Cuentas: {n_cuentas}"
            f" | Saldo total: ${total:,.2f}"
        )


# ---------------------------------------------------------------------------
# Función auxiliar (privada por convención)
# ---------------------------------------------------------------------------

def _buscar_cuenta(cliente: dict, numero: int) -> dict | None:
    """
    Devuelve la cuenta del cliente con el número dado, o None si no existe.
    Función interna; no forma parte de la interfaz pública.
    """
    for cuenta in cliente["cuentas"]:
        if cuenta["numero"] == numero:
            return cuenta
    return None


# ---------------------------------------------------------------------------
# Demostración
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Crear clientes
    ana = crear_cliente(12345678, "Ana", "López")
    carlos = crear_cliente(87654321, "Carlos", "García")
    marta = crear_cliente(11223344, "Marta", "Fernández")

    # Crear y asignar cuentas
    agregar_cuenta(ana, crear_cuenta(1001, "caja_ahorro", 1_500.0))
    agregar_cuenta(ana, crear_cuenta(1002, "cuenta_corriente", 800.0))

    agregar_cuenta(carlos, crear_cuenta(2001, "caja_ahorro", 300.0))

    agregar_cuenta(marta, crear_cuenta(3001, "caja_ahorro", 2_000.0))
    agregar_cuenta(marta, crear_cuenta(3002, "cuenta_corriente", 500.0))
    agregar_cuenta(marta, crear_cuenta(3003, "caja_ahorro", 750.0))

    # Operaciones
    depositar(ana, 1001, 200.0)
    extraer(carlos, 2001, 50.0)

    # Resumen
    clientes = [ana, carlos, marta]
    print("=== Resumen de clientes ===")
    resumen_clientes(clientes)

    print("\n=== Cliente más rico ===")
    rico = cliente_mas_rico(clientes)
    print(f"{nombre_completo(rico)} con ${saldo_total(rico):,.2f}")

    print("\n=== Clientes con saldo >= $1000 ===")
    ricos = clientes_con_saldo_minimo(clientes, 1_000.0)
    for c in ricos:
        print(f"  {nombre_completo(c)}")
