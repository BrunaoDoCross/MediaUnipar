from selenium.webdriver.common.keys import Keys
import pwinput
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
import locale



def mainn():
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
    
    mediaAnalise = (float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[4]/td[5]/span').text.replace(',', '.'))
    + float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[4]/td[6]/span').text.replace(',', '.'))) / 2
    print(mediaAnalise)

    mediaEstatistica = (float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[5]/td[5]/span').text.replace(',', '.'))
    + float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[5]/td[6]/span').text.replace(',', '.'))) / 2
    print(mediaEstatistica)
    
    mediaEstrutura = (float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[6]/td[5]/span').text.replace(',', '.'))
    + float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[6]/td[6]/span').text.replace(',', '.'))) / 2
    print(mediaEstrutura)

    mediaFilosofia = (float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[7]/td[5]/span').text.replace(',', '.'))
    + float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[7]/td[6]/span').text.replace(',', '.'))) / 2
    print(mediaFilosofia)
    
    mediaMarketing = (float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[8]/td[5]/span').text.replace(',', '.'))
    + float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[8]/td[6]/span').text.replace(',', '.'))) / 2
    print(mediaMarketing)
    
    mediaProgramacao = (float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[9]/td[5]/span').text.replace(',', '.'))
    + float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[9]/td[6]/span').text.replace(',', '.'))) / 2
    print(mediaProgramacao)
    
    mediaRedes = (float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[10]/td[5]/span').text.replace(',', '.'))
    + float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[10]/td[6]/span').text.replace(',', '.'))) / 2
    print(mediaRedes)
    
    mediaTic = (float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[11]/td[5]/span').text.replace(',', '.'))
    + float(driver.find_element(By.XPATH, '//*[@id="extrato_notas"]/tbody/tr[11]/td[6]/span').text.replace(',', '.'))) / 2
    print(mediaTic)

        
def main():
    mainn()
if __name__ == '__main__':
    main()
    time.sleep(1000)