"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
Print na tela com "print"
"""

primeira = float(input('Digite a primeira nota: '))
segunda = float(input('Digite a segunda nota: '))
terceira = float(input('Digite a terceira nota: '))

media = float((primeira + segunda + terceira)/3)

print(f'Média: {media:.2f}')
