from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os

chromedriver_path = r"C:\Users\chalh\Documents\chrome_driver\chromedriver-win32\chromedriver.exe"

# Configuration du service Selenium
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Liste des URLs à scraper
urls = [
    "https://www.nature.com/articles/d41586-020-00502-w",
    "https://www.nejm.org/doi/full/10.1056/NEJMoa2033700?query-featured_coronavirus=",
    "https://www.nejm.org/doi/full/10.1056/NEJMoa2030340?query=featured_coronavirus",
    "https://www.nejm.org/doi/full/10.1056/NEJMoa2035002?query-featured_coronavirus=",
    "https://www.nejm.org/doi/full/10.1056/NEJMoa2029849?query=featured_coronavirus",
    "https://www.nejm.org/doi/full/10.1056/NEJMpv2035416?query=featured_coronavirus",
    "https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(21)00007-2/fulltext",
    "https://www.thelancet.com/journals/lanres/article/PIIS2213-2600(21)00025-4/fulltext",
    "https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)32656-8/fulltext",
    "https://science.sciencemag.org/content/early/2021/01/11/science.abe6522"
]

#  un dossier pour les corpus_covid19
if not os.path.exists('corpus_covid19'):
    os.makedirs('corpus_covid19')


for i, url in enumerate(urls, start=1):
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Accepter les cookies
    try:
        cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Accepter")]'))
        )
        cookies_button.click()
    except:
        print("Pas de bouton de cookies trouvé ou le bouton n'est pas cliquable.")

    # Cocher la case d'humain
    try:
        human_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'human-checkbox'))
        )
        human_checkbox.click()
    except:
        print("Pas de case d'humain trouvée ou la case n'est pas cliquable.")

    # Extrait le contenu de la page
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extrait le texte de l'article, sans les légendes des images
    text = ' '.join([p.text for p in soup.find_all('p') if p.parent.name != 'figcaption'])

    # Sauvegarde dans un fichier txt
    file_path = f'corpus_covid19/document_{i}.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f'Document {i} saved in {file_path}.')


driver.quit()
print("All corpus_covid19 saved.")
