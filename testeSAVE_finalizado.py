import pyautogui, time, os, pyperclip, sys


confirma =pyautogui.confirm('Tela do saveweb tem que estar aberta\n em SAEOI010')
if confirma == 'OK': 
    caminho = input('INFORME O CAMINHO :')
    data_passada = input('Digite a data menos 3 messes: ')
    data_atual = input('Digite a data atual: ')
    pyperclip.copy(caminho)
    #VERIFICAÇÃO DE TELA
    cordenada1 = None
    cordenada2 = None
    cordenada3 = None
    cordenada3_1 =None
    cordenada4 = None
    cordenada5 = None
    cordenada6 = None
    cordenada7 = None
    cordenada8 =None
    cordenada9 =None
    cordenada9_1 =None
    cordenada10=None
    cordenada11=None
    cordenada12=None
    cordenada13=None
    carregando = None


    while cordenada1 == None:
        cordenada1 = pyautogui.locateCenterOnScreen("Screenshot_1.png")
        pyautogui.click(cordenada1)
        print(cordenada1)
        print('fim1')
    else:
        time.sleep(1)
        while cordenada2 == None:
            cordenada2 = pyautogui.locateCenterOnScreen("Screenshot_2.png")
            pyautogui.click(cordenada2)
            print(cordenada2)
            print('fim2')
        else:
            time.sleep(1)
            pyautogui.write('salvar arquivos')
            
            while cordenada4 == None:
                cordenada4 = pyautogui.locateCenterOnScreen("Screenshot_4.png")
                pyautogui.click(cordenada4)
                print(cordenada4)
                print('fim3')
            else:
                time.sleep(1)
                pyautogui.hotkey('ctrl','v')
                while cordenada5 == None:
                    cordenada5 = pyautogui.locateCenterOnScreen("Screenshot_13.png")
                    pyautogui.click(cordenada5)
                    print(cordenada5)
                    print('fim4')
                else:
                    time.sleep(1)
                    while cordenada6 == None:
                        cordenada6 = pyautogui.locateCenterOnScreen("Screenshot_1_ataca_logo.png")
                        pyautogui.click(cordenada6)
                        print(cordenada6)
                        print('fim5')
                    else:
                        while cordenada9 ==None and cordenada9_1 ==None :
                            cordenada9 = pyautogui.locateCenterOnScreen("Screenshot_12.png")
                            cordenada9_1 = pyautogui.locateCenterOnScreen("Screenshot_12_1.png")
                            pyautogui.click(cordenada9)
                            pyautogui.click(cordenada9_1)
                            pyautogui.write('17906',interval=0.25)
                            print(f'{cordenada9}{cordenada9_1}')
                            print('fim6')
                        else:
                            carregando =  pyautogui.locateCenterOnScreen("Screenshot_1_carregando.png")
                            while carregando != None:
                                carregando =  pyautogui.locateCenterOnScreen("Screenshot_1_carregando.png")
                                print("Carregando informações")
                            else:
                                print("OK")
                                if cordenada9 ==None:
                                    cordenada9 = cordenada9_1
                                  
                                while cordenada7 == None:
                                    cordenada7 = pyautogui.locateCenterOnScreen("Screenshot_8.png")
                                    pyautogui.click(cordenada7)
                                    print(cordenada7)
                                    time.sleep(1)
                                    pyautogui.write(data_passada,interval=0.25)
                                    print('fim7')
                                else:
                                    pyautogui.press('enter')
                                    time.sleep(1)
                                    while cordenada8== None:
                                        cordenada8 = pyautogui.locateCenterOnScreen("Screenshot_9.png")
                                        pyautogui.click(cordenada8)
                                        print(cordenada8)
                                        pyautogui.write(data_atual,interval=0.25)
                                        print('fim8')
                                    else:
                                        time.sleep(1)
                                        pyautogui.press('enter')
                                        while cordenada10== None:
                                            cordenada10 = pyautogui.locateCenterOnScreen("Screenshot_10.png")
                                            pyautogui.click(cordenada10)
                                            print(cordenada10)
                                            print('fim9')
                                        else:
                                            carregando = pyautogui.locateCenterOnScreen("Screenshot_1_carregando.png")
                                            while carregando != None:
                                                carregando =  pyautogui.locateCenterOnScreen("Screenshot_1_carregando.png")
                                                print("Carregando informações")
                                            else:
                                                print("OK")
                                                while cordenada11== None:
                                                    cordenada11 = pyautogui.locateCenterOnScreen("Screenshot_18.png")
                                                    pyautogui.click(cordenada11)
                                                    print(cordenada11)
                                                    print('fim10')
                                                else:
                                                    time.sleep(1)
                                                    while cordenada12== None:
                                                        cordenada12 = pyautogui.locateCenterOnScreen("Screenshot_17.png")
                                                        pyautogui.click(cordenada12)
                                                        print(cordenada12)
                                                    else:
                                                        print('fim12_Da ferificação')
    #FIM DA VERIFICAÇÃO                                      
    print('aqui começa')
    texto = '.txt'
    lista_diretorio = []
    lista_segundaria =[]
    lista_arquivo = []
    lista_conteudo =[]
    conta_diretorio = 0
    conta_arquivo = 0
    conta_um =0
    conta_dois=0
    enquanto =0
    conta_linha =0
    caminho_completo_diretorio = ''
    caminho_dois = ''
    consome_arquivo = ''
    arquivo =[]
    diretorio = ''
    recebe =''
    coisas =''
    judite=''
    juliete =''
    abre_arquivo =''
    while enquanto <= 10:
        try:
            for raiz, diretorios, arquivos in os.walk(caminho):
                if conta_um == conta_dois:
                    for diretorio in diretorios:
                        caminho_completo_diretorio = os.path.join(raiz, diretorio)
                        lista_diretorio.insert(conta_diretorio, caminho_completo_diretorio)
                        print(lista_diretorio[conta_diretorio])
                        conta_diretorio +=1
                    print(lista_diretorio[conta_um])
                    pyperclip.copy(lista_diretorio[conta_um])
                    pyautogui.click(cordenada12)
                    time.sleep(1)
                    pyautogui.click(cordenada4)
                    time.sleep(1)
                    pyautogui.hotkey('ctrl','v')
                    time.sleep(1)
                    pyautogui.click(cordenada5)
                    time.sleep(1)
                    pyautogui.click(cordenada6)
                    conta_um +=1
                elif conta_um != conta_dois:
                    for arquivo in os.walk(lista_diretorio[conta_dois]):
                        for coisas in arquivo:
                            lista_arquivo.insert(conta_arquivo, coisas)
                            #print(recebe)
                            conta_arquivo +=1
                            continue
                        judite=lista_arquivo[2]
                        juliete=judite[0]
                        recebe = open(f'{lista_arquivo[0]}\{juliete}','r+')
                        for abre_arquivo in recebe:
                            lista_conteudo.insert(conta_linha,abre_arquivo)
                            print(lista_conteudo)
                            time.sleep(2)
                            pyautogui.doubleClick(cordenada9)
                            time.sleep(2)
                            pyautogui.write(lista_conteudo[conta_linha],interval=0.25)
                            conta_linha +=1
                            time.sleep(1)
                            pyautogui.click(cordenada10)
                            carregando = pyautogui.locateCenterOnScreen("Screenshot_1_carregando.png")
                            while carregando != None:
                                carregando =  pyautogui.locateCenterOnScreen("Screenshot_1_carregando.png")
                                print("Carregando informações")
                            else:
                                print("OK")
                            pyautogui.click(cordenada9)
                            pyautogui.click(cordenada10)
                            carregando =  pyautogui.locateCenterOnScreen("Screenshot_1_carregando.png")
                            while carregando != None:
                                carregando =  pyautogui.locateCenterOnScreen("Screenshot_1_carregando.png")
                                print("Carregando informações")
                            else:
                                print("OK")
                            pyautogui.click(cordenada11)
                            carregando =  pyautogui.locateCenterOnScreen("Screenshot_1_carregando.png")
                            while carregando != None:
                                carregando =  pyautogui.locateCenterOnScreen("Screenshot_1_carregando.png")
                                print("Carregando informações")
                            else:
                                print("OK")
                            continue
                        conta_dois +=1
                        juliete= ''
                        arquivo=('')
                        del(lista_arquivo[0:3])
                        del(judite[0])
                        lista_conteudo.clear()
                        conta_linha =0
                        conta_diretorio=0
                        time.sleep(2)
                        pyautogui.click(cordenada12)
        except IndexError as erro:
            pyautogui.alert("Fim da execução")
            break
else:
    pyautogui.alert('Abra o save-web e tente novamente')
    sys.exit()
    


