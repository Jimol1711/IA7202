from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(
        self,
        nombre: str,
        unidad: str,
    ) -> None:
        self.nombre = nombre
        self.unidad = unidad

    @abstractmethod
    def es_riesgo(self, valor: float) -> bool:
        return False


class SensorTemperatura(Sensor):
    def __init__(
        self,
        _minimo: int,
        _maximo: int,
    ) -> None:
        super().__init__("temperatura", "°C")
        self._minimo = _minimo
        self._maximo = _maximo

    def es_riesgo(self, valor: float) -> bool:
        if not -100 <= valor <= 100:
            return False
        return valor < self._minimo or valor > self._maximo


class SensorViento(Sensor):
    def __init__(
        self,
        _maximo: int,
    ) -> None:
        super().__init__("viento", "km/h")
        self._maximo = _maximo

    def es_riesgo(self, valor: float) -> bool:
        if not 0 <= valor <= 500:
            return False
        return valor > self._maximo


class SensorHumedad(Sensor):
    def __init__(
        self,
        _maximo: int,
    ) -> None:
        super().__init__("humedad", "%")
        self._maximo = _maximo

    def es_riesgo(self, valor: float) -> bool:
        if not 0 <= valor <= 100:
            return False
        return valor > self._maximo
