from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import window, contracts
import sqlite3


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
            self.contract_window.show()

    # To be implemented later
    def show_new_contract_window(self):
        self.new_contract_window = ContractWindow()
        self.new_contract_window.show()

    def add_contract(self):
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


class ContractWindow(QtWidgets.QWidget, contracts.Ui_Form):
    def __init__(self, contract_name, project_name):
        QtWidgets.QWidget.__init__(self)
        self.contract_ui = contracts.Ui_Form()
        self.contract_ui.setupUi(self, contract_name, project_name)

        self.contract_ui.contract_label

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = Main()
    Window.show()
    sys.exit(app.exec_())