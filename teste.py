notas = []

for i in range(5):
       nota = float(input(f"Digite a nota {i+1}: "))
       notas.append(nota)

media = sum(notas)/len(notas)
maior = max(notas)
menor = min(notas)

def situacao(media):
     if media >= 7:
        return "Aprovado"
     elif media >= 5:
        return "Recuperação"
     else:
        return "Reprovado"
     
aprovados = [nota for nota in notas if nota >= 7]

print("Notas:", notas)
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média:", media)
print("Notas aprovadas:", aprovados)
print("notas reprovadas:", aprovados)