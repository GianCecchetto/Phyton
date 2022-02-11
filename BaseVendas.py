import pandas as pd
import win32com.client as win32

#importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

#visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

#faturamento po loja
Faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(Faturamento)

#quantidade de produtos vendidos por loja
Produtos = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(Produtos)

print('-' * 50)
#ticket médio por produto em cada loja física
ticket_medio = (Faturamento['Valor Final'] / Produtos['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

#enviar um email com o relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'gececchetto@gmail.com'
mail.Subject = 'Relatório de Vendas po Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de vendas por cada Loja</p>

<p>Faturamento:</p>
{Faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Produtos:</p>
{Produtos.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>Gianlucca</p>
'''

mail.Send()

print('Email Enviado')