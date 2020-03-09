from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox
import ui
import sqlite3
import os

import webbrowser
from shutil import copyfile

class Main(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # Menu Buttons
        self.ui.dashboard_btn.clicked.connect(self.show_dashboard)
        self.ui.contracts_btn.clicked.connect(self.show_contracts)
        self.ui.people_btn.clicked.connect(self.show_people)
        self.ui.companies_btn.clicked.connect(self.show_companies)
        self.ui.reminders_btn.clicked.connect(self.show_reminders)
        self.ui.risks_btn.clicked.connect(self.show_risks)
        self.ui.todos_btn.clicked.connect(self.show_todos)
        self.ui.library_btn.clicked.connect(self.show_library)
        self.ui.reports_btn.clicked.connect(self.show_reports)
        self.ui.archive_btn.clicked.connect(self.show_archives)

        # New Buttons
        self.ui.new_contract.clicked.connect(self.new_contract)
        self.ui.new_person.clicked.connect(self.new_person)
        self.ui.new_company.clicked.connect(self.new_company)
        self.ui.new_reminder.clicked.connect(self.new_reminder)
        self.ui.new_risk.clicked.connect(self.new_risk)
        self.ui.new_todo.clicked.connect(self.new_todo)

        # Cancel Buttons
        self.ui.cancel_contract.clicked.connect(self.cancel_contract)
        self.ui.cancel_person.clicked.connect(self.cancel_person)
        self.ui.cancel_company.clicked.connect(self.cancel_company)
        self.ui.cancel_reminder.clicked.connect(self.cancel_reminder)
        self.ui.cancel_risk.clicked.connect(self.cancel_risk)
        self.ui.cancel_todo.clicked.connect(self.cancel_todo)

    def show_dashboard(self):
        self.ui.main_widget.setCurrentIndex(0)

    def show_contracts(self):
        self.ui.main_widget.setCurrentIndex(1)

    def new_contract(self):
        self.ui.main_widget.setCurrentIndex(2)

    def cancel_contract(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_contracts()

    def show_people(self):
        self.ui.main_widget.setCurrentIndex(3)

    def new_person(self):
        self.ui.main_widget.setCurrentIndex(4)

    def cancel_person(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_people()

    def show_companies(self):
        self.ui.main_widget.setCurrentIndex(5)

    def new_company(self):
        self.ui.main_widget.setCurrentIndex(6)

    def cancel_company(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_companies()

    def show_reminders(self):
        self.ui.main_widget.setCurrentIndex(7)

    def new_reminder(self):
        self.ui.main_widget.setCurrentIndex(8)

    def cancel_reminder(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_reminders()

    def show_risks(self):
        self.ui.main_widget.setCurrentIndex(9)

    def new_risk(self):
        self.ui.main_widget.setCurrentIndex(10)

    def cancel_risk(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_risks()

    def show_todos(self):
        self.ui.main_widget.setCurrentIndex(11)

    def new_todo(self):
        self.ui.main_widget.setCurrentIndex(12)

    def cancel_todo(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_todos()

    def show_library(self):
        self.ui.main_widget.setCurrentIndex(13)

    def show_reports(self):
        self.ui.main_widget.setCurrentIndex(14)

    def show_archives(self):
        self.ui.main_widget.setCurrentIndex(15)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = Main()
    Window.show()

    sys.exit(app.exec_())