import pyautogui
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv("produtos.csv")

#tempo de pausa
pyautogui.PAUSE = 1

#entrar no GOOGLE CHROME
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no link
pyautogui.write(link)
pyautogui.press("enter")
set.time(5)

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
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linhas, "codigo"])

    #salvar marca

    pyautogui.press("tab")
    pyautogui.write("marca")

    #salvar tipo

    pyautogui.press("tab")
    pyautogui.write("tipo")

    #salvar categoria

    pyautogui.press("tab")
    pyautogui.write("categoria")

    #salvar preco
    pyautogui.press("tab")
    pyautogui.write("preco_unitario")

    #salvar custo
    pyautogui.press("tab")
    pyautogui.write("custo")

    #salvar onbs
    pyautogui.press("tab")
    pyautogui.write("observacoes")

    #salvar
    pyautogui.press("tab")  
    pyautogui.press("enter")

    #scroll 

    pyautogui.scroll(1000)