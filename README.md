# WhatsApp API on Selenium
Easy to use API on selenium to have control of WhatsApp Web over the browser. 

### Implemented features
- Get all contacts from a selected group

### Possible future features
- Send message
- Add contacts

### Requirements
- Selenium: `pip install selenium`
- ChromeDriver: http://chromedriver.chromium.org/
    - After downloading chromedriver, make sure to add in a folder accessible from the PATH

### Example of Usage:

```
In [1]: from whatsapp_api import WhatsApp
In [2]: wp = WhatsApp()
Loading...
Please scan the QR Code and enter in the group
In [3]: wp.get_contacts()
Out[3]:
[u'+1...
```

### LICENCE
MIT
