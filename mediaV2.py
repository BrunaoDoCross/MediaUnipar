from selenium.webdriver.common.keys import Keys
import pwinput
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
        
def main():
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
        lista.append(disciplina)
        i+=1
        
    print(lista)
              
if __name__ == '__main__':
    main()