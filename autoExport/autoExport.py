from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


DOMAIN = 'YOUR DOMAIN HERE' # with / included
PATH = 'YOUR WEBDRIVER PATH HERE'
numberOfEmptyRecipesBeforQuit = 10
username = 'YOUR USERNAME HERE'
password = 'YOUR PASSWORD HERE'



driver = webdriver.Chrome(PATH)
driver.get(DOMAIN + 'accounts/login/')

usernameBox = driver.find_element_by_id('id_username').send_keys(username)
passwordBox = driver.find_element_by_id('id_password').send_keys(password)
loginButton = driver.find_element_by_class_name('btn.btn-primary').click()

run = True
currentRecipe = 1
currentURL = DOMAIN + 'export/?r='
emptyRecipesInARow = 0
wait = WebDriverWait(driver, 10)

while (run==True):
    currentURL = DOMAIN + 'export/?r=' + str(currentRecipe)
    driver.get(currentURL)

    if emptyRecipesInARow > numberOfEmptyRecipesBeforQuit:
        driver.quit()
    else:
        if driver.find_element_by_id('select2-id_recipe-container').get_attribute('title') == '---------':
            print('EMPTY RECIPE, #' + str(currentRecipe))
            emptyRecipesInARow  = emptyRecipesInARow + 1
            currentRecipe = currentRecipe + 1
        else:
            imageButton = wait.until(EC.element_to_be_clickable((By.ID, 'id_image'))).click()
            imageButton = wait.until(EC.element_to_be_clickable((By.ID, 'id_download'))).click()

            exportFinalButton = driver.find_element_by_class_name('btn.btn-success').click()

            currentRecipe = currentRecipe + 1
            emptyRecipesInARow = 0

            print('FOUND RECIPE, #' + str(currentRecipe))
