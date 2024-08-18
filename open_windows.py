from PyQt5 import QtCore, QtWidgets, QtGui
def main_open_window(parent):
    open_window = QtWidgets.QWidget(parent)
    open_window.setGeometry(QtCore.QRect(150, 150, 500, 300))
    open_window.setStyleSheet(
        "background-color: rgb(176, 196, 222, 235); border: 1px solid grey; border-radius: 3px;")
    open_window.setObjectName("open_window")
    btn_close_ow = QtWidgets.QPushButton(open_window)
    btn_close_ow.setGeometry(QtCore.QRect(470, 0, 30, 30))
    btn_close_ow.setStyleSheet("QPushButton {\n"
                               "      background-color: rgb(252, 59, 59, 200);\n"
                               "      border: none;\n"
                               "      border: 1px solid black;\n"
                               "      color: white;\n"
                               "      padding: 3px 3px;\n"
                               "      font-size: 16px;\n"
                               "}\n"
                               "QPushButton:hover {\n"
                               "      border: 1px solid grey;\n"
                               "      background-color: rgb(252, 59, 59, 220);\n"
                               "}")
    btn_close_ow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn_close_ow.setText("✕")
    btn_close_ow.clicked.connect(open_window.close)
    return open_window
def open_window_r_add(parent):
    open_window = main_open_window(parent)

    text_title = QtWidgets.QLabel(open_window)
    text_title.setText("Добавление маршрута")
    text_title.setGeometry(150, 0, 200, 50)
    text_title.setStyleSheet(
        "background-color: rgb(176, 196, 222, 0); font-size: 16px; border: none; border-radius: none; font-weight: bold;")
    text_title.setAlignment(QtCore.Qt.AlignCenter)

    style = "background-color: rgb(176, 196, 222, 0); font-size: 12px; border: none; border-bottom: 1px solid black; border-radius: none; font-weight: bold;"

    text_add_code_rout = QtWidgets.QLabel(open_window)
    text_add_code_rout.setText("Код маршрута")
    text_add_code_rout.setGeometry(53, 50, 170, 20)
    text_add_code_rout.setStyleSheet(style)
    text_add_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_add_name = QtWidgets.QLabel(open_window)
    text_add_name.setText("Имя")
    text_add_name.setGeometry(53, 80, 170, 20)
    text_add_name.setStyleSheet(style)
    text_add_name.setAlignment(QtCore.Qt.AlignCenter)

    text_add_fareway = QtWidgets.QLabel(open_window)
    text_add_fareway.setText("Дальность(в км)")
    text_add_fareway.setGeometry(53, 110, 170, 20)
    text_add_fareway.setStyleSheet(style)
    text_add_fareway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Время в пути(в часах)")
    text_add_timeinway.setGeometry(53, 140, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Оплата(в рублях)")
    text_add_timeinway.setGeometry(53, 170, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_error = QtWidgets.QLabel(open_window)
    text_error.setText("")
    text_error.setGeometry(100, 200, 300, 30)
    text_error.setStyleSheet(
        "border: none; font-weight: bold; font-size: 14px; background-color: none;")
    text_error.setAlignment(QtCore.Qt.AlignCenter)

    style_input = "background-color: rgb(140, 169, 207, 120); font-size: 13px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;"

    input_code = QtWidgets.QLineEdit(open_window)
    input_code.setGeometry(276, 50, 170, 20)
    input_code.setStyleSheet(style_input)
    input_code.setPlaceholderText("Введите код")

    input_name = QtWidgets.QLineEdit(open_window)
    input_name.setGeometry(276, 80, 170, 20)
    input_name.setStyleSheet(style_input)
    input_name.setPlaceholderText("Введите имя")

    input_fareway = QtWidgets.QLineEdit(open_window)
    input_fareway.setGeometry(276, 110, 170, 20)
    input_fareway.setStyleSheet(style_input)
    input_fareway.setPlaceholderText("Введите дальность")

    input_timeinway = QtWidgets.QLineEdit(open_window)
    input_timeinway.setGeometry(276, 140, 170, 20)
    input_timeinway.setStyleSheet(style_input)
    input_timeinway.setPlaceholderText("Введите время")

    input_payment = QtWidgets.QLineEdit(open_window)
    input_payment.setGeometry(276, 170, 170, 20)
    input_payment.setStyleSheet(style_input)
    input_payment.setPlaceholderText("Введите оплату")


    btn_accept = QtWidgets.QPushButton(open_window)
    btn_accept.setGeometry(175, 240, 150, 40)
    btn_accept.setText("Применить")
    btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn_accept.setStyleSheet("border-radius: none; font-size: 16px; background-color: #04AA6D;")

    return open_window
def open_window_r_delete(parent):
    open_window = main_open_window(parent)

    style = "background-color: rgb(176, 196, 222, 0); font-size: 13px; border: none; border-radius: none; font-weight: bold;"

    text_title = QtWidgets.QLabel(open_window)
    text_title.setText("Удаление маршрута")
    text_title.setGeometry(160, 0, 180, 50)
    text_title.setStyleSheet(
        "background-color: rgb(176, 196, 222, 0); font-size: 16px; border: none; border-radius: none; font-weight: bold;")
    text_title.setAlignment(QtCore.Qt.AlignCenter)

    text_delete_code_rout = QtWidgets.QLabel(open_window)
    text_delete_code_rout.setText("Код маршрута")
    text_delete_code_rout.setGeometry(53, 60, 170, 30)
    text_delete_code_rout.setStyleSheet(style)
    text_delete_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_delete_code_rout = QtWidgets.QLabel(open_window)
    text_delete_code_rout.setText("Пароль администратора")
    text_delete_code_rout.setGeometry(53, 130, 170, 30)
    text_delete_code_rout.setStyleSheet(style)
    text_delete_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_error = QtWidgets.QLabel(open_window)
    text_error.setText("")
    text_error.setGeometry(110, 200, 280, 30)
    text_error.setStyleSheet(
        "border: none; font-weight: bold; font-size: 14px; background-color: none;")
    text_error.setAlignment(QtCore.Qt.AlignCenter)

    input_code = QtWidgets.QLineEdit(open_window)
    input_code.setGeometry(276, 60, 170, 30)
    input_code.setStyleSheet(
        "background-color: rgb(140, 169, 207, 120); font-size: 14px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;")
    input_code.setPlaceholderText("Введите код")

    input_pass = QtWidgets.QLineEdit(open_window)
    input_pass.setGeometry(276, 130, 170, 30)
    input_pass.setStyleSheet(
        "background-color: rgb(140, 169, 207, 120); font-size: 14px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;")
    input_pass.setPlaceholderText("Введите пароль")
    input_pass.setEchoMode(QtWidgets.QLineEdit.Password)

    btn_accept = QtWidgets.QPushButton(open_window)
    btn_accept.setGeometry(175, 240, 150, 40)
    btn_accept.setText("Применить")
    btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn_accept.setStyleSheet("border-radius: none; font-size: 16px; background-color: #04AA6D;")
    return open_window

def open_window_r_edit(parent):
    open_window = main_open_window(parent)

    text_title = QtWidgets.QLabel(open_window)
    text_title.setText("Изменение маршрута")
    text_title.setGeometry(150, 0, 200, 50)
    text_title.setStyleSheet(
        "background-color: rgb(176, 196, 222, 0); font-size: 16px; border: none; border-radius: none; font-weight: bold;")
    text_title.setAlignment(QtCore.Qt.AlignCenter)

    style = "background-color: rgb(176, 196, 222, 0); font-size: 12px; border: none; border-bottom: 1px solid black; border-radius: none; font-weight: bold;"

    text_add_code_rout = QtWidgets.QLabel(open_window)
    text_add_code_rout.setText("Код маршрута(сущ-ий)")
    text_add_code_rout.setGeometry(53, 50, 170, 20)
    text_add_code_rout.setStyleSheet(style)
    text_add_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_add_name = QtWidgets.QLabel(open_window)
    text_add_name.setText("Имя")
    text_add_name.setGeometry(53, 80, 170, 20)
    text_add_name.setStyleSheet(style)
    text_add_name.setAlignment(QtCore.Qt.AlignCenter)

    text_add_fareway = QtWidgets.QLabel(open_window)
    text_add_fareway.setText("Дальность(в км)")
    text_add_fareway.setGeometry(53, 110, 170, 20)
    text_add_fareway.setStyleSheet(style)
    text_add_fareway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Время в пути(в часах)")
    text_add_timeinway.setGeometry(53, 140, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Оплата(в рублях)")
    text_add_timeinway.setGeometry(53, 170, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_error = QtWidgets.QLabel(open_window)
    text_error.setText("")
    text_error.setGeometry(100, 200, 300, 30)
    text_error.setStyleSheet(
        "border: none; font-weight: bold; font-size: 14px; background-color: none;")
    text_error.setAlignment(QtCore.Qt.AlignCenter)

    style_input = "background-color: rgb(140, 169, 207, 120); font-size: 13px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;"

    input_code = QtWidgets.QLineEdit(open_window)
    input_code.setGeometry(276, 50, 170, 20)
    input_code.setStyleSheet(style_input)
    input_code.setPlaceholderText("Введите код")

    input_name = QtWidgets.QLineEdit(open_window)
    input_name.setGeometry(276, 80, 170, 20)
    input_name.setStyleSheet(style_input)

    input_fareway = QtWidgets.QLineEdit(open_window)
    input_fareway.setGeometry(276, 110, 170, 20)
    input_fareway.setStyleSheet(style_input)

    input_timeinway = QtWidgets.QLineEdit(open_window)
    input_timeinway.setGeometry(276, 140, 170, 20)
    input_timeinway.setStyleSheet(style_input)

    input_payment = QtWidgets.QLineEdit(open_window)
    input_payment.setGeometry(276, 170, 170, 20)
    input_payment.setStyleSheet(style_input)

    btn_accept = QtWidgets.QPushButton(open_window)
    btn_accept.setGeometry(175, 240, 150, 40)
    btn_accept.setText("Применить")
    btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn_accept.setStyleSheet("border-radius: none; font-size: 16px; background-color: #04AA6D;")
    return open_window

def open_window_d_add(parent):
    open_window = main_open_window(parent)

    text_title = QtWidgets.QLabel(open_window)
    text_title.setText("Добавление водителя")
    text_title.setGeometry(150, 0, 200, 50)
    text_title.setStyleSheet(
        "background-color: rgb(176, 196, 222, 0); font-size: 16px; border: none; border-radius: none; font-weight: bold;")
    text_title.setAlignment(QtCore.Qt.AlignCenter)

    style = "background-color: rgb(176, 196, 222, 0); font-size: 12px; border: none; border-bottom: 1px solid black; border-radius: none; font-weight: bold;"

    text_add_code_rout = QtWidgets.QLabel(open_window)
    text_add_code_rout.setText("Код водителя")
    text_add_code_rout.setGeometry(53, 50, 170, 20)
    text_add_code_rout.setStyleSheet(style)
    text_add_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_add_name = QtWidgets.QLabel(open_window)
    text_add_name.setText("Имя")
    text_add_name.setGeometry(53, 80, 170, 20)
    text_add_name.setStyleSheet(style)
    text_add_name.setAlignment(QtCore.Qt.AlignCenter)

    text_add_fareway = QtWidgets.QLabel(open_window)
    text_add_fareway.setText("Фамилия")
    text_add_fareway.setGeometry(53, 110, 170, 20)
    text_add_fareway.setStyleSheet(style)
    text_add_fareway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Отчество")
    text_add_timeinway.setGeometry(53, 140, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Стаж(в днях)")
    text_add_timeinway.setGeometry(53, 170, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_error = QtWidgets.QLabel(open_window)
    text_error.setText("")
    text_error.setGeometry(100, 200, 300, 30)
    text_error.setStyleSheet(
        "border: none; font-weight: bold; font-size: 14px; background-color: none;")
    text_error.setAlignment(QtCore.Qt.AlignCenter)

    style_input = "background-color: rgb(140, 169, 207, 120); font-size: 13px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;"

    input_code = QtWidgets.QLineEdit(open_window)
    input_code.setGeometry(276, 50, 170, 20)
    input_code.setStyleSheet(style_input)
    input_code.setPlaceholderText("Введите код")

    input_name = QtWidgets.QLineEdit(open_window)
    input_name.setGeometry(276, 80, 170, 20)
    input_name.setStyleSheet(style_input)
    input_name.setPlaceholderText("Введите имя")

    input_fareway = QtWidgets.QLineEdit(open_window)
    input_fareway.setGeometry(276, 110, 170, 20)
    input_fareway.setStyleSheet(style_input)
    input_fareway.setPlaceholderText("Введите фамилию")

    input_timeinway = QtWidgets.QLineEdit(open_window)
    input_timeinway.setGeometry(276, 140, 170, 20)
    input_timeinway.setStyleSheet(style_input)
    input_timeinway.setPlaceholderText("Введите отчество")

    input_payment = QtWidgets.QLineEdit(open_window)
    input_payment.setGeometry(276, 170, 170, 20)
    input_payment.setStyleSheet(style_input)
    input_payment.setPlaceholderText("Введите стаж")


    btn_accept = QtWidgets.QPushButton(open_window)
    btn_accept.setGeometry(175, 240, 150, 40)
    btn_accept.setText("Применить")
    btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn_accept.setStyleSheet("border-radius: none; font-size: 16px; background-color: #04AA6D;")

    return open_window
def open_window_d_delete(parent):
    open_window = main_open_window(parent)

    style = "background-color: rgb(176, 196, 222, 0); font-size: 13px; border: none; border-radius: none; font-weight: bold;"

    text_title = QtWidgets.QLabel(open_window)
    text_title.setText("Удаление водителя")
    text_title.setGeometry(160, 0, 180, 50)
    text_title.setStyleSheet(
        "background-color: rgb(176, 196, 222, 0); font-size: 16px; border: none; border-radius: none; font-weight: bold;")
    text_title.setAlignment(QtCore.Qt.AlignCenter)

    text_delete_code_rout = QtWidgets.QLabel(open_window)
    text_delete_code_rout.setText("Код водителя")
    text_delete_code_rout.setGeometry(53, 60, 170, 30)
    text_delete_code_rout.setStyleSheet(style)
    text_delete_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_delete_code_rout = QtWidgets.QLabel(open_window)
    text_delete_code_rout.setText("Пароль администратора")
    text_delete_code_rout.setGeometry(53, 130, 170, 30)
    text_delete_code_rout.setStyleSheet(style)
    text_delete_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_error = QtWidgets.QLabel(open_window)
    text_error.setText("")
    text_error.setGeometry(110, 200, 280, 30)
    text_error.setStyleSheet(
        "border: none; font-weight: bold; font-size: 14px; background-color: none;")
    text_error.setAlignment(QtCore.Qt.AlignCenter)

    input_code = QtWidgets.QLineEdit(open_window)
    input_code.setGeometry(276, 60, 170, 30)
    input_code.setStyleSheet(
        "background-color: rgb(140, 169, 207, 120); font-size: 14px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;")
    input_code.setPlaceholderText("Введите код")

    input_pass = QtWidgets.QLineEdit(open_window)
    input_pass.setGeometry(276, 130, 170, 30)
    input_pass.setStyleSheet(
        "background-color: rgb(140, 169, 207, 120); font-size: 14px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;")
    input_pass.setPlaceholderText("Введите пароль")
    input_pass.setEchoMode(QtWidgets.QLineEdit.Password)

    btn_accept = QtWidgets.QPushButton(open_window)
    btn_accept.setGeometry(175, 240, 150, 40)
    btn_accept.setText("Применить")
    btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn_accept.setStyleSheet("border-radius: none; font-size: 16px; background-color: #04AA6D;")
    return open_window

def open_window_d_edit(parent):
    open_window = main_open_window(parent)

    text_title = QtWidgets.QLabel(open_window)
    text_title.setText("Изменение водителя")
    text_title.setGeometry(150, 0, 200, 50)
    text_title.setStyleSheet(
        "background-color: rgb(176, 196, 222, 0); font-size: 16px; border: none; border-radius: none; font-weight: bold;")
    text_title.setAlignment(QtCore.Qt.AlignCenter)

    style = "background-color: rgb(176, 196, 222, 0); font-size: 12px; border: none; border-bottom: 1px solid black; border-radius: none; font-weight: bold;"

    text_add_code_rout = QtWidgets.QLabel(open_window)
    text_add_code_rout.setText("Код водителя(сущ-ий)")
    text_add_code_rout.setGeometry(53, 50, 170, 20)
    text_add_code_rout.setStyleSheet(style)
    text_add_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_add_name = QtWidgets.QLabel(open_window)
    text_add_name.setText("Имя")
    text_add_name.setGeometry(53, 110, 170, 20)
    text_add_name.setStyleSheet(style)
    text_add_name.setAlignment(QtCore.Qt.AlignCenter)

    text_add_fareway = QtWidgets.QLabel(open_window)
    text_add_fareway.setText("Фамилия")
    text_add_fareway.setGeometry(53, 80, 170, 20)
    text_add_fareway.setStyleSheet(style)
    text_add_fareway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Отчество")
    text_add_timeinway.setGeometry(53, 140, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Стаж(в днях)")
    text_add_timeinway.setGeometry(53, 170, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_error = QtWidgets.QLabel(open_window)
    text_error.setText("")
    text_error.setGeometry(100, 200, 300, 30)
    text_error.setStyleSheet(
        "border: none; font-weight: bold; font-size: 14px; background-color: none;")
    text_error.setAlignment(QtCore.Qt.AlignCenter)

    style_input = "background-color: rgb(140, 169, 207, 120); font-size: 13px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;"

    input_code = QtWidgets.QLineEdit(open_window)
    input_code.setGeometry(276, 50, 170, 20)
    input_code.setStyleSheet(style_input)
    input_code.setPlaceholderText("Введите код")

    input_name = QtWidgets.QLineEdit(open_window)
    input_name.setGeometry(276, 80, 170, 20)
    input_name.setStyleSheet(style_input)

    input_fareway = QtWidgets.QLineEdit(open_window)
    input_fareway.setGeometry(276, 110, 170, 20)
    input_fareway.setStyleSheet(style_input)

    input_timeinway = QtWidgets.QLineEdit(open_window)
    input_timeinway.setGeometry(276, 140, 170, 20)
    input_timeinway.setStyleSheet(style_input)

    input_payment = QtWidgets.QLineEdit(open_window)
    input_payment.setGeometry(276, 170, 170, 20)
    input_payment.setStyleSheet(style_input)


    btn_accept = QtWidgets.QPushButton(open_window)
    btn_accept.setGeometry(175, 240, 150, 40)
    btn_accept.setText("Применить")
    btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn_accept.setStyleSheet("border-radius: none; font-size: 16px; background-color: #04AA6D;")
    return open_window

def open_window_w_add(parent):
    open_window = main_open_window(parent)

    text_title = QtWidgets.QLabel(open_window)
    text_title.setText("Добавление события")
    text_title.setGeometry(150, 0, 200, 50)
    text_title.setStyleSheet(
        "background-color: rgb(176, 196, 222, 0); font-size: 16px; border: none; border-radius: none; font-weight: bold;")
    text_title.setAlignment(QtCore.Qt.AlignCenter)

    style = "background-color: rgb(176, 196, 222, 0); font-size: 12px; border: none; border-bottom: 1px solid black; border-radius: none; font-weight: bold;"

    text_add_code_rout = QtWidgets.QLabel(open_window)
    text_add_code_rout.setText("Код маршрута")
    text_add_code_rout.setGeometry(53, 50, 170, 20)
    text_add_code_rout.setStyleSheet(style)
    text_add_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_add_name = QtWidgets.QLabel(open_window)
    text_add_name.setText("Код водителя")
    text_add_name.setGeometry(53, 80, 170, 20)
    text_add_name.setStyleSheet(style)
    text_add_name.setAlignment(QtCore.Qt.AlignCenter)

    text_add_fareway = QtWidgets.QLabel(open_window)
    text_add_fareway.setText("Дата отправки")
    text_add_fareway.setGeometry(53, 110, 170, 20)
    text_add_fareway.setStyleSheet(style)
    text_add_fareway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Дата возвращения")
    text_add_timeinway.setGeometry(53, 140, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_error = QtWidgets.QLabel(open_window)
    text_error.setText("")
    text_error.setGeometry(100, 200, 300, 30)
    text_error.setStyleSheet(
        "border: none; font-weight: bold; font-size: 14px; background-color: none;")
    text_error.setAlignment(QtCore.Qt.AlignCenter)

    style_input = "background-color: rgb(140, 169, 207, 120); font-size: 13px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;"

    input_code = QtWidgets.QLineEdit(open_window)
    input_code.setGeometry(276, 50, 170, 20)
    input_code.setStyleSheet(style_input)
    input_code.setPlaceholderText("Введите код м.")

    input_name = QtWidgets.QLineEdit(open_window)
    input_name.setGeometry(276, 80, 170, 20)
    input_name.setStyleSheet(style_input)
    input_name.setPlaceholderText("Введите код в.")

    input_fareway = QtWidgets.QDateTimeEdit(open_window)
    input_fareway.setGeometry(276, 110, 170, 20)
    input_fareway.setStyleSheet(style_input)
    input_fareway.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))

    input_timeinway = QtWidgets.QDateTimeEdit(open_window)
    input_timeinway.setGeometry(276, 140, 170, 20)
    input_timeinway.setStyleSheet(style_input)
    input_timeinway.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))

    btn_accept = QtWidgets.QPushButton(open_window)
    btn_accept.setGeometry(175, 240, 150, 40)
    btn_accept.setText("Применить")
    btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn_accept.setStyleSheet("border-radius: none; font-size: 16px; background-color: #04AA6D;")

    return open_window
def open_window_w_delete(parent):
    open_window = main_open_window(parent)

    style = "background-color: rgb(176, 196, 222, 0); font-size: 13px; border: none; border-bottom: 1px solid black; border-radius: none; font-weight: bold;"

    text_title = QtWidgets.QLabel(open_window)
    text_title.setText("Удаление события")
    text_title.setGeometry(160, 0, 180, 50)
    text_title.setStyleSheet(
        "background-color: rgb(176, 196, 222, 0); font-size: 16px; border: none; border-radius: none; font-weight: bold;")
    text_title.setAlignment(QtCore.Qt.AlignCenter)

    text_delete_code_rout = QtWidgets.QLabel(open_window)
    text_delete_code_rout.setText("ID")
    text_delete_code_rout.setGeometry(53, 60, 170, 30)
    text_delete_code_rout.setStyleSheet(style)
    text_delete_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_delete_code_rout = QtWidgets.QLabel(open_window)
    text_delete_code_rout.setText("Пароль администратора")
    text_delete_code_rout.setGeometry(53, 130, 170, 30)
    text_delete_code_rout.setStyleSheet(style)
    text_delete_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_error = QtWidgets.QLabel(open_window)
    text_error.setText("")
    text_error.setGeometry(110, 200, 280, 30)
    text_error.setStyleSheet(
        "border: none; font-weight: bold; font-size: 14px; background-color: none;")
    text_error.setAlignment(QtCore.Qt.AlignCenter)

    input_code = QtWidgets.QLineEdit(open_window)
    input_code.setGeometry(276, 60, 170, 30)
    input_code.setStyleSheet(
        "background-color: rgb(140, 169, 207, 120); font-size: 14px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;")
    input_code.setPlaceholderText("Введите ID")

    input_pass = QtWidgets.QLineEdit(open_window)
    input_pass.setGeometry(276, 130, 170, 30)
    input_pass.setStyleSheet(
        "background-color: rgb(140, 169, 207, 120); font-size: 14px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;")
    input_pass.setPlaceholderText("Введите пароль")
    input_pass.setEchoMode(QtWidgets.QLineEdit.Password)

    btn_accept = QtWidgets.QPushButton(open_window)
    btn_accept.setGeometry(175, 240, 150, 40)
    btn_accept.setText("Применить")
    btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn_accept.setStyleSheet("border-radius: none; font-size: 16px; background-color: #04AA6D;")
    return open_window

def open_window_w_edit(parent):
    open_window = main_open_window(parent)

    text_title = QtWidgets.QLabel(open_window)
    text_title.setText("Изменение события")
    text_title.setGeometry(150, 0, 200, 50)
    text_title.setStyleSheet(
        "background-color: rgb(176, 196, 222, 0); font-size: 16px; border: none; border-radius: none; font-weight: bold;")
    text_title.setAlignment(QtCore.Qt.AlignCenter)

    style = "background-color: rgb(176, 196, 222, 0); font-size: 12px; border: none; border-bottom: 1px solid black; border-radius: none; font-weight: bold;"

    text_add_code_rout = QtWidgets.QLabel(open_window)
    text_add_code_rout.setText("ID")
    text_add_code_rout.setGeometry(53, 50, 170, 20)
    text_add_code_rout.setStyleSheet(style)
    text_add_code_rout.setAlignment(QtCore.Qt.AlignCenter)

    text_add_name = QtWidgets.QLabel(open_window)
    text_add_name.setText("Код маршрута")
    text_add_name.setGeometry(53, 80, 170, 20)
    text_add_name.setStyleSheet(style)
    text_add_name.setAlignment(QtCore.Qt.AlignCenter)

    text_add_fareway = QtWidgets.QLabel(open_window)
    text_add_fareway.setText("Код водителя")
    text_add_fareway.setGeometry(53, 110, 170, 20)
    text_add_fareway.setStyleSheet(style)
    text_add_fareway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Дата отправки")
    text_add_timeinway.setGeometry(53, 140, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Дата возвращения")
    text_add_timeinway.setGeometry(53, 170, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_add_timeinway = QtWidgets.QLabel(open_window)
    text_add_timeinway.setText("Премия")
    text_add_timeinway.setGeometry(53, 200, 170, 20)
    text_add_timeinway.setStyleSheet(style)
    text_add_timeinway.setAlignment(QtCore.Qt.AlignCenter)

    text_error = QtWidgets.QLabel(open_window)
    text_error.setText("")
    text_error.setGeometry(100, 230, 300, 20)
    text_error.setStyleSheet(
        "border: none; font-weight: bold; font-size: 14px; background-color: none;")
    text_error.setAlignment(QtCore.Qt.AlignCenter)

    style_input = "background-color: rgb(140, 169, 207, 120); font-size: 13px; border: none; border-bottom: 1px solid black; border-radius: none; padding-left: 5px;"

    input_id = QtWidgets.QLineEdit(open_window)
    input_id.setGeometry(276, 50, 170, 20)
    input_id.setStyleSheet(style_input)
    input_id.setPlaceholderText("Введите ID")

    input_code_rout = QtWidgets.QLineEdit(open_window)
    input_code_rout.setGeometry(276, 80, 170, 20)
    input_code_rout.setStyleSheet(style_input)

    input_code_driver = QtWidgets.QLineEdit(open_window)
    input_code_driver.setGeometry(276, 110, 170, 20)
    input_code_driver.setStyleSheet(style_input)

    input_dateshipment = QtWidgets.QDateTimeEdit(open_window)
    input_dateshipment.setGeometry(276, 140, 170, 20)
    input_dateshipment.setStyleSheet(style_input)
    input_dateshipment.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))

    input_datereturn = QtWidgets.QDateTimeEdit(open_window)
    input_datereturn.setGeometry(276, 170, 170, 20)
    input_datereturn.setStyleSheet(style_input)
    input_datereturn.setDateTime(QtCore.QDateTime(1970, 1, 1, 0, 0, 1))

    input_payment = QtWidgets.QLineEdit(open_window)
    input_payment.setGeometry(276, 200, 170, 20)
    input_payment.setStyleSheet(style_input)


    btn_accept = QtWidgets.QPushButton(open_window)
    btn_accept.setGeometry(175, 250, 150, 40)
    btn_accept.setText("Применить")
    btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn_accept.setStyleSheet("border-radius: none; font-size: 16px; background-color: #04AA6D;")
    return open_window