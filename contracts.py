from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
import ui, calendar, person
import sqlite3
import os
import re

import webbrowser
from shutil import copyfile

class Main(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.dir = os.path.dirname(os.path.realpath(__file__)) + "\\documents\\"

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

        # Save Buttons
        self.ui.save_contract.clicked.connect(self.save_contract)
        self.ui.save_person.clicked.connect(self.save_person)

        # Dates
        self.ui.contract_start_btn.clicked.connect(self.get_start)
        self.ui.contract_cancel_btn.clicked.connect(self.get_cancel)
        self.ui.contract_end_btn.clicked.connect(self.get_end)
        self.ui.contract_review_btn.clicked.connect(self.get_review)

        # Attachments
        self.ui.contract_add_attachment.clicked.connect(self.add_contract_attachment)
        self.ui.contract_open_attachment.clicked.connect(self.open_contract_attachment)
        self.ui.contract_delete_attachment.clicked.connect(self.delete_contract_attachment)

        # Parties
        self.ui.add_party.clicked.connect(self.party_window)
        self.ui.delete_party.clicked.connect(self.delete_party)

        # Edits
        self.ui.edit_contract_btn.clicked.connect(self.edit_contract)
        self.ui.edit_person_btn.clicked.connect(self.edit_person)

        # Deletes
        self.ui.delete_contract_btn.clicked.connect(self.delete_contract)
        self.ui.delete_person_btn.clicked.connect(self.delete_person)

        # Archives
        self.ui.archive_contract_btn.clicked.connect(self.archive_contract)
        self.ui.archive_person_btn.clicked.connect(self.archive_person)

        # Favorites
        self.ui.favorite_contract_btn.clicked.connect(self.favorite_contract)
        self.ui.favorite_person_btn.clicked.connect(self.favorite_person)

    # Sql Commands
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

    # Show
    def show_dashboard(self):
        self.ui.main_widget.setCurrentIndex(0)

    def show_contracts(self):
        self.ui.update_contracts()
        self.ui.main_widget.setCurrentIndex(1)

    def show_people(self):
        self.ui.update_people()
        self.ui.main_widget.setCurrentIndex(3)

    def show_companies(self):
        self.ui.main_widget.setCurrentIndex(5)

    def show_reminders(self):
        self.ui.main_widget.setCurrentIndex(7)

    def show_risks(self):
        self.ui.main_widget.setCurrentIndex(9)

    def show_todos(self):
        self.ui.main_widget.setCurrentIndex(11)

    def show_library(self):
        self.ui.main_widget.setCurrentIndex(13)

    def show_reports(self):
        self.ui.main_widget.setCurrentIndex(14)

    def show_archives(self):
        self.ui.main_widget.setCurrentIndex(15)

    # New
    def new_contract(self):
        self.ui.new_contract_window() # This clears all fields
        self.ui.main_widget.setCurrentIndex(2)

    def new_person(self):
        self.ui.new_person_window()
        self.ui.main_widget.setCurrentIndex(4)

    def new_company(self):
        self.ui.main_widget.setCurrentIndex(6)

    def new_reminder(self):
        self.ui.main_widget.setCurrentIndex(8)

    def new_risk(self):
        self.ui.main_widget.setCurrentIndex(10)

    def new_todo(self):
        self.ui.main_widget.setCurrentIndex(12)

    # Cancel
    def cancel_contract(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_contracts()

            # Remove attachments and parties if contract is cancelled
            docs = self.fetch_query("SELECT url FROM documents WHERE owner_id=?", (self.next_contract_id(),))
            for doc in docs:
                os.remove(doc)
            self.run_query("DELETE FROM documents WHERE owner_id=?", (self.next_contract_id(),))
            self.run_query("DELETE FROM people_contracts WHERE contract_id=?", (self.next_contract_id(),))

    def cancel_person(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_people()

    def cancel_company(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_companies()

    def cancel_reminder(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_reminders()

    def cancel_risk(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_risks()

    def cancel_todo(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_todos()

    # Save
    def save_contract(self):
        contract_id = self.ui.contract_id_lb.text()
        title = self.ui.contract_title.text()
        type = self.ui.contract_type.currentIndex()
        category = self.ui.contract_category.currentIndex()
        classification = self.ui.contract_classification.currentIndex()
        reference = self.ui.contract_reference.text()
        account = self.ui.contract_account.text()
        status = self.ui.contract_status.currentIndex()
        master = int(re.findall(r'\d+', self.ui.contract_master.currentText())[0])
        value = self.ui.contract_value.text()
        currency = self.ui.contract_currency.currentIndex()

        start = self.ui.contract_start.text()
        end = self.ui.contract_end.text()
        cancel = self.ui.contract_cancel.text()
        review = self.ui.contract_review.text()
        limit = self.ui.contract_extension.text()

        if self.ui.term_none.isChecked():
            term = 0
            start = ''
            end = ''
            cancel = ''
            review = ''
        elif self.ui.term_fixed.isChecked():
            term = 1
        # TODO: Add calculation for next recurrence
        elif self.ui.term_recurring.isChecked():
            term = 2
        elif self.ui.term_rolling.isChecked():
            term = 3
            end = ''

        description = self.ui.contract_description.toPlainText()

        if title == '':
            self.message = QMessageBox()
            self.message.setText('Title cannot be empty')
            self.message.show()
        else:
            if contract_id == '': # New contract
                self.run_query("INSERT INTO contracts (title, type_id, category_id, classification_id, reference, account_reference, status_id, master_contract_id, value, currency_id, term_id, start_date, end_date, review_date, cancel_date, extension_limit, description, date_created) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,strftime('%m/%d/%Y','now'))", (title,type,category,classification,reference,account,status,master,value,currency,term, start, end, review, cancel, limit,description))
            else: # Edit contract
                self.run_query("UPDATE contracts SET title=?, type_id=?, category_id=?, classification_id=?, reference=?, account_reference=?, status_id=?, master_contract_id=?, value=?, currency_id=?, term_id=?, start_date=?, end_date=?, review_date=?, cancel_date=?, extension_limit=?, description=? WHERE id=?", (title,type,category,classification,reference,account,status,master,value,currency,term, start, end, review, cancel, limit,description, contract_id))
            self.show_contracts()

    def save_person(self):
        person_id = self.ui.person_id_lb.text()
        salutation_id = self.ui.salutation.currentIndex()
        first = self.ui.first_name.text()
        last = self.ui.last_name.text()
        gender_id = self.ui.gender.currentIndex()
        job = self.ui.job.text()
        company_id = self.ui.company.currentIndex()
        type = self.ui.person_type.text()
        phone = self.ui.phone.text()
        mobile = self.ui.mobile.text()
        email = self.ui.email.text()
        fax = self.ui.fax.text()

        if first == '' and last == '':
            self.message = QMessageBox()
            self.message.setText('Name cannot be empty')
            self.message.show()
        else:
            if person_id == '': # New person
                self.run_query("INSERT INTO people (salutation_id, first, last, gender_id, job, company_id, type, phone, mobile, email, fax, date_created) VALUES(?,?,?,?,?,?,?,?,?,?,?,strftime('%m/%d/%Y','now'))", (salutation_id, first, last, gender_id, job, company_id, type, phone, mobile, email, fax))
            else: # Edit contract
                self.run_query("UPDATE people SET salutation_id=?, first=?, last=?, gender_id=?, job=?, company_id=?, type=?, phone=?, mobile=?, email=?, fax=? WHERE id=?", (salutation_id, first, last, gender_id, job, company_id, type, phone, mobile, email, fax, person_id))
            self.show_people()
    # Edit
    def edit_contract(self):
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.contracts_tree.selectedIndexes()[0]
            contract_id = self.ui.contracts_tree.model().itemData(id_index)[0]
            self.ui.edit_contract_window(contract_id)
            self.ui.main_widget.setCurrentIndex(2)

    def edit_person(self):
        if self.ui.people_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.people_tree.selectedIndexes()[0]
            person_id = self.ui.people_tree.model().itemData(id_index)[0]
            self.ui.edit_person_window(person_id)
            self.ui.main_widget.setCurrentIndex(4)
    
    # Delete
    def delete_contract(self):
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.contracts_tree.selectedIndexes()[0]
            contract_id = self.ui.contracts_tree.model().itemData(id_index)[0]
            title_index = self.ui.contracts_tree.selectedIndexes()[1]
            contract_title = self.ui.contracts_tree.model().itemData(title_index)[0]
            prompt = 'Are you sure you want to delete ' + contract_title + '?'
            buttonReply = QMessageBox.question(self, 'Delete Contract', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM contracts WHERE id=?', (contract_id,))
                self.ui.update_contracts()
    
    def delete_person(self):
        if self.ui.people_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.people_tree.selectedIndexes()[0]
            person_id = self.ui.people_tree.model().itemData(id_index)[0]
            first_index = self.ui.people_tree.selectedIndexes()[1]
            first = self.ui.people_tree.model().itemData(first_index)[0]
            last_index = self.ui.people_tree.selectedIndexes()[1]
            last = self.ui.people_tree.model().itemData(last_index)[0]
            prompt = 'Are you sure you want to delete' + first + ' ' + last + '?'
            buttonReply = QMessageBox.question(self, 'Archive person', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM people WHERE id=?', (person_id,))
                self.ui.update_people()
                
    # Archive
    def archive_contract(self):
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.contracts_tree.selectedIndexes()[0]
            contract_id = self.ui.contracts_tree.model().itemData(id_index)[0]
            title_index = self.ui.contracts_tree.selectedIndexes()[1]
            contract_title = self.ui.contracts_tree.model().itemData(title_index)[0]
            prompt = 'Are you sure you want to archive' + contract_title + '?'
            buttonReply = QMessageBox.question(self, 'Archive Contract', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('UPDATE contracts SET archived=1 WHERE id=?', (contract_id,))
                self.ui.update_contracts()
    
    def archive_person(self):
        if self.ui.people_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.people_tree.selectedIndexes()[0]
            person_id = self.ui.people_tree.model().itemData(id_index)[0]
            first_index = self.ui.people_tree.selectedIndexes()[1]
            first = self.ui.people_tree.model().itemData(first_index)[0]
            last_index = self.ui.people_tree.selectedIndexes()[1]
            last = self.ui.people_tree.model().itemData(last_index)[0]
            prompt = 'Are you sure you want to archive' + first + ' ' + last + '?'
            buttonReply = QMessageBox.question(self, 'Archive person', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('UPDATE people SET archived=1 WHERE id=?', (person_id,))
                self.ui.update_people()
    # Favorite
    def favorite_contract(self):
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.contracts_tree.selectedIndexes()[0]
            contract_id = self.ui.contracts_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM contracts WHERE id=?',(contract_id,))
            if fav_status == 0:
                self.run_query('UPDATE contracts SET favorite=1 WHERE id=?', (contract_id,))
            else:
                self.run_query('UPDATE contracts SET favorite=0 WHERE id=?', (contract_id,))
            self.message = QMessageBox()
            self.message.setText('(Un)marked as favorite')
            self.message.show()
            self.ui.update_contracts()

    def favorite_person(self):
        if self.ui.people_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.people_tree.selectedIndexes()[0]
            person_id = self.ui.people_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM people WHERE id=?',(person_id,))
            if fav_status == 0:
                self.run_query('UPDATE people SET favorite=1 WHERE id=?', (person_id,))
            else:
                self.run_query('UPDATE people SET favorite=0 WHERE id=?', (person_id,))
            self.message = QMessageBox()
            self.message.setText('(Un)marked as favorite')
            self.message.show()
            self.ui.update_people()
            
    # Dates
    def get_start(self):
        self.calendar_window = Calendar()
        self.calendar_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.calendar_window.select_signal.connect(self.set_start)
        self.calendar_window.show()

    def set_start(self, date):
        self.ui.contract_start.setText(date.toString('MM/dd/yyyy'))

    def get_end(self):
        self.calendar_window = Calendar()
        self.calendar_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.calendar_window.select_signal.connect(self.set_end)
        self.calendar_window.show()

    def set_end(self, date):
        self.ui.contract_end.setText(date.toString('MM/dd/yyyy'))

    def get_review(self):
        self.calendar_window = Calendar()
        self.calendar_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.calendar_window.select_signal.connect(self.set_review)
        self.calendar_window.show()

    def set_review(self, date):
        self.ui.contract_review.setText(date.toString('MM/dd/yyyy'))
        
    def get_cancel(self):
        self.calendar_window = Calendar()
        self.calendar_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.calendar_window.select_signal.connect(self.set_cancel)
        self.calendar_window.show()

    def set_cancel(self, date):
        self.ui.contract_cancel.setText(date.toString('MM/dd/yyyy'))

    # Attachments
    def add_contract_attachment(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Add File', '.')
        name = QtCore.QUrl.fromLocalFile(filename[0]).fileName()
        if name == '':
            return
        dir = self.dir + name
        copyfile(filename[0], dir)

        if self.ui.contract_id_lb.text() == "":
            contract_id = self.next_contract_id()
        else:
            contract_id = self.ui.contract_id_lb.text()
        # Insert into database
        try:
            sqliteConnection = sqlite3.connect('data.db')
            cursor = sqliteConnection.cursor()
            print('Connected to SQLite')
            query = """ INSERT INTO documents (name, url, type_id, date_created, owner_id) VALUES (?, ?, ?, strftime('%m/%d/%Y','now'), ?)"""
            record = (name, dir, 1, contract_id)
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

        if self.ui.contract_id_lb.text() == "":
            self.ui.update_contracts_attachments()
        else:
            self.ui.update_contracts_attachments(contract_id)

    def open_contract_attachment(self):
        if self.ui.contract_attachments.selectedIndexes() == []:
            return
        else:
            url_index = self.ui.contract_attachments.selectedIndexes()[2]
            url = self.ui.contract_attachments.model().itemData(url_index)[0]
            os.startfile(url)

    def delete_contract_attachment(self):
        if self.ui.contract_attachments.selectedIndexes() == []:
            return
        else:
            name_index = self.ui.contract_attachments.selectedIndexes()[1]
            name = self.ui.contract_attachments.model().itemData(name_index)[0]
            url_index = self.ui.contract_attachments.selectedIndexes()[2]
            url = self.ui.contract_attachments.model().itemData(url_index)[0]
            id_index = self.ui.contract_attachments.selectedIndexes()[0]
            id = self.ui.contract_attachments.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete ' + name + '?'
            buttonReply = QMessageBox.question(self, 'Delete Document', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                if self.ui.contract_id_lb.text() == "":
                    contract_id = self.next_contract_id()
                    self.run_query('DELETE FROM documents WHERE id=?', (id,))
                    os.remove(url)
                    self.ui.update_contracts_attachments()
                else:
                    contract_id = self.ui.contract_id_lb.text()
                    self.run_query('DELETE FROM documents WHERE id=?', (id,))
                    os.remove(url)
                    self.ui.update_contracts_attachments(contract_id)

    # Parties
    def party_window(self):
        self.party_window = PersonDialog()
        self.party_window.show()
        self.party_window.select_signal.connect(self.select_party)

    def select_party(self, person_id):
        if self.ui.contract_id_lb.text() == "":
            contract_id = self.next_contract_id()
            self.run_query(
                'INSERT INTO people_contracts(person_id,contract_id) SELECT ?, ? WHERE NOT EXISTS(SELECT 1 FROM people_contracts WHERE person_id = ? AND contract_id=?);',
                (person_id, contract_id, person_id, contract_id))
            self.ui.update_parties()

        else:
            contract_id = self.ui.contract_id_lb.text()
            self.run_query('INSERT INTO people_contracts(person_id,contract_id) SELECT ?, ? WHERE NOT EXISTS(SELECT 1 FROM people_contracts WHERE person_id = ? AND contract_id=?);',(person_id, contract_id, person_id, contract_id))
            self.ui.update_parties(contract_id)
        
    def delete_party(self):
        if self.ui.contract_parties.selectedIndexes() == []:
            return
        else:
            first_index = self.ui.contract_parties.selectedIndexes()[1]
            first = self.ui.contract_parties.model().itemData(first_index)[0]
            last_index = self.ui.contract_parties.selectedIndexes()[2]
            last = self.ui.contract_parties.model().itemData(last_index)[0]
            id_index = self.ui.contract_parties.selectedIndexes()[0]
            person_id = self.ui.contract_parties.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete ' + first + ' ' + last + '?'
            buttonReply = QMessageBox.question(self, 'Delete Party', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                if self.ui.contract_id_lb.text() == "":
                    contract_id = self.next_contract_id()
                    self.run_query('DELETE FROM people_contracts WHERE person_id=? AND contract_id=?', (person_id, contract_id))
                    self.ui.update_parties()
                else:
                    contract_id = self.ui.contract_id_lb.text()
                    self.run_query('DELETE FROM people_contracts WHERE person_id=? AND contract_id=?',
                                   (person_id, contract_id))
                    self.ui.update_parties(contract_id)

    # Next IDs
    def next_contract_id(self):
        next_id = self.fetch_query("SELECT seq FROM sqlite_sequence WHERE name='contracts'")[0] + 1
        return next_id

        
class Calendar(QtWidgets.QWidget, calendar.Ui_Form):
    select_signal = QtCore.pyqtSignal(QtCore.QDate)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.calendar_ui = calendar.Ui_Form()
        self.calendar_ui.setupUi(self)
        self.calendar_ui.select.clicked.connect(self.select)
        self.calendar_ui.cancel.clicked.connect(self.close)

    def select(self):
        self.select_signal.emit(self.calendar_ui.calendarWidget.selectedDate())
        self.close()


class PersonDialog(QtWidgets.QWidget, person.Ui_Form):
    select_signal = QtCore.pyqtSignal(int)
    new_signal = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.person_ui = person.Ui_Form()
        self.person_ui.setupUi(self)
        self.person_ui.select.clicked.connect(self.select)
        self.person_ui.new_2.clicked.connect(self.new_person)
        self.person_ui.cancel.clicked.connect(self.close)

    def select(self):
        if self.person_ui.comboBox.currentText() == '':
            return

        person_id = int(re.findall(r'\d+', self.person_ui.comboBox.currentText())[0])
        self.select_signal.emit(person_id)
        self.close()

    def new_person(self):
        self.new_signal.emit()
        self.close()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = Main()
    Window.show()

    sys.exit(app.exec_())