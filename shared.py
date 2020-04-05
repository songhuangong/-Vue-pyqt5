from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import *


class Myshared(QWidget):
    '''
    共享类
    '''

    @pyqtSlot(str, result=int)
    def test_str_int(self, one_str):
        print(one_str)
        try:
            r = int(one_str)
        except Exception:
            return -1
        return r

    @pyqtSlot(int, result=str)
    def test_int_str(self, num):
        return str(num + 111)