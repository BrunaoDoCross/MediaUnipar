from PySimpleGUI import PySimpleGUI as sg
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import xlsxwriter
import decimal
from termcolor import colored

def all():
    print("\x1b[2J\x1b[1;1H")
    print(colored("\nLendo os dados do usuário...", "white", attrs=['bold']))
    def unipar(login, senha):
        print(colored("\nDeixando Aplicação invisível...",
            "white", attrs=['bold']))
        # Deixa a aplicação invisível
        options = webdriver.ChromeOptions()
        options.headless = False
        driver = uc.Chrome(options)
        print(colored("Feito...", "green", attrs=['bold']))

        print(colored("\nCriando xlsx...", "white", attrs=['bold']))
        # Cria arquivo xlsx com as linhas e colunas
        workbook = xlsxwriter.Workbook("MédiaUnipar.xlsx")
        worksheet = workbook.add_worksheet(name="Médias")
        bold = workbook.add_format({'bold': True})
        worksheet.write("A1", "DISCIPLINA", bold)
        worksheet.write("B1", "NOTA 1° BI", bold)
        worksheet.write("C1", "NOTA 2° BI", bold)
        worksheet.write("D1", "MÉDIA", bold)
        worksheet.write("E1", "RELAÇÃO", bold)
        print(colored("Feito...", "green", attrs=['bold']))
        cont = 0

        # Entra com login e senha e entra na aba de notas
        print(colored("\nEntrando no site da unipar...", "white", attrs=['bold']))
        driver.get("https://aluno.unipar.br/index.html")
        print(colored("Feito...", "green", attrs=['bold']))
        print(colored("\nFazendo login...", "white", attrs=['bold']))
        driver.find_element(By.NAME, "login").send_keys(login)
        driver.find_element(By.NAME, "senha").send_keys(senha, Keys.RETURN)
        print(colored("Feito...", "green", attrs=['bold']))
        print(colored("\nNavegando até a aba de notas...", "white", attrs=['bold']))
        driver.find_element(By.XPATH, '//*[@id="curso"]').click()
        driver.find_element(By.XPATH, '//*[@id="curso"]').send_keys(Keys.RETURN)
        driver.get("https://aluno.unipar.br/site/home.php?conteudo=notas&acao=extrato_notas_fun")
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div/div[2]/input').click()
        print(colored("Feito...", "green", attrs=['bold']))
        # Lê todas as notas e disciplinas, calcula a média entre elas e armazena em uma lista
        lista = []
        i = 0

        print(colored(f"Lendo disciplinas e fazendo calculos...","white", attrs=['bold']))
        while i < 8:
            disciplina = []
            nome = str(((driver.find_element(
                By.XPATH, f'//*[@id="extrato_notas"]/tbody/tr[{i+4}]').find_element(By.ID, 'disciplina')).text))
            nota1 = float(driver.find_element(
                By.XPATH, f'//*[@id="extrato_notas"]/tbody/tr[{i+4}]/td[5]/span').text.replace(',', '.'))
            nota2 = float(driver.find_element(
                By.XPATH, f'//*[@id="extrato_notas"]/tbody/tr[{i+4}]/td[6]/span').text.replace(',', '.'))
            disciplina.append(nome.lower().title())
            disciplina.append(nota1)
            disciplina.append(nota2)
            media = ((nota1 + nota2)/2)
            disciplina.append(media)
            lista.append(disciplina)
            print(colored(f"Disciplina {i+1} Lida!", "green", attrs=['bold']))
            i += 1

        # Função para eliminar os algarismos '0' inúteis dos números
        def formatar(num):
            try:
                dec = decimal.Decimal(num)
            except:
                return 'bad'
            tup = dec.as_tuple()
            delta = len(tup.digits) + tup.exponent
            digits = ''.join(str(d) for d in tup.digits)
            if delta <= 0:
                zeros = abs(tup.exponent) - len(tup.digits)
                val = '0.' + ('0'*zeros) + digits
            else:
                val = digits[:delta] + \
                    ('0'*tup.exponent) + '.' + digits[delta:]
            val = val.rstrip('0')
            if val[-1] == '.':
                val = val[:-1]
            if tup.sign:
                return '-' + val
            return val

        # Função que completa o arquivo xlsx com notas utilizando um loop e mostra a porcentagem de aumento de uma nota em relação a outra com um if
        def montaXls(nome, n1, n2, media, x):
            worksheet.write(f'A{x+2}', nome)
            worksheet.write(f'B{x+2}', formatar(n1))
            worksheet.write(f'C{x+2}', formatar(n2))
            worksheet.write(f'D{x+2}', formatar(media))
            if n2 > n1:
                return worksheet.write(f'E{x+2}', f'Aumento de {formatar((n2-n1)*10)}%')
            elif n1 == n2:
                return worksheet.write(f'E{x+2}', "Notas iguais")
            else:
                return worksheet.write(f'E{x+2}', f'Diminuição de {formatar((n1-n2)*10)}%')

        # Chama a função de montar o xlsx para cada disciplina na presente na lista
        print(colored("\nAdicionando as disciplinas lidas no arquivo xlsx",
            "white", attrs=['bold']))
        for disciplina in lista:
            montaXls(disciplina[0], disciplina[1], disciplina[2], disciplina[3], cont)
            print(colored(f"Disciplina {cont+1} adicionada!", "green", attrs=['bold']))
            cont += 1

        # Fecha o xlwx e o Chrome Driver
        workbook.close()
        driver.quit()
        print(colored("\n\nPrograma concluido!!!", color='green', attrs=['bold', 'underline']))

    # Layout
    sg.theme('Reddit')
    layout = [
        [sg.Text('RA'), sg.Input(key='login')],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
        [sg.Button('Confirmar')],
    ]

    # Janela
    janela = sg.Window('Tela de Cadastro', layout)

    # Ler elementos na tela
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Confirmar':
            login = valores['login']
            senha = valores['senha']
            janela.close()
            print(colored("Feito...", "green", attrs=['bold']))
            unipar(login, senha)
            break
        
    janela.close()
    

if __name__ == '__main__':
    all()
