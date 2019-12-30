from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox
import window, contract, party
import sqlite3
import os
from shutil import copyfile

class Main(QtWidgets.QMainWindow, window.UiMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = window.UiMainWindow()
        self.ui.setup_ui(self)

        self.ui.contracts_open.clicked.connect(self.open_contract)
        self.ui.contracts_delete.clicked.connect(self.delete_contract)
        self.ui.new_button.clicked.connect(self.show_new_contract_window)

    def open_contract(self):
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            contract_index = self.ui.contracts_tree.selectedIndexes()[0]
            self.contract_name = contract_index.model().itemData(contract_index)[0]
            project_index = self.ui.contracts_tree.selectedIndexes()[1]
            self.project_name = project_index.model().itemData(project_index)[0]

            self.contract_window = ContractWindow(self.contract_name, self.project_name)
            self.contract_window.setWindowModality(QtCore.Qt.ApplicationModal)
            self.contract_window.contract_tree_signal.connect(self.update_contract_tree)
            self.contract_window.party_signal.connect(self.new_party_window)
            self.contract_window.show()

    def new_party_window(self):
        self.party_window = PartyWindow(self.contract_window.project_name)
        self.party_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.party_window.party_changed.connect(self.update_parties_tree)
        self.party_window.show()

    def new_project(self):
        # TODO: Implement new_project
        pass

    def settings(self):
        # TODO: Implement settings
        pass

    def show_new_contract_window(self):
        # TODO: Implement show_new_contract_window
        pass

    def add_contract(self):
        # TODO: Implement add_contract
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()
        add_contract_query = "INSERT INTO contracts(name, priority, deleted) VALUES('Contract 4', 3, 0)"
        cursor.execute(add_contract_query)
        connection.commit()
        connection.close()
        self.ui.contracts_tree.addItem('Added item')

    def delete_contract(self):
        # TODO: Implement delete_contract
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            contract_index = self.ui.contracts_tree.selectedIndexes()[0]
            contract_name = contract_index.model().itemData(contract_index)[0]
            project_index = self.ui.contracts_tree.selectedIndexes()[1]
            project_name = project_index.model().itemData(project_index)[0]

    def complete_contract(self):
        # TODO: Implement complete_contract
        pass

    def show_filters(self):
        # TODO: Implement show_filters
        pass

    def search_contracts(self):
        # TODO: Implement search_contracts
        pass

    def show_settings(self):
        # TODO: Implement show_settings
        pass

    def open_task(self):
        # TODO: Implement open_task
        pass

    def complete_task(self):
        # TODO: Implement complete_tasks
        pass

    def open_contract_from_task(self):
        # TODO: open_contract_from_task
        pass

    def delete_task(self):
        # TODO: delete_task
        pass

    def update_contract_tree(self):
        self.ui.refresh_contract_tree()

    def update_parties_tree(self):
        self.contract_window.update_parties_tree()

class ContractWindow(QtWidgets.QWidget, contract.Ui_Form):
    contract_tree_signal = QtCore.pyqtSignal()
    party_signal = QtCore.pyqtSignal()

    def __init__(self, contract_name, project_name):
        QtWidgets.QWidget.__init__(self)
        self.contract_name = contract_name
        self.project_name = project_name

        # Project ID:
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.notes_model = QtSql.QSqlRelationalTableModel()
        self.notes_model.setTable('projects')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT id FROM projects where name=?")
        query.addBindValue(self.project_name)
        query.exec_()
        if query.next():
            self.project_id = query.value(0)
        db.close()

        # Contract ID
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.notes_model = QtSql.QSqlRelationalTableModel()
        self.notes_model.setTable('contracts')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT id FROM contracts where name=? and project_id=?")
        query.addBindValue(self.contract_name)
        query.addBindValue(self.project_id)
        query.exec_()
        if query.next():
            self.contract_id = query.value(0)
        db.close()

        self.contract_ui = contract.Ui_Form()
        self.contract_ui.setupUi(self, self.contract_id, self.project_id)

        self.contract_ui.add_document_button.clicked.connect(self.add_document)
        self.contract_ui.pushButton_12.clicked.connect(self.edit_contract)
        self.contract_ui.pushButton_13.clicked.connect(self.edit_project)
        self.contract_ui.pushButton.clicked.connect(self.add_party)

    # Helping method to run simple queries
    def run_query(self, query, values=()):
        sqliteConnection = sqlite3.connect('Contracts.db')
        cursor = sqliteConnection.cursor()
        print('Connected to SQLite')
        cursor.execute(query, values)
        sqliteConnection.commit()
        print('Query executed')
        cursor.close()

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

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox()
        close.setWindowTitle('Exit Contract')
        close.setText('Exit contract?')
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def add_document(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Add File', '.')
        name = QtCore.QUrl.fromLocalFile(filename[0]).fileName()
        dir = os.path.dirname(os.path.realpath(__file__)) + "\\documents\\" + name

        copyfile(filename[0], dir)
        # Insert into database
        try:
            sqliteConnection = sqlite3.connect('Contracts.db')
            cursor = sqliteConnection.cursor()
            print('Connected to SQLite')
            query = """ INSERT INTO documents (contract_id, project_id, document) VALUES (?, ?, ?)"""
            record = (self.contract_id, self.project_id, name)
            cursor.execute(query, record)
            sqliteConnection.commit()
            print('Document added')
            cursor.close()

        except sqlite3.Error as error:
            print('Failed to insert document', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('Closed db')

    def open_document(self):
        # TODO: Implement open_document
        pass

    def delete_document(self):
        # TODO: Implement delete_document
        pass

    def edit_contract(self):
        # TODO: Check that name doesn't already exist
        dialog = QtWidgets.QInputDialog(self)
        dialog.setModal(True)
        new_name, ok = dialog.getText(self, 'Edit Name', 'Enter Contract Name', QtWidgets.QLineEdit.Normal, text=self.contract_name)
        if ok and new_name != '':
            self.original_contract_name = self.contract_name
            self.contract_name = new_name

        self.run_query("UPDATE contracts SET name=? WHERE id=?", (self.contract_name, self.contract_id))
        self.contract_ui.contract_label.setText(self.contract_name)
        self.contract_tree_signal.emit()

    def edit_project(self):
        dialog = QtWidgets.QInputDialog(self)
        dialog.setWindowTitle("Edit Project")
        dialog.setLabelText("Enter Project Name:")
        dialog.setTextValue(self.project_name)
        line_edit = dialog.findChild(QtWidgets.QLineEdit)
        self.project_list = self.fetch_query("SELECT name FROM projects")
        print(self.project_list)
        completer = QtWidgets.QCompleter(self.project_list, line_edit)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        line_edit.setCompleter(completer)

        ok, new_name = (
            dialog.exec_() == QtWidgets.QDialog.Accepted,
            dialog.textValue(),
        )
        if ok:
            if ok and new_name != '':
                self.original_project_name = self.project_name
                self.project_name = new_name

        self.run_query("UPDATE projects SET name=? WHERE id=?", (self.project_name, self.project_id))
        self.contract_ui.project_label.setText(self.project_name)
        self.contract_tree_signal.emit()

    def add_party(self):
        self.party_signal.emit()

    def edit_party(self):
        # TODO: Implement edit_party
        pass

    def delete_party(self):
        # TODO: Implement delete_party
        pass

    def add_task(self):
        # TODO: Implement add_task
        pass

    def complete_task(self):
        # TODO: Implement complete_task (from contract)
        pass

    def open_task(self):
        # TODO: Implement open_task (from contract)
        pass

    def delete_task(self):
        # TODO: Implement delete_task (from contract)
        pass

    def save_changes(self):
        # TODO: Implement save_changes
        pass

    def update_parties_tree(self):
        self.contract_ui.refresh_parties_tree()

class PartyWindow(QtWidgets.QWidget, party.Ui_partyDialog):
    party_changed = QtCore.pyqtSignal()

    def __init__(self, project_name):
        QtWidgets.QWidget.__init__(self)
        self.project_name = project_name

        # Project ID:
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        self.notes_model = QtSql.QSqlRelationalTableModel()
        self.notes_model.setTable('projects')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT id FROM projects where name=?")
        query.addBindValue(self.project_name)
        query.exec_()

        if query.next():
            self.project_id = query.value(0)

        db.close()

        self.party_ui = party.Ui_partyDialog()
        self.party_ui.setupUi(self, self.project_id)

        self.party_ui.pushButton.clicked.connect(self.save_party)
        self.party_ui.pushButton.clicked.connect(QtWidgets.QApplication.closeAllWindows)
        self.party_ui.pushButton_2.clicked.connect(self.close)

    def run_query(self, query, values=()):
        sqliteConnection = sqlite3.connect('Contracts.db')
        cursor = sqliteConnection.cursor()
        print('Connected to SQLite')
        cursor.execute(query, values)
        sqliteConnection.commit()
        print('Query executed')
        cursor.close()

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

    def save_party(self):
        name = self.party_ui.lineEdit.text()
        first = self.party_ui.lineEdit_2.text()
        last = self.party_ui.lineEdit_3.text()
        phone = self.party_ui.lineEdit_4.text()
        email = self.party_ui.lineEdit_5.text()

        if name != '' and first != '' and last != '' and phone != '' and email != '':
            self.run_query('INSERT INTO parties (project_id, name, representative_first, representative_last, phone, '
                           'email) VALUES (?, ?, ?, ?, ?, ?)', (self.project_id, name, first, last, phone, email))
            self.party_changed.emit()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = Main()
    Window.show()

    sys.exit(app.exec_())