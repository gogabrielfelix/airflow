from __future__ import annotations

from airflow.plugins_manager import AirflowPlugin
from plugins.operators.hello_operator import HelloOperator

# Expondo nossos operadores personalizados
__all__ = [
    'HelloOperator',
]

# Classe que registra nosso plugin no Airflow
class CustomOperatorsPlugin(AirflowPlugin):
    name = "custom_operators_plugin"
    operators = [HelloOperator] 