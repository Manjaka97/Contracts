from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(321, 95)
        Form.setMinimumSize(QtCore.QSize(321, 95))
        Form.setMaximumSize(QtCore.QSize(321, 95))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 20, 297, 61))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # ComboBox
        ids = self.fetch_query('SELECT id FROM people')
        firsts = self.fetch_query('SELECT first FROM people')
        lasts = self.fetch_query('SELECT last FROM people')
        people = []
        for id_num, first, last in zip(ids, firsts, lasts):
            name = str(id_num) + ' - ' + str(first) + ' ' + str(last)
            people.append(name)

        self.comboBox = QtWidgets.QComboBox(self.widget)
        for person in people:
            self.comboBox.addItem(person)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select = QtWidgets.QPushButton(self.widget)
        self.select.setObjectName("select")
        self.horizontalLayout.addWidget(self.select)
        self.new_2 = QtWidgets.QPushButton(self.widget)
        self.new_2.setObjectName("new_2")
        self.horizontalLayout.addWidget(self.new_2)
        self.cancel = QtWidgets.QPushButton(self.widget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.select.setText(_translate("Form", "Select"))
        self.new_2.setText(_translate("Form", "Create New"))
        self.cancel.setText(_translate("Form", "Cancel"))

    def run_query(self, query, values=()):
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()
        print('Connected to SQLite')
        cursor.execute(query, values)
        sqliteConnection.commit()
        print('Query executed')
        cursor.close()

    def fetch_query(self, query, values=()):
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()
        print('Connected to SQLite')
        cursor.execute(query, values)
        sqliteConnection.commit()
        print('Query executed')
        results_tuple = cursor.fetchall()
        results = [item for t in results_tuple for item in t]
        cursor.close()
        return results