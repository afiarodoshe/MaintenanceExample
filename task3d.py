from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'D:/chromedriver_win32/chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

link = driver.find_element_by_link_text('Software Testing Tutorials').click()

elem = driver.find_element_by_class_name('menu-primary-items')

all_li = elem.find_elements_by_tag_name('li')

print(len(all_li))
def testLink():
    assert(list.size() == 5)
    print('test')

testLink()