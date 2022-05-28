from selenium import webdriver #инициализируем Селениум
from selenium.webdriver.common.keys import Keys #инициализируем ключи Селениума

driver = webdriver.Chrome('/home/azamat/Загрузки/chromedriver') #путь к Вебдрайверу

driver.get('https://www.ozon.ru/') #ссылка на проверяемый сайт

searchbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/header/div[1]/div[3]/div/form/div[2]/input[1]') #идентификатор элемента (строка поиска)
searchbox.click()
searchbox.send_keys('Nike') #вводимое значение

searchbox.send_keys(Keys.ENTER) #нажатие Enter