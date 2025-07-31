"""
Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas 
até que o professor digite 'fim'. Notas válidas são de 0 a 10. 
O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.
"""
def registrar_notas():

    notas = []
    
    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
        
        if entrada.lower() == 'fim':
            break
           notas = float(entrada)
           if 0 <= notas <= 10:
              lista_notas.append(notas)
           else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
            continue    
            except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim' para

    if lista_notas:
        media = sum(lista_notas) / len(lista_notas)
        print(f"A média da turma é: {media:.2f}")
        print(f"Total de notas válidas registradas: {len(lista_notas)}")
    else:
        print("Nenhuma nota foi lançada.") 
          





















        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim' para encerrar.")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"A média da turma é: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada.")
registrar_notas()



                

