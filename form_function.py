import unittest
from form_setting import driver
from form_setting import formSetUp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pdb
from selenium.common.exceptions import TimeoutException
from form_setting import log
import csv


# class FormFunc(formSetUp) : 
class FormFunc(unittest.TestCase) :

    disable_back_before_hover = 'rgba(255, 255, 255, 1)'
    disable_back_after_hover = 'rgba(255, 255, 255, 1)'
    enable_back_before_hover = 'rgb(255, 133, 0)' 
    enable_back_after_hover     = 'rgb(255,159, 41)'

    disable_continue_before_hover = 'rgba(245, 245, 245, 1)'
    disable_continue_after_hover = 'rgba(245, 245, 245, 1)'
    enable_continue_before_hover = 'rgba(255, 133, 0, 1)'
    enable_continue_after_hover  = 'rgba(255, 159, 41, 1)'
    # self.locator = LocatorClass()


    # self.locator.method_name()

    def check_continue_button_presence(self):

        try:

            continue_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(3)')))        

            log.info('Continue button present : {}'.format(
                continue_button.is_displayed()))
            # print ('Continue button is present : {}'.format(continue_button.is_displayed()))

            return continue_button.is_displayed() 


        except TimeoutException as e:

            log.info('continue button not present')

    
    def check_continue_button_enabled(self):

        continue_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(3)'))) 

        if ((self.check_continue_button_presence()) == True) :
            log.info('Continue button is enabled : {}'.format(
                continue_button.is_enabled()))
            return continue_button.is_enabled()

        else :

            log.info('continue button is not present')

    def check_hover_on_continue_button(self) :


        if ((self.check_continue_button_enabled()) == True) :

            continue_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(3)'))) 

            bg_color_before_hovering = continue_button.value_of_css_property('background-color')

            log.info('background color before hovering on element : {}'.format(
                bg_color_before_hovering))
            self.assertEqual(bg_color_before_hovering, self.enable_continue_before_hover)

            ActionChains(driver).move_to_element(continue_button).perform()
            sleep(1)

            bg_color_after_hovering = continue_button.value_of_css_property('background-color')
            
            log.info('background color after hovering on element : {}'.format(
                bg_color_after_hovering))
            self.assertEqual(bg_color_after_hovering, self.enable_continue_after_hover)

        else :

            continue_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(3)'))) 

            bg_color_before_hovering = continue_button.value_of_css_property('background-color')

            log.info('background color before hovering on element : {}'.format(
                bg_color_before_hovering))
            self.assertEqual(bg_color_before_hovering, self.disable_continue_before_hover)

            ActionChains(driver).move_to_element(continue_button).perform()
            sleep(1)

            bg_color_after_hovering = continue_button.value_of_css_property('background-color')
            
            log.info('background color after hovering on element : {}'.format(
                bg_color_after_hovering))
            self.assertEqual(bg_color_after_hovering, self.disable_continue_after_hover)

    def select_continue_button_check_popup(self):

        continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(3)')))
        enability_of_continue = continue_button.is_enabled()

        self.assertIs(enability_of_continue , True)


        if(enability_of_continue == True):
            continue_button.click()
            try :
                email_close = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, 'ant-modal-close')))
                email_close.click()
            except  TimeoutException as ex:
                log.info('no email pop up')
        else:
            log.info('Continue button is disable')


    def select_continue_enter_email_if_present(self) :

        continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(3)')))
        enability_of_continue = continue_button.is_enabled()
        print(continue_button.is_enabled())

        print('continue enable = {}'.format(self.assertTrue(enability_of_continue)))

        if(enability_of_continue == True):
            continue_button.click()
        else:
            log.info('Continue button is disable')

        if(driver.find_elements_by_css_selector('body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div.ant-form-item-control-wrapper > div > input')) :
            try :
                email_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div.ant-form-item-control-wrapper > div > input')))
                email_field.send_keys("abc@gmail.com")
                
                email_send = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ant-modal-body > button.ant-btn result-modal-btn ant-btn-secondary')))
                email_send.click()
            except  TimeoutException as ex:
                log.info('no email pop up')
        else:
            log.info('Pop up not present')


    def select_continue_test_email_data(self) :

        continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(3)')))
        enability_of_continue = continue_button.is_enabled()

        self.assertIs(enability_of_continue , True)

        if(enability_of_continue == True):
            continue_button.click()
        else:
            log.info('Continue button is disable')

        if(driver.find_elements_by_css_selector('body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div.ant-form-item-control-wrapper > div > input')) :
                
            email_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div.ant-form-item-control-wrapper > div > input')))
               
            with open('/home/alqama/workspace/autotest-englishduniya/webform/email_test_data.csv' , newline = '') as csvfile :
                spamreader =  csv.reader(csvfile , delimiter ='\t' )  

                for row in spamreader :

                    email_field.clear()
                    email_field.send_keys(row[0])          
                    
                    email_send = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-modal-body > button')))
                    enability_of_email_send = email_send.is_enabled()


                
                    try :
                    
                        self.assertEqual(row[1],str(enability_of_email_send))
                    

                    except AssertionError as e:
                        
                        print('{} should be {} but it is {}'.format(row[0] , row[1], str(enability_of_email_send)))
                    
                    email_close = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, 'ant-modal-close')))
                    email_close.click() 
                    
                    
        else:
            print('email Pop up not present')

             


    def select_continue_button(self):

        continue_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(3)')))
        enability_of_continue = continue_button.is_enabled()
        self.assertIs(enability_of_continue , True)

        if(enability_of_continue == True):
            continue_button.click()
            
        else:
            log.info('Continue button is disable')

    def check_back_button_presence(self) :

        back_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(2)')))        

        log.info('Back button present : {}'.format(back_button.is_displayed()))

        return back_button.is_displayed()

    def check_back_button_enabled(self) :
   

        if ((self.check_back_button_presence()) == True) :
            back_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(2)')))

            log.info('Back button is enabled : {}'.format(
                back_button.is_enabled()))
            return back_button.is_enabled()

        else :

            log.info('back button is not present')

    def check_hover_on_back_button(self) :

         
        if ((self.check_back_button_enabled()) == True) :

            back_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(2)'))) 


            bg_color_before_hovering = back_button.value_of_css_property('color')
            

            log.info('background color before hovering on enabled back element : {}'.format(
                bg_color_before_hovering))

            self.assertEqual(bg_color_before_hovering, self.enable_back_before_hover)

            ActionChains(driver).move_to_element(back_button).perform()
            sleep(1)

            bg_color_after_hovering = back_button.value_of_css_property('color')
            
            
            log.info('background color after hovering on enabled back element : {}'.format(
                bg_color_after_hovering))
            self.assertEqual(bg_color_after_hovering, self.enable_back_after_hover)

        else :

            back_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(2)'))) 

            bg_color_before_hovering = back_button.value_of_css_property('background-color')

            log.info('background color after hovering on element : {}'.format(
                bg_color_before_hovering))
            
            self.assertEqual(bg_color_before_hovering, self.disable_back_before_hover)

            ActionChains(driver).move_to_element(back_button).perform()
            sleep(1)

            bg_color_after_hovering = back_button.value_of_css_property('background-color')
            
            
            self.assertEqual(bg_color_after_hovering, self.disable_back_after_hover)
    

    def select_back_button(self):

        back_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.section-carousel-btn-container > button:nth-child(2)')))

        enability_of_back = back_button.is_enabled()

        self.assertIs(enability_of_back , True)

        if(enability_of_back == True):
            back_button.click()

        else:
            log.info('Back button is disable')

    def radio_button(self, i):

        radio_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.control-scq > div > div > div > div > div:nth-child({}) > div'.format(i))))

        
        return radio_button

    def radio_button_inner(self, i):

        radio_button_inner = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.control-scq > div > div > div > div > div:nth-child({}) > div > label > span.ant-radio > span'.format(i))))

        return radio_button_inner

    def radio_buttons_list(self):

        radio_buttons_list = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, '.control-scq > div > div > div > div > div > div')))

        return radio_buttons_list

    def radio_buttons_inner_list(self):

        radio_buttons_inner_list = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, '.control-scq > div > div > div > div > div > div > label > span.ant-radio > span')))

        return radio_buttons_inner_list

    def select_radio_button(self, i):

        ActionChains(driver).move_to_element(self.radio_button_inner(i)).click().perform()

        # self.radio_button_inner(i).click()
        log.info('radio button {} is selected'.format(i))
        log.info('it is located at {}'.format(self.radio_button(i).location))

    def check_radio_button_selection(self, i):

        self.radio_button(i)
        

        status = self.radio_button(i).get_attribute('class')
        status_check = 'checked' in status
        return status_check

    def check_radio_button_hover(self, i):

        self.radio_button(i)

        bg_color_before_hovering = self.radio_button(i).value_of_css_property(
            'background-color')
        log.info('background color before hovering on element : {}'.format(
            bg_color_before_hovering))
        self.assertEqual(bg_color_before_hovering, 'rgba(0, 0, 0, 0)')

        ActionChains(driver).move_to_element(self.radio_button(i)).perform()
        sleep(1)

        bg_color_after_hovering = self.radio_button(i).value_of_css_property(
            'background-color')
        log.info('background color after hovering on element : {}'.format(
            bg_color_after_hovering))
        self.assertEqual(bg_color_after_hovering, 'rgba(217, 217, 217, 0.3)')

    def check_radio_selection_color(self, i):

        sleep(1)

        self.radio_button(i)

        bg_color_after_selection = self.radio_button(i).value_of_css_property(
            'background-color')
        log.info('background color after selecting radio: {}'.format(
            bg_color_after_selection))
        return bg_color_after_selection


    element_default_color = 'rgba(0, 0, 0, 0)'
    element_hover_color = 'rgba(217, 217, 217, 0.3)'
    checkbox_selection_color = 'rgba(4, 210, 200, 0.2)'
    checkbox_border_color = 'rgba(4, 210, 200, 1)'
    checkbox_border_default_color = 'rgba(0, 0, 0, 0.65)'

    def checkbox(self, i):

        checkbox = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.control-mcq > div > div > div > div > div:nth-child({}) > div'.format(i))))

        return checkbox

    def checkbox_inner(self, i):

        checkbox_inner = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.control-mcq > div > div > div > div > div:nth-child({}) > div > label > span.ant-checkbox '.format(i))))

        return checkbox_inner

    def checkbox_list(self):

        checkbox = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, '.control-mcq > div > div > div > div > div > div')))

        return checkbox

    def checkbox_inner_list(self):

        checkbox_inner = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, '.control-mcq > div > div > div > div > div > div > label > span.ant-checkbox ')))

        return checkbox_inner

    def select_checkbox(self, i):

        ActionChains(driver).move_to_element(self.checkbox_inner(i)).perform()
        # log.info('it is located at {}'.format(self.checkbox_inner(i)).location())
        self.checkbox_inner(i).click()
        log.info('checkbox {} is selected'.format(i))

    def check_checkbox_selection(self, i):
        sleep(0.5)
        status = self.checkbox(i).get_attribute('class')
        status_check = 'checked' in status
        return status_check

    def check_checkbox_hover(self, i):

        bg_color_before_hovering = self.checkbox(i).value_of_css_property(
            'background-color')
        log.info('background color before hovering on element : {}'.format(
            bg_color_before_hovering))
        self.assertEqual(bg_color_before_hovering, self.element_default_color)

        ActionChains(driver).move_to_element(self.checkbox(i)).perform()
        sleep(1)

        bg_color_after_hovering = self.checkbox(i).value_of_css_property(
            'background-color')
        log.info('background color after hovering on element : {}'.format(
            bg_color_after_hovering))
        self.assertEqual(bg_color_after_hovering, self.element_hover_color)

    def check_checkbox_selection_color(self, i):

        sleep(1)

        bg_color_after_selection = self.checkbox(i).value_of_css_property(
            'background-color')
        log.info('background color after selecting checkbox: {}'.format(
            bg_color_after_selection))
        return bg_color_after_selection

    def check_checkbox_border_color(self, i):

        sleep(1)

        border_color = self.checkbox_inner(i).value_of_css_property(
            'border-color')
        return border_color