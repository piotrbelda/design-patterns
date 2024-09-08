from .builder import FieldEngineer
from .director import Supervisor

builder = FieldEngineer()
supervisor = Supervisor(builder)
supervisor.execute_job()
print(builder.get_results())
