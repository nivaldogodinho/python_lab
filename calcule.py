print ('Calcule a média do aluno 2020.1')
nome=input('Qual o nome do aluno?')
nota1=int(input('Qual a primeira nota'))
nota2=int(input('Qual a segunta nota'))
media=int((nota1+nota2)/2)

if media >= 60:
    print('Aluno passou')
else:
    print('Aluno reprovado')

print('A média do aluno',nome,'é',media)