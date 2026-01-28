from dataclasses import dataclass
from typing import List, Dict


@dataclass(frozen=True)
class Transaccion:
    """Representa una transacción contable."""
    fecha: str
    descripcion: str
    monto: float
    tipo: str


class LibroDiario:
    """Gestiona las transacciones del libro diario."""

    def __init__(self) -> None:
        """Inicializa el libro diario."""
        self.transacciones: List[Transaccion] = []

    def agregar_transaccion(
        self,
        fecha: str,
        descripcion: str,
        monto: float,
        tipo: str,
    ) -> None:
        """Agrega una transacción validando los datos."""
        if tipo not in {"ingreso", "egreso"}:
            raise ValueError("Tipo de transacción inválido")

        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser numérico")

        if monto <= 0:
            raise ValueError("El monto debe ser positivo")

        transaccion = Transaccion(
            fecha=fecha,
            descripcion=descripcion,
            monto=float(monto),
            tipo=tipo,
        )
        self.transacciones.append(transaccion)

    def obtener_resumen(self) -> Dict[str, float]:
        """Devuelve el total de ingresos y egresos."""
        ingresos = 0.0
        egresos = 0.0

        for transaccion in self.transacciones:
            if transaccion.tipo == "ingreso":
                ingresos += transaccion.monto
            else:
                egresos += transaccion.monto

        return {
            "ingresos": ingresos,
            "egresos": egresos,
        }
