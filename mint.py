import pyautogui as souris
import time

def main():
    # Délai de 5 secondes pour vous permettre de passer à la fenêtre souhaitée
    print("L'automatisation commencera dans 10 secondes...")
    time.sleep(10)

    currentMouseX, currentMouseY = souris.position()
    print(currentMouseX, currentMouseY)

    # Déplacement de la souris pour Mint
    try:
        souris.moveTo(725, 838, duration=1)
    except Exception as e:
        print(f'Erreur en déplaçant la souris: {e}')
    # Exemple de clic de souris
    souris.click()

    time.sleep(5)
    # Déplacement de la souris pour cliquer sur le wallet
    try:
        souris.moveTo(725, 850, duration=1)
        souris.click()
    except Exception as e:
        print(f'Erreur en déplaçant la souris: {e}')

    time.sleep(10)



if __name__ == "__main__":
    while True:
        main()
