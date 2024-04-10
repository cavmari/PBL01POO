import random

def preencher_lista(tamanho):
    lista = [random.randint(1, 100) for _ in range(tamanho)]
    return lista

def verificar_numeros(lista):
    for numero in lista:
        print(f"Número: {numero}")
        if numero % 3 == 0:
            print("  É múltiplo de 3")
        if numero % 2 == 0:
            print("  É par")
        else:
            print("  É ímpar")

def main():
    tamanho = int(input("Informe o tamanho da lista: "))
    lista = preencher_lista(tamanho)
    print("Lista gerada:", lista)
    verificar_numeros(lista)

if __name__ == "__main__":
    main()
