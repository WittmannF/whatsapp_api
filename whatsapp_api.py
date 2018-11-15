from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Parameters
WP_LINK = 'https://web.whatsapp.com'

## XPATHS
CONTACTS_XPATH = '//*[@id="main"]/header/div[2]/div[2]/span'
SEND = '//*[@id="main"]/footer/div[1]/div[3]'
MESSAGE_BOX = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'


class WhatsApp:
    def __init__(self):
        self.driver = self._setup_driver()
        self.driver.get(WP_LINK)
        print("Please scan the QR Code and enter in the group that you want to \
        have control")

    @staticmethod
    def _setup_driver():
        print('Loading...')
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver

    def _get_element(self, xpath, attempts=5, _count=0):
        '''Safe get_element method with multiple attempts'''
        try:
            element = self.driver.find_element_by_xpath(xpath)
            return element
        except Exception as e:
            if _count<attempts:
                sleep(1)
                self._get_element(driver, xpath, attempts=attempts, _count=_count+1)
            else:
                print("Element not found")

    def _click(self, xpath):
        el = self._get_element(xpath)
        el.click()

    @staticmethod
    def _convert(param):
        if isinstance(param, str):
            return param.decode('utf-8')
        else:
            return param

    def _send_keys(self, xpath, message):
        el = self._get_element(xpath)
        el.send_keys(self._convert(message))

    def write_message(self, message):
        '''Write message in the text box but not send it'''
        self._click(MESSAGE_BOX)
        self._send_keys(MESSAGE_BOX, message)

    def send_message(self, message):
        '''Write and send message'''
        self.write_message(message)
        self._click(SEND)

    def get_group_numbers(self):
        '''Get phone numbers from a whatsapp group'''
        try:
            el = self.driver.find_element_by_xpath(CONTACTS_XPATH)
            return el.text.split(',')
        except Exception as e:
            print("Group header not found")


