from PyQt5 import QtWidgets, uic , QtGui 
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox  , QFileDialog
import sys , os ,pysubs2 , time , asyncio
from requests import get 
from bs4 import BeautifulSoup
import io
template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1003</width>
    <height>837</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <pointsize>10</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true"/>
  </property>
  <property name="animated">
   <bool>true</bool>
  </property>
  <property name="documentMode">
   <bool>false</bool>
  </property>
  <property name="tabShape">
   <enum>QTabWidget::Rounded</enum>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="autoFillBackground">
    <bool>false</bool>
   </property>
   <property name="styleSheet">
    <string notr="true"/>
   </property>
   <widget class="QPushButton" name="search_button">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>150</y>
      <width>200</width>
      <height>50</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>B Badr</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
	color: rgb(58, 134, 255);
	background-color: white;
	border: 2px solid rgb(58, 134, 255);
	border-radius: 20px;
}
QPushButton:hover {
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
  color: white;
}</string>
    </property>
    <property name="text">
     <string>Click to Search</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>80</y>
      <width>690</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>B Badr</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="tabletTracking">
     <bool>false</bool>
    </property>
    <property name="accessibleName">
     <string/>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">    QComboBox {
   		 border-radius: 10px;
		border: 2px solid rgb(255, 69, 0);
    	color: rgb(0, 0, 255);
    }    
    QComboBox::drop-down {
     	subcontrol-origin: padding;
    	subcontrol-position: top right;
    	width: 20px;
    }</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhPreferNumbers</set>
    </property>
    <property name="currentText">
     <string/>
    </property>
    <property name="currentIndex">
     <number>-1</number>
    </property>
    <property name="sizeAdjustPolicy">
     <enum>QComboBox::AdjustToContentsOnFirstShow</enum>
    </property>
    <property name="minimumContentsLength">
     <number>0</number>
    </property>
    <property name="duplicatesEnabled">
     <bool>false</bool>
    </property>
    <property name="frame">
     <bool>false</bool>
    </property>
    <property name="placeholderText" stdset="0">
     <string notr="true"/>
    </property>
   </widget>
   <widget class="Line" name="line_6">
    <property name="geometry">
     <rect>
      <x>121</x>
      <y>40</y>
      <width>20</width>
      <height>181</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="QPushButton" name="clear_button">
    <property name="geometry">
     <rect>
      <x>650</x>
      <y>150</y>
      <width>200</width>
      <height>50</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>B Badr</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
	color: rgb(58, 134, 255);
	background-color: white;
	border: 2px solid rgb(58, 134, 255);
	border-radius: 20px;
}
QPushButton:hover {
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
  color: white;
}</string>
    </property>
    <property name="text">
     <string>Clear Results</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>15</y>
      <width>141</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>B Badr</family>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Category</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="Line" name="line_7">
    <property name="geometry">
     <rect>
      <x>872</x>
      <y>40</y>
      <width>20</width>
      <height>181</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_8">
    <property name="geometry">
     <rect>
      <x>380</x>
      <y>30</y>
      <width>501</width>
      <height>21</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="Line" name="line_9">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>210</y>
      <width>751</width>
      <height>21</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="Line" name="line_10">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>30</y>
      <width>91</width>
      <height>20</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>235</y>
      <width>141</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>B Badr</family>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Output</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="Line" name="line_11">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>770</y>
      <width>751</width>
      <height>21</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="Line" name="line_12">
    <property name="geometry">
     <rect>
      <x>380</x>
      <y>250</y>
      <width>501</width>
      <height>21</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="Line" name="line_13">
    <property name="geometry">
     <rect>
      <x>121</x>
      <y>260</y>
      <width>20</width>
      <height>521</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_14">
    <property name="geometry">
     <rect>
      <x>872</x>
      <y>260</y>
      <width>20</width>
      <height>521</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_15">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>250</y>
      <width>91</width>
      <height>20</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="QListWidget" name="listWidget">
    <property name="geometry">
     <rect>
      <x>155</x>
      <y>311</y>
      <width>701</width>
      <height>451</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>15</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QListWidget {
    border: 2px solid gray;
    border-radius: 10px;
    padding: 0 8px;
	color: rgb(58, 134, 255);
	background-color: white;
	border: 2px solid rgb(255, 69, 0);
    selection-background-color: darkgray;
}
</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""



list_options = {}

class craigslist:
    def __init__(self):
        pass

    def get_menu(self):
        global list_options
        site_source = get("https://boston.craigslist.org/search/jjj?").text
        soup = BeautifulSoup(site_source, 'html.parser')
        drop_menu = soup.find_all('li',attrs={"class": "crumb category"})
        options = drop_menu[0].find_all('option')
        list_options = {}
        for option in options:
            list_options[option.text] = option.attrs['value']

        return list_options

    def get_jobs(self , tag):
        site_source = get(f"https://boston.craigslist.org/search/{tag}?").text
        soup = BeautifulSoup(site_source, 'html.parser')
        rows = soup.find_all('li',attrs={"class": "result-row"})
        list_jobs = []
        for row in rows:
            text = row.find('h3',{"class":"result-heading"}).text.strip()
            link = row.find('h3',{"class":"result-heading"}).find('a')['href']
            text += " "
            try:
                text += row.find('span',{"class":"result-hood"}).text.strip()
            except:
                text += row.find('span',{"class":"nearby"}).text.strip()

            text += " ||| " + link
            list_jobs.append(text)
    
        return list_jobs
    
    def get_page(self , url):
        site_source = get(url).text
        soup = BeautifulSoup(site_source, 'html.parser')
        return soup.find_all('section',attrs={"id": "postingbody"})[0].text.strip()
    
    
class AnotherWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self,name,url):
        super().__init__()
        self.setWindowTitle(name)
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        layout = QtWidgets.QVBoxLayout()
        self.textEdit = QtWidgets.QTextEdit()
        text = craigslist().get_page(url)
        self.textEdit.setPlainText(text)
        self.textEdit.setStyleSheet("QTextEdit {\n    border: 2px solid gray;\n    border-radius: 10px;\n    padding: 0 8px;\n	color: rgb(58, 134, 255);\n	background-color: white;\n	border: 2px solid rgb(255, 69, 0);\n    selection-background-color: darkgray;\n}\n")
        layout.addWidget(self.textEdit)
        self.setLayout(layout)

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        #uic.loadUi('untitled1.ui', self)
        uic.loadUi(io.StringIO(template), self)
        self.setFixedWidth(1003)
        self.setFixedHeight(837) 
        self.setWindowTitle("Boston Jobs")
        self.API = craigslist()
        self.findChild(QtWidgets.QPushButton, 'search_button').clicked.connect(self.search_function)
        self.findChild(QtWidgets.QPushButton, 'clear_button').clicked.connect(self.clear_function)
        self.findChild(QtWidgets.QListWidget, 'listWidget').itemClicked.connect(self.on_selection_changed)
        self.show()
        QTimer.singleShot(1,self.load_catagories) #waits for this to finish until gui displayed

        

    def on_selection_changed(self):
        url = self.findChild(QtWidgets.QListWidget, 'listWidget').selectedItems()[0].text().split("|||")
        self.a = AnotherWindow(url[0].strip(),url[1].strip())
        self.a.show()
        
    def load_catagories(self):
        QMessageBox.warning(self,"Wait","Loading catagories ...")
        try:
            for i in self.API.get_menu():
                self.findChild(QtWidgets.QComboBox, 'comboBox').addItem(i)
        except:
            QMessageBox.warning(self,"Error","There is a problem with your internet connections")

    def search_function(self):
        global list_options
        selected_catagory = self.findChild(QtWidgets.QComboBox, 'comboBox').currentText()
        tag_name = list_options[selected_catagory]
        QMessageBox.warning(self,"Wait","Loading jobs ...")
        try:
            for i in self.API.get_jobs(tag_name):
                self.findChild(QtWidgets.QListWidget, 'listWidget').addItem(i)
        except:
            QMessageBox.warning(self,"Error","There is a problem with your internet connections")
            
    def clear_function(self):
        self.findChild(QtWidgets.QListWidget, 'listWidget').clear()
            
app = QtWidgets.QApplication(sys.argv)
window = Ui()
asyncio.run(app.exec_())
