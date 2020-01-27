from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sqlite3

class Ui_Form(object):
    def setupUi(self, Form, contract_id, project_id):
        self.contract_id = contract_id
        self.project_id = project_id
        self.executed  = self.fetch_query('SELECT executed FROM contracts WHERE id=?', (contract_id,))[0]
        self.active_check = self.fetch_query('SELECT active FROM contracts WHERE id=?', (contract_id,))[0]
        self.completed_check = self.fetch_query('SELECT completed FROM contracts WHERE id=?', (contract_id,))[0]
        Form.setObjectName("Form")
        Form.resize(1250, 680)
        Form.setMinimumSize(QtCore.QSize(1250, 680))
        Form.setMinimumSize(QtCore.QSize(1250, 680))
        Form.setMaximumSize(QtCore.QSize(1250, 680))


        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(1000, 29, 120, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(184, 184, 184);")
        self.label_4.setObjectName("label_4")

        # Notes model
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.notes_model = QtSql.QSqlRelationalTableModel()
        self.notes_model.setTable('contracts')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT notes FROM contracts where id=?")
        query.addBindValue(self.contract_id)
        query.exec_()
        if query.next():
            notes = query.value(0)
        db.close()

        # Notes
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(840, 80, 391, 311))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFontPointSize(11)
        self.textEdit.setText(notes)

        # Document model
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.document_model = QtSql.QSqlRelationalTableModel()
        self.document_model.setTable('tasks')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT document AS '' FROM documents WHERE contract_id=? AND project_id=?")
        query.addBindValue(self.contract_id)
        query.addBindValue(self.project_id)
        query.exec_()
        self.document_model.setQuery(query)
        db.close()

        # Documents List
        self.documents_list = QtWidgets.QListView(Form)
        self.documents_list.setGeometry(QtCore.QRect(840, 450, 391, 101))
        self.documents_list.setObjectName("documents_list")
        self.documents_list.setModel(self.document_model)
        self.documents_list.setAlternatingRowColors(True)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(980, 400, 131, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(184, 184, 184);")
        self.label_5.setObjectName("label_5")

        # Party model
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.party_model = QtSql.QSqlRelationalTableModel()
        self.party_model.setTable('parties')
        query = QtSql.QSqlQuery()
        query.prepare(
            "SELECT parties.name as Name, parties.representative_first as 'Representative "
            "First Name', parties.representative_last as 'Representative Last Name', parties.phone as 'Phone Number', "
            "parties.email as 'Email Address' FROM parties WHERE project_id = ?")
        query.addBindValue(self.project_id)
        query.exec_()
        self.party_model.setQuery(query)
        db.close()

        # Parties Tree
        # TODO: Change width of all columns
        self.parties_tree = QtWidgets.QTreeView(Form)
        self.parties_tree.setGeometry(QtCore.QRect(30, 140, 731, 131))
        self.parties_tree.setObjectName("parties_tree")
        self.parties_tree.setAlternatingRowColors(True)
        self.parties_tree.setModel(self.party_model)


        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 340, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Task model
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.task_model = QtSql.QSqlRelationalTableModel()
        self.task_model.setTable('tasks')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT tasks.Name as name, tasks.description as Description, tasks.deadline as Deadline, "
                      "parties.name as 'Assigned To', tasks.completed as Status, tasks.id as ID FROM tasks LEFT JOIN parties ON "
                      "tasks.party_id=parties.id WHERE contract_id=?")
        query.addBindValue(self.contract_id)
        query.exec_()
        self.task_model.setQuery(query)
        db.close()

        # Tasks tree
        self.tasks_tree = QtWidgets.QTreeView(Form)
        self.tasks_tree.setGeometry(QtCore.QRect(30, 430, 731, 181))
        self.tasks_tree.setObjectName("tasks_tree")
        self.tasks_tree.setAlternatingRowColors(True)
        self.tasks_tree.setModel(self.task_model)


        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1341, 701))
        self.frame.setStyleSheet("background-color: rgb(0, 7, 45);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 290, 295, 30))
        self.layoutWidget.setObjectName("layoutWidget")


        self.parties_buttons = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.parties_buttons.setContentsMargins(0, 0, 0, 0)
        self.parties_buttons.setObjectName("parties_buttons")


        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")


        self.parties_buttons.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")


        self.parties_buttons.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.parties_buttons.addWidget(self.pushButton_3)


        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 630, 295, 30))
        self.layoutWidget_2.setObjectName("layoutWidget_2")


        self.tasks_buttons = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.tasks_buttons.setContentsMargins(0, 0, 0, 0)
        self.tasks_buttons.setObjectName("tasks_buttons")

        # TODO: Add complete task button

        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tasks_buttons.addWidget(self.pushButton_4)


        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.tasks_buttons.addWidget(self.pushButton_5)


        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.tasks_buttons.addWidget(self.pushButton_6)


        self.layoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_3.setGeometry(QtCore.QRect(840, 580, 295, 30))
        self.layoutWidget_3.setObjectName("layoutWidget_3")


        self.documents_buttons = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.documents_buttons.setContentsMargins(0, 0, 0, 0)
        self.documents_buttons.setObjectName("documents_buttons")


        self.add_document_button = QtWidgets.QPushButton(self.layoutWidget_3)
        self.add_document_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add_document_button.setObjectName("add_document_button")
        self.documents_buttons.addWidget(self.add_document_button)


        self.open_document_button = QtWidgets.QPushButton(self.layoutWidget_3)
        self.open_document_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.open_document_button.setObjectName("open_document_button")
        self.documents_buttons.addWidget(self.open_document_button)

        self.delete_document_button = QtWidgets.QPushButton(self.layoutWidget_3)
        self.delete_document_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delete_document_button.setObjectName("delete_document_button")
        self.documents_buttons.addWidget(self.delete_document_button)


        self.save = QtWidgets.QPushButton(self.frame)
        self.save.setGeometry(QtCore.QRect(840, 630, 171, 28))
        self.save.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.save.setObjectName("save")


        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(335, 90, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(184, 184, 184);")
        self.label_6.setObjectName("label_6")


        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(370, 380, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(184, 184, 184);")
        self.label_7.setObjectName("label_7")


        self.status_buttons = QtWidgets.QWidget(self.frame)
        self.status_buttons.setGeometry(QtCore.QRect(450, 300, 314, 22))
        self.status_buttons.setObjectName("status_buttons")


        self.status_layout = QtWidgets.QHBoxLayout(self.status_buttons)
        self.status_layout.setContentsMargins(0, 0, 0, 0)
        self.status_layout.setObjectName("status_layout")


        self.checkBox = QtWidgets.QCheckBox(self.status_buttons)
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.status_layout.addWidget(self.checkBox)


        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.status_layout.addItem(spacerItem)

        self.active = QtWidgets.QRadioButton(self.status_buttons)
        self.active.setStyleSheet("color: rgb(255, 255, 255);")
        self.active.setObjectName("active")
        self.status_layout.addWidget(self.active)


        self.completed = QtWidgets.QRadioButton(self.status_buttons)
        self.completed.setStyleSheet("color: rgb(255, 255, 255);")
        self.completed.setObjectName("completed")
        self.status_layout.addWidget(self.completed)

        # Status buttons
        if self.executed == 1:
            self.checkBox.setChecked(True)

        if self.active_check == 1:
            self.active.setChecked(True)

        if self.completed_check == 1:
            self.completed.setChecked(True)

        self.names = QtWidgets.QWidget(Form)
        self.names.setGeometry(QtCore.QRect(31, 21, 731, 61))
        self.names.setObjectName("names")


        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.names)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Contract Name
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.notes_model = QtSql.QSqlRelationalTableModel()
        self.notes_model.setTable('contracts')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT name FROM contracts where id=? AND project_id=?")
        query.addBindValue(self.contract_id)
        query.addBindValue(self.project_id)
        query.exec_()
        if query.next():
            contract = query.value(0)
        db.close()
        self.contract_label = QtWidgets.QLabel(self.names)
        self.contract_label.setText(contract)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.contract_label.setFont(font)
        self.contract_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.contract_label.setObjectName("contract_label")
        self.horizontalLayout_2.addWidget(self.contract_label)


        self.pushButton_12 = QtWidgets.QPushButton(self.names)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_2.addWidget(self.pushButton_12)


        self.label_3 = QtWidgets.QLabel(self.names)
        font = QtGui.QFont()
        font.setPointSize(52)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        # Project Name
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT name FROM projects where id=?")
        query.addBindValue(project_id)
        query.exec_()
        if query.next():
            project = query.value(0)
        db.close()
        self.project_label = QtWidgets.QLabel(self.names)
        self.project_label.setText(project)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.project_label.setText(project)
        self.project_label.setFont(font)
        self.project_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.project_label.setObjectName("project_label")
        self.horizontalLayout_2.addWidget(self.project_label)


        self.pushButton_13 = QtWidgets.QPushButton(self.names)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_2.addWidget(self.pushButton_13)


        self.frame.raise_()
        self.label_4.raise_()
        self.textEdit.raise_()
        self.documents_list.raise_()
        self.label_5.raise_()
        self.parties_tree.raise_()
        self.line.raise_()
        self.tasks_tree.raise_()
        self.names.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Notes"))
        self.label_5.setText(_translate("Form", "Documents"))
        self.pushButton.setText(_translate("Form", "Add"))
        self.pushButton_2.setText(_translate("Form", "Edit"))
        self.pushButton_3.setText(_translate("Form", "Delete"))
        self.pushButton_4.setText(_translate("Form", "Add"))
        self.pushButton_5.setText(_translate("Form", "View/Edit"))
        self.pushButton_6.setText(_translate("Form", "Delete"))
        self.add_document_button.setText(_translate("Form", "Add"))
        self.open_document_button.setText(_translate("Form", "Open"))
        self.delete_document_button.setText(_translate("Form", "Delete"))
        self.save.setText(_translate("Form", "SAVE CHANGES"))
        self.label_6.setText(_translate("Form", "Parties"))
        self.label_7.setText(_translate("Form", "Tasks"))
        self.checkBox.setText(_translate("Form", "Fully Executed"))
        self.active.setText(_translate("Form", "Active"))
        self.completed.setText(_translate("Form", "Completed"))
        self.pushButton_12.setText(_translate("Form", "Edit"))
        self.label_3.setText(_translate("Form", "-"))
        self.pushButton_13.setText(_translate("Form", "Edit"))

    def refresh_parties_tree(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.party_model = QtSql.QSqlRelationalTableModel()
        self.party_model.setTable('parties')
        query = QtSql.QSqlQuery()
        query.prepare(
            "SELECT parties.name as Name, parties.representative_first as 'Representative "
            "First Name', parties.representative_last as 'Representative Last Name', parties.phone as 'Phone Number', "
            "parties.email as 'Email Address' FROM parties WHERE project_id = ?")
        query.addBindValue(self.project_id)
        query.exec_()
        self.party_model.setQuery(query)
        db.close()
        self.parties_tree.setModel(self.party_model)

    def fetch_query(self, query, values=()):
        sqliteConnection = sqlite3.connect('Contracts.db')
        cursor = sqliteConnection.cursor()
        print('Connected to SQLite')
        cursor.execute(query, values)
        sqliteConnection.commit()
        print('Query executed')
        results_tuple = cursor.fetchall()
        results = [item for t in results_tuple for item in t]
        cursor.close()
        return results

    def refresh_document_list(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.document_model = QtSql.QSqlRelationalTableModel()
        self.document_model.setTable('tasks')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT document AS '' FROM documents WHERE contract_id=? AND project_id=?")
        query.addBindValue(self.contract_id)
        query.addBindValue(self.project_id)
        query.exec_()
        self.document_model.setQuery(query)
        db.close()
        self.documents_list.setModel(self.document_model)

    def refresh_tasks_tree(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.task_model = QtSql.QSqlRelationalTableModel()
        self.task_model.setTable('tasks')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT tasks.Name as name, tasks.description as Description, tasks.deadline as Deadline, "
                      "parties.name as 'Assigned To', tasks.completed as Status, tasks.id as ID FROM tasks LEFT JOIN parties ON "
                      "tasks.party_id=parties.id WHERE contract_id=?")
        query.addBindValue(self.contract_id)
        query.exec_()
        self.task_model.setQuery(query)
        db.close()
        self.tasks_tree.setModel(self.task_model)