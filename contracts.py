from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import ui, calendarWidget, person
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
        self.ui.save_company.clicked.connect(self.save_company)
        self.ui.save_reminder.clicked.connect(self.save_reminder)
        self.ui.save_risk.clicked.connect(self.save_risk)

        # Dates
        self.ui.contract_start_btn.clicked.connect(self.get_start)
        self.ui.contract_cancel_btn.clicked.connect(self.get_cancel)
        self.ui.contract_end_btn.clicked.connect(self.get_end)
        self.ui.contract_review_btn.clicked.connect(self.get_review)
        self.ui.specific_date_btn.clicked.connect(self.get_specific)
        self.ui.recur_until_btn.clicked.connect(self.get_until_specific)
        self.ui.risk_end_btn.clicked.connect(self.get_risk_end)

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

        # Deletes
        self.ui.delete_contract_btn.clicked.connect(self.delete_contract)
        self.ui.delete_person_btn.clicked.connect(self.delete_person)
        self.ui.delete_company_btn.clicked.connect(self.delete_company)
        self.ui.delete_reminder_btn.clicked.connect(self.delete_reminder)
        self.ui.delete_risk_btn.clicked.connect(self.delete_risk)

        # Archives
        self.ui.archive_contract_btn.clicked.connect(self.archive_contract)
        self.ui.archive_person_btn.clicked.connect(self.archive_person)
        self.ui.archive_company_btn.clicked.connect(self.archive_company)
        self.ui.archive_reminder_btn.clicked.connect(self.archive_reminder)
        self.ui.archive_risk_btn.clicked.connect(self.archive_risk)

        # Favorites
        self.ui.favorite_contract_btn.clicked.connect(self.favorite_contract)
        self.ui.favorite_person_btn.clicked.connect(self.favorite_person)
        self.ui.favorite_company_btn.clicked.connect(self.favorite_company)
        self.ui.favorite_risk_btn.clicked.connect(self.favorite_risk)

        self.ui.complete_reminder_btn.clicked.connect(self.complete_reminder)
        self.ui.uncomplete_reminder_btn.clicked.connect(self.uncomplete_reminder)
        self.ui.snooze_reminder_btn.clicked.connect(self.snooze_reminder)

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
        self.ui.update_companies()
        self.ui.main_widget.setCurrentIndex(5)

    def show_reminders(self):
        self.ui.update_reminders()
        self.ui.main_widget.setCurrentIndex(7)

    def show_risks(self):
        self.ui.update_risks()
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
        self.ui.new_company_window()
        self.ui.main_widget.setCurrentIndex(6)

    def new_reminder(self):
        self.ui.new_reminder_window()
        self.ui.main_widget.setCurrentIndex(8)

    def new_risk(self):
        self.ui.new_risk_window()
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
            docs = self.fetch_query("SELECT url FROM documents WHERE type_id=1 AND owner_id=?", (self.next_contract_id(),))
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

            # Remove attachments and parties if contract is cancelled
            docs = self.fetch_query("SELECT url FROM documents WHERE type_id=2 AND owner_id=?", (self.next_reminder_id(),))
            for doc in docs:
                os.remove(doc)
            self.run_query("DELETE FROM documents WHERE type_id=2 AND owner_id=?", (self.next_reminder_id(),))
            self.run_query("DELETE FROM people_reminders WHERE reminder_id=?", (self.next_reminder_id(),))
            
    def cancel_risk(self):
        buttonReply = QMessageBox.question(self, 'Cancel', 'Cancel?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.show_risks()

            # Remove attachments if risk is cancelled
            docs = self.fetch_query("SELECT url FROM documents WHERE type_id=3 AND owner_id=?",
                                    (self.next_risk_id(),))
            for doc in docs:
                os.remove(doc)
            self.run_query("DELETE FROM documents WHERE type_id=3 AND owner_id=?", (self.next_risk_id(),))
            
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

        if self.ui.specific_date_radio.isChecked():
            relative_date = ''
        else:
            specific_date = ''

        if self.ui.do_not_recur_radio.isChecked():
            until_date = ''
        else:
            if self.ui.until_key_date_radio.isChecked() or self.ui.recur_indefinitely_radio.isChecked():
                until_date = ''

        # Data validation
        if name == '':
            self.message = QMessageBox()
            self.message.setText('Name cannot be empty')
            self.message.show()
            return

        if self.ui.specific_date_radio.isChecked() and specific_date == '':
            self.message = QMessageBox()
            self.message.setText('Please provide a reminder date')
            self.message.show()
            return

        if self.ui.relative_date_radio.isChecked() and relative_date == '':
            self.message = QMessageBox()
            self.message.setText('Please provide a reminder date')
            self.message.show()
            return

        if self.ui.recur_radio.isChecked():
            if self.ui.recur_until_specific.isChecked() and until_date == '':
                self.message = QMessageBox()
                self.message.setText('Please provide a reminder date')
                self.message.show()
                return

        if self.ui.recur_radio.isChecked():
            if self.ui.recur_until_specific.isChecked() and until_date == 'None':
                self.message = QMessageBox()
                self.message.setText('Please provide a reminder date')
                self.message.show()
                return

        if self.ui.relative_date_radio.isChecked() and contract_id == 0:
                self.message = QMessageBox()
                self.message.setText('Please select a contract to get a reminder date')
                self.message.show()
                return

        if self.ui.recur_radio.isChecked() and not self.ui.recur_until_specific.isChecked() and not self.ui.until_key_date_radio.isChecked() and not self.ui.recur_indefinitely_radio.isChecked():
            self.message = QMessageBox()
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

        # Calculation for next recurrence
        if self.ui.do_not_recur_radio.isChecked():
            next_recurrence = ''
        else:
            if self.ui.recur_until_specific.isChecked():
                if recur_id == 0:
                    if deadline_object + timedelta(days=1) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + timedelta(days=1)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''
                if recur_id == 1:
                    if deadline_object + timedelta(weeks=1) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + timedelta(weeks=1)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''
                if recur_id == 2:
                    if deadline_object + timedelta(weeks=2) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + timedelta(weeks=2)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''
                if recur_id == 3:
                    if deadline_object + relativedelta(months=1) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + relativedelta(months=1)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''
                if recur_id == 4:
                    if deadline_object + relativedelta(months=3) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + relativedelta(months=3)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''
                if recur_id == 5:
                    if deadline_object + relativedelta(months=6) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + relativedelta(months=6)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''
                if recur_id == 6:
                    if deadline_object + relativedelta(years=1) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + relativedelta(years=1)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''
                if recur_id == 7:
                    if deadline_object + relativedelta(years=2) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + relativedelta(years=2)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''
                if recur_id == 8:
                    if deadline_object + relativedelta(years=3) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + relativedelta(years=3)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''
                if recur_id == 9:
                    if deadline_object + relativedelta(years=4) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + relativedelta(years=4)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''
                if recur_id == 10:
                    if deadline_object + relativedelta(years=5) > datetime.strptime(until_date, '%m/%d/%Y'):
                        next_recurrence_object = deadline_object + relativedelta(years=5)
                        next_recurrence = datetime.strftime(next_recurrence_object, '%m/%d/%Y')
                    else:
                        next_recurrence = ''

        # Saving or Updating
        if reminder_id == '': # New reminder
            self.run_query("INSERT INTO reminders (name, contract_id, company_id, description, complete, snoozed, "
                           "specific_radio, relative_radio, do_not_recur_radio, recur_radio, "
                           "until_specific_radio, until_key_radio, indefinitely_radio, specific_date, "
                           "relative_date, time_id, before_after, date_id, recur_id, until_date, until_key_id, deadline, next_recurrence, date_created) "
                           "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,strftime('%m/%d/%Y','now'))", (name, contract_id, company_id, description,
                                                                   complete, snoozed, specific_radio,
                                                                   relative_radio, do_not_recur_radio,
                                                                   recur_radio, until_specific_radio,
                                                                   until_key_radio, indefinitely_radio,
                                                                   specific_date, relative_date, time_id, before_after,
                                                                   date_id, recur_id, until_date, until_key_id, deadline, next_recurrence))
        else: # Edit reminder
            self.run_query("UPDATE reminders SET name=?, contract_id=?, company_id=?, description=?, complete=?, snoozed=?, "
                           "specific_radio=?, relative_radio=?, do_not_recur_radio=?, recur_radio=?, "
                           "until_specific_radio=?, until_key_radio=?, indefinitely_radio=?, specific_date=?, "
                           "relative_date=?, time_id=?, before_after=?, date_id=?, recur_id=?, until_date=?, until_key_id=?, deadline=?, next_recurrence=? WHERE id=?",
                           (name, contract_id, company_id, description,
                            complete, snoozed, specific_radio,
                            relative_radio, do_not_recur_radio,
                            recur_radio, until_specific_radio,
                            until_key_radio, indefinitely_radio,
                            specific_date, relative_date, time_id, before_after,
                            date_id, recur_id, until_date, until_key_id, deadline, next_recurrence, reminder_id))
        self.show_reminders()
        
    def save_risk(self):
        risk_id = self.ui.risk_id_lb.text()
        name = self.ui.risk_name.text()
        contract_id = self.ui.risk_contract.currentIndex()
        probability_id = self.ui.risk_probability.currentIndex()
        impact_id = self.ui.risk_impact.currentIndex()
        type_id = self.ui.risk_type.currentIndex()
        end_date = self.ui.risk_end.text()
        notes = self.ui.risk_notes.toPlainText()
        mitigation = self.ui.risk_mitigation.toPlainText()
        
        if name == '':
            self.message = QMessageBox()
            self.message.setText('Name cannot be empty')
            self.message.show()
        else:
            if risk_id == '': # New risk
                self.run_query("INSERT INTO risks (name, contract_id, probability_id, impact_id, type_id, end_date, notes, mitigation, date_created) VALUES(?,?,?,?,?,?,?,?,strftime('%m/%d/%Y','now'))", (name, contract_id, probability_id, impact_id, type_id, end_date, notes, mitigation))
            else: # Edit contract
                self.run_query("UPDATE risks SET name=?, contract_id=?, probability_id=?, impact_id=?, type_id=?, end_date=?, notes=?, mitigation=? WHERE id=?", (name, contract_id, probability_id, impact_id, type_id, end_date, notes, mitigation, risk_id))
            self.show_risks()

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

    def edit_person_from_contract(self):
        if self.ui.contract_parties.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.contract_parties.selectedIndexes()[0]
            person_id = self.ui.contract_parties.model().itemData(id_index)[0]
            self.ui.edit_person_window(person_id)
            self.ui.main_widget.setCurrentIndex(4)
    
    def edit_company(self):
        if self.ui.companies_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.companies_tree.selectedIndexes()[0]
            company_id = self.ui.companies_tree.model().itemData(id_index)[0]
            self.ui.edit_company_window(company_id)
            self.ui.main_widget.setCurrentIndex(6)
    
    def edit_reminder(self):
        if self.ui.reminders_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.reminders_tree.selectedIndexes()[0]
            reminder_id = self.ui.reminders_tree.model().itemData(id_index)[0]
            self.ui.edit_reminder_window(reminder_id)
            self.ui.main_widget.setCurrentIndex(8)

    def edit_person_from_reminder(self):
        if self.ui.reminder_people.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.reminder_people.selectedIndexes()[0]
            person_id = self.ui.reminder_people.model().itemData(id_index)[0]
            self.ui.edit_person_window(person_id)
            self.ui.main_widget.setCurrentIndex(4)
            
    def edit_risk(self):
        if self.ui.risks_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.risks_tree.selectedIndexes()[0]
            risk_id = self.ui.risks_tree.model().itemData(id_index)[0]
            self.ui.edit_risk_window(risk_id)
            self.ui.main_widget.setCurrentIndex(10)
            
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
                # Remove associated documents
                urls = self.fetch_query('SELECT url FROM documents WHERE type_id=? AND owner_id=?',(1, contract_id))
                for url in urls:
                    os.remove(url)
                self.run_query('DELETE FROM documents WHERE type_id=? AND owner_id=?', (1,contract_id))
                # Remove parties
                self.run_query('DELETE FROM people_contracts WHERE contract_id=?',
                               (contract_id,))
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
            buttonReply = QMessageBox.question(self, 'Delete person', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM people WHERE id=?', (person_id,))
                self.ui.update_people()
     
    def delete_company(self):
        if self.ui.companies_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.companies_tree.selectedIndexes()[0]
            company_id = self.ui.companies_tree.model().itemData(id_index)[0]
            name_index = self.ui.companies_tree.selectedIndexes()[1]
            name = self.ui.companies_tree.model().itemData(name_index)[0]
            
            prompt = 'Are you sure you want to delete' + name + '?'
            buttonReply = QMessageBox.question(self, 'Delete company', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM companies WHERE id=?', (company_id,))
                self.ui.update_companies()
                
    def delete_reminder(self):
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
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM reminders WHERE id=?', (reminder_id,))
                # Remove associated documents
                urls = self.fetch_query('SELECT url FROM documents WHERE type_id=? AND owner_id=?', (2, reminder_id))
                for url in urls:
                    os.remove(url)
                self.run_query('DELETE FROM documents WHERE type_id=? AND owner_id=?', (2, reminder_id))
                # Remove people
                self.run_query('DELETE FROM people_reminders WHERE reminder_id=?',
                               (reminder_id,))
                self.ui.update_reminders()
    
    def delete_risk(self):
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
            if buttonReply == QMessageBox.Yes:
                self.run_query('DELETE FROM risks WHERE id=?', (risk_id,))
                # Remove associated documents
                urls = self.fetch_query('SELECT url FROM documents WHERE type_id=? AND owner_id=?', (3, risk_id))
                for url in urls:
                    os.remove(url)
                self.run_query('DELETE FROM documents WHERE type_id=? AND owner_id=?', (3, risk_id))
                self.ui.update_risks()

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
                
    def archive_company(self):
        if self.ui.companies_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.companies_tree.selectedIndexes()[0]
            company_id = self.ui.companies_tree.model().itemData(id_index)[0]
            name_index = self.ui.companies_tree.selectedIndexes()[1]
            company_name = self.ui.companies_tree.model().itemData(name_index)[0]
            prompt = 'Are you sure you want to archive' + company_name + '?'
            buttonReply = QMessageBox.question(self, 'Archive company', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('UPDATE companies SET archived=1 WHERE id=?', (company_id,))
                self.ui.update_companies()
                
    def archive_reminder(self):
        if self.ui.reminders_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.reminders_tree.selectedIndexes()[0]
            reminder_id = self.ui.reminders_tree.model().itemData(id_index)[0]
            name_index = self.ui.reminders_tree.selectedIndexes()[1]
            reminder_name = self.ui.reminders_tree.model().itemData(name_index)[0]
            prompt = 'Are you sure you want to archive' + reminder_name + '?'
            buttonReply = QMessageBox.question(self, 'Archive reminder', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('UPDATE reminders SET archived=1 WHERE id=?', (reminder_id,))
                self.ui.update_reminders()
                
    def archive_risk(self):
        if self.ui.risks_tree.selectedIndexes() == []:
            return
        else:
            id_index = self.ui.risks_tree.selectedIndexes()[0]
            risk_id = self.ui.risks_tree.model().itemData(id_index)[0]
            name_index = self.ui.risks_tree.selectedIndexes()[1]
            risk_name = self.ui.risks_tree.model().itemData(name_index)[0]
            prompt = 'Are you sure you want to archive' + risk_name + '?'
            buttonReply = QMessageBox.question(self, 'Archive risk', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.run_query('UPDATE risks SET archived=1 WHERE id=?', (risk_id,))
                self.ui.update_risks()
                
    # Favorite
    def favorite_contract(self):
        if self.ui.contracts_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            id_index = self.ui.contracts_tree.selectedIndexes()[0]
            contract_id = self.ui.contracts_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM contracts WHERE id=?', (contract_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE contracts SET favorite=1 WHERE id=?', (contract_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE contracts SET favorite=0 WHERE id=?', (contract_id,))
                self.message.setText('(Unmarked as favorite')

            self.message.show()
            self.ui.update_contracts()

    def favorite_person(self):
        if self.ui.people_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            id_index = self.ui.people_tree.selectedIndexes()[0]
            person_id = self.ui.people_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM people WHERE id=?', (person_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE people SET favorite=1 WHERE id=?', (person_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE people SET favorite=0 WHERE id=?', (person_id,))
                self.message.setText('(Unmarked as favorite')

            self.message.show()
            self.ui.update_people()

    def favorite_company(self):
        if self.ui.companies_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            id_index = self.ui.companies_tree.selectedIndexes()[0]
            company_id = self.ui.companies_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM companies WHERE id=?', (company_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE companies SET favorite=1 WHERE id=?', (company_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE companies SET favorite=0 WHERE id=?', (company_id,))
                self.message.setText('(Unmarked as favorite')

            self.message.show()
            self.ui.update_companies()
    
    def favorite_reminder(self):
        if self.ui.reminders_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            id_index = self.ui.reminders_tree.selectedIndexes()[0]
            reminder_id = self.ui.reminders_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM reminders WHERE id=?',(reminder_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE reminders SET favorite=1 WHERE id=?', (reminder_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE reminders SET favorite=0 WHERE id=?', (reminder_id,))
                self.message.setText('(Unmarked as favorite')
            
            self.message.show()
            self.ui.update_reminders()\

    def favorite_risk(self):
        if self.ui.risks_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
            id_index = self.ui.risks_tree.selectedIndexes()[0]
            risk_id = self.ui.risks_tree.model().itemData(id_index)[0]
            fav_status = self.fetch_query('SELECT favorite FROM risks WHERE id=?', (risk_id,))[0]
            if fav_status == 0:
                self.run_query('UPDATE risks SET favorite=1 WHERE id=?', (risk_id,))
                self.message.setText('Marked as favorite')
            else:
                self.run_query('UPDATE risks SET favorite=0 WHERE id=?', (risk_id,))
                self.message.setText('(Unmarked as favorite')

            self.message.show()
            self.ui.update_risks()

    def complete_reminder(self):
        if self.ui.reminders_tree.selectedIndexes() == []:
            return
        else:
            self.message = QMessageBox()
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
            url_index = self.ui.contract_attachments.selectedIndexes()[2]
            url = self.ui.contract_attachments.model().itemData(url_index)[0]
            id_index = self.ui.contract_attachments.selectedIndexes()[0]
            contract_id = self.ui.contract_attachments.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete ' + name + '?'
            buttonReply = QMessageBox.question(self, 'Delete Document', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                if self.ui.contract_id_lb.text() == "":
                    contract_id = self.next_contract_id()
                    self.run_query('DELETE FROM documents WHERE id=?', (contract_id,))
                    os.remove(url)
                    self.ui.update_contract_attachments()
                else:
                    contract_id = self.ui.contract_id_lb.text()
                    self.run_query('DELETE FROM documents WHERE id=?', (contract_id,))
                    os.remove(url)
                    self.ui.update_contract_attachments(contract_id)

    def add_reminder_attachment(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Add File', '.')
        name = QtCore.QUrl.fromLocalFile(filename[0]).fileName()
        if name == '':
            return
        dir = self.dir + name
        copyfile(filename[0], dir)

        if self.ui.reminder_id_lb.text() == "":
            reminder_id = self.next_reminder_id()
        else:
            reminder_id = self.ui.reminder_id_lb.text()
        # Insert into database
        try:
            sqliteConnection = sqlite3.connect('data.db')
            cursor = sqliteConnection.cursor()
            print('Connected to SQLite')
            query = """ INSERT INTO documents (name, url, type_id, date_created, owner_id) VALUES (?, ?, ?, strftime('%m/%d/%Y','now'), ?)"""
            record = (name, dir, 2, reminder_id)
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
            url_index = self.ui.reminder_attachments.selectedIndexes()[2]
            url = self.ui.reminder_attachments.model().itemData(url_index)[0]
            id_index = self.ui.reminder_attachments.selectedIndexes()[0]
            reminder_id = self.ui.reminder_attachments.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete ' + name + '?'
            buttonReply = QMessageBox.question(self, 'Delete Document', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                if self.ui.reminder_id_lb.text() == "":
                    reminder_id = self.next_reminder_id()
                    self.run_query('DELETE FROM documents WHERE id=?', (reminder_id,))
                    os.remove(url)
                    self.ui.update_reminder_attachments()
                else:
                    reminder_id = self.ui.reminder_id_lb.text()
                    self.run_query('DELETE FROM documents WHERE id=?', (reminder_id,))
                    os.remove(url)
                    self.ui.update_reminder_attachments(reminder_id)
    
    def add_risk_attachment(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Add File', '.')
        name = QtCore.QUrl.fromLocalFile(filename[0]).fileName()
        if name == '':
            return
        dir = self.dir + name
        copyfile(filename[0], dir)

        if self.ui.risk_id_lb.text() == "":
            risk_id = self.next_risk_id()
        else:
            risk_id = self.ui.risk_id_lb.text()
        # Insert into database
        try:
            sqliteConnection = sqlite3.connect('data.db')
            cursor = sqliteConnection.cursor()
            print('Connected to SQLite')
            query = """ INSERT INTO documents (name, url, type_id, date_created, owner_id) VALUES (?, ?, ?, strftime('%m/%d/%Y','now'), ?)"""
            record = (name, dir, 3, risk_id)
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
            url_index = self.ui.risk_attachments.selectedIndexes()[2]
            url = self.ui.risk_attachments.model().itemData(url_index)[0]
            id_index = self.ui.risk_attachments.selectedIndexes()[0]
            risk_id = self.ui.risk_attachments.model().itemData(id_index)[0]

            prompt = 'Are you sure you want to delete ' + name + '?'
            buttonReply = QMessageBox.question(self, 'Delete Document', prompt,
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                if self.ui.risk_id_lb.text() == "":
                    risk_id = self.next_risk_id()
                    self.run_query('DELETE FROM documents WHERE id=?', (risk_id,))
                    os.remove(url)
                    self.ui.update_risk_attachments()
                else:
                    risk_id = self.ui.risk_id_lb.text()
                    self.run_query('DELETE FROM documents WHERE id=?', (risk_id,))
                    os.remove(url)
                    self.ui.update_risk_attachments(risk_id)
                    
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
                if self.ui.reminder_id_lb.text() == "":
                    reminder_id = self.next_reminder_id()
                    self.run_query('DELETE FROM people_reminders WHERE person_id=? AND reminder_id=?',
                                   (person_id, reminder_id))
                    self.ui.update_reminder_people()
                else:
                    reminder_id = self.ui.reminder_id_lb.text()
                    self.run_query('DELETE FROM people_reminders WHERE person_id=? AND reminder_id=?',
                                   (person_id, reminder_id))
                    self.ui.update_reminder_people(reminder_id)

    # Next IDs
    def next_contract_id(self):
        next_id = self.fetch_query("SELECT seq FROM sqlite_sequence WHERE name='contracts'")[0] + 1
        return next_id
    
    def next_reminder_id(self):
        next_id = self.fetch_query("SELECT seq FROM sqlite_sequence WHERE name='reminders'")[0] + 1
        return next_id

    def next_risk_id(self):
        next_id = self.fetch_query("SELECT seq FROM sqlite_sequence WHERE name='risks'")[0] + 1
        return next_id


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

    sys.exit(app.exec_())