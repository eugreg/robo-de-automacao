import pyautogui
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#tempo de pausa
pyautogui.PAUSE = 0.5

#entrar no GOOGLE CHROME
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no link
pyautogui.write(link)
pyautogui.press("enter")

#login