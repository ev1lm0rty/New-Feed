from PyQt5 import QtCore, QtGui, QtWidgets
import R_Papers as RS
import News as NW
import Videos as VD

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.allTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.allTabs.setObjectName("allTabs")
        self.research = QtWidgets.QWidget()
        self.research.setObjectName("research")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.research)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.resMain = QtWidgets.QWidget(self.research)
        self.resMain.setObjectName("resMain")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.resMain)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.resSroll = QtWidgets.QScrollArea(self.resMain)
        self.resSroll.setWidgetResizable(True)
        self.resSroll.setObjectName("resSroll")
        self.resScrollContents = QtWidgets.QWidget()
        self.resScrollContents.setGeometry(QtCore.QRect(0, 0, 781, 436))
        self.resScrollContents.setObjectName("resScrollContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.resScrollContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resText = QtWidgets.QTextBrowser(self.resScrollContents)
        self.resText.setReadOnly(True)
        self.resText.setOpenExternalLinks(True)
        self.resText.setObjectName("resText")
        self.horizontalLayout_2.addWidget(self.resText)
        self.resSroll.setWidget(self.resScrollContents)
        self.verticalLayout_3.addWidget(self.resSroll)
        self.resInput = QtWidgets.QLineEdit(self.resMain)
        self.resInput.setObjectName("resInput")
        self.verticalLayout_3.addWidget(self.resInput)
        self.resButton = QtWidgets.QPushButton(self.resMain)
        self.resButton.setObjectName("resButton")
        self.verticalLayout_3.addWidget(self.resButton)
        self.verticalLayout_4.addWidget(self.resMain)
        self.allTabs.addTab(self.research, "")
        self.news = QtWidgets.QWidget()
        self.news.setObjectName("news")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.news)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newsMain = QtWidgets.QWidget(self.news)
        self.newsMain.setObjectName("newsMain")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.newsMain)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.newsScroll = QtWidgets.QScrollArea(self.newsMain)
        self.newsScroll.setWidgetResizable(True)
        self.newsScroll.setObjectName("newsScroll")
        self.newsScrollContents = QtWidgets.QWidget()
        self.newsScrollContents.setGeometry(QtCore.QRect(0, 0, 781, 467))
        self.newsScrollContents.setObjectName("newsScrollContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.newsScrollContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.newsText = QtWidgets.QTextBrowser(self.newsScrollContents)
        self.newsText.setOpenExternalLinks(True)
        self.newsText.setObjectName("newsText")
        self.verticalLayout_5.addWidget(self.newsText)
        self.newsScroll.setWidget(self.newsScrollContents)
        self.verticalLayout_6.addWidget(self.newsScroll)
        self.newsButton = QtWidgets.QPushButton(self.newsMain)
        self.newsButton.setObjectName("newsButton")
        self.verticalLayout_6.addWidget(self.newsButton)
        self.horizontalLayout.addWidget(self.newsMain)
        self.allTabs.addTab(self.news, "")
        self.videos = QtWidgets.QWidget()
        self.videos.setObjectName("videos")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.videos)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.videos)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 516))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.videoText = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.videoText.setOpenExternalLinks(True)
        self.videoText.setObjectName("videoText")
        self.verticalLayout_8.addWidget(self.videoText)
        self.videoInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.videoInput.setObjectName("videoInput")
        self.verticalLayout_8.addWidget(self.videoInput)
        self.videoButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.videoButton.setObjectName("videoButton")
        self.verticalLayout_8.addWidget(self.videoButton)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.allTabs.addTab(self.videos, "")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.about)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.aboutText = QtWidgets.QTextBrowser(self.about)
        self.aboutText.setEnabled(True)
        self.aboutText.setAutoFillBackground(False)
        self.aboutText.setReadOnly(True)
        self.aboutText.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.aboutText.setOpenExternalLinks(True)
        self.aboutText.setObjectName("aboutText")
        self.verticalLayout_7.addWidget(self.aboutText)
        self.allTabs.addTab(self.about, "")
        self.verticalLayout.addWidget(self.allTabs)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.allTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New-Feed"))
        self.resText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Research Papers</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\"># About</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    * This  module lets you search research papers from thefollowing sites :-</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    -- Ieeexplore</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    -- ScienceOpen</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    * Enter your query and hit </span><span style=\" font-size:16pt; font-style:italic;\">Search.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-style:italic;\">    * </span><span style=\" font-size:16pt;\">Wait for 10 seconds for the page to load.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))
        self.resInput.setPlaceholderText(_translate("MainWindow", "Enter Keywords Here...."))
        self.resButton.setText(_translate("MainWindow", "Search"))
        self.allTabs.setTabText(self.allTabs.indexOf(self.research), _translate("MainWindow", "Research Papers"))
        self.newsText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">News</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\"># About</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    * Get Latest news from around the globe..!!</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    * Click </span><span style=\" font-size:16pt; font-style:italic;\">Get News .</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-style:italic;\">    * </span><span style=\" font-size:16pt;\">Wait for 10 seconds for the page to load.</span></p></body></html>"))
        self.newsButton.setText(_translate("MainWindow", "Get News"))
        self.allTabs.setTabText(self.allTabs.indexOf(self.news), _translate("MainWindow", "News"))
        self.videoText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Videos</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">#About</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    * Search for your youtube queries and get releveant results.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    * Enter your query and hit </span><span style=\" font-size:16pt; font-style:italic;\">Search.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-style:italic;\">    * </span><span style=\" font-size:16pt;\">Wait for 10 seconds for the page to load.</span></p></body></html>"))
        self.videoButton.setText(_translate("MainWindow", "Search"))
        self.allTabs.setTabText(self.allTabs.indexOf(self.videos), _translate("MainWindow", "Videos"))
        self.about.setAccessibleName(_translate("MainWindow", "Info"))
        self.aboutText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">New-Feed</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"># About:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    New-Feed provides a single platform for all your research content searching </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    such as videos, research papers etc.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    Its simple and distraction free. It only uses basic text and html to display data.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"># Made By:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    1. Shubham Arya</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    2. Shubham Dixit</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    3. Sudeep Dalai </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"># Contribute:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">   This is an opensource project under the GNU-Open source Licence.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">   You can contribute to this project </span><a href=\"https://github.com/mrjoker05/New-Feed.git\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">here</span></a></p></body></html>"))
        self.allTabs.setTabText(self.allTabs.indexOf(self.about), _translate("MainWindow", "Info"))
        self.resButton.clicked.connect(self.clickRes)
        self.newsButton.clicked.connect(self.clickNews)
        self.videoButton.clicked.connect(self.clickVid)

    def clickNews(self):
        NW.getNews();
        main = open('./Data/news.html')
        self.newsText.setHtml(main.read())
        main.close()

    def clickRes(self):
                query = self.resInput.text()
                print("Searching for: "+ query)
                RS.ieeeSite(query)
                RS.scOpen(query)
                main = open('./Data/ResearchPapers.html')
                self.resText.setHtml(main.read())
                main.close()

    def clickVid(self):
                query = self.videoInput.text()
                print("Searching for: "+ query)
                VD.getVideo(query)
                main = open('./Data/Video.html')
                self.videoText.setHtml(main.read())
                main.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

