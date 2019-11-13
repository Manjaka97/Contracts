from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import window
import sqlite3


class Main(QtWidgets.QMainWindow, window.UiMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = window.UiMainWindow()
        self.ui.setup_ui(self)

        self.ui.new_button.clicked.connect(self.add_contract)
        self.ui.contracts_delete.clicked.connect(self.delete_contract)
        #self.ui.new_button.clicked.connect(self.show_new_contract_window)

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
        self.ui.contracts_list.addItem('Added item')

    def delete_contract(self):
        row = self.ui.contracts_list.currentRow()
        item = self.ui.contracts_list.item(row)
        if item is None:
            return
        reply = QMessageBox.question(self, 'Delete Contract', 'Are you sure you want to delete {0}?'.format(
            str(item.text())), QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.ui.contracts_list.takeItem(row)
            name = item.text()
            del item

            connection = sqlite3.connect('test.db')
            cursor = connection.cursor()
            name_query = (name,)
            #contract_id = connection.execute("SELECT id FROM contracts WHERE name = ? AND deleted = 0", (name,))
            cursor.execute('UPDATE contracts SET deleted=1 WHERE name=?', name_query)
            connection.commit()
            connection.close()


class ContractWindow(QtWidgets.QInputDialog):
    def __init__(self):
        super(ContractWindow, self).__init__()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = Main()
    Window.show()
    sys.exit(app.exec_())