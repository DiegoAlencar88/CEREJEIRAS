#VARIAVEIS 

import pyautogui
import time
##BIBLIOTECA INFO

linha_atual = 0


for _ in range(532):

    time.sleep(3)
    pyautogui.PAUSE = 2
    #ABRIR ABA
    pyautogui.click(x=234, y=488)
    #CLICAR ABA
    pyautogui.click(x=213, y=603)

    #SELEÇÂO QNTS X

    pyautogui.click(x=458, y=300)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    #QUANTAS UNIDADES

    pyautogui.click(x=454, y=359)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    #CONTA CONTABIL


    pyautogui.click(x=467, y=344)
    pyautogui.write("1.10 ")
    pyautogui.press("tab")
    pyautogui.click(x=484, y=412)

    #CRIAR O VINCULO COM A PLANILHA
    import pandas as pd


    ####AQUI CODIGO PARA PUCHAR
    pyautogui.write(" REEMBOLSO DIF. AGUA ")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")



    #PAGINA VALOR E UNIDADE


    ####CRIAR LINHA VALOR PLANILHA
    pyautogui.press("-")

    tabela = pd.read_csv("cerejeiras.csv", sep=";")

    for linha in tabela.index:
        
        pagar = tabela.loc[linha_atual, "pagar"]
    pyautogui.write(str(pagar))

    pyautogui.press("tab")

    ##CRIAR LINHA PARA UNIDADE E BLOCO (COLOCAR COMANDO PARA ESPAÇO)

    tabela = pd.read_csv("cerejeiras.csv", sep=";")

    for linha in tabela.index:

        apto = tabela.loc[linha_atual, "apto"]
    pyautogui.write(str(apto))

    pyautogui.press("space")

    tabela = pd.read_csv("cerejeiras.csv", sep=";")

    for linha in tabela.index:

        bloco = tabela.loc[linha_atual, "bloco"]
        bloco_format = '{:02d}'.format(bloco)

    pyautogui.write(str(bloco_format))
    #comando para clicar na unidade

#CLICAR UNIDADE

    pyautogui.click(x=487, y=427)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    linha_atual += 1

