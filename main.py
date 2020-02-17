# TODO: Remove unnecessary signals and simplify method calls
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox
import window, contract, party
import sqlite3
import os
# TODO: fix open pdf with webbrowser or other alternative
import webbrowser
from shutil import copyfile

class Main(QtWidgets.QMainWindow, window.UiMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = window.UiMainWindow()
        self.ui.setup_ui(self)

        self.ui.contracts_open.clicked.connect(self.open_contract)
        self.ui.contracts_delete.clicked.connect(self.delete_contract)
        self.ui.new_button.clicked.connect(self.show_new_contract_window)
        self.ui.tasks_delete.clicked.connect(self.delete_completed_task)
        self.ui.tasks_delete.clicked.connect(self.delete_overdue_task)
        self.ui.tasks_delete.clicked.connect(self.delete_upcoming_task)

    def open_contract(self):
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.contracts_tree.selectedIndexes()[2]
            self.contract_id = id_index.model().itemData(id_index)[0]

            self.contract_window = ContractWindow(self.contract_id)
            self.contract_window.setWindowModality(QtCore.Qt.ApplicationModal)
            self.contract_window.contract_tree_signal.connect(self.update_contracts_tree)
            self.contract_window.new_party_signal.connect(self.new_party_window)
            self.contract_window.edit_party_signal.connect(self.edit_party_window)
            self.contract_window.delete_party_signal.connect(self.delete_party)
            self.contract_window.delete_document_signal.connect(self.update_document_list)
            self.contract_window.new_document_signal.connect(self.update_document_list)
            self.contract_window.delete_task_signal.connect(self.update_tasks_tree)
            self.contract_window.show()

    def run_query(self, query, values=()):
        sqliteConnection = sqlite3.connect('Contracts.db')
        cursor = sqliteConnection.cursor()
        print('Connected to SQLite')
        cursor.execute(query, values)
        sqliteConnection.commit()
        print('Query executed')
        cursor.close()

    def delete_party(self, name, project_id):
        prompt = 'Are you sure you want to delete ' + name + '?'
        buttonReply = QMessageBox.question(self, 'Delete Party', prompt,
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.run_query('DELETE FROM parties WHERE name=? AND project_id=?', (name, project_id))
            self.contract_window.update_parties_tree()

    def new_party_window(self):
        self.party_window = PartyWindow(self.contract_window.project_name)
        self.party_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.party_window.party_changed.connect(self.update_parties_tree)
        self.party_window.show()

    def edit_party_window(self, name, first, last, phone, email):
        self.party_window = PartyWindow(self.contract_window.project_name, name=name, first=first, last=last, phone=phone, email=email, update=True)
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

    def open_upcoming_task_contract(self):
        if self.ui.upcoming_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.upcoming_tree.selectedIndexes()[3]
            task_id = id_index.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete this task?'
            buttonReply = QMessageBox.question(self, 'Delete Task', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM tasks WHERE id=?', (task_id,))
                self.ui.refresh_tasks_trees()

    def open_overdue_task_contract(self):
        if self.ui.overdue_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.overdue_tree.selectedIndexes()[3]
            task_id = id_index.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete this task?'
            buttonReply = QMessageBox.question(self, 'Delete Task', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM tasks WHERE id=?', (task_id,))
                self.ui.refresh_tasks_trees()

    def open_completed_task_contract(self):
        if self.ui.completed_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.completed_tree.selectedIndexes()[3]
            task_id = id_index.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete this task?'
            buttonReply = QMessageBox.question(self, 'Delete Task', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM tasks WHERE id=?', (task_id,))
                self.ui.refresh_tasks_trees()

    def open_contract_from_task(self):
        # TODO: open_contract_from_task
        pass

    def delete_upcoming_task(self):
        if self.ui.upcoming_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.upcoming_tree.selectedIndexes()[3]
            task_id = id_index.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete this task?'
            buttonReply = QMessageBox.question(self, 'Delete Task', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM tasks WHERE id=?', (task_id,))
                self.ui.refresh_tasks_trees()

    def delete_overdue_task(self):
        if self.ui.overdue_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.overdue_tree.selectedIndexes()[3]
            task_id = id_index.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete this task?'
            buttonReply = QMessageBox.question(self, 'Delete Task', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM tasks WHERE id=?', (task_id,))
                self.ui.refresh_tasks_trees()

    def delete_completed_task(self):
        if self.ui.completed_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.completed_tree.selectedIndexes()[3]
            task_id = id_index.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete this task?'
            buttonReply = QMessageBox.question(self, 'Delete Task', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM tasks WHERE id=?', (task_id,))
                self.ui.refresh_tasks_trees()

    def update_contracts_tree(self):
        self.ui.refresh_contract_tree()

    def update_parties_tree(self):
        self.contract_window.update_parties_tree()

    def update_document_list(self):
        self.contract_window.update_document_list()

    def update_tasks_tree(self):
        self.ui.refresh_tasks_trees()
        self.contract_window.update_tasks_tree()

class ContractWindow(QtWidgets.QWidget, contract.Ui_Form):
    contract_tree_signal = QtCore.pyqtSignal()
    new_party_signal = QtCore.pyqtSignal()
    edit_party_signal = QtCore.pyqtSignal(str, str, str, str, str)
    delete_party_signal = QtCore.pyqtSignal(str, int)
    new_document_signal = QtCore.pyqtSignal()
    delete_document_signal = QtCore.pyqtSignal()
    delete_task_signal = QtCore.pyqtSignal()

    def __init__(self, contract_id):
        QtWidgets.QWidget.__init__(self)
        self.contract_id = contract_id
        self.dir = os.path.dirname(os.path.realpath(__file__)) + "\\documents\\"

        # Project ID:
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT project_id FROM contracts where id=?")
        query.addBindValue(self.contract_id)
        query.exec_()
        if query.next():
            self.project_id = query.value(0)
        db.close()

        self.contract_ui = contract.Ui_Form()
        self.contract_ui.setupUi(self, self.contract_id, self.project_id)

        self.contract_ui.add_document_button.clicked.connect(self.add_document)
        self.contract_ui.pushButton_12.clicked.connect(self.edit_contract)
        self.contract_ui.pushButton_13.clicked.connect(self.edit_project)
        self.contract_ui.pushButton.clicked.connect(self.add_party)
        self.contract_ui.pushButton_2.clicked.connect(self.edit_party)
        self.contract_ui.pushButton_3.clicked.connect(self.delete_party)
        self.contract_ui.delete_document_button.clicked.connect(self.delete_document)
        self.contract_ui.open_document_button.clicked.connect(self.open_document)
        self.contract_ui.pushButton_6.clicked.connect(self.delete_task)
        self.contract_ui.save.clicked.connect(self.save_changes)

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
        if name == '':
            return
        dir = self.dir + name

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
        self.new_document_signal.emit()

    def open_document(self):
        if self.contract_ui.documents_list.selectedIndexes() == []:
            return
        else:
            name_index = self.contract_ui.documents_list.selectedIndexes()[0]
            name = self.contract_ui.documents_list.model().itemData(name_index)[0]
            filename = self.dir + name
            os.startfile(filename)

    def delete_document(self):
        if self.contract_ui.documents_list.selectedIndexes() == []:
            return
        else:
            name_index = self.contract_ui.documents_list.selectedIndexes()[0]
            name = self.contract_ui.documents_list.model().itemData(name_index)[0]
            prompt = 'Are you sure you want to delete ' + name + '?'
            buttonReply = QMessageBox.question(self, 'Delete Document', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM documents WHERE document=? AND contract_id=?', (name, self.contract_id))
                path = self.dir + name
                os.remove(path)
                self.delete_document_signal.emit()

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
        self.new_party_signal.emit()

    def edit_party(self):
        if self.contract_ui.parties_tree.selectedIndexes() == []:
            return
        else:
            name_index = self.contract_ui.parties_tree.selectedIndexes()[0]
            name = name_index.model().itemData(name_index)[0]
            first_index = self.contract_ui.parties_tree.selectedIndexes()[1]
            first = first_index.model().itemData(first_index)[0]
            last_index = self.contract_ui.parties_tree.selectedIndexes()[2]
            last = last_index.model().itemData(last_index)[0]
            phone_index = self.contract_ui.parties_tree.selectedIndexes()[3]
            phone = phone_index.model().itemData(phone_index)[0]
            email_index = self.contract_ui.parties_tree.selectedIndexes()[4]
            email = email_index.model().itemData(email_index)[0]
            self.edit_party_signal.emit(str(name), str(first), str(last), str(phone), str(email))

    def delete_party(self):
        if self.contract_ui.parties_tree.selectedIndexes() == []:
            return
        else:
            name_index = self.contract_ui.parties_tree.selectedIndexes()[0]
            name = name_index.model().itemData(name_index)[0]
            self.delete_party_signal.emit(str(name), self.project_id)

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
        if self.contract_ui.tasks_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.contract_ui.tasks_tree.selectedIndexes()[5]
            task_id = id_index.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete this task?'
            buttonReply = QMessageBox.question(self, 'Delete Task', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM tasks WHERE id=?', (task_id,))
                self.delete_task_signal.emit()

    def save_changes(self):
        prompt = 'Save Changes?'
        buttonReply = QMessageBox.question(self, 'Save Changes', prompt,
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        notes = self.contract_ui.textEdit.toPlainText()
        if buttonReply == QMessageBox.Yes:
            self.run_query('UPDATE contracts SET notes=? WHERE id=?', (notes, self.contract_id))

    def update_parties_tree(self):
        self.contract_ui.refresh_parties_tree()

    def update_document_list(self):
        self.contract_ui.refresh_document_list()

    def update_tasks_tree(self):
        self.contract_ui.refresh_tasks_tree()

class PartyWindow(QtWidgets.QWidget, party.Ui_partyDialog):
    party_changed = QtCore.pyqtSignal()

    def __init__(self, project_name, name='', first='', last='', phone='', email='', update=False):
        QtWidgets.QWidget.__init__(self)
        self.project_name = project_name
        self.name = name
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.update = update

        # Project ID:
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT id FROM projects where name=?")
        query.addBindValue(self.project_name)
        query.exec_()
        if query.next():
            self.project_id = query.value(0)
        db.close()

        # Party ID:
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Contracts.db')
        if not db.open():
            print('Db not open')
        query = QtSql.QSqlQuery()
        query.prepare("SELECT id FROM parties where name=?")
        query.addBindValue(self.name)
        query.exec_()
        if query.next():
            self.party_id = query.value(0)
        db.close()

        self.party_ui = party.Ui_partyDialog()
        self.party_ui.setupUi(self, self.project_id, self.name, self.first, self.last, self.phone, self.email)

        self.party_ui.pushButton.clicked.connect(self.save_party)
        self.party_changed.connect(self.close)
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

        existing_parties = self.fetch_query('SELECT name FROM parties WHERE project_id=?', (self.project_id,))

        if name == '':
            buttonReply = QMessageBox.question(self, 'Empty Name','Name cannot be blank',
                                               QMessageBox.Ok)
        else:
            if self.update is True:
                if name == self.name:
                    self.run_query(
                        'Update parties SET name=?, representative_first=?, representative_last=?, phone=?, email=? WHERE '
                        'project_id=? AND id=?', (name, first, last, phone, email, self.project_id, self.party_id))
                    self.party_changed.emit()

                elif name in existing_parties:
                    prompt = name + ' already exists. Please choose another name'
                    buttonReply = QMessageBox.question(self, 'Name taken', prompt, QMessageBox.Ok)

                else:
                    self.run_query(
                        'Update parties SET name=?, representative_first=?, representative_last=?, phone=?, email=? WHERE '
                        'project_id=? AND id=?', (name, first, last, phone, email, self.project_id, self.party_id))
                    self.party_changed.emit()
            else:
                if name in existing_parties:
                    prompt = name + ' already exists. Please choose another name'
                    buttonReply = QMessageBox.question(self, 'Name taken', prompt, QMessageBox.Ok)

                else:
                    self.run_query(
                        'INSERT INTO parties (project_id, name, representative_first, representative_last, phone, '
                        'email) VALUES (?, ?, ?, ?, ?, ?)', (self.project_id, name, first, last, phone, email))
                    self.party_changed.emit()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = Main()
    Window.show()

    sys.exit(app.exec_())