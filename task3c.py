from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'D:/chromedriver_win32/chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407');


btns=driver.find_elements_by_xpath("//input[@type='checkbox']")

def checkDaySelector():
    assert (len(btns)==7)
    print('selected', len(btns))

def checkboxSelected():
    for choice in btns:
        if(choice.is_selected()):
            print('selected')
            return
    print('deselected')

checkDaySelector()
checkboxSelected()