'''
这个模块用来装基础的定义和页面元素的操作
'''''
import unittest
from selenium.webdriver.common.by import By
class  Basepage(unittest.TestCase):
    @classmethod
    def  set_driver(cls,driver):  #设置一个driver
       cls.driver = driver
       # return cls.driver
    @classmethod
    def  get_driver(cls):   #获取一个driver
        return  cls.driver
    @classmethod
    def  find_element(cls,element):  #封装元素定位的方法
            type=element[0]
            value=element[1]
            if type=="id":
                elem=    cls.driver.find_element(By.ID,value)
            elif  type=="name":
                elem=    cls.driver.find_element(By.NAME,value)
            elif  type=="class":
                elem=    cls.driver.find_element(By.CLASS_NAME,value)
            elif  type=="xpath":
                elem=    cls.driver.find_element(By.XPATH,value)
            elif  type=="linktext":
                elem=    cls.driver.find_element(By.LINK_TEXT,value)
            elif type=="css":
                elem=    cls.driver.find_element(By.CSS_SELECTOR,value)
            elif  type=="tag":
                elem=   cls.driver.find_elements(By.TAG_NAME,value)
            else:
                raise  ValueError("please  input correct  parameter")
            return elem

    @classmethod
    def  sendkeys(cls,elem,text):  #封装一个输入内容的方法
        return elem.send_keys(text)
    @classmethod
    def click(cls,elem):  #封装一个点击方法
        return  elem.click()
    @classmethod       #封装一个窗口最大化的方法
    def  max(cls,elem):
        return elem.maximize_window()
    @classmethod    #封装一个获取文本的方法
    def  text(cls,elem):
        return elem.text
    @classmethod
    def  wait(cls,sec):      #封装一个隐式等待的方法
        return cls.driver.implicitly_wait(sec)
    @classmethod
    def  switch_iframe(cls,elem):  #封装一个切换iframe框的方法
        return  cls.driver.switch_to.frame(elem)


if __name__ == '__main__':
    unittest.main()
    # from selenium import webdriver
    # driver=webdriver.Chrome()
    # driver.get("http://www.baidu.com")
    #
    # baidu=("xpath",'//*[@id="kw"]')
    # elem=Basepage.find_element(baidu)   # driver.find_element_by_xpath(value)
    # Basepage.sendkeys(elem,"python")
    # b=Basepage()
    # b.set_driver(driver)
    # b.find_element("id","kw").send_keys("python")












