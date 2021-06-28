import translatemodule
import pyperclip
def shapeText():
    mes = pyperclip.paste()
    print(mes)
    mes = mes.split('\r\n')
    reText = ""
    
    for i in range(len(mes)):
        reText = reText + mes[i]
    reText = translatemodule.get_translated_text('en', 'ja', reText)
    pyperclip.copy(reText)