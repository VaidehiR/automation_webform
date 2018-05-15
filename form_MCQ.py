import unittest
from form_setting import driver
# from form_setting import formSetUp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from form_function import FormFunc
import pdb
from form_setting import log


class McqForm(FormFunc):


    def test_01_check_hover_state_on_continue_button(self):   

        pdb.set_trace()         

        self.check_hover_on_continue_button()

    def test_02_check_hover_state_on_back_button(self):            
        
        self.check_hover_on_back_button()

    def test_03_check_hover_state_on_checkbox(self):

        for j in range(1, len(self.checkbox_list()) + 1):

            self.check_checkbox_hover(j)

    # @unittest.skip('check_checkbox_selection_color')
    def test_04_check_checkbox_selection_color(self):

        for j in range(1, len(self.checkbox_list()) + 1):

            self.select_checkbox(j)
            self.assertEqual(self.check_checkbox_selection_color(
                j), self.checkbox_selection_color)

        for j in range(1, len(self.checkbox_list()) + 1):

            self.select_checkbox(j)

    # @unittest.skip('check_checkbox_functionality')
    def test_05_check_checkbox_selection_after_clicking_twice(self):

        for j in range(1, len(self.checkbox_inner_list()) + 1):

            self.select_checkbox(j)
            self.select_checkbox(j)

            log.info('Clicked twice on chackbox {}'.format(j))

            self.assertEqual(self.check_checkbox_selection(j), False)

            self.check_continue_button_enabled()

    # @unittest.skip('check_checkboxe_selection_after_another_checkbox_selection')
    def test_06_check_checkboxe_selection_after_another_checkbox_selection(self):

        for j in range(1, len(self.checkbox_list()) + 1) :
            
            self.select_checkbox(j)

        for j in range(1, len(self.checkbox_list()) + 1) :
                
            self.assertEqual(self.check_checkbox_selection(j), True)               
            self.select_checkbox(j)

    # @unittest.skip('check_Continue_button_state_after_selecting_checkbox')
    def test_07_check_Continue_button_state_after_selecting_checkbox(self):

        for j in range(1, len(self.checkbox_list()) + 1) :
            
            self.select_checkbox(j)
            self.check_continue_button_enabled()

    # @unittest.skip('check_Continue_button_state_after_deselecting_checkbox')
    def test_08_check_Continue_button_state_after_deselecting_checkbox(self):

        for j in range(1, len(self.checkbox_list()) + 1) :
            
            self.select_checkbox(j)
            self.check_continue_button_enabled()

    def test_09_check_answer_selection_retains_on_Continue(self):


        for j in range(1, len(self.checkbox_list()) + 1) :

            self.select_checkbox(j)            
            self.select_continue_button()
            if (driver.find_elements_by_class_name('ant-modal-footer')) :
                try :
                    email_back = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-modal-footer > button:nth-child(1)')))
                    sleep(1)
                    email_back.click()
                except  TimeoutException as ex:
                    log.info('no email pop up')

            else :            
                self.select_back_button()
            
            self.assertEqual(self.check_checkbox_selection(j), True)

    # @unittest.skip('check_answer_selection_retains_on_Back')
    def test_10_check_answer_selection_retains_on_Back(self) :

        for j in range(1, len(self.checkbox_list()) + 1) :

            self.select_checkbox(j)
            self.select_back_button()  
                     
            self.select_continue_button_check_popup()
            
            self.assertEqual(self.check_checkbox_selection(j), True)
            # pdb.set_trace()
            self.select_checkbox(j)

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



if __name__ == '__main__':
    unittest.main()
