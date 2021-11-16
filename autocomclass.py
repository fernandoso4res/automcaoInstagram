from PySimpleGUI import PySimpleGUI as sg
from selenium import webdriver
import time
# Abre o navegador
# interface das informções
#layout
sg.theme('Reddit')
layout = [
        [sg.Text('Usuário'), sg.Input(key='usuario')],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
        [sg.Button('Entrar')]]
        
#janela
janela = sg.Window('Login a ser inserido no Instagram', layout)
    #Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        username = valores['usuario']
        senha = valores['senha']
        navegador = webdriver.Chrome("chromedriver.exe")
        navegador.get('https://www.instagram.com/')
        time.sleep(2)
               

        #Fazer login
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        time.sleep(2)
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(3)
        #Clica no agora não
        navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)
        navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        time.sleep(3)
        #CLICA PARA VER OS STORIES
        navegador.find_element_by_class_name('OE3OK ').click()
       