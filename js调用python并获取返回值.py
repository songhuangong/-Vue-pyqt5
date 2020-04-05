import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import QWebChannel
from shared import Myshared


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('js <-> py')
        self.resize(330, 220)
        self.layout = QVBoxLayout()

        self.btn_test = QPushButton('test')
        # self.btn_test.clicked.connect(self.test)

        # 创建一个 QWebEngineView 对象
        self.web = QWebEngineView()
        file_path = QFileInfo("./test.html").absoluteFilePath()
        self.web.load(QUrl(file_path))

        # 把QWebView和button加载到layout布局中
        self.layout.addWidget(self.web)
        self.layout.addWidget(self.btn_test)
        self.setLayout(self.layout)

        self.channel = QWebChannel()
        self.shared = Myshared()
        self.set_channel()

    def set_channel(self):
        self.channel.registerObject("conn_shared", self.shared)
        self.web.page().setWebChannel(self.channel)

    def __del__(self):
        '''
        删除相关对象
        '''
        self.web.deleteLater()
        # 让系统加快释放这部分内存，避免QWebEngineView崩溃


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())
