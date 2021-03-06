import sqlite3
from datetime import datetime, timedelta

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from dateutil.relativedelta import relativedelta
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 637.5)
        MainWindow.setMinimumSize(QtCore.QSize(1125, 637.5))
        MainWindow.setMaximumSize(QtCore.QSize(1125, 637.5))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.top_menu_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_menu_frame.setGeometry(QtCore.QRect(0, 0, 1125, 70))
        self.top_menu_frame.setMinimumSize(QtCore.QSize(1125, 52.5))
        self.top_menu_frame.setMaximumSize(QtCore.QSize(1125, 52.5))
        self.top_menu_frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.top_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_menu_frame.setObjectName("top_menu_frame")
        self.logo = QtWidgets.QLabel(self.top_menu_frame)
        self.logo.setGeometry(QtCore.QRect(15, 11.25, 112.5, 30))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/images/images/logo.svg"))
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 52.5, 300, 585))
        self.frame.setStyleSheet("background-color: rgb(240, 10, 70);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(22.5, 22.5, 225, 520))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.contracts_search = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contracts_search.sizePolicy().hasHeightForWidth())
        self.contracts_search.setSizePolicy(sizePolicy)
        self.contracts_search.setMinimumSize(QtCore.QSize(0, 22.5))
        self.contracts_search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contracts_search.setText("")
        self.contracts_search.setObjectName("contracts_search")
        # self.horizontalLayout.addWidget(self.contracts_search)
        self.search_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.search_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "background-image: url(:/images/images/search_icon.png);\n"
                                      "background-position: center;\n"
                                      "background-repeat: no-repeat;\n"
                                      "")
        self.search_btn.setText("")
        self.search_btn.setObjectName("search_btn")
        # self.horizontalLayout.addWidget(self.search_btn)
        self.contracts_filter = QtWidgets.QPushButton(self.layoutWidget)
        self.contracts_filter.setStyleSheet("background-color: white;")
        self.contracts_filter.setObjectName("contracts_filter")
        # self.horizontalLayout.addWidget(self.contracts_filter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 252.75, 508.5))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.dashboard_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.dashboard_btn.sizePolicy().hasHeightForWidth())
        # self.dashboard_btn.setSizePolicy(sizePolicy)
        # self.dashboard_btn.setMinimumSize(QtCore.QSize(0, 30))
        # self.dashboard_btn.setMaximumSize(QtCore.QSize(16777215, 56.25))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.dashboard_btn.setFont(font)
        # self.dashboard_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.dashboard_btn.setObjectName("dashboard_btn")
        # self.verticalLayout.addWidget(self.dashboard_btn)
        self.contracts_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contracts_btn.sizePolicy().hasHeightForWidth())
        self.contracts_btn.setSizePolicy(sizePolicy)
        self.contracts_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.contracts_btn.setMaximumSize(QtCore.QSize(16777215, 56.25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.contracts_btn.setFont(font)
        self.contracts_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contracts_btn.setObjectName("contracts_btn")
        self.verticalLayout.addWidget(self.contracts_btn)
        self.people_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.people_btn.sizePolicy().hasHeightForWidth())
        self.people_btn.setSizePolicy(sizePolicy)
        self.people_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.people_btn.setMaximumSize(QtCore.QSize(16777215, 56.25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.people_btn.setFont(font)
        self.people_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.people_btn.setObjectName("people_btn")
        self.verticalLayout.addWidget(self.people_btn)
        self.companies_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companies_btn.sizePolicy().hasHeightForWidth())
        self.companies_btn.setSizePolicy(sizePolicy)
        self.companies_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.companies_btn.setMaximumSize(QtCore.QSize(16777215, 56.25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.companies_btn.setFont(font)
        self.companies_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.companies_btn.setObjectName("companies_btn")
        self.verticalLayout.addWidget(self.companies_btn)
        self.reminders_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reminders_btn.sizePolicy().hasHeightForWidth())
        self.reminders_btn.setSizePolicy(sizePolicy)
        self.reminders_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.reminders_btn.setMaximumSize(QtCore.QSize(16777215, 56.25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reminders_btn.setFont(font)
        self.reminders_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reminders_btn.setObjectName("reminders_btn")
        self.verticalLayout.addWidget(self.reminders_btn)
        self.risks_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.risks_btn.sizePolicy().hasHeightForWidth())
        self.risks_btn.setSizePolicy(sizePolicy)
        self.risks_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.risks_btn.setMaximumSize(QtCore.QSize(16777215, 56.25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.risks_btn.setFont(font)
        self.risks_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.risks_btn.setObjectName("risks_btn")
        self.verticalLayout.addWidget(self.risks_btn)
        self.todos_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.todos_btn.sizePolicy().hasHeightForWidth())
        self.todos_btn.setSizePolicy(sizePolicy)
        self.todos_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.todos_btn.setMaximumSize(QtCore.QSize(16777215, 56.25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.todos_btn.setFont(font)
        self.todos_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.todos_btn.setObjectName("todos_btn")
        self.verticalLayout.addWidget(self.todos_btn)
        self.library_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.library_btn.sizePolicy().hasHeightForWidth())
        self.library_btn.setSizePolicy(sizePolicy)
        self.library_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.library_btn.setMaximumSize(QtCore.QSize(16777215, 56.25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.library_btn.setFont(font)
        self.library_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.library_btn.setObjectName("library_btn")
        self.verticalLayout.addWidget(self.library_btn)
        # self.reports_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.reports_btn.sizePolicy().hasHeightForWidth())
        # self.reports_btn.setSizePolicy(sizePolicy)
        # self.reports_btn.setMinimumSize(QtCore.QSize(0, 30))
        # self.reports_btn.setMaximumSize(QtCore.QSize(16777215, 56.25))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.reports_btn.setFont(font)
        # self.reports_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.reports_btn.setObjectName("reports_btn")
        # self.verticalLayout.addWidget(self.reports_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(300, 52.5, 825, 585))
        self.main_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.main_widget = QtWidgets.QStackedWidget(self.main_frame)
        self.main_widget.setGeometry(QtCore.QRect(0, 0, 828, 585))
        self.main_widget.setMaximumSize(QtCore.QSize(828, 1125))
        self.main_widget.setAutoFillBackground(False)
        self.main_widget.setStyleSheet("")
        self.main_widget.setObjectName("main_widget")
        self.dashboard_page = QtWidgets.QWidget()
        self.dashboard_page.setObjectName("dashboard_page")
        self.dashboard_lb = QtWidgets.QLabel(self.dashboard_page)
        self.dashboard_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dashboard_lb.setFont(font)
        self.dashboard_lb.setObjectName("dashboard_lb")
        self.main_widget.addWidget(self.dashboard_page)
        self.contracts_page = QtWidgets.QWidget()
        self.contracts_page.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.contracts_page.setObjectName("contracts_page")
        self.contracts_lb = QtWidgets.QLabel(self.contracts_page)
        self.contracts_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.contracts_lb.setFont(font)
        self.contracts_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.contracts_lb.setObjectName("contracts_lb")
        self.contracts_frame = QtWidgets.QFrame(self.contracts_page)
        self.contracts_frame.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.contracts_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contracts_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contracts_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contracts_frame.setObjectName("contracts_frame")
        self.layoutWidget4 = QtWidgets.QWidget(self.contracts_frame)
        self.layoutWidget4.setGeometry(QtCore.QRect(9, 2, 765, 487.5))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.contract_type_menu = QtWidgets.QComboBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_type_menu.setFont(font)
        self.contract_type_menu.setStyleSheet("background-color: rgb(255,255,255);\n"
                                              "")
        self.contract_type_menu.setObjectName("contract_type_menu")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.contract_type_menu.addItem("")
        self.horizontalLayout_65.addWidget(self.contract_type_menu)
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem1)
        self.edit_contract_btn = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_contract_btn.setFont(font)
        self.edit_contract_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.edit_contract_btn.setObjectName("edit_contract_btn")
        self.horizontalLayout_64.addWidget(self.edit_contract_btn)
        self.delete_contract_btn = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_contract_btn.setFont(font)
        self.delete_contract_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.delete_contract_btn.setObjectName("delete_contract_btn")
        self.horizontalLayout_64.addWidget(self.delete_contract_btn)
        self.archive_contract_btn = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archive_contract_btn.setFont(font)
        self.archive_contract_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.archive_contract_btn.setObjectName("archive_contract_btn")
        self.horizontalLayout_64.addWidget(self.archive_contract_btn)
        self.favorite_contract_btn = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.favorite_contract_btn.setFont(font)
        self.favorite_contract_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.favorite_contract_btn.setObjectName("favorite_contract_btn")
        self.horizontalLayout_64.addWidget(self.favorite_contract_btn)
        self.horizontalLayout_65.addLayout(self.horizontalLayout_64)
        self.verticalLayout_51.addLayout(self.horizontalLayout_65)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.contract_id_search = QtWidgets.QLineEdit(self.layoutWidget4)
        self.contract_id_search.setPlaceholderText('Search Id')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_id_search.setFont(font)
        self.contract_id_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.contract_id_search.setText("")
        self.contract_id_search.setObjectName("contract_id_search")
        self.horizontalLayout_34.addWidget(self.contract_id_search)
        self.contract_title_search = QtWidgets.QLineEdit(self.layoutWidget4)
        self.contract_title_search.setPlaceholderText('Search Title')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_title_search.setFont(font)
        self.contract_title_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.contract_title_search.setText("")
        self.contract_title_search.setObjectName("contract_title_search")
        self.horizontalLayout_34.addWidget(self.contract_title_search)
        self.contract_type_search = QtWidgets.QLineEdit(self.layoutWidget4)
        self.contract_type_search.setPlaceholderText('Search Type')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_type_search.setFont(font)
        self.contract_type_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.contract_type_search.setText("")
        self.contract_type_search.setObjectName("contract_type_search")
        self.horizontalLayout_34.addWidget(self.contract_type_search)
        self.contract_classificatiion_type = QtWidgets.QLineEdit(self.layoutWidget4)
        self.contract_classificatiion_type.setPlaceholderText('Search Classification')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_classificatiion_type.setFont(font)
        self.contract_classificatiion_type.setStyleSheet("background-color: rgb(255,255,255)")
        self.contract_classificatiion_type.setText("")
        self.contract_classificatiion_type.setObjectName("contract_classificatiion_type")
        self.horizontalLayout_34.addWidget(self.contract_classificatiion_type)
        self.contract_start_type = QtWidgets.QLineEdit(self.layoutWidget4)
        self.contract_start_type.setPlaceholderText('Search Start Date')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_start_type.setFont(font)
        self.contract_start_type.setStyleSheet("background-color: rgb(255,255,255)")
        self.contract_start_type.setText("")
        self.contract_start_type.setObjectName("contract_start_type")
        self.horizontalLayout_34.addWidget(self.contract_start_type)
        self.contract_end_search = QtWidgets.QLineEdit(self.layoutWidget4)
        self.contract_end_search.setPlaceholderText('Search End Date')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_end_search.setFont(font)
        self.contract_end_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.contract_end_search.setText("")
        self.contract_end_search.setObjectName("contract_end_search")
        self.horizontalLayout_34.addWidget(self.contract_end_search)
        self.contract_value_search = QtWidgets.QLineEdit(self.layoutWidget4)
        self.contract_value_search.setPlaceholderText('Search Value')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_value_search.setFont(font)
        self.contract_value_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.contract_value_search.setText("")
        self.contract_value_search.setObjectName("contract_value_search")
        self.horizontalLayout_34.addWidget(self.contract_value_search)
        self.contract_status_menu = QtWidgets.QComboBox(self.layoutWidget4)
        self.contract_status_menu.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_status_menu.setFont(font)
        self.contract_status_menu.setStyleSheet("background-color: rgb(255,255,255)")
        self.contract_status_menu.setObjectName("contract_status_menu")
        self.contract_status_menu.addItem("")
        self.contract_status_menu.addItem("")
        self.contract_status_menu.addItem("")
        self.contract_status_menu.addItem("")
        self.contract_status_menu.addItem("")
        self.contract_status_menu.addItem("")
        self.contract_status_menu.addItem("")
        self.horizontalLayout_34.addWidget(self.contract_status_menu)
        self.verticalLayout_51.addLayout(self.horizontalLayout_34)

        # Contracts Tree
        self.contracts_tree = QtWidgets.QTreeView(self.layoutWidget4)
        self.update_contracts()
        self.contracts_tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contracts_tree.setFont(font)
        self.contracts_tree.setStyleSheet("background-color: rgb(255,255,255)")
        self.contracts_tree.setObjectName("contracts_tree")
        self.contracts_tree.setModel(self.contract_model)
        self.contracts_tree.setAlternatingRowColors(True)
        self.contracts_tree.setColumnWidth(0, 125 * .75)
        self.contracts_tree.setColumnWidth(1, 135 * .75)
        self.contracts_tree.setColumnWidth(2, 130 * .75)
        self.contracts_tree.setColumnWidth(3, 135 * .75)
        self.contracts_tree.setColumnWidth(4, 134 * .75)
        self.contracts_tree.setColumnWidth(5, 133 * .75)
        self.contracts_tree.setColumnWidth(6, 82 * .75)
        self.contracts_tree.setColumnWidth(7, 34 * .75)
        self.contracts_tree.setColumnWidth(8, 55 * .75)
        self.verticalLayout_51.addWidget(self.contracts_tree)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem2)
        # self.previous_contracts = QtWidgets.QPushButton(self.layoutWidget4)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.previous_contracts.setFont(font)
        # self.previous_contracts.setStyleSheet("background-color: rgb(255,255,255)")
        # self.previous_contracts.setObjectName("previous_contracts")
        # self.horizontalLayout_33.addWidget(self.previous_contracts)
        # self.next_contracts = QtWidgets.QPushButton(self.layoutWidget4)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.next_contracts.setFont(font)
        # self.next_contracts.setStyleSheet("background-color: rgb(255,255,255)")
        # self.next_contracts.setObjectName("next_contracts")
        # self.horizontalLayout_33.addWidget(self.next_contracts)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem3)
        self.verticalLayout_51.addLayout(self.horizontalLayout_33)
        self.layoutWidget5 = QtWidgets.QWidget(self.contracts_page)
        self.layoutWidget5.setGeometry(QtCore.QRect(585, 15, 221.25, 22.5))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.new_contract = QtWidgets.QPushButton(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_contract.setFont(font)
        self.new_contract.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.new_contract.setObjectName("new_contract")
        self.horizontalLayout_63.addWidget(self.new_contract)
        self.export_contracts = QtWidgets.QPushButton(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.export_contracts.setFont(font)
        self.export_contracts.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.export_contracts.setObjectName("export_contracts")
        self.horizontalLayout_63.addWidget(self.export_contracts)
        # self.print_contracts = QtWidgets.QPushButton(self.layoutWidget5)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.print_contracts.setFont(font)
        # self.print_contracts.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.print_contracts.setObjectName("print_contracts")
        # self.horizontalLayout_63.addWidget(self.print_contracts)
        self.main_widget.addWidget(self.contracts_page)
        self.new_contract_page = QtWidgets.QWidget()
        self.new_contract_page.setStyleSheet("")
        self.new_contract_page.setObjectName("new_contract_page")
        self.new_contract_lb = QtWidgets.QLabel(self.new_contract_page)
        self.new_contract_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.new_contract_lb.setFont(font)
        self.new_contract_lb.setStyleSheet("")
        self.new_contract_lb.setObjectName("new_contract_lb")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.new_contract_page)
        self.scrollArea_8.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.scrollArea_8.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 780, 495))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_30.setSpacing(7)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_97 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_97.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_97.setFont(font)
        self.label_97.setText("")
        self.label_97.setObjectName("label_97")
        self.gridLayout_8.addWidget(self.label_97, 8, 0, 1, 1)
        self.label_86 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_86.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_86.setFont(font)
        self.label_86.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_86.setObjectName("label_86")
        self.gridLayout_8.addWidget(self.label_86, 3, 0, 1, 1)

        # Contract Master
        self.contract_master = QtWidgets.QComboBox(self.scrollAreaWidgetContents_8)
        self.contract_master.addItem('0 - No Master Contract')
        for contract in self.contract_list():
            self.contract_master.addItem(contract)
        self.contract_master.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_master.setFont(font)
        self.contract_master.setAutoFillBackground(False)
        self.contract_master.setObjectName("contract_master")
        self.gridLayout_8.addWidget(self.contract_master, 5, 6, 1, 1)

        # Contract Parties
        self.contract_parties = QtWidgets.QTreeView(self.scrollAreaWidgetContents_8)
        self.update_parties()
        self.contract_parties.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.contract_parties.setModel(self.contract_party_model)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_parties.setFont(font)
        self.contract_parties.setAutoFillBackground(False)
        self.contract_parties.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: rgb(0,0,0)")
        self.contract_parties.setColumnWidth(0, 30)
        self.contract_parties.setObjectName("contract_parties")
        self.gridLayout_8.addWidget(self.contract_parties, 7, 3, 1, 1)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.add_party = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_party.setFont(font)
        self.add_party.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                     "color: rgb(0,0,0)")
        self.add_party.setObjectName("add_party")
        self.verticalLayout_32.addWidget(self.add_party)
        self.open_party = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.open_party.setFont(font)
        self.open_party.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                      "color: rgb(0,0,0)")
        self.open_party.setObjectName("open_party")
        self.verticalLayout_32.addWidget(self.open_party)
        self.delete_party = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_party.setFont(font)
        self.delete_party.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                        "color: rgb(0,0,0)")
        self.delete_party.setObjectName("delete_party")
        self.verticalLayout_32.addWidget(self.delete_party)
        self.gridLayout_8.addLayout(self.verticalLayout_32, 7, 4, 1, 1)
        self.contract_category = QtWidgets.QComboBox(self.scrollAreaWidgetContents_8)
        self.contract_category.addItem('Not Selected')
        self.contract_category.addItem('Common Commodities')
        self.contract_category.addItem('Construction')
        self.contract_category.addItem('Energy & Utilites')
        self.contract_category.addItem('Facilities')
        self.contract_category.addItem('Fuel, Lubricant & Gas')
        self.contract_category.addItem('ICT')
        self.contract_category.addItem('Logistics')
        self.contract_category.addItem('Marketing & Media')
        self.contract_category.addItem('Medical Supplies')
        self.contract_category.addItem('Office Solutions')
        self.contract_category.addItem('Personnel Related')
        self.contract_category.addItem('Professional Services')
        self.contract_category.addItem('Social Care')
        self.contract_category.addItem('Travel')
        self.contract_category.addItem('Vehicles')
        self.contract_category.addItem('Waste Management')
        self.contract_category.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_category.setFont(font)
        self.contract_category.setAutoFillBackground(False)
        self.contract_category.setObjectName("contract_category")
        self.gridLayout_8.addWidget(self.contract_category, 3, 3, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_74.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_74.setFont(font)
        self.label_74.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_74.setObjectName("label_74")
        self.gridLayout_8.addWidget(self.label_74, 4, 0, 1, 1)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.term_none = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_8)
        self.term_none.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.term_none.setFont(font)
        self.term_none.setStyleSheet("")
        self.term_none.setObjectName("term_none")
        self.horizontalLayout_37.addWidget(self.term_none)
        self.term_fixed = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.term_fixed.setFont(font)
        self.term_fixed.setStyleSheet("")
        self.term_fixed.setObjectName("term_fixed")
        self.horizontalLayout_37.addWidget(self.term_fixed)
        self.term_recurring = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.term_recurring.setFont(font)
        self.term_recurring.setStyleSheet("")
        self.term_recurring.setObjectName("term_recurring")
        self.horizontalLayout_37.addWidget(self.term_recurring)
        self.term_rolling = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.term_rolling.setFont(font)
        self.term_rolling.setStyleSheet("")
        self.term_rolling.setObjectName("term_rolling")
        self.horizontalLayout_37.addWidget(self.term_rolling)
        self.gridLayout_8.addLayout(self.horizontalLayout_37, 11, 3, 1, 1)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.contract_start = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.contract_start.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_start.setFont(font)
        self.contract_start.setAutoFillBackground(False)
        self.contract_start.setObjectName("contract_start")
        self.horizontalLayout_38.addWidget(self.contract_start)
        self.contract_start_btn = QtWidgets.QToolButton(self.scrollAreaWidgetContents_8)
        self.contract_start_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_start_btn.setFont(font)
        self.contract_start_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contract_start_btn.setObjectName("contract_start_btn")
        self.horizontalLayout_38.addWidget(self.contract_start_btn)
        self.gridLayout_8.addLayout(self.horizontalLayout_38, 11, 6, 1, 1)
        self.label_98 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_98.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_98.setFont(font)
        self.label_98.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_98.setObjectName("label_98")
        self.gridLayout_8.addWidget(self.label_98, 14, 4, 1, 1)
        self.label_91 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_91.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_91.setFont(font)
        self.label_91.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_91.setObjectName("label_91")
        self.gridLayout_8.addWidget(self.label_91, 3, 4, 1, 1)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.contract_cancel = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.contract_cancel.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_cancel.setFont(font)
        self.contract_cancel.setAutoFillBackground(False)
        self.contract_cancel.setObjectName("contract_cancel")
        self.horizontalLayout_36.addWidget(self.contract_cancel)
        self.contract_cancel_btn = QtWidgets.QToolButton(self.scrollAreaWidgetContents_8)
        self.contract_cancel_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_cancel_btn.setFont(font)
        self.contract_cancel_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contract_cancel_btn.setObjectName("contract_cancel_btn")
        self.horizontalLayout_36.addWidget(self.contract_cancel_btn)
        self.gridLayout_8.addLayout(self.horizontalLayout_36, 14, 3, 1, 1)
        self.contract_value = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.contract_value.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_value.setFont(font)
        self.contract_value.setAutoFillBackground(False)
        self.contract_value.setObjectName("contract_value")
        self.gridLayout_8.addWidget(self.contract_value, 9, 3, 1, 1)
        self.label_89 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_89.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_89.setFont(font)
        self.label_89.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_89.setObjectName("label_89")
        self.gridLayout_8.addWidget(self.label_89, 13, 4, 1, 1)
        self.label_78 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_78.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_78.setFont(font)
        self.label_78.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_78.setObjectName("label_78")
        self.gridLayout_8.addWidget(self.label_78, 14, 0, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_75.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_75.setFont(font)
        self.label_75.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_75.setObjectName("label_75")
        self.gridLayout_8.addWidget(self.label_75, 1, 4, 1, 1)
        self.label_94 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_94.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_94.setFont(font)
        self.label_94.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_94.setObjectName("label_94")
        self.gridLayout_8.addWidget(self.label_94, 1, 0, 1, 1)
        self.label_92 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_92.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_92.setFont(font)
        self.label_92.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_92.setObjectName("label_92")
        self.gridLayout_8.addWidget(self.label_92, 11, 0, 1, 1)
        self.label_95 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_95.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_95.setFont(font)
        self.label_95.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_95.setObjectName("label_95")
        self.gridLayout_8.addWidget(self.label_95, 11, 4, 1, 1)
        self.label_96 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_96.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_96.setFont(font)
        self.label_96.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_96.setObjectName("label_96")
        self.gridLayout_8.addWidget(self.label_96, 7, 0, 1, 1)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.contract_review = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.contract_review.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_review.setFont(font)
        self.contract_review.setAutoFillBackground(False)
        self.contract_review.setObjectName("contract_review")
        self.horizontalLayout_35.addWidget(self.contract_review)
        self.contract_review_btn = QtWidgets.QToolButton(self.scrollAreaWidgetContents_8)
        self.contract_review_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_review_btn.setFont(font)
        self.contract_review_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contract_review_btn.setObjectName("contract_review_btn")
        self.horizontalLayout_35.addWidget(self.contract_review_btn)
        self.gridLayout_8.addLayout(self.horizontalLayout_35, 13, 6, 1, 1)
        self.contract_currency = QtWidgets.QComboBox(self.scrollAreaWidgetContents_8)
        self.contract_currency.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_currency.setFont(font)
        self.contract_currency.setAutoFillBackground(False)
        self.contract_currency.setObjectName("contract_currency")
        self.contract_currency.addItem("")
        self.contract_currency.addItem("")
        self.contract_currency.addItem("")
        self.gridLayout_8.addWidget(self.contract_currency, 9, 6, 1, 1)
        self.label_93 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_93.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_93.setFont(font)
        self.label_93.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_93.setObjectName("label_93")
        self.gridLayout_8.addWidget(self.label_93, 4, 4, 1, 1)
        self.contract_extension = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contract_extension.sizePolicy().hasHeightForWidth())
        self.contract_extension.setSizePolicy(sizePolicy)
        self.contract_extension.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_extension.setFont(font)
        self.contract_extension.setAutoFillBackground(False)
        self.contract_extension.setObjectName("contract_extension")
        self.gridLayout_8.addWidget(self.contract_extension, 14, 6, 1, 1)
        self.contract_id_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.contract_id_lb.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_id_lb.setFont(font)
        self.contract_id_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.contract_id_lb.setText("")
        self.contract_id_lb.setObjectName("contract_id_lb")
        self.gridLayout_8.addWidget(self.contract_id_lb, 0, 3, 1, 1)
        self.contract_status = QtWidgets.QComboBox(self.scrollAreaWidgetContents_8)
        self.contract_status.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_status.setFont(font)
        self.contract_status.setAutoFillBackground(False)
        self.contract_status.setObjectName("contract_status")
        self.contract_status.addItem("")
        self.contract_status.addItem("")
        self.contract_status.addItem("")
        self.contract_status.addItem("")
        self.contract_status.addItem("")
        self.contract_status.addItem("")
        self.contract_status.addItem("")
        self.gridLayout_8.addWidget(self.contract_status, 5, 3, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_80.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_80.setObjectName("label_80")
        self.gridLayout_8.addWidget(self.label_80, 5, 4, 1, 1)
        self.label_117 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_117.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_117.setFont(font)
        self.label_117.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(75, 75, 75);")
        self.label_117.setObjectName("label_117")
        self.gridLayout_8.addWidget(self.label_117, 13, 0, 1, 1)

        # Contract Type
        self.contract_type = QtWidgets.QComboBox(self.scrollAreaWidgetContents_8)
        types = self.fetch_query('SELECT name FROM contract_types')
        for type in types:
            self.contract_type.addItem(type)
        self.contract_type.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_type.setFont(font)
        self.contract_type.setAutoFillBackground(False)
        self.contract_type.setObjectName("contract_type")
        self.gridLayout_8.addWidget(self.contract_type, 1, 6, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_68.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_68.setFont(font)
        self.label_68.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_68.setObjectName("label_68")
        self.gridLayout_8.addWidget(self.label_68, 5, 0, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_76.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_76.setObjectName("label_76")
        self.gridLayout_8.addWidget(self.label_76, 9, 4, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_71.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_71.setFont(font)
        self.label_71.setText("")
        self.label_71.setObjectName("label_71")
        self.gridLayout_8.addWidget(self.label_71, 6, 0, 1, 1)
        self.contract_classification = QtWidgets.QComboBox(self.scrollAreaWidgetContents_8)
        self.contract_classification.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_classification.setFont(font)
        self.contract_classification.setAutoFillBackground(False)
        self.contract_classification.setObjectName("contract_classification")
        self.contract_classification.addItem("")
        self.contract_classification.addItem("")
        self.contract_classification.addItem("")
        self.gridLayout_8.addWidget(self.contract_classification, 3, 6, 1, 1)
        self.label_90 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_90.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_90.setObjectName("label_90")
        self.gridLayout_8.addWidget(self.label_90, 0, 0, 1, 1)
        self.contract_reference = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contract_reference.sizePolicy().hasHeightForWidth())
        self.contract_reference.setSizePolicy(sizePolicy)
        self.contract_reference.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_reference.setFont(font)
        self.contract_reference.setAutoFillBackground(False)
        self.contract_reference.setObjectName("contract_reference")
        self.gridLayout_8.addWidget(self.contract_reference, 4, 3, 1, 1)
        self.contract_account = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contract_account.sizePolicy().hasHeightForWidth())
        self.contract_account.setSizePolicy(sizePolicy)
        self.contract_account.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_account.setFont(font)
        self.contract_account.setAutoFillBackground(False)
        self.contract_account.setObjectName("contract_account")
        self.gridLayout_8.addWidget(self.contract_account, 4, 6, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_81.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_81.setFont(font)
        self.label_81.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(75, 75, 75);")
        self.label_81.setObjectName("label_81")
        self.gridLayout_8.addWidget(self.label_81, 9, 0, 1, 1)
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.contract_end = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.contract_end.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_end.setFont(font)
        self.contract_end.setAutoFillBackground(False)
        self.contract_end.setObjectName("contract_end")
        self.horizontalLayout_87.addWidget(self.contract_end)
        self.contract_end_btn = QtWidgets.QToolButton(self.scrollAreaWidgetContents_8)
        self.contract_end_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_end_btn.setFont(font)
        self.contract_end_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contract_end_btn.setObjectName("contract_end_btn")
        self.horizontalLayout_87.addWidget(self.contract_end_btn)
        self.gridLayout_8.addLayout(self.horizontalLayout_87, 13, 3, 1, 1)
        self.contract_title = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contract_title.sizePolicy().hasHeightForWidth())
        self.contract_title.setSizePolicy(sizePolicy)
        self.contract_title.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_title.setFont(font)
        self.contract_title.setAutoFillBackground(False)
        self.contract_title.setObjectName("contract_title")
        self.gridLayout_8.addWidget(self.contract_title, 1, 3, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_72.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_72.setFont(font)
        self.label_72.setText("")
        self.label_72.setObjectName("label_72")
        self.gridLayout_8.addWidget(self.label_72, 10, 0, 1, 1)
        self.verticalLayout_31.addLayout(self.gridLayout_8)
        self.label_99 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_99.setText("")
        self.label_99.setObjectName("label_99")
        self.verticalLayout_31.addWidget(self.label_99)
        self.label_100 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_100.setFont(font)
        self.label_100.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(75, 75, 75);")
        self.label_100.setObjectName("label_100")
        self.verticalLayout_31.addWidget(self.label_100)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.contract_description = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_8)
        self.contract_description.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_description.setFont(font)
        self.contract_description.setAutoFillBackground(False)
        self.contract_description.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "color: rgb(0,0,0)")
        self.contract_description.setObjectName("contract_description")
        self.horizontalLayout_39.addWidget(self.contract_description)
        self.verticalLayout_31.addLayout(self.horizontalLayout_39)
        self.verticalLayout_30.addLayout(self.verticalLayout_31)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_101 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_101.setText("")
        self.label_101.setObjectName("label_101")
        self.verticalLayout_33.addWidget(self.label_101)
        self.label_102 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_102.setFont(font)
        self.label_102.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(75, 75, 75);")
        self.label_102.setObjectName("label_102")
        self.verticalLayout_33.addWidget(self.label_102)

        # Contracts Attachments
        self.contract_attachments = QtWidgets.QTreeView(self.scrollAreaWidgetContents_8)
        self.update_contract_attachments()
        self.contract_attachments.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.contract_attachments.setModel(self.contract_attachment_model)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_attachments.setFont(font)
        self.contract_attachments.setAutoFillBackground(False)
        self.contract_attachments.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "color: rgb(0,0,0)")
        self.contract_attachments.setColumnWidth(0, 90)
        self.contract_attachments.setColumnWidth(1, 250)
        self.contract_attachments.setObjectName("contract_attachments")
        self.verticalLayout_33.addWidget(self.contract_attachments)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem4)
        self.contract_add_attachment = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_add_attachment.setFont(font)
        self.contract_add_attachment.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                                   "color: rgb(0,0,0)")
        self.contract_add_attachment.setObjectName("contract_add_attachment")
        self.horizontalLayout_40.addWidget(self.contract_add_attachment)
        self.contract_open_attachment = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_open_attachment.setFont(font)
        self.contract_open_attachment.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                                    "color: rgb(0,0,0)")
        self.contract_open_attachment.setObjectName("contract_open_attachment")
        self.horizontalLayout_40.addWidget(self.contract_open_attachment)
        self.contract_delete_attachment = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_delete_attachment.setFont(font)
        self.contract_delete_attachment.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                                      "color: rgb(0,0,0)")
        self.contract_delete_attachment.setObjectName("contract_delete_attachment")
        self.horizontalLayout_40.addWidget(self.contract_delete_attachment)
        self.verticalLayout_33.addLayout(self.horizontalLayout_40)
        self.verticalLayout_30.addLayout(self.verticalLayout_33)
        self.verticalLayout_29.addLayout(self.verticalLayout_30)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.layoutWidget_12 = QtWidgets.QWidget(self.new_contract_page)
        self.layoutWidget_12.setGeometry(QtCore.QRect(652.5, 22.5, 146.25, 22.5))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.save_contract = QtWidgets.QPushButton(self.layoutWidget_12)
        self.save_contract.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.save_contract.setObjectName("save_contract")
        self.horizontalLayout_41.addWidget(self.save_contract)
        self.cancel_contract = QtWidgets.QPushButton(self.layoutWidget_12)
        self.cancel_contract.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.cancel_contract.setObjectName("cancel_contract")
        self.horizontalLayout_41.addWidget(self.cancel_contract)
        self.main_widget.addWidget(self.new_contract_page)
        self.people_page = QtWidgets.QWidget()
        self.people_page.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.people_page.setObjectName("people_page")
        self.people_lb = QtWidgets.QLabel(self.people_page)
        self.people_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.people_lb.setFont(font)
        self.people_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.people_lb.setObjectName("people_lb")
        self.frame_3 = QtWidgets.QFrame(self.people_page)
        self.frame_3.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(9, 2, 765, 487.5))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.people_type_menu = QtWidgets.QComboBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.people_type_menu.setFont(font)
        self.people_type_menu.setStyleSheet("background-color: rgb(255,255,255);\n"
                                            "")
        self.people_type_menu.setObjectName("people_type_menu")
        self.people_type_menu.addItem("")
        self.people_type_menu.addItem("")
        self.people_type_menu.addItem("")
        self.people_type_menu.addItem("")
        self.people_type_menu.addItem("")
        self.people_type_menu.addItem("")
        self.people_type_menu.addItem("")
        self.people_type_menu.addItem("")
        self.people_type_menu.addItem("")
        self.people_type_menu.addItem("")
        self.people_type_menu.addItem("")
        self.horizontalLayout_66.addWidget(self.people_type_menu)
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_67.addItem(spacerItem5)
        self.edit_person_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_person_btn.setFont(font)
        self.edit_person_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.edit_person_btn.setObjectName("edit_person_btn")
        self.horizontalLayout_67.addWidget(self.edit_person_btn)
        self.delete_person_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_person_btn.setFont(font)
        self.delete_person_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.delete_person_btn.setObjectName("delete_person_btn")
        self.horizontalLayout_67.addWidget(self.delete_person_btn)
        self.archive_person_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archive_person_btn.setFont(font)
        self.archive_person_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.archive_person_btn.setObjectName("archive_person_btn")
        self.horizontalLayout_67.addWidget(self.archive_person_btn)
        self.favorite_person_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.favorite_person_btn.setFont(font)
        self.favorite_person_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.favorite_person_btn.setObjectName("favorite_person_btn")
        self.horizontalLayout_67.addWidget(self.favorite_person_btn)
        self.horizontalLayout_66.addLayout(self.horizontalLayout_67)
        self.verticalLayout_53.addLayout(self.horizontalLayout_66)
        self.horizontalLayout_68 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        self.person_id_search = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.person_id_search.setPlaceholderText('Search Id')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_id_search.setFont(font)
        self.person_id_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.person_id_search.setText("")
        self.person_id_search.setObjectName("person_id_search")
        self.horizontalLayout_68.addWidget(self.person_id_search)
        self.person_first_search = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.person_first_search.setPlaceholderText('Search First')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_first_search.setFont(font)
        self.person_first_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.person_first_search.setText("")
        self.person_first_search.setObjectName("person_first_search")
        self.horizontalLayout_68.addWidget(self.person_first_search)
        self.person_last_search = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.person_last_search.setPlaceholderText('Search Last')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_last_search.setFont(font)
        self.person_last_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.person_last_search.setText("")
        self.person_last_search.setObjectName("person_last_search")
        self.horizontalLayout_68.addWidget(self.person_last_search)
        self.person_email_search = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.person_email_search.setPlaceholderText('Search Email')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_email_search.setFont(font)
        self.person_email_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.person_email_search.setText("")
        self.person_email_search.setObjectName("person_email_search")
        self.horizontalLayout_68.addWidget(self.person_email_search)
        self.person_phone_search = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.person_phone_search.setPlaceholderText('Search Phone')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_phone_search.setFont(font)
        self.person_phone_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.person_phone_search.setText("")
        self.person_phone_search.setObjectName("person_phone_search")
        self.horizontalLayout_68.addWidget(self.person_phone_search)
        self.person_mobile_search = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.person_mobile_search.setPlaceholderText('Search Mobile')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_mobile_search.setFont(font)
        self.person_mobile_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.person_mobile_search.setText("")
        self.person_mobile_search.setObjectName("person_mobile_search")
        self.horizontalLayout_68.addWidget(self.person_mobile_search)
        self.person_job_search = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.person_job_search.setPlaceholderText('Search Job')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_job_search.setFont(font)
        self.person_job_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.person_job_search.setText("")
        self.person_job_search.setObjectName("person_job_search")
        self.horizontalLayout_68.addWidget(self.person_job_search)
        self.person_type_search = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.person_type_search.setPlaceholderText('Search Type')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_type_search.setFont(font)
        self.person_type_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.person_type_search.setText("")
        self.person_type_search.setObjectName("person_type_search")
        self.horizontalLayout_68.addWidget(self.person_type_search)
        self.verticalLayout_53.addLayout(self.horizontalLayout_68)

        # People Tree
        self.people_tree = QtWidgets.QTreeView(self.layoutWidget_2)
        self.update_people()
        self.people_tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.people_tree.setModel(self.person_model)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.people_tree.setFont(font)
        self.people_tree.setStyleSheet("background-color: rgb(255,255,255)")
        self.people_tree.setAlternatingRowColors(True)
        self.people_tree.setColumnWidth(0, 120 * .75)
        self.people_tree.setColumnWidth(1, 130 * .75)
        self.people_tree.setColumnWidth(2, 130 * .75)
        self.people_tree.setColumnWidth(3, 130 * .75)
        self.people_tree.setColumnWidth(4, 125 * .75)
        self.people_tree.setColumnWidth(5, 130 * .75)
        self.people_tree.setColumnWidth(6, 125 * .75)
        self.people_tree.setColumnWidth(7, 125 * .75)
        self.people_tree.setObjectName("people_tree")
        self.verticalLayout_53.addWidget(self.people_tree)
        self.horizontalLayout_69 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_69.addItem(spacerItem6)
        # self.previous_people = QtWidgets.QPushButton(self.layoutWidget_2)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.previous_people.setFont(font)
        # self.previous_people.setStyleSheet("background-color: rgb(255,255,255)")
        # self.previous_people.setObjectName("previous_people")
        # self.horizontalLayout_69.addWidget(self.previous_people)
        # self.next_people = QtWidgets.QPushButton(self.layoutWidget_2)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.next_people.setFont(font)
        # self.next_people.setStyleSheet("background-color: rgb(255,255,255)")
        # self.next_people.setObjectName("next_people")
        # self.horizontalLayout_69.addWidget(self.next_people)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_69.addItem(spacerItem7)
        self.verticalLayout_53.addLayout(self.horizontalLayout_69)
        self.layoutWidget_3 = QtWidgets.QWidget(self.people_page)
        self.layoutWidget_3.setGeometry(QtCore.QRect(585, 15, 221.25, 22.5))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_70 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_70.setObjectName("horizontalLayout_70")
        self.new_person = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_person.setFont(font)
        self.new_person.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.new_person.setObjectName("new_person")
        self.horizontalLayout_70.addWidget(self.new_person)
        self.export_people = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.export_people.setFont(font)
        self.export_people.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.export_people.setObjectName("export_people")
        self.horizontalLayout_70.addWidget(self.export_people)
        # self.print_people = QtWidgets.QPushButton(self.layoutWidget_3)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.print_people.setFont(font)
        # self.print_people.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.print_people.setObjectName("print_people")
        # self.horizontalLayout_70.addWidget(self.print_people)
        self.main_widget.addWidget(self.people_page)
        self.new_person_page = QtWidgets.QWidget()
        self.new_person_page.setObjectName("new_person_page")
        self.new_person_lb = QtWidgets.QLabel(self.new_person_page)
        self.new_person_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.new_person_lb.setFont(font)
        self.new_person_lb.setStyleSheet("")
        self.new_person_lb.setObjectName("new_person_lb")
        self.layoutWidget_13 = QtWidgets.QWidget(self.new_person_page)
        self.layoutWidget_13.setGeometry(QtCore.QRect(652.5, 22.5, 146.25, 22.5))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.layoutWidget_13)
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.save_person = QtWidgets.QPushButton(self.layoutWidget_13)
        self.save_person.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.save_person.setObjectName("save_person")
        self.horizontalLayout_42.addWidget(self.save_person)
        self.cancel_person = QtWidgets.QPushButton(self.layoutWidget_13)
        self.cancel_person.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.cancel_person.setObjectName("cancel_person")
        self.horizontalLayout_42.addWidget(self.cancel_person)
        self.scrollArea_9 = QtWidgets.QScrollArea(self.new_person_page)
        self.scrollArea_9.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.scrollArea_9.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 1039, 679))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout()
        self.verticalLayout_35.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_35.setSpacing(7)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_103 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_103.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_103.setFont(font)
        self.label_103.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_103.setObjectName("label_103")
        self.gridLayout_9.addWidget(self.label_103, 5, 5, 1, 1)
        self.label_104 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_104.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_104.setFont(font)
        self.label_104.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_104.setObjectName("label_104")
        self.gridLayout_9.addWidget(self.label_104, 1, 0, 1, 1)
        self.person_type = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.person_type.sizePolicy().hasHeightForWidth())
        self.person_type.setSizePolicy(sizePolicy)
        self.person_type.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_type.setFont(font)
        self.person_type.setAutoFillBackground(False)
        self.person_type.setObjectName("person_type")
        self.gridLayout_9.addWidget(self.person_type, 5, 7, 1, 1)

        # Person salutation
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.salutation_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_(
            "SELECT salutation FROM salutations")
        self.salutation_model.setQuery(query)
        db.close()

        self.salutation = QtWidgets.QComboBox(self.scrollAreaWidgetContents_9)
        self.salutation.setModel(self.salutation_model)
        self.salutation.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.salutation.setFont(font)
        self.salutation.setAutoFillBackground(False)
        self.salutation.setObjectName("salutation")
        self.gridLayout_9.addWidget(self.salutation, 1, 3, 1, 1)
        self.label_105 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_105.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_105.setFont(font)
        self.label_105.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_105.setObjectName("label_105")
        self.gridLayout_9.addWidget(self.label_105, 8, 5, 1, 1)
        self.label_106 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_106.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_106.setFont(font)
        self.label_106.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_106.setObjectName("label_106")
        self.gridLayout_9.addWidget(self.label_106, 4, 0, 1, 1)
        self.email = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy)
        self.email.setMinimumSize(QtCore.QSize(0, 35))
        self.email.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setAutoFillBackground(False)
        self.email.setObjectName("email")
        self.gridLayout_9.addWidget(self.email, 8, 3, 1, 1)
        self.phone = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        self.phone.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phone.setFont(font)
        self.phone.setAutoFillBackground(False)
        self.phone.setObjectName("phone")
        self.gridLayout_9.addWidget(self.phone, 7, 3, 1, 1)
        self.label_107 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_107.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_107.setFont(font)
        self.label_107.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_107.setObjectName("label_107")
        self.gridLayout_9.addWidget(self.label_107, 8, 0, 1, 1)
        self.person_id_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.person_id_lb.setMinimumSize(QtCore.QSize(0, 35))
        self.person_id_lb.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_id_lb.setFont(font)
        self.person_id_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.person_id_lb.setText("")
        self.person_id_lb.setObjectName("person_id_lb")
        self.gridLayout_9.addWidget(self.person_id_lb, 0, 3, 1, 1)
        self.label_108 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_108.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_108.setFont(font)
        self.label_108.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_108.setObjectName("label_108")
        self.gridLayout_9.addWidget(self.label_108, 7, 5, 1, 1)
        self.fax = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fax.sizePolicy().hasHeightForWidth())
        self.fax.setSizePolicy(sizePolicy)
        self.fax.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fax.setFont(font)
        self.fax.setAutoFillBackground(False)
        self.fax.setObjectName("fax")
        self.gridLayout_9.addWidget(self.fax, 8, 7, 1, 1)
        self.label_109 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_109.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_109.setFont(font)
        self.label_109.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_109.setObjectName("label_109")
        self.gridLayout_9.addWidget(self.label_109, 5, 0, 1, 1)
        self.last_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.last_name.sizePolicy().hasHeightForWidth())
        self.last_name.setSizePolicy(sizePolicy)
        self.last_name.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.last_name.setFont(font)
        self.last_name.setAutoFillBackground(False)
        self.last_name.setObjectName("last_name")
        self.gridLayout_9.addWidget(self.last_name, 3, 7, 1, 1)
        self.label_110 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_110.setMinimumSize(QtCore.QSize(0, 35))
        self.label_110.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_110.setFont(font)
        self.label_110.setText("")
        self.label_110.setObjectName("label_110")
        self.gridLayout_9.addWidget(self.label_110, 6, 0, 1, 1)

        # Person company
        ids = self.fetch_query('SELECT id FROM companies')
        names = self.fetch_query('SELECT name FROM companies')
        companies = []
        for company_id, name in zip(ids, names):
            comp = str(company_id) + ' - ' + str(name)
            companies.append(comp)

        self.company = QtWidgets.QComboBox(self.scrollAreaWidgetContents_9)
        self.company.addItem('0 - No Company')
        for item in companies:
            self.company.addItem(item)
        self.company.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company.setFont(font)
        self.company.setAutoFillBackground(False)
        self.company.setObjectName("company")
        self.gridLayout_9.addWidget(self.company, 5, 3, 1, 1)
        self.mobile = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        self.mobile.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mobile.setFont(font)
        self.mobile.setAutoFillBackground(False)
        self.mobile.setObjectName("mobile")
        self.gridLayout_9.addWidget(self.mobile, 7, 7, 1, 1)
        self.label_111 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_111.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_111.setFont(font)
        self.label_111.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_111.setObjectName("label_111")
        self.gridLayout_9.addWidget(self.label_111, 4, 5, 1, 1)
        self.label_112 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_112.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_112.setFont(font)
        self.label_112.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_112.setObjectName("label_112")
        self.gridLayout_9.addWidget(self.label_112, 3, 0, 1, 1)
        self.job = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.job.sizePolicy().hasHeightForWidth())
        self.job.setSizePolicy(sizePolicy)
        self.job.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.job.setFont(font)
        self.job.setAutoFillBackground(False)
        self.job.setObjectName("job")
        self.gridLayout_9.addWidget(self.job, 4, 7, 1, 1)
        self.first_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_name.sizePolicy().hasHeightForWidth())
        self.first_name.setSizePolicy(sizePolicy)
        self.first_name.setMinimumSize(QtCore.QSize(0, 35))
        self.first_name.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.first_name.setFont(font)
        self.first_name.setAutoFillBackground(False)
        self.first_name.setObjectName("first_name")
        self.gridLayout_9.addWidget(self.first_name, 3, 3, 1, 1)
        self.label_113 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_113.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_113.setFont(font)
        self.label_113.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_113.setObjectName("label_113")
        self.gridLayout_9.addWidget(self.label_113, 3, 5, 1, 1)
        self.label_114 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_114.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_114.setFont(font)
        self.label_114.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_114.setObjectName("label_114")
        self.gridLayout_9.addWidget(self.label_114, 7, 0, 1, 1)
        self.label_115 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_115.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_115.setFont(font)
        self.label_115.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_115.setObjectName("label_115")
        self.gridLayout_9.addWidget(self.label_115, 0, 0, 1, 1)
        self.gender = QtWidgets.QComboBox(self.scrollAreaWidgetContents_9)
        self.gender.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gender.setFont(font)
        self.gender.setAutoFillBackground(False)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gridLayout_9.addWidget(self.gender, 4, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem8, 9, 5, 1, 1)
        self.verticalLayout_36.addLayout(self.gridLayout_9)
        self.verticalLayout_35.addLayout(self.verticalLayout_36)
        self.verticalLayout_34.addLayout(self.verticalLayout_35)
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.main_widget.addWidget(self.new_person_page)
        self.companies_page = QtWidgets.QWidget()
        self.companies_page.setStyleSheet("background-color: rgb(75, 75, 75);\n"
                                          "")
        self.companies_page.setObjectName("companies_page")
        self.companies_lb = QtWidgets.QLabel(self.companies_page)
        self.companies_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.companies_lb.setFont(font)
        self.companies_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.companies_lb.setObjectName("companies_lb")
        self.frame_4 = QtWidgets.QFrame(self.companies_page)
        self.frame_4.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.layoutWidget_4 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_4.setGeometry(QtCore.QRect(9, 2, 765, 487.5))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.horizontalLayout_71 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.company_type_menu = QtWidgets.QComboBox(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_type_menu.setFont(font)
        self.company_type_menu.setStyleSheet("background-color: rgb(255,255,255);\n"
                                             "")
        self.company_type_menu.setObjectName("company_type_menu")
        self.company_type_menu.addItem("")
        self.company_type_menu.addItem("")
        self.company_type_menu.addItem("")
        self.company_type_menu.addItem("")
        self.company_type_menu.addItem("")
        self.company_type_menu.addItem("")
        self.company_type_menu.addItem("")
        self.company_type_menu.addItem("")
        self.company_type_menu.addItem("")
        self.horizontalLayout_71.addWidget(self.company_type_menu)
        self.horizontalLayout_72 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_72.setObjectName("horizontalLayout_72")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(spacerItem9)
        self.edit_company_btn = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_company_btn.setFont(font)
        self.edit_company_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.edit_company_btn.setObjectName("edit_company_btn")
        self.horizontalLayout_72.addWidget(self.edit_company_btn)
        self.delete_company_btn = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_company_btn.setFont(font)
        self.delete_company_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.delete_company_btn.setObjectName("delete_company_btn")
        self.horizontalLayout_72.addWidget(self.delete_company_btn)
        self.archive_company_btn = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archive_company_btn.setFont(font)
        self.archive_company_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.archive_company_btn.setObjectName("archive_company_btn")
        self.horizontalLayout_72.addWidget(self.archive_company_btn)
        self.favorite_company_btn = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.favorite_company_btn.setFont(font)
        self.favorite_company_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.favorite_company_btn.setObjectName("favorite_company_btn")
        self.horizontalLayout_72.addWidget(self.favorite_company_btn)
        self.horizontalLayout_71.addLayout(self.horizontalLayout_72)
        self.verticalLayout_54.addLayout(self.horizontalLayout_71)
        self.horizontalLayout_73 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_73.setObjectName("horizontalLayout_73")
        self.company_id_search = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.company_id_search.setPlaceholderText('Search Id')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_id_search.setFont(font)
        self.company_id_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.company_id_search.setText("")
        self.company_id_search.setObjectName("company_id_search")
        self.horizontalLayout_73.addWidget(self.company_id_search)
        self.company_name_search = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.company_name_search.setPlaceholderText('Search Name')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_name_search.setFont(font)
        self.company_name_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.company_name_search.setText("")
        self.company_name_search.setObjectName("company_name_search")
        self.horizontalLayout_73.addWidget(self.company_name_search)
        self.company_address_search = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.company_address_search.setPlaceholderText('Search Address')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_address_search.setFont(font)
        self.company_address_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.company_address_search.setText("")
        self.company_address_search.setObjectName("company_address_search")
        self.horizontalLayout_73.addWidget(self.company_address_search)
        self.company_city_search = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.company_city_search.setPlaceholderText('Search City')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_city_search.setFont(font)
        self.company_city_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.company_city_search.setText("")
        self.company_city_search.setObjectName("company_city_search")
        self.horizontalLayout_73.addWidget(self.company_city_search)
        self.company_state_search = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.company_state_search.setPlaceholderText('Search State')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_state_search.setFont(font)
        self.company_state_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.company_state_search.setText("")
        self.company_state_search.setObjectName("company_state_search")
        self.horizontalLayout_73.addWidget(self.company_state_search)
        self.company_zip_search = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.company_zip_search.setPlaceholderText('Search Zip')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_zip_search.setFont(font)
        self.company_zip_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.company_zip_search.setText("")
        self.company_zip_search.setObjectName("company_zip_search")
        self.horizontalLayout_73.addWidget(self.company_zip_search)
        self.company_country_search = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.company_country_search.setPlaceholderText('Search Country')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_country_search.setFont(font)
        self.company_country_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.company_country_search.setText("")
        self.company_country_search.setObjectName("company_country_search")
        self.horizontalLayout_73.addWidget(self.company_country_search)
        self.company_website_search = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.company_website_search.setPlaceholderText('Search Website')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_website_search.setFont(font)
        self.company_website_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.company_website_search.setText("")
        self.company_website_search.setObjectName("company_website_search")
        self.horizontalLayout_73.addWidget(self.company_website_search)
        self.verticalLayout_54.addLayout(self.horizontalLayout_73)

        # Companies Tree
        self.companies_tree = QtWidgets.QTreeView(self.layoutWidget_4)
        self.update_companies()
        self.companies_tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.companies_tree.setModel(self.company_model)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.companies_tree.setFont(font)
        self.companies_tree.setStyleSheet("background-color: rgb(255,255,255)")
        self.companies_tree.setAlternatingRowColors(True)
        self.companies_tree.setColumnWidth(0, 120 * .75)
        self.companies_tree.setColumnWidth(1, 130 * .75)
        self.companies_tree.setColumnWidth(2, 130 * .75)
        self.companies_tree.setColumnWidth(3, 128 * .75)
        self.companies_tree.setColumnWidth(4, 125 * .75)
        self.companies_tree.setColumnWidth(5, 128 * .75)
        self.companies_tree.setColumnWidth(6, 129 * .75)
        self.companies_tree.setColumnWidth(7, 55 * .75)
        self.companies_tree.setObjectName("companies_tree")
        self.verticalLayout_54.addWidget(self.companies_tree)
        self.horizontalLayout_74 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_74.setObjectName("horizontalLayout_74")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_74.addItem(spacerItem10)
        # self.previous_companies = QtWidgets.QPushButton(self.layoutWidget_4)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.previous_companies.setFont(font)
        # self.previous_companies.setStyleSheet("background-color: rgb(255,255,255)")
        # self.previous_companies.setObjectName("previous_companies")
        # self.horizontalLayout_74.addWidget(self.previous_companies)
        # self.next_companies = QtWidgets.QPushButton(self.layoutWidget_4)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.next_companies.setFont(font)
        # self.next_companies.setStyleSheet("background-color: rgb(255,255,255)")
        # self.next_companies.setObjectName("next_companies")
        # self.horizontalLayout_74.addWidget(self.next_companies)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_74.addItem(spacerItem11)
        self.verticalLayout_54.addLayout(self.horizontalLayout_74)
        self.layoutWidget_5 = QtWidgets.QWidget(self.companies_page)
        self.layoutWidget_5.setGeometry(QtCore.QRect(585, 15, 221.25, 22.5))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_75 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_75.setObjectName("horizontalLayout_75")
        self.new_company = QtWidgets.QPushButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_company.setFont(font)
        self.new_company.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.new_company.setObjectName("new_company")
        self.horizontalLayout_75.addWidget(self.new_company)
        self.export_companies = QtWidgets.QPushButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.export_companies.setFont(font)
        self.export_companies.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.export_companies.setObjectName("export_companies")
        self.horizontalLayout_75.addWidget(self.export_companies)
        # self.print_companies = QtWidgets.QPushButton(self.layoutWidget_5)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.print_companies.setFont(font)
        # self.print_companies.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.print_companies.setObjectName("print_companies")
        # self.horizontalLayout_75.addWidget(self.print_companies)
        self.main_widget.addWidget(self.companies_page)
        self.new_company_page = QtWidgets.QWidget()
        self.new_company_page.setObjectName("new_company_page")
        self.new_company_lb = QtWidgets.QLabel(self.new_company_page)
        self.new_company_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.new_company_lb.setFont(font)
        self.new_company_lb.setStyleSheet("")
        self.new_company_lb.setObjectName("new_company_lb")
        self.layoutWidget_14 = QtWidgets.QWidget(self.new_company_page)
        self.layoutWidget_14.setGeometry(QtCore.QRect(652.5, 22.5, 146.25, 22.5))
        self.layoutWidget_14.setObjectName("layoutWidget_14")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.layoutWidget_14)
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.save_company = QtWidgets.QPushButton(self.layoutWidget_14)
        self.save_company.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.save_company.setObjectName("save_company")
        self.horizontalLayout_43.addWidget(self.save_company)
        self.cancel_company = QtWidgets.QPushButton(self.layoutWidget_14)
        self.cancel_company.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.cancel_company.setObjectName("cancel_company")
        self.horizontalLayout_43.addWidget(self.cancel_company)
        self.scrollArea_10 = QtWidgets.QScrollArea(self.new_company_page)
        self.scrollArea_10.setGeometry(QtCore.QRect(22.5, 52.5, 780, 510))
        self.scrollArea_10.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setObjectName("scrollArea_10")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 780, 510))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_38.setSpacing(7)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.zip = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.zip.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.zip.setFont(font)
        self.zip.setAutoFillBackground(False)
        self.zip.setObjectName("zip")
        self.gridLayout_10.addWidget(self.zip, 5, 3, 1, 1)
        self.address_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.address_2.sizePolicy().hasHeightForWidth())
        self.address_2.setSizePolicy(sizePolicy)
        self.address_2.setMinimumSize(QtCore.QSize(0, 35))
        self.address_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.address_2.setFont(font)
        self.address_2.setAutoFillBackground(False)
        self.address_2.setObjectName("address_2")
        self.gridLayout_10.addWidget(self.address_2, 3, 7, 1, 1)
        self.company_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_name.sizePolicy().hasHeightForWidth())
        self.company_name.setSizePolicy(sizePolicy)
        self.company_name.setMinimumSize(QtCore.QSize(0, 35))
        self.company_name.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_name.setFont(font)
        self.company_name.setAutoFillBackground(False)
        self.company_name.setObjectName("company_name")
        self.gridLayout_10.addWidget(self.company_name, 1, 3, 1, 1)
        self.label_116 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_116.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_116.setFont(font)
        self.label_116.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_116.setObjectName("label_116")
        self.gridLayout_10.addWidget(self.label_116, 1, 5, 1, 1)
        self.label_125 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_125.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_125.setFont(font)
        self.label_125.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_125.setObjectName("label_125")
        self.gridLayout_10.addWidget(self.label_125, 5, 0, 1, 1)
        self.contact = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.contact.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contact.setFont(font)
        self.contact.setAutoFillBackground(False)
        self.contact.setObjectName("contact")
        self.gridLayout_10.addWidget(self.contact, 10, 3, 1, 1)
        self.label_126 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_126.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_126.setFont(font)
        self.label_126.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_126.setObjectName("label_126")
        self.gridLayout_10.addWidget(self.label_126, 7, 0, 1, 1)
        self.address_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.address_1.sizePolicy().hasHeightForWidth())
        self.address_1.setSizePolicy(sizePolicy)
        self.address_1.setMinimumSize(QtCore.QSize(0, 35))
        self.address_1.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.address_1.setFont(font)
        self.address_1.setAutoFillBackground(False)
        self.address_1.setObjectName("address_1")
        self.gridLayout_10.addWidget(self.address_1, 3, 3, 1, 1)
        self.label_127 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_127.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_127.setFont(font)
        self.label_127.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_127.setObjectName("label_127")
        self.gridLayout_10.addWidget(self.label_127, 1, 0, 1, 1)
        self.label_128 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_128.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_128.setFont(font)
        self.label_128.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_128.setObjectName("label_128")
        self.gridLayout_10.addWidget(self.label_128, 10, 0, 1, 1)
        self.company_id_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.company_id_lb.setMinimumSize(QtCore.QSize(0, 35))
        self.company_id_lb.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_id_lb.setFont(font)
        self.company_id_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.company_id_lb.setText("")
        self.company_id_lb.setObjectName("company_id_lb")
        self.gridLayout_10.addWidget(self.company_id_lb, 0, 3, 1, 1)
        self.label_129 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_129.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_129.setFont(font)
        self.label_129.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_129.setObjectName("label_129")
        self.gridLayout_10.addWidget(self.label_129, 3, 5, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem12, 11, 5, 1, 1)
        self.company_fax = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.company_fax.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_fax.setFont(font)
        self.company_fax.setAutoFillBackground(False)
        self.company_fax.setObjectName("company_fax")
        self.gridLayout_10.addWidget(self.company_fax, 10, 7, 1, 1)
        self.label_130 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_130.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_130.setFont(font)
        self.label_130.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_130.setObjectName("label_130")
        self.gridLayout_10.addWidget(self.label_130, 0, 0, 1, 1)
        self.label_131 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_131.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_131.setFont(font)
        self.label_131.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_131.setObjectName("label_131")
        self.gridLayout_10.addWidget(self.label_131, 10, 5, 1, 1)

        # Company segment
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.segment_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_(
            "SELECT segment FROM segments")
        self.segment_model.setQuery(query)
        db.close()

        self.segment = QtWidgets.QComboBox(self.scrollAreaWidgetContents_10)
        self.segment.setModel(self.segment_model)
        self.segment.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.segment.setFont(font)
        self.segment.setAutoFillBackground(False)
        self.segment.setObjectName("segment")
        self.gridLayout_10.addWidget(self.segment, 7, 3, 1, 1)
        self.website = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.website.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.website.setFont(font)
        self.website.setAutoFillBackground(False)
        self.website.setObjectName("website")
        self.gridLayout_10.addWidget(self.website, 9, 3, 1, 1)
        self.country = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.country.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.country.setFont(font)
        self.country.setAutoFillBackground(False)
        self.country.setObjectName("country")
        self.gridLayout_10.addWidget(self.country, 5, 7, 1, 1)
        self.label_132 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_132.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_132.setFont(font)
        self.label_132.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_132.setObjectName("label_132")
        self.gridLayout_10.addWidget(self.label_132, 3, 0, 1, 1)
        self.label_133 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_133.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_133.setFont(font)
        self.label_133.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_133.setObjectName("label_133")
        self.gridLayout_10.addWidget(self.label_133, 7, 5, 1, 1)
        self.label_134 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_134.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_134.setFont(font)
        self.label_134.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_134.setObjectName("label_134")
        self.gridLayout_10.addWidget(self.label_134, 5, 5, 1, 1)
        self.company_email = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.company_email.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_email.setFont(font)
        self.company_email.setAutoFillBackground(False)
        self.company_email.setObjectName("company_email")
        self.gridLayout_10.addWidget(self.company_email, 9, 7, 1, 1)
        self.label_135 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_135.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_135.setFont(font)
        self.label_135.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_135.setObjectName("label_135")
        self.gridLayout_10.addWidget(self.label_135, 9, 5, 1, 1)
        self.label_136 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_136.setMinimumSize(QtCore.QSize(0, 35))
        self.label_136.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_136.setFont(font)
        self.label_136.setText("")
        self.label_136.setObjectName("label_136")
        self.gridLayout_10.addWidget(self.label_136, 8, 0, 1, 1)
        self.label_137 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_137.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_137.setFont(font)
        self.label_137.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_137.setObjectName("label_137")
        self.gridLayout_10.addWidget(self.label_137, 9, 0, 1, 1)
        self.company_number = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_number.sizePolicy().hasHeightForWidth())
        self.company_number.setSizePolicy(sizePolicy)
        self.company_number.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_number.setFont(font)
        self.company_number.setAutoFillBackground(False)
        self.company_number.setObjectName("company_number")
        self.gridLayout_10.addWidget(self.company_number, 7, 7, 1, 1)

        # Company type
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.company_type_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_(
            "SELECT type FROM company_types")
        self.company_type_model.setQuery(query)
        db.close()

        self.company_type = QtWidgets.QComboBox(self.scrollAreaWidgetContents_10)
        self.company_type.setModel(self.company_type_model)
        self.company_type.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_type.setFont(font)
        self.company_type.setAutoFillBackground(False)
        self.company_type.setObjectName("company_type")
        self.gridLayout_10.addWidget(self.company_type, 1, 7, 1, 1)
        self.label_138 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_138.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_138.setFont(font)
        self.label_138.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_138.setObjectName("label_138")
        self.gridLayout_10.addWidget(self.label_138, 4, 0, 1, 1)
        self.label_139 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_139.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_139.setFont(font)
        self.label_139.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_139.setObjectName("label_139")
        self.gridLayout_10.addWidget(self.label_139, 4, 5, 1, 1)
        self.city = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city.sizePolicy().hasHeightForWidth())
        self.city.setSizePolicy(sizePolicy)
        self.city.setMinimumSize(QtCore.QSize(0, 35))
        self.city.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.city.setFont(font)
        self.city.setAutoFillBackground(False)
        self.city.setObjectName("city")
        self.gridLayout_10.addWidget(self.city, 4, 3, 1, 1)
        self.state = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state.sizePolicy().hasHeightForWidth())
        self.state.setSizePolicy(sizePolicy)
        self.state.setMinimumSize(QtCore.QSize(0, 35))
        self.state.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.state.setFont(font)
        self.state.setAutoFillBackground(False)
        self.state.setObjectName("state")
        self.gridLayout_10.addWidget(self.state, 4, 7, 1, 1)
        self.verticalLayout_39.addLayout(self.gridLayout_10)
        self.verticalLayout_38.addLayout(self.verticalLayout_39)
        self.verticalLayout_37.addLayout(self.verticalLayout_38)
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)
        self.main_widget.addWidget(self.new_company_page)
        self.reminders_page = QtWidgets.QWidget()
        self.reminders_page.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.reminders_page.setObjectName("reminders_page")
        self.reminder_lb = QtWidgets.QLabel(self.reminders_page)
        self.reminder_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reminder_lb.setFont(font)
        self.reminder_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.reminder_lb.setObjectName("reminder_lb")
        self.frame_5 = QtWidgets.QFrame(self.reminders_page)
        self.frame_5.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.layoutWidget_6 = QtWidgets.QWidget(self.frame_5)
        self.layoutWidget_6.setGeometry(QtCore.QRect(9, 2, 765, 487.5))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.horizontalLayout_76 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_76.setObjectName("horizontalLayout_76")
        self.reminder_type_menu = QtWidgets.QComboBox(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_type_menu.setFont(font)
        self.reminder_type_menu.setStyleSheet("background-color: rgb(255,255,255);\n"
                                              "")
        self.reminder_type_menu.setObjectName("reminder_type_menu")
        self.reminder_type_menu.addItem("")
        self.reminder_type_menu.addItem("")
        self.reminder_type_menu.addItem("")
        self.reminder_type_menu.addItem("")
        self.reminder_type_menu.addItem("")
        self.reminder_type_menu.addItem("")
        self.reminder_type_menu.addItem("")
        self.reminder_type_menu.addItem("")
        self.horizontalLayout_76.addWidget(self.reminder_type_menu)
        self.horizontalLayout_77 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_77.addItem(spacerItem13)
        self.edit_reminder_btn = QtWidgets.QPushButton(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_reminder_btn.setFont(font)
        self.edit_reminder_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.edit_reminder_btn.setObjectName("edit_reminder_btn")
        self.horizontalLayout_77.addWidget(self.edit_reminder_btn)
        self.delete_reminder_btn = QtWidgets.QPushButton(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_reminder_btn.setFont(font)
        self.delete_reminder_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.delete_reminder_btn.setObjectName("delete_reminder_btn")
        self.horizontalLayout_77.addWidget(self.delete_reminder_btn)
        self.archive_reminder_btn = QtWidgets.QPushButton(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archive_reminder_btn.setFont(font)
        self.archive_reminder_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.archive_reminder_btn.setObjectName("archive_reminder_btn")
        self.horizontalLayout_77.addWidget(self.archive_reminder_btn)
        self.complete_reminder_btn = QtWidgets.QPushButton(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.complete_reminder_btn.setFont(font)
        self.complete_reminder_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.complete_reminder_btn.setObjectName("complete_reminder_btn")
        self.horizontalLayout_77.addWidget(self.complete_reminder_btn)
        self.uncomplete_reminder_btn = QtWidgets.QPushButton(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uncomplete_reminder_btn.setFont(font)
        self.uncomplete_reminder_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.uncomplete_reminder_btn.setObjectName("uncomplete_reminder_btn")
        self.horizontalLayout_77.addWidget(self.uncomplete_reminder_btn)
        self.snooze_reminder_btn = QtWidgets.QPushButton(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.snooze_reminder_btn.setFont(font)
        self.snooze_reminder_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.snooze_reminder_btn.setObjectName("snooze_reminder_btn")
        self.horizontalLayout_77.addWidget(self.snooze_reminder_btn)
        self.horizontalLayout_76.addLayout(self.horizontalLayout_77)
        self.verticalLayout_55.addLayout(self.horizontalLayout_76)
        self.horizontalLayout_78 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_78.setObjectName("horizontalLayout_78")
        self.reminder_id_search = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.reminder_id_search.setPlaceholderText('Search Id')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_id_search.setFont(font)
        self.reminder_id_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.reminder_id_search.setText("")
        self.reminder_id_search.setObjectName("reminder_id_search")
        self.horizontalLayout_78.addWidget(self.reminder_id_search)
        self.reminder_name_search = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.reminder_name_search.setPlaceholderText('Search Name')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_name_search.setFont(font)
        self.reminder_name_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.reminder_name_search.setText("")
        self.reminder_name_search.setObjectName("reminder_name_search")
        self.horizontalLayout_78.addWidget(self.reminder_name_search)
        self.reminder_description_search = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.reminder_description_search.setPlaceholderText('Search Description')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_description_search.setFont(font)
        self.reminder_description_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.reminder_description_search.setText("")
        self.reminder_description_search.setObjectName("reminder_description_search")
        self.horizontalLayout_78.addWidget(self.reminder_description_search)
        self.reminder_date_search = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.reminder_date_search.setPlaceholderText('Search Reminder Date')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_date_search.setFont(font)
        self.reminder_date_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.reminder_date_search.setText("")
        self.reminder_date_search.setObjectName("reminder_date_search")
        self.horizontalLayout_78.addWidget(self.reminder_date_search)
        self.reminder_complete_search = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.reminder_complete_search.setPlaceholderText('Search Complete')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_complete_search.setFont(font)
        self.reminder_complete_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.reminder_complete_search.setText("")
        self.reminder_complete_search.setObjectName("reminder_complete_search")
        self.horizontalLayout_78.addWidget(self.reminder_complete_search)
        self.reminder_snoozed_search = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.reminder_snoozed_search.setPlaceholderText('Search Snoozed')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_snoozed_search.setFont(font)
        self.reminder_snoozed_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.reminder_snoozed_search.setText("")
        self.reminder_snoozed_search.setObjectName("reminder_snoozed_search")
        self.horizontalLayout_78.addWidget(self.reminder_snoozed_search)
        self.verticalLayout_55.addLayout(self.horizontalLayout_78)

        # Reminders tree
        self.reminders_tree = QtWidgets.QTreeView(self.layoutWidget_6)
        self.update_reminders()
        self.reminders_tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.reminders_tree.setModel(self.reminder_model)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminders_tree.setFont(font)
        self.reminders_tree.setStyleSheet("background-color: rgb(255,255,255)")
        self.reminders_tree.setAlternatingRowColors(True)
        self.reminders_tree.setColumnWidth(0, 162 * .75)
        self.reminders_tree.setColumnWidth(1, 170 * .75)
        self.reminders_tree.setColumnWidth(2, 170 * .75)
        self.reminders_tree.setColumnWidth(3, 171 * .75)
        self.reminders_tree.setColumnWidth(4, 171 * .75)
        self.reminders_tree.setColumnWidth(5, 175 * .75)
        self.reminders_tree.setObjectName("reminders_tree")
        self.verticalLayout_55.addWidget(self.reminders_tree)
        self.horizontalLayout_79 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_79.addItem(spacerItem14)
        # self.previous_reminders = QtWidgets.QPushButton(self.layoutWidget_6)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.previous_reminders.setFont(font)
        # self.previous_reminders.setStyleSheet("background-color: rgb(255,255,255)")
        # self.previous_reminders.setObjectName("previous_reminders")
        # self.horizontalLayout_79.addWidget(self.previous_reminders)
        # self.next_reminders = QtWidgets.QPushButton(self.layoutWidget_6)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.next_reminders.setFont(font)
        # self.next_reminders.setStyleSheet("background-color: rgb(255,255,255)")
        # self.next_reminders.setObjectName("next_reminders")
        # self.horizontalLayout_79.addWidget(self.next_reminders)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_79.addItem(spacerItem15)
        self.verticalLayout_55.addLayout(self.horizontalLayout_79)
        self.layoutWidget_7 = QtWidgets.QWidget(self.reminders_page)
        self.layoutWidget_7.setGeometry(QtCore.QRect(585, 15, 221.25, 22.5))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_80 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")
        self.new_reminder = QtWidgets.QPushButton(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_reminder.setFont(font)
        self.new_reminder.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.new_reminder.setObjectName("new_reminder")
        self.horizontalLayout_80.addWidget(self.new_reminder)
        self.export_reminders = QtWidgets.QPushButton(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.export_reminders.setFont(font)
        self.export_reminders.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.export_reminders.setObjectName("export_reminders")
        self.horizontalLayout_80.addWidget(self.export_reminders)
        # self.print_reminders = QtWidgets.QPushButton(self.layoutWidget_7)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.print_reminders.setFont(font)
        # self.print_reminders.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.print_reminders.setObjectName("print_reminders")
        # self.horizontalLayout_80.addWidget(self.print_reminders)
        self.main_widget.addWidget(self.reminders_page)
        self.new_reminder_page = QtWidgets.QWidget()
        self.new_reminder_page.setObjectName("new_reminder_page")
        self.new_reminder_lb = QtWidgets.QLabel(self.new_reminder_page)
        self.new_reminder_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.new_reminder_lb.setFont(font)
        self.new_reminder_lb.setStyleSheet("")
        self.new_reminder_lb.setObjectName("new_reminder_lb")
        self.scrollArea_11 = QtWidgets.QScrollArea(self.new_reminder_page)
        self.scrollArea_11.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.scrollArea_11.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollArea_11.setObjectName("scrollArea_11")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 1018, 961))
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout()
        self.verticalLayout_41.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_41.setSpacing(7)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout()
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_140 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_140.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_140.setFont(font)
        self.label_140.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_140.setObjectName("label_140")
        self.gridLayout_11.addWidget(self.label_140, 0, 0, 1, 1)

        # Reminder people tree
        self.reminder_people = QtWidgets.QTreeView(self.scrollAreaWidgetContents_11)
        self.update_reminder_people()
        self.reminder_people.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.reminder_people.setModel(self.reminder_person_model)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_people.setFont(font)
        self.reminder_people.setAutoFillBackground(False)
        self.reminder_people.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reminder_people.setColumnWidth(0, 30)
        self.reminder_people.setObjectName("reminder_people")
        self.gridLayout_11.addWidget(self.reminder_people, 6, 1, 1, 1)
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.reminder_add_party = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_add_party.setFont(font)
        self.reminder_add_party.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                              "")
        self.reminder_add_party.setObjectName("reminder_add_party")
        self.verticalLayout_43.addWidget(self.reminder_add_party)
        self.reminder_open_party = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_open_party.setFont(font)
        self.reminder_open_party.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                               "")
        self.reminder_open_party.setObjectName("reminder_open_party")
        self.verticalLayout_43.addWidget(self.reminder_open_party)
        self.reminder_delete_party = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_delete_party.setFont(font)
        self.reminder_delete_party.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                                 "")
        self.reminder_delete_party.setObjectName("reminder_delete_party")
        self.verticalLayout_43.addWidget(self.reminder_delete_party)
        self.gridLayout_11.addLayout(self.verticalLayout_43, 6, 2, 1, 1)
        self.label_141 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_141.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_141.setFont(font)
        self.label_141.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_141.setObjectName("label_141")
        self.gridLayout_11.addWidget(self.label_141, 1, 0, 1, 1)
        self.reminder_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reminder_name.sizePolicy().hasHeightForWidth())
        self.reminder_name.setSizePolicy(sizePolicy)
        self.reminder_name.setMinimumSize(QtCore.QSize(0, 35))
        self.reminder_name.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_name.setFont(font)
        self.reminder_name.setAutoFillBackground(False)
        self.reminder_name.setObjectName("reminder_name")
        self.gridLayout_11.addWidget(self.reminder_name, 1, 1, 1, 1)
        self.label_142 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_142.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_142.setFont(font)
        self.label_142.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_142.setObjectName("label_142")
        self.gridLayout_11.addWidget(self.label_142, 2, 0, 1, 1)
        self.label_143 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_143.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_143.setFont(font)
        self.label_143.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_143.setObjectName("label_143")
        self.gridLayout_11.addWidget(self.label_143, 3, 0, 1, 1)

        # Reminder Contract
        contracts_id = self.fetch_query('SELECT id FROM contracts')
        contracts_title = self.fetch_query('SELECT title FROM contracts')
        contracts = []
        for c_id, c_title in zip(contracts_id, contracts_title):
            c = str(c_id) + ' - ' + c_title
            contracts.append(c)

        self.reminder_contract = QtWidgets.QComboBox(self.scrollAreaWidgetContents_11)

        self.reminder_contract.addItem('0 - No Contract')
        for contract in contracts:
            self.reminder_contract.addItem(contract)

        self.reminder_contract.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_contract.setFont(font)
        self.reminder_contract.setAutoFillBackground(False)
        self.reminder_contract.setObjectName("reminder_contract")
        self.gridLayout_11.addWidget(self.reminder_contract, 2, 1, 1, 1)

        # Reminder company
        companies_id = self.fetch_query('SELECT id FROM companies')
        companies_title = self.fetch_query('SELECT name FROM companies')
        companies = []
        for c_id, c_title in zip(companies_id, companies_title):
            c = str(c_id) + ' - ' + c_title
            companies.append(c)

        self.reminder_company = QtWidgets.QComboBox(self.scrollAreaWidgetContents_11)

        self.reminder_company.addItem('0 - No company')
        for company in companies:
            self.reminder_company.addItem(company)
        self.reminder_company.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_company.setFont(font)
        self.reminder_company.setAutoFillBackground(False)
        self.reminder_company.setObjectName("reminder_company")
        self.gridLayout_11.addWidget(self.reminder_company, 3, 1, 1, 1)
        self.reminder_id_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.reminder_id_lb.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_id_lb.setFont(font)
        self.reminder_id_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.reminder_id_lb.setText("")
        self.reminder_id_lb.setObjectName("reminder_id_lb")
        self.gridLayout_11.addWidget(self.reminder_id_lb, 0, 1, 1, 1)
        self.label_144 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_144.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_144.setFont(font)
        self.label_144.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_144.setObjectName("label_144")
        self.gridLayout_11.addWidget(self.label_144, 6, 0, 1, 1)
        self.verticalLayout_42.addLayout(self.gridLayout_11)
        self.verticalLayout_41.addLayout(self.verticalLayout_42)
        self.verticalLayout_40.addLayout(self.verticalLayout_41)
        self.label_145 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_145.setFont(font)
        self.label_145.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_145.setObjectName("label_145")
        self.verticalLayout_40.addWidget(self.label_145)
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.reminder_description = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_11)
        self.reminder_description.setMinimumSize(QtCore.QSize(0, 125))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_description.setFont(font)
        self.reminder_description.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reminder_description.setObjectName("reminder_description")
        self.horizontalLayout_44.addWidget(self.reminder_description)
        self.verticalLayout_40.addLayout(self.horizontalLayout_44)
        self.label_146 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_146.setFont(font)
        self.label_146.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_146.setObjectName("label_146")
        self.verticalLayout_40.addWidget(self.label_146)

        # Reminder attachments
        self.reminder_attachments = QtWidgets.QTreeView(self.scrollAreaWidgetContents_11)
        self.update_reminder_attachments()
        self.reminder_attachments.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.reminder_attachments.setModel(self.reminder_attachment_model)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_attachments.setFont(font)
        self.reminder_attachments.setAutoFillBackground(False)
        self.reminder_attachments.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reminder_attachments.setColumnWidth(0, 90)
        self.reminder_attachments.setColumnWidth(1, 250)
        self.reminder_attachments.setObjectName("reminder_attachments")
        self.verticalLayout_40.addWidget(self.reminder_attachments)
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem16)
        self.reminder_add_attachment = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_add_attachment.setFont(font)
        self.reminder_add_attachment.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                                   "")
        self.reminder_add_attachment.setObjectName("reminder_add_attachment")
        self.horizontalLayout_45.addWidget(self.reminder_add_attachment)
        self.reminder_open_attachment = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_open_attachment.setFont(font)
        self.reminder_open_attachment.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                                    "")
        self.reminder_open_attachment.setObjectName("reminder_open_attachment")
        self.horizontalLayout_45.addWidget(self.reminder_open_attachment)
        self.reminder_delete_attachment = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_delete_attachment.setFont(font)
        self.reminder_delete_attachment.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                                      "")
        self.reminder_delete_attachment.setObjectName("reminder_delete_attachment")
        self.horizontalLayout_45.addWidget(self.reminder_delete_attachment)
        self.verticalLayout_40.addLayout(self.horizontalLayout_45)
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.reminder_complete = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_complete.setFont(font)
        self.reminder_complete.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.reminder_complete.setObjectName("reminder_complete")
        self.horizontalLayout_46.addWidget(self.reminder_complete)
        self.reminder_snoozed = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_snoozed.setFont(font)
        self.reminder_snoozed.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.reminder_snoozed.setObjectName("reminder_snoozed")
        self.horizontalLayout_46.addWidget(self.reminder_snoozed)
        self.verticalLayout_40.addLayout(self.horizontalLayout_46)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.recur_indefinitely_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_11)
        self.recur_indefinitely_radio.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.recur_indefinitely_radio.setObjectName("recur_indefinitely_radio")
        self.gridLayout_12.addWidget(self.recur_indefinitely_radio, 7, 6, 1, 1)
        self.before = QtWidgets.QComboBox(self.scrollAreaWidgetContents_11)
        self.before.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.before.setFont(font)
        self.before.setAutoFillBackground(False)
        self.before.setObjectName("before")
        self.before.addItem("")
        self.before.addItem("")
        self.gridLayout_12.addWidget(self.before, 6, 2, 1, 2)
        self.time_type = QtWidgets.QComboBox(self.scrollAreaWidgetContents_11)
        self.time_type.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_type.setFont(font)
        self.time_type.setAutoFillBackground(False)
        self.time_type.setObjectName("time_type")
        self.time_type.addItem("")
        self.time_type.addItem("")
        self.time_type.addItem("")
        self.time_type.addItem("")
        self.gridLayout_12.addWidget(self.time_type, 5, 2, 1, 2)
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.recur_until_specific = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_11)
        self.recur_until_specific.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.recur_until_specific.setObjectName("recur_until_specific")
        self.horizontalLayout_47.addWidget(self.recur_until_specific)
        self.recur_until_specific_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recur_until_specific_2.sizePolicy().hasHeightForWidth())
        self.recur_until_specific_2.setSizePolicy(sizePolicy)
        self.recur_until_specific_2.setMinimumSize(QtCore.QSize(0, 35))
        self.recur_until_specific_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.recur_until_specific_2.setFont(font)
        self.recur_until_specific_2.setAutoFillBackground(False)
        self.recur_until_specific_2.setObjectName("recur_until_specific_2")
        self.horizontalLayout_47.addWidget(self.recur_until_specific_2)
        self.recur_until_btn = QtWidgets.QToolButton(self.scrollAreaWidgetContents_11)
        self.recur_until_btn.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                           "")
        self.recur_until_btn.setObjectName("recur_until_btn")
        self.horizontalLayout_47.addWidget(self.recur_until_btn)
        self.gridLayout_12.addLayout(self.horizontalLayout_47, 5, 6, 1, 1)
        self.label_147 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_147.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_147.setFont(font)
        self.label_147.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_147.setObjectName("label_147")
        self.gridLayout_12.addWidget(self.label_147, 1, 5, 1, 1)
        self.label_148 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_148.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_148.setFont(font)
        self.label_148.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_148.setObjectName("label_148")
        self.gridLayout_12.addWidget(self.label_148, 1, 1, 1, 1)
        self.specific_date_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_11)
        self.specific_date_radio.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.specific_date_radio.setObjectName("specific_date_radio")
        self.gridLayout_12.addWidget(self.specific_date_radio, 2, 1, 1, 2)
        self.do_not_recur_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_11)
        self.do_not_recur_radio.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.do_not_recur_radio.setObjectName("do_not_recur_radio")
        self.gridLayout_12.addWidget(self.do_not_recur_radio, 2, 5, 1, 1)
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.reminder_specific_date = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reminder_specific_date.sizePolicy().hasHeightForWidth())
        self.reminder_specific_date.setSizePolicy(sizePolicy)
        self.reminder_specific_date.setMinimumSize(QtCore.QSize(0, 35))
        self.reminder_specific_date.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_specific_date.setFont(font)
        self.reminder_specific_date.setAutoFillBackground(False)
        self.reminder_specific_date.setObjectName("reminder_specific_date")
        self.horizontalLayout_48.addWidget(self.reminder_specific_date)
        self.specific_date_btn = QtWidgets.QToolButton(self.scrollAreaWidgetContents_11)
        self.specific_date_btn.setStyleSheet("background-color: rgb(242, 242, 247);\n"
                                             "")
        self.specific_date_btn.setObjectName("specific_date_btn")
        self.horizontalLayout_48.addWidget(self.specific_date_btn)
        self.gridLayout_12.addLayout(self.horizontalLayout_48, 2, 3, 1, 1)
        self.recur_type = QtWidgets.QComboBox(self.scrollAreaWidgetContents_11)
        self.recur_type.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.recur_type.setFont(font)
        self.recur_type.setAutoFillBackground(False)
        self.recur_type.setObjectName("recur_type")
        self.recur_type.addItem("")
        self.recur_type.addItem("")
        self.recur_type.addItem("")
        self.recur_type.addItem("")
        self.recur_type.addItem("")
        self.recur_type.addItem("")
        self.recur_type.addItem("")
        self.recur_type.addItem("")
        self.recur_type.addItem("")
        self.recur_type.addItem("")
        self.recur_type.addItem("")
        self.gridLayout_12.addWidget(self.recur_type, 3, 6, 1, 1)
        self.reminder_relative_date = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reminder_relative_date.sizePolicy().hasHeightForWidth())
        self.reminder_relative_date.setSizePolicy(sizePolicy)
        self.reminder_relative_date.setMinimumSize(QtCore.QSize(0, 35))
        self.reminder_relative_date.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminder_relative_date.setFont(font)
        self.reminder_relative_date.setAutoFillBackground(False)
        self.reminder_relative_date.setObjectName("reminder_relative_date")
        self.gridLayout_12.addWidget(self.reminder_relative_date, 3, 3, 1, 1)
        self.recur_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_11)
        self.recur_radio.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.recur_radio.setObjectName("recur_radio")
        self.gridLayout_12.addWidget(self.recur_radio, 3, 5, 1, 1)
        self.relative_date_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_11)
        self.relative_date_radio.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.relative_date_radio.setObjectName("relative_date_radio")
        self.gridLayout_12.addWidget(self.relative_date_radio, 3, 1, 1, 1)
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.until_key_date_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_11)
        self.until_key_date_radio.setMaximumSize(QtCore.QSize(52, 16777215))
        self.until_key_date_radio.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.until_key_date_radio.setObjectName("until_key_date_radio")
        self.horizontalLayout_49.addWidget(self.until_key_date_radio)
        self.until_key_date = QtWidgets.QComboBox(self.scrollAreaWidgetContents_11)
        self.until_key_date.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.until_key_date.setFont(font)
        self.until_key_date.setAutoFillBackground(False)
        self.until_key_date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(0,0,0)\n"
                                          "")
        self.until_key_date.setObjectName("until_key_date")
        self.until_key_date.addItem("")
        self.until_key_date.addItem("")
        self.until_key_date.addItem("")
        self.until_key_date.addItem("")
        self.horizontalLayout_49.addWidget(self.until_key_date)
        self.gridLayout_12.addLayout(self.horizontalLayout_49, 6, 6, 1, 1)
        self.key_date = QtWidgets.QComboBox(self.scrollAreaWidgetContents_11)
        self.key_date.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.key_date.setFont(font)
        self.key_date.setAutoFillBackground(False)
        self.key_date.setObjectName("key_date")
        self.key_date.addItem("")
        self.key_date.addItem("")
        self.key_date.addItem("")
        self.key_date.addItem("")
        self.gridLayout_12.addWidget(self.key_date, 7, 2, 1, 2)
        self.label_149 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_149.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_149.setFont(font)
        self.label_149.setText("")
        self.label_149.setObjectName("label_149")
        self.gridLayout_12.addWidget(self.label_149, 0, 1, 1, 1)
        self.label_150 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_150.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_150.setFont(font)
        self.label_150.setText("")
        self.label_150.setObjectName("label_150")
        self.gridLayout_12.addWidget(self.label_150, 1, 4, 1, 1)
        self.verticalLayout_40.addLayout(self.gridLayout_12)
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)
        self.layoutWidget_15 = QtWidgets.QWidget(self.new_reminder_page)
        self.layoutWidget_15.setGeometry(QtCore.QRect(652.5, 22.5, 146.25, 22.5))
        self.layoutWidget_15.setObjectName("layoutWidget_15")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.save_reminder = QtWidgets.QPushButton(self.layoutWidget_15)
        self.save_reminder.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.save_reminder.setObjectName("save_reminder")
        self.horizontalLayout_50.addWidget(self.save_reminder)
        self.cancel_reminder = QtWidgets.QPushButton(self.layoutWidget_15)
        self.cancel_reminder.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.cancel_reminder.setObjectName("cancel_reminder")
        self.horizontalLayout_50.addWidget(self.cancel_reminder)
        self.main_widget.addWidget(self.new_reminder_page)
        self.risks_page = QtWidgets.QWidget()
        self.risks_page.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.risks_page.setObjectName("risks_page")
        self.risk_lb = QtWidgets.QLabel(self.risks_page)
        self.risk_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.risk_lb.setFont(font)
        self.risk_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.risk_lb.setObjectName("risk_lb")
        self.frame_6 = QtWidgets.QFrame(self.risks_page)
        self.frame_6.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.layoutWidget_8 = QtWidgets.QWidget(self.frame_6)
        self.layoutWidget_8.setGeometry(QtCore.QRect(9, 2, 765, 487.5))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        self.risk_type_menu = QtWidgets.QComboBox(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_type_menu.setFont(font)
        self.risk_type_menu.setStyleSheet("background-color: rgb(255,255,255);\n"
                                          "")
        self.risk_type_menu.setObjectName("risk_type_menu")
        self.risk_type_menu.addItem("")
        self.risk_type_menu.addItem("")
        self.risk_type_menu.addItem("")
        self.risk_type_menu.addItem("")
        self.risk_type_menu.addItem("")
        self.risk_type_menu.addItem("")
        self.risk_type_menu.addItem("")
        self.risk_type_menu.addItem("")
        self.risk_type_menu.addItem("")
        self.risk_type_menu.addItem("")
        self.risk_type_menu.addItem("")
        self.horizontalLayout_81.addWidget(self.risk_type_menu)
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem17)
        self.edit_risk_btn = QtWidgets.QPushButton(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_risk_btn.setFont(font)
        self.edit_risk_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.edit_risk_btn.setObjectName("edit_risk_btn")
        self.horizontalLayout_82.addWidget(self.edit_risk_btn)
        self.delete_risk_btn = QtWidgets.QPushButton(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_risk_btn.setFont(font)
        self.delete_risk_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.delete_risk_btn.setObjectName("delete_risk_btn")
        self.horizontalLayout_82.addWidget(self.delete_risk_btn)
        self.archive_risk_btn = QtWidgets.QPushButton(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archive_risk_btn.setFont(font)
        self.archive_risk_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.archive_risk_btn.setObjectName("archive_risk_btn")
        self.horizontalLayout_82.addWidget(self.archive_risk_btn)
        self.favorite_risk_btn = QtWidgets.QPushButton(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.favorite_risk_btn.setFont(font)
        self.favorite_risk_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.favorite_risk_btn.setObjectName("favorite_risk_btn")
        self.horizontalLayout_82.addWidget(self.favorite_risk_btn)
        self.horizontalLayout_81.addLayout(self.horizontalLayout_82)
        self.verticalLayout_56.addLayout(self.horizontalLayout_81)
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        self.risk_id_search = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.risk_id_search.setPlaceholderText('Search Id')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_id_search.setFont(font)
        self.risk_id_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.risk_id_search.setText("")
        self.risk_id_search.setObjectName("risk_id_search")
        self.horizontalLayout_83.addWidget(self.risk_id_search)
        self.risk_name_search = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.risk_name_search.setPlaceholderText('Search Name')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_name_search.setFont(font)
        self.risk_name_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.risk_name_search.setText("")
        self.risk_name_search.setObjectName("risk_name_search")
        self.horizontalLayout_83.addWidget(self.risk_name_search)
        self.risk_type_search = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.risk_type_search.setPlaceholderText('Search Type')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_type_search.setFont(font)
        self.risk_type_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.risk_type_search.setText("")
        self.risk_type_search.setObjectName("risk_type_search")
        self.horizontalLayout_83.addWidget(self.risk_type_search)
        self.risk_severity_search = QtWidgets.QComboBox(self.layoutWidget_8)
        self.risk_severity_search.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_severity_search.setFont(font)
        self.risk_severity_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.risk_severity_search.setObjectName("risk_severity_search")
        self.risk_severity_search.addItem("")
        self.risk_severity_search.addItem("")
        self.risk_severity_search.addItem("")
        self.risk_severity_search.addItem("")
        self.horizontalLayout_83.addWidget(self.risk_severity_search)
        self.risk_end_search = QtWidgets.QComboBox(self.layoutWidget_8)
        self.risk_end_search.addItem('Any')
        self.risk_end_search.addItem('Low')
        self.risk_end_search.addItem('Medium')
        self.risk_end_search.addItem('High')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_end_search.setFont(font)
        self.risk_end_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.risk_end_search.setObjectName("risk_end_search")
        self.horizontalLayout_83.addWidget(self.risk_end_search)
        self.risk_expired_search = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.risk_expired_search.setPlaceholderText('Search End Date')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_expired_search.setFont(font)
        self.risk_expired_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.risk_expired_search.setText("")
        self.risk_expired_search.setObjectName("risk_expired_search")
        self.horizontalLayout_83.addWidget(self.risk_expired_search)
        self.risk_filename_search = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.risk_filename_search.setPlaceholderText('Search Expired Search')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_filename_search.setFont(font)
        self.risk_filename_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.risk_filename_search.setText("")
        self.risk_filename_search.setObjectName("risk_filename_search")
        self.horizontalLayout_83.addWidget(self.risk_filename_search)
        self.verticalLayout_56.addLayout(self.horizontalLayout_83)

        # Risks Tree
        self.risks_tree = QtWidgets.QTreeView(self.layoutWidget_8)
        self.update_risks()
        self.risks_tree.setModel(self.risk_model)
        self.risks_tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risks_tree.setFont(font)
        self.risks_tree.setStyleSheet("background-color: rgb(255,255,255)")
        self.risks_tree.setAlternatingRowColors(True)
        self.risks_tree.setObjectName("risks_tree")
        self.verticalLayout_56.addWidget(self.risks_tree)
        self.risks_tree.setColumnWidth(0, 170 * .75)
        self.risks_tree.setColumnWidth(1, 155 * .75)
        self.risks_tree.setColumnWidth(2, 150 * .75)
        self.risks_tree.setColumnWidth(3, 85 * .75)
        self.risks_tree.setColumnWidth(4, 154 * .75)
        self.risks_tree.setColumnWidth(5, 153 * .75)
        self.risks_tree.setColumnWidth(6, 154 * .75)
        self.risks_tree.setColumnWidth(7, 155 * .75)
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_84.addItem(spacerItem18)
        # self.previous_risks = QtWidgets.QPushButton(self.layoutWidget_8)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.previous_risks.setFont(font)
        # self.previous_risks.setStyleSheet("background-color: rgb(255,255,255)")
        # self.previous_risks.setObjectName("previous_risks")
        # self.horizontalLayout_84.addWidget(self.previous_risks)
        # self.next_risks = QtWidgets.QPushButton(self.layoutWidget_8)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.next_risks.setFont(font)
        # self.next_risks.setStyleSheet("background-color: rgb(255,255,255)")
        # self.next_risks.setObjectName("next_risks")
        # self.horizontalLayout_84.addWidget(self.next_risks)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_84.addItem(spacerItem19)
        self.verticalLayout_56.addLayout(self.horizontalLayout_84)
        self.layoutWidget_9 = QtWidgets.QWidget(self.risks_page)
        self.layoutWidget_9.setGeometry(QtCore.QRect(585, 15, 221.25, 22.5))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        self.new_risk = QtWidgets.QPushButton(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_risk.setFont(font)
        self.new_risk.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.new_risk.setObjectName("new_risk")
        self.horizontalLayout_85.addWidget(self.new_risk)
        self.export_risks = QtWidgets.QPushButton(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.export_risks.setFont(font)
        self.export_risks.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.export_risks.setObjectName("export_risks")
        self.horizontalLayout_85.addWidget(self.export_risks)
        # self.print_risks = QtWidgets.QPushButton(self.layoutWidget_9)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.print_risks.setFont(font)
        # self.print_risks.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.print_risks.setObjectName("print_risks")
        # self.horizontalLayout_85.addWidget(self.print_risks)
        self.main_widget.addWidget(self.risks_page)
        self.new_risk_page = QtWidgets.QWidget()
        self.new_risk_page.setObjectName("new_risk_page")
        self.new_risk_lb = QtWidgets.QLabel(self.new_risk_page)
        self.new_risk_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.new_risk_lb.setFont(font)
        self.new_risk_lb.setStyleSheet("")
        self.new_risk_lb.setObjectName("new_risk_lb")
        self.layoutWidget_16 = QtWidgets.QWidget(self.new_risk_page)
        self.layoutWidget_16.setGeometry(QtCore.QRect(652.5, 22.5, 146.25, 22.5))
        self.layoutWidget_16.setObjectName("layoutWidget_16")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.layoutWidget_16)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.save_risk = QtWidgets.QPushButton(self.layoutWidget_16)
        self.save_risk.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.save_risk.setObjectName("save_risk")
        self.horizontalLayout_51.addWidget(self.save_risk)
        self.cancel_risk = QtWidgets.QPushButton(self.layoutWidget_16)
        self.cancel_risk.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.cancel_risk.setObjectName("cancel_risk")
        self.horizontalLayout_51.addWidget(self.cancel_risk)
        self.scrollArea_12 = QtWidgets.QScrollArea(self.new_risk_page)
        self.scrollArea_12.setGeometry(QtCore.QRect(22.5, 52.5, 780, 510))
        self.scrollArea_12.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollArea_12.setObjectName("scrollArea_12")
        self.scrollAreaWidgetContents_12 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 780, 510))
        self.scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout()
        self.verticalLayout_45.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_45.setSpacing(7)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout()
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.risk_id_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.risk_id_lb.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_id_lb.setFont(font)
        self.risk_id_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.risk_id_lb.setText("")
        self.risk_id_lb.setObjectName("risk_id_lb")
        self.gridLayout_13.addWidget(self.risk_id_lb, 0, 1, 1, 1)
        self.label_151 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_151.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_151.setFont(font)
        self.label_151.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_151.setObjectName("label_151")
        self.gridLayout_13.addWidget(self.label_151, 1, 0, 1, 1)
        self.label_152 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_152.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_152.setFont(font)
        self.label_152.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_152.setObjectName("label_152")
        self.gridLayout_13.addWidget(self.label_152, 3, 0, 1, 1)
        self.risk_type = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.risk_type.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_type.setFont(font)
        self.risk_type.setAutoFillBackground(False)
        self.risk_type.setObjectName("risk_type")
        self.risk_type.addItem("")
        self.risk_type.addItem("")
        self.risk_type.addItem("")
        self.risk_type.addItem("")
        self.risk_type.addItem("")
        self.risk_type.addItem("")
        self.gridLayout_13.addWidget(self.risk_type, 3, 3, 1, 1)

        # Risk end date
        self.label_175 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_175.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_175.setFont(font)
        self.label_175.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_175.setObjectName("label_175")
        self.gridLayout_13.addWidget(self.label_175, 4, 0, 1, 1)
        self.horizontalLayout_93 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_93.setObjectName("horizontalLayout_93")
        self.risk_end = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.risk_end.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_end.setFont(font)
        self.risk_end.setAutoFillBackground(False)
        self.risk_end.setObjectName("risk_end")
        self.horizontalLayout_93.addWidget(self.risk_end)
        self.risk_end_btn = QtWidgets.QToolButton(self.scrollAreaWidgetContents_12)
        self.risk_end_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_end_btn.setFont(font)
        self.risk_end_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.risk_end_btn.setObjectName("risk_end_btn")
        self.horizontalLayout_93.addWidget(self.risk_end_btn)
        self.gridLayout_13.addLayout(self.horizontalLayout_93, 4, 1, 1, 1)

        self.verticalLayout_47 = QtWidgets.QVBoxLayout()
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.label_153 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_153.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_153.setFont(font)
        self.label_153.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_153.setObjectName("label_153")
        self.horizontalLayout_52.addWidget(self.label_153)
        self.risk_probability = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.risk_probability.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_probability.setFont(font)
        self.risk_probability.setAutoFillBackground(False)
        self.risk_probability.setObjectName("risk_probability")
        self.risk_probability.addItem("")
        self.risk_probability.addItem("")
        self.risk_probability.addItem("")
        self.horizontalLayout_52.addWidget(self.risk_probability)
        self.verticalLayout_47.addLayout(self.horizontalLayout_52)
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.label_154 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_154.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_154.setFont(font)
        self.label_154.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_154.setObjectName("label_154")
        self.horizontalLayout_53.addWidget(self.label_154)
        self.risk_impact = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.risk_impact.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_impact.setFont(font)
        self.risk_impact.setAutoFillBackground(False)
        self.risk_impact.setObjectName("risk_impact")
        self.risk_impact.addItem("")
        self.risk_impact.addItem("")
        self.risk_impact.addItem("")
        self.horizontalLayout_53.addWidget(self.risk_impact)
        self.verticalLayout_47.addLayout(self.horizontalLayout_53)
        self.gridLayout_13.addLayout(self.verticalLayout_47, 3, 1, 1, 1)
        self.label_155 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_155.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_155.setFont(font)
        self.label_155.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_155.setObjectName("label_155")
        self.gridLayout_13.addWidget(self.label_155, 0, 0, 1, 1)
        self.label_156 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_156.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_156.setFont(font)
        self.label_156.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_156.setObjectName("label_156")
        self.gridLayout_13.addWidget(self.label_156, 3, 2, 1, 1)

        # Risk contract
        contracts_id = self.fetch_query('SELECT id FROM contracts')
        contracts_title = self.fetch_query('SELECT title FROM contracts')
        contracts = []
        for c_id, c_title in zip(contracts_id, contracts_title):
            c = str(c_id) + ' - ' + c_title
            contracts.append(c)

        self.risk_contract = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.risk_contract.addItem('0 - No Master Contract')
        for contract in contracts:
            self.risk_contract.addItem(contract)

        self.risk_contract.setMinimumSize(QtCore.QSize(423, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_contract.setFont(font)
        self.risk_contract.setAutoFillBackground(False)
        self.risk_contract.setObjectName("risk_contract")
        self.gridLayout_13.addWidget(self.risk_contract, 1, 3, 1, 1)
        self.label_157 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_157.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_157.setFont(font)
        self.label_157.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_157.setObjectName("label_157")
        self.gridLayout_13.addWidget(self.label_157, 1, 2, 1, 1)
        self.risk_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.risk_name.sizePolicy().hasHeightForWidth())
        self.risk_name.setSizePolicy(sizePolicy)
        self.risk_name.setMinimumSize(QtCore.QSize(0, 35))
        self.risk_name.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_name.setFont(font)
        self.risk_name.setAutoFillBackground(False)
        self.risk_name.setObjectName("risk_name")
        self.gridLayout_13.addWidget(self.risk_name, 1, 1, 1, 1)
        self.verticalLayout_46.addLayout(self.gridLayout_13)
        self.verticalLayout_45.addLayout(self.verticalLayout_46)
        self.verticalLayout_44.addLayout(self.verticalLayout_45)
        self.label_158 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_158.setFont(font)
        self.label_158.setText("")
        self.label_158.setObjectName("label_158")
        self.verticalLayout_44.addWidget(self.label_158)
        self.label_159 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_159.setFont(font)
        self.label_159.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_159.setObjectName("label_159")
        self.verticalLayout_44.addWidget(self.label_159)
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.risk_notes = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_12)
        self.risk_notes.setMinimumSize(QtCore.QSize(0, 125))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_notes.setFont(font)
        self.risk_notes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.risk_notes.setObjectName("risk_notes")
        self.horizontalLayout_54.addWidget(self.risk_notes)
        self.verticalLayout_44.addLayout(self.horizontalLayout_54)
        self.label_160 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_160.setFont(font)
        self.label_160.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_160.setObjectName("label_160")
        self.verticalLayout_44.addWidget(self.label_160)
        self.risk_mitigation = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_12)
        self.risk_mitigation.setMinimumSize(QtCore.QSize(0, 125))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_mitigation.setFont(font)
        self.risk_mitigation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.risk_mitigation.setObjectName("risk_mitigation")
        self.verticalLayout_44.addWidget(self.risk_mitigation)
        self.label_161 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_161.setFont(font)
        self.label_161.setText("")
        self.label_161.setObjectName("label_161")
        self.verticalLayout_44.addWidget(self.label_161)
        self.label_162 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_162.setFont(font)
        self.label_162.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_162.setObjectName("label_162")
        self.verticalLayout_44.addWidget(self.label_162)

        # Risk attachments
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.risk_attachment_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_(
            "SELECT id as ID, name as Name, url as Url, date_created as 'Date Created' FROM documents WHERE type_id=3 "
            "AND owner_id=" + str(
                self.next_risk_id()))
        self.risk_attachment_model.setQuery(query)
        db.close()

        self.risk_attachments = QtWidgets.QTreeView(self.scrollAreaWidgetContents_12)
        self.update_risk_attachments()
        self.risk_attachments.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.risk_attachments.setModel(self.risk_attachment_model)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_attachments.setFont(font)
        self.risk_attachments.setAutoFillBackground(False)
        self.risk_attachments.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.risk_attachments.setColumnWidth(0, 90)
        self.risk_attachments.setColumnWidth(1, 250)
        self.risk_attachments.setObjectName("risk_attachments")
        self.verticalLayout_44.addWidget(self.risk_attachments)
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_55.addItem(spacerItem20)
        self.risk_add_attachment_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_add_attachment_3.setFont(font)
        self.risk_add_attachment_3.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.risk_add_attachment_3.setObjectName("risk_add_attachment_3")
        self.horizontalLayout_55.addWidget(self.risk_add_attachment_3)
        self.risk_open_attachment_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_open_attachment_3.setFont(font)
        self.risk_open_attachment_3.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.risk_open_attachment_3.setObjectName("risk_open_attachment_3")
        self.horizontalLayout_55.addWidget(self.risk_open_attachment_3)
        self.risk_delete_attachment_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risk_delete_attachment_3.setFont(font)
        self.risk_delete_attachment_3.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.risk_delete_attachment_3.setObjectName("risk_delete_attachment_3")
        self.horizontalLayout_55.addWidget(self.risk_delete_attachment_3)
        self.verticalLayout_44.addLayout(self.horizontalLayout_55)
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.verticalLayout_44.addLayout(self.horizontalLayout_56)
        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)
        self.main_widget.addWidget(self.new_risk_page)
        self.todos_page = QtWidgets.QWidget()
        self.todos_page.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.todos_page.setObjectName("todos_page")
        self.todos_lb = QtWidgets.QLabel(self.todos_page)
        self.todos_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.todos_lb.setFont(font)
        self.todos_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.todos_lb.setObjectName("todos_lb")
        self.layoutWidget_11 = QtWidgets.QWidget(self.todos_page)
        self.layoutWidget_11.setGeometry(QtCore.QRect(585, 15, 221.25, 22.5))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.new_todo = QtWidgets.QPushButton(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_todo.setFont(font)
        self.new_todo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.new_todo.setObjectName("new_todo")
        self.horizontalLayout_88.addWidget(self.new_todo)
        self.export_todos = QtWidgets.QPushButton(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.export_todos.setFont(font)
        self.export_todos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.export_todos.setObjectName("export_todos")
        self.horizontalLayout_88.addWidget(self.export_todos)
        # self.print_todos = QtWidgets.QPushButton(self.layoutWidget_11)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.print_todos.setFont(font)
        # self.print_todos.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.print_todos.setObjectName("print_todos")
        # self.horizontalLayout_88.addWidget(self.print_todos)
        self.frame_7 = QtWidgets.QFrame(self.todos_page)
        self.frame_7.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.layoutWidget_18 = QtWidgets.QWidget(self.frame_7)
        self.layoutWidget_18.setGeometry(QtCore.QRect(9, 2, 765, 487.5))
        self.layoutWidget_18.setObjectName("layoutWidget_18")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.layoutWidget_18)
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.horizontalLayout_89 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.todos_type_menu = QtWidgets.QComboBox(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todos_type_menu.setFont(font)
        self.todos_type_menu.setStyleSheet("background-color: rgb(255,255,255);\n"
                                           "")
        self.todos_type_menu.setObjectName("todos_type_menu")
        self.todos_type_menu.addItem("")
        self.todos_type_menu.addItem("")
        self.todos_type_menu.addItem("")
        self.todos_type_menu.addItem("")
        self.todos_type_menu.addItem("")
        self.todos_type_menu.addItem("")
        self.todos_type_menu.addItem("")
        self.todos_type_menu.addItem("")
        self.todos_type_menu.addItem("")
        self.todos_type_menu.addItem("")
        self.todos_type_menu.addItem("")
        self.horizontalLayout_89.addWidget(self.todos_type_menu)
        self.horizontalLayout_90 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_90.addItem(spacerItem21)
        self.edit_todo_btn = QtWidgets.QPushButton(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_todo_btn.setFont(font)
        self.edit_todo_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.edit_todo_btn.setObjectName("edit_todo_btn")
        self.horizontalLayout_90.addWidget(self.edit_todo_btn)
        self.delete_todo_btn = QtWidgets.QPushButton(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_todo_btn.setFont(font)
        self.delete_todo_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.delete_todo_btn.setObjectName("delete_todo_btn")
        self.horizontalLayout_90.addWidget(self.delete_todo_btn)
        self.archive_todo_btn = QtWidgets.QPushButton(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archive_todo_btn.setFont(font)
        self.archive_todo_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.archive_todo_btn.setObjectName("archive_todo_btn")
        self.horizontalLayout_90.addWidget(self.archive_todo_btn)
        self.favorite_todo_btn = QtWidgets.QPushButton(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.favorite_todo_btn.setFont(font)
        self.favorite_todo_btn.setStyleSheet("background-color: rgb(255,255,255)")
        self.favorite_todo_btn.setObjectName("favorite_todo_btn")
        self.horizontalLayout_90.addWidget(self.favorite_todo_btn)
        self.horizontalLayout_89.addLayout(self.horizontalLayout_90)
        self.verticalLayout_57.addLayout(self.horizontalLayout_89)
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        self.todo_id_search = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.todo_id_search.setPlaceholderText('Search Id')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_id_search.setFont(font)
        self.todo_id_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.todo_id_search.setText("")
        self.todo_id_search.setObjectName("todo_id_search")
        self.horizontalLayout_91.addWidget(self.todo_id_search)
        self.todo_subject_search = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.todo_subject_search.setPlaceholderText('Search Subject')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_subject_search.setFont(font)
        self.todo_subject_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.todo_subject_search.setText("")
        self.todo_subject_search.setObjectName("todo_subject_search")
        self.horizontalLayout_91.addWidget(self.todo_subject_search)
        self.todo_responsible_search = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.todo_responsible_search.setPlaceholderText('Search Assigned To')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_responsible_search.setFont(font)
        self.todo_responsible_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.todo_responsible_search.setText("")
        self.todo_responsible_search.setObjectName("todo_responsible_search")
        self.horizontalLayout_91.addWidget(self.todo_responsible_search)
        self.todo_status_search = QtWidgets.QComboBox(self.layoutWidget_18)
        self.todo_status_search.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_status_search.setFont(font)
        self.todo_status_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.todo_status_search.setObjectName("todo_status_search")
        self.todo_status_search.addItem("")
        self.todo_status_search.addItem("")
        self.todo_status_search.addItem("")
        self.todo_status_search.addItem("")
        self.todo_status_search.addItem("")
        self.horizontalLayout_91.addWidget(self.todo_status_search)
        self.todo_priority_search = QtWidgets.QComboBox(self.layoutWidget_18)
        self.todo_priority_search.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_priority_search.setFont(font)
        self.todo_priority_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.todo_priority_search.setObjectName("todo_priority_search")
        self.todo_priority_search.addItem("")
        self.todo_priority_search.addItem("")
        self.todo_priority_search.addItem("")
        self.todo_priority_search.addItem("")
        self.todo_priority_search.addItem("")
        self.todo_priority_search.addItem("")
        self.horizontalLayout_91.addWidget(self.todo_priority_search)
        self.todo_severity_search = QtWidgets.QComboBox(self.layoutWidget_18)
        self.todo_severity_search.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_severity_search.setFont(font)
        self.todo_severity_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.todo_severity_search.setObjectName("todo_severity_search")
        self.todo_severity_search.addItem("")
        self.todo_severity_search.addItem("")
        self.todo_severity_search.addItem("")
        self.todo_severity_search.addItem("")
        self.todo_severity_search.addItem("")
        self.horizontalLayout_91.addWidget(self.todo_severity_search)
        self.todo_type_search = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.todo_type_search.setPlaceholderText('Search Start Date')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_type_search.setFont(font)
        self.todo_type_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.todo_type_search.setText("")
        self.todo_type_search.setObjectName("todo_type_search")
        self.horizontalLayout_91.addWidget(self.todo_type_search)
        self.todo_resolution_search = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.todo_resolution_search.setPlaceholderText('Search Resolution Date')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_resolution_search.setFont(font)
        self.todo_resolution_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.todo_resolution_search.setText("")
        self.todo_resolution_search.setObjectName("todo_resolution_search")
        self.horizontalLayout_91.addWidget(self.todo_resolution_search)
        self.verticalLayout_57.addLayout(self.horizontalLayout_91)

        # Todos tree
        self.todos_tree = QtWidgets.QTreeView(self.layoutWidget_18)
        self.update_todos()
        self.todos_tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.todos_tree.setModel(self.todo_model)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todos_tree.setFont(font)
        self.todos_tree.setStyleSheet("background-color: rgb(255,255,255)")
        self.todos_tree.setColumnWidth(0, 140 * .75)
        self.todos_tree.setColumnWidth(1, 140 * .75)
        self.todos_tree.setColumnWidth(2, 150 * .75)
        self.todos_tree.setColumnWidth(3, 100 * .75)
        self.todos_tree.setColumnWidth(4, 100 * .75)
        self.todos_tree.setColumnWidth(5, 100 * .75)
        self.todos_tree.setColumnWidth(6, 145 * .75)
        self.todos_tree.setColumnWidth(7, 130 * .75)
        self.todos_tree.setAlternatingRowColors(True)
        self.todos_tree.setObjectName("todos_tree")
        self.verticalLayout_57.addWidget(self.todos_tree)
        self.horizontalLayout_92 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_92.setObjectName("horizontalLayout_92")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_92.addItem(spacerItem22)
        # self.previous_todos = QtWidgets.QPushButton(self.layoutWidget_18)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.previous_todos.setFont(font)
        # self.previous_todos.setStyleSheet("background-color: rgb(255,255,255)")
        # self.previous_todos.setObjectName("previous_todos")
        # self.horizontalLayout_92.addWidget(self.previous_todos)
        # self.next_todos = QtWidgets.QPushButton(self.layoutWidget_18)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.next_todos.setFont(font)
        # self.next_todos.setStyleSheet("background-color: rgb(255,255,255)")
        # self.next_todos.setObjectName("next_todos")
        # self.horizontalLayout_92.addWidget(self.next_todos)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_92.addItem(spacerItem23)
        self.verticalLayout_57.addLayout(self.horizontalLayout_92)
        self.main_widget.addWidget(self.todos_page)
        self.new_todo_page = QtWidgets.QWidget()
        self.new_todo_page.setObjectName("new_todo_page")
        self.new_todo_lb = QtWidgets.QLabel(self.new_todo_page)
        self.new_todo_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.new_todo_lb.setFont(font)
        self.new_todo_lb.setStyleSheet("")
        self.new_todo_lb.setObjectName("new_todo_lb")
        self.scrollArea_13 = QtWidgets.QScrollArea(self.new_todo_page)
        self.scrollArea_13.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.scrollArea_13.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollArea_13.setObjectName("scrollArea_13")
        self.scrollAreaWidgetContents_13 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_13.setGeometry(QtCore.QRect(0, 0, 1039, 679))
        self.scrollAreaWidgetContents_13.setObjectName("scrollAreaWidgetContents_13")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_13)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout()
        self.verticalLayout_49.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_49.setSpacing(7)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout()
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_163 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_163.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_163.setFont(font)
        self.label_163.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_163.setObjectName("label_163")
        self.gridLayout_14.addWidget(self.label_163, 0, 0, 1, 1)
        self.todo_id_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.todo_id_lb.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_id_lb.setFont(font)
        self.todo_id_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.todo_id_lb.setText("")
        self.todo_id_lb.setObjectName("todo_id_lb")
        self.gridLayout_14.addWidget(self.todo_id_lb, 0, 3, 1, 1)
        self.label_164 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_164.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_164.setFont(font)
        self.label_164.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_164.setObjectName("label_164")
        self.gridLayout_14.addWidget(self.label_164, 6, 4, 1, 1)
        self.label_165 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_165.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_165.setFont(font)
        self.label_165.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_165.setObjectName("label_165")
        self.gridLayout_14.addWidget(self.label_165, 3, 0, 1, 1)
        self.label_166 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_166.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_166.setFont(font)
        self.label_166.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_166.setObjectName("label_166")
        self.gridLayout_14.addWidget(self.label_166, 2, 4, 1, 1)
        self.label_167 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_167.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_167.setFont(font)
        self.label_167.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_167.setObjectName("label_167")
        self.gridLayout_14.addWidget(self.label_167, 3, 4, 1, 1)
        self.todo_status = QtWidgets.QComboBox(self.scrollAreaWidgetContents_13)
        self.todo_status.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_status.setFont(font)
        self.todo_status.setAutoFillBackground(False)
        self.todo_status.setObjectName("todo_status")
        self.todo_status.addItem("")
        self.todo_status.addItem("")
        self.todo_status.addItem("")
        self.todo_status.addItem("")
        self.gridLayout_14.addWidget(self.todo_status, 2, 3, 1, 1)
        self.label_168 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_168.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_168.setFont(font)
        self.label_168.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_168.setObjectName("label_168")
        self.gridLayout_14.addWidget(self.label_168, 1, 0, 1, 1)
        self.todo_priority = QtWidgets.QComboBox(self.scrollAreaWidgetContents_13)
        self.todo_priority.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_priority.setFont(font)
        self.todo_priority.setAutoFillBackground(False)
        self.todo_priority.setObjectName("todo_priority")
        self.todo_priority.addItem("")
        self.todo_priority.addItem("")
        self.todo_priority.addItem("")
        self.todo_priority.addItem("")
        self.todo_priority.addItem("")
        self.gridLayout_14.addWidget(self.todo_priority, 4, 3, 1, 1)

        # To Do company
        companies_id = self.fetch_query('SELECT id FROM companies')
        companies_title = self.fetch_query('SELECT name FROM companies')
        companies = []
        for c_id, c_title in zip(companies_id, companies_title):
            c = str(c_id) + ' - ' + c_title
            companies.append(c)
        self.todo_company = QtWidgets.QComboBox(self.scrollAreaWidgetContents_13)
        self.todo_company.addItem('0 - No company')
        for company in companies:
            self.todo_company.addItem(company)
        self.todo_company.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_company.setFont(font)
        self.todo_company.setAutoFillBackground(False)
        self.todo_company.setObjectName("todo_company")
        self.gridLayout_14.addWidget(self.todo_company, 6, 6, 1, 1)
        self.label_169 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_169.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_169.setFont(font)
        self.label_169.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_169.setObjectName("label_169")
        self.gridLayout_14.addWidget(self.label_169, 4, 0, 1, 1)
        self.todo_severity = QtWidgets.QComboBox(self.scrollAreaWidgetContents_13)
        self.todo_severity.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_severity.setFont(font)
        self.todo_severity.setAutoFillBackground(False)
        self.todo_severity.setObjectName("todo_severity")
        self.todo_severity.addItem("")
        self.todo_severity.addItem("")
        self.todo_severity.addItem("")
        self.gridLayout_14.addWidget(self.todo_severity, 4, 6, 1, 1)
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.todo_resolutio_date = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_13)
        self.todo_resolutio_date.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_resolutio_date.setFont(font)
        self.todo_resolutio_date.setAutoFillBackground(False)
        self.todo_resolutio_date.setObjectName("todo_resolutio_date")
        self.horizontalLayout_57.addWidget(self.todo_resolutio_date)
        self.todo_resolution_btn = QtWidgets.QToolButton(self.scrollAreaWidgetContents_13)
        self.todo_resolution_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_resolution_btn.setFont(font)
        self.todo_resolution_btn.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.todo_resolution_btn.setObjectName("todo_resolution_btn")
        self.horizontalLayout_57.addWidget(self.todo_resolution_btn)
        self.gridLayout_14.addLayout(self.horizontalLayout_57, 3, 6, 1, 1)
        self.label_170 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_170.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_170.setFont(font)
        self.label_170.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_170.setObjectName("label_170")
        self.gridLayout_14.addWidget(self.label_170, 4, 4, 1, 1)
        self.label_171 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_171.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_171.setFont(font)
        self.label_171.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_171.setObjectName("label_171")
        self.gridLayout_14.addWidget(self.label_171, 6, 0, 1, 1)
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")

        # To do contract
        self.todo_contract = QtWidgets.QComboBox(self.scrollAreaWidgetContents_13)
        self.todo_contract.addItem('0 - No Master Contract')
        for contract in self.contract_list():
            self.todo_contract.addItem(contract)

        self.todo_contract.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_contract.setFont(font)
        self.todo_contract.setAutoFillBackground(False)
        self.todo_contract.setObjectName("todo_contract")
        self.horizontalLayout_58.addWidget(self.todo_contract)
        self.gridLayout_14.addLayout(self.horizontalLayout_58, 6, 3, 1, 1)
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.todo_start_date = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_13)
        self.todo_start_date.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_start_date.setFont(font)
        self.todo_start_date.setAutoFillBackground(False)
        self.todo_start_date.setObjectName("todo_start_date")
        self.horizontalLayout_59.addWidget(self.todo_start_date)
        self.todo_start_btn = QtWidgets.QToolButton(self.scrollAreaWidgetContents_13)
        self.todo_start_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_start_btn.setFont(font)
        self.todo_start_btn.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.todo_start_btn.setObjectName("todo_start_btn")
        self.horizontalLayout_59.addWidget(self.todo_start_btn)
        self.gridLayout_14.addLayout(self.horizontalLayout_59, 3, 3, 1, 1)
        self.todo_subject = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.todo_subject.sizePolicy().hasHeightForWidth())
        self.todo_subject.setSizePolicy(sizePolicy)
        self.todo_subject.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_subject.setFont(font)
        self.todo_subject.setAutoFillBackground(False)
        self.todo_subject.setObjectName("todo_subject")
        self.gridLayout_14.addWidget(self.todo_subject, 1, 3, 1, 1)
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")

        # To do responsible
        people_id = self.fetch_query('SELECT id FROM people')
        first = self.fetch_query('SELECT first FROM people')
        last = self.fetch_query('SELECT last FROM people')
        people = []
        for p_id, p_first, p_last in zip(people_id, first, last):
            c = str(p_id) + ' - ' + p_first + ' ' + p_last
            people.append(c)
        self.todo_responsible = QtWidgets.QComboBox(self.scrollAreaWidgetContents_13)
        for p in people:
            self.todo_responsible.addItem(p)
        self.todo_responsible.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_responsible.setFont(font)
        self.todo_responsible.setAutoFillBackground(False)
        self.todo_responsible.setObjectName("todo_responsible")
        self.horizontalLayout_60.addWidget(self.todo_responsible)
        self.add_responsible = QtWidgets.QPushButton(self.scrollAreaWidgetContents_13)
        self.add_responsible.setMaximumSize(QtCore.QSize(30, 16777215))
        self.add_responsible.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.add_responsible.setObjectName("add_responsible")
        self.horizontalLayout_60.addWidget(self.add_responsible)
        self.gridLayout_14.addLayout(self.horizontalLayout_60, 2, 6, 1, 1)
        self.label_172 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_172.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_172.setFont(font)
        self.label_172.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_172.setObjectName("label_172")
        self.gridLayout_14.addWidget(self.label_172, 2, 0, 1, 1)
        self.verticalLayout_50.addLayout(self.gridLayout_14)
        self.label_173 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_173.setText("")
        self.label_173.setObjectName("label_173")
        self.verticalLayout_50.addWidget(self.label_173)
        self.label_174 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_174.setFont(font)
        self.label_174.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(75, 75, 75);")
        self.label_174.setObjectName("label_174")
        self.verticalLayout_50.addWidget(self.label_174)
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.todo_description = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_13)
        self.todo_description.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.todo_description.setFont(font)
        self.todo_description.setAutoFillBackground(False)
        self.todo_description.setObjectName("todo_description")
        self.horizontalLayout_61.addWidget(self.todo_description)
        self.verticalLayout_50.addLayout(self.horizontalLayout_61)
        self.verticalLayout_49.addLayout(self.verticalLayout_50)
        self.verticalLayout_48.addLayout(self.verticalLayout_49)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_48.addItem(spacerItem24)
        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_13)
        self.layoutWidget_17 = QtWidgets.QWidget(self.new_todo_page)
        self.layoutWidget_17.setGeometry(QtCore.QRect(652.5, 22.5, 146.25, 22.5))
        self.layoutWidget_17.setObjectName("layoutWidget_17")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout(self.layoutWidget_17)
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.save_todo = QtWidgets.QPushButton(self.layoutWidget_17)
        self.save_todo.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.save_todo.setObjectName("save_todo")
        self.horizontalLayout_62.addWidget(self.save_todo)
        self.cancel_todo = QtWidgets.QPushButton(self.layoutWidget_17)
        self.cancel_todo.setStyleSheet("background-color: rgb(242, 242, 247);")
        self.cancel_todo.setObjectName("cancel_todo")
        self.horizontalLayout_62.addWidget(self.cancel_todo)
        self.main_widget.addWidget(self.new_todo_page)
        self.library_page = QtWidgets.QWidget()
        self.library_page.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.library_page.setObjectName("library_page")
        self.library_lb = QtWidgets.QLabel(self.library_page)
        self.library_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.library_lb.setFont(font)
        self.library_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.library_lb.setObjectName("library_lb")
        self.layoutWidget6 = QtWidgets.QWidget(self.library_page)
        self.layoutWidget6.setGeometry(QtCore.QRect(22.5, 67.5, 780, 495))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.document_type = QtWidgets.QHBoxLayout()
        self.document_type.setObjectName("document_type")
        self.document_type.setAlignment(QtCore.Qt.AlignLeft)
        self.document_type_search = QtWidgets.QComboBox(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.document_type_search.setFont(font)
        self.document_type_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.document_type_search.setFixedWidth(150)
        for t in ['Any', 'Contracts', 'Reminders', 'Risks']:
            self.document_type_search.addItem(t)
        self.document_type.addWidget(self.document_type_search)
        self.verticalLayout_3.addLayout(self.document_type)

        self.library_searches = QtWidgets.QHBoxLayout()
        self.library_searches.setObjectName("library_searches")
        self.document_id_search = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.document_id_search.setFixedWidth(100 * .75)
        self.document_id_search.setPlaceholderText('Search Id')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.document_id_search.setFont(font)
        self.document_id_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.document_id_search.setText("")
        self.document_id_search.setObjectName("document_id_search")
        self.library_searches.addWidget(self.document_id_search)

        self.document_name_search = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.document_name_search.setFixedWidth(380 * .75)
        self.document_name_search.setPlaceholderText('Search Name')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.document_name_search.setFont(font)
        self.document_name_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.document_name_search.setText("")
        self.document_name_search.setObjectName("document_name_search")
        self.library_searches.addWidget(self.document_name_search)

        self.document_url_search = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.document_url_search.setFixedWidth(340 * .75)
        self.document_url_search.setPlaceholderText('Search Url')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.document_url_search.setFont(font)
        self.document_url_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.document_url_search.setText("")
        self.document_url_search.setObjectName("document_url_search")
        self.library_searches.addWidget(self.document_url_search)

        self.document_date_search = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.document_date_search.setPlaceholderText('Search Date')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.document_date_search.setFont(font)
        self.document_date_search.setStyleSheet("background-color: rgb(255,255,255)")
        self.document_date_search.setText("")
        self.document_date_search.setObjectName("document_date_search")
        self.library_searches.addWidget(self.document_date_search)

        self.verticalLayout_3.addLayout(self.library_searches)

        # Library Tree
        self.library_tree = QtWidgets.QTreeView(self.layoutWidget6)
        self.library_tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.library_tree.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.library_tree.setObjectName("library_tree")
        self.library_tree.setAlternatingRowColors(True)
        self.verticalLayout_3.addWidget(self.library_tree)
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_86.addItem(spacerItem25)
        self.open_document = QtWidgets.QPushButton(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.open_document.setFont(font)
        self.open_document.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.open_document.setObjectName("open_document")
        self.horizontalLayout_86.addWidget(self.open_document)
        self.delete_document = QtWidgets.QPushButton(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_document.setFont(font)
        self.delete_document.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delete_document.setObjectName("delete_document")
        self.horizontalLayout_86.addWidget(self.delete_document)
        self.verticalLayout_3.addLayout(self.horizontalLayout_86)
        self.main_widget.addWidget(self.library_page)
        self.reports_page = QtWidgets.QWidget()
        self.reports_page.setObjectName("reports_page")
        self.reports_lb = QtWidgets.QLabel(self.reports_page)
        self.reports_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reports_lb.setFont(font)
        self.reports_lb.setObjectName("reports_lb")
        self.main_widget.addWidget(self.reports_page)
        self.archives_page = QtWidgets.QWidget()
        self.archives_page.setObjectName("archives_page")
        self.archives_lb = QtWidgets.QLabel(self.archives_page)
        self.archives_lb.setGeometry(QtCore.QRect(22.5, 15, 157.5, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.archives_lb.setFont(font)
        self.archives_lb.setObjectName("archives_lb")
        self.main_widget.addWidget(self.archives_page)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.frame.raise_()
        self.top_menu_frame.raise_()
        self.main_frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.new_contract, self.export_contracts)
        MainWindow.setTabOrder(self.export_contracts, self.contract_type_menu)
        MainWindow.setTabOrder(self.contract_type_menu, self.edit_contract_btn)
        MainWindow.setTabOrder(self.edit_contract_btn, self.delete_contract_btn)
        MainWindow.setTabOrder(self.delete_contract_btn, self.archive_contract_btn)
        MainWindow.setTabOrder(self.archive_contract_btn, self.favorite_contract_btn)
        MainWindow.setTabOrder(self.favorite_contract_btn, self.contract_id_search)
        MainWindow.setTabOrder(self.contract_id_search, self.contract_title_search)
        MainWindow.setTabOrder(self.contract_title_search, self.contract_type_search)
        MainWindow.setTabOrder(self.contract_type_search, self.contract_classificatiion_type)
        MainWindow.setTabOrder(self.contract_classificatiion_type, self.contract_start_type)
        MainWindow.setTabOrder(self.contract_start_type, self.contract_end_search)
        MainWindow.setTabOrder(self.contract_end_search, self.contract_value_search)
        MainWindow.setTabOrder(self.contract_value_search, self.contract_status_menu)
        MainWindow.setTabOrder(self.contract_status_menu, self.contracts_tree)
        # MainWindow.setTabOrder(self.contracts_tree, self.previous_contracts)
        # MainWindow.setTabOrder(self.previous_contracts, self.next_contracts)
        # MainWindow.setTabOrder(self.next_contracts, self.save_contract)
        MainWindow.setTabOrder(self.save_contract, self.cancel_contract)
        MainWindow.setTabOrder(self.cancel_contract, self.scrollArea_8)
        MainWindow.setTabOrder(self.scrollArea_8, self.contract_title)
        MainWindow.setTabOrder(self.contract_title, self.contract_type)
        MainWindow.setTabOrder(self.contract_type, self.contract_category)
        MainWindow.setTabOrder(self.contract_category, self.contract_classification)
        MainWindow.setTabOrder(self.contract_classification, self.contract_reference)
        MainWindow.setTabOrder(self.contract_reference, self.contract_account)
        MainWindow.setTabOrder(self.contract_account, self.contract_status)
        MainWindow.setTabOrder(self.contract_status, self.contract_master)
        MainWindow.setTabOrder(self.contract_master, self.contract_parties)
        MainWindow.setTabOrder(self.contract_parties, self.add_party)
        MainWindow.setTabOrder(self.add_party, self.open_party)
        MainWindow.setTabOrder(self.open_party, self.delete_party)
        MainWindow.setTabOrder(self.delete_party, self.contract_value)
        MainWindow.setTabOrder(self.contract_value, self.contract_currency)
        MainWindow.setTabOrder(self.contract_currency, self.term_none)
        MainWindow.setTabOrder(self.term_none, self.term_fixed)
        MainWindow.setTabOrder(self.term_fixed, self.term_recurring)
        MainWindow.setTabOrder(self.term_recurring, self.term_rolling)
        MainWindow.setTabOrder(self.term_rolling, self.contract_start)
        MainWindow.setTabOrder(self.contract_start, self.contract_start_btn)
        MainWindow.setTabOrder(self.contract_start_btn, self.contract_end)
        MainWindow.setTabOrder(self.contract_end, self.contract_end_btn)
        MainWindow.setTabOrder(self.contract_end_btn, self.contract_review)
        MainWindow.setTabOrder(self.contract_review, self.contract_review_btn)
        MainWindow.setTabOrder(self.contract_review_btn, self.contract_cancel)
        MainWindow.setTabOrder(self.contract_cancel, self.contract_cancel_btn)
        MainWindow.setTabOrder(self.contract_cancel_btn, self.contract_extension)
        MainWindow.setTabOrder(self.contract_extension, self.contract_description)
        MainWindow.setTabOrder(self.contract_description, self.contract_attachments)
        MainWindow.setTabOrder(self.contract_attachments, self.contract_add_attachment)
        MainWindow.setTabOrder(self.contract_add_attachment, self.contract_open_attachment)
        MainWindow.setTabOrder(self.contract_open_attachment, self.contract_delete_attachment)
        MainWindow.setTabOrder(self.contract_delete_attachment, self.new_person)
        MainWindow.setTabOrder(self.new_person, self.export_people)
        MainWindow.setTabOrder(self.export_people, self.people_type_menu)
        MainWindow.setTabOrder(self.people_type_menu, self.edit_person_btn)
        MainWindow.setTabOrder(self.edit_person_btn, self.delete_person_btn)
        MainWindow.setTabOrder(self.delete_person_btn, self.archive_person_btn)
        MainWindow.setTabOrder(self.archive_person_btn, self.favorite_person_btn)
        MainWindow.setTabOrder(self.favorite_person_btn, self.person_id_search)
        MainWindow.setTabOrder(self.person_id_search, self.person_first_search)
        MainWindow.setTabOrder(self.person_first_search, self.person_last_search)
        MainWindow.setTabOrder(self.person_last_search, self.person_email_search)
        MainWindow.setTabOrder(self.person_email_search, self.person_phone_search)
        MainWindow.setTabOrder(self.person_phone_search, self.person_mobile_search)
        MainWindow.setTabOrder(self.person_mobile_search, self.person_job_search)
        MainWindow.setTabOrder(self.person_job_search, self.person_type_search)
        MainWindow.setTabOrder(self.person_type_search, self.people_tree)
        # MainWindow.setTabOrder(self.people_tree, self.previous_people)
        # MainWindow.setTabOrder(self.previous_people, self.next_people)
        # MainWindow.setTabOrder(self.next_people, self.save_person)
        MainWindow.setTabOrder(self.save_person, self.cancel_person)
        MainWindow.setTabOrder(self.cancel_person, self.scrollArea_9)
        MainWindow.setTabOrder(self.scrollArea_9, self.salutation)
        MainWindow.setTabOrder(self.salutation, self.first_name)
        MainWindow.setTabOrder(self.first_name, self.last_name)
        MainWindow.setTabOrder(self.last_name, self.gender)
        MainWindow.setTabOrder(self.gender, self.job)
        MainWindow.setTabOrder(self.job, self.company)
        MainWindow.setTabOrder(self.company, self.person_type)
        MainWindow.setTabOrder(self.person_type, self.phone)
        MainWindow.setTabOrder(self.phone, self.mobile)
        MainWindow.setTabOrder(self.mobile, self.email)
        MainWindow.setTabOrder(self.email, self.fax)
        MainWindow.setTabOrder(self.fax, self.new_company)
        MainWindow.setTabOrder(self.new_company, self.export_companies)
        MainWindow.setTabOrder(self.export_companies, self.company_type_menu)
        MainWindow.setTabOrder(self.company_type_menu, self.edit_company_btn)
        MainWindow.setTabOrder(self.edit_company_btn, self.delete_company_btn)
        MainWindow.setTabOrder(self.delete_company_btn, self.archive_company_btn)
        MainWindow.setTabOrder(self.archive_company_btn, self.favorite_company_btn)
        MainWindow.setTabOrder(self.favorite_company_btn, self.company_id_search)
        MainWindow.setTabOrder(self.company_id_search, self.company_name_search)
        MainWindow.setTabOrder(self.company_name_search, self.company_address_search)
        MainWindow.setTabOrder(self.company_address_search, self.company_city_search)
        MainWindow.setTabOrder(self.company_city_search, self.company_state_search)
        MainWindow.setTabOrder(self.company_state_search, self.company_zip_search)
        MainWindow.setTabOrder(self.company_zip_search, self.company_country_search)
        MainWindow.setTabOrder(self.company_country_search, self.company_website_search)
        MainWindow.setTabOrder(self.company_website_search, self.companies_tree)
        # MainWindow.setTabOrder(self.companies_tree, self.previous_companies)
        # MainWindow.setTabOrder(self.previous_companies, self.next_companies)
        # MainWindow.setTabOrder(self.next_companies, self.save_company)
        MainWindow.setTabOrder(self.save_company, self.cancel_company)
        MainWindow.setTabOrder(self.cancel_company, self.scrollArea_10)
        MainWindow.setTabOrder(self.scrollArea_10, self.company_name)
        MainWindow.setTabOrder(self.company_name, self.company_type)
        MainWindow.setTabOrder(self.company_type, self.address_1)
        MainWindow.setTabOrder(self.address_1, self.address_2)
        MainWindow.setTabOrder(self.address_2, self.city)
        MainWindow.setTabOrder(self.city, self.state)
        MainWindow.setTabOrder(self.state, self.zip)
        MainWindow.setTabOrder(self.zip, self.country)
        MainWindow.setTabOrder(self.country, self.segment)
        MainWindow.setTabOrder(self.segment, self.company_number)
        MainWindow.setTabOrder(self.company_number, self.website)
        MainWindow.setTabOrder(self.website, self.company_email)
        MainWindow.setTabOrder(self.company_email, self.contact)
        MainWindow.setTabOrder(self.contact, self.company_fax)
        MainWindow.setTabOrder(self.company_fax, self.new_reminder)
        MainWindow.setTabOrder(self.new_reminder, self.export_reminders)
        MainWindow.setTabOrder(self.export_reminders, self.reminder_type_menu)
        MainWindow.setTabOrder(self.reminder_type_menu, self.edit_reminder_btn)
        MainWindow.setTabOrder(self.edit_reminder_btn, self.delete_reminder_btn)
        MainWindow.setTabOrder(self.delete_reminder_btn, self.archive_reminder_btn)
        MainWindow.setTabOrder(self.archive_reminder_btn, self.complete_reminder_btn)
        MainWindow.setTabOrder(self.complete_reminder_btn, self.uncomplete_reminder_btn)
        MainWindow.setTabOrder(self.uncomplete_reminder_btn, self.snooze_reminder_btn)
        MainWindow.setTabOrder(self.snooze_reminder_btn, self.reminder_id_search)
        MainWindow.setTabOrder(self.reminder_id_search, self.reminder_name_search)
        MainWindow.setTabOrder(self.reminder_name_search, self.reminder_description_search)
        MainWindow.setTabOrder(self.reminder_description_search, self.reminder_date_search)
        MainWindow.setTabOrder(self.reminder_date_search, self.reminder_complete_search)
        MainWindow.setTabOrder(self.reminder_complete_search, self.reminder_snoozed_search)
        MainWindow.setTabOrder(self.reminder_snoozed_search, self.reminders_tree)
        # MainWindow.setTabOrder(self.reminders_tree, self.previous_reminders)
        # MainWindow.setTabOrder(self.previous_reminders, self.next_reminders)
        # MainWindow.setTabOrder(self.next_reminders, self.save_reminder)
        MainWindow.setTabOrder(self.save_reminder, self.cancel_reminder)
        MainWindow.setTabOrder(self.cancel_reminder, self.scrollArea_11)
        MainWindow.setTabOrder(self.scrollArea_11, self.reminder_name)
        MainWindow.setTabOrder(self.reminder_name, self.reminder_contract)
        MainWindow.setTabOrder(self.reminder_contract, self.reminder_company)
        MainWindow.setTabOrder(self.reminder_company, self.reminder_people)
        MainWindow.setTabOrder(self.reminder_people, self.reminder_add_party)
        MainWindow.setTabOrder(self.reminder_add_party, self.reminder_open_party)
        MainWindow.setTabOrder(self.reminder_open_party, self.reminder_delete_party)
        MainWindow.setTabOrder(self.reminder_delete_party, self.reminder_description)
        MainWindow.setTabOrder(self.reminder_description, self.reminder_attachments)
        MainWindow.setTabOrder(self.reminder_attachments, self.reminder_add_attachment)
        MainWindow.setTabOrder(self.reminder_add_attachment, self.reminder_open_attachment)
        MainWindow.setTabOrder(self.reminder_open_attachment, self.reminder_delete_attachment)
        MainWindow.setTabOrder(self.reminder_delete_attachment, self.reminder_complete)
        MainWindow.setTabOrder(self.reminder_complete, self.reminder_snoozed)
        MainWindow.setTabOrder(self.reminder_snoozed, self.specific_date_radio)
        MainWindow.setTabOrder(self.specific_date_radio, self.reminder_specific_date)
        MainWindow.setTabOrder(self.reminder_specific_date, self.specific_date_btn)
        MainWindow.setTabOrder(self.specific_date_btn, self.relative_date_radio)
        MainWindow.setTabOrder(self.relative_date_radio, self.reminder_relative_date)
        MainWindow.setTabOrder(self.reminder_relative_date, self.time_type)
        MainWindow.setTabOrder(self.time_type, self.before)
        MainWindow.setTabOrder(self.before, self.key_date)
        MainWindow.setTabOrder(self.key_date, self.do_not_recur_radio)
        MainWindow.setTabOrder(self.do_not_recur_radio, self.recur_radio)
        MainWindow.setTabOrder(self.recur_radio, self.recur_type)
        MainWindow.setTabOrder(self.recur_type, self.recur_until_specific)
        MainWindow.setTabOrder(self.recur_until_specific, self.recur_until_specific_2)
        MainWindow.setTabOrder(self.recur_until_specific_2, self.recur_until_btn)
        MainWindow.setTabOrder(self.recur_until_btn, self.until_key_date_radio)
        MainWindow.setTabOrder(self.until_key_date_radio, self.until_key_date)
        MainWindow.setTabOrder(self.until_key_date, self.recur_indefinitely_radio)
        MainWindow.setTabOrder(self.recur_indefinitely_radio, self.new_risk)
        MainWindow.setTabOrder(self.new_risk, self.export_risks)
        MainWindow.setTabOrder(self.export_risks, self.risk_type_menu)
        MainWindow.setTabOrder(self.risk_type_menu, self.edit_risk_btn)
        MainWindow.setTabOrder(self.edit_risk_btn, self.delete_risk_btn)
        MainWindow.setTabOrder(self.delete_risk_btn, self.archive_risk_btn)
        MainWindow.setTabOrder(self.archive_risk_btn, self.favorite_risk_btn)
        MainWindow.setTabOrder(self.favorite_risk_btn, self.risk_id_search)
        MainWindow.setTabOrder(self.risk_id_search, self.risk_name_search)
        MainWindow.setTabOrder(self.risk_name_search, self.risk_type_search)
        MainWindow.setTabOrder(self.risk_type_search, self.risk_severity_search)
        MainWindow.setTabOrder(self.risk_severity_search, self.risk_end_search)
        MainWindow.setTabOrder(self.risk_end_search, self.risk_expired_search)
        MainWindow.setTabOrder(self.risk_expired_search, self.risk_filename_search)
        MainWindow.setTabOrder(self.risk_filename_search, self.risks_tree)
        # MainWindow.setTabOrder(self.risks_tree, self.previous_risks)
        # MainWindow.setTabOrder(self.previous_risks, self.next_risks)
        # MainWindow.setTabOrder(self.next_risks, self.save_risk)
        MainWindow.setTabOrder(self.save_risk, self.cancel_risk)
        MainWindow.setTabOrder(self.cancel_risk, self.scrollArea_12)
        MainWindow.setTabOrder(self.scrollArea_12, self.risk_name)
        MainWindow.setTabOrder(self.risk_name, self.risk_contract)
        MainWindow.setTabOrder(self.risk_contract, self.risk_probability)
        MainWindow.setTabOrder(self.risk_probability, self.risk_impact)
        MainWindow.setTabOrder(self.risk_impact, self.risk_type)
        MainWindow.setTabOrder(self.risk_type, self.risk_notes)
        MainWindow.setTabOrder(self.risk_notes, self.risk_mitigation)
        MainWindow.setTabOrder(self.risk_mitigation, self.risk_attachments)
        MainWindow.setTabOrder(self.risk_attachments, self.risk_add_attachment_3)
        MainWindow.setTabOrder(self.risk_add_attachment_3, self.risk_open_attachment_3)
        MainWindow.setTabOrder(self.risk_open_attachment_3, self.risk_delete_attachment_3)
        MainWindow.setTabOrder(self.risk_delete_attachment_3, self.new_todo)
        MainWindow.setTabOrder(self.new_todo, self.export_todos)
        MainWindow.setTabOrder(self.export_todos, self.todos_type_menu)
        MainWindow.setTabOrder(self.todos_type_menu, self.edit_todo_btn)
        MainWindow.setTabOrder(self.edit_todo_btn, self.delete_todo_btn)
        MainWindow.setTabOrder(self.delete_todo_btn, self.archive_todo_btn)
        MainWindow.setTabOrder(self.archive_todo_btn, self.favorite_todo_btn)
        MainWindow.setTabOrder(self.favorite_todo_btn, self.todo_id_search)
        MainWindow.setTabOrder(self.todo_id_search, self.todo_subject_search)
        MainWindow.setTabOrder(self.todo_subject_search, self.todo_responsible_search)
        MainWindow.setTabOrder(self.todo_responsible_search, self.todo_status_search)
        MainWindow.setTabOrder(self.todo_status_search, self.todo_priority_search)
        MainWindow.setTabOrder(self.todo_priority_search, self.todo_severity_search)
        MainWindow.setTabOrder(self.todo_severity_search, self.todo_type_search)
        MainWindow.setTabOrder(self.todo_type_search, self.todo_resolution_search)
        MainWindow.setTabOrder(self.todo_resolution_search, self.todos_tree)
        # MainWindow.setTabOrder(self.todos_tree, self.previous_todos)
        # MainWindow.setTabOrder(self.previous_todos, self.next_todos)
        # MainWindow.setTabOrder(self.next_todos, self.save_todo)
        MainWindow.setTabOrder(self.save_todo, self.cancel_todo)
        MainWindow.setTabOrder(self.cancel_todo, self.scrollArea_13)
        MainWindow.setTabOrder(self.scrollArea_13, self.todo_subject)
        MainWindow.setTabOrder(self.todo_subject, self.todo_status)
        MainWindow.setTabOrder(self.todo_status, self.todo_responsible)
        MainWindow.setTabOrder(self.todo_responsible, self.add_responsible)
        MainWindow.setTabOrder(self.add_responsible, self.todo_start_date)
        MainWindow.setTabOrder(self.todo_start_date, self.todo_start_btn)
        MainWindow.setTabOrder(self.todo_start_btn, self.todo_resolutio_date)
        MainWindow.setTabOrder(self.todo_resolutio_date, self.todo_resolution_btn)
        MainWindow.setTabOrder(self.todo_resolution_btn, self.todo_priority)
        MainWindow.setTabOrder(self.todo_priority, self.todo_severity)
        MainWindow.setTabOrder(self.todo_severity, self.todo_contract)
        MainWindow.setTabOrder(self.todo_contract, self.todo_company)
        MainWindow.setTabOrder(self.todo_company, self.todo_description)
        MainWindow.setTabOrder(self.todo_description, self.library_tree)
        MainWindow.setTabOrder(self.library_tree, self.open_document)
        MainWindow.setTabOrder(self.open_document, self.delete_document)
        MainWindow.setTabOrder(self.delete_document, self.contracts_search)
        MainWindow.setTabOrder(self.contracts_search, self.search_btn)
        MainWindow.setTabOrder(self.search_btn, self.contracts_filter)
        MainWindow.setTabOrder(self.contracts_filter, self.scrollArea)
        # MainWindow.setTabOrder(self.scrollArea, self.dashboard_btn)
        # MainWindow.setTabOrder(self.dashboard_btn, self.contracts_btn)
        MainWindow.setTabOrder(self.contracts_btn, self.people_btn)
        MainWindow.setTabOrder(self.people_btn, self.companies_btn)
        MainWindow.setTabOrder(self.companies_btn, self.reminders_btn)
        MainWindow.setTabOrder(self.reminders_btn, self.risks_btn)
        MainWindow.setTabOrder(self.risks_btn, self.todos_btn)
        MainWindow.setTabOrder(self.todos_btn, self.library_btn)
        # MainWindow.setTabOrder(self.library_btn, self.reports_btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contracts By Elvnosix"))
        icon = QtGui.QIcon(":/images/images/icon - black.svg")
        MainWindow.setWindowIcon(icon)
        self.contracts_search.setPlaceholderText(_translate("MainWindow", "Search contracts"))
        self.contracts_filter.setText(_translate("MainWindow", "Filters"))
        # self.dashboard_btn.setText(_translate("MainWindow", "Dashboard"))
        self.contracts_btn.setText(_translate("MainWindow", "Contracts"))
        self.people_btn.setText(_translate("MainWindow", "People"))
        self.companies_btn.setText(_translate("MainWindow", "Companies"))
        self.reminders_btn.setText(_translate("MainWindow", "Reminders"))
        self.risks_btn.setText(_translate("MainWindow", "Risks"))
        self.todos_btn.setText(_translate("MainWindow", "To-Dos"))
        self.library_btn.setText(_translate("MainWindow", "Library"))
        # self.reports_btn.setText(_translate("MainWindow", "Reports"))
        # self.dashboard_lb.setText(_translate("MainWindow", "Dashboard"))
        self.contracts_lb.setText(_translate("MainWindow", "Contracts"))
        self.contract_type_menu.setItemText(0, _translate("MainWindow", "All Contracts"))
        self.contract_type_menu.setItemText(1, _translate("MainWindow", "All Active Contracts"))
        self.contract_type_menu.setItemText(2, _translate("MainWindow", "All Inactive Contracts"))
        self.contract_type_menu.setItemText(3, _translate("MainWindow", "My Contracts"))
        self.contract_type_menu.setItemText(4, _translate("MainWindow", "My Active Contracts"))
        self.contract_type_menu.setItemText(5, _translate("MainWindow", "My Inactive Contracts"))
        self.contract_type_menu.setItemText(6, _translate("MainWindow", "Active Customer Contracts"))
        self.contract_type_menu.setItemText(7, _translate("MainWindow", "Active Supplier Contracts"))
        self.contract_type_menu.setItemText(8, _translate("MainWindow", "Favorites"))
        self.contract_type_menu.setItemText(9, _translate("MainWindow", "Created Today"))
        self.contract_type_menu.setItemText(10, _translate("MainWindow", "Created This Week"))
        self.contract_type_menu.setItemText(11, _translate("MainWindow", "Created This Month"))
        self.contract_type_menu.setItemText(12, _translate("MainWindow", "Created This Year"))
        self.contract_type_menu.setItemText(13, _translate("MainWindow", "Created Last Month"))
        self.contract_type_menu.setItemText(14, _translate("MainWindow", "Created Last Year"))
        self.contract_type_menu.setItemText(15, _translate("MainWindow", "Archived"))
        self.edit_contract_btn.setText(_translate("MainWindow", "Edit"))
        self.delete_contract_btn.setText(_translate("MainWindow", "Delete"))
        self.archive_contract_btn.setText(_translate("MainWindow", "Archive"))
        self.favorite_contract_btn.setText(_translate("MainWindow", "Mark As Favorite"))
        self.contract_status_menu.setItemText(0, _translate("MainWindow", "Any"))
        self.contract_status_menu.setItemText(1, _translate("MainWindow", "Active"))
        self.contract_status_menu.setItemText(2, _translate("MainWindow", "Expired"))
        self.contract_status_menu.setItemText(3, _translate("MainWindow", "Draft"))
        self.contract_status_menu.setItemText(4, _translate("MainWindow", "Due"))
        self.contract_status_menu.setItemText(5, _translate("MainWindow", "Future"))
        self.contract_status_menu.setItemText(6, _translate("MainWindow", "Closed"))
        # self.previous_contracts.setText(_translate("MainWindow", "Previous"))
        # self.next_contracts.setText(_translate("MainWindow", "Next"))
        self.new_contract.setText(_translate("MainWindow", "New"))
        self.export_contracts.setText(_translate("MainWindow", "Export"))
        # self.print_contracts.setText(_translate("MainWindow", "Print"))
        self.new_contract_lb.setText(_translate("MainWindow", "Contract"))
        self.label_86.setText(_translate("MainWindow", "Category"))
        self.contract_master.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                    "color: rgb(0,0,0)"))
        self.add_party.setText(_translate("MainWindow", "Add"))
        self.open_party.setText(_translate("MainWindow", "Open"))
        self.delete_party.setText(_translate("MainWindow", "Delete"))
        self.contract_category.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                      "color: rgb(0,0,0)"))
        self.label_74.setText(_translate("MainWindow", "Contract Reference"))
        self.term_none.setText(_translate("MainWindow", "None"))
        self.term_fixed.setText(_translate("MainWindow", "Fixed"))
        self.term_recurring.setText(_translate("MainWindow", "Recurring"))
        self.term_rolling.setText(_translate("MainWindow", "Rolling"))
        self.contract_start.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                   "color: rgb(0,0,0)"))
        self.contract_start_btn.setText(_translate("MainWindow", "..."))
        self.label_98.setText(_translate("MainWindow", "Extension Limit"))
        self.label_91.setText(_translate("MainWindow", "Classification"))
        self.contract_cancel.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                    "color: rgb(0,0,0)"))
        self.contract_cancel_btn.setText(_translate("MainWindow", "..."))
        self.contract_value.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                   "color: rgb(0,0,0)"))
        self.label_89.setText(_translate("MainWindow", "Review Date"))
        self.label_78.setText(_translate("MainWindow", "Cancellation Date"))
        self.label_75.setText(_translate("MainWindow", "Type"))
        self.label_94.setText(_translate("MainWindow", "Title"))
        self.label_92.setText(_translate("MainWindow", "Term"))
        self.label_95.setText(_translate("MainWindow", "Start Date"))
        self.label_96.setText(_translate("MainWindow", "Parties"))
        self.contract_review.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                    "color: rgb(0,0,0)"))
        self.contract_review_btn.setText(_translate("MainWindow", "..."))
        self.contract_currency.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                      "color: rgb(0,0,0)"))
        self.contract_currency.setItemText(0, _translate("MainWindow", "Euro"))
        self.contract_currency.setItemText(1, _translate("MainWindow", "Malagasy Ariary"))
        self.contract_currency.setItemText(2, _translate("MainWindow", "US Dollars"))
        self.label_93.setText(_translate("MainWindow", "Account Reference"))
        self.contract_extension.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                       "color: rgb(0,0,0)"))
        self.contract_status.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                    "color: rgb(0,0,0)"))
        self.contract_status.setItemText(0, _translate("MainWindow", "Auto"))
        self.contract_status.setItemText(1, _translate("MainWindow", "Active"))
        self.contract_status.setItemText(2, _translate("MainWindow", "Expired"))
        self.contract_status.setItemText(3, _translate("MainWindow", "Due"))
        self.contract_status.setItemText(4, _translate("MainWindow", "Draft"))
        self.contract_status.setItemText(5, _translate("MainWindow", "Future"))
        self.contract_status.setItemText(6, _translate("MainWindow", "Closed"))
        self.label_80.setText(_translate("MainWindow", "Master Contract"))
        self.label_117.setText(_translate("MainWindow", "End Date"))
        self.contract_type.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                  "color: rgb(0,0,0)"))
        self.label_68.setText(_translate("MainWindow", "Status"))
        self.label_76.setText(_translate("MainWindow", "Currency"))
        self.contract_classification.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                            "color: rgb(0,0,0)"))
        self.contract_classification.setItemText(0, _translate("MainWindow", "Not Selected"))
        self.contract_classification.setItemText(1, _translate("MainWindow", "Customer"))
        self.contract_classification.setItemText(2, _translate("MainWindow", "Supplier"))
        self.label_90.setText(_translate("MainWindow", "Id"))
        self.contract_reference.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                       "color: rgb(0,0,0)"))
        self.contract_account.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                     "color: rgb(0,0,0)"))
        self.label_81.setText(_translate("MainWindow", "Contract Value"))
        self.contract_end.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                 "color: rgb(0,0,0)"))
        self.contract_end_btn.setText(_translate("MainWindow", "..."))
        self.contract_title.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                                   "color: rgb(0,0,0)"))
        self.label_100.setText(_translate("MainWindow", "Description"))
        self.label_102.setText(_translate("MainWindow", "Attachments"))
        self.contract_add_attachment.setText(_translate("MainWindow", "Add"))
        self.contract_open_attachment.setText(_translate("MainWindow", "Open"))
        self.contract_delete_attachment.setText(_translate("MainWindow", "Delete"))
        self.save_contract.setText(_translate("MainWindow", "Save"))
        self.cancel_contract.setText(_translate("MainWindow", "Cancel"))
        self.people_lb.setText(_translate("MainWindow", "People"))
        self.people_type_menu.setItemText(0, _translate("MainWindow", "All People"))
        self.people_type_menu.setItemText(1, _translate("MainWindow", "Me"))
        self.people_type_menu.setItemText(2, _translate("MainWindow", "People With Contracts"))
        self.people_type_menu.setItemText(3, _translate("MainWindow", "Favorites"))
        self.people_type_menu.setItemText(4, _translate("MainWindow", "Created Today"))
        self.people_type_menu.setItemText(5, _translate("MainWindow", "Created This Week"))
        self.people_type_menu.setItemText(6, _translate("MainWindow", "Created This Month"))
        self.people_type_menu.setItemText(7, _translate("MainWindow", "Created This Year"))
        self.people_type_menu.setItemText(8, _translate("MainWindow", "Created Last Month"))
        self.people_type_menu.setItemText(9, _translate("MainWindow", "Created Last Year"))
        self.people_type_menu.setItemText(10, _translate("MainWindow", "Archived"))
        self.edit_person_btn.setText(_translate("MainWindow", "Edit"))
        self.delete_person_btn.setText(_translate("MainWindow", "Delete"))
        self.archive_person_btn.setText(_translate("MainWindow", "Archive"))
        self.favorite_person_btn.setText(_translate("MainWindow", "Mark As Favorite"))
        # self.previous_people.setText(_translate("MainWindow", "Previous"))
        # self.next_people.setText(_translate("MainWindow", "Next"))
        self.new_person.setText(_translate("MainWindow", "New"))
        self.export_people.setText(_translate("MainWindow", "Export"))
        # self.print_people.setText(_translate("MainWindow", "Print"))
        self.new_person_lb.setText(_translate("MainWindow", "Person"))
        self.save_person.setText(_translate("MainWindow", "Save"))
        self.cancel_person.setText(_translate("MainWindow", "Cancel"))
        self.label_103.setText(_translate("MainWindow", "Type"))
        self.label_104.setText(_translate("MainWindow", "Salutation"))
        self.person_type.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.salutation.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_105.setText(_translate("MainWindow", "Fax"))
        self.label_106.setText(_translate("MainWindow", "Gender"))
        self.email.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.phone.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_107.setText(_translate("MainWindow", "Email Address"))
        self.label_108.setText(_translate("MainWindow", "Mobile"))
        self.fax.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_109.setText(_translate("MainWindow", "Company"))
        self.last_name.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.company.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.mobile.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_111.setText(_translate("MainWindow", "Job Title"))
        self.label_112.setText(_translate("MainWindow", "First Name"))
        self.job.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.first_name.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_113.setText(_translate("MainWindow", "Last Name"))
        self.label_114.setText(_translate("MainWindow", "Phone"))
        self.label_115.setText(_translate("MainWindow", "Id"))
        self.gender.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.gender.setItemText(0, _translate("MainWindow", "Not Selected"))
        self.gender.setItemText(1, _translate("MainWindow", "Male"))
        self.gender.setItemText(2, _translate("MainWindow", "Female"))
        self.companies_lb.setText(_translate("MainWindow", "Companies"))
        self.company_type_menu.setItemText(0, _translate("MainWindow", "All Companies"))
        self.company_type_menu.setItemText(1, _translate("MainWindow", "Favorites"))
        self.company_type_menu.setItemText(2, _translate("MainWindow", "Created Today"))
        self.company_type_menu.setItemText(3, _translate("MainWindow", "Created This Week"))
        self.company_type_menu.setItemText(4, _translate("MainWindow", "Created This Month"))
        self.company_type_menu.setItemText(5, _translate("MainWindow", "Created This Year"))
        self.company_type_menu.setItemText(6, _translate("MainWindow", "Created Last Month"))
        self.company_type_menu.setItemText(7, _translate("MainWindow", "Created Last Year"))
        self.company_type_menu.setItemText(8, _translate("MainWindow", "Archived"))
        self.edit_company_btn.setText(_translate("MainWindow", "Edit"))
        self.delete_company_btn.setText(_translate("MainWindow", "Delete"))
        self.archive_company_btn.setText(_translate("MainWindow", "Archive"))
        self.favorite_company_btn.setText(_translate("MainWindow", "Mark As Favorite"))
        # self.previous_companies.setText(_translate("MainWindow", "Previous"))
        # self.next_companies.setText(_translate("MainWindow", "Next"))
        self.new_company.setText(_translate("MainWindow", "New"))
        self.export_companies.setText(_translate("MainWindow", "Export"))
        # self.print_companies.setText(_translate("MainWindow", "Print"))
        self.new_company_lb.setText(_translate("MainWindow", "Company"))
        self.save_company.setText(_translate("MainWindow", "Save"))
        self.cancel_company.setText(_translate("MainWindow", "Cancel"))
        self.zip.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.address_2.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.company_name.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_116.setText(_translate("MainWindow", "Type"))
        self.label_125.setText(_translate("MainWindow", "Zip Code"))
        self.contact.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_126.setText(_translate("MainWindow", "Segment"))
        self.address_1.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_127.setText(_translate("MainWindow", "Name"))
        self.label_128.setText(_translate("MainWindow", "Contact Number"))
        self.label_129.setText(_translate("MainWindow", "Address 2"))
        self.company_fax.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_130.setText(_translate("MainWindow", "Id"))
        self.label_131.setText(_translate("MainWindow", "Fax Number"))
        self.segment.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.website.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.country.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_132.setText(_translate("MainWindow", "Address 1"))
        self.label_133.setText(_translate("MainWindow", "Company Number"))
        self.label_134.setText(_translate("MainWindow", "Country"))
        self.company_email.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_135.setText(_translate("MainWindow", "Email Address"))
        self.label_137.setText(_translate("MainWindow", "Website"))
        self.company_number.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.company_type.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_138.setText(_translate("MainWindow", "City"))
        self.label_139.setText(_translate("MainWindow", "State"))
        self.city.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.state.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.reminder_lb.setText(_translate("MainWindow", "Reminders"))
        self.reminder_type_menu.setItemText(0, _translate("MainWindow", "All Reminders"))
        self.reminder_type_menu.setItemText(1, _translate("MainWindow", "Current Reminders"))
        self.reminder_type_menu.setItemText(2, _translate("MainWindow", "Snoozed"))
        self.reminder_type_menu.setItemText(3, _translate("MainWindow", "Upcoming Reminders"))
        self.reminder_type_menu.setItemText(4, _translate("MainWindow", "Completed Reminders"))
        self.reminder_type_menu.setItemText(5, _translate("MainWindow", "Upcoming This Week"))
        self.reminder_type_menu.setItemText(6, _translate("MainWindow", "Upcoming This Month"))
        self.reminder_type_menu.setItemText(7, _translate("MainWindow", "Archived"))
        self.edit_reminder_btn.setText(_translate("MainWindow", "Edit"))
        self.delete_reminder_btn.setText(_translate("MainWindow", "Delete"))
        self.archive_reminder_btn.setText(_translate("MainWindow", "Archive"))
        self.complete_reminder_btn.setText(_translate("MainWindow", "Complete"))
        self.uncomplete_reminder_btn.setText(_translate("MainWindow", "Uncomplete"))
        self.snooze_reminder_btn.setText(_translate("MainWindow", "Snooze"))
        # self.previous_reminders.setText(_translate("MainWindow", "Previous"))
        # self.next_reminders.setText(_translate("MainWindow", "Next"))
        self.new_reminder.setText(_translate("MainWindow", "New"))
        self.export_reminders.setText(_translate("MainWindow", "Export"))
        # self.print_reminders.setText(_translate("MainWindow", "Print"))
        self.new_reminder_lb.setText(_translate("MainWindow", "Reminder"))
        self.label_140.setText(_translate("MainWindow", "Id"))
        self.reminder_add_party.setText(_translate("MainWindow", "Add"))
        self.reminder_open_party.setText(_translate("MainWindow", "Open"))
        self.reminder_delete_party.setText(_translate("MainWindow", "Delete"))
        self.label_141.setText(_translate("MainWindow", "Name"))
        self.reminder_name.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_142.setText(_translate("MainWindow", "Contract"))
        self.label_143.setText(_translate("MainWindow", "Company"))
        self.reminder_contract.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.reminder_company.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_144.setText(_translate("MainWindow", "Linked People"))
        self.label_145.setText(_translate("MainWindow", "Description"))
        self.label_146.setText(_translate("MainWindow", "Attachments"))
        self.reminder_add_attachment.setText(_translate("MainWindow", "Add"))
        self.reminder_open_attachment.setText(_translate("MainWindow", "Open"))
        self.reminder_delete_attachment.setText(_translate("MainWindow", "Delete"))
        self.reminder_complete.setText(_translate("MainWindow", "Complete"))
        self.reminder_snoozed.setText(_translate("MainWindow", "Snoozed"))
        self.recur_indefinitely_radio.setText(_translate("MainWindow", "Indefinitely"))
        self.before.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.before.setItemText(0, _translate("MainWindow", "Before"))
        self.before.setItemText(1, _translate("MainWindow", "After"))
        self.time_type.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.time_type.setItemText(0, _translate("MainWindow", "Day(s)"))
        self.time_type.setItemText(1, _translate("MainWindow", "Week(s)"))
        self.time_type.setItemText(2, _translate("MainWindow", "Month(s)"))
        self.time_type.setItemText(3, _translate("MainWindow", "Year(s)"))
        self.recur_until_specific.setText(_translate("MainWindow", "Until"))
        self.recur_until_specific_2.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.recur_until_btn.setText(_translate("MainWindow", "..."))
        self.label_147.setText(_translate("MainWindow", "Recurrence"))
        self.label_148.setText(_translate("MainWindow", "Reminder"))
        self.specific_date_radio.setText(_translate("MainWindow", "Specific Date"))
        self.do_not_recur_radio.setText(_translate("MainWindow", "Do Not Recur"))
        self.reminder_specific_date.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.specific_date_btn.setText(_translate("MainWindow", "..."))
        self.recur_type.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.recur_type.setItemText(0, _translate("MainWindow", "Daily"))
        self.recur_type.setItemText(1, _translate("MainWindow", "Weekly"))
        self.recur_type.setItemText(2, _translate("MainWindow", "Bi-weekly"))
        self.recur_type.setItemText(3, _translate("MainWindow", "Monthly"))
        self.recur_type.setItemText(4, _translate("MainWindow", "Quarterly"))
        self.recur_type.setItemText(5, _translate("MainWindow", "Bi_annually"))
        self.recur_type.setItemText(6, _translate("MainWindow", "Annually"))
        self.recur_type.setItemText(7, _translate("MainWindow", "Every 2 Years"))
        self.recur_type.setItemText(8, _translate("MainWindow", "Every 3 Years"))
        self.recur_type.setItemText(9, _translate("MainWindow", "Every 4 Years"))
        self.recur_type.setItemText(10, _translate("MainWindow", "Every 5 Years"))
        self.reminder_relative_date.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.recur_radio.setText(_translate("MainWindow", "Recur"))
        self.relative_date_radio.setText(_translate("MainWindow", "Relative Date"))
        self.until_key_date_radio.setText(_translate("MainWindow", "Until"))
        self.until_key_date.setItemText(0, _translate("MainWindow", "Contract Start Date"))
        self.until_key_date.setItemText(1, _translate("MainWindow", "Contract End Date"))
        self.until_key_date.setItemText(2, _translate("MainWindow", "Contract Cancel Date"))
        self.until_key_date.setItemText(3, _translate("MainWindow", "Contract Review Date"))
        self.key_date.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.key_date.setItemText(0, _translate("MainWindow", "Contract Start Date"))
        self.key_date.setItemText(1, _translate("MainWindow", "Contract End Date"))
        self.key_date.setItemText(2, _translate("MainWindow", "Contract Cancel Date"))
        self.key_date.setItemText(3, _translate("MainWindow", "Contract Review Date"))
        self.save_reminder.setText(_translate("MainWindow", "Save"))
        self.cancel_reminder.setText(_translate("MainWindow", "Cancel"))
        self.risk_lb.setText(_translate("MainWindow", "Risks"))
        self.risk_type_menu.setItemText(0, _translate("MainWindow", "All Risks"))
        self.risk_type_menu.setItemText(1, _translate("MainWindow", "Current Risks"))
        self.risk_type_menu.setItemText(2, _translate("MainWindow", "Overdue Risks"))
        self.risk_type_menu.setItemText(3, _translate("MainWindow", "Favorites"))
        self.risk_type_menu.setItemText(4, _translate("MainWindow", "Created Today"))
        self.risk_type_menu.setItemText(5, _translate("MainWindow", "Created This Week"))
        self.risk_type_menu.setItemText(6, _translate("MainWindow", "Created This Month"))
        self.risk_type_menu.setItemText(7, _translate("MainWindow", "Created This Year"))
        self.risk_type_menu.setItemText(8, _translate("MainWindow", "Created Last Month"))
        self.risk_type_menu.setItemText(9, _translate("MainWindow", "Created Last Year"))
        self.risk_type_menu.setItemText(10, _translate("MainWindow", "Archived"))
        self.edit_risk_btn.setText(_translate("MainWindow", "Edit"))
        self.delete_risk_btn.setText(_translate("MainWindow", "Delete"))
        self.archive_risk_btn.setText(_translate("MainWindow", "Archive"))
        self.favorite_risk_btn.setText(_translate("MainWindow", "Mark As Favorite"))
        self.risk_severity_search.setItemText(0, _translate("MainWindow", "Any"))
        self.risk_severity_search.setItemText(1, _translate("MainWindow", "Medium"))
        self.risk_severity_search.setItemText(2, _translate("MainWindow", "Low"))
        self.risk_severity_search.setItemText(3, _translate("MainWindow", "High"))
        # self.previous_risks.setText(_translate("MainWindow", "Previous"))
        # self.next_risks.setText(_translate("MainWindow", "Next"))
        self.new_risk.setText(_translate("MainWindow", "New"))
        self.export_risks.setText(_translate("MainWindow", "Export"))
        # self.print_risks.setText(_translate("MainWindow", "Print"))
        self.new_risk_lb.setText(_translate("MainWindow", "Risk"))
        self.save_risk.setText(_translate("MainWindow", "Save"))
        self.cancel_risk.setText(_translate("MainWindow", "Cancel"))
        self.label_151.setText(_translate("MainWindow", "Name"))
        self.label_152.setText(_translate("MainWindow", "Severity            "))
        self.risk_type.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.risk_type.setItemText(0, _translate("MainWindow", "Not Selected"))
        self.risk_type.setItemText(1, _translate("MainWindow", "3rd Party"))
        self.risk_type.setItemText(2, _translate("MainWindow", "Financial"))
        self.risk_type.setItemText(3, _translate("MainWindow", "Quality"))
        self.risk_type.setItemText(4, _translate("MainWindow", "Resource"))
        self.risk_type.setItemText(5, _translate("MainWindow", "Time"))
        self.label_175.setText(_translate("MainWindow", "End Date"))
        self.risk_end.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);\n"
                                                             "color: rgb(0,0,0)"))
        self.risk_end_btn.setText(_translate("MainWindow", "..."))
        self.label_153.setText(_translate("MainWindow", "Probability"))
        self.risk_probability.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.risk_probability.setItemText(0, _translate("MainWindow", "Low"))
        self.risk_probability.setItemText(1, _translate("MainWindow", "Medium"))
        self.risk_probability.setItemText(2, _translate("MainWindow", "High"))
        self.label_154.setText(_translate("MainWindow", "Impact"))
        self.risk_impact.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.risk_impact.setItemText(0, _translate("MainWindow", "Low"))
        self.risk_impact.setItemText(1, _translate("MainWindow", "Medium"))
        self.risk_impact.setItemText(2, _translate("MainWindow", "High"))
        self.label_155.setText(_translate("MainWindow", "Id"))
        self.label_156.setText(_translate("MainWindow", "Type"))
        self.risk_contract.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_157.setText(_translate("MainWindow", "Contract"))
        self.risk_name.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_159.setText(_translate("MainWindow", "Description"))
        self.label_160.setText(_translate("MainWindow", "Mitigation Measures"))
        self.label_162.setText(_translate("MainWindow", "Attachments"))
        self.risk_add_attachment_3.setText(_translate("MainWindow", "Add"))
        self.risk_open_attachment_3.setText(_translate("MainWindow", "Open"))
        self.risk_delete_attachment_3.setText(_translate("MainWindow", "Delete"))
        self.todos_lb.setText(_translate("MainWindow", "To-Dos"))
        self.new_todo.setText(_translate("MainWindow", "New"))
        self.export_todos.setText(_translate("MainWindow", "Export"))
        # self.print_todos.setText(_translate("MainWindow", "Print"))
        self.todos_type_menu.setItemText(0, _translate("MainWindow", "All Todos"))
        self.todos_type_menu.setItemText(1, _translate("MainWindow", "Incomplete Todos"))
        self.todos_type_menu.setItemText(2, _translate("MainWindow", "Passed Expected Resolution Date"))
        self.todos_type_menu.setItemText(3, _translate("MainWindow", "Favorites"))
        self.todos_type_menu.setItemText(4, _translate("MainWindow", "Created Today"))
        self.todos_type_menu.setItemText(5, _translate("MainWindow", "Created This Week"))
        self.todos_type_menu.setItemText(6, _translate("MainWindow", "Created This Month"))
        self.todos_type_menu.setItemText(7, _translate("MainWindow", "Created This Year"))
        self.todos_type_menu.setItemText(8, _translate("MainWindow", "Created Last Month"))
        self.todos_type_menu.setItemText(9, _translate("MainWindow", "Created Last Year"))
        self.todos_type_menu.setItemText(10, _translate("MainWindow", "Archived"))
        self.edit_todo_btn.setText(_translate("MainWindow", "Edit"))
        self.delete_todo_btn.setText(_translate("MainWindow", "Delete"))
        self.archive_todo_btn.setText(_translate("MainWindow", "Archive"))
        self.favorite_todo_btn.setText(_translate("MainWindow", "Mark As Favorite"))
        self.todo_status_search.setItemText(0, _translate("MainWindow", "Any"))
        self.todo_status_search.setItemText(1, _translate("MainWindow", "New"))
        self.todo_status_search.setItemText(2, _translate("MainWindow", "Open"))
        self.todo_status_search.setItemText(3, _translate("MainWindow", "Pending"))
        self.todo_status_search.setItemText(4, _translate("MainWindow", "Complete"))
        self.todo_priority_search.setItemText(0, _translate("MainWindow", "Any"))
        self.todo_priority_search.setItemText(1, _translate("MainWindow", "None"))
        self.todo_priority_search.setItemText(2, _translate("MainWindow", "Low"))
        self.todo_priority_search.setItemText(3, _translate("MainWindow", "Normal"))
        self.todo_priority_search.setItemText(4, _translate("MainWindow", "High"))
        self.todo_priority_search.setItemText(5, _translate("MainWindow", "Urgent"))
        self.todo_severity_search.setItemText(0, _translate("MainWindow", "Any"))
        self.todo_severity_search.setItemText(1, _translate("MainWindow", "None"))
        self.todo_severity_search.setItemText(2, _translate("MainWindow", "Low"))
        self.todo_severity_search.setItemText(3, _translate("MainWindow", "Medium"))
        self.todo_severity_search.setItemText(4, _translate("MainWindow", "High"))
        # self.previous_todos.setText(_translate("MainWindow", "Previous"))
        # self.next_todos.setText(_translate("MainWindow", "Next"))
        self.new_todo_lb.setText(_translate("MainWindow", "To-Do"))
        self.label_163.setText(_translate("MainWindow", "Id"))
        self.label_164.setText(_translate("MainWindow", "Company"))
        self.label_165.setText(_translate("MainWindow", "Start Date"))
        self.label_166.setText(_translate("MainWindow", "Assigned to"))
        self.label_167.setText(_translate("MainWindow", "Expected Resolution Date"))
        self.todo_status.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.todo_status.setItemText(0, _translate("MainWindow", "New"))
        self.todo_status.setItemText(1, _translate("MainWindow", "Open"))
        self.todo_status.setItemText(2, _translate("MainWindow", "Pending"))
        self.todo_status.setItemText(3, _translate("MainWindow", "Complete"))
        self.label_168.setText(_translate("MainWindow", "Subject"))
        self.todo_priority.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.todo_priority.setItemText(0, _translate("MainWindow", "None"))
        self.todo_priority.setItemText(1, _translate("MainWindow", "Low"))
        self.todo_priority.setItemText(2, _translate("MainWindow", "Normal"))
        self.todo_priority.setItemText(3, _translate("MainWindow", "High"))
        self.todo_priority.setItemText(4, _translate("MainWindow", "Urgent"))
        self.todo_company.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.label_169.setText(_translate("MainWindow", "Priority"))
        self.todo_severity.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.todo_severity.setItemText(0, _translate("MainWindow", "Low"))
        self.todo_severity.setItemText(1, _translate("MainWindow", "Medium"))
        self.todo_severity.setItemText(2, _translate("MainWindow", "High"))
        self.todo_resolutio_date.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.todo_resolution_btn.setText(_translate("MainWindow", "..."))
        self.label_170.setText(_translate("MainWindow", "Severity"))
        self.label_171.setText(_translate("MainWindow", "Contract"))
        self.todo_contract.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.todo_start_date.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.todo_start_btn.setText(_translate("MainWindow", "..."))
        self.todo_subject.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.todo_responsible.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.add_responsible.setText(_translate("MainWindow", "+"))
        self.label_172.setText(_translate("MainWindow", "Status"))
        self.label_174.setText(_translate("MainWindow", "Description"))
        self.todo_description.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 255);"))
        self.save_todo.setText(_translate("MainWindow", "Save"))
        self.cancel_todo.setText(_translate("MainWindow", "Cancel"))
        self.library_lb.setText(_translate("MainWindow", "Library"))
        self.open_document.setText(_translate("MainWindow", "Open"))
        self.delete_document.setText(_translate("MainWindow", "Delete"))
        # self.reports_lb.setText(_translate("MainWindow", "Reports"))
        self.archives_lb.setText(_translate("MainWindow", "Archives"))
        self.group1 = QtWidgets.QButtonGroup()
        self.group1.addButton(self.specific_date_radio)
        self.group1.addButton(self.relative_date_radio)
        self.group2 = QtWidgets.QButtonGroup()
        self.group2.addButton(self.do_not_recur_radio)
        self.group2.addButton(self.recur_radio)
        self.group3 = QtWidgets.QButtonGroup()
        self.group3.addButton(self.until_key_date_radio)
        self.group3.addButton(self.recur_until_specific)
        self.group3.addButton(self.recur_indefinitely_radio)

    # SQL commands
    def run_query(self, query, values=()):
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(query, values)
        sqliteConnection.commit()
        cursor.close()

    def fetch_query(self, query, values=()):
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(query, values)
        sqliteConnection.commit()
        results_tuple = cursor.fetchall()
        results = [item for t in results_tuple for item in t]
        cursor.close()
        return results

    # Next IDs
    def next_contract_id(self):
        next_id = int(self.fetch_query("SELECT seq FROM sqlite_sequence WHERE name='contracts'")[0]) + 1
        return next_id

    def next_reminder_id(self):
        next_id = int(self.fetch_query("SELECT seq FROM sqlite_sequence WHERE name='reminders'")[0]) + 1
        return next_id

    def next_risk_id(self):
        next_id = int(self.fetch_query("SELECT seq FROM sqlite_sequence WHERE name='risks'")[0]) + 1
        return next_id

    # Lists
    def contract_list(self):
        contracts_id = self.fetch_query('SELECT id FROM contracts')
        contracts_title = self.fetch_query('SELECT title FROM contracts')
        contracts = []
        for c_id, c_title in zip(contracts_id, contracts_title):
            c = str(c_id) + ' - ' + c_title
            contracts.append(c)
        return contracts

    def company_list(self):
        companies_id = self.fetch_query('SELECT id FROM companies')
        companies_title = self.fetch_query('SELECT name FROM companies')
        companies = []
        for c_id, c_title in zip(companies_id, companies_title):
            c = str(c_id) + ' - ' + c_title
            companies.append(c)
        return companies

    def person_list(self):
        people_id = self.fetch_query('SELECT id FROM people')
        first = self.fetch_query('SELECT first FROM people')
        last = self.fetch_query('SELECT last FROM people')
        people = []
        for p_id, p_first, p_last in zip(people_id, first, last):
            c = str(p_id) + ' - ' + p_first + ' ' + p_last
            people.append(c)
        return people

    # New windows
    def new_contract_window(self):
        self.contract_id_lb.clear()
        self.contract_title.clear()
        self.contract_type.setCurrentIndex(0)
        self.contract_category.setCurrentIndex(0)
        self.contract_classification.setCurrentIndex(0)
        self.contract_reference.clear()
        self.contract_account.clear()
        self.contract_status.setCurrentIndex(0)
        self.update_contract_masters()
        self.contract_master.setCurrentIndex(0)
        self.contract_value.clear()
        self.contract_currency.setCurrentIndex(0)
        self.term_none.setChecked(True)
        self.contract_start.clear()
        self.contract_end.clear()
        self.contract_review.clear()
        self.contract_cancel.clear()
        self.contract_extension.clear()
        self.contract_description.clear()
        self.update_contract_attachments()
        self.update_parties()

    def new_person_window(self):
        self.person_id_lb.clear()
        self.salutation.setCurrentIndex(0)
        self.first_name.clear()
        self.last_name.clear()
        self.gender.setCurrentIndex(0)
        self.job.clear()
        self.update_person_company()
        self.company.setCurrentIndex(0)
        self.person_type.clear()
        self.phone.clear()
        self.mobile.clear()
        self.email.clear()
        self.fax.clear()

    def new_company_window(self):
        self.company_id_lb.clear()
        self.company_name.clear()
        self.company_type.setCurrentIndex(0)
        self.address_1.clear()
        self.address_2.clear()
        self.city.clear()
        self.state.clear()
        self.zip.clear()
        self.country.clear()
        self.segment.setCurrentIndex(0)
        self.company_number.clear()
        self.website.clear()
        self.company_email.clear()
        self.contact.clear()
        self.company_fax.clear()

    def new_reminder_window(self):
        self.reminder_id_lb.clear()
        self.reminder_name.clear()
        self.update_reminder_contracts()
        self.reminder_contract.setCurrentIndex(0)
        self.update_reminder_company()
        self.reminder_company.setCurrentIndex(0)
        self.update_reminder_attachments()
        self.reminder_description.clear()
        self.update_reminder_people()
        self.reminder_complete.setChecked(False)
        self.reminder_snoozed.setChecked(False)
        self.specific_date_radio.setChecked(True)
        self.relative_date_radio.setChecked(False)
        self.do_not_recur_radio.setChecked(True)
        self.recur_radio.setChecked(False)
        self.recur_until_specific.setChecked(False)
        self.until_key_date_radio.setChecked(False)
        self.recur_indefinitely_radio.setChecked(False)
        self.reminder_specific_date.clear()
        self.reminder_relative_date.clear()
        self.time_type.setCurrentIndex(0)
        self.before.setCurrentIndex(0)
        self.key_date.setCurrentIndex(0)
        self.recur_type.setCurrentIndex(0)
        self.recur_until_specific_2.clear()
        self.until_key_date.setCurrentIndex(0)

    def new_risk_window(self):
        self.risk_id_lb.clear()
        self.risk_name.clear()
        self.update_risk_contracts()
        self.risk_contract.setCurrentIndex(0)
        self.risk_probability.setCurrentIndex(0)
        self.risk_impact.setCurrentIndex(0)
        self.risk_type.setCurrentIndex(0)
        self.risk_end.clear()
        self.risk_notes.clear()
        self.risk_mitigation.clear()
        self.update_risk_attachments()

    def new_todo_window(self):
        self.todo_id_lb.clear()
        self.todo_subject.clear()
        self.todo_status.setCurrentIndex(0)
        self.update_todo_people()
        self.todo_responsible.setCurrentIndex(0)
        self.todo_start_date.clear()
        self.todo_resolutio_date.clear()
        self.todo_priority.setCurrentIndex(0)
        self.todo_severity.setCurrentIndex(0)
        self.update_todo_contracts()
        self.todo_contract.setCurrentIndex(0)
        self.update_todo_company()
        self.todo_company.setCurrentIndex(0)
        self.todo_description.clear()

    # Edits
    def edit_contract_window(self, contract_id):
        self.contract_id_lb.setText(str(contract_id))
        self.contract_title.setText(str(self.fetch_query('SELECT title from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_type.setCurrentIndex(
            int(self.fetch_query('SELECT type_id from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_category.setCurrentIndex(
            int(self.fetch_query('SELECT category_id from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_classification.setCurrentIndex(int(self.fetch_query('SELECT classification_id from contracts '
                                                                          'WHERE id=?', (contract_id,))[0]))
        self.contract_reference.setText(
            str(self.fetch_query('SELECT reference from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_account.setText(
            str(self.fetch_query('SELECT account_reference from contracts WHERE id=?', (contract_id,))[0]))

        self.update_contract_masters()
        master_id = str(
            self.fetch_query('SELECT master_contract_id FROM contracts WHERE id=?', (contract_id,))[0]) + ' - '
        m_id = self.contract_master.findText(master_id, QtCore.Qt.MatchStartsWith)
        if m_id < 0:
            m_id = 0
        self.contract_master.setCurrentIndex(m_id)

        self.contract_status.setCurrentIndex(
            int(self.fetch_query('SELECT status_id from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_value.setText(str(self.fetch_query('SELECT value from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_currency.setCurrentIndex(
            int(self.fetch_query('SELECT currency_id from contracts WHERE id=?', (contract_id,))[0]))
        term = self.fetch_query('SELECT term_id from contracts WHERE id=?', (contract_id,))[0]
        if term == 0:
            self.term_none.setChecked(True)
        elif term == 1:
            self.term_fixed.setChecked(True)
        elif term == 2:
            self.term_recurring.setChecked(True)
        elif term == 3:
            self.term_rolling.setChecked(True)
        self.contract_start.setText(
            str(self.fetch_query('SELECT start_date from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_end.setText(str(self.fetch_query('SELECT end_date from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_review.setText(
            str(self.fetch_query('SELECT review_date from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_cancel.setText(
            str(self.fetch_query('SELECT cancel_date from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_extension.setText(
            str(self.fetch_query('SELECT extension_limit from contracts WHERE id=?', (contract_id,))[0]))
        self.contract_description.setText(
            str(self.fetch_query('SELECT description from contracts WHERE id=?', (contract_id,))[0]))
        self.update_contract_attachments(contract_id)
        self.update_parties(contract_id)

    def edit_person_window(self, person_id):
        self.person_id_lb.setText(str(person_id))
        self.salutation.setCurrentIndex(
            int(self.fetch_query('SELECT salutation_id FROM people WHERE id=?', (person_id,))[0]))
        self.first_name.setText(str(self.fetch_query('SELECT first FROM people WHERE id=?', (person_id,))[0]))
        self.last_name.setText(str(self.fetch_query('SELECT last FROM people WHERE id=?', (person_id,))[0]))
        self.gender.setCurrentIndex(int(self.fetch_query('SELECT gender_id FROM people WHERE id=?', (person_id,))[0]))
        self.job.setText(str(self.fetch_query('SELECT job FROM people WHERE id=?', (person_id,))[0]))

        self.update_person_company()
        company_id = str(self.fetch_query('SELECT company_id FROM people WHERE id=?', (person_id,))[0]) + ' - '
        c_id = self.company.findText(company_id, QtCore.Qt.MatchStartsWith)
        if c_id < 0:
            c_id = 0
        self.company.setCurrentIndex(c_id)

        self.person_type.setText(str(self.fetch_query('SELECT type FROM people WHERE id=?', (person_id,))[0]))
        self.phone.setText(str(self.fetch_query('SELECT phone FROM people WHERE id=?', (person_id,))[0]))
        self.mobile.setText(str(self.fetch_query('SELECT mobile FROM people WHERE id=?', (person_id,))[0]))
        self.email.setText(str(self.fetch_query('SELECT email FROM people WHERE id=?', (person_id,))[0]))
        self.fax.setText(str(self.fetch_query('SELECT fax FROM people WHERE id=?', (person_id,))[0]))

    def edit_company_window(self, company_id):
        self.company_id_lb.setText(str(company_id))
        self.company_name.setText(self.fetch_query('SELECT name FROM companies WHERE id=?', (company_id,))[0])
        self.company_type.setCurrentIndex(
            int(self.fetch_query('SELECT type_id FROM companies WHERE id=?', (company_id,))[0]))
        self.address_1.setText(self.fetch_query('SELECT address1 FROM companies WHERE id=?', (company_id,))[0])
        self.address_2.setText(self.fetch_query('SELECT address2 FROM companies WHERE id=?', (company_id,))[0])
        self.city.setText(self.fetch_query('SELECT city FROM companies WHERE id=?', (company_id,))[0])
        self.state.setText(self.fetch_query('SELECT state FROM companies WHERE id=?', (company_id,))[0])
        self.zip.setText(str(self.fetch_query('SELECT zip FROM companies WHERE id=?', (company_id,))[0]))
        self.country.setText(self.fetch_query('SELECT country FROM companies WHERE id=?', (company_id,))[0])
        self.segment.setCurrentIndex(
            int(self.fetch_query('SELECT segment_id FROM companies WHERE id=?', (company_id,))[0]))
        self.company_number.setText(str(self.fetch_query('SELECT number FROM companies WHERE id=?', (company_id,))[0]))
        self.website.setText(self.fetch_query('SELECT website FROM companies WHERE id=?', (company_id,))[0])
        self.company_email.setText(self.fetch_query('SELECT email FROM companies WHERE id=?', (company_id,))[0])
        self.contact.setText(str(self.fetch_query('SELECT phone FROM companies WHERE id=?', (company_id,))[0]))
        self.company_fax.setText(str(self.fetch_query('SELECT fax FROM companies WHERE id=?', (company_id,))[0]))

    def edit_reminder_window(self, reminder_id):
        self.reminder_id_lb.setText(str(reminder_id))
        self.reminder_name.setText(str(self.fetch_query('SELECT name FROM reminders WHERE id=?', (reminder_id,))[0]))

        self.update_reminder_contracts()
        contract_id = str(self.fetch_query('SELECT contract_id FROM reminders WHERE id=?', (reminder_id,))[0]) + ' - '
        c_id = self.reminder_contract.findText(contract_id, QtCore.Qt.MatchStartsWith)
        if c_id < 0:
            c_id = 0
        self.reminder_contract.setCurrentIndex(c_id)

        self.update_reminder_company()
        company_id = str(self.fetch_query('SELECT company_id FROM reminders WHERE id=?', (reminder_id,))[0]) + ' - '
        c_id = self.reminder_company.findText(company_id, QtCore.Qt.MatchStartsWith)
        if c_id < 0:
            c_id = 0
        self.reminder_company.setCurrentIndex(c_id)

        self.update_reminder_attachments()
        self.reminder_description.setText(
            str(self.fetch_query('SELECT description FROM reminders WHERE id=?', (reminder_id,))[0]))
        self.update_reminder_people()
        if int(self.fetch_query('SELECT complete FROM reminders WHERE id=?', (reminder_id,))[0]) == 1:
            self.reminder_complete.setChecked(True)
        if int(self.fetch_query('SELECT snoozed FROM reminders WHERE id=?', (reminder_id,))[0]) == 1:
            self.reminder_snoozed.setChecked(True)
        if int(self.fetch_query('SELECT specific_radio FROM reminders WHERE id=?', (reminder_id,))[0]) == 1:
            self.specific_date_radio.setChecked(True)
        if int(self.fetch_query('SELECT relative_radio FROM reminders WHERE id=?', (reminder_id,))[0]) == 1:
            self.relative_date_radio.setChecked(True)
        if int(self.fetch_query('SELECT do_not_recur_radio FROM reminders WHERE id=?', (reminder_id,))[0]) == 1:
            self.do_not_recur_radio.setChecked(True)
        if int(self.fetch_query('SELECT recur_radio FROM reminders WHERE id=?', (reminder_id,))[0]) == 1:
            self.recur_radio.setChecked(True)
        if int(self.fetch_query('SELECT until_specific_radio FROM reminders WHERE id=?', (reminder_id,))[0]) == 1:
            self.recur_until_specific.setChecked(True)
        if int(self.fetch_query('SELECT until_key_radio FROM reminders WHERE id=?', (reminder_id,))[0]) == 1:
            self.until_key_date_radio.setChecked(True)
        if int(self.fetch_query('SELECT indefinitely_radio FROM reminders WHERE id=?', (reminder_id,))[0]) == 1:
            self.recur_indefinitely_radio.setChecked(True)
        self.reminder_specific_date.setText(
            str(self.fetch_query('SELECT specific_date FROM reminders WHERE id=?', (reminder_id,))[0]))
        self.reminder_relative_date.setText(
            str(self.fetch_query('SELECT relative_date FROM reminders WHERE id=?', (reminder_id,))[0]))
        self.time_type.setCurrentIndex(
            int(self.fetch_query('SELECT time_id FROM reminders WHERE id=?', (reminder_id,))[0]))
        self.before.setCurrentIndex(
            int(self.fetch_query('SELECT before_after FROM reminders WHERE id=?', (reminder_id,))[0]))
        self.key_date.setCurrentIndex(
            int(self.fetch_query('SELECT date_id FROM reminders WHERE id=?', (reminder_id,))[0]))
        self.recur_type.setCurrentIndex(
            int(self.fetch_query('SELECT recur_id FROM reminders WHERE id=?', (reminder_id,))[0]))
        self.recur_until_specific_2.setText(
            str(self.fetch_query('SELECT until_date FROM reminders WHERE id=?', (reminder_id,))[0]))
        self.until_key_date.setCurrentIndex(
            int(self.fetch_query('SELECT until_key_id FROM reminders WHERE id=?', (reminder_id,))[0]))

    def edit_risk_window(self, risk_id):
        self.risk_id_lb.setText(str(risk_id))
        self.risk_name.setText(str(self.fetch_query('SELECT name FROM risks WHERE id=?', (risk_id,))[0]))

        self.update_risk_contracts()
        contract_id = str(self.fetch_query('SELECT contract_id FROM risks WHERE id=?', (risk_id,))[0]) + ' - '
        c_id = self.risk_contract.findText(contract_id, QtCore.Qt.MatchStartsWith)
        if c_id < 0:
            c_id = 0
        self.risk_contract.setCurrentIndex(c_id)

        self.risk_probability.setCurrentIndex(
            int(self.fetch_query('SELECT probability_id FROM risks WHERE id=?', (risk_id,))[0]))
        self.risk_impact.setCurrentIndex(int(self.fetch_query('SELECT impact_id FROM risks WHERE id=?', (risk_id,))[0]))
        self.risk_type.setCurrentIndex(int(self.fetch_query('SELECT type_id FROM risks WHERE id=?', (risk_id,))[0]))
        self.risk_end.setText(str(self.fetch_query('SELECT end_date FROM risks WHERE id=?', (risk_id,))[0]))
        self.risk_notes.setText(str(self.fetch_query('SELECT notes FROM risks WHERE id=?', (risk_id,))[0]))
        self.risk_mitigation.setText(str(self.fetch_query('SELECT mitigation FROM risks WHERE id=?', (risk_id,))[0]))
        self.update_risk_attachments(risk_id)

    def edit_todo_window(self, todo_id):
        self.todo_id_lb.setText(str(todo_id))
        self.todo_subject.setText(str(self.fetch_query('SELECT subject FROM todos WHERE id=?', (todo_id,))[0]))
        self.todo_status.setCurrentIndex(int(self.fetch_query('SELECT status_id FROM todos WHERE id=?', (todo_id,))[0]))

        self.update_todo_people()
        person_id = str(self.fetch_query('SELECT responsible_id FROM todos WHERE id=?', (todo_id,))[0]) + ' - '
        p_id = self.todo_responsible.findText(person_id, QtCore.Qt.MatchStartsWith)
        self.todo_responsible.setCurrentIndex(p_id)

        self.todo_start_date.setText(str(self.fetch_query('SELECT start_date FROM todos WHERE id=?', (todo_id,))[0]))
        self.todo_resolutio_date.setText(str(self.fetch_query('SELECT deadline FROM todos WHERE id=?', (todo_id,))[0]))
        self.todo_priority.setCurrentIndex(
            int(self.fetch_query('SELECT priority_id FROM todos WHERE id=?', (todo_id,))[0]))
        self.todo_severity.setCurrentIndex(
            int(self.fetch_query('SELECT severity_id FROM todos WHERE id=?', (todo_id,))[0]))

        self.update_todo_contracts()
        contract_id = str(
            self.fetch_query('SELECT contract_id FROM todos WHERE id=?', (todo_id,))[0]) + ' - '
        c_id = self.todo_contract.findText(contract_id, QtCore.Qt.MatchStartsWith)
        if c_id < 0:
            c_id = 0
        self.todo_contract.setCurrentIndex(c_id)

        self.update_todo_company()
        company_id = str(self.fetch_query('SELECT company_id FROM todos WHERE id=?', (todo_id,))[0]) + ' - '
        c_id = self.todo_company.findText(company_id, QtCore.Qt.MatchStartsWith)
        if c_id < 0:
            c_id = 0
        self.todo_company.setCurrentIndex(c_id)

        self.todo_description.setText(str(self.fetch_query('SELECT description FROM todos WHERE id=?', (todo_id,))[0]))

    # Updates
    def update_contracts(self):
        self.run_query("CREATE VIEW IF NOT EXISTS contracts_view AS SELECT contracts.id as ID, title as Title, "
                       "contract_types.name as Type, classifications.name as Classification, start_date as 'Start "
                       "Date', end_date as 'End Date', value as Value, currencies.symbol as '', CASE WHEN status_id = "
                       "0 THEN status_.name ELSE status.name END as Status FROM contracts JOIN currencies ON "
                       "contracts.currency_id=currencies.id JOIN classifications ON "
                       "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id "
                       "LEFT JOIN status status_ ON contracts.status_id_=status_.id JOIN contract_types ON "
                       "contracts.type_id=contract_types.id WHERE archived=0")
        self.run_query("CREATE VIEW IF NOT EXISTS my_contracts_view AS SELECT contracts.id as ID, title as Title, "
                       "contract_types.name as Type, classifications.name as Classification, start_date as 'Start "
                       "Date', end_date as 'End Date', value as Value, currencies.symbol as '', CASE WHEN status_id = "
                       "0 THEN status_.name ELSE status.name END as Status FROM contracts JOIN currencies ON "
                       "contracts.currency_id=currencies.id JOIN classifications ON "
                       "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id "
                       "LEFT JOIN status status_ ON contracts.status_id_=status.id JOIN contract_types ON "
                       "contracts.type_id=contract_types.id JOIN people_contracts on "
                       "people_contracts.contract_id=contracts.id WHERE person_id=1 AND archived=0")

        # Contracts Tree
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.contract_model = QtSql.QSqlRelationalTableModel()
        self.contract_model.setTable('contracts')
        query = QtSql.QSqlQuery()

        if self.contract_type_menu.currentIndex() == 0:
            s = "SELECT * FROM contracts_view"
        elif self.contract_type_menu.currentIndex() == 1:
            s = "SELECT * FROM contracts_view WHERE status = 'Active'"
        elif self.contract_type_menu.currentIndex() == 2:
            s = "SELECT * FROM contracts_view WHERE status != 'Active'"
        elif self.contract_type_menu.currentIndex() == 3:
            s = "SELECT * FROM my_contracts_view"
        elif self.contract_type_menu.currentIndex() == 4:
            s = "SELECT * FROM my_contracts_view WHERE status = 'Active'"
        elif self.contract_type_menu.currentIndex() == 5:
            s = "SELECT * FROM my_contracts_view WHERE status != 'Active'"
        elif self.contract_type_menu.currentIndex() == 6:
            s = "SELECT * FROM contracts_view WHERE status = 'Active' AND Classification = 'Customer'"
        elif self.contract_type_menu.currentIndex() == 7:
            s = "SELECT * FROM contracts_view WHERE status = 'Active' AND Classification = 'Supplier'"
        elif self.contract_type_menu.currentIndex() == 8:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE contracts.favorite=1 AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 9:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2)=DATE('now') " \
                "AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 10:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2) >= DATE(" \
                "'now', 'weekday 0','-7 days') AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 11:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2) >= DATE(" \
                "'now', 'start of month') AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 12:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2) >= DATE(" \
                "'now', 'start of year') AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 13:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of month', '-1 month') and DATE('now', 'start of month') AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 14:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of year', '-1 year') and DATE('now', 'start of year') AND archived=0 "
        else:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE archived=1 "

        query.exec_(s)
        self.contract_model.setQuery(query)
        db.close()
        self.contracts_tree.setModel(self.contract_model)
        self.contracts_query = s

    def update_status(self):
        self.run_query("UPDATE contracts SET status_id_ = 1 WHERE status_id = 0 AND (((term_id = 1 OR term_id = 2) "
                       "AND DATE('now') BETWEEN substr(start_date, 7, 4)||'-'||substr (start_date, 1,2)||'-'||substr("
                       "start_date, 4,2) and substr(end_date, 7, 4)||'-'||substr (end_date, 1,2)||'-'||substr("
                       "end_date, 4,2)) OR (term_id = 3 AND DATE('now') >= substr(start_date, 7, 4)||'-'||substr ("
                       "start_date, 1,2)||'-'||substr(start_date, 4,2)))")
        self.run_query("UPDATE contracts SET status_id_ = 2 WHERE status_id = 0 AND ( (term_id = 1 OR term_id = 2) "
                       "AND DATE('now') >= substr(end_date, 7, 4)||'-'||substr (end_date, 1,2)||'-'||substr(end_date,"
                       " 4,2))")
        self.run_query("UPDATE contracts SET status_id_ = 5 WHERE status_id = 0 AND ( (term_id = 1 OR term_id = 2) "
                       "AND DATE('now') < substr(start_date, 7, 4)||'-'||substr (start_date, 1,2)||'-'||substr("
                       "start_date, 4,2))")

    def update_people(self):
        # People Tree
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.person_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()

        if self.people_type_menu.currentIndex() == 0:
            s = "SELECT id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', phone as " \
                "'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE archived=0 "
        elif self.people_type_menu.currentIndex() == 1:
            s = "SELECT id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', phone as " \
                "'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE id=1 AND " \
                "archived=0 "
        elif self.people_type_menu.currentIndex() == 2:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people JOIN " \
                "people_contracts ON people.id=people_contracts.person_id AND archived=0 "
        elif self.people_type_menu.currentIndex() == 3:
            s = "SELECT id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', phone as " \
                "'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE favorite=1 " \
                "AND archived=0 "
        elif self.people_type_menu.currentIndex() == 4:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4," \
                "2)=DATE('now') AND archived=0 "
        elif self.people_type_menu.currentIndex() == 5:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE(" \
                "'now', 'weekday 0','-7 days') AND archived=0 "
        elif self.people_type_menu.currentIndex() == 6:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE(" \
                "'now', 'start of month') AND archived=0 "
        elif self.people_type_menu.currentIndex() == 7:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE(" \
                "'now', 'start of year') AND archived=0 "
        elif self.people_type_menu.currentIndex() == 8:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of month', '-1 month') and DATE('now', 'start of month') AND archived=0 "
        elif self.people_type_menu.currentIndex() == 9:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of year', '-1 year') and DATE('now', 'start of year') AND archived=0 "
        else:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "archived=1 "

        query.exec_(s)
        self.person_model.setQuery(query)
        db.close()
        self.people_tree.setModel(self.person_model)
        self.people_query = s

    def update_companies(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.company_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()

        if self.company_type_menu.currentIndex() == 0:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE archived=0 "
        elif self.company_type_menu.currentIndex() == 1:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE favorite=1 and archived=0 "
        elif self.company_type_menu.currentIndex() == 2:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2)=DATE('now') AND archived=0 "
        elif self.company_type_menu.currentIndex() == 3:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE('now', 'weekday 0'," \
                "'-7 days') AND archived=0 "
        elif self.company_type_menu.currentIndex() == 4:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE('now', 'start of month') " \
                "AND archived=0 "
        elif self.company_type_menu.currentIndex() == 5:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE('now', 'start of year') " \
                "AND archived=0 "
        elif self.company_type_menu.currentIndex() == 6:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) BETWEEN DATE('now', " \
                "'start of month', '-1 month') and DATE('now', 'start of month') AND archived=0 "
        elif self.company_type_menu.currentIndex() == 7:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) BETWEEN DATE('now', " \
                "'start of year', '-1 year') and DATE('now', 'start of year') AND archived=0 "
        else:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE archived=1 "

        query.exec_(s)
        self.company_model.setQuery(query)
        db.close()

        self.companies_tree.setModel(self.company_model)
        self.companies_query = s

    def update_reminders(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.reminder_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()

        self.update_reminders_dates()

        t = datetime.today() + timedelta(days=1)
        t2 = datetime.today() + timedelta(days=2)
        y = datetime.today() - timedelta(days=1)
        y2 = datetime.today() - timedelta(days=2)

        tmr = datetime.strftime(t, '%m/%d/%Y')
        tmr2 = datetime.strftime(t2, '%m/%d/%Y')
        ytd = datetime.strftime(y, '%m/%d/%Y')
        ytd2 = datetime.strftime(y2, '%m/%d/%Y')
        today = datetime.strftime(datetime.today(), '%m/%d/%Y')

        if self.reminder_type_menu.currentIndex() == 0:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN \'" + today + "\' THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 days' WHEN \'" + ytd + "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON r.snoozed=b.id WHERE r.archived=0 ORDER BY DATE(substr(r.deadline, 7, 4)||'-'||substr (r.deadline, 1,2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 1:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE substr(r.deadline, 7, 4)||'-'||substr (" \
                                                       "r.deadline, 1,2)||'-'||substr(r.deadline, 4,2)<=DATE('now') " \
                                                       "AND r.archived=0 AND r.complete=0 ORDER BY DATE(substr(" \
                                                       "r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 2:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE r.snoozed=1 AND r.archived=0 ORDER BY " \
                                                       "DATE(substr(r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 3:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE substr(r.deadline, 7, 4)||'-'||substr (" \
                                                       "r.deadline, 1,2)||'-'||substr(r.deadline, 4,2)>DATE('now') " \
                                                       "AND r.archived=0 AND r.complete=0 ORDER BY DATE(substr(" \
                                                       "r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 4:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE r.complete=1 AND r.archived=0 ORDER BY " \
                                                       "DATE(substr(r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 5:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE substr(r.deadline, 7, 4)||'-'||substr (" \
                                                       "r.deadline, 1,2)||'-'||substr(r.deadline, 4,2) BETWEEN DATE(" \
                                                       "'now', '+1 day') AND DATE('now', 'weekday 0') AND " \
                                                       "r.archived=0 AND r.complete=0 ORDER BY DATE(substr(" \
                                                       "r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 6:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE substr(r.deadline, 7, 4)||'-'||substr (" \
                                                       "r.deadline, 1,2)||'-'||substr(r.deadline, 4,2) BETWEEN DATE(" \
                                                       "'now', '+1 day') AND DATE('now', 'start of month', " \
                                                       "'+1 month') AND r.archived=0 AND r.complete=0 ORDER BY DATE(" \
                                                       "substr(r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        else:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE r.archived=1 ORDER BY DATE(substr(" \
                                                       "r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "

        query.exec_(s)
        self.reminder_model.setQuery(query)
        db.close()

        self.reminders_tree.setModel(self.reminder_model)
        self.reminders_query = s

    def update_reminders_dates(self):
        ids = self.fetch_query("SELECT id FROM reminders WHERE recur_radio=1 AND substr(deadline, 7, 4)||'-'||substr "
                               "(deadline, 1,2)||'-'||substr(deadline, 4,2)<DATE('now')")
        if ids == []:
            count = self.fetch_query("SELECT count(id) FROM reminders WHERE substr(deadline, 7, 4) || '-' || substr("
                                     "deadline, 1, 2) || '-' || substr(deadline, 4, 2)<=DATE('now') AND complete=0 "
                                     "AND snoozed=0")[0]
            if count > 0:
                self.reminders_btn.setText('Reminders (' + str(count) + ')')
                self.reminders_btn.setStyleSheet("background-color: rgb(240, 10, 70);")
            else:
                self.reminders_btn.setText('Reminders')
                self.reminders_btn.setStyleSheet("background-color: rgb(255, 255, 255);")

        for reminder_id in ids:
            recur_id = self.fetch_query("SELECT recur_id FROM reminders WHERE id=?", (reminder_id,))[0]
            prev_deadline = self.fetch_query("SELECT deadline FROM reminders WHERE id=?", (reminder_id,))[0]
            prev_deadline_object = datetime.strptime(prev_deadline, '%m/%d/%Y')
            last_recurrence = self.fetch_query("SELECT last_recurrence FROM reminders WHERE id=?", (reminder_id,))[0]
            next_recurrence = 'temp'
            if last_recurrence != '':
                i = 1
                if recur_id == 0:
                    while next_recurrence != '':
                        if prev_deadline_object + timedelta(days=1 * i) < datetime.strptime(last_recurrence,
                                                                                            '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + timedelta(days=1 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                            i += 1
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 1:
                    while next_recurrence != '':
                        if prev_deadline_object + timedelta(weeks=1 * i) < datetime.strptime(last_recurrence,
                                                                                             '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + timedelta(weeks=1 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                            i += 1
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 2:
                    while next_recurrence != '':
                        if prev_deadline_object + timedelta(weeks=2 * i) < datetime.strptime(last_recurrence,
                                                                                             '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + timedelta(weeks=2 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                            i += 1
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 3:
                    while next_recurrence != '':
                        if prev_deadline_object + relativedelta(months=1 * i) < datetime.strptime(last_recurrence,
                                                                                                  '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + relativedelta(months=1 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                            i += 1
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 4:
                    while next_recurrence != '':
                        if prev_deadline_object + relativedelta(months=3 * i) < datetime.strptime(last_recurrence,
                                                                                                  '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + relativedelta(months=3 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                            i += 1
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 5:
                    while next_recurrence != '':
                        if prev_deadline_object + relativedelta(months=6 * i) < datetime.strptime(last_recurrence,
                                                                                                  '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + relativedelta(months=6 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                            i += 1
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 6:
                    while next_recurrence != '':
                        if prev_deadline_object + relativedelta(years=1 * i) < datetime.strptime(last_recurrence,
                                                                                                 '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + relativedelta(years=1 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                            i += 1
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 7:
                    while next_recurrence != '':
                        if prev_deadline_object + relativedelta(years=2 * i) < datetime.strptime(last_recurrence,
                                                                                                 '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + relativedelta(years=2 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                            i += 1
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 8:
                    while next_recurrence != '':
                        if prev_deadline_object + relativedelta(years=3 * i) < datetime.strptime(last_recurrence,
                                                                                                 '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + relativedelta(years=3 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 9:
                    while next_recurrence != '':
                        if prev_deadline_object + relativedelta(years=4 * i) < datetime.strptime(last_recurrence,
                                                                                                 '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + relativedelta(years=4 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                            i += 1
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 10:
                    while next_recurrence != '':
                        if prev_deadline_object + relativedelta(years=5 * i) < datetime.strptime(last_recurrence,
                                                                                                 '%m/%d/%Y'):
                            next_recurrence_object = prev_deadline_object + relativedelta(years=5 * i)
                            next_recurrence = datetime.strftime(next_recurrence_object,
                                                                '%m/%d/%Y')
                            i += 1
                        else:
                            next_recurrence = ''
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
            else:
                i = 1
                if recur_id == 0:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + timedelta(days=1 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 1:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + timedelta(weeks=1 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 2:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + timedelta(weeks=2 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 3:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + relativedelta(months=1 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 4:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + relativedelta(months=3 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 5:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + relativedelta(months=6 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 6:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + relativedelta(years=1 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 7:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + relativedelta(years=2 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 8:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + relativedelta(years=3 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 9:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + relativedelta(years=4 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break
                elif recur_id == 10:
                    while next_recurrence != '':
                        next_recurrence_object = prev_deadline_object + relativedelta(years=5 * i)
                        next_recurrence = datetime.strftime(next_recurrence_object,
                                                            '%m/%d/%Y')
                        i += 1
                        if next_recurrence == '' or next_recurrence_object >= datetime.today():
                            break

            if next_recurrence == '':
                self.run_query("UPDATE reminders SET recur_radio=0, last_recurrence='' WHERE id=?", (reminder_id,))
            else:
                self.run_query("UPDATE reminders SET deadline=? WHERE id=?",
                               (next_recurrence, reminder_id))

        count = self.fetch_query(
            "SELECT count(id) FROM reminders WHERE substr(deadline, 7, 4) || '-' || substr(deadline, 1, 2) || '-' || "
            "substr(deadline, 4, 2)<=DATE('now') AND complete=0 AND snoozed=0")[
            0]
        if count > 0:
            self.reminders_btn.setText('Reminders (' + str(count) + ')')
            self.reminders_btn.setStyleSheet("background-color: rgb(240, 10, 70);")
        else:
            self.reminders_btn.setText('Reminders')
            self.reminders_btn.setStyleSheet("background-color: rgb(255, 255, 255);")

    def update_risks(self):
        ids = self.fetch_query("SELECT id FROM risks WHERE  substr(end_date, 7, 4)||'-'||substr (end_date, 1,"
                               "2)||'-'||substr(end_date, 4,2)<DATE('now') AND expired=0")
        if ids != []:
            for risk_id in ids:
                self.run_query("UPDATE risks SET expired=1 WHERE id=?", (risk_id,))
        ids = self.fetch_query(
            "SELECT id FROM risks WHERE  (substr(end_date, 7, 4)||'-'||substr (end_date, 1,2)||'-'||substr(end_date, "
            "4,2)>=DATE('now') AND expired=1) OR end_date=''")
        if ids != []:
            for risk_id in ids:
                self.run_query("UPDATE risks SET expired=0 WHERE id=?", (risk_id,))

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.risk_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        if self.risk_type_menu.currentIndex() == 0:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 1:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE r.expired=0 AND r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 2:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE r.expired=1 AND r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 3:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE r.favorite=1 AND r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 4:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2)=DATE('now') AND r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 5:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2) >= DATE('now', 'weekday 0', '-7 days') AND " \
                "r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 6:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2) >= DATE('now', 'start of month') AND " \
                "r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 7:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2) >= DATE('now', 'start of year') AND " \
                "r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 8:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2) BETWEEN DATE('now', 'start of month', " \
                "'-1 month') AND DATE('now', 'start of month') AND r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 9:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2) BETWEEN DATE('now', 'start of year', " \
                "'-1 year') AND DATE('now', 'start of year') AND r.archived=0 "
        else:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE r.archived=1 "

        query.exec_(s)
        self.risk_model.setQuery(query)
        db.close()

        self.risks_tree.setModel(self.risk_model)
        self.risks_query = s
        # All other tree views do not need this. I don't know why, but it works so I'll leave it here
        self.risks_tree.setColumnWidth(0, 155 * .75)
        self.risks_tree.setColumnWidth(1, 155 * .75)
        self.risks_tree.setColumnWidth(2, 150 * .75)
        self.risks_tree.setColumnWidth(3, 100 * .75)
        self.risks_tree.setColumnWidth(4, 150 * .75)
        self.risks_tree.setColumnWidth(5, 150 * .75)
        self.risks_tree.setColumnWidth(6, 155 * .75)
        self.risks_tree.setColumnWidth(7, 155 * .75)

    def update_todos(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.todo_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        if self.todos_type_menu.currentIndex() == 0:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 1:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE NOT t.status_id=3 " \
                "AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 2:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(t.deadline, " \
                "7, 4) || '-' || substr(t.deadline, 1, 2) || '-' || substr(t.deadline, 4,2)<=DATE('now') AND NOT " \
                "t.deadline='' AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 3:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE t.favorite=1 AND " \
                "t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 4:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4," \
                "2)=DATE('now') AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 5:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4,2) >= DATE(" \
                "'now', 'weekday 0', '-7 days') AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 6:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4,2) >= DATE(" \
                "'now', 'start of month') AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 7:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4,2) >= DATE(" \
                "'now', 'start of year') AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 8:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of month', '-1 month') AND DATE('now', 'start of month') AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 9:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of year', '-1 year') AND DATE('now', 'start of year') AND t.archived=0 "
        else:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE t.archived=1 "

        query.exec_(s)
        self.todo_model.setQuery(query)
        db.close()

        self.todos_tree.setModel(self.todo_model)
        self.todos_query = s

    def update_library(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.library_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()

        s = "SELECT id as ID, name as Name, url as Url, date_created as 'Date Created' FROM documents WHERE del=0"
        if self.document_type_search.currentIndex() != 0:
            s += " AND type_id = " + str(self.document_type_search.currentIndex())

        query.exec_(s)
        self.library_model.setQuery(query)
        db.close()

        self.library_tree.setModel(self.library_model)
        self.library_tree.setColumnWidth(0, 100 * .75)
        self.library_tree.setColumnWidth(1, 390 * .75)
        self.library_tree.setColumnWidth(2, 350 * .75)
        self.library_tree.setColumnWidth(3, 190 * .75)

    def update_contract_masters(self):
        self.contract_master.clear()
        self.contract_master.addItem('0 - No Master Contract')
        for contract in self.contract_list():
            self.contract_master.addItem(contract)

    def update_reminder_contracts(self):
        self.reminder_contract.clear()
        self.reminder_contract.addItem('0 - No Contract')
        for contract in self.contract_list():
            self.reminder_contract.addItem(contract)

    def update_person_company(self):
        self.company.clear()
        self.company.addItem('0 - No Company')
        for company in self.company_list():
            self.company.addItem(company)

    def update_reminder_company(self):
        self.reminder_company.clear()
        self.reminder_company.addItem('0 - No Company')
        for company in self.company_list():
            self.reminder_company.addItem(company)

    def update_risk_contracts(self):
        self.risk_contract.clear()
        self.risk_contract.addItem('0 - No Contract')
        for contract in self.contract_list():
            self.risk_contract.addItem(contract)

    def update_todo_people(self):
        self.todo_responsible.clear()
        for person in self.person_list():
            self.todo_responsible.addItem(person)

    def update_todo_contracts(self):
        self.todo_contract.clear()
        self.todo_contract.addItem('0 - No Contract')
        for contract in self.contract_list():
            self.todo_contract.addItem(contract)

    def update_todo_company(self):
        self.todo_company.clear()
        self.todo_company.addItem('0 - No Company')
        for company in self.company_list():
            self.todo_company.addItem(company)

    # Attachments
    def update_contract_attachments(self, contract_id=None):
        if contract_id is None:
            contract_id = self.next_contract_id()

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.contract_attachment_model = QtSql.QSqlRelationalTableModel()
        self.contract_attachment_model.setTable('documents')
        query = QtSql.QSqlQuery()
        query.exec_(
            "SELECT id as ID, name as Name, url as Url, date_created as 'Date Created' FROM documents WHERE type_id=1 "
            "AND del=0 AND owner_id=" + str(contract_id))
        self.contract_attachment_model.setQuery(query)
        db.close()

        self.contract_attachments.setModel(self.contract_attachment_model)

    def update_reminder_attachments(self, reminder_id=None):
        if reminder_id is None:
            reminder_id = self.next_reminder_id()

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.reminder_attachment_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_(
            "SELECT id as ID, name as Name, url as Url, date_created as 'Date Created' FROM documents WHERE type_id=2 "
            "AND del=0 AND owner_id=" + str(reminder_id))
        self.reminder_attachment_model.setQuery(query)
        db.close()

        self.reminder_attachments.setModel(self.reminder_attachment_model)

    def update_risk_attachments(self, risk_id=None):
        if risk_id is None:
            risk_id = self.next_risk_id()

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.risk_attachment_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_(
            "SELECT id as ID, name as Name, url as Url, date_created as 'Date Created' FROM documents WHERE type_id=3 "
            "AND del=0 AND owner_id=" + str(risk_id))
        self.risk_attachment_model.setQuery(query)
        db.close()

        self.risk_attachments.setModel(self.risk_attachment_model)

    # Parties
    def update_parties(self, contract_id=None):
        if contract_id is None:
            contract_id = self.next_contract_id()

        # Contract Parties
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.contract_party_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_(
            "SELECT people.id as ID, people.first as 'First Name', people.last as 'Last Name', people.email as 'Email "
            "Address' FROM people_contracts JOIN people ON people_contracts.person_id=people.id WHERE "
            "people_contracts.del=0 AND people_contracts.contract_id=" + str(contract_id))
        self.contract_party_model.setQuery(query)
        db.close()
        self.contract_parties.setModel(self.contract_party_model)

    def update_reminder_people(self, reminder_id=None):
        if reminder_id is None:
            reminder_id = self.next_reminder_id()

        # reminder people
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.reminder_person_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_(
            "SELECT people.id as ID, people.first as 'First Name', people.last as 'Last Name', people.email as 'Email "
            "Address' FROM people_reminders JOIN people ON people_reminders.person_id=people.id WHERE "
            "people_reminders.del=0 AND people_reminders.reminder_id=" + str(
                reminder_id))
        self.reminder_person_model.setQuery(query)
        db.close()
        self.reminder_people.setModel(self.reminder_person_model)

    # Searches
    def search_contract(self):
        id = self.contract_id_search.text()
        title = self.contract_title_search.text()
        type = self.contract_type_search.text()
        classification = self.contract_classificatiion_type.text()
        start = self.contract_start_type.text()
        end = self.contract_end_search.text()
        value = self.contract_value_search.text()
        status = self.contract_status_menu.currentText()

        self.run_query(
            "CREATE VIEW IF NOT EXISTS contracts_view AS SELECT contracts.id as ID, title as Title, "
            "contract_types.name as Type, classifications.name as Classification, start_date as 'Start Date', "
            "end_date as 'End Date', value as Value, currencies.symbol as '', CASE WHEN status_id = 0 THEN "
            "status_.name ELSE status.name END as Status FROM contracts JOIN currencies ON "
            "contracts.currency_id=currencies.id JOIN classifications ON "
            "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id LEFT JOIN "
            "status status_ ON contracts.status_id_=status_.id JOIN contract_types ON "
            "contracts.type_id=contract_types.id WHERE archived=0")
        self.run_query(
            "CREATE VIEW IF NOT EXISTS my_contracts_view AS SELECT contracts.id as ID, title as Title, "
            "contract_types.name as Type, classifications.name as Classification, start_date as 'Start Date', "
            "end_date as 'End Date', value as Value, currencies.symbol as '', CASE WHEN status_id = 0 THEN "
            "status_.name ELSE status.name END as Status FROM contracts JOIN currencies ON "
            "contracts.currency_id=currencies.id JOIN classifications ON "
            "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id LEFT JOIN "
            "status status_ ON contracts.status_id_=status.id JOIN contract_types ON "
            "contracts.type_id=contract_types.id JOIN people_contracts on people_contracts.contract_id=contracts.id "
            "WHERE person_id=1 AND archived=0")

        # Contracts Tree
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.contract_model = QtSql.QSqlRelationalTableModel()
        self.contract_model.setTable('contracts')
        query = QtSql.QSqlQuery()

        if self.contract_type_menu.currentIndex() == 0:
            s = "SELECT * FROM contracts_view"
        elif self.contract_type_menu.currentIndex() == 1:
            s = "SELECT * FROM contracts_view WHERE status = 'Active'"
        elif self.contract_type_menu.currentIndex() == 2:
            s = "SELECT * FROM contracts_view WHERE status != 'Active'"
        elif self.contract_type_menu.currentIndex() == 3:
            s = "SELECT * FROM my_contracts_view"
        elif self.contract_type_menu.currentIndex() == 4:
            s = "SELECT * FROM my_contracts_view WHERE status = 'Active'"
        elif self.contract_type_menu.currentIndex() == 5:
            s = "SELECT * FROM my_contracts_view WHERE status != 'Active'"
        elif self.contract_type_menu.currentIndex() == 6:
            s = "SELECT * FROM contracts_view WHERE status = 'Active' AND Classification = 'Customer'"
        elif self.contract_type_menu.currentIndex() == 7:
            s = "SELECT * FROM contracts_view WHERE status = 'Active' AND Classification = 'Supplier'"
        elif self.contract_type_menu.currentIndex() == 8:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE contracts.favorite=1 AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 9:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2)=DATE('now') " \
                "AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 10:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2) >= DATE(" \
                "'now', 'weekday 0','-7 days') AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 11:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2) >= DATE(" \
                "'now', 'start of month') AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 12:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2) >= DATE(" \
                "'now', 'start of year') AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 13:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of month', '-1 month') and DATE('now', 'start of month') AND archived=0 "
        elif self.contract_type_menu.currentIndex() == 14:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE substr(contracts.date_created, 7, " \
                "4)||'-'||substr (contracts.date_created, 1,2)||'-'||substr(contracts.date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of year', '-1 year') and DATE('now', 'start of year') AND archived=0 "
        else:
            s = "SELECT contracts.id as ID, title as Title, contract_types.name as Type, classifications.name as " \
                "Classification, start_date as 'Start Date', end_date as 'End Date', value as Value, " \
                "currencies.symbol as '', status.name as Status FROM contracts JOIN currencies ON " \
                "contracts.currency_id=currencies.id JOIN classifications ON " \
                "contracts.classification_id=classifications.id JOIN status ON contracts.status_id=status.id JOIN " \
                "contract_types ON contracts.type_id=contract_types.id WHERE archived=1 "

        if id:
            s = "SELECT * FROM (" + s + ") WHERE CAST(ID AS text) LIKE '" + id + "%'"
        if title:
            s = "SELECT * FROM (" + s + ") WHERE CAST(Title AS text) LIKE '" + title + "%'"
        if type:
            s = "SELECT * FROM (" + s + ") WHERE CAST(Type AS text) LIKE '" + type + "%'"
        if classification:
            s = "SELECT * FROM (" + s + ") WHERE CAST(Classification AS text) LIKE '" + classification + "%'"
        if start:
            s = "SELECT * FROM (" + s + ") WHERE \"Start Date\" LIKE '" + start + "%'"
        if end:
            s = "SELECT * FROM (" + s + ") WHERE \"End Date\" LIKE '" + end + "%'"
        if value:
            s = "SELECT * FROM (" + s + ") WHERE CAST(Value AS text) LIKE '" + value + "%'"
        if status != 'Any':
            s = "SELECT * FROM (" + s + ") WHERE Status = '" + status + "'"
        query.exec_(s)
        self.contract_model.setQuery(query)
        db.close()
        self.contracts_tree.setModel(self.contract_model)
        self.contracts_query = s

    def search_person(self):
        id = self.person_id_search.text()
        first = self.person_first_search.text()
        last = self.person_last_search.text()
        email = self.person_email_search.text()
        phone = self.person_phone_search.text()
        mobile = self.person_mobile_search.text()
        job = self.person_job_search.text()
        type = self.person_type_search.text()

        # People Tree
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.person_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()

        if self.people_type_menu.currentIndex() == 0:
            s = "SELECT id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', phone as " \
                "'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE archived=0 "
        elif self.people_type_menu.currentIndex() == 1:
            s = "SELECT id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', phone as " \
                "'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE id=1 AND " \
                "archived=0 "
        elif self.people_type_menu.currentIndex() == 2:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people JOIN " \
                "people_contracts ON people.id=people_contracts.person_id AND archived=0 "
        elif self.people_type_menu.currentIndex() == 3:
            s = "SELECT id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', phone as " \
                "'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE favorite=1 " \
                "AND archived=0 "
        elif self.people_type_menu.currentIndex() == 4:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4," \
                "2)=DATE('now') AND archived=0 "
        elif self.people_type_menu.currentIndex() == 5:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE(" \
                "'now', 'weekday 0','-7 days') AND archived=0 "
        elif self.people_type_menu.currentIndex() == 6:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE(" \
                "'now', 'start of month') AND archived=0 "
        elif self.people_type_menu.currentIndex() == 7:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE(" \
                "'now', 'start of year') AND archived=0 "
        elif self.people_type_menu.currentIndex() == 8:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of month', '-1 month') and DATE('now', 'start of month') AND archived=0 "
        elif self.people_type_menu.currentIndex() == 9:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "substr(date_created, 7, 4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of year', '-1 year') and DATE('now', 'start of year') AND archived=0 "
        else:
            s = "SELECT people.id as ID, first as 'First Name', last as 'Last Name', email as 'Email Address', " \
                "phone as 'Phone Number', mobile as 'Mobile Number', job as 'Job', type as Type FROM people WHERE " \
                "archived=1 "

        if id:
            s = "SELECT * FROM (" + s + ") WHERE CAST(ID as text) LIKE '" + id + "%'"
        if first:
            s = "SELECT * FROM (" + s + ") WHERE \"First Name\" LIKE '" + first + "%'"
        if last:
            s = "SELECT * FROM (" + s + ") WHERE \"Last Name\" LIKE '" + last + "%'"
        if email:
            s = "SELECT * FROM (" + s + ") WHERE \"Email Address\" LIKE '" + email + "%'"
        if phone:
            s = "SELECT * FROM (" + s + ") WHERE CAST(\"Phone Number\" as text) LIKE '" + phone + "%'"
        if mobile:
            s = "SELECT * FROM (" + s + ") WHERE CAST(\"Mobile Number\" as text) LIKE '" + mobile + "%'"
        if job:
            s = "SELECT * FROM (" + s + ") WHERE Job LIKE '" + job + "%'"
        if type:
            s = "SELECT * FROM (" + s + ") WHERE Type LIKE '" + type + "%'"
        query.exec_(s)
        self.person_model.setQuery(query)
        db.close()
        self.people_tree.setModel(self.person_model)
        self.people_query = s

    def search_company(self):
        id = self.company_id_search.text()
        name = self.company_name_search.text()
        address = self.company_address_search.text()
        city = self.company_city_search.text()
        state = self.company_state_search.text()
        zip = self.company_zip_search.text()
        country = self.company_country_search.text()
        website = self.company_website_search.text()

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.company_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()

        if self.company_type_menu.currentIndex() == 0:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE archived=0 "
        elif self.company_type_menu.currentIndex() == 1:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE favorite=1 and archived=0 "
        elif self.company_type_menu.currentIndex() == 2:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2)=DATE('now') AND archived=0 "
        elif self.company_type_menu.currentIndex() == 3:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE('now', 'weekday 0'," \
                "'-7 days') AND archived=0 "
        elif self.company_type_menu.currentIndex() == 4:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE('now', 'start of month') " \
                "AND archived=0 "
        elif self.company_type_menu.currentIndex() == 5:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) >= DATE('now', 'start of year') " \
                "AND archived=0 "
        elif self.company_type_menu.currentIndex() == 6:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) BETWEEN DATE('now', " \
                "'start of month', '-1 month') and DATE('now', 'start of month') AND archived=0 "
        elif self.company_type_menu.currentIndex() == 7:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE substr(date_created, 7, " \
                "4)||'-'||substr (date_created, 1,2)||'-'||substr(date_created, 4,2) BETWEEN DATE('now', " \
                "'start of year', '-1 year') and DATE('now', 'start of year') AND archived=0 "
        else:
            s = "SELECT id as Id, name as Name, address1 as Address, city as City, state as State, zip as 'Zip Code', " \
                "country as 'Country', website as Website FROM companies WHERE archived=1 "

        if id:
            s = "SELECT * FROM (" + s + ") WHERE CAST(ID as text) LIKE '" + id + "%'"
        if name:
            s = "SELECT * FROM (" + s + ") WHERE Name LIKE '" + name + "%'"
        if address:
            s = "SELECT * FROM (" + s + ") WHERE Address LIKE '" + address + "%'"
        if city:
            s = "SELECT * FROM (" + s + ") WHERE City LIKE '" + city + "%'"
        if state:
            s = "SELECT * FROM (" + s + ") WHERE State LIKE '" + state + "%'"
        if zip:
            s = "SELECT * FROM (" + s + ") WHERE \"Zip Code\" LIKE '" + zip + "%'"
        if country:
            s = "SELECT * FROM (" + s + ") WHERE Country LIKE '" + country + "%'"
        if website:
            s = "SELECT * FROM (" + s + ") WHERE Website LIKE '" + website + "%'"

        query.exec_(s)
        self.company_model.setQuery(query)
        db.close()

        self.companies_tree.setModel(self.company_model)
        self.companies_query = s

    def search_reminder(self):
        id = self.reminder_id_search.text()
        name = self.reminder_name_search.text()
        description = self.reminder_description_search.text()
        date = self.reminder_date_search.text()
        complete = self.reminder_complete_search.text()
        snoozed = self.reminder_snoozed_search.text()

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.reminder_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()

        self.update_reminders_dates()

        t = datetime.today() + timedelta(days=1)
        t2 = datetime.today() + timedelta(days=2)
        y = datetime.today() - timedelta(days=1)
        y2 = datetime.today() - timedelta(days=2)

        tmr = datetime.strftime(t, '%m/%d/%Y')
        tmr2 = datetime.strftime(t2, '%m/%d/%Y')
        ytd = datetime.strftime(y, '%m/%d/%Y')
        ytd2 = datetime.strftime(y2, '%m/%d/%Y')
        today = datetime.strftime(datetime.today(), '%m/%d/%Y')

        if self.reminder_type_menu.currentIndex() == 0:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN \'" + today + "\' THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 days' WHEN \'" + ytd + "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON r.snoozed=b.id WHERE r.archived=0 ORDER BY DATE(substr(r.deadline, 7, 4)||'-'||substr (r.deadline, 1,2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 1:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE substr(r.deadline, 7, 4)||'-'||substr (" \
                                                       "r.deadline, 1,2)||'-'||substr(r.deadline, 4,2)<=DATE('now') " \
                                                       "AND r.archived=0 AND r.complete=0 ORDER BY DATE(substr(" \
                                                       "r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 2:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE r.snoozed=1 AND r.archived=0 ORDER BY " \
                                                       "DATE(substr(r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 3:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE substr(r.deadline, 7, 4)||'-'||substr (" \
                                                       "r.deadline, 1,2)||'-'||substr(r.deadline, 4,2)>DATE('now') " \
                                                       "AND r.archived=0 AND r.complete=0 ORDER BY DATE(substr(" \
                                                       "r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 4:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE r.complete=1 AND r.archived=0 ORDER BY " \
                                                       "DATE(substr(r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 5:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE substr(r.deadline, 7, 4)||'-'||substr (" \
                                                       "r.deadline, 1,2)||'-'||substr(r.deadline, 4,2) BETWEEN DATE(" \
                                                       "'now', '+1 day') AND DATE('now', 'weekday 0') AND " \
                                                       "r.archived=0 AND r.complete=0 ORDER BY DATE(substr(" \
                                                       "r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        elif self.reminder_type_menu.currentIndex() == 6:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE substr(r.deadline, 7, 4)||'-'||substr (" \
                                                       "r.deadline, 1,2)||'-'||substr(r.deadline, 4,2) BETWEEN DATE(" \
                                                       "'now', '+1 day') AND DATE('now', 'start of month', " \
                                                       "'+1 month') AND r.archived=0 AND r.complete=0 ORDER BY DATE(" \
                                                       "substr(r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "
        else:
            s = "SELECT r.id as Id, r.name as Name, r.description as Description, CASE r.deadline WHEN strftime(" \
                "'%m/%d/%Y','now') THEN 'Today' WHEN \'" + tmr + "\' THEN 'Tomorrow' WHEN \'" + tmr2 + "\' THEN 'In 2 " \
                                                                                                       "days' WHEN " \
                                                                                                       "\'" + ytd + \
                "\' THEN 'Yesterday' WHEN \'" + ytd2 + "\' THEN '2 days ago' ELSE r.deadline END 'Reminder Date', " \
                                                       "a.name as 'Complete?', b.name as 'Snoozed?' FROM reminders r " \
                                                       "JOIN yes_no a ON r.complete=a.id JOIN yes_no b ON " \
                                                       "r.snoozed=b.id WHERE r.archived=1 ORDER BY DATE(substr(" \
                                                       "r.deadline, 7, 4)||'-'||substr (r.deadline, 1," \
                                                       "2)||'-'||substr(r.deadline, 4,2)) ASC "

        if id:
            s = "SELECT * FROM (" + s + ") WHERE CAST(ID AS text) LIKE '" + id + "%'"
        if name:
            s = "SELECT * FROM (" + s + ") WHERE Name LIKE '" + name + "%'"
        if description:
            s = "SELECT * FROM (" + s + ") WHERE Description LIKE '" + description + "%'"
        if date:
            s = "SELECT * FROM (" + s + ") WHERE \"Reminder Date\" LIKE '" + date + "%'"
        if complete:
            s = "SELECT * FROM (" + s + ") WHERE \"Complete?\" LIKE '" + complete + "%'"
        if snoozed:
            s = "SELECT * FROM (" + s + ") WHERE \"Snoozed?\" LIKE '" + snoozed + "%'"

        query.exec_(s)
        self.reminder_model.setQuery(query)
        db.close()

        self.reminders_tree.setModel(self.reminder_model)
        self.reminders_query = s

    def search_risk(self):
        id = self.risk_id_search.text()
        name = self.risk_name_search.text()
        type = self.risk_type_search.text()
        probability = self.risk_severity_search.currentText()
        impact = self.risk_end_search.currentText()
        end = self.risk_expired_search.text()
        expired = self.risk_filename_search.text()

        ids = self.fetch_query(
            "SELECT id FROM risks WHERE  substr(end_date, 7, 4)||'-'||substr (end_date, 1,2)||'-'||substr(end_date, "
            "4,2)<DATE('now') AND expired=0")
        if ids != []:
            for risk_id in ids:
                self.run_query("UPDATE risks SET expired=1 WHERE id=?", (risk_id,))
        ids = self.fetch_query(
            "SELECT id FROM risks WHERE  (substr(end_date, 7, 4)||'-'||substr (end_date, 1,2)||'-'||substr(end_date, "
            "4,2)>=DATE('now') AND expired=1) OR end_date=''")
        if ids != []:
            for risk_id in ids:
                self.run_query("UPDATE risks SET expired=0 WHERE id=?", (risk_id,))

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.risk_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        if self.risk_type_menu.currentIndex() == 0:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 1:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE r.expired=0 AND r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 2:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE r.expired=1 AND r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 3:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE r.favorite=1 AND r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 4:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2)=DATE('now') AND r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 5:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2) >= DATE('now', 'weekday 0', '-7 days') AND " \
                "r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 6:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2) >= DATE('now', 'start of month') AND " \
                "r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 7:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2) >= DATE('now', 'start of year') AND " \
                "r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 8:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2) BETWEEN DATE('now', 'start of month', " \
                "'-1 month') AND DATE('now', 'start of month') AND r.archived=0 "
        elif self.risk_type_menu.currentIndex() == 9:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE substr(r.date_created, 7, 4)||'-'||substr (" \
                "r.date_created, 1,2)||'-'||substr(r.date_created, 4,2) BETWEEN DATE('now', 'start of year', " \
                "'-1 year') AND DATE('now', 'start of year') AND r.archived=0 "
        else:
            s = "SELECT r.id as Id, r.name as Name, risk_types.name as Type, a.name as Probability, b.name as Impact, " \
                "r.end_date as 'End Date', c.name as 'Expired ?' FROM risks r JOIN risk_types ON " \
                "r.type_id=risk_types.id JOIN severities a on r.probability_id=a.id JOIN severities b ON " \
                "r.impact_id=b.id JOIN yes_no c ON r.expired=c.id WHERE r.archived=1 "

        if id:
            s = "SELECT * FROM (" + s + ") WHERE CAST(Id AS text) LIKE '" + id + "%'"
        if name:
            s = "SELECT * FROM (" + s + ") WHERE Name LIKE '" + name + "%'"
        if type:
            s = "SELECT * FROM (" + s + ") WHERE Type LIKE '" + type + "%'"
        if probability != 'Any':
            s = "SELECT * FROM (" + s + ") WHERE Probability LIKE '" + probability + "%'"
        if impact != 'Any':
            s = "SELECT * FROM (" + s + ") WHERE Impact LIKE '" + impact + "%'"
        if end:
            s = "SELECT * FROM (" + s + ") WHERE \"End Date\" LIKE '" + end + "%'"
        if expired:
            s = "SELECT * FROM (" + s + ") WHERE \"Expired ?\" LIKE '" + expired + "%'"

        query.exec_(s)
        self.risk_model.setQuery(query)
        db.close()

        self.risks_tree.setModel(self.risk_model)
        self.risks_query = s

        # All other tree views do not need this. I don't know why, but it works so I'll leave it here
        self.risks_tree.setColumnWidth(0, 155 * .75)
        self.risks_tree.setColumnWidth(1, 155 * .75)
        self.risks_tree.setColumnWidth(2, 150 * .75)
        self.risks_tree.setColumnWidth(3, 100 * .75)
        self.risks_tree.setColumnWidth(4, 150 * .75)
        self.risks_tree.setColumnWidth(5, 150 * .75)
        self.risks_tree.setColumnWidth(6, 155 * .75)
        self.risks_tree.setColumnWidth(7, 155 * .75)

    def search_todo(self):
        id = self.todo_id_search.text()
        subject = self.todo_subject_search.text()
        responsible = self.todo_responsible_search.text()
        status = self.todo_status_search.currentText()
        priority = self.todo_priority_search.currentText()
        severity = self.todo_severity_search.currentText()
        start = self.todo_type_search.text()
        resolution = self.todo_resolution_search.text()

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.todo_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        if self.todos_type_menu.currentIndex() == 0:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 1:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE NOT t.status_id=3 " \
                "AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 2:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(t.deadline, " \
                "7, 4) || '-' || substr(t.deadline, 1, 2) || '-' || substr(t.deadline, 4,2)<=DATE('now') AND NOT " \
                "t.deadline='' AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 3:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE t.favorite=1 AND " \
                "t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 4:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4," \
                "2)=DATE('now') AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 5:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4,2) >= DATE(" \
                "'now', 'weekday 0', '-7 days') AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 6:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4,2) >= DATE(" \
                "'now', 'start of month') AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 7:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4,2) >= DATE(" \
                "'now', 'start of year') AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 8:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of month', '-1 month') AND DATE('now', 'start of month') AND t.archived=0 "
        elif self.todos_type_menu.currentIndex() == 9:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE substr(" \
                "t.date_created, 7, 4)||'-'||substr (t.date_created, 1,2)||'-'||substr(t.date_created, 4,2) BETWEEN " \
                "DATE('now', 'start of year', '-1 year') AND DATE('now', 'start of year') AND t.archived=0 "
        else:
            s = "SELECT t.id as Id, t.subject as Subject, d.last as 'Assigned To', a.name as Status, b.name as " \
                "Priority, c.name as Severity, t.start_date as 'Start Date', t.deadline as 'Resolution Date' FROM " \
                "todos t JOIN todo_status a ON t.status_id=a.id JOIN severities c on t.severity_id=c.id JOIN " \
                "priorities b ON t.priority_id=b.id JOIN people d ON t.responsible_id=d.id WHERE t.archived=1 "

        if id:
            s = "SELECT * FROM (" + s + ") WHERE CAST(Id AS text) LIKE '" + id + "%'"
        if subject:
            s = "SELECT * FROM (" + s + ") WHERE Subject LIKE '" + subject + "%'"
        if responsible:
            s = "SELECT * FROM (" + s + ") WHERE \"Assigned To\" LIKE '" + responsible + "%'"
        if status != 'Any':
            s = "SELECT * FROM (" + s + ") WHERE Status LIKE '" + status + "%'"
        if priority != 'Any':
            s = "SELECT * FROM (" + s + ") WHERE Priority LIKE '" + priority + "%'"
        if severity != 'Any':
            s = "SELECT * FROM (" + s + ") WHERE Severity LIKE '" + severity + "%'"
        if start:
            s = "SELECT * FROM (" + s + ") WHERE \"Start Date\" LIKE '" + start + "%'"
        if resolution:
            s = "SELECT * FROM (" + s + ") WHERE \"Resolution Date\" LIKE '" + resolution + "%'"

        query.exec_(s)
        self.todo_model.setQuery(query)
        db.close()

        self.todos_tree.setModel(self.todo_model)
        self.todos_query = s

    def search_library(self):
        id = self.document_id_search.text()
        name = self.document_name_search.text()
        url = self.document_url_search.text()
        date = self.document_date_search.text()

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('data.db')
        if not db.open():
            print('Db not open')
        self.library_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()

        s = "SELECT id as ID, name as Name, url as Url, date_created as 'Date Created' FROM documents WHERE del=0"

        if self.document_type_search.currentIndex() != 0:
            s += " AND type_id = " + str(self.document_type_search.currentIndex())

        if id:
            s = "SELECT * FROM (" + s + ") WHERE CAST(ID AS TEXT) LIKE '" + str(id) + "%'"

        if name:
            s = "SELECT * FROM (" + s + ") WHERE Name LIKE '" + str(name) + "%'"

        if url:
            s = "SELECT * FROM (" + s + ") WHERE Url LIKE '%" + str(url) + "%'"

        if date:
            s = "SELECT * FROM (" + s + ") WHERE \"Date Created\" LIKE '" + str(date) + "%'"

        query.exec_(s)
        self.library_model.setQuery(query)
        db.close()

        self.library_tree.setModel(self.library_model)
        self.library_tree.setColumnWidth(0, 100 * .75)
        self.library_tree.setColumnWidth(1, 390 * .75)
        self.library_tree.setColumnWidth(2, 350 * .75)
        self.library_tree.setColumnWidth(3, 190 * .75)
