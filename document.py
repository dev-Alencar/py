
import pandas as pd
import plotly.express as px

# 1. Criando os dados (como se fosse uma planilha)
vendas = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr'],
    'Receita': [10500, 12000, 9000, 15000]
}

# 2. Transformando em um DataFrame (A "super tabela" do Pandas)
df = pd.DataFrame(vendas)

# 3. Criando um gráfico de linha interativo
fig = px.line(df,
              x='Mês',
              y='Receita',
              title='Desempenho de Vendas da Startup',
              markers=True) # Adiciona pontos nos meses

# 4. Exibindo o resultado
print(fig.show())
