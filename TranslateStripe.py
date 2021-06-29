import translatemodule
import pyperclip
def shapeText(target, source):
    mes = pyperclip.paste()
    print(mes)
    mes = mes.split('\r\n')
    reText = ""
    
    for i in range(len(mes)):
        reText = reText + mes[i]
    reText = translatemodule.get_translated_text(target, source, reText)
    pyperclip.copy(reText)