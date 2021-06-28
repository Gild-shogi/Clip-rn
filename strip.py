import pyperclip
def shapeText():
    mes = pyperclip.paste()
    print(mes)
    mes = mes.split('\r\n')
    reText = ""
    
    for i in range(len(mes)):
        reText = reText + mes[i]
    pyperclip.copy(reText)
"""
before = ""
while True:
    message = pyperclip.paste()
    if before != message:
        shapeText()
    before = pyperclip.paste()
"""