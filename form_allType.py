import unittest
from form_setting import driver
from form_setting import email_test_data
from form_setting import email_invalid_data
from form_setting import formSetUp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pdb
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import random
import form_SCQ
import form_MCQ
from form_function import FormFunc
from form_setting import log


# from form_SCQ import ScqForm
# from form_MCQ import McqForm



class AllType(FormFunc) :

    # def setUp(self) :
    #     driver.maximize_window()
    #     driver.get('http://o3-webform-test.zaya.in/workflow/6d72f66a-1521-4a20-992a-564c529f9659/6f5398f2-db88-4c1c-b2b4-35052e54d430/')

    #     email_test_data = '/home/alqama/workspace/autotest-englishduniya/webform/email_test_data.csv'
    #     email_invalid_data = '/home/alqama/workspace/autotest-englishduniya/webform/email_invalid_data.csv'

    @unittest.skip('check_if_text_present_in_Learn_More')
    def test_01_check_if_text_present_in_Learn_More(self) :

        self.select_continue_button()

        try :
            Learn_More_list = WebDriverWait(driver , 10).until(EC.visibility_of_all_elements_located((By.XPATH , "//button[contains(text(),'Learn more')]")))

            for count , i in enumerate(Learn_More_list) :
                
                sleep(1)
                ActionChains(driver).move_to_element(i).click(i).perform()            
                sleep(1)
                learn_more_text = WebDriverWait(driver , 10).until(EC.visibility_of_element_located((By.CLASS_NAME , 'help-container')))
                
                print(count , 'Text present in Learn more container:{} '.format(learn_more_text.text))

        except TimeoutException :

            print('Learn More is not present in this question')


    @unittest.skip('check_if_user_can_close_Learn_More') 
    def test_02_check_if_user_can_close_Learn_More(self) :

        try :
            Learn_More_list = WebDriverWait(driver , 10).until(EC.visibility_of_all_elements_located((By.XPATH , "//button[contains(text(),'Learn more')]")))

            for i in Learn_More_list:
                
                sleep(1)
                ActionChains(driver).move_to_element(i).click(i).perform()

                close = WebDriverWait(driver , 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR , '.anticon.anticon-cross')))
                close_presence = close.is_displayed()
                print('Close button is present : {}'.format(close_presence))
                
                if (close_presence == True) :

                    close.click()

                else :
                    print('Close button not present')


        except TimeoutException :

            print('Learn More is not present in this question')

    @unittest.skip('test_check_media_presence')
    def test_check_media_presence(self) :
        
        self.select_continue_button()
       

        self.select_radio_button(2)
        self.select_continue_button()

        img_list = WebDriverWait(driver , 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.content-image-wrapper > img')))
        print(len(img_list))

        for count , i in enumerate(img_list) :
                
            sleep(1)
            ActionChains(driver).move_to_element(i).click(i).perform() 
            img_modal  = WebDriverWait(driver , 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rz-bg')))
            ActionChains(driver).move_to_element(img_modal).click(i).perform()       
            sleep(1)

        # video_list = WebDriverWait(driver , 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.content-video-wrapper > div.content-video > video')))
        # print(len(video_list))

    def test_valid_email_data(self) :

        pdb.set_trace()

        self.select_continue_button()
        self.select_continue_button()
        self.select_radio_button(5)
        self.select_continue_test_email_data()
                            

    @unittest.skip('check_type')
    def test_01_check_type(self) :            
        
        while(self.check_continue_button_presence()) :

            pdb.set_trace()

            if driver.find_elements_by_class_name('control-mcq'):
                # j = self.checkbox_inner_list()
                # self.select_checkbox(random.randint(2 , len(j)))
                # self.select_continue_button()
                # sleep(1)
                # pdb.set_trace()
                suite = unittest.TestSuite()
                suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(form_MCQ.McqForm))
                
                unittest.TextTestRunner().run(suite)
                sleep(1)
                self.select_continue_enter_email_if_present()
                sleep(1)
                

            elif driver.find_elements_by_class_name('control-scq') :

                # j = self.radio_buttons_inner_list()        
                # self.select_radio_button(random.randint(2 , len(j)))
                # self.select_continue_button()
                
                suite = unittest.TestSuite()

                suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(form_SCQ.ScqForm))
                unittest.TextTestRunner().run(suite)
                sleep(1)
                self.select_continue_enter_email_if_present()
                # pdb.set_trace()
                sleep(1)


    # def test_email_functionality(self) :

    #     self.start()
    #     pdb.set_trace()

    #     email_back = WebDriverWait(driver , 5).until(EC.presence_of_element_located((By.CLASS_NAME , 'ant-modal-footer')))
    #     email_back.click()

        # field = driver.find_element_by_css_selector('body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div.ant-form-item-control-wrapper > div > input')
                
        # field.send_keys('text')






       

        # sleep(4)
        # slider = driver.find_element_by_class_name('ant-slider-step')
        # slider_size = slider.size
        # x = slider.value_of_css_property('width')
        # print(x)


        # ActionChains(driver).click_and_hold(slider).move_by_offset(50 , 0).release().perform()
            



# ant-slider ant-slider-with-marks

if __name__ == '__main__':
    unittest.main()

