from PyQt5 import QtCore, QtWidgets, QtGui
from design import Ui_MainWindow
from database import DataBase
from open_windows import *
from SECRET_DATA import *
from rus_alpha import *
from datetime import datetime
from filter_window import *
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Грузовые перевозки")
        #var

        # __rout
        self.find_string_rout = "SELECT * FROM Routs"
        self.code_r = ""
        self.name_r = ""
        self.fareway_min_r = ""
        self.fareway_max_r = ""
        self.time_min_r = ""
        self.time_max_r = ""
        self.payment_min_r = ""
        self.payment_max_r = ""

        # __driver
        self.find_string_driver = "SELECT * FROM Drivers"
        self.code_d = ""
        self.name_d = ""
        self.surname_d = ""
        self.patronymic_d = ""
        self.seniority_min_d = ""
        self.seniority_max_d = ""

        # __workdone
        self.find_string_workdone = "SELECT * FROM DoneWork"
        self.code_driver_wd = ""
        self.code_rout_wd = ""
        self.date_shipment_min_wd = "01.01.1970 0:00"
        self.date_shipment_max_wd = "01.01.1970 0:00"
        self.date_return_min_wd = "01.01.1970 0:00"
        self.date_return_max_wd = "01.01.1970 0:00"
        self.payment_min_wd = ""
        self.payment_max_wd = ""

        self.open_filter = False
        # class database
        self.database = DataBase()
        # page
        self.init_buttons_page()
        self.init_buttons_page_rout()
        self.init_buttons_page_driver()
        self.init_buttons_page_workdone()
        # load database
        self.load_from_database()
        # load filters(page)
        self.init_buttons_filters()
        self.init_open_filter()
        self.init_clear_btns_filter()
        # close other windows
        self.init_window_feach_button()

    def load_from_database(self, need=1, filter=False):
        if need == 1:
            if filter == False:
                Routs_data = self.database.cur.execute("""SELECT * FROM Routs""").fetchall()
            else:
                Routs_data = self.database.cur.execute(filter).fetchall()
            self.ui.tableRouts.setRowCount(len(Routs_data))
            for ind_r in range(len(Routs_data)):
                for ind_c in range(1, len(Routs_data[ind_r])):
                    item_text = str(Routs_data[ind_r][ind_c])
                    if ind_c == 3:
                        item_text += " км."
                    elif ind_c == 4:
                        item_text = f"{int(item_text)//24}д. {int(item_text)%24}ч."
                    elif ind_c == 5:
                        item_text = f"{round(float(item_text), 2):,} руб."
                    item = QtWidgets.QTableWidgetItem(item_text)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFont(QtGui.QFont('Times', 8, QtGui.QFont.Black))
                    self.ui.tableRouts.setItem(ind_r, ind_c-1, item)
        elif need == 2:
            if filter == False:
                Drivers_data = self.database.cur.execute("""SELECT * FROM Drivers""").fetchall()
            else:
                Drivers_data = self.database.cur.execute(filter).fetchall()
            self.ui.tableDrivers.setRowCount(len(Drivers_data))
            for ind_r in range(len(Drivers_data)):
                for ind_c in range(1, len(Drivers_data[ind_r])):
                    item_text = Drivers_data[ind_r][ind_c]
                    if ind_c == 5:
                        if item_text//365 > 4 and item_text//365 < 21:
                            letter = "л."
                        else:
                            if item_text//365%10 < 5:
                                letter = "г."
                            else:
                                letter = "л."
                        item_text = f"{item_text//365}{letter} {item_text%365//30}м. {item_text%365%30}д."
                    item = QtWidgets.QTableWidgetItem(str(item_text))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFont(QtGui.QFont('Times', 8, QtGui.QFont.Black))
                    self.ui.tableDrivers.setItem(ind_r, ind_c - 1, item)
        elif need == 3:
            if type(filter) == type([]):
                DoneWork_data = filter
                self.ui.tableWorkDone.setRowCount(len(DoneWork_data))
            else:
                if filter == False:
                    DoneWork_data = self.database.cur.execute("""SELECT * FROM DoneWork""").fetchall()
                else:
                    DoneWork_data = self.database.cur.execute(filter).fetchall()
                self.ui.tableWorkDone.setRowCount(len(DoneWork_data))
            for ind_r in range(len(DoneWork_data)):
                for ind_c in range(0, len(DoneWork_data[ind_r])):
                    item_text = str(DoneWork_data[ind_r][ind_c])
                    if ind_c == 5:
                        item_text = f"{round(float(item_text), 2):,} руб."
                    item = QtWidgets.QTableWidgetItem(item_text)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFont(QtGui.QFont('Times', 8, QtGui.QFont.Black))
                    self.ui.tableWorkDone.setItem(ind_r, ind_c, item)

    def init_buttons_page(self):
        self.ui.btn_page_drivers.clicked.connect(lambda state, x=self.ui.btn_page_drivers.text(): self.btns_page(x))
        self.ui.btn_page_routs.clicked.connect(lambda state, x=self.ui.btn_page_routs.text(): self.btns_page(x))
        self.ui.btn_page_workDone.clicked.connect(lambda state, x=self.ui.btn_page_workDone.text(): self.btns_page(x))

    def init_buttons_page_rout(self):
        self.ui.btn_addRout.clicked.connect(lambda state, x=self.ui.btn_addRout.text(): self.btns_rout(x))
        self.ui.btn_deleteRout.clicked.connect(lambda state, x=self.ui.btn_deleteRout.text(): self.btns_rout(x))
        self.ui.btn_editRout.clicked.connect(lambda state, x=self.ui.btn_editRout.text(): self.btns_rout(x))

    def init_buttons_page_driver(self):
        self.ui.btn_addDriver.clicked.connect(lambda state, x=self.ui.btn_addDriver.text(): self.btns_driver(x))
        self.ui.btn_deleteDriver.clicked.connect(lambda state, x=self.ui.btn_deleteDriver.text(): self.btns_driver(x))
        self.ui.btn_editDriver.clicked.connect(lambda state, x=self.ui.btn_editDriver.text(): self.btns_driver(x))

    def init_buttons_page_workdone(self):
        self.ui.btn_addWorkDone.clicked.connect(lambda state, x=self.ui.btn_addWorkDone.text(): self.btns_workdone(x))
        self.ui.btn_deleteWorkDone.clicked.connect(lambda state, x=self.ui.btn_deleteWorkDone.text(): self.btns_workdone(x))
        self.ui.btn_editWorkDone.clicked.connect(lambda state, x=self.ui.btn_editWorkDone.text(): self.btns_workdone(x))

    def init_buttons_filters(self):
        self.ui.btn_rout_filter.clicked.connect(lambda state, x="rout": self.btns_filters(x))
        self.ui.btn_driver_filter.clicked.connect(lambda state, x="driver": self.btns_filters(x))
        self.ui.btn_wd_filter.clicked.connect(lambda state, x="wd": self.btns_filters(x))

    def init_open_filter(self):
        self.open_window_filter_rout = open_window_rout_filter(self.ui.centralwidget)
        self.open_window_filter_driver = open_window_driver_filter(self.ui.centralwidget)
        self.open_window_filter_wd = open_window_wd_filter(self.ui.centralwidget)

        #init filter inputs_rout
        self.open_window_filter_rout.children()[-8].textEdited.connect(
            lambda x, v="code": self.change_find_string_rout(x, v))
        self.open_window_filter_rout.children()[-7].textEdited.connect(
            lambda x, v="name": self.change_find_string_rout(x, v))
        self.open_window_filter_rout.children()[-6].textEdited.connect(
            lambda x, v="fareway_min": self.change_find_string_rout(x, v))
        self.open_window_filter_rout.children()[-5].textEdited.connect(
            lambda x, v="fareway_max": self.change_find_string_rout(x, v))
        self.open_window_filter_rout.children()[-4].textEdited.connect(
            lambda x, v="time_min": self.change_find_string_rout(x, v))
        self.open_window_filter_rout.children()[-3].textEdited.connect(
            lambda x, v="time_max": self.change_find_string_rout(x, v))
        self.open_window_filter_rout.children()[-2].textEdited.connect(
            lambda x, v="payment_min": self.change_find_string_rout(x, v))
        self.open_window_filter_rout.children()[-1].textEdited.connect(
            lambda x, v="payment_max": self.change_find_string_rout(x, v))

        #init filter inputs_driver

        self.open_window_filter_driver.children()[-6].textEdited.connect(
            lambda x, v="code": self.change_find_string_driver(x, v))
        self.open_window_filter_driver.children()[-5].textEdited.connect(
            lambda x, v="name": self.change_find_string_driver(x, v))
        self.open_window_filter_driver.children()[-4].textEdited.connect(
            lambda x, v="surname": self.change_find_string_driver(x, v))
        self.open_window_filter_driver.children()[-3].textEdited.connect(
            lambda x, v="patronymic": self.change_find_string_driver(x, v))
        self.open_window_filter_driver.children()[-2].textEdited.connect(
            lambda x, v="seniority_min": self.change_find_string_driver(x, v))
        self.open_window_filter_driver.children()[-1].textEdited.connect(
            lambda x, v="seniority_max": self.change_find_string_driver(x, v))

        #init filter inputs_workdone

        self.open_window_filter_wd.children()[-8].textEdited.connect(
            lambda x, v="code_rout": self.change_find_string_workdone(x, v))
        self.open_window_filter_wd.children()[-7].textEdited.connect(
            lambda x, v="code_driver": self.change_find_string_workdone(x, v))
        self.open_window_filter_wd.children()[-6].dateTimeChanged.connect(
            lambda x, v="shipment_min": self.change_find_string_workdone(x, v))
        self.open_window_filter_wd.children()[-5].dateTimeChanged.connect(
            lambda x, v="shipment_max": self.change_find_string_workdone(x, v))
        self.open_window_filter_wd.children()[-4].dateTimeChanged.connect(
            lambda x, v="return_min": self.change_find_string_workdone(x, v))
        self.open_window_filter_wd.children()[-3].dateTimeChanged.connect(
            lambda x, v="return_max": self.change_find_string_workdone(x, v))
        self.open_window_filter_wd.children()[-2].textEdited.connect(
            lambda x, v="payment_min": self.change_find_string_workdone(x, v))
        self.open_window_filter_wd.children()[-1].textEdited.connect(
            lambda x, v="payment_max": self.change_find_string_workdone(x, v))


    def init_clear_btns_filter(self):
        self.open_window_filter_rout.children()[0].clicked.connect(
            lambda x, page="rout": self.clear_buttons(page))
        self.open_window_filter_driver.children()[0].clicked.connect(
            lambda x, page="driver": self.clear_buttons(page))
        self.open_window_filter_wd.children()[0].clicked.connect(
            lambda x, page="workdone": self.clear_buttons(page))

    def clear_buttons(self, page: str):
        if page == "rout":
            self.code_r = ""
            self.name_r = ""
            self.fareway_min_r = ""
            self.fareway_max_r = ""
            self.time_min_r = ""
            self.time_max_r = ""
            self.payment_min_r = ""
            self.payment_max_r = ""
            self.open_window_filter_rout.children()[-8].setText("")
            self.open_window_filter_rout.children()[-7].setText("")
            self.open_window_filter_rout.children()[-6].setText("")
            self.open_window_filter_rout.children()[-5].setText("")
            self.open_window_filter_rout.children()[-4].setText("")
            self.open_window_filter_rout.children()[-3].setText("")
            self.open_window_filter_rout.children()[-2].setText("")
            self.open_window_filter_rout.children()[-1].setText("")
            self.load_from_database(1)
        elif page == "driver":
            self.code_d = ""
            self.name_d = ""
            self.surname_d = ""
            self.patronymic_d = ""
            self.seniority_min_d = ""
            self.seniority_max_d = ""
            self.load_from_database(2)
            self.open_window_filter_driver.children()[-6].setText("")
            self.open_window_filter_driver.children()[-5].setText("")
            self.open_window_filter_driver.children()[-4].setText("")
            self.open_window_filter_driver.children()[-3].setText("")
            self.open_window_filter_driver.children()[-2].setText("")
            self.open_window_filter_driver.children()[-1].setText("")
        elif page == "workdone":
            self.code_driver_wd = ""
            self.code_rout_wd = ""
            self.date_shipment_min_wd = "01.01.1970 0:00"
            self.date_shipment_max_wd = "01.01.1970 0:00"
            self.date_return_min_wd = "01.01.1970 0:00"
            self.date_return_max_wd = "01.01.1970 0:00"
            self.payment_min_wd = ""
            self.payment_max_wd = ""
            self.load_from_database(3)
            self.open_window_filter_wd.children()[-8].setText("")
            self.open_window_filter_wd.children()[-7].setText("")
            self.open_window_filter_wd.children()[-6].setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))
            self.open_window_filter_wd.children()[-5].setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))
            self.open_window_filter_wd.children()[-4].setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))
            self.open_window_filter_wd.children()[-3].setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))
            self.open_window_filter_wd.children()[-2].setText("")
            self.open_window_filter_wd.children()[-1].setText("")

    def change_find_string_rout(self, t, v):
        find_string = "SELECT * FROM Routs"
        if v == "code":
            self.code_r = self.open_window_filter_rout.children()[-8].text()
        elif v == "name":
            self.name_r = self.open_window_filter_rout.children()[-7].text()
        elif v == "fareway_min":
            self.fareway_min_r = self.open_window_filter_rout.children()[-6].text()
        elif v == "fareway_max":
            self.fareway_max_r = self.open_window_filter_rout.children()[-5].text()
        elif v == "time_min":
            self.time_min_r = self.open_window_filter_rout.children()[-4].text()
        elif v == "time_max":
            self.time_max_r = self.open_window_filter_rout.children()[-3].text()
        elif v == "payment_min":
            self.payment_min_r = self.open_window_filter_rout.children()[-2].text()
        elif v == "payment_max":
            self.payment_max_r = self.open_window_filter_rout.children()[-1].text()
        if self.code_r != "":
            try:
                int(self.code_r)
                if find_string[-1] == 's' and find_string[-2] == 't':
                    find_string += " WHERE "
                else:
                    find_string += " AND "
                find_string += f"code_rout = {self.code_r}"
            except:
                pass
        if self.name_r != "":
            if find_string[-1] == 's' and find_string[-2] == 't':
                find_string += " WHERE "
            else:
                find_string += " AND "
            find_string += f"name = '{self.name_r}'"
        if self.fareway_min_r != "":
            if self.fareway_max_r != "":
                try:
                    if int(self.fareway_min_r) <= int(self.fareway_max_r):
                        if find_string[-1] == 's' and find_string[-2] == 't':
                            find_string += " WHERE "
                        else:
                            find_string += " AND "
                        find_string += f"fareway >= {self.fareway_min_r} AND fareway <= {self.fareway_max_r}"
                except:
                    pass
        elif self.fareway_max_r != "":
            if self.fareway_min_r != "":
                try:
                    if int(self.fareway_min_r) <= int(self.fareway_max_r):
                        if find_string[-1] == 's' and find_string[-2] == 't':
                            find_string += " WHERE "
                        else:
                            find_string += " AND "
                        find_string += f"fareway >= {self.fareway_min_r} AND fareway <= {self.fareway_max_r}"
                except:
                    pass
        if self.time_min_r != "":
            if self.time_max_r != "":
                try:
                    if int(self.time_min_r) <= int(self.time_max_r):
                        if find_string[-1] == 's' and find_string[-2] == 't':
                            find_string += " WHERE "
                        else:
                            find_string += " AND "
                        find_string += f"timeinway >= {self.time_min_r} AND timeinway <= {self.time_max_r}"
                except:
                    pass
        elif self.time_max_r != "":
            if self.time_min_r != "":
                try:
                    if int(self.time_min_r) <= int(self.time_max_r):
                        if find_string[-1] == 's' and find_string[-2] == 't':
                            find_string += " WHERE "
                        else:
                            find_string += " AND "
                        find_string += f"timeinway >= {self.time_min_r} AND timeinway <= {self.time_max_r}"
                except:
                    pass
        if self.payment_min_r != "":
            if self.payment_max_r != "":
                try:
                    if int(self.payment_min_r) <= int(self.payment_max_r):
                        if find_string[-1] == 's' and find_string[-2] == 't':
                            find_string += " WHERE "
                        else:
                            find_string += " AND "
                        find_string += f"payment >= {self.payment_min_r} AND payment <= {self.payment_max_r}"
                except:
                    pass
        elif self.payment_max_r != "":
            if self.payment_min_r != "":
                try:
                    if int(self.payment_min_r) <= int(self.payment_max_r):
                        if find_string[-1] == 's' and find_string[-2] == 't':
                            find_string += " WHERE "
                        else:
                            find_string += " AND "
                        find_string += f"payment >= {self.payment_min_r} AND payment <= {self.payment_max_r}"
                except:
                    pass
        self.load_from_database(1, find_string)

    def change_find_string_driver(self, t, v):
        find_string = "SELECT * FROM Drivers"
        if v == "code":
            self.code_d = self.open_window_filter_driver.children()[-6].text()
        elif v == "name":
            self.name_d = self.open_window_filter_driver.children()[-5].text()
        elif v == "surname":
            self.surname_d = self.open_window_filter_driver.children()[-4].text()
        elif v == "patronymic":
            self.patronymic_d = self.open_window_filter_driver.children()[-3].text()
        elif v == "seniority_min":
            self.seniority_min_d = self.open_window_filter_driver.children()[-2].text()
        elif v == "seniority_max":
            self.seniority_max_d = self.open_window_filter_driver.children()[-1].text()
        if self.code_d != "":
            try:
                int(self.code_d)
                if find_string[-1] == 's' and find_string[-2] == 'r':
                    find_string += " WHERE "
                else:
                    find_string += " AND "
                find_string += f"code_driver = {self.code_d}"
            except:
                pass
        if self.name_d != "":
            if find_string[-1] == 's' and find_string[-2] == 'r':
                find_string += " WHERE "
            else:
                find_string += " AND "
            find_string += f"name = '{self.name_d}'"
        if self.surname_d != "":
            if find_string[-1] == 's' and find_string[-2] == 'r':
                find_string += " WHERE "
            else:
                find_string += " AND "
            find_string += f"surname = '{self.surname_d}'"
        if self.patronymic_d != "":
            if find_string[-1] == 's' and find_string[-2] == 'r':
                find_string += " WHERE "
            else:
                find_string += " AND "
            find_string += f"patronymic = '{self.patronymic_d}'"
        if self.seniority_min_d != "":
            if self.seniority_max_d != "":
                try:
                    if int(self.seniority_min_d) <= int(self.seniority_max_d):
                        if find_string[-1] == 's' and find_string[-2] == 'r':
                            find_string += " WHERE "
                        else:
                            find_string += " AND "
                        find_string += f"seniority >= {self.seniority_min_d} AND seniority <= {self.seniority_max_d}"
                except:
                    pass
        elif self.seniority_max_d != "":
            if self.seniority_min_d != "":
                try:
                    if int(self.seniority_min_d) <= int(self.seniority_max_d):
                        if find_string[-1] == 's' and find_string[-2] == 'r':
                            find_string += " WHERE "
                        else:
                            find_string += " AND "
                        find_string += f"seniority >= {self.seniority_min_d} AND seniority <= {self.seniority_max_d}"
                except:
                    pass
        self.load_from_database(2, find_string)

    def change_find_string_workdone(self, t, v):
        find_string = "SELECT * FROM DoneWork"
        if v == "code_rout":
            self.code_rout_wd = self.open_window_filter_wd.children()[-8].text()
        elif v == "code_driver":
            self.code_driver_wd = self.open_window_filter_wd.children()[-7].text()
        elif v == "shipment_min":
            self.date_shipment_min_wd = self.open_window_filter_wd.children()[-6].text()
        elif v == "shipment_max":
            self.date_shipment_max_wd = self.open_window_filter_wd.children()[-5].text()
        elif v == "return_min":
            self.date_return_min_wd = self.open_window_filter_wd.children()[-4].text()
        elif v == "return_max":
            self.date_return_max_wd = self.open_window_filter_wd.children()[-3].text()
        elif v == "payment_min":
            self.payment_min_wd = self.open_window_filter_wd.children()[-2].text()
        elif v == "payment_max":
            self.payment_max_wd = self.open_window_filter_wd.children()[-1].text()
        if self.code_rout_wd != "":
            try:
                int(self.code_rout_wd)
                if find_string[-1] == 'k' and find_string[-2] == 'r':
                    find_string += " WHERE "
                else:
                    find_string += " AND "
                find_string += f"code_rout = {self.code_rout_wd}"
            except:
                pass
        if self.code_driver_wd != "":
            try:
                int(self.code_driver_wd)
                if find_string[-1] == 'k' and find_string[-2] == 'r':
                    find_string += " WHERE "
                else:
                    find_string += " AND "
                find_string += f"code_driver = {self.code_driver_wd}"
            except:
                pass
        if self.payment_min_wd != "" and self.payment_max_wd != "":
            try:
                if int(self.payment_min_wd) <= int(self.payment_max_wd):
                    if find_string[-1] == 'k' and find_string[-2] == 'r':
                        find_string += " WHERE "
                    else:
                        find_string += " AND "
                    find_string += f"payment >= {self.payment_min_wd} AND payment <= {self.payment_max_wd}"
            except:
                pass
        self.load_from_database(3, find_string)
        if self.date_shipment_min_wd != "01.01.1970 0:00" and self.date_shipment_max_wd != "01.01.1970 0:00":
            date_format = "%d.%m.%Y %H:%M"
            date1_obj = datetime.strptime(self.date_shipment_min_wd, date_format)
            date2_obj = datetime.strptime(self.date_shipment_max_wd, date_format)
            hours_difference = round((date2_obj - date1_obj).total_seconds() / 3600, 1)
            find1 = []
            if hours_difference > 0:
                cur_ex = self.database.cur.execute(find_string).fetchall()
                for finded in cur_ex:
                    if datetime.strptime(finded[3], date_format) >= date1_obj and datetime.strptime(finded[3], date_format) <= date2_obj:
                        find1.append(finded)
            self.load_from_database(3, find1)
            print(find1)
        if self.date_return_min_wd != "01.01.1970 0:00" and self.date_return_max_wd != "01.01.1970 0:00":
            date_format = "%d.%m.%Y %H:%M"
            date1_obj = datetime.strptime(self.date_return_min_wd, date_format)
            date2_obj = datetime.strptime(self.date_return_max_wd, date_format)
            hours_difference = round((date2_obj - date1_obj).total_seconds() / 3600, 1)
            find = []
            if self.date_shipment_min_wd != "01.01.1970 0:00" and self.date_shipment_max_wd != "01.01.1970 0:00":
                for finded in find1:
                    if datetime.strptime(finded[4], date_format) >= date1_obj and datetime.strptime(finded[4],
                                                                                           date_format) <= date2_obj:
                        find.append(finded)
            else:
                if hours_difference >= 0:
                    cur_ex = self.database.cur.execute(find_string).fetchall()
                    for finded in cur_ex:
                        if datetime.strptime(finded[4], date_format) >= date1_obj and datetime.strptime(finded[4], date_format) <= date2_obj:
                            find.append(finded)
                self.load_from_database(3, find)
            print(find)

    def btns_filters(self, page):
        if page == "rout":
            if not self.open_filter:
                self.open_filter = True
                self.open_window_filter_rout.show()
            else:
                self.open_filter = False
                self.open_window_filter_rout.close()
                self.open_window_filter_driver.close()
                self.open_window_filter_wd.close()
        elif page == "driver":
            if not self.open_filter:
                self.open_filter = True
                self.open_window_filter_driver.show()
            else:
                self.open_filter = False
                self.open_window_filter_rout.close()
                self.open_window_filter_driver.close()
                self.open_window_filter_wd.close()
        elif page == "wd":
            if not self.open_filter:
                self.open_filter = True
                self.open_window_filter_wd.show()
            else:
                self.open_filter = False
                self.open_window_filter_rout.close()
                self.open_window_filter_driver.close()
                self.open_window_filter_wd.close()
        else:
            print("FAIL")

    def init_window_feach_button(self):
        self.open_window_add_rout = open_window_r_add(self.ui.centralwidget)
        self.open_window_delete_rout = open_window_r_delete(self.ui.centralwidget)
        self.open_window_edit_rout = open_window_r_edit(self.ui.centralwidget)
        self.open_window_add_driver = open_window_d_add(self.ui.centralwidget)
        self.open_window_delete_driver = open_window_d_delete(self.ui.centralwidget)
        self.open_window_edit_driver = open_window_d_edit(self.ui.centralwidget)
        self.open_window_add_workdone = open_window_w_add(self.ui.centralwidget)
        self.open_window_delete_workdone = open_window_w_delete(self.ui.centralwidget)
        self.open_window_edit_workdone = open_window_w_edit(self.ui.centralwidget)

        #for edit

        self.open_window_edit_rout.children()[-6].textEdited.connect(
            lambda state, x="Routs": self.logic_edited(x, state))
        self.open_window_edit_driver.children()[-6].textEdited.connect(
            lambda state, x="Drivers": self.logic_edited(x, state))
        self.open_window_edit_workdone.children()[-7].textEdited.connect(
            lambda state, x="WorkDone": self.logic_edited(x, state))

        #close
        self.close_window_feach()

        #rout
        self.open_window_delete_rout.children()[-1].clicked.connect(
            lambda state, x="delete": self.logic_rout_buttons(x))
        self.open_window_add_rout.children()[-1].clicked.connect(
            lambda state, x="add": self.logic_rout_buttons(x))
        self.open_window_edit_rout.children()[-1].clicked.connect(
            lambda state, x="edit": self.logic_rout_buttons(x))
        #driver
        self.open_window_delete_driver.children()[-1].clicked.connect(
            lambda state, x="delete": self.logic_driver_buttons(x))
        self.open_window_add_driver.children()[-1].clicked.connect(
            lambda state, x="add": self.logic_driver_buttons(x))
        self.open_window_edit_driver.children()[-1].clicked.connect(
            lambda state, x="edit": self.logic_driver_buttons(x))
        #workdone
        self.open_window_delete_workdone.children()[-1].clicked.connect(
            lambda state, x="delete": self.logic_workdone_buttons(x))
        self.open_window_add_workdone.children()[-1].clicked.connect(
            lambda state, x="add": self.logic_workdone_buttons(x))
        self.open_window_edit_workdone.children()[-1].clicked.connect(
            lambda state, x="edit": self.logic_workdone_buttons(x))

    def logic_edited(self, var, state):
        if var == "Routs":
            try:
                code_rout = int(state)
                finded = self.database.cur.execute("SELECT * FROM Routs WHERE code_rout=?", (code_rout,)).fetchone()
                input_name = self.open_window_edit_rout.children()[-5]
                input_fareway = self.open_window_edit_rout.children()[-4]
                input_timeinway = self.open_window_edit_rout.children()[-3]
                input_payment = self.open_window_edit_rout.children()[-2]
                inputs = [input_name, input_fareway, input_timeinway, input_payment]
                if finded:
                    input_name.setText(str(finded[2]))
                    input_fareway.setText(str(finded[3]))
                    input_timeinway.setText(str(finded[4]))
                    input_payment.setText(str(finded[5]))
                else:
                    for inp in inputs:
                        inp.setText("")
            except:
                pass
        if var == "Drivers":
            try:
                code_driver = int(state)
                finded = self.database.cur.execute("SELECT * FROM Drivers\
                 WHERE code_driver=?", (code_driver,)).fetchone()
                input_name = self.open_window_edit_driver.children()[-5]
                input_surname = self.open_window_edit_driver.children()[-4]
                input_patronymic = self.open_window_edit_driver.children()[-3]
                input_seniority = self.open_window_edit_driver.children()[-2]
                inputs = [input_name, input_surname, input_patronymic, input_seniority]
                if finded:
                    input_name.setText(str(finded[2]))
                    input_surname.setText(str(finded[3]))
                    input_patronymic.setText(str(finded[4]))
                    input_seniority.setText(str(finded[5]))
                else:
                    for inp in inputs:
                        inp.setText("")
            except:
                pass
        if var == "WorkDone":
            try:
                id_need = int(state)
                finded = self.database.cur.execute("SELECT * FROM DoneWork\
                 WHERE id=?", (id_need,)).fetchone()
                print(finded)
                input_code_rout = self.open_window_edit_workdone.children()[-6]
                input_code_driver = self.open_window_edit_workdone.children()[-5]
                input_dateshipment = self.open_window_edit_workdone.children()[-4]
                input_datereturn = self.open_window_edit_workdone.children()[-3]
                input_payment = self.open_window_edit_workdone.children()[-2]
                inputs = [input_code_rout, input_code_driver, input_payment]
                if finded and id_need:
                    format_dateshipment = [int(x) for x in finded[3].replace(".", " ").replace(":", " ").split()]
                    format_return = [int(x) for x in finded[4].replace(".", " ").replace(":", " ").split()]
                    format_dateshipment = format_dateshipment[:3][::-1] + format_dateshipment[3:]
                    format_return = (format_return[:3])[::-1] + format_return[3:]
                    input_code_rout.setText(str(finded[1]))
                    input_code_driver.setText(str(finded[2]))
                    input_dateshipment.setDateTime(QtCore.QDateTime(*format_dateshipment, 0))
                    input_datereturn.setDateTime(QtCore.QDateTime(*format_return, 0))
                    input_payment.setText(str(finded[5]))
                else:
                    input_dateshipment.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))
                    input_datereturn.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))
                    for inp in inputs:
                        inp.setText("")
            except:
                pass

    def logic_workdone_buttons(self, button):
        if button == "add":
            text_error = self.open_window_add_workdone.children()[-6]
            text_error.setText("")
            input_code_route = self.open_window_add_workdone.children()[-5]
            input_code_driver = self.open_window_add_workdone.children()[-4]
            input_dateshipment = self.open_window_add_workdone.children()[-3]
            input_datereturn = self.open_window_add_workdone.children()[-2]

            inputs = [input_code_route, input_code_driver]
            code_route = input_code_route.text()
            code_driver = input_code_driver.text()
            dateshipment = input_dateshipment.text()
            datereturn = input_datereturn.text()
            date_format = "%d.%m.%Y %H:%M"
            date1_obj = datetime.strptime(dateshipment, date_format)
            date2_obj = datetime.strptime(datereturn, date_format)
            hours_difference = round((date2_obj - date1_obj).total_seconds() / 3600, 1)
            if code_driver == "" or code_route == "" or dateshipment == "" or datereturn == "":
                text_error.setText("Все поля должны быть заполнены")
            else:
                try:
                    code_driver = int(code_driver)
                    code_route = int(code_route)
                    rout_from_db = self.database.cur.execute("SELECT * FROM Routs WHERE code_rout = ?",
                                                             (code_route,)).fetchone()
                    driver_from_db = self.database.cur.execute("SELECT * FROM Drivers WHERE code_driver = ?",
                                                             (code_driver,)).fetchone()
                    premia = 0.0
                    if rout_from_db[4]*2 > hours_difference:
                        premia = rout_from_db[5]*0.1
                    if rout_from_db and driver_from_db:
                        if hours_difference <= 0:
                            text_error.setText("Неправильно указаны даты")
                        else:
                            self.database.cur.execute("INSERT INTO DoneWork (code_rout, code_driver, date_shipment,\
                             date_return, payment) VALUES\
                              (?, ?, ?, ?, ?)", (code_route, code_driver, dateshipment, datereturn, premia))
                            self.database.db.commit()
                            input_dateshipment.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 0))
                            input_datereturn.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 0))
                            for inp in inputs:
                                inp.setText("")
                            self.load_from_database(3)
                            text_error.setText("Событие добавлено")
                    else:
                        if rout_from_db:
                            text_error.setText("Код водителя не найден")
                        else:
                            text_error.setText("Код маршрута не найден")
                except ValueError:
                    text_error.setText("Некорректно введены данные")

        if button == "delete":
            input_id = self.open_window_delete_workdone.children()[-3]
            input_pass_driver = self.open_window_delete_workdone.children()[-2]
            list_inputs = [input_id, input_pass_driver]
            text_error = self.open_window_delete_workdone.children()[-4]
            text_error.setText("")
            id_need = input_id.text()
            pass_driver = input_pass_driver.text()
            if id_need == "" or pass_driver == "":
                text_error.setText("Все поля должны быть заполнены")
            else:
                try:
                    id_need = int(id_need)
                    rout_from_db = self.database.cur.execute("SELECT * FROM DoneWork\
                     WHERE id = ?", (id_need,)).fetchone()
                    if rout_from_db:
                        if pass_driver == SECRET_KEY:
                            for inp in list_inputs:
                                inp.setText("")
                            self.database.cur.execute("DELETE FROM DoneWork WHERE id = ?", (id_need,))
                            self.database.db.commit()
                            text_error.setText("Событие удалено")
                            self.load_from_database(3)
                        else:
                            text_error.setText("Пароль администратора неверный")
                    else:
                        text_error.setText("Код водителя неверный")
                except ValueError:
                    text_error.setText("Код состоит только из цифр")
        if button == "edit":
            text_error = self.open_window_edit_workdone.children()[-8]
            text_error.setText("")
            input_id = self.open_window_edit_workdone.children()[-7]
            input_code_rout = self.open_window_edit_workdone.children()[-6]
            input_code_driver = self.open_window_edit_workdone.children()[-5]
            input_dateshipment = self.open_window_edit_workdone.children()[-4]
            input_datereturn = self.open_window_edit_workdone.children()[-3]
            input_payment = self.open_window_edit_workdone.children()[-2]
            inputs = [input_id, input_code_rout, input_code_driver, input_payment]
            id_need = input_id.text()
            code_rout = input_code_rout.text()
            code_driver = input_code_driver.text()
            dateshipment = input_dateshipment.text()
            datereturn = input_datereturn.text()
            payment = input_payment.text()
            finded = self.database.cur.execute("SELECT * FROM DoneWork WHERE id=?", (id_need,)).fetchone()
            if finded:
                if code_driver == "" or code_rout == "" or dateshipment == "" or datereturn == "" or payment == "":
                    text_error.setText("Все поля должны быть заполнены")
                else:
                    try:
                        code_rout = int(code_rout)
                        code_driver = int(code_driver)
                        payment = float(payment)
                        self.database.cur.execute("UPDATE DoneWork SET code_rout=?, code_driver=?, date_shipment=?, date_return=?, payment=? WHERE id=?", (code_rout, code_driver, dateshipment, datereturn, payment, int(id_need)))
                        self.database.db.commit()
                        text_error.setText("Данные изменены")
                        input_dateshipment.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 0))
                        input_datereturn.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 0))
                        for inp in inputs:
                            inp.setText("")
                        self.load_from_database(3)
                    except ValueError:
                        text_error.setText("Некорректные данные")
            else:
                text_error.setText("ID события не найден")

    def logic_driver_buttons(self, button):
        if button == "add":
            text_error = self.open_window_add_driver.children()[-7]
            text_error.setText("")
            input_code_driver = self.open_window_add_driver.children()[-6]
            input_name = self.open_window_add_driver.children()[-5]
            input_surname = self.open_window_add_driver.children()[-4]
            input_patronymic = self.open_window_add_driver.children()[-3]
            input_seniority = self.open_window_add_driver.children()[-2]

            inputs = [input_code_driver, input_name, input_surname, input_patronymic, input_seniority]

            code_driver = input_code_driver.text()
            name = input_name.text()
            surname = input_surname.text()
            patronymic = input_patronymic.text()
            seniority = input_seniority.text()
            if code_driver == "" or name == "" or surname == "" or patronymic == "" or seniority == "":
                text_error.setText("Все поля должны быть заполнены")
            else:
                try:
                    code_driver = int(code_driver)
                    seniority = int(seniority)
                    rout_from_db = self.database.cur.execute("SELECT id FROM Drivers WHERE code_driver = ?",
                                                             (code_driver,)).fetchone()
                    if rout_from_db:
                        text_error.setText("Уже существует водитель с таким кодом")
                    else:
                        if rus_word_check(name) and rus_word_check(surname) and rus_word_check(patronymic):
                            for inp in inputs:
                                inp.setText("")
                            self.database.cur.execute("INSERT INTO Drivers (code_driver, name, \
                            surname, patronymic, seniority) VALUES (?,?,?,?,?)", (code_driver, str(name).title(),
                                                                                  str(surname).title(),
                                                                                  str(patronymic).title(), seniority))
                            self.database.db.commit()
                            text_error.setText("Водитель добавлен")
                            self.load_from_database(2)
                        else:
                            if not rus_word_check(name):
                                text_error.setText("Неккоректное имя")
                            elif not rus_word_check(surname):
                                text_error.setText("Неккоректная фамилия")
                            elif not rus_word_check(patronymic):
                                text_error.setText("Неккоректное отчество")

                except ValueError:
                    text_error.setText("Неккоректно введены данные")

        if button == "delete":
            input_code_driver = self.open_window_delete_driver.children()[-3]
            input_pass_driver = self.open_window_delete_driver.children()[-2]
            list_inputs = [input_code_driver, input_pass_driver]
            text_error = self.open_window_delete_driver.children()[-4]
            text_error.setText("")
            code_driver = input_code_driver.text()
            pass_driver = input_pass_driver.text()
            if code_driver == "" or pass_driver == "":
                text_error.setText("Все поля должны быть заполнены")
            else:
                try:
                    code_driver = int(code_driver)
                    rout_from_db = self.database.cur.execute("SELECT id FROM Drivers\
                     WHERE code_driver = ?", (code_driver,)).fetchone()
                    if rout_from_db:
                        if pass_driver == SECRET_KEY:
                            for inp in list_inputs:
                                inp.setText("")
                            self.database.cur.execute("DELETE FROM Drivers WHERE code_driver = ?", (code_driver,))
                            self.database.db.commit()
                            text_error.setText("Водитель удалён")
                            self.load_from_database(2)
                        else:
                            text_error.setText("Пароль администратора неверный")
                    else:
                        text_error.setText("Код водителя неверный")
                except ValueError:
                    text_error.setText("Код состоит только из цифр")
        if button == "edit":
            text_error = self.open_window_edit_driver.children()[-7]
            text_error.setText("")
            input_code_driver = self.open_window_edit_driver.children()[-6]
            input_name = self.open_window_edit_driver.children()[-4]
            input_surname = self.open_window_edit_driver.children()[-5]
            print(input_name.text())
            input_patronymic = self.open_window_edit_driver.children()[-3]
            input_seniority = self.open_window_edit_driver.children()[-2]
            inputs = [input_code_driver, input_name, input_surname, input_patronymic, input_seniority]
            code_driver = input_code_driver.text()
            name = input_name.text()
            surname = input_surname.text()
            patronymic = input_patronymic.text()
            seniority = input_seniority.text()
            finded = self.database.cur.execute("SELECT * FROM Drivers WHERE code_driver=?", (code_driver,)).fetchone()
            if finded:
                if code_driver == "" or name == "" or surname == "" or patronymic == "" or seniority == "":
                    text_error.setText("Все поля должны быть заполнены")
                else:
                    code_driver = int(code_driver)
                    seniority = int(seniority)
                    self.database.cur.execute("UPDATE Drivers SET name = ?, surname = ?, patronymic = ?, seniority = ?\
                     WHERE code_driver = ?", (name, surname, patronymic, seniority, code_driver))
                    self.database.db.commit()
                    text_error.setText("Данные изменены")
                    for inp in inputs:
                        inp.setText("")
                    self.load_from_database(2)
            else:
                if code_driver != "":
                    text_error.setText("Водитель не найден")

    def logic_rout_buttons(self, button):
        if button == "add":
            text_error = self.open_window_add_rout.children()[-7]
            text_error.setText("")
            input_code_rout = self.open_window_add_rout.children()[-6]
            input_name = self.open_window_add_rout.children()[-5]
            input_fareway = self.open_window_add_rout.children()[-4]
            input_timeinway = self.open_window_add_rout.children()[-3]
            input_payment = self.open_window_add_rout.children()[-2]

            inputs = [input_code_rout, input_name, input_fareway, input_timeinway, input_payment]

            code_rout = input_code_rout.text()
            name = input_name.text()
            fareway = input_fareway.text()
            timeinway = input_timeinway.text()
            payment = input_payment.text()
            if code_rout == "" or name == "" or fareway == "" or timeinway == "" or payment == "":
                text_error.setText("Все поля должны быть заполнены")
            else:
                try:
                    code_rout = int(code_rout)
                    fareway = int(fareway)
                    timeinway = int(timeinway)
                    payment = float(payment)
                    rout_from_db = self.database.cur.execute("SELECT id FROM Routs WHERE code_rout = ?",
                                                             (code_rout,)).fetchone()
                    if rout_from_db:
                        text_error.setText("Уже существует маршрут с таким кодом")
                    else:
                        for inp in inputs:
                            inp.setText("")
                        self.database.cur.execute("INSERT INTO Routs (code_rout, name, fareway, timeinway, payment) \
                        VALUES (?,?,?,?,?)", (code_rout, str(name), fareway, timeinway, payment))
                        self.database.db.commit()
                        text_error.setText("Маршрут добавлен")
                        self.load_from_database(1)

                except ValueError:
                    text_error.setText("Неккоректно введены данные")

        if button == "delete":
            input_code_rout = self.open_window_delete_rout.children()[-3]
            input_pass_rout = self.open_window_delete_rout.children()[-2]
            list_inputs = [input_code_rout, input_pass_rout]
            text_error = self.open_window_delete_rout.children()[-4]
            text_error.setText("")
            code_rout = input_code_rout.text()
            pass_rout = input_pass_rout.text()
            if code_rout == "" or pass_rout == "":
                text_error.setText("Все поля должны быть заполнены")
            else:
                try:
                    int(code_rout)
                    rout_from_db = self.database.cur.execute("SELECT id FROM Routs\
                     WHERE code_rout = ?", (code_rout,)).fetchone()
                    if rout_from_db:
                        if pass_rout == SECRET_KEY:
                            for inp in list_inputs:
                                inp.setText("")
                            self.database.cur.execute("DELETE FROM Routs WHERE code_rout = ?", (int(code_rout),))
                            self.database.db.commit()
                            text_error.setText("Маршрут удалён")
                            self.load_from_database(1)
                        else:
                            text_error.setText("Пароль администратора неверный")
                    else:
                        text_error.setText("Код маршрута неверный")
                except ValueError:
                    text_error.setText("Код состоит только из цифр")
        if button == "edit":
            text_error = self.open_window_edit_rout.children()[-7]
            text_error.setText("")
            input_code_rout = self.open_window_edit_rout.children()[-6]
            input_name = self.open_window_edit_rout.children()[-5]
            input_fareway = self.open_window_edit_rout.children()[-4]
            input_timeinway = self.open_window_edit_rout.children()[-3]
            input_payment = self.open_window_edit_rout.children()[-2]
            inputs = [input_code_rout, input_name, input_fareway, input_timeinway, input_payment]
            code_rout = input_code_rout.text()
            name = input_name.text()
            fareway = input_fareway.text()
            timeinway = input_timeinway.text()
            payment = input_payment.text()
            finded = self.database.cur.execute("SELECT * FROM Routs WHERE code_rout=?", (code_rout,)).fetchone()
            if not finded:
                text_error.setText("Маршрут не найден")
            else:
                if code_rout == "" or name == "" or fareway == "" or timeinway == "" or payment == "":
                    text_error.setText("Все поля должны быть заполнены")
                else:
                    code_rout = int(code_rout)
                    fareway = int(fareway)
                    timeinway = int(timeinway)
                    payment = float(payment)
                    self.database.cur.execute("UPDATE Routs SET name = ?, fareway = ?, timeinway = ?, payment = ? WHERE\
                     code_rout = ?", (str(name), fareway, timeinway, payment, code_rout))
                    self.database.db.commit()
                    text_error.setText("Маршрут изменён")
                    for inp in inputs:
                        inp.setText("")
                    self.load_from_database(1)

    def close_window_feach(self):
        self.open_window_add_rout.close()
        self.open_window_delete_rout.close()
        self.open_window_edit_rout.close()
        self.open_window_add_driver.close()
        self.open_window_edit_driver.close()
        self.open_window_delete_driver.close()
        self.open_window_add_workdone.close()
        self.open_window_delete_workdone.close()
        self.open_window_edit_workdone.close()
        self.open_window_filter_rout.close()
        self.open_window_filter_driver.close()
        self.open_window_filter_wd.close()

    def btns_page(self, title_button):
        match title_button:
            case "Маршруты":
                self.ui.windows.setCurrentIndex(0)
                self.load_from_database()
                self.close_window_feach()
                self.open_filter = False
            case "Водители":
                self.ui.windows.setCurrentIndex(1)
                self.load_from_database(2)
                self.close_window_feach()
                self.open_filter = False
            case "Проделанная работа":
                self.load_from_database(3)
                self.ui.windows.setCurrentIndex(2)
                self.close_window_feach()
                self.open_filter = False

    def btns_rout(self, title_button):
        self.close_window_feach()
        match title_button:
            case "Добавить маршрут":
                self.open_window_add_rout.show()
            case "Удалить маршрут":
                self.open_window_delete_rout.show()
            case "Изменить маршрут":
                self.open_window_edit_rout.show()

    def btns_driver(self, title_button):
        self.close_window_feach()
        match title_button:
            case "Добавить водителя":
                self.open_window_add_driver.show()
            case "Удалить водителя":
                self.open_window_delete_driver.show()
            case "Изменить данные":
                self.open_window_edit_driver.show()

    def btns_workdone(self, title_button):
        self.close_window_feach()
        match title_button:
            case "Добавить":
                self.open_window_add_workdone.show()
            case "Удалить":
                self.open_window_delete_workdone.show()
            case "Изменить данные":
                self.open_window_edit_workdone.show()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())