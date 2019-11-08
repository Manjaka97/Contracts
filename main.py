from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import window


class Main(QtWidgets.QMainWindow, window.UiMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = window.UiMainWindow()
        self.ui.setup_ui(self)

        self.ui.new_button.clicked.connect(self.add_contract)
        self.ui.contracts_delete.clicked.connect(self.delete_contract)

    def add_contract(self):
        self.ui.contracts_list.addItem('Test')

    def delete_contract(self):
        row = self.ui.contracts_list.currentRow()
        item = self.ui.contracts_list.item(row)
        if item is None:
            return
        reply = QMessageBox.question(self, 'Delete Contract', 'Are you sure you want to delete {0}?'.format(
            str(item.text())), QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.ui.contracts_list.takeItem(row)
            del item


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = Main()
    Window.show()
    sys.exit(app.exec_())
