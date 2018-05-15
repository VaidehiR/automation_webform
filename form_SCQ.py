import unittest
from form_setting import driver
from form_setting import formSetUp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pdb
from form_function import FormFunc
from form_setting import log
from selenium.webdriver.common.keys import Keys


class ScqForm(FormFunc):
    # pdb.set_trace()

    def test_01_check_hover_state_on_continue_button(self):            
        # pdb.set_trace()
        # driver.find_element_by_tag_name('body').send_keys(Keys.F5)
        self.check_hover_on_continue_button()
        

    def test_02_check_hover_state_on_back_button(self):            

        self.check_hover_on_back_button()

    
    # @unittest.skip('check_hover_state_on_radio')
    def test_03_check_hover_state_on_radio(self):            

        for j in range(1, len(self.radio_buttons_list()) + 1):
            self.check_radio_button_hover(j)    

    # @unittest.skip('check_radio_button_selection_color')
    def test_04_check_radio_button_selection_color(self):
        
        for j in range(1, len(self.radio_buttons_list()) + 1):

            self.select_radio_button(j)
            self.check_radio_selection_color(j)       

    # @unittest.skip('check_radio_button_selection_after_clicking_twice')
    def test_05_check_radio_button_selection_after_clicking_twice(self):

        for j in range(1, len(self.radio_buttons_inner_list()) + 1):

            ActionChains(driver).double_click(self.radio_button(j)).perform()

            log.info('Clicked twice on radio button {}'.format(j))
            self.assertEqual(self.check_radio_button_selection(j), True)

            self.check_continue_button_enabled()

    # @unittest.skip('check_radio_selection_after_another_radio_selection')
    def test_06_check_radio_selection_after_another_radio_selection(self):

        for j in range(1, len(self.radio_buttons_list()) + 1) :
            
            self.select_radio_button(j)
            for i in range(1, len(self.radio_buttons_list()) + 1) :
                if (i != j) :
                    self.assertEqual(self.check_radio_button_selection(i), False)
                else :

                    self.assertEqual(self.check_radio_button_selection(i), True)


    # @unittest.skip('check_continue_state_after_radio_selected')
    def test_07_check_continue_state_after_radio_selected(self):

        for j in range(1, len(self.radio_buttons_list()) + 1) :

            self.select_radio_button(j)
            self.check_continue_button_enabled()

    # @unittest.skip('check_answer_selection_retains_on_Back')
    def test_08_check_answer_selection_retains_on_Back(self):

        for j in range(1, len(self.radio_buttons_list()) + 1) :

            self.select_radio_button(j)
            self.select_back_button()
            self.select_continue_button_check_popup()
            self.assertEqual(self.check_radio_button_selection(j), True)

    # @unittest.skip('check_answer_selection_retains_on_Continue')
    def test_09_check_answer_selection_retains_on_Continue(self):        

        for j in range(1, len(self.radio_buttons_list())+1) :

            self.select_radio_button(j) 
                       
            self.select_continue_button()
            if (driver.find_elements_by_class_name('ant-modal-footer')) :
                try :
                    email_back = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ant-modal-footer > button:nth-child(1)')))
                    sleep(1)
                    email_back.click()
                except  TimeoutException as ex:
                    log.info('no email pop up')

            else :            
                self.select_back_button()
            
            
            self.assertEqual(self.check_radio_button_selection(j), True)


    # @unittest.skip('check_font_of_answer_options')
    def test_10_check_font_of_answer_options(self):

        sleep(3)

        for i in driver.find_elements_by_css_selector('output > div'):

            log.info(i.value_of_css_property('font-size'))
            log.info(i.value_of_css_property('font-family'))

    def test_11_check_URL(self) :

        url = driver.current_url
        url_status = url.startswith('https://')
        self.assertIs(url_status , True)


    @unittest.skip('check_if_text_present_in_Learn_More')
    def test_12_check_if_text_present_in_Learn_More(self) :

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
    def test_13_check_if_user_can_close_Learn_More(self) :

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


    def test_select_continue_test_email_data(self) :

        try :
            self.assertTrue(self.select_continue_test_email_data(email_test_data))                
                    

        except AssertionError as e:
            print('{} for {}'.format(e , row))
                    






if __name__ == '__main__':
  unittest.main()

