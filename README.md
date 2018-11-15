# WhatsApp Group API on Selenium
Easy to use API on selenium to have control of a WhatsApp group using the web browser. 

### Implemented features
- Get all contacts from a selected group
```
In [1]: from whatsapp_api import WhatsApp
In [2]: wp = WhatsApp()
Loading...
Please scan the QR Code and enter in the group
In [3]: wp.get_group_numbers()
```
- Write and/or send messages
```
In [1]: from whatsapp_api import WhatsApp
In [2]: wp = WhatsApp()
Loading...
Please scan the QR Code and enter in the group
In [3]: wp.send_message('This message is going to be sent')
In [4]: wp.write_message('This message is going to be written but not sent')
```

### Possible future features
- ?

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
In [3]: wp.get_group_numbers()
Out[3]:
[u'+1...
```

### LICENCE
MIT
