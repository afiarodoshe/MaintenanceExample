from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'D:/4-2/SWE 4802 (Maintenance Lab)/Lab Final/chromedriver_win32\chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407');

first_name=driver.find_element_by_name('RESULT_TextField-1')


last_name = driver.find_element_by_name('RESULT_TextField-2')


def maxLength():
    firstname = "x" * 255
    lastname = "y" * 255
    first_name.send_keys(firstname)
    last_name.send_keys(lastname)

maxLength()