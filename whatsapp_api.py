from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep
import sys

# Parameters
WP_LINK = 'https://web.whatsapp.com'

# XPATHS
CONTACTS = '//*[@id="main"]/header/div[2]/div[2]/span'
SEND = '//*[@id="main"]/footer/div[1]/div[3]'
MESSAGE_BOX = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
NEW_CHAT = '//*[@id="side"]/header/div[2]/div/span/div[2]/div'
SEARCH_CONTACT = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input'
FIRST_CONTACT = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div'
MoreContactsXPath = '//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[5]/div[2]'
GroupInfoXPath = '// *[ @ id = "app"] / div / div / div[2] / div[3] / span / div / span / div / div / div[1]'

# Classes
nameClass = '_19RFN._1ovWX._F7Vk'
messageClass = '_12pGw'
messageMenuClass = '_2-qoA'
messageMenuButtonsClass = '_3zy-4.Sl-9e._3_4Kp'
eraseButtonsClass = '_2eK7W._23_1v'

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
            # print('Found element!')
            return element
        except Exception as e:
            if _count < attempts:
                sleep(1)
                # print(f'Attempt {_count}')
                self._get_element(xpath, attempts=attempts, _count=_count + 1)
            else:
                print("Element not found")

    def _click(self, xpath):
        el = self._get_element(xpath)
        el.click()

    def _send_keys(self, xpath, message):
        el = self._get_element(xpath)
        el.send_keys(message)

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
            el = self.driver.find_element_by_xpath(CONTACTS)
            return el.text.split(', ')
        except Exception as e:
            print("Group header not found")

    def get_group_members_long(self):
        """Get complete members' names (or numbers, if person is not in contact list) from a WhatsApp group"""
        try:
            # Click on contacts:
            el = self.driver.find_element_by_xpath(CONTACTS)
            el.click()
            sleep(3)

            # Trying to click in more contacts (it may not exist)
            try:
                el = self.driver.find_element_by_xpath(MoreContactsXPath)
                el.click()
            except Exception as e:
                msg = 'Error in {}.{}. Message: {}'.format(
                    self.__class__.__name__,            # Ref. for getting class name on 2019-06-26:  https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
                    sys._getframe().f_code.co_name,     # Ref. for getting method name on 2019-06-26: https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
                    e)
                print(msg)

            el1 = self.driver.find_element_by_xpath(GroupInfoXPath) # Getting element for Group Info box panel.
            el2 = el1.find_elements_by_class_name(nameClass)        # Locating all elements of such class inside el1.
            Members = [e.text for e in el2]                         # Getting only the texts, not the whole objects.

            return Members

        except Exception as e:
            msg = 'Error in {}.{}. Message: {}'.format(
                self.__class__.__name__,
                # Ref. for getting class name on 2019-06-26:  https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
                sys._getframe().f_code.co_name,
                # Ref. for getting method name on 2019-06-26: https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
                e)
            print(msg)

    def search_contact(self, keyword):
        '''Write and send message'''
        self._click(NEW_CHAT)
        self._send_keys(SEARCH_CONTACT, keyword)
        sleep(1)
        try:
            self._click(FIRST_CONTACT)
        except Exception as e:
            print("Contact not found")

    def get_all_messages(self):
        all_messages_element = self.driver.find_elements_by_class_name('_12pGw')
        all_messages_text = [e.text for e in all_messages_element]
        return all_messages_text

    def get_last_message(self):
        all_messages = self.get_all_messages()
        return all_messages[-1]

    def get_all_messages_elements(self):
        """Gets all messages currently shown in screen."""
        all_messages_element = self.driver.find_elements_by_class_name(messageClass)
        return all_messages_element

    def delete_message_from_recent(self, text):
        """From recent (visible) messages, deletes the one with text equals to 'text'."""
        try:
            all_messages_element = self.get_all_messages_elements()     # Getting all recent messages.

            for e in reversed(all_messages_element):                    # Looking at each element in reversed order.
                if e.text == text:
                    # Moving mouse over message, so menu appear. Ref: http://allselenium.info/mouse-over-actions-using-python-selenium-webdriver/
                    action = ActionChains(self.driver)
                    action.move_to_element(e).perform()
                    sleep(1)

                    # Clicking on menu
                    msgMenu = self.driver.find_elements_by_class_name(messageMenuClass)
                    msgMenu[0].click()
                    sleep(1)

                    # Clicking on delete button:
                    msgMenuButtons = self.driver.find_elements_by_class_name(messageMenuButtonsClass)   # Getting buttons
                    msgMenuButtons[-1].click()                                                          # Clicking on last button.
                    sleep(1)

                    # Clicking on 'Erase for me' button:
                    eraseButtons = self.driver.find_elements_by_class_name(eraseButtonsClass)   # Getting buttons
                    eraseButtons[0].click()                                                     # Clicking on first button.

                    break                                                                       # After deleting last msg that corresponds to 'text', breaks for loop.
            else:
                print('Did not find recent message with text: ' + text)

        except Exception as e:
            msg = 'Error in {}.{}. Message: {}'.format(
                self.__class__.__name__,            # Ref. for getting class name on 2019-06-26:  https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
                sys._getframe().f_code.co_name,     # Ref. for getting method name on 2019-06-26: https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
                e)
            print(msg)
