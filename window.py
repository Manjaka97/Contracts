from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox
import resources_rc
import sqlite3

class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1500, 900)
        main_window.setMinimumSize(QtCore.QSize(1500, 900))
        main_window.setMaximumSize(QtCore.QSize(1500, 900))
        main_window.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setStyleSheet("QPushButton#new_button:hover\n"
                                         "{\n"
                                         "    color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#new_button\n"
                                         "{\n"
                                         "    color: rgb(205,205,205);\n"
                                         "    background-image: url(:/images/images/new_contract_icon.svg);\n"
                                         "    background-position: center left;\n"
                                         "    background-repeat: no-repeat;\n"
                                         "    padding-left:5px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#settings_button\n"
                                         "{\n"
                                         "    color: rgb(205,205,205);\n"
                                         "    background-image: url(:/images/images/settings_icon.svg);\n"
                                         "    background-position: center left;\n"
                                         "    background-repeat: no-repeat;\n"
                                         "    padding-left:5px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#settings_button:hover\n"
                                         "{\n"
                                         "    color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QFrame#tasks_frame\n"
                                         "{\n"
                                         "    background-image: url(:/images/images/task_bg.jpg);\n"                                        
                                         "    background-repeat:no-repeat;\n"
                                         "}\n"
                                         "\n"
                                         "QFrame#contracts_frame\n"
                                         "{\n"
                                         "    background-color: rgb(240, 10, 70);\n"
                                         "}\n"
                                         "QTreeView#contracts_tree:item\n"
                                         "{\n"
                                         "    padding: 4px;\n"
                                         "}\n"
                                         "QTreeView#upcoming_tree:item\n"
                                         "{\n"
                                         "    padding: 10px;\n"
                                         "}\n"
                                         "QTreeView#overdue_tree:item\n"
                                         "{\n"
                                         "    padding: 10px;\n"
                                         "}\n"
                                         "QTreeView#completed_tree:item\n"
                                         "{\n"
                                         "    padding: 10px;\n"
                                         "}\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")

        # Top menu frame
        self.top_menu_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_menu_frame.setGeometry(QtCore.QRect(0, 0, 1500, 70))
        self.top_menu_frame.setMinimumSize(QtCore.QSize(1500, 70))
        self.top_menu_frame.setMaximumSize(QtCore.QSize(1500, 70))
        self.top_menu_frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.top_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_menu_frame.setObjectName("top_menu_frame")

        # Logo
        self.logo = QtWidgets.QLabel(self.top_menu_frame)
        self.logo.setGeometry(QtCore.QRect(1350, 15, 150, 40))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/images/images/logo.svg"))
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")

        # New contract button
        self.new_button = QtWidgets.QPushButton(self.top_menu_frame)
        self.new_button.setGeometry(QtCore.QRect(50, 0, 150, 70))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(14)
        self.new_button.setFont(font)
        self.new_button.setObjectName("new_button")

        # Settings button
        self.settings_button = QtWidgets.QPushButton(self.top_menu_frame)
        self.settings_button.setGeometry(QtCore.QRect(240, 0, 110, 70))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(14)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.new_button.raise_()
        self.logo.raise_()
        self.settings_button.raise_()

        # Contracts frame
        self.contracts_frame = QtWidgets.QFrame(self.centralwidget)
        self.contracts_frame.setGeometry(QtCore.QRect(0, 70, 450, 900))
        self.contracts_frame.setMinimumSize(QtCore.QSize(450, 900))
        self.contracts_frame.setStyleSheet("")
        self.contracts_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contracts_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contracts_frame.setObjectName("contracts_frame")

        # Contracts label
        self.contracts_label = QtWidgets.QLabel(self.contracts_frame)
        self.contracts_label.setGeometry(QtCore.QRect(180, 10, 60, 40))
        self.contracts_label.setText("")
        self.contracts_label.setPixmap(QtGui.QPixmap(":/images/images/contract.svg"))
        self.contracts_label.setScaledContents(True)
        self.contracts_label.setObjectName("contracts_label")

        # Contracts icon
        self.contracts_icon = QtWidgets.QLabel(self.contracts_frame)
        self.contracts_icon.setGeometry(QtCore.QRect(40, 0, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.contracts_icon.setFont(font)
        self.contracts_icon.setObjectName("contracts_icon")

        # Contracts line
        self.contracts_line = QtWidgets.QFrame(self.contracts_frame)
        self.contracts_line.setGeometry(QtCore.QRect(40, 60, 200, 15))
        self.contracts_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.contracts_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.contracts_line.setObjectName("contracts_line")

        # Contracts search bar
        self.contracts_search = QtWidgets.QLineEdit(self.contracts_frame)
        self.contracts_search.setGeometry(QtCore.QRect(40, 80, 200, 30))
        self.contracts_search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contracts_search.setText("")
        self.contracts_search.setObjectName("contracts_search")

        # Contracts search button
        self.contracts_search_2 = QtWidgets.QPushButton(self.contracts_frame)
        self.contracts_search_2.setEnabled(True)
        self.contracts_search_2.setGeometry(QtCore.QRect(250, 82, 30, 28))
        self.contracts_search_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "background-image: url(:/images/images/search_icon.png);\n"
                                              "background-position: center;\n"
                                              "background-repeat: no-repeat;\n"
                                              "")
        self.contracts_search_2.setText("")
        self.contracts_search_2.setObjectName("contracts_search_2")

        # Contracts search filter button
        self.contracts_filter = QtWidgets.QPushButton(self.contracts_frame)
        self.contracts_filter.setGeometry(QtCore.QRect(290, 80, 93, 30))
        self.contracts_filter.setStyleSheet("background-color: white;")
        self.contracts_filter.setObjectName("contracts_filter")

        # Contracts model
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.contract_model = QtSql.QSqlRelationalTableModel()
        self.contract_model.setTable('contracts')
        query = QtSql.QSqlQuery()
        query.exec_("SELECT contracts.name as Name, projects.name as Project FROM contracts JOIN projects ON contracts.project_id = projects.id")
        self.contract_model.setQuery(query)
        db.close()

        # Contracts tree
        self.contracts_tree = QtWidgets.QTreeView(self.contracts_frame)
        self.contracts_tree.setGeometry(QtCore.QRect(40, 170, 350, 520))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.contracts_tree.setFont(font)
        self.contracts_tree.setStyleSheet("background-color: white;")
        self.contracts_tree.setObjectName("contracts_tree")

        self.contracts_tree.setModel(self.contract_model)
        self.contracts_tree.setColumnWidth(0, 200)

        # Contracts buttons layout
        self.layoutWidget = QtWidgets.QWidget(self.contracts_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 720, 315, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.contracts_buttons = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.contracts_buttons.setContentsMargins(0, 0, 0, 0)
        self.contracts_buttons.setObjectName("contracts_buttons")

        # Contracts open button
        self.contracts_open = QtWidgets.QPushButton(self.layoutWidget)
        self.contracts_open.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contracts_open.setObjectName("contracts_open")
        self.contracts_buttons.addWidget(self.contracts_open)

        # Contracts mark as complete button
        self.contracts_complete = QtWidgets.QPushButton(self.layoutWidget)
        self.contracts_complete.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contracts_complete.setObjectName("contracts_complete")
        self.contracts_buttons.addWidget(self.contracts_complete)

        # Contracts delete button
        self.contracts_delete = QtWidgets.QPushButton(self.layoutWidget)
        self.contracts_delete.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contracts_delete.setObjectName("contracts_delete")
        self.contracts_buttons.addWidget(self.contracts_delete)

        # Tasks label
        self.tasks_label = QtWidgets.QLabel(self.centralwidget)
        self.tasks_label.setGeometry(QtCore.QRect(560, 70, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tasks_label.setFont(font)
        self.tasks_label.setObjectName("tasks_label")

        # Tasks icon
        self.tasks_icon = QtWidgets.QLabel(self.centralwidget)
        self.tasks_icon.setGeometry(QtCore.QRect(500, 80, 40, 40))
        self.tasks_icon.setText("")
        self.tasks_icon.setPixmap(QtGui.QPixmap(":/images/images/tasks_icon.svg"))
        self.tasks_icon.setScaledContents(True)
        self.tasks_icon.setObjectName("tasks_icon")

        # Tasks line
        self.tasks_line = QtWidgets.QFrame(self.centralwidget)
        self.tasks_line.setGeometry(QtCore.QRect(500, 130, 140, 15))
        self.tasks_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.tasks_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tasks_line.setObjectName("tasks_line")

        # Tasks tabs
        self.tasks_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tasks_tab.setGeometry(QtCore.QRect(500, 150, 950, 611))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tasks_tab.setFont(font)
        self.tasks_tab.setObjectName("tasks_tab")

        # Tasks upcoming tab
        self.upcoming_tab = QtWidgets.QWidget()
        self.upcoming_tab.setObjectName("upcoming_tab")

        # Tasks upcoming frame
        self.upcoming_frame = QtWidgets.QFrame(self.upcoming_tab)
        self.upcoming_frame.setGeometry(QtCore.QRect(0, 10, 1050, 80))
        self.upcoming_frame.setStyleSheet("background-color: rgb(0, 100, 167);")
        self.upcoming_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upcoming_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upcoming_frame.setObjectName("upcoming_frame")

        # Tasks upcoming layout
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.upcoming_frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 950, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.upcoming_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.upcoming_layout.setContentsMargins(0, 0, 0, 0)
        self.upcoming_layout.setObjectName("upcoming_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.upcoming_layout.addItem(spacerItem)

        # Tasks upcoming label
        self.upcoming_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.upcoming_label.setFont(font)
        self.upcoming_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.upcoming_label.setObjectName("upcoming_label")
        self.upcoming_layout.addWidget(self.upcoming_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.upcoming_layout.addItem(spacerItem1)

        # Upcoming Tasks model
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.upcoming_tasks_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_("SELECT name as Name, description as Description, deadline as Deadline FROM tasks WHERE deadline>=DATE('now') AND completed=0;")
        self.upcoming_tasks_model.setQuery(query)
        db.close()

        # Tasks upcoming tree
        self.upcoming_tree = QtWidgets.QTreeView(self.upcoming_tab)
        self.upcoming_tree.setGeometry(QtCore.QRect(0, 90, 950, 490))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(30)
        self.upcoming_tree.setFont(font)
        self.upcoming_tree.setObjectName("upcoming_tree")
        self.tasks_tab.addTab(self.upcoming_tab, "")

        self.upcoming_tree.setModel(self.upcoming_tasks_model)
        self.upcoming_tree.setColumnWidth(0, 180)
        self.upcoming_tree.setColumnWidth(1, 600)
        self.upcoming_tree.setAlternatingRowColors(True)


        # Tasks overdue tab
        self.overdue_tab = QtWidgets.QWidget()
        self.overdue_tab.setObjectName("overdue_tab")

        # Tasks overdue frame
        self.overdue_frame = QtWidgets.QFrame(self.overdue_tab)
        self.overdue_frame.setGeometry(QtCore.QRect(0, 10, 1050, 80))
        self.overdue_frame.setStyleSheet("background-color: rgb(240, 10, 70);")
        self.overdue_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.overdue_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.overdue_frame.setObjectName("overdue_frame")

        # tasks overdue layout
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.overdue_frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 950, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.overdue_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.overdue_layout.setContentsMargins(0, 0, 0, 0)
        self.overdue_layout.setObjectName("overdue_layout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.overdue_layout.addItem(spacerItem2)

        # Tasks overdue label
        self.overdue_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.overdue_label.setFont(font)
        self.overdue_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.overdue_label.setObjectName("overdue_label")
        self.overdue_layout.addWidget(self.overdue_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.overdue_layout.addItem(spacerItem3)

        # Overdue Tasks model
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.overdue_tasks_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_("SELECT name as Name, description as Description, deadline as Deadline FROM tasks WHERE deadline<DATE('now') AND completed=0;")
        self.overdue_tasks_model.setQuery(query)
        db.close()

        # Tasks overdue tree
        self.overdue_tree = QtWidgets.QTreeView(self.overdue_tab)
        self.overdue_tree.setGeometry(QtCore.QRect(0, 90, 950, 490))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.overdue_tree.setFont(font)
        self.overdue_tree.setObjectName("overdue_tree")
        self.tasks_tab.addTab(self.overdue_tab, "")

        self.overdue_tree.setModel(self.overdue_tasks_model)
        self.overdue_tree.setColumnWidth(0, 180)
        self.overdue_tree.setColumnWidth(1, 600)
        self.overdue_tree.setAlternatingRowColors(True)

        # Tasks complete tab
        self.completed_tab = QtWidgets.QWidget()
        self.completed_tab.setObjectName("completed_tab")

        # Tasks completed frame
        self.completed_frame = QtWidgets.QFrame(self.completed_tab)
        self.completed_frame.setGeometry(QtCore.QRect(0, 10, 1050, 80))
        self.completed_frame.setStyleSheet("background-color: rgb(0, 225, 100);")
        self.completed_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.completed_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.completed_frame.setObjectName("completed_frame")

        # Tasks completed layout
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.completed_frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 950, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.completed_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.completed_layout.setContentsMargins(0, 0, 0, 0)
        self.completed_layout.setObjectName("completed_layout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.completed_layout.addItem(spacerItem4)

        # Tasks completed label
        self.completed_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.completed_label.setFont(font)
        self.completed_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.completed_label.setObjectName("completed_label")
        self.completed_layout.addWidget(self.completed_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.completed_layout.addItem(spacerItem5)

        # Completed Tasks model
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.completed_tasks_model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_("SELECT name as Name, description as Description, date_completed as 'Completion Date' FROM tasks WHERE completed=1;")
        self.completed_tasks_model.setQuery(query)
        db.close()

        # Tasks completed tree
        self.completed_tree = QtWidgets.QTreeView(self.completed_tab)
        self.completed_tree.setGeometry(QtCore.QRect(0, 90, 950, 490))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.completed_tree.setFont(font)
        self.completed_tree.setObjectName("completed_tree")
        self.tasks_tab.addTab(self.completed_tab, "")

        self.completed_tree.setModel(self.completed_tasks_model)
        self.completed_tree.setColumnWidth(0, 180)
        self.completed_tree.setColumnWidth(1, 600)
        self.completed_tree.setAlternatingRowColors(True)

        # Tasks frame
        self.tasks_frame = QtWidgets.QFrame(self.centralwidget)
        self.tasks_frame.setGeometry(QtCore.QRect(450, 69, 1050, 831))
        self.tasks_frame.setStyleSheet("")
        self.tasks_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tasks_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tasks_frame.setObjectName("tasks_frame")

        # Tasks buttons layout
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(500, 790, 415, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.tasks_buttons = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.tasks_buttons.setContentsMargins(0, 0, 0, 0)
        self.tasks_buttons.setObjectName("tasks_buttons")

        # Tasks open button
        self.tasks_open = QtWidgets.QPushButton(self.layoutWidget1)
        self.tasks_open.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tasks_open.setObjectName("tasks_open")
        self.tasks_buttons.addWidget(self.tasks_open)

        # Tasks complete button
        self.tasks_complete = QtWidgets.QPushButton(self.layoutWidget1)
        self.tasks_complete.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tasks_complete.setObjectName("tasks_complete")
        self.tasks_buttons.addWidget(self.tasks_complete)

        # Tasks view button
        self.tasks_view = QtWidgets.QPushButton(self.layoutWidget1)
        self.tasks_view.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tasks_view.setObjectName("tasks_view")
        self.tasks_buttons.addWidget(self.tasks_view)

        # Tasks delete button
        self.tasks_delete = QtWidgets.QPushButton(self.layoutWidget1)
        self.tasks_delete.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tasks_delete.setObjectName("tasks_delete")
        self.tasks_buttons.addWidget(self.tasks_delete)

        # Raise
        self.tasks_delete.raise_()
        self.tasks_view.raise_()
        self.tasks_complete.raise_()
        self.tasks_open.raise_()
        self.tasks_frame.raise_()
        self.top_menu_frame.raise_()
        self.contracts_frame.raise_()
        self.tasks_label.raise_()
        self.tasks_icon.raise_()
        self.tasks_line.raise_()
        self.tasks_tab.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget1.raise_()

        main_window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(main_window)
        self.tasks_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Contracts"))
        self.new_button.setText(_translate("MainWindow", "New Contract"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))
        self.contracts_icon.setText(_translate("MainWindow", "Contracts                  "))
        self.contracts_search.setPlaceholderText(_translate("MainWindow", "Search contracts"))
        self.contracts_filter.setText(_translate("MainWindow", "Filters"))
        self.contracts_open.setText(_translate("MainWindow", "Open"))
        self.contracts_complete.setText(_translate("MainWindow", "Mark As Complete"))
        self.contracts_delete.setText(_translate("MainWindow", "Delete"))
        self.tasks_label.setText(_translate("MainWindow", "Tasks"))
        self.upcoming_label.setText(_translate("MainWindow", "UPCOMING TASKS: "))
        self.tasks_tab.setTabText(self.tasks_tab.indexOf(self.upcoming_tab), _translate("MainWindow", "Upcoming"))
        self.overdue_label.setText(_translate("MainWindow", "OVERDUE TASKS: "))
        self.tasks_tab.setTabText(self.tasks_tab.indexOf(self.overdue_tab), _translate("MainWindow", "Overdue"))
        self.completed_label.setText(_translate("MainWindow", "RECENTLY COMPLETED TASKS: "))
        self.tasks_tab.setTabText(self.tasks_tab.indexOf(self.completed_tab),
                                  _translate("MainWindow", "Recently Completed"))
        self.tasks_open.setText(_translate("MainWindow", "Open"))
        self.tasks_complete.setText(_translate("MainWindow", "Mark As Complete"))
        self.tasks_view.setText(_translate("MainWindow", "View Contract"))
        self.tasks_delete.setText(_translate("MainWindow", "Delete"))
