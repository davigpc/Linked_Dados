# Linked_Dados

Projeto desenvolvido para o processo seletivo em análise de dados da Linked EJ - 2024.

## Descrição

Este projeto consiste na análise exploratória de um conjunto de dados fictício sobre atendimentos ao cliente em um ambiente de e-commerce. O objetivo é realizar análises estatísticas e visualizações para extrair insights relevantes que possam ser úteis para a empresa.

## Requisitos

- Python 3.x
- Bibliotecas: Pandas, Matplotlib, Seaborn

Certifique-se de ter Python instalado em sua máquina e as bibliotecas listadas. Você pode instalar as dependências com o seguinte comando:

```bash
pip install pandas matplotlib seaborn
```

## Conjunto de Dados
O conjunto de dados utilizado contém informações sobre atendimentos ao cliente e inclui as seguintes colunas:

- Unique id: Identificador único do atendimento
- channel_name: Nome do canal de atendimento (inbound, outcall, etc.)
- category: Categoria do atendimento
- Sub-category: Subcategoria do atendimento
- Customer Remarks: Observações do cliente
- Order_id: Identificador do pedido
- order_date_time: Data e hora do pedido
- Issue_reported at: Data e hora do reporte do problema
- issue_responded: Data e hora da resposta ao problema
- Survey_response_Date: Data da resposta à pesquisa de satisfação (formato: DD-Mmm-YY)
- Customer_City: Cidade do cliente
- Product_category: Categoria do produto relacionado ao atendimento
- Item_price: Preço do item
- connected_handling_time: Tempo de atendimento conectado
- Agent_name: Nome do agente responsável pelo atendimento
- Supervisor: Nome do supervisor do agente
- Manager: Nome do gerente do agente
- Tenure Bucket: Intervalo de tempo de permanência do agente
- Agent Shift: Turno do agente
- CSAT Score: Pontuação de satisfação do cliente (1 a 5)

## Análises Realizadas
- Distribuição do CSAT Score.
- Relação entre o CSAT Score e categorias de produtos.
- Relação entre o CSAT Score e canais de atendimento.
- Distribuição e contagem de atendimentos por intervalo de tempo de permanência de funcionários.

## Como executar

Clone o repositório em sua máquina
```bash
git clone https://github.com/davigpc/Linked_Dados
```

Execute o script

```bash
python analise.py
```
