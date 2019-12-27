from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox
import window, contracts
import sqlite3
import os
from shutil import copyfile

class Main(QtWidgets.QMainWindow, window.UiMainWindow):
    main_signal = QtCore.pyqtSignal()

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
            self.contract_window.show()

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

        # print('here')
        # reply = QMessageBox.question(self, 'Delete Contract', 'Are you sure you want to delete {0}?'.format(
        #     str(item.text())), QMessageBox.Yes | QMessageBox.No)
        # if reply == QMessageBox.Yes:
        #     item = self.ui.contracts_tree.takeItem(row)
        #     name = item.text()
        #     del item

            # connection = sqlite3.connect('test.db')
            # cursor = connection.cursor()
            # name_query = (name,)
            # #contract_id = connection.execute("SELECT id FROM contracts WHERE name = ? AND deleted = 0", (name,))
            # cursor.execute('UPDATE contracts SET deleted=1 WHERE name=?', name_query)
            # connection.commit()
            # connection.close()

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


class ContractWindow(QtWidgets.QWidget, contracts.Ui_Form):
    contract_tree_signal = QtCore.pyqtSignal()

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

        self.contract_ui = contracts.Ui_Form()
        self.contract_ui.setupUi(self, self.contract_id, self.project_id)

        self.contract_ui.add_document_button.clicked.connect(self.add_document)
        self.contract_ui.pushButton_12.clicked.connect(self.edit_contract)
        self.contract_ui.pushButton_13.clicked.connect(self.edit_project)

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

            print('here')
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
        # TODO: Implement add_party
        pass

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = Main()
    Window.show()

    sys.exit(app.exec_())