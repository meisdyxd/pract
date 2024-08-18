from PyQt5 import QtCore, QtWidgets, QtGui
def main_open_window(parent):
    open_window = QtWidgets.QWidget(parent)
    open_window.setStyleSheet(
        "background-color: rgb(102, 102, 255, 200)")
    open_window.setObjectName("open_window")
    return open_window

def open_window_rout_filter(parent):
    open_window = main_open_window(parent)
    open_window.setGeometry(QtCore.QRect(490, 90, 300, 250))

    # clear button
    clear_button = QtWidgets.QPushButton(open_window)
    clear_button.setGeometry(QtCore.QRect(90, 210, 120, 30))
    clear_button.setText("Очистить")
    clear_button.setStyleSheet("font-size: 16px; color: white; border: 1px solid white; background-color: rgb(102, 102, 255, 0)")
    clear_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    # ______TEXT_____
    text_style = "font-size: 14px; color: white; border-bottom: 1px solid white; background-color: rgb(102, 102, 255, 0)"
    text_code = QtWidgets.QLabel(open_window)
    text_code.setGeometry(QtCore.QRect(10, 10, 90, 30))
    text_code.setText("Код")
    text_code.setAlignment(QtCore.Qt.AlignCenter)
    text_code.setStyleSheet(text_style)
    text_code.setObjectName("text_code")

    text_name = QtWidgets.QLabel(open_window)
    text_name.setGeometry(QtCore.QRect(10, 50, 90, 30))
    text_name.setText("Название")
    text_name.setAlignment(QtCore.Qt.AlignCenter)
    text_name.setStyleSheet(text_style)
    text_name.setObjectName("text_name")

    text_fareway = QtWidgets.QLabel(open_window)
    text_fareway.setGeometry(QtCore.QRect(10, 90, 90, 30))
    text_fareway.setText("Дальность")
    text_fareway.setAlignment(QtCore.Qt.AlignCenter)
    text_fareway.setStyleSheet(text_style)
    text_fareway.setObjectName("text_fareway")

    text_time = QtWidgets.QLabel(open_window)
    text_time.setGeometry(QtCore.QRect(10, 130, 90, 30))
    text_time.setText("Время в пути")
    text_time.setAlignment(QtCore.Qt.AlignCenter)
    text_time.setStyleSheet(text_style)
    text_time.setObjectName("text_time")

    text_payment = QtWidgets.QLabel(open_window)
    text_payment.setGeometry(QtCore.QRect(10, 170, 90, 30))
    text_payment.setText("Оплата")
    text_payment.setAlignment(QtCore.Qt.AlignCenter)
    text_payment.setStyleSheet(text_style)
    text_payment.setObjectName("text_payment")
    # ______TEXT_____

    # _____INPUTS______
    style_inputs = "color: white; font-size: 15px; padding-left: 5px;"
    text_code_input = QtWidgets.QLineEdit(open_window)
    text_code_input.setGeometry(QtCore.QRect(110, 10, 180, 30))
    text_code_input.setStyleSheet(style_inputs)

    text_name_input = QtWidgets.QLineEdit(open_window)
    text_name_input.setGeometry(QtCore.QRect(110, 50, 180, 30))
    text_name_input.setStyleSheet(style_inputs)

    text_fareway_input_min = QtWidgets.QLineEdit(open_window)
    text_fareway_input_min.setGeometry(QtCore.QRect(110, 90, 80, 30))
    text_fareway_input_min.setPlaceholderText("мин. км")
    text_fareway_input_min.setStyleSheet(style_inputs)

    text_fareway_input_max = QtWidgets.QLineEdit(open_window)
    text_fareway_input_max.setGeometry(QtCore.QRect(210, 90, 80, 30))
    text_fareway_input_max.setPlaceholderText("макс. км")
    text_fareway_input_max.setStyleSheet(style_inputs)

    text_time_input_min = QtWidgets.QLineEdit(open_window)
    text_time_input_min.setGeometry(QtCore.QRect(110, 130, 80, 30))
    text_time_input_min.setPlaceholderText("мин. час")
    text_time_input_min.setStyleSheet(style_inputs)

    text_time_input_max = QtWidgets.QLineEdit(open_window)
    text_time_input_max.setGeometry(QtCore.QRect(210, 130, 80, 30))
    text_time_input_max.setPlaceholderText("макс. час")
    text_time_input_max.setStyleSheet(style_inputs)

    text_payment_input_min = QtWidgets.QLineEdit(open_window)
    text_payment_input_min.setGeometry(QtCore.QRect(110, 170, 80, 30))
    text_payment_input_min.setPlaceholderText("мин. руб")
    text_payment_input_min.setStyleSheet(style_inputs)

    text_payment_input_max = QtWidgets.QLineEdit(open_window)
    text_payment_input_max.setGeometry(QtCore.QRect(210, 170, 80, 30))
    text_payment_input_max.setPlaceholderText("макс. руб")
    text_payment_input_max.setStyleSheet(style_inputs)

    return open_window

def open_window_driver_filter(parent):
    open_window = main_open_window(parent)
    open_window.setGeometry(QtCore.QRect(490, 90, 300, 250))

    # clear button
    clear_button = QtWidgets.QPushButton(open_window)
    clear_button.setGeometry(QtCore.QRect(90, 210, 120, 30))
    clear_button.setText("Очистить")
    clear_button.setStyleSheet("font-size: 16px; color: white; border: 1px solid white;")
    clear_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    # ______TEXT_____
    text_style = "font-size: 14px; color: white; border-bottom: 1px solid white; background-color: rgb(102, 102, 255, 0)"
    text_code = QtWidgets.QLabel(open_window)
    text_code.setGeometry(QtCore.QRect(10, 10, 90, 30))
    text_code.setText("Код")
    text_code.setAlignment(QtCore.Qt.AlignCenter)
    text_code.setStyleSheet(text_style)
    text_code.setObjectName("text_code")

    text_name = QtWidgets.QLabel(open_window)
    text_name.setGeometry(QtCore.QRect(10, 50, 90, 30))
    text_name.setText("Имя")
    text_name.setAlignment(QtCore.Qt.AlignCenter)
    text_name.setStyleSheet(text_style)
    text_name.setObjectName("text_name")

    text_surname = QtWidgets.QLabel(open_window)
    text_surname.setGeometry(QtCore.QRect(10, 90, 90, 30))
    text_surname.setText("Фамилия")
    text_surname.setAlignment(QtCore.Qt.AlignCenter)
    text_surname.setStyleSheet(text_style)
    text_surname.setObjectName("text_surname")

    text_patronymic = QtWidgets.QLabel(open_window)
    text_patronymic.setGeometry(QtCore.QRect(10, 130, 90, 30))
    text_patronymic.setText("Отчество")
    text_patronymic.setAlignment(QtCore.Qt.AlignCenter)
    text_patronymic.setStyleSheet(text_style)
    text_patronymic.setObjectName("text_patronymic")

    text_seniority = QtWidgets.QLabel(open_window)
    text_seniority.setGeometry(QtCore.QRect(10, 170, 90, 30))
    text_seniority.setText("Стаж")
    text_seniority.setAlignment(QtCore.Qt.AlignCenter)
    text_seniority.setStyleSheet(text_style)
    text_seniority.setObjectName("text_seniority")
    # ______TEXT_____

    # _____INPUTS______
    style_inputs = "color: white; font-size: 15px; padding-left: 5px;"
    text_code_input = QtWidgets.QLineEdit(open_window)
    text_code_input.setGeometry(QtCore.QRect(110, 10, 180, 30))
    text_code_input.setStyleSheet(style_inputs)

    text_name_input = QtWidgets.QLineEdit(open_window)
    text_name_input.setGeometry(QtCore.QRect(110, 50, 180, 30))
    text_name_input.setStyleSheet(style_inputs)

    text_surname_input = QtWidgets.QLineEdit(open_window)
    text_surname_input.setGeometry(QtCore.QRect(110, 90, 180, 30))
    text_surname_input.setStyleSheet(style_inputs)

    text_patronymic_input = QtWidgets.QLineEdit(open_window)
    text_patronymic_input.setGeometry(QtCore.QRect(110, 130, 180, 30))
    text_patronymic_input.setStyleSheet(style_inputs)

    text_seniority_input_min = QtWidgets.QLineEdit(open_window)
    text_seniority_input_min.setGeometry(QtCore.QRect(110, 170, 80, 30))
    text_seniority_input_min.setPlaceholderText("мин.")
    text_seniority_input_min.setStyleSheet(style_inputs)

    text_seniority_input_max = QtWidgets.QLineEdit(open_window)
    text_seniority_input_max.setGeometry(QtCore.QRect(210, 170, 80, 30))
    text_seniority_input_max.setPlaceholderText("макс.")
    text_seniority_input_max.setStyleSheet(style_inputs)

    return open_window

def open_window_wd_filter(parent):
    open_window = main_open_window(parent)
    open_window.setGeometry(QtCore.QRect(440, 90, 350, 250))

    # clear button
    clear_button = QtWidgets.QPushButton(open_window)
    clear_button.setGeometry(QtCore.QRect(115, 210, 120, 30))
    clear_button.setText("Очистить")
    clear_button.setStyleSheet("font-size: 16px; color: white; border: 1px solid white;")
    clear_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    # ______TEXT_____
    text_style = "font-size: 14px; color: white; border-bottom: 1px solid white; background-color: rgb(102, 102, 255, 0)"
    text_code_rout = QtWidgets.QLabel(open_window)
    text_code_rout.setGeometry(QtCore.QRect(10, 10, 100, 30))
    text_code_rout.setText("Код маршрута")
    text_code_rout.setAlignment(QtCore.Qt.AlignCenter)
    text_code_rout.setStyleSheet(text_style)
    text_code_rout.setObjectName("text_code")

    text_code_driver = QtWidgets.QLabel(open_window)
    text_code_driver.setGeometry(QtCore.QRect(10, 50, 100, 30))
    text_code_driver.setText("Код водителя")
    text_code_driver.setAlignment(QtCore.Qt.AlignCenter)
    text_code_driver.setStyleSheet(text_style)
    text_code_driver.setObjectName("text_name")

    text_date_shipment = QtWidgets.QLabel(open_window)
    text_date_shipment.setGeometry(QtCore.QRect(10, 90, 100, 30))
    text_date_shipment.setText("Дата отпр.")
    text_date_shipment.setAlignment(QtCore.Qt.AlignCenter)
    text_date_shipment.setStyleSheet(text_style)
    text_date_shipment.setObjectName("text_surname")

    text_date_return = QtWidgets.QLabel(open_window)
    text_date_return.setGeometry(QtCore.QRect(10, 130, 100, 30))
    text_date_return.setText("Дата возвр.")
    text_date_return.setAlignment(QtCore.Qt.AlignCenter)
    text_date_return.setStyleSheet(text_style)
    text_date_return.setObjectName("text_patronymic")

    text_payment = QtWidgets.QLabel(open_window)
    text_payment.setGeometry(QtCore.QRect(10, 170, 100, 30))
    text_payment.setText("Премия")
    text_payment.setAlignment(QtCore.Qt.AlignCenter)
    text_payment.setStyleSheet(text_style)
    text_payment.setObjectName("text_seniority")
    # ______TEXT_____

    # _____INPUTS______
    style_inputs = "color: white; font-size: 15px; padding-left: 5px;"
    text_code_rout_input = QtWidgets.QLineEdit(open_window)
    text_code_rout_input.setGeometry(QtCore.QRect(120, 10, 220, 30))
    text_code_rout_input.setStyleSheet(style_inputs)

    text_code_driver_input = QtWidgets.QLineEdit(open_window)
    text_code_driver_input.setGeometry(QtCore.QRect(120, 50, 220, 30))
    text_code_driver_input.setStyleSheet(style_inputs)

    style_date = """QDateTimeEdit
{
border : 1px solid white;
background-color : #6666ff;
color: white;
font-size: 11px;
}
QDateTimeEdit::up-arrow
{}
QDateTimeEdit::down-arrow
{}"""


    text_date_shipment_input_min = QtWidgets.QDateTimeEdit(open_window)
    text_date_shipment_input_min.setGeometry(QtCore.QRect(120, 90, 105, 30))
    text_date_shipment_input_min.setStyleSheet(style_date)
    text_date_shipment_input_min.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
    text_date_shipment_input_min.setAlignment(QtCore.Qt.AlignCenter)
    text_date_shipment_input_min.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))

    text_date_shipment_input_max = QtWidgets.QDateTimeEdit(open_window)
    text_date_shipment_input_max.setGeometry(QtCore.QRect(235, 90, 105, 30))
    text_date_shipment_input_max.setStyleSheet(style_date)
    text_date_shipment_input_max.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
    text_date_shipment_input_max.setAlignment(QtCore.Qt.AlignCenter)
    text_date_shipment_input_max.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))

    text_date_return_input_min = QtWidgets.QDateTimeEdit(open_window)
    text_date_return_input_min.setGeometry(QtCore.QRect(120, 130, 105, 30))
    text_date_return_input_min.setStyleSheet(style_date)
    text_date_return_input_min.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
    text_date_return_input_min.setAlignment(QtCore.Qt.AlignCenter)
    text_date_return_input_min.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))

    text_date_return_input_max = QtWidgets.QDateTimeEdit(open_window)
    text_date_return_input_max.setGeometry(QtCore.QRect(235, 130, 105, 30))
    text_date_return_input_max.setStyleSheet(style_date)
    text_date_return_input_max.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
    text_date_return_input_max.setAlignment(QtCore.Qt.AlignCenter)
    text_date_return_input_max.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))

    text_payment_input_min = QtWidgets.QLineEdit(open_window)
    text_payment_input_min.setGeometry(QtCore.QRect(120, 170, 105, 30))
    text_payment_input_min.setPlaceholderText("мин.")
    text_payment_input_min.setStyleSheet("color: white; font-size: 14px; padding-left: 5px;")

    text_payment_input_max = QtWidgets.QLineEdit(open_window)
    text_payment_input_max.setGeometry(QtCore.QRect(235, 170, 105, 30))
    text_payment_input_max.setPlaceholderText("макс.")
    text_payment_input_max.setStyleSheet("color: white; font-size: 14px; padding-left: 5px;")

    return open_window
