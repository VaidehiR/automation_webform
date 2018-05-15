import unittest
import os
import HTMLTestRunner
import form_SCQ
import form_MCQ
import form_setting
import form_allType
from form_setting import formlink
from form_function import FormFunc
from form_setting import driver
from time import sleep
from form_setting import log
import pdb

class MainTestRunner(FormFunc):

    def setUp(self) :
        driver.maximize_window()
        driver.get(formlink)
        
    def test_01_check_type(self) : 
        count = 1

        
        while(self.check_continue_button_presence()) :


            if driver.find_elements_by_class_name('control-mcq'):

                # suite = unittest.TestSuite()
                # suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(form_MCQ.McqForm))              
                
                # unittest.TextTestRunner().run(suite)
                
                # self.select_continue_enter_email_if_present()
                # sleep(1)

                suite = unittest.TestSuite()
                suite.addTest(
                unittest.defaultTestLoader.loadTestsFromTestCase(form_MCQ.McqForm))

                outfile = open("/home/alqama/workspace/autotest-englishduniya/webform/form_test_result" + "/WebFormReportMCQ{}.html".format(count), "w")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description='Webform Tests Report'
                )
                runner1.run(suite)
                self.select_continue_enter_email_if_present()
                
                count = count + 1
                sleep(1)
                

            elif driver.find_elements_by_class_name('control-scq') :
                
                # suite = unittest.TestSuite()

                # suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(form_SCQ.ScqForm))
                # unittest.TextTestRunner().run(suite)
                
                # self.select_continue_enter_email_if_present()
                # sleep(1)

                suite = unittest.TestSuite()
                suite.addTest(
                unittest.defaultTestLoader.loadTestsFromTestCase(form_SCQ.ScqForm))

                outfile = open("/home/alqama/workspace/autotest-englishduniya/webform/form_test_result" + "/WebFormReportSCQ{}.html".format(count), "w")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description='Webform Tests Report'
                )
                # pdb.set_trace()
                runner1.run(suite)

                self.select_continue_enter_email_if_present()
                
                count = count + 1
                sleep(1)

            
            elif driver.find_elements_by_class_name('item-block') :
                

            
                self.select_continue_enter_email_if_present()

                sleep(1)






                
    def tearDown(self) :

        driver.quit()



if __name__ == '__main__':
     unittest.main()