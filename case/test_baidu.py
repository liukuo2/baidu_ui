from selenium import webdriver
import unittest
from unittest import TestCase
from time import sleep
from public.pages.basepage import Basepage
class Baidu(Basepage):
    @classmethod
    def setUpClass(cls) -> None:
        sleep(0.7)
        driver = webdriver.Chrome()
        Basepage.set_driver(driver)
        sleep(0.7)
        Basepage.max(driver)
    def test1_open_web(self):
        driver=Basepage.get_driver()
        sleep(1.5)
        driver.get("https://console.bce.baidu.com/znzs/#/znzs/robot-chat")
        sleep(1)
        #选择点击登录方式（账号登录）
    def test2_login_method(self):
        login_method = ("xpath",'//*[@id="TANGRAM__PSP_4__qrcode"]/p[2]/span')
        elem1=Basepage.find_element(login_method)
        Basepage.click(elem1)
        # 输入账号
    def test3_login_account(self):
        sleep(0.8)
        login_account = ("name","userName")
        elem2=Basepage.find_element(login_account)
        Basepage.sendkeys(elem2,"acg_cts_qa")
        #输入密码
    def test4_login_password(self):
        sleep(0.8)
        login_password=("name","password")
        elem3=Basepage.find_element(login_password)
        Basepage.sendkeys(elem3,"d4faDa3opd")
        # 点击登录
    def test5_login_submit(self):
        sleep(0.8)
        login_submit=("id","TANGRAM__PSP_4__submit")
        elem4=Basepage.find_element(login_submit)
        Basepage.click(elem4)
    @classmethod
    def tearDownClass(cls) -> None:
        sleep(1)

        #点击输入内容
    def test6_input_text(self):
        sleep(4)
        input_text = ("id","textarea")
        elem5=Basepage.find_element(input_text)
        Basepage.sendkeys(elem5,"测试")
        # 点击发送
    def test7_send_text(self):
        sleep(1.5)
        send_text = ("xpath",'//span[@class="label chat-send"]')
        elem6 = Basepage.find_element(send_text)
        Basepage.click(elem6)
    def test8_assert_text(self):
        sleep(4)
        assert_text1 = ("class","time-msg")
        elem7=Basepage.find_element(assert_text1)
        a = Basepage.text(elem7)
        print(a)
        if "智能助手" in a:
           print("执行成功")


if __name__ == '__main__':
    unittest.main()

