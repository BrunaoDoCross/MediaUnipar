from selenium.webdriver.common.keys import Keys
import pwinput
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import locale
import xlsxwriter
        
def main():
    locale.setlocale(locale.LC_NUMERIC, "pt_BR")
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
    
    analise1 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[4]/td[5]/span').text.replace(',', '.'))
    analise2 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[4]/td[6]/span').text.replace(',', '.'))
    mediaAnalise = (analise1+analise2)/2

    estatistica1 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[5]/td[5]/span').text.replace(',', '.'))
    estatistica2 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[5]/td[6]/span').text.replace(',', '.'))
    mediaEstatistica = (estatistica1 + estatistica2)/2
    
    estrutura1 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[6]/td[5]/span').text.replace(',', '.'))
    estrutura2 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[6]/td[6]/span').text.replace(',', '.'))
    mediaEstrutura = (estrutura1 + estrutura2)/2
    
    filosofia1 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[7]/td[5]/span').text.replace(',', '.'))
    filosofia2 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[7]/td[6]/span').text.replace(',', '.'))
    mediaFilosofia = (filosofia1+filosofia2)/2
    
    marketing1 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[8]/td[5]/span').text.replace(',', '.'))
    marketing2 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[8]/td[6]/span').text.replace(',', '.'))
    mediaMarketing = (marketing1+marketing2)/2
    
    programacao1 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[9]/td[5]/span').text.replace(',', '.'))
    programacao2 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[9]/td[6]/span').text.replace(',', '.'))
    mediaProgramacao = (programacao1+programacao2)/2
    
    redes1 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[10]/td[5]/span').text.replace(',', '.'))
    redes2 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[10]/td[6]/span').text.replace(',', '.'))
    mediaRedes = (redes1+redes2)/2
    
    tic1 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[11]/td[5]/span').text.replace(',', '.'))
    tic2 = float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[11]/td[6]/span').text.replace(',', '.'))
    mediaTic = (tic1+tic2)/2
    
    workbook = xlsxwriter.Workbook("MédiaUnipar.xlsx")
    worksheet = workbook.add_worksheet(name="Médias")
    bold = workbook.add_format({'bold': True})
    worksheet.write("A1", "DISCIPLINA", bold)
    worksheet.write("B1", "NOTA 1° BI", bold)
    worksheet.write("C1", "NOTA 2° BI", bold)
    worksheet.write("D1", "MÉDIA", bold) 
    worksheet.write("E1", "RELAÇÃO", bold)
    
    
    worksheet.write("D2", mediaAnalise)
    worksheet.write("A2", "Análise e Projeto de Sistemas")
    worksheet.write("B2", analise1)
    worksheet.write("C2", analise2)
    if analise2 > analise1:
        worksheet.write("E2", f'Aumento de {((analise2-analise1)*10):.2f}%')
    elif analise1==analise2:
        worksheet.write("E2", "Notas iguais")
    else:
        worksheet.write("E2", f'Diminuição de {((analise1-analise2)*10):.2f}%')
        
    worksheet.write("D3", mediaEstatistica) 
    worksheet.write("A3", "Estatística")
    worksheet.write("B3", estatistica1)
    worksheet.write("C3", estatistica2)
    if estatistica2 > estatistica1:
        worksheet.write("E3", f'Aumento de {((estatistica2-estatistica1)*10):.2f}%')
    elif estatistica1==estatistica2:
        worksheet.write("E3", "Notas iguais")
    else:
        worksheet.write("E3", f'Diminuição de {((estatistica1-estatistica2)*10):.2f}%')
    
    
    worksheet.write("D4", mediaEstrutura) 
    worksheet.write("A4", "Estrutura e Classificação de Dados")
    worksheet.write("B4", estrutura1)
    worksheet.write("C4", estrutura2)
    if estrutura2 > estrutura1:
        worksheet.write("E4", f'Aumento de {((estrutura2-estrutura1)*10):.2f}%')
    elif estrutura1==estrutura2:
        worksheet.write("E4", "Notas iguais")
    else:
        worksheet.write("E4", f'Diminuição de {((estrutura1-estrutura2)*10):.2f}%')
    
    
    worksheet.write("D5", mediaFilosofia) 
    worksheet.write("A5", "Filosofia e Ética")
    worksheet.write("B5", filosofia1)
    worksheet.write("C5", filosofia2)
    if filosofia2 > filosofia1:
        worksheet.write("E5", f'Aumento de {((filosofia2-filosofia1)*10):.2f}%')
    elif filosofia1==filosofia2:
        worksheet.write("E5", "Notas iguais")
    else:
        worksheet.write("E5", f'Diminuição de {((filosofia1-filosofia2)*10):.2f}%')
    
    
    worksheet.write("D6", mediaMarketing) 
    worksheet.write("A6", "Fundamentos de Marketing")
    worksheet.write("B6", marketing1)
    worksheet.write("C6", marketing2)
    if marketing2 > marketing1:
        worksheet.write("E6", f'Aumento de {((marketing2-marketing1)*10):.2f}%')
    elif marketing1==marketing2:
        worksheet.write("E6", "Notas iguais")
    else:
        worksheet.write("E6", f'Diminuição de {((marketing1-marketing2)*10):.2f}%')
    
    
    worksheet.write("D7", mediaProgramacao) 
    worksheet.write("A7", "Programação Orientada a Objetos")
    worksheet.write("B7", programacao1)
    worksheet.write("C7", programacao2)
    if programacao2 > programacao1:
        worksheet.write("E7", f'Aumento de {((programacao2-programacao1)*10):.2f}%')
    elif programacao1==programacao2:
        worksheet.write("E7", "Notas iguais")
    else:
        worksheet.write("E7", f'Diminuição de {((programacao1-programacao2)*10):.2f}%')
    
    
    worksheet.write("D8", mediaRedes) 
    worksheet.write("A8", "Redes de Computadores e Segurança")
    worksheet.write("B8", programacao1)
    worksheet.write("C8", programacao2)
    if redes2 > redes1:
        worksheet.write("E8", f'Aumento de {((redes2-redes1)*10):.2f}%')
    elif redes1==redes2:
        worksheet.write("E8", "Notas iguais")
    else:
        worksheet.write("E8", f'Diminuição de {((redes1-redes2)*10):.2f}%')
    
    
    worksheet.write("D9", mediaTic) 
    worksheet.write("A9", "Tecnologia da Informação e Comunicação")
    worksheet.write("B9", tic1)
    worksheet.write("C9", tic2)
    if tic2 > tic1:
        worksheet.write("E9", f'Aumento de {((tic2-tic1)*10):.2f}%')
    elif tic1==tic2:
        worksheet.write("E9", "Notas iguais")
    else:
        worksheet.write("E9", f'Diminuição de {((tic1-tic2)*10):.2f}%')
    
    
    workbook.close()
        
    
if __name__ == '__main__':
    main()