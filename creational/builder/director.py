from .builder import Engineer


class Supervisor:
    def __init__(self, engineer: Engineer) -> None:
        self.engineer = engineer

    def execute_job(self):
        self.engineer.make_foundations()
        self.engineer.raise_wall('east')
        self.engineer.raise_wall('west')
        self.engineer.raise_wall('south')
        self.engineer.raise_wall('north')
        self.engineer.create_roof()
        self.engineer.mount_insulation()
        self.engineer.paint()
        self.engineer.install_waterpool()
        self.engineer.make_garage()
