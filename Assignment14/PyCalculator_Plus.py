from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
import math

TITLE = 'PyCalculator by AMK'

class modes:
    DEFAULT = 0
    ADD = 1
    SUBS = 2
    MUL = 3
    DIV = 4
    MOD = 5
    

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mode = modes.DEFAULT
        self.num1 = None

        self.ui = QUiLoader().load('user_interface_PLUS.ui') #loaded ui file
        self.ui.show()

        self.initButtons()
        

    def initButtons(self):
        self.ui.btnEqual.clicked.connect(self.equal)
        self.ui.btnPlus.clicked.connect(self.add)
        self.ui.btnMinus.clicked.connect(self.subs)
        self.ui.btnMul.clicked.connect(self.mul)
        self.ui.btnDiv.clicked.connect(self.div)
        self.ui.ac.clicked.connect(self.ac)
        self.ui.btn1.clicked.connect(self.btn1)
        self.ui.btn2.clicked.connect(self.btn2)
        self.ui.btn3.clicked.connect(self.btn3)
        self.ui.btn4.clicked.connect(self.btn4)
        self.ui.btn5.clicked.connect(self.btn5)
        self.ui.btn6.clicked.connect(self.btn6)
        self.ui.btn7.clicked.connect(self.btn7)
        self.ui.btn8.clicked.connect(self.btn8)
        self.ui.btn9.clicked.connect(self.btn9)
        self.ui.btn0.clicked.connect(self.btn0)
        self.ui.mod.clicked.connect(self.mod)
        self.ui.sign.clicked.connect(self.sign)
        self.ui.btnDot.clicked.connect(self.btnDot)
        self.ui.sin.clicked.connect(self.sin)
        self.ui.cos.clicked.connect(self.cos)
        self.ui.tan.clicked.connect(self.tan)
        self.ui.cot.clicked.connect(self.cot)
        self.ui.log.clicked.connect(self.log)
        self.ui.sqrt.clicked.connect(self.sqrt)

    def equal(self):
        num2 = self.getDisplay()
        if self.num1 is None or num2 == '':
            return
        num2 = float(num2)
        if self.mode == modes.ADD:
            sum = self.num1 + num2
        elif self.mode == modes.SUBS:
            sum = self.num1 - num2
        elif self.mode == modes.MUL:
            sum = self.num1 * num2
        elif self.mode == modes.DIV:
            try:
                sum = self.num1 / num2
            except ZeroDivisionError:
                sum = 0
                self.setEquation('DIVISION BY ZERO ERROR')
        elif self.mode == modes.MOD:
            try:
                sum = self.num1 % num2
            except ZeroDivisionError:
                sum = 0
                self.setEquation('DIVISION BY ZERO ERROR')
        else:
            sum = 0
        self.setEquation(self.ui.equation.text() + ' ' + str(num2) + ' =')
        self.setDisplay(sum)
        self.num1 = None

    def add(self):
        self.mode = modes.ADD
        self.num1 = float(self.getDisplay())
        self.setEquation(str(self.num1) + ' +')
        self.ui.display.clear()
    
    def subs(self):
        self.mode = modes.SUBS
        self.num1 = float(self.getDisplay())
        self.setEquation(str(self.num1) + ' -')
        self.ui.display.clear()

    def mul(self):
        self.mode = modes.MUL
        self.num1 = float(self.getDisplay())
        self.setEquation(str(self.num1) + ' *')
        self.ui.display.clear()

    def div(self):
        self.mode = modes.DIV
        self.num1 = float(self.getDisplay())
        self.setEquation(str(self.num1) + ' /')
        self.ui.display.clear()

    def mod(self):
        self.mode = modes.MOD
        self.num1 = float(self.getDisplay())
        self.setEquation(str(self.num1) + ' %')
        self.ui.display.clear()

    def ac(self):
        self.setDisplay('')
        self.setEquation(TITLE)
        self.num1 = None

    def sign(self):
        self.setDisplay(0 - float(self.getDisplay()))

    def sin(self):
        angle = float(self.getDisplay())
        result = math.sin(math.radians(angle))
        self.setDisplay(result)

    def cos(self):
        angle = float(self.getDisplay())
        result = math.cos(math.radians(angle))
        self.setDisplay(result)

    def tan(self):
        angle = float(self.getDisplay())
        result = math.tan(math.radians(angle))
        self.setDisplay(result)

    def cot(self):
        angle = float(self.getDisplay())
        result = 1/math.tan(math.radians(angle))
        self.setDisplay(result)

    def log(self):
        number = float(self.getDisplay())
        result = math.log10(number)
        self.setDisplay(result)

    def sqrt(self):
        number = float(self.getDisplay())
        result = math.sqrt(number)
        self.setDisplay(result)



    def btn1(self):
        self.setDisplay(self.getDisplay() + '1')
    def btn2(self):
        self.setDisplay(self.getDisplay() + '2')
    def btn3(self):
        self.setDisplay(self.getDisplay() + '3')
    def btn4(self):
        self.setDisplay(self.getDisplay() + '4')
    def btn5(self):
        self.setDisplay(self.getDisplay() + '5')
    def btn6(self):
        self.setDisplay(self.getDisplay() + '6')
    def btn7(self):
        self.setDisplay(self.getDisplay() + '7')
    def btn8(self):
        self.setDisplay(self.getDisplay() + '8')
    def btn9(self):
        self.setDisplay(self.getDisplay() + '9')
    def btn0(self):
        self.setDisplay(self.getDisplay() + '0')
    def btnDot(self):
        self.setDisplay(self.getDisplay() + '.')


    def setDisplay(self, text):
        self.ui.display.setText(str(text))

    def getDisplay(self):
        return self.ui.display.text()


    def setEquation(self, text):
        self.ui.equation.setText(str(text))
    
    '''def keyPressEvent(self, event: QKeyEvent) -> None:
        super().keyPressEvent(event)
        if event.key() == Qt.Key_Enter:
            self.equal()'''
        
        
        
if __name__ == '__main__':
    app = QApplication()
    cal_obj = Calculator()
    app.exec()

