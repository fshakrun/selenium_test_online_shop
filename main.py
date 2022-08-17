import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# здесь, в (), указывается путь к chromedriver.exe
driver = webdriver.Chrome()

# переход на главную страницу
driver.get('https://henderson.ru/')
driver.maximize_window()
time.sleep(3)

# переход на страницу входа в личный кабинет
click_login_button = driver.find_element(By.XPATH,"//*[@href='/hlogin/']").click()
time.sleep(4)

# ввод корректного логина
user_name = driver.find_element(By.XPATH, "//*[@name='email']")
user_name.send_keys("virleo777@gmail.com")
time.sleep(3)

# ввод корректного пароля
user_pass = driver.find_element(By.XPATH, "//*[@name='password']")
user_pass.send_keys("virleo777")
time.sleep(2)

# вход с помощью нажатия клавиши enter
user_pass.send_keys(u'\ue007')
time.sleep(10)

# поиск товара
search_item = driver.find_element(By.XPATH, "//*[@class='js-autocomplite']")
search_item.send_keys("носки")
search_item.send_keys(u'\ue007')
time.sleep(5)

# скролл страницы
driver.execute_script("window.scrollTo(0, 200)")

# скриншот выдачи
driver.save_screenshot('выдача.png')
time.sleep(5)

# проверка релевантности выдачи запросу
item_text = driver.find_element(By.XPATH, "//*[@class='card-product__name-link']")
value_item_text = item_text.text
search_item_results = value_item_text.split(" ")
for el in search_item_results:
    if search_item_results[0] == "Носки":
        continue
    else:
        print("Выдача не релевантна запросу")
        break

# переход на карточку товара
card_product_click = driver.find_element(By.XPATH,"//*[@class='card-product__wrap-img']").click()
time.sleep(5)

# выбор размера
size_choising = driver.find_element(By.XPATH, "//*[@class='wrap-btns__item pp_add_basket']").click()
time.sleep(3)

# добавление в корзину
add_to_basket = driver.find_element(By.XPATH, "//*[@class='select2-results__option select2-results__option--highlighted']").click()
time.sleep(7)

# скриншот того что товар добавлен
driver.save_screenshot('товар в корзине.png')
time.sleep(6)

# обновляем страницу
driver.refresh()
time.sleep(5)

# переход в корзину
driver.get('https://henderson.ru/cart/')
driver.maximize_window()
time.sleep(7)

# скриншот корзины
driver.save_screenshot('скрин корзины.png')
time.sleep(5)

# закрытие браузера
driver.quit()

