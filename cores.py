cores={'red':'vermelho' , 'blue':'azul' , 'yellow':'amarelo' , 'black':'preto' , 'white':'branco' , 'green':'verde'}
suacor=input('Escreva uma cor em inglês: ').lower()
traducao= cores.get(suacor, 'Esta cor não consta no dicionário')
print(traducao)
