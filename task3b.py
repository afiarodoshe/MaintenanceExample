from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'D:/4-2/SWE 4802 (Maintenance Lab)/Lab Final/chromedriver_win32\chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407');


btns=driver.find_elements_by_xpath("//input[@type='radio']")

def checkButton():
    assert (len(btns)==2)
    print('radio', len(btns))

def checkSelected():
    for choice in btns:
        if(choice.is_selected()):
            print('selected')
            return
    print('deselected')


checkButton()
checkSelected()