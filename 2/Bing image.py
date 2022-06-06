from PyQt5 import QtWidgets, uic , QtGui ,QtCore
from PyQt5.QtCore import QObject, QThread, pyqtSignal , QTimer
from time import sleep 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox  , QFileDialog
import sys , os  , time , asyncio
from requests import get 
from bs4 import BeautifulSoup
import json
from PyQt5.QtCore import QObject, QThread, pyqtSignal
all_images = []

class Bing:
    def __init__(self):
        pass

    def image_search(self, text , count = 25):
        site_source = get(f"https://www.bing.com/images/async?q={text}&first=0&count={count}&cw=1177&ch=696&relp=35&tsc=ImageHoverTitle&datsrc=I&layout=RowBased&mmasync=1",
        headers={'Host': 'www.bing.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0', 'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}).text
        soup = BeautifulSoup(site_source, 'html.parser')
        images = soup.find_all('a',attrs={"class": "iusc"})
        list_images = []
        for image in images:
            y = json.loads(image.attrs['m'])
            list_images.append(y["murl"])
        return list_images
  
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('untitled1.ui', self)
        self.setWindowIcon(QtGui.QIcon('app_icon.png')) 
        self.setWindowTitle("Boston Jobs")
        
        self.findChild(QtWidgets.QPushButton, 'search_button').clicked.connect(self.search_function)
        self.findChild(QtWidgets.QPushButton, 'clear_button').clicked.connect(self.clear_function)
        
        content_widget = QtWidgets.QWidget()
        #self.scrollArea.setWidget(content_widget)
            
        self.findChild(QtWidgets.QScrollArea, 'scrollArea').setWidget(content_widget)
        self._lay = QtWidgets.QVBoxLayout(content_widget)


        self.counter = 0
        self.show()
    def add_all(self):
        global all_images
        for image in all_images:
            self.add_pixmap(image)
        
    def clear_function(self):
        for i in reversed(range(self._lay.count())): 
            self._lay.itemAt(i).widget().deleteLater()

    def search_function(self):
        global all_images , text_search
        all_images = []
        text_search = self.findChild(QtWidgets.QLineEdit, 'lineEdit').text()
        if text_search == "" :
            QMessageBox.warning(self,"Error","There nothing to search")
            return False

        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.add_all)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.thread.start()
        
    def add_pixmap(self, pixmap):
        if not pixmap.isNull():
            label = QtWidgets.QLabel(pixmap=pixmap)
            self._lay.addWidget(label)
     
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    def run(self):
        print("run rask")
        global all_images , text_search
        try:
            list_images = Bing().image_search(text_search,5)
            print("Successfully Bing")
        except:
            print("Error Bing")
        for image in list_images:
            try:
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0','Pragma': 'no-cache', 'Cache-Control': 'no-cache'}
                data = get(image,headers=headers, timeout=2).content
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(data)
                try:
                    pixmap5 = pixmap.scaled(650, 400)
                except:
                    pixmap5 = pixmap
                all_images.append(pixmap5)
            except Exception as e: 
                print("Error get image")
        self.finished.emit()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    sys.exit(app.exec_())
