from selenium.webdriver.common.keys import Keys
import pwinput
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import xlsxwriter
import decimal

def main():
    workbook = xlsxwriter.Workbook("MédiaUnipar.xlsx")
    worksheet = workbook.add_worksheet(name="Médias")
    bold = workbook.add_format({'bold': True})
    worksheet.write("A1", "DISCIPLINA", bold)
    worksheet.write("B1", "NOTA 1° BI", bold)
    worksheet.write("C1", "NOTA 2° BI", bold)
    worksheet.write("D1", "MÉDIA", bold) 
    worksheet.write("E1", "RELAÇÃO", bold)
    cont = 0
    quantidadeDeMaterias = int(input("Digite quantas matérias você tem: "))
    login = input("Digite o seu RA: ")
    senha = pwinput.pwinput(prompt='Digite sua senha: ', mask= '*')
    driver = uc.Chrome()
    driver.get("https://aluno.unipar.br/index.html")
    driver.find_element(By.NAME, "login").send_keys(login)
    driver.find_element(By.NAME, "senha").send_keys(senha, Keys.RETURN)
    driver.find_element(By.XPATH, '//*[@id="curso"]').click()
    driver.find_element(By.XPATH, '//*[@id="curso"]').send_keys(Keys.RETURN)
    driver.get("https://aluno.unipar.br/site/home.php?conteudo=notas&acao=extrato_notas_fun")
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div/div[2]/input').click()
    lista = []
    i = 0
    
    while i<quantidadeDeMaterias:
        disciplina = []
        nome = str(((driver.find_element(By.XPATH, f'//*[@id="extrato_notas"]/tbody/tr[{i+4}]').find_element(By.ID, 'disciplina')).text))
        nota1 = float(driver.find_element(By.XPATH, f'//*[@id="extrato_notas"]/tbody/tr[{i+4}]/td[5]/span').text.replace(',', '.'))
        nota2 = float(driver.find_element(By.XPATH, f'//*[@id="extrato_notas"]/tbody/tr[{i+4}]/td[6]/span').text.replace(',', '.'))
        disciplina.append(nome.lower().title())
        disciplina.append(nota1)
        disciplina.append(nota2)
        media = ((nota1 + nota2)/2)
        disciplina.append(media)
        lista.append(disciplina)
        i+=1       

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
            val = digits[:delta] + ('0'*tup.exponent) + '.' + digits[delta:]
        val = val.rstrip('0')
        if val[-1] == '.':
            val = val[:-1]
        if tup.sign:
            return '-' + val
        return val
    
    def montaXls(nome, n1, n2, media, x):
        worksheet.write(f'A{x+2}', nome)
        worksheet.write(f'B{x+2}', formatar(n1))
        worksheet.write(f'C{x+2}', formatar(n2))
        worksheet.write(f'D{x+2}', formatar(media))
        if n2 > n1:
            return worksheet.write(f'E{x+2}', f'Aumento de {formatar((n2-n1)*10)}%')
        elif n1==n2:
            return worksheet.write(f'E{x+2}', "Notas iguais")
        else:
            return worksheet.write(f'E{x+2}', f'Diminuição de {formatar((n1-n2)*10)}%')   
    
    for disciplina in lista:
        montaXls(disciplina[0], disciplina[1], disciplina[2], disciplina[3], cont)
        cont+=1
    
    workbook.close()
    
if __name__ == '__main__':
    main()