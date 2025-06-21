import os
import time
import threading
from random import randint

print(f"{'-=-'*12} JOGO DA BOMBA {'-=-'*12}")
print(f"\n Você tem 30 segundos para advinhar a combinação de 3 dígitos para desativar a bomba.")
print(f"\n{'-=-'*29}")
print(f'\n- Modo de jogo: [1] Fácil [2] Difícil')


while True:
    modo = input("\nEscolha: ")
    if modo == "1":
        for contagem in range(3, 0, -1):
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Modo fácil escolhido. Iniciando em {contagem}...")
            time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        print("Começou!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        break
    elif modo == "2":
        for contagem in range(3, 0, -1):
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Modo difícil escolhido. Iniciando em {contagem}...")
            time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        print("Começou!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        break
    else:
        print("\nOpção inválida. Tente novamente!")

tempo_esgotado = False
inicio = time.time()
cronometro_thread = threading.Thread(target=lambda: [
    (time.sleep(1), globals().__setitem__('tempo_esgotado', True)) if i == 29 else time.sleep(1)
    for i in range(30)
])
cronometro_thread.start()

codigo = f"{randint(0, 999):03d}"  


if modo == "1":
    acertou_primeiro = False
    acertou_segundo = False

    while not tempo_esgotado:
        if not acertou_primeiro:
            primeiro_digito = input("Primeiro dígito: ")
            if tempo_esgotado:
                break
            if primeiro_digito != codigo[0]:
                time.sleep(0.3)
                os.system("cls" if os.name == "nt" else "clear")
                print("Errado!\n***")
                continue
            acertou_primeiro = True

        if not acertou_segundo:
            time.sleep(0.3)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{primeiro_digito}**")
            segundo_digito = input("Segundo dígito: ")
            if tempo_esgotado:
                break
            if segundo_digito != codigo[1]:
                time.sleep(0.3)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Errado!\n{primeiro_digito}**")
                continue
            acertou_segundo = True

        time.sleep(0.3)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{primeiro_digito}{segundo_digito}*")
        terceiro_digito = input("Terceiro dígito: ")
        if tempo_esgotado:
            break
        if terceiro_digito != codigo[2]:
            time.sleep(0.3)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Errado!\n{primeiro_digito}{segundo_digito}*")
            continue

        # ✅ Acertou todos
        os.system("cls" if os.name == "nt" else "clear")
        print(f"✅ Código correto: {primeiro_digito}{segundo_digito}{terceiro_digito}")
        print("💣 Bomba desarmada! Parabéns!")
        fim = time.time()
        print(f"⏱️ Você levou {fim - inicio:.2f} segundos.")
        break

elif modo == "2":
    while not tempo_esgotado:
        tentativa = input("Digite os 3 dígitos de uma vez (ex: 042): ")

        if tempo_esgotado:
            break
        if tentativa == codigo:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"✅ Código correto: {tentativa}")
            print("💣 Bomba desarmada! Parabéns!")
            fim = time.time()
            print(f"⏱️ Você levou {fim - inicio:.2f} segundos.")
            break
        else:
            print("❌ Combinação incorreta. Tente novamente.")

if tempo_esgotado:
    print("\n💥 Tempo esgotado! A bomba explodiu!")
