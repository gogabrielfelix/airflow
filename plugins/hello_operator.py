from airflow.models.baseoperator import BaseOperator
from typing import Any, Dict

class HelloOperator(BaseOperator):
    """
    Operador personalizado que imprime uma mensagem de saudação.
    
    :param name: Nome da pessoa a cumprimentar
    :type name: str
    """
    
    def __init__(self, name: str = "Mundo", **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name
        
    def execute(self, context: Dict[str, Any]) -> str:
        """
        Método chamado pelo Airflow quando a tarefa é executada
        """
        message = f"Olá, {self.name}!"
        print(message)
        return message 