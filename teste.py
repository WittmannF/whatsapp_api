from whatsapp_api import WhatsApp
from time import sleep

wp = WhatsApp()

listnumbers = [ '553192684127',
                '553186500997',
                '553199880216',
                '553196387488',
                '553184367274',
                '553175789449',
                '553187626533',
                '553191579935',
                '553195655165',
                '553198242405',
                '553196976289',
                '553197586016',
                '553175819872',
                '553175799483',
                '553185838372',
                '553193367723',
                '553191432155',
                '553186320685',
                '553198176683',
                '553186972822',
                '553191145475',
                '553191145475',
                '553186268681',
                '553199645360',
                '553199054543',

]

sleep(10)
for member in listnumbers:
    wp.without_contact(wp.parser(member))
    sleep(5)
    wp.send_message("Bom dia!")
    sleep(5)
    wp.send_message("Conseguiu acessar suas aulas?")
    sleep(5)
