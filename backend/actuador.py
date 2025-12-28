class SimulatedActuator:
    """
    Actuador industrial simulado.
    Representa pistones, semáforos o desviadores en una línea de producción.
    """

    def pass_piece(self):
        print("🟢 ACTUADOR: Pieza aceptada → continúa en la línea")

    def alert(self):
        print("🟡 ACTUADOR: Defecto leve → marcar para revisión")

    def reject(self):
        print("🔴 ACTUADOR: Defecto crítico → pieza rechazada (pistón simulado)")
