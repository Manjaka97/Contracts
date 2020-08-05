from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from shutil import copyfile
import ui, calendarWidget, person
import sqlite3
import os
import re
import schedule, time
import threading

# TODO: Implementing search filters
# TODO: Exporting to csv based on filters
# TODO: Implementing Dashboard, Library, Reports and Archives

class Main(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    refresh_signal = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        # Using dir_ because dir is a reserved keyword
        # The line below does not work after freezing the app
        self.dir_ = os.path.dirname(os.path.realpath(__file__)) + "\\documents\\"
        if getattr(sys, 'frozen', False):
            # frozen
            self.dir_ = os.path.dirname(sys.executable) + "\\documents\\"
        else:
            # unfrozen
            dir_ = os.path.dirname(os.path.realpath(__file__))
        # if not os.path.exists(self.dir_):
        #     os.makedirs(self.dir_)

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

        # New Buttons
        self.ui.new_contract.clicked.connect(self.new_contract)
        self.ui.new_person.clicked.connect(self.new_person)
        self.ui.new_company.clicked.connect(self.new_company)
        self.ui.new_reminder.clicked.connect(self.new_reminder)
        self.ui.new_risk.clicked.connect(self.new_risk)
        self.ui.new_todo.clicked.connect(self.new_todo)
        self.ui.add_responsible.clicked.connect(self.add_responsible)

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
        self.ui.save_company.clicked.connect(self.save_company)
        self.ui.save_reminder.clicked.connect(self.save_reminder)
        self.ui.save_risk.clicked.connect(self.save_risk)
        self.ui.save_todo.clicked.connect(self.save_todo)

        # Dates
        self.ui.contract_start_btn.clicked.connect(self.get_start)
        self.ui.contract_cancel_btn.clicked.connect(self.get_cancel)
        self.ui.contract_end_btn.clicked.connect(self.get_end)
        self.ui.contract_review_btn.clicked.connect(self.get_review)
        self.ui.specific_date_btn.clicked.connect(self.get_specific)
        self.ui.recur_until_btn.clicked.connect(self.get_until_specific)
        self.ui.risk_end_btn.clicked.connect(self.get_risk_end)
        self.ui.todo_start_btn.clicked.connect(self.get_todo_start)
        self.ui.todo_resolution_btn.clicked.connect(self.get_todo_end)

        # Attachments
        self.ui.contract_add_attachment.clicked.connect(self.add_contract_attachment)
        self.ui.contract_open_attachment.clicked.connect(self.open_contract_attachment)
        self.ui.contract_delete_attachment.clicked.connect(self.delete_contract_attachment)
        self.ui.reminder_add_attachment.clicked.connect(self.add_reminder_attachment)
        self.ui.reminder_open_attachment.clicked.connect(self.open_reminder_attachment)
        self.ui.reminder_delete_attachment.clicked.connect(self.delete_reminder_attachment)
        self.ui.risk_add_attachment_3.clicked.connect(self.add_risk_attachment)
        self.ui.risk_open_attachment_3.clicked.connect(self.open_risk_attachment)
        self.ui.risk_delete_attachment_3.clicked.connect(self.delete_risk_attachment)

        # Parties
        self.ui.add_party.clicked.connect(self.party_window)
        self.ui.delete_party.clicked.connect(self.delete_party)
        self.ui.reminder_add_party.clicked.connect(self.reminder_person_window)
        self.ui.reminder_delete_party.clicked.connect(self.delete_reminder_person)

        # Edits
        self.ui.edit_contract_btn.clicked.connect(self.edit_contract)
        self.ui.edit_person_btn.clicked.connect(self.edit_person)
        self.ui.open_party.clicked.connect(self.edit_person_from_contract)
        self.ui.edit_company_btn.clicked.connect(self.edit_company)
        self.ui.edit_reminder_btn.clicked.connect(self.edit_reminder)
        self.ui.reminder_open_party.clicked.connect(self.edit_person_from_reminder)
        self.ui.edit_risk_btn.clicked.connect(self.edit_risk)
        self.ui.edit_todo_btn.clicked.connect(self.edit_todo)

        # Deletes
        self.ui.delete_contract_btn.clicked.connect(self.delete_contract)
        self.ui.delete_person_btn.clicked.connect(self.delete_person)
        self.ui.delete_company_btn.clicked.connect(self.delete_company)
        self.ui.delete_reminder_btn.clicked.connect(self.delete_reminder)
        self.ui.delete_risk_btn.clicked.connect(self.delete_risk)
        self.ui.delete_todo_btn.clicked.connect(self.delete_todo)

        # Archives
        self.ui.archive_contract_btn.clicked.connect(self.archive_contract)
        self.ui.archive_person_btn.clicked.connect(self.archive_person)
        self.ui.archive_company_btn.clicked.connect(self.archive_company)
        self.ui.archive_reminder_btn.clicked.connect(self.archive_reminder)
        self.ui.archive_risk_btn.clicked.connect(self.archive_risk)
        self.ui.archive_todo_btn.clicked.connect(self.archive_todo)

        # Favorites
        self.ui.favorite_contract_btn.clicked.connect(self.favorite_contract)
        self.ui.favorite_person_btn.clicked.connect(self.favorite_person)
        self.ui.favorite_company_btn.clicked.connect(self.favorite_company)
        self.ui.favorite_risk_btn.clicked.connect(self.favorite_risk)
        self.ui.favorite_todo_btn.clicked.connect(self.favorite_todo)

        self.ui.complete_reminder_btn.clicked.connect(self.complete_reminder)
        self.ui.uncomplete_reminder_btn.clicked.connect(self.uncomplete_reminder)
        self.ui.snooze_reminder_btn.clicked.connect(self.snooze_reminder)

        # Dropdown filters
        self.ui.contract_type_menu.currentIndexChanged.connect(self.show_contracts)
        self.ui.people_type_menu.currentIndexChanged.connect(self.show_people)
        self.ui.company_type_menu.currentIndexChanged.connect(self.show_companies)
        self.ui.reminder_type_menu.currentIndexChanged.connect(self.show_reminders)
        self.ui.risk_type_menu.currentIndexChanged.connect(self.show_risks)
        self.ui.todos_type_menu.currentIndexChanged.connect(self.show_todos)

        # Search Bars
        self.ui.contract_id_search.textChanged.connect(self.search_contract)
        self.ui.contract_title_search.textChanged.connect(self.search_contract)
        self.ui.contract_type_search.textChanged.connect(self.search_contract)
        self.ui.contract_classificatiion_type.textChanged.connect(self.search_contract)
        # TODO: Fix search dates
       # self.ui.contract_start_type.textChanged.connect(self.search_contract)
       # self.ui.contract_end_search.textChanged.connect(self.search_contract)
        self.ui.contract_value_search.textChanged.connect(self.search_contract)
        self.ui.contract_status_menu.currentIndexChanged.connect(self.search_contract)

        # Refresh
        self.refresh_signal.connect(self.ui.update_reminders_dates)
        self.refresh_signal.connect(self.ui.update_status)

        # Updates everytime app is launched
        self.ui.update_reminders_dates()
        self.ui.update_status()

    # Searches
    def search_contract(self):
        self.ui.search_contract()

    # Simple date validation method
    def is_valid(self, date_text):
        try:
            datetime.strptime(date_text, '%m/%d/%Y')
            return True
        except ValueError:
            return False

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
        self.remove_unsaved()
        self.restore_unsaved()
        self.ui.main_widget.setCurrentIndex(0)

    def show_contracts(self):
        self.remove_unsaved()
        self.restore_unsaved()
        self.ui.update_contracts()
        self.ui.main_widget.setCurrentIndex(1)

    def show_people(self):
        self.remove_unsaved()
        self.restore_unsaved()
        self.ui.update_people()
        self.ui.main_widget.setCurrentIndex(3)

    def show_companies(self):
        self.remove_unsaved()
        self.restore_unsaved()
        self.ui.update_companies()
        self.ui.main_widget.setCurrentIndex(5)

    def show_reminders(self):
        self.remove_unsaved()
        self.restore_unsaved()
        self.ui.update_reminders()
        self.ui.main_widget.setCurrentIndex(7)

    def show_risks(self):
        self.remove_unsaved()
        self.restore_unsaved()
        self.ui.update_risks()
        self.ui.main_widget.setCurrentIndex(9)

    def show_todos(self):
        self.remove_unsaved()
        self.restore_unsaved()
        self.ui.update_todos()
        self.ui.main_widget.setCurrentIndex(11)

    def show_library(self):
        self.remove_unsaved()
        self.restore_unsaved()
        self.ui.main_widget.setCurrentIndex(13)

    def show_reports(self):
        self.remove_unsaved()
        self.restore_unsaved()
        self.ui.main_widget.setCurrentIndex(14)

    def show_archives(self):
        self.remove_unsaved()
        self.restore_unsaved()
        self.ui.main_widget.setCurrentIndex(15)

    # New
    def new_contract(self):
        self.ui.new_contract_window() # This clears all fields
        self.ui.main_widget.setCurrentIndex(2)

    def new_person(self):
        self.ui.new_person_window()
        self.ui.main_widget.setCurrentIndex(4)

    def new_company(self):
        self.ui.new_company_window()
        self.ui.main_widget.setCurrentIndex(6)

    def new_reminder(self):
        self.ui.new_reminder_window()
        self.ui.main_widget.setCurrentIndex(8)

    def new_risk(self):
        self.ui.new_risk_window()
        self.ui.main_widget.setCurrentIndex(10)

    def new_todo(self):
        self.ui.new_todo_window()
        self.ui.main_widget.setCurrentIndex(12)

    # Cancel
    def cancel_contract(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.remove_unsaved()
            self.restore_unsaved()
            self.show_contracts()

    def cancel_person(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.remove_unsaved()
            self.restore_unsaved()
            self.show_people()

    def cancel_company(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.remove_unsaved()
            self.restore_unsaved()
            self.show_companies()

    def cancel_reminder(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.remove_unsaved()
            self.restore_unsaved()
            self.show_reminders()

    def cancel_risk(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.remove_unsaved()
            self.restore_unsaved()
            self.show_risks()

    def cancel_todo(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.remove_unsaved()
            self.restore_unsaved()
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

        for date in [start, end, cancel, review]:
            if date != '' and self.is_valid(date) is False:
                self.message = QMessageBox()
                self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
                self.message.setWindowTitle('Contracts')
                self.message.setText('Please make sure all dates are in MM/DD/YYYY format')
                self.message.show()
                return

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
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Title cannot be empty')
            self.message.show()

        else:
            if contract_id == '': # New contract
                contract_id = self.next_contract_id()
                self.run_query("INSERT INTO contracts (title, type_id, category_id, classification_id, reference, account_reference, status_id, master_contract_id, value, currency_id, term_id, start_date, end_date, review_date, cancel_date, extension_limit, description, date_created) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,strftime('%m/%d/%Y','now'))", (title,type,category,classification,reference,account,status,master,value,currency,term, start, end, review, cancel, limit,description))
                self.run_query("UPDATE documents SET temp=0 WHERE type_id=1 AND owner_id=? ", (contract_id,))
                self.run_query("UPDATE people_contracts SET temp=0 WHERE contract_id=?", (contract_id,))
            else: # Edit contract
                self.run_query("UPDATE contracts SET title=?, type_id=?, category_id=?, classification_id=?, reference=?, account_reference=?, status_id=?, master_contract_id=?, value=?, currency_id=?, term_id=?, start_date=?, end_date=?, review_date=?, cancel_date=?, extension_limit=?, description=? WHERE id=?", (title,type,category,classification,reference,account,status,master,value,currency,term, start, end, review, cancel, limit,description, contract_id))
                self.run_query("UPDATE documents SET temp=0 WHERE type_id=1 AND owner_id=? ", (contract_id,))
                self.run_query("UPDATE people_contracts SET temp=0 WHERE contract_id=?", (contract_id,))
            self.confirm_delete()
            self.show_contracts()
        if status == 0:
            print('Status updated')
            self.ui.update_status()

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
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Name cannot be empty')
            self.message.show()
        else:
            if person_id == '': # New person
                self.run_query("INSERT INTO people (salutation_id, first, last, gender_id, job, company_id, type, phone, mobile, email, fax, date_created) VALUES(?,?,?,?,?,?,?,?,?,?,?,strftime('%m/%d/%Y','now'))", (salutation_id, first, last, gender_id, job, company_id, type, phone, mobile, email, fax))
            else: # Edit contract
                self.run_query("UPDATE people SET salutation_id=?, first=?, last=?, gender_id=?, job=?, company_id=?, type=?, phone=?, mobile=?, email=?, fax=? WHERE id=?", (salutation_id, first, last, gender_id, job, company_id, type, phone, mobile, email, fax, person_id))
            self.show_people()

    def save_company(self):
        company_id = self.ui.company_id_lb.text()
        name = self.ui.company_name.text()
        type_id = self.ui.company_type.currentIndex()
        address1 = self.ui.address_1.text()
        address2 = self.ui.address_2.text()
        city = self.ui.city.text()
        state = self.ui.state.text()
        zip = self.ui.zip.text()
        country = self.ui.country.text()
        segment_id = self.ui.segment.currentIndex()
        number = self.ui.company_number.text()
        website = self.ui.website.text()
        email = self.ui.company_email.text()
        phone = self.ui.contact.text()
        fax = self.ui.company_fax.text()

        if name == '':
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Name cannot be empty')
            self.message.show()
        else:
            if company_id == '': # New company
                self.run_query("INSERT INTO companies (name, type_id, address1, address2, city, state, zip, country, segment_id, number, website, email, phone, fax, date_created) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,strftime('%m/%d/%Y','now'))", (name, type_id, address1, address2, city, state, zip, country, segment_id, number, website, email, phone, fax))
            else: # Edit company
                self.run_query("UPDATE companies SET name=?, type_id=?, address1=?, address2=?, city=?, state=?, zip=?, country=?, segment_id=?, number=?, website=?, email=?, phone=?, fax=? WHERE id=?", (name, type_id, address1, address2, city, state, zip, country, segment_id, number, website, email, phone, fax, company_id))
            self.show_companies()

    def save_reminder(self):
        reminder_id = self.ui.reminder_id_lb.text()
        name = self.ui.reminder_name.text()
        contract_id = int(re.findall(r'\d+', self.ui.reminder_contract.currentText())[0])
        company_id = int(re.findall(r'\d+', self.ui.reminder_company.currentText())[0])
        description = self.ui.reminder_description.toPlainText()
        complete = int(self.ui.reminder_complete.isChecked())
        snoozed = int(self.ui.reminder_snoozed.isChecked())
        specific_radio = int(self.ui.specific_date_radio.isChecked())
        relative_radio = int(self.ui.relative_date_radio.isChecked())
        do_not_recur_radio = int(self.ui.do_not_recur_radio.isChecked())
        recur_radio = int(self.ui.recur_radio.isChecked())
        until_specific_radio = int(self.ui.recur_until_specific.isChecked())
        until_key_radio = int(self.ui.until_key_date_radio.isChecked())
        indefinitely_radio = int(self.ui.recur_indefinitely_radio.isChecked())
        specific_date = self.ui.reminder_specific_date.text()
        relative_date = self.ui.reminder_relative_date.text()
        time_id = self.ui.time_type.currentIndex()
        before_after = self.ui.before.currentIndex()
        date_id = self.ui.key_date.currentIndex()
        recur_id = self.ui.recur_type.currentIndex()
        until_date = self.ui.recur_until_specific_2.text()
        until_key_id = self.ui.until_key_date.currentIndex()

        # Data Validation
        if self.ui.specific_date_radio.isChecked():
            relative_date = ''
        else:
            specific_date = ''

        if self.ui.do_not_recur_radio.isChecked():
            until_date = ''
        else:
            if self.ui.until_key_date_radio.isChecked() or self.ui.recur_indefinitely_radio.isChecked():
                until_date = ''

        for date in [specific_date, until_date]:
            if date != '' and self.is_valid(date) is False:
                self.message = QMessageBox()
                self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
                self.message.setWindowTitle('Contracts')
                self.message.setText('Please make sure all dates are in MM/DD/YYYY format')
                self.message.show()
                return

        if name == '':
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Name cannot be empty')
            self.message.show()
            return

        if self.ui.specific_date_radio.isChecked() and specific_date == '':
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Please provide a reminder date')
            self.message.show()
            return

        if self.ui.relative_date_radio.isChecked() and relative_date == '':
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Please provide a reminder date')
            self.message.show()
            return

        if self.ui.recur_radio.isChecked():
            if self.ui.recur_until_specific.isChecked() and until_date == '':
                self.message = QMessageBox()
                self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
                self.message.setWindowTitle('Contracts')
                self.message.setText('Please provide a reminder date')
                self.message.show()
                return

        if self.ui.recur_radio.isChecked():
            if self.ui.recur_until_specific.isChecked() and until_date == 'None':
                self.message = QMessageBox()
                self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
                self.message.setWindowTitle('Contracts')
                self.message.setText('Please provide a reminder date')
                self.message.show()
                return

        if self.ui.relative_date_radio.isChecked() and contract_id == 0:
                self.message = QMessageBox()
                self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
                self.message.setWindowTitle('Contracts')
                self.message.setText('Please select a contract to get a reminder date')
                self.message.show()
                return

        if not self.ui.do_not_recur_radio.isChecked() and self.ui.until_key_date_radio.isChecked() and contract_id == 0:
                self.message = QMessageBox()
                self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
                self.message.setWindowTitle('Contracts')
                self.message.setText("Please select a contract or check ''Do not recur''")
                self.message.show()
                return

        if self.ui.recur_radio.isChecked() and not self.ui.recur_until_specific.isChecked() and not self.ui.until_key_date_radio.isChecked() and not self.ui.recur_indefinitely_radio.isChecked():
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Please choose a recurrence type')
            self.message.show()
            return

        # Calculation for Deadline if relative date:
        if self.ui.specific_date_radio.isChecked():
            deadline = specific_date
            deadline_object = datetime.strptime(deadline, '%m/%d/%Y')

        else:
            if date_id == 0:
                reference_date = self.fetch_query('SELECT start_date FROM contracts WHERE id=?', (contract_id,))
            if date_id == 1:
                reference_date = self.fetch_query('SELECT end_date FROM contracts WHERE id=?', (contract_id,))
            if date_id == 2:
                reference_date = self.fetch_query('SELECT review_date FROM contracts WHERE id=?', (contract_id,))
            if date_id == 3:
                reference_date = self.fetch_query('SELECT cancel_date FROM contracts WHERE id=?', (contract_id,))

            if reference_date == []:
                self.message = QMessageBox()
                self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
                self.message.setWindowTitle('Contracts')
                self.message.setText('That contract does not have the Key date you selected. Please review your contract dates first.')
                self.message.show()
                return
            else:
                reference_date_object = datetime.strptime(reference_date[0], '%m/%d/%Y')

            if before_after == 0:
                if time_id == 0:
                    deadline_object = reference_date_object - timedelta(days=int(relative_date))
                if time_id == 1:
                    deadline_object = reference_date_object - timedelta(weeks=int(relative_date))
                if time_id == 2:
                    deadline_object = reference_date_object - relativedelta(months=int(relative_date))
                if time_id == 3:
                    deadline_object = reference_date_object - relativedelta(years=int(relative_date))
            else:
                if time_id == 0:
                    deadline_object = reference_date_object + timedelta(days=int(relative_date))
                if time_id == 1:
                    deadline_object = reference_date_object + timedelta(weeks=int(relative_date))
                if time_id == 2:
                    deadline_object = reference_date_object + relativedelta(months=int(relative_date))
                if time_id == 3:
                    deadline_object = reference_date_object + relativedelta(years=int(relative_date))
            deadline = deadline_object.strftime('%m/%d/%Y')

        # Calculation for last recurrence
        if self.ui.do_not_recur_radio.isChecked():
            last_recurrence = ''

        else:
            if self.ui.recur_until_specific.isChecked():
                last_recurrence = self.ui.recur_until_specific_2.text()

            elif self.ui.until_key_date_radio.isChecked():
                if self.ui.until_key_date.currentIndex() == 0:
                    last_recurrence = self.fetch_query("SELECT start_date FROM contracts WHERE id=?", (contract_id,))[0]
                elif self.ui.until_key_date.currentIndex() == 1:
                    last_recurrence = self.fetch_query("SELECT end_date FROM contracts WHERE id=?", (contract_id,))[0]
                elif self.ui.until_key_date.currentIndex() == 2:
                    last_recurrence = self.fetch_query("SELECT cancel_date FROM contracts WHERE id=?", (contract_id,))[0]
                else:
                    last_recurrence = self.fetch_query("SELECT cancel_date FROM contracts WHERE id=?", (contract_id,))[0]
            else:
                last_recurrence = ''
        # Saving or Updating
        if reminder_id == '': # New reminder
            reminder_id = self.next_reminder_id()
            self.run_query("INSERT INTO reminders (name, contract_id, company_id, description, complete, snoozed, "
                           "specific_radio, relative_radio, do_not_recur_radio, recur_radio, "
                           "until_specific_radio, until_key_radio, indefinitely_radio, specific_date, "
                           "relative_date, time_id, before_after, date_id, recur_id, until_date, until_key_id, deadline, last_recurrence, date_created) "
                           "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,strftime('%m/%d/%Y','now'))", (name, contract_id, company_id, description,
                                                                   complete, snoozed, specific_radio,
                                                                   relative_radio, do_not_recur_radio,
                                                                   recur_radio, until_specific_radio,
                                                                   until_key_radio, indefinitely_radio,
                                                                   specific_date, relative_date, time_id, before_after,
                                                                   date_id, recur_id, until_date, until_key_id, deadline, last_recurrence))
            self.run_query("UPDATE documents SET temp=0 WHERE type_id=2 AND owner_id=? ", (reminder_id,))
            self.run_query("UPDATE people_reminders SET temp=0 WHERE reminder_id=?", (reminder_id,))
        else: # Edit reminder
            self.run_query("UPDATE reminders SET name=?, contract_id=?, company_id=?, description=?, complete=?, snoozed=?, "
                           "specific_radio=?, relative_radio=?, do_not_recur_radio=?, recur_radio=?, "
                           "until_specific_radio=?, until_key_radio=?, indefinitely_radio=?, specific_date=?, "
                           "relative_date=?, time_id=?, before_after=?, date_id=?, recur_id=?, until_date=?, until_key_id=?, deadline=?, last_recurrence=? WHERE id=?",
                           (name, contract_id, company_id, description,
                            complete, snoozed, specific_radio,
                            relative_radio, do_not_recur_radio,
                            recur_radio, until_specific_radio,
                            until_key_radio, indefinitely_radio,
                            specific_date, relative_date, time_id, before_after,
                            date_id, recur_id, until_date, until_key_id, deadline, last_recurrence, reminder_id))
            self.run_query("UPDATE documents SET temp=0 WHERE type_id=2 AND owner_id=? ", (reminder_id,))
            self.run_query("UPDATE people_reminders SET temp=0 WHERE reminder_id=?", (reminder_id,))
        self.confirm_delete()
        self.show_reminders()

    def save_risk(self):
        risk_id = self.ui.risk_id_lb.text()
        name = self.ui.risk_name.text()
        contract_id = int(re.findall(r'\d+', self.ui.risk_contract.currentText())[0])
        probability_id = self.ui.risk_probability.currentIndex()
        impact_id = self.ui.risk_impact.currentIndex()
        type_id = self.ui.risk_type.currentIndex()
        end_date = self.ui.risk_end.text()
        notes = self.ui.risk_notes.toPlainText()
        mitigation = self.ui.risk_mitigation.toPlainText()

        if end_date != '' and self.is_valid(end_date) is False:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Please make sure all dates are in MM/DD/YYYY format')
            self.message.show()
            return

        if name == '':
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Name cannot be empty')
            self.message.show()
        else:
            if risk_id == '': # New risk
                risk_id = self.next_risk_id()
                self.run_query("INSERT INTO risks (name, contract_id, probability_id, impact_id, type_id, end_date, notes, mitigation, date_created) VALUES(?,?,?,?,?,?,?,?,strftime('%m/%d/%Y','now'))", (name, contract_id, probability_id, impact_id, type_id, end_date, notes, mitigation))
                self.run_query("UPDATE documents SET temp=0 WHERE type_id=3 AND owner_id=? ", (risk_id,))
            else: # Edit contract
                self.run_query("UPDATE risks SET name=?, contract_id=?, probability_id=?, impact_id=?, type_id=?, end_date=?, notes=?, mitigation=? WHERE id=?", (name, contract_id, probability_id, impact_id, type_id, end_date, notes, mitigation, risk_id))
                self.run_query("UPDATE documents SET temp=0 WHERE type_id=3 AND owner_id=? ", (risk_id,))
            self.confirm_delete()
            self.show_risks()

    def save_todo(self):
        todo_id = self.ui.todo_id_lb.text()
        subject = self.ui.todo_subject.text()
        status_id = self.ui.todo_status.currentIndex()
        if int(self.ui.todo_responsible.currentIndex() ) < 0:
            responsible_id = 0
        else:
            responsible_id = int(re.findall(r'\d+', self.ui.todo_responsible.currentText())[0])
        start_date = self.ui.todo_start_date.text()
        deadline = self.ui.todo_resolutio_date.text()
        priority_id = self.ui.todo_priority.currentIndex()
        severity_id = self.ui.todo_severity.currentIndex()
        contract_id = int(re.findall(r'\d+', self.ui.todo_contract.currentText())[0])
        company_id = int(re.findall(r'\d+', self.ui.todo_company.currentText())[0])
        description = self.ui.todo_description.toPlainText()

        for date in [start_date, deadline]:
            if date != '' and self.is_valid(date) is False:
                self.message = QMessageBox()
                self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
                self.message.setWindowTitle('Contracts')
                self.message.setText('Please make sure all dates are in MM/DD/YYYY format')
                self.message.show()
                return

        if subject == '':
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Subject cannot be empty')
            self.message.show()
        elif responsible_id == 0:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            self.message.setText('Please assign the todo to someone')
            self.message.show()
        else:
            if todo_id == '': # New to do
                self.run_query("INSERT INTO todos (subject, status_id, responsible_id, start_date, deadline, priority_id, severity_id, contract_id, company_id, description, date_created) VALUES(?,?,?,?,?,?,?,?,?,?,strftime('%m/%d/%Y','now'))", (subject, status_id, responsible_id, start_date, deadline, priority_id, severity_id, contract_id, company_id, description))
            else: # Edit contract
                self.run_query("UPDATE todos SET subject=?, status_id=?, responsible_id=?, start_date=?, deadline=?, priority_id=?, severity_id=?, contract_id=?, company_id=?, description=? WHERE id=?", (subject, status_id, responsible_id, start_date, deadline, priority_id, severity_id, contract_id, company_id, description, todo_id))
            self.show_todos()

    # Edit
    def edit_contract(self):
        self.remove_unsaved()
        self.restore_unsaved()
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.contracts_tree.selectedIndexes()[0]
            contract_id = self.ui.contracts_tree.model().itemData(id_index)[0]
            self.ui.edit_contract_window(contract_id)
            self.ui.main_widget.setCurrentIndex(2)

    def edit_person(self):
        self.remove_unsaved()
        self.restore_unsaved()
        if self.ui.people_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.people_tree.selectedIndexes()[0]
            person_id = self.ui.people_tree.model().itemData(id_index)[0]
            self.ui.edit_person_window(person_id)
            self.ui.main_widget.setCurrentIndex(4)

    def edit_person_from_contract(self):
        self.remove_unsaved()
        self.restore_unsaved()
        if self.ui.contract_parties.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.contract_parties.selectedIndexes()[0]
            person_id = self.ui.contract_parties.model().itemData(id_index)[0]
            self.ui.edit_person_window(person_id)
            self.ui.main_widget.setCurrentIndex(4)

    def edit_company(self):
        self.remove_unsaved()
        self.restore_unsaved()
        if self.ui.companies_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.companies_tree.selectedIndexes()[0]
            company_id = self.ui.companies_tree.model().itemData(id_index)[0]
            self.ui.edit_company_window(company_id)
            self.ui.main_widget.setCurrentIndex(6)

    def edit_reminder(self):
        self.remove_unsaved()
        self.restore_unsaved()
        if self.ui.reminders_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.reminders_tree.selectedIndexes()[0]
            reminder_id = self.ui.reminders_tree.model().itemData(id_index)[0]
            self.ui.edit_reminder_window(reminder_id)
            self.ui.main_widget.setCurrentIndex(8)

    def edit_person_from_reminder(self):
        self.remove_unsaved()
        self.restore_unsaved()
        if self.ui.reminder_people.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.reminder_people.selectedIndexes()[0]
            person_id = self.ui.reminder_people.model().itemData(id_index)[0]
            self.ui.edit_person_window(person_id)
            self.ui.main_widget.setCurrentIndex(4)

    def edit_risk(self):
        self.remove_unsaved()
        self.restore_unsaved()
        if self.ui.risks_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.risks_tree.selectedIndexes()[0]
            risk_id = self.ui.risks_tree.model().itemData(id_index)[0]
            self.ui.edit_risk_window(risk_id)
            self.ui.main_widget.setCurrentIndex(10)

    def edit_todo(self):
        self.remove_unsaved()
        self.restore_unsaved()
        if self.ui.todos_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.todos_tree.selectedIndexes()[0]
            todo_id = self.ui.todos_tree.model().itemData(id_index)[0]
            self.ui.edit_todo_window(todo_id)
            self.ui.main_widget.setCurrentIndex(12)

    # Delete
    def delete_contract(self, contract_id=None):
        # Calling this method from button clicked signals defaults contract_id to False
        if contract_id is False:
            if self.ui.contracts_tree.selectedIndexes() == []:
                return
            else:
                id_index = self.ui.contracts_tree.selectedIndexes()[0]
                contract_id = self.ui.contracts_tree.model().itemData(id_index)[0]
                title_index = self.ui.contracts_tree.selectedIndexes()[1]
                contract_title = self.ui.contracts_tree.model().itemData(title_index)[0]
                prompt = 'Are you sure you want to delete ' + contract_title + '?\nAll reminders, risks and to-dos associated  with this contract will be deleted as well!'
                buttonReply = QMessageBox.question(self, 'Delete Contract', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply != QMessageBox.Yes:
                    return

        # Remove associated documents
        urls = self.fetch_query('SELECT url FROM documents WHERE type_id=? AND owner_id=?', (1, contract_id))
        for url in urls:
            os.remove(url)
        self.run_query('DELETE FROM contracts WHERE id=?', (contract_id,))
        self.run_query('DELETE FROM documents WHERE type_id=? AND owner_id=?', (1, contract_id))
        # Remove parties
        self.run_query('DELETE FROM people_contracts WHERE contract_id=?',
                       (contract_id,))

        # Delete dependent contracts, reminders, risks and todos
        reminders = self.fetch_query('SELECT id FROM reminders WHERE contract_id=?', (contract_id,))
        for reminder in reminders:
            self.delete_reminder(reminder_id=reminder)
        risks = self.fetch_query('SELECT id FROM risks WHERE contract_id=?', (contract_id,))
        for risk in risks:
            self.delete_risk(risk_id=risk)
        todos = self.fetch_query('SELECT id FROM todos WHERE contract_id=?', (contract_id,))
        for todo in todos:
            self.delete_todo(todo_id=todo)

        self.ui.update_contracts()

    def delete_person(self, person_id=None):
        if person_id is False:
            if self.ui.people_tree.selectedIndexes() == []:
                return
            else:
                id_index = self.ui.people_tree.selectedIndexes()[0]
                person_id = self.ui.people_tree.model().itemData(id_index)[0]

                first_index = self.ui.people_tree.selectedIndexes()[1]
                first = self.ui.people_tree.model().itemData(first_index)[0]
                last_index = self.ui.people_tree.selectedIndexes()[2]
                last = self.ui.people_tree.model().itemData(last_index)[0]
                prompt = 'Are you sure you want to delete ' + first + ' ' + last + '?\nAll to-dos assigned to this person will be deleted'
                buttonReply = QMessageBox.question(self, 'Delete person', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply != QMessageBox.Yes:
                    return
        self.run_query('DELETE FROM people WHERE id=?', (person_id,))
        # Remove todos
        todos = self.fetch_query('SELECT id FROM todos WHERE responsible_id=?', (person_id,))
        for todo in todos:
            self.delete_todo(todo_id=todo)
        self.ui.update_people()

    def delete_company(self, company_id=None):
        if company_id is False:
            if self.ui.companies_tree.selectedIndexes() == []:
                return
            else:
                id_index = self.ui.companies_tree.selectedIndexes()[0]
                company_id = self.ui.companies_tree.model().itemData(id_index)[0]

                name_index = self.ui.companies_tree.selectedIndexes()[1]
                name = self.ui.companies_tree.model().itemData(name_index)[0]

                prompt = 'Are you sure you want to delete ' + name + '?\nAll reminders and to-dos associated with this company will be deleted as well!'
                buttonReply = QMessageBox.question(self, 'Delete company', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply != QMessageBox.Yes:
                    return
        self.run_query('DELETE FROM companies WHERE id=?', (company_id,))

        reminders = self.fetch_query('SELECT id FROM reminders WHERE company_id=?', (company_id,))
        for reminder in reminders:
            self.delete_reminder(reminder_id=reminder)
        todos = self.fetch_query('SELECT id FROM todos WHERE company_id=?', (company_id,))
        for todo in todos:
            self.delete_todo(todo_id=todo)
        self.ui.update_companies()

    def delete_reminder(self, reminder_id=None):
        if reminder_id is False:
            if self.ui.reminders_tree.selectedIndexes() == []:
                return
            else:
                id_index = self.ui.reminders_tree.selectedIndexes()[0]
                reminder_id = self.ui.reminders_tree.model().itemData(id_index)[0]
                name_index = self.ui.reminders_tree.selectedIndexes()[1]
                reminder_name = self.ui.reminders_tree.model().itemData(name_index)[0]
                prompt = 'Are you sure you want to delete ' + reminder_name + '?'
                buttonReply = QMessageBox.question(self, 'Delete reminder', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply != QMessageBox.Yes:
                    return
        # Remove associated documents
        urls = self.fetch_query('SELECT url FROM documents WHERE type_id=? AND owner_id=?', (2, reminder_id))
        for url in urls:
            os.remove(url)
        self.run_query('DELETE FROM reminders WHERE id=?', (reminder_id,))
        self.run_query('DELETE FROM documents WHERE type_id=? AND owner_id=?', (2, reminder_id))
        # Remove people
        self.run_query('DELETE FROM people_reminders WHERE reminder_id=?',
                       (reminder_id,))
        self.ui.update_reminders()

    def delete_risk(self, risk_id=None):
        if risk_id is False:
            if self.ui.risks_tree.selectedIndexes() == []:
                return
            else:
                id_index = self.ui.risks_tree.selectedIndexes()[0]
                risk_id = self.ui.risks_tree.model().itemData(id_index)[0]
                name_index = self.ui.risks_tree.selectedIndexes()[1]
                risk_name = self.ui.risks_tree.model().itemData(name_index)[0]
                prompt = 'Are you sure you want to delete ' + risk_name + '?'
                buttonReply = QMessageBox.question(self, 'Delete risk', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply != QMessageBox.Yes:
                    return
        # Remove associated documents
        urls = self.fetch_query('SELECT url FROM documents WHERE type_id=? AND owner_id=?', (3, risk_id))
        for url in urls:
            if self.fetch_query("SELECT count(url) FROM documents GROUP BY url HAVING url=?", (url,))[0] <= 1:
                os.remove(url)
        self.run_query('DELETE FROM risks WHERE id=?', (risk_id,))
        self.run_query('DELETE FROM documents WHERE type_id=? AND owner_id=?', (3, risk_id))
        self.ui.update_risks()

    def delete_todo(self, todo_id=None):
        if todo_id is False:
            if self.ui.todos_tree.selectedIndexes() == []:
                return
            else:
                id_index = self.ui.todos_tree.selectedIndexes()[0]
                todo_id = self.ui.todos_tree.model().itemData(id_index)[0]
                name_index = self.ui.todos_tree.selectedIndexes()[1]
                name = self.ui.todos_tree.model().itemData(name_index)[0]

                prompt = 'Are you sure you want to delete ' + name + '?'
                buttonReply = QMessageBox.question(self, 'Delete todo', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    return
        self.run_query('DELETE FROM todos WHERE id=?', (todo_id,))
        self.ui.update_todos()

    # Archive
    def archive_contract(self):
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.contracts_tree.selectedIndexes()[0]
            contract_id = self.ui.contracts_tree.model().itemData(id_index)[0]
            title_index = self.ui.contracts_tree.selectedIndexes()[1]
            contract_title = self.ui.contracts_tree.model().itemData(title_index)[0]
            arc_status = int(self.fetch_query('SELECT archived FROM contracts WHERE id=?', (contract_id,))[0])
            if arc_status == 0:
                prompt = 'Are you sure you want to archive ' + contract_title + '?'
                buttonReply = QMessageBox.question(self, 'Archive contract', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE contracts SET archived=1 WHERE id=?', (contract_id,))
                    self.ui.update_contracts()
            else:
                prompt = 'Are you sure you want to restore ' + contract_title + '?'
                buttonReply = QMessageBox.question(self, 'Archive contract', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE contracts SET archived=0 WHERE id=?', (contract_id,))
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
            arc_status = int(self.fetch_query('SELECT archived FROM people WHERE id=?', (person_id,))[0])
            if arc_status == 0:
                prompt = 'Are you sure you want to archive ' + first + ' ' + last + '?'
                buttonReply = QMessageBox.question(self, 'Archive person', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE people SET archived=1 WHERE id=?', (person_id,))
                    self.ui.update_people()
            else:
                prompt = 'Are you sure you want to restore ' + first + ' ' + last + '?'
                buttonReply = QMessageBox.question(self, 'Archive person', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE people SET archived=0 WHERE id=?', (person_id,))
                    self.ui.update_people()      

    def archive_company(self):
        if self.ui.companies_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.companies_tree.selectedIndexes()[0]
            company_id = self.ui.companies_tree.model().itemData(id_index)[0]
            name_index = self.ui.companies_tree.selectedIndexes()[1]
            company_name = self.ui.companies_tree.model().itemData(name_index)[0]
            arc_status = int(self.fetch_query('SELECT archived FROM companies WHERE id=?', (company_id,))[0])
            if arc_status == 0:
                prompt = 'Are you sure you want to archive ' + company_name + '?'
                buttonReply = QMessageBox.question(self, 'Archive company', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE companies SET archived=1 WHERE id=?', (company_id,))
                    self.ui.update_companies()
            else:
                prompt = 'Are you sure you want to restore ' + company_name + '?'
                buttonReply = QMessageBox.question(self, 'Archive company', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE companies SET archived=0 WHERE id=?', (company_id,))
                    self.ui.update_companies()

    def archive_reminder(self):
        if self.ui.reminders_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.reminders_tree.selectedIndexes()[0]
            reminder_id = self.ui.reminders_tree.model().itemData(id_index)[0]
            name_index = self.ui.reminders_tree.selectedIndexes()[1]
            reminder_name = self.ui.reminders_tree.model().itemData(name_index)[0]
            arc_status = int(self.fetch_query('SELECT archived FROM reminders WHERE id=?', (reminder_id,))[0])
            if arc_status == 0:
                prompt = 'Are you sure you want to archive ' + reminder_name + '?'
                buttonReply = QMessageBox.question(self, 'Archive reminder', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE reminders SET archived=1 WHERE id=?', (reminder_id,))
                    self.ui.update_reminders()
            else:
                prompt = 'Are you sure you want to restore ' + reminder_name + '?'
                buttonReply = QMessageBox.question(self, 'Archive reminder', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE reminders SET archived=0 WHERE id=?', (reminder_id,))
                    self.ui.update_reminders()

    def archive_risk(self):
        if self.ui.risks_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.risks_tree.selectedIndexes()[0]
            risk_id = self.ui.risks_tree.model().itemData(id_index)[0]
            name_index = self.ui.risks_tree.selectedIndexes()[1]
            risk_name = self.ui.risks_tree.model().itemData(name_index)[0]
            arc_status = int(self.fetch_query('SELECT archived FROM risks WHERE id=?', (risk_id,))[0])
            if arc_status == 0:
                prompt = 'Are you sure you want to archive ' + risk_name + '?'
                buttonReply = QMessageBox.question(self, 'Archive risk', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE risks SET archived=1 WHERE id=?', (risk_id,))
                    self.ui.update_risks()
            else:
                prompt = 'Are you sure you want to restore ' + risk_name + '?'
                buttonReply = QMessageBox.question(self, 'Archive risk', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE risks SET archived=0 WHERE id=?', (risk_id,))
                    self.ui.update_risks()
    
    def archive_todo(self):
        if self.ui.todos_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.todos_tree.selectedIndexes()[0]
            todo_id = self.ui.todos_tree.model().itemData(id_index)[0]
            name_index = self.ui.todos_tree.selectedIndexes()[1]
            todo_name = self.ui.todos_tree.model().itemData(name_index)[0]
            arc_status = int(self.fetch_query('SELECT archived FROM todos WHERE id=?', (todo_id,))[0])
            if arc_status == 0:
                prompt = 'Are you sure you want to archive ' + todo_name + '?'
                buttonReply = QMessageBox.question(self, 'Archive todo', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE todos SET archived=1 WHERE id=?', (todo_id,))
                    self.ui.update_todos()
            else:
                prompt = 'Are you sure you want to restore ' + todo_name + '?'
                buttonReply = QMessageBox.question(self, 'Archive todo', prompt,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.run_query('UPDATE todos SET archived=0 WHERE id=?', (todo_id,))
                    self.ui.update_todos()

    # Favorite
    def favorite_contract(self):
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            id_index = self.ui.contracts_tree.selectedIndexes()[0]
            contract_id = self.ui.contracts_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM contracts WHERE id=?', (contract_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE contracts SET favorite=1 WHERE id=?', (contract_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE contracts SET favorite=0 WHERE id=?', (contract_id,))
                self.message.setText('Unmarked as favorite')

            self.message.show()
            self.ui.update_contracts()

    def favorite_person(self):
        if self.ui.people_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            id_index = self.ui.people_tree.selectedIndexes()[0]
            person_id = self.ui.people_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM people WHERE id=?', (person_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE people SET favorite=1 WHERE id=?', (person_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE people SET favorite=0 WHERE id=?', (person_id,))
                self.message.setText('Unmarked as favorite')

            self.message.show()
            self.ui.update_people()

    def favorite_company(self):
        if self.ui.companies_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            id_index = self.ui.companies_tree.selectedIndexes()[0]
            company_id = self.ui.companies_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM companies WHERE id=?', (company_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE companies SET favorite=1 WHERE id=?', (company_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE companies SET favorite=0 WHERE id=?', (company_id,))
                self.message.setText('Unmarked as favorite')

            self.message.show()
            self.ui.update_companies()

    def favorite_reminder(self):
        if self.ui.reminders_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            id_index = self.ui.reminders_tree.selectedIndexes()[0]
            reminder_id = self.ui.reminders_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM reminders WHERE id=?',(reminder_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE reminders SET favorite=1 WHERE id=?', (reminder_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE reminders SET favorite=0 WHERE id=?', (reminder_id,))
                self.message.setText('Unmarked as favorite')

            self.message.show()
            self.ui.update_reminders()\

    def favorite_risk(self):
        if self.ui.risks_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            id_index = self.ui.risks_tree.selectedIndexes()[0]
            risk_id = self.ui.risks_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM risks WHERE id=?', (risk_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE risks SET favorite=1 WHERE id=?', (risk_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE risks SET favorite=0 WHERE id=?', (risk_id,))
                self.message.setText('Unmarked as favorite')

            self.message.show()
            self.ui.update_risks()

    def complete_reminder(self):
        if self.ui.reminders_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            id_index = self.ui.reminders_tree.selectedIndexes()[0]
            reminder_id = self.ui.reminders_tree.model().itemData(id_index)[0]
            complete_status = self.fetch_query('SELECT complete FROM reminders WHERE id=?',(reminder_id,))[0]
            if complete_status == 0:
                self.run_query('UPDATE reminders SET complete=1 WHERE id=?', (reminder_id,))
                self.message.setText('Marked as complete')
            else:
                self.message.setText('Reminder is already complete')

            self.message.show()
            self.ui.update_reminders()

    def uncomplete_reminder(self):
        if self.ui.reminders_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            id_index = self.ui.reminders_tree.selectedIndexes()[0]
            reminder_id = self.ui.reminders_tree.model().itemData(id_index)[0]
            complete_status = self.fetch_query('SELECT complete FROM reminders WHERE id=?', (reminder_id,))[0]
            if complete_status == 1:
                self.run_query('UPDATE reminders SET complete=0 WHERE id=?', (reminder_id,))
                self.message.setText('Marked as uncomplete')
            else:
                self.message.setText('Reminder is already uncomplete')

            self.message.show()
            self.ui.update_reminders()

    def snooze_reminder(self):
        if self.ui.reminders_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            id_index = self.ui.reminders_tree.selectedIndexes()[0]
            reminder_id = self.ui.reminders_tree.model().itemData(id_index)[0]
            snooze_status = self.fetch_query('SELECT snoozed FROM reminders WHERE id=?',(reminder_id,))[0]
            if snooze_status == 0:
                self.run_query('UPDATE reminders SET snoozed=1 WHERE id=?', (reminder_id,))
                self.message.setText('Snoozed reminder')
            else:
                self.run_query('UPDATE reminders SET snoozed=0 WHERE id=?', (reminder_id,))
                self.message.setText('Unsnoozed reminder')

            self.message.show()
            self.ui.update_reminders()

    def favorite_todo(self):
        if self.ui.todos_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon(":/images/images/icon - black.svg"))
            self.message.setWindowTitle('Contracts')
            id_index = self.ui.todos_tree.selectedIndexes()[0]
            todo_id = self.ui.todos_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM todos WHERE id=?', (todo_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE todos SET favorite=1 WHERE id=?', (todo_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE todos SET favorite=0 WHERE id=?', (todo_id,))
                self.message.setText('Unmarked as favorite')

            self.message.show()
            self.ui.update_todos()

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

    def get_specific(self):
        self.calendar_window = Calendar()
        self.calendar_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.calendar_window.select_signal.connect(self.set_specific)
        self.calendar_window.show()

    def set_specific(self, date):
        self.ui.reminder_specific_date.setText(date.toString('MM/dd/yyyy'))

    def get_until_specific(self):
        self.calendar_window = Calendar()
        self.calendar_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.calendar_window.select_signal.connect(self.set_until_specific)
        self.calendar_window.show()

    def set_until_specific(self, date):
        self.ui.recur_until_specific_2.setText(date.toString('MM/dd/yyyy'))

    def get_risk_end(self):
        self.calendar_window = Calendar()
        self.calendar_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.calendar_window.select_signal.connect(self.set_risk_end)
        self.calendar_window.show()

    def set_risk_end(self, date):
        self.ui.risk_end.setText(date.toString('MM/dd/yyyy'))

    def get_todo_start(self):
        self.calendar_window = Calendar()
        self.calendar_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.calendar_window.select_signal.connect(self.set_todo_start)
        self.calendar_window.show()

    def set_todo_start(self, date):
        self.ui.todo_start_date.setText(date.toString('MM/dd/yyyy'))

    def get_todo_end(self):
        self.calendar_window = Calendar()
        self.calendar_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.calendar_window.select_signal.connect(self.set_todo_end)
        self.calendar_window.show()

    def set_todo_end(self, date):
        self.ui.todo_resolutio_date.setText(date.toString('MM/dd/yyyy'))

    # Attachments
    def add_contract_attachment(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Add File', '.')
        name = QtCore.QUrl.fromLocalFile(filename[0]).fileName()
        if name == '':
            return

        # Adding a timestamp to make sure all urls are unique
        timestamp = str(datetime.now())[:19]
        timestamp = timestamp.replace(':','_')
        dir_ = self.dir_ + timestamp + name
        copyfile(filename[0], dir_)

        if self.ui.contract_id_lb.text() == "":
            contract_id = self.next_contract_id()
        else:
            contract_id = self.ui.contract_id_lb.text()
        # Insert into database
        try:
            sqliteConnection = sqlite3.connect('data.db')
            cursor = sqliteConnection.cursor()
            print('Connected to SQLite')
            query = """ INSERT INTO documents (name, url, type_id, date_created, owner_id, temp) VALUES (?, ?, ?, strftime('%m/%d/%Y','now'), ?, 1)"""
            record = (name, dir_, 1, contract_id)
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
            self.ui.update_contract_attachments()
        else:
            self.ui.update_contract_attachments(contract_id)

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
            id_index = self.ui.contract_attachments.selectedIndexes()[0]
            attachment_id = self.ui.contract_attachments.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete ' + name + '?'
            buttonReply = QMessageBox.question(self, 'Delete Document', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query("UPDATE documents SET del=1 WHERE id=?", (attachment_id,))
                if self.ui.contract_id_lb.text() == "":
                    self.ui.update_contract_attachments()
                else:
                    self.ui.update_contract_attachments(self.ui.contract_id_lb.text())

    def add_reminder_attachment(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Add File', '.')
        name = QtCore.QUrl.fromLocalFile(filename[0]).fileName()
        if name == '':
            return

        # Adding a timestamp to make sure all urls are unique
        timestamp = str(datetime.now())[:19]
        timestamp = timestamp.replace(':', '_')
        dir_ = self.dir_ + timestamp + name
        copyfile(filename[0], dir_)

        if self.ui.reminder_id_lb.text() == "":
            reminder_id = self.next_reminder_id()
        else:
            reminder_id = self.ui.reminder_id_lb.text()
        # Insert into database
        try:
            sqliteConnection = sqlite3.connect('data.db')
            cursor = sqliteConnection.cursor()
            print('Connected to SQLite')
            query = """ INSERT INTO documents (name, url, type_id, date_created, owner_id, temp) VALUES (?, ?, ?, strftime('%m/%d/%Y','now'), ?, 1)"""
            record = (name, dir_, 2, reminder_id)
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

        if self.ui.reminder_id_lb.text() == "":
            self.ui.update_reminder_attachments()
        else:
            self.ui.update_reminder_attachments(reminder_id)

    def open_reminder_attachment(self):
        if self.ui.reminder_attachments.selectedIndexes() == []:
            return
        else:
            url_index = self.ui.reminder_attachments.selectedIndexes()[2]
            url = self.ui.reminder_attachments.model().itemData(url_index)[0]
            os.startfile(url)

    def delete_reminder_attachment(self):
        if self.ui.reminder_attachments.selectedIndexes() == []:
            return
        else:
            name_index = self.ui.reminder_attachments.selectedIndexes()[1]
            name = self.ui.reminder_attachments.model().itemData(name_index)[0]
            id_index = self.ui.reminder_attachments.selectedIndexes()[0]
            attachment_id = self.ui.reminder_attachments.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete ' + name + '?'
            buttonReply = QMessageBox.question(self, 'Delete Document', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query("UPDATE documents SET del=1 WHERE id=?", (attachment_id,))
                if self.ui.reminder_id_lb.text() == "":
                    self.ui.update_reminder_attachments()
                else:
                    self.ui.update_reminder_attachments(self.ui.reminder_id_lb.text())

    def add_risk_attachment(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Add File', '.')
        name = QtCore.QUrl.fromLocalFile(filename[0]).fileName()
        if name == '':
            return

        # Adding a timestamp to make sure all urls are unique
        timestamp = str(datetime.now())[:19]
        timestamp = timestamp.replace(':', '_')
        dir_ = self.dir_ + timestamp + name
        copyfile(filename[0], dir_)

        if self.ui.risk_id_lb.text() == "":
            risk_id = self.next_risk_id()
        else:
            risk_id = self.ui.risk_id_lb.text()
        # Insert into database
        try:
            sqliteConnection = sqlite3.connect('data.db')
            cursor = sqliteConnection.cursor()
            print('Connected to SQLite')
            query = """ INSERT INTO documents (name, url, type_id, date_created, owner_id, temp) VALUES (?, ?, ?, strftime('%m/%d/%Y','now'), ?, 1)"""
            record = (name, dir_, 3, risk_id)
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

        if self.ui.risk_id_lb.text() == "":
            self.ui.update_risk_attachments()
        else:
            self.ui.update_risk_attachments(risk_id)

    def open_risk_attachment(self):
        if self.ui.risk_attachments.selectedIndexes() == []:
            return
        else:
            url_index = self.ui.risk_attachments.selectedIndexes()[2]
            url = self.ui.risk_attachments.model().itemData(url_index)[0]
            os.startfile(url)

    def delete_risk_attachment(self):
        if self.ui.risk_attachments.selectedIndexes() == []:
            return
        else:
            name_index = self.ui.risk_attachments.selectedIndexes()[1]
            name = self.ui.risk_attachments.model().itemData(name_index)[0]
            id_index = self.ui.risk_attachments.selectedIndexes()[0]
            attachment_id = self.ui.risk_attachments.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete ' + name + '?'
            buttonReply = QMessageBox.question(self, 'Delete Document', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query("UPDATE documents SET del=1 WHERE id=?", (attachment_id,))
                if self.ui.risk_id_lb.text() == "":
                    self.ui.update_risk_attachments()
                else:
                    self.ui.update_risk_attachments(self.ui.risk_id_lb.text())

    # People
    def party_window(self):
        self.party_window = PersonDialog()
        self.party_window.show()
        self.party_window.select_signal.connect(self.select_party)
        self.party_window.new_signal.connect(self.new_person)

    def select_party(self, person_id):
        if self.ui.contract_id_lb.text() == "":
            contract_id = self.next_contract_id()
            self.run_query(
                'INSERT INTO people_contracts(person_id,contract_id,temp) SELECT ?, ?, 1 WHERE NOT EXISTS(SELECT 1 FROM people_contracts WHERE person_id = ? AND contract_id=?);',
                (person_id, contract_id, person_id, contract_id))
            self.ui.update_parties()

        else:
            contract_id = self.ui.contract_id_lb.text()
            self.run_query('INSERT INTO people_contracts(person_id,contract_id,temp) SELECT ?, ?, 1 WHERE NOT EXISTS(SELECT 1 FROM people_contracts WHERE person_id = ? AND contract_id=?);',(person_id, contract_id, person_id, contract_id))
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
                self.run_query("UPDATE people_contracts SET del=1 WHERE person_id=?", (person_id,))
                if self.ui.contract_id_lb.text() == "":
                    self.ui.update_parties()
                else:
                    contract_id = self.ui.contract_id_lb.text()
                    self.ui.update_parties(contract_id)

    def reminder_person_window(self):
        self.reminder_person_window = PersonDialog()
        self.reminder_person_window.show()
        self.reminder_person_window.select_signal.connect(self.select_reminder_person)
        self.reminder_person_window.new_signal.connect(self.new_person)

    def select_reminder_person(self, person_id):
        if self.ui.reminder_id_lb.text() == "":
            reminder_id = self.next_reminder_id()
            self.run_query(
                'INSERT INTO people_reminders(person_id,reminder_id) SELECT ?, ? WHERE NOT EXISTS(SELECT 1 FROM people_reminders WHERE person_id = ? AND reminder_id=?);',
                (person_id, reminder_id, person_id, reminder_id))
            self.ui.update_reminder_people()

        else:
            reminder_id = self.ui.reminder_id_lb.text()
            self.run_query(
                'INSERT INTO people_reminders(person_id,reminder_id) SELECT ?, ? WHERE NOT EXISTS(SELECT 1 FROM people_reminders WHERE person_id = ? AND reminder_id=?);',
                (person_id, reminder_id, person_id, reminder_id))
            self.ui.update_reminder_people(reminder_id)

    def delete_reminder_person(self):
        if self.ui.reminder_people.selectedIndexes() == []:
            return
        else:
            first_index = self.ui.reminder_people.selectedIndexes()[1]
            first = self.ui.reminder_people.model().itemData(first_index)[0]
            last_index = self.ui.reminder_people.selectedIndexes()[2]
            last = self.ui.reminder_people.model().itemData(last_index)[0]
            id_index = self.ui.reminder_people.selectedIndexes()[0]
            person_id = self.ui.reminder_people.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete ' + first + ' ' + last + '?'
            buttonReply = QMessageBox.question(self, 'Delete reminder_person', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('UPDATE people_reminders SET del=1 WHERE person_id=?', (person_id,))
                if self.ui.reminder_id_lb.text() == "":
                    self.ui.update_reminder_people()
                else:
                    reminder_id = self.ui.reminder_id_lb.text()
                    self.ui.update_reminder_people(reminder_id)

    def add_responsible(self):
        self.new_person()

    # Next IDs
    def next_contract_id(self):
        next_id = int(self.fetch_query("SELECT seq FROM sqlite_sequence WHERE name='contracts'")[0]) + 1
        return next_id

    def next_reminder_id(self):
        next_id = int(self.fetch_query("SELECT seq FROM sqlite_sequence WHERE name='reminders'")[0]) + 1
        return next_id

    def next_risk_id(self):
        next_id = int(self.fetch_query("SELECT seq FROM sqlite_sequence WHERE name='risks'")[0]) + 1
        return next_id

    # Cleaning
    def remove_unsaved(self):
        # Remove attachments and parties if contract is cancelled
        urls = self.fetch_query("SELECT url FROM documents WHERE temp=1")
        for url in urls:
            os.remove(url)
        self.run_query("DELETE FROM documents WHERE temp=1")
        self.run_query("DELETE FROM people_contracts WHERE temp=1")
        self.run_query("DELETE FROM people_reminders WHERE temp=1")

    def restore_unsaved(self):
        self.run_query("UPDATE documents SET del=0")
        self.run_query("UPDATE people_contracts SET del=0")
        self.run_query("UPDATE people_reminders SET del=0")

    def confirm_delete(self):
        # Attachments
        urls = self.fetch_query("SELECT url FROM documents WHERE del=1")
        for url in urls:
            os.remove(url)
            self.run_query('DELETE FROM documents WHERE url=?', (url,))

        # People
        self.run_query("DELETE FROM people_contracts WHERE del=1")
        self.run_query("DELETE FROM people_reminders WHERE del=1")

    def refresh(self):
        self.refresh_signal.emit()

class Calendar(QtWidgets.QWidget, calendarWidget.Ui_Form):
    select_signal = QtCore.pyqtSignal(QtCore.QDate)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.calendar_ui = calendarWidget.Ui_Form()
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

    def refresh():
        schedule.every().day.at("00:00").do(Window.refresh)

        while True:
            schedule.run_pending()
            time.sleep(1)

    t = threading.Thread(target=refresh)
    t.start()

    sys.exit(app.exec_())