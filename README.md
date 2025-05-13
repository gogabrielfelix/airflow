# Projeto Airflow

Este repositório contém a configuração do Apache Airflow utilizando Docker Compose.

## Estrutura do Projeto

```
.
├── config/          # Configurações personalizadas do Airflow
├── dags/            # DAGs do Airflow
├── logs/            # Logs do Airflow (não versionado)
├── plugins/         # Plugins personalizados
├── docker-compose.yaml  # Configuração do Docker Compose
├── requirements.txt # Dependências adicionais
└── README.md        # Este arquivo
```

## Como Usar

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. Inicie o Airflow:
   ```
   docker-compose up -d
   ```

3. Acesse a interface web:
   ```
   http://localhost:8080
   ```

4. Credenciais padrão:
   - Usuário: admin
   - Senha: (gerada na primeira execução, verifique os logs)

## Configurações

- A opção de carregar exemplos está desativada (`AIRFLOW__CORE__LOAD_EXAMPLES=False`)
- Volume de dados persistentes para PostgreSQL
- Montagem de diretórios locais para dags, logs, plugins e configurações
- Dependências extras instaladas automaticamente a partir do arquivo requirements.txt

## Publicando no GitHub

1. Inicialize um repositório Git:
   ```
   git init
   ```

2. Adicione os arquivos:
   ```
   git add .
   ```

3. Faça o primeiro commit:
   ```
   git commit -m "Configuração inicial do Airflow"
   ```

4. Crie um repositório no GitHub e adicione-o como remoto:
   ```
   git remote add origin https://github.com/seu-usuario/seu-repositorio.git
   ```

5. Envie os arquivos para o GitHub:
   ```
   git push -u origin main
   ```

## Como Migrar do Portainer

1. Pare e remova o container existente no Portainer (se estiver em execução).

2. Clone o repositório do GitHub no servidor:
   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

3. Inicie o Airflow usando o docker-compose:
   ```
   docker-compose up -d
   ```

4. Para preservar os dados anteriores, você pode:
   - Realizar backup do banco de dados PostgreSQL
   - Copiar suas DAGs anteriores para o diretório dags/
   - Restaurar variáveis e conexões importantes 