nome=input('Qual seu nome? ').lower()
nota1=float(input('Qual a sua nota 1? '))
nota2=float(input('Qual a sua nota 1? '))
faltas=int(input('Qual o total de faltas? '))
presenca=int(((20-faltas)/20)*100)
media=(nota1 + nota2) / 2

if presenca >= 70 and media >= 6:
    resultado = 'Aluno Aprovado!!!'
    
elif presenca < 70 and media < 6:
    resultado = 'Reprovado por falta e por média'

elif presenca < 70 :
    resultado = 'Reprovado por falta'

elif media < 6:
    resultado = 'Reprovado por média'
        
else:
    print('erro')

print('Nome do aluno: ',nome)
print('Média: ',media)
print('Presença nas aulas: ',presenca,'%')
print('Resultado final: ',resultado)