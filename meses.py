meses=('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
datanasc=input('Coloque a sua data de nascimento, no formato DD-MM-AAAA: ')
mesnascNum=int(datanasc[3:5])
mesnascMenos1=mesnascNum-1
mesnascStr=meses[mesnascMenos1]
print('Você nasceu no mês: ',mesnascStr)