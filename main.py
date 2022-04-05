 
                                    #░░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▄▄
                                    #░░░░░░░░▄▀▀░░░░░░░░░░░░▀▄▄
                                    #░░░░░░▄▀░░░░░░░░░░░░░░░░░░▀▄
                                    #░░░░░▌░░░░░░░░░░░░░▀▄░░░░░░░▀▀▄
                                    #░░░░▌░░░░░░░░░░░░░░░░▀▌░░░░░░░░▌
                                    #░░░▐░░░░░░░░░░░░▒░░░░░▌░░░░░░░░▐
                                    #░░░▌▐░░░░▐░░░░▐▒▒░░░░░▌░░░░░░░░░▌
                                    #░░▐░▌░░░░▌░░▐░▌▒▒▒░░░▐░░░░░▒░▌▐░▐
                                    #░░▐░▌▒░░░▌▄▄▀▀▌▌▒▒░▒░▐▀▌▀▌▄▒░▐▒▌░▌
                                    #░░░▌▌░▒░░▐▀▄▌▌▐▐▒▒▒▒▐▐▐▒▐▒▌▌░▐▒▌▄▐
                                    #░▄▀▄▐▒▒▒░▌▌▄▀▄▐░▌▌▒▐░▌▄▀▄░▐▒░▐▒▌░▀▄
                                    #▀▄▀▒▒▌▒▒▄▀░▌█▐░░▐▐▀░░░▌█▐░▀▄▐▒▌▌░░░▀
                                    #░▀▀▄▄▐▒▀▄▀░▀▄▀░░░░░░░░▀▄▀▄▀▒▌░▐
                                    #░░░░▀▐▀▄▒▀▄░░░░░░░░▐░░░░░░▀▌▐
                                    #░░░░░░▌▒▌▐▒▀░░░░░░░░░░░░░░▐▒▐
                                    #░░░░░░▐░▐▒▌░░░░▄▄▀▀▀▀▄░░░░▌▒▐
                                    #░░░░░░░▌▐▒▐▄░░░▐▒▒▒▒▒▌░░▄▀▒░▐
                                    #░░░░░░▐░░▌▐▐▀▄░░▀▄▄▄▀░▄▀▐▒░░▐
                                    #░░░░░░▌▌░▌▐░▌▒▀▄▄░░░░▄▌▐░▌▒░▐
                                    #░░░░░▐▒▐░▐▐░▌▒▒▒▒▀▀▄▀▌▐░░▌▒░▌
                                    #░░░░░▌▒▒▌▐▒▌▒▒▒▒▒▒▒▒▐▀▄▌░▐▒▒
 #################################### DESENVOLVIDO POR JULIO MELO ##########################################
from selenium import webdriver
import time
import os
###########################################################################################################
global navegador
navegador = webdriver.Chrome() 

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main3(): #ENVIA 3 LINHA
    while True:
        try:
            navegador.find_element_by_css_selector('[alt="New chat"]').click()
            navegador.find_element_by_css_selector("#recaptcha-anchor > div.recaptcha-checkbox-border").click()#Recaptcha

        except:
            pass
        try:
            navegador.find_element_by_css_selector("body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.chatmsgcell > div > textarea").send_keys(chat)
            navegador.find_element_by_css_selector("body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.sendbthcell > div > button").click()
            time.sleep(tempo) 
            navegador.find_element_by_css_selector("body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.disconnectbtncell > div > button").click()
            navegador.find_element_by_css_selector("body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.disconnectbtncell > div > button").click()
        except:
            pass #continue nao reiniciou o loop


def main2(): #ENVIA 1 LINHA
    while True:
        try:
            navegador.find_element_by_css_selector('[alt="New chat"]').click()
            navegador.find_element_by_css_selector("#recaptcha-anchor > div.recaptcha-checkbox-border").click()#Recaptcha

        except:
            pass
        try:
            navegador.find_element_by_css_selector("body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.chatmsgcell > div > textarea").send_keys(chat)
            navegador.find_element_by_css_selector("body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.sendbthcell > div > button").click()
            time.sleep(tempo) # Sleep 2  = 1 Hora de recaptcha
            navegador.find_element_by_css_selector("body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.disconnectbtncell > div > button").click()
            navegador.find_element_by_css_selector("body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.disconnectbtncell > div > button").click()
        except:
            pass #LOOP FALHOU

def main():
    global chat
    global tempo
    #chat = input("Texto para enviar:")
    navegador.get("https://www.omegle.com")
    cls()
    time.sleep(3)
    print("              zkawayz")
    print ("░░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▄▄")
    print ("░░░░░░░░▄▀▀░░░░░░░░░░░░▀▄▄")
    print ("░░░░░░▄▀░░░░░░░░░░░░░░░░░░▀▄")
    print ("░░░░░▌░░░░░░░░░░░░░▀▄░░░░░░░▀▀▄")
    print ("░░░░▌░░░░░░░░░░░░░░░░▀▌░░░░░░░░▌")
    print ("░░░▐░░░░░░░░░░░░▒░░░░░▌░░░░░░░░▐")
    print ("░░░▌▐░░░░▐░░░░▐▒▒░░░░░▌░░░░░░░░░▌")
    print ("░░▐░▌░░░░▌░░▐░▌▒▒▒░░░▐░░░░░▒░▌▐░▐")
    print ("░░▐░▌▒░░░▌▄▄▀▀▌▌▒▒░▒░▐▀▌▀▌▄▒░▐▒▌░▌")
    print ("░░░▌▌░▒░░▐▀▄▌▌▐▐▒▒▒▒▐▐▐▒▐▒▌▌░▐▒▌▄▐")
    print ("░▄▀▄▐▒▒▒░▌▌▄▀▄▐░▌▌▒▐░▌▄▀▄░▐▒░▐▒▌░▀▄")
    print ("▀▄▀▒▒▌▒▒▄▀░▌█▐░░▐▐▀░░░▌█▐░▀▄▐▒▌▌░░░▀")
    print ("░▀▀▄▄▐▒▀▄▀░▀▄▀░░░░░░░░▀▄▀▄▀▒▌░▐")
    print ("░░░░▀▐▀▄▒▀▄░░░░░░░░▐░░░░░░▀▌▐")
    print ("░░░░░░▌▒▌▐▒▀░░░░░░░░░░░░░░▐▒▐")
    print ("░░░░░░▐░▐▒▌░░░░▄▄▀▀▀▀▄░░░░▌▒▐")
    print ("░░░░░░░▌▐▒▐▄░░░▐▒▒▒▒▒▌░░▄▀▒░▐")
    print ("░░░░░░▐░░▌▐▐▀▄░░▀▄▄▄▀░▄▀▐▒░░▐")
    print("░░░░░░▌▌░▌▐░▌▒▀▄▄░░░░▄▌▐░▌▒░▐")
    print("░░░░░▐▒▐░▐▐░▌▒▒▒▒▀▀▄▀▌▐░░▌▒░▌")
    print("░░░░░▌▒▒▌▐▒▌▒▒▒▒▒▒▒▒▐▀▄▌░▐▒▒")
    print("Criado por zkawayz | Juliomelo259")
    print("    Omegle Automation Tool")
    print("Made with selenium and webdriver chorme\n")
    chat = input("Texto para enviar: ")
    tempo = int(input("Digite Agora o Tempo em Segundos entre a troca de sala: [1]Super-Agressivo [2]Agressivo [3] Padrao [4]Semi-Seguro [5]Seguro "))
    print("Aviso, Quanto mais agressivo maior a chance de Re-captcha, Use 5 para melhor uso\n")
    print("BOT INICIADO. !!!!")
    time.sleep(2)
    navegador.find_element_by_css_selector("#textbtn").click() # CLICA NO CHAT POR TEXTO
    time.sleep(1)
    navegador.find_element_by_css_selector("body > div:nth-child(11) > div > p:nth-child(2) > label > input[type=checkbox]").click() #CLICA NO CHECKBOX1 DE GUIDELINES
    time.sleep(1)
    navegador.find_element_by_css_selector("body > div:nth-child(11) > div > p:nth-child(3) > label > input[type=checkbox]").click() # CLICA NO CHECKBOX2 DE GUIDELINES
    time.sleep(1)
    navegador.find_element_by_css_selector("body > div:nth-child(11) > div > p:nth-child(4) > input[type=button]").click() # PROCEDE PARA A CONVERSA EM TEXTO
    main2()


main()
