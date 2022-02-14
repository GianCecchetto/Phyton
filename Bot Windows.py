import pyautogui

pyautogui.PAUSE = 2
#Abrir ferramenta / o sistema/ o programa
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")

#preencher o login
pyautogui.click(x=472, y=267)
pyautogui.write("Enter name")

#preencher a senha
pyautogui.click(x=460, y=323)
pyautogui.write("Enter Password")

#clicar em fazer login
pyautogui.click(x=645, y=425)