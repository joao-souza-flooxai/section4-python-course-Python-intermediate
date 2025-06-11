# Operadores Úteis:

# unido | uniao (union) - Une

# interseccao & (intersection) - Itens presentes em ambos
# diferenca - Itens presentes apenas no set da esquerda
# diferenca simétrica ~ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
print(s3)
s3 = s1 & s2
print(s3)
s3 = s1 - s2
print(s3)
s3 =  s2 - s1 
print(s3)
s3 =  s2 ^ s1 
print(s3)