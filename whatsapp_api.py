from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Whatsapp Parameters
WP_LINK = 'https://web.whatsapp.com'
CONTACTS_XPATH = '//*[@id="main"]/header/div[2]/div[2]/span'

class WhatsApp:
    def __init__(self):
        self.driver = self._setup_driver(self)
        self.driver.get(WP_LINK)
        print("Please scan the QR Code and enter in the group that you want to have control")

    @staticmethod
    def _setup_driver(self):
        print('Loading...')
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver

    def get_contacts(self):
        el = self.driver.find_element_by_xpath(CONTACTS_XPATH)
        return el.text.split(',')

