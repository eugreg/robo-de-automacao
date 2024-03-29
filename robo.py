import pyautogui
import pandas
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv("produtos.csv")

#tempo de pausa
pyautogui.PAUSE = 0.5

#entrar no GOOGLE CHROMEMOLO000251  Logitech    Mouse   1   25.95   6.5
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no link
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)

#login
pyautogui.press("tab")
pyautogui.write("greg@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

#salvar dados
for linhas in tabela.index:
    #salavar codigo
    pyautogui.click(x=1151, y=254)
    pyautogui.write(tabela.loc[linhas, "codigo"])

    #salvar marca

    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linhas, "marca"])

    #salvar tipo

    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linhas, "tipo"])

    #salvar categoria

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linhas, "categoria"]))

    #salvar preco
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linhas, "preco_unitario"]))

    #salvar custo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linhas, "custo"]))

    #salvar onbs
    pyautogui.press("tab")
    obs = tabela.loc[linhas, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    

    #salvar
    pyautogui.press("tab")  
    pyautogui.press("enter")

    #scroll 

    pyautogui.scroll(1000)