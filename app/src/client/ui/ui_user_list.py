from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 611)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_login = QtWidgets.QLineEdit(parent=self.groupBox)
        self.line_login.setObjectName("line_login")
        self.horizontalLayout.addWidget(self.line_login)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_password = QtWidgets.QLineEdit(parent=self.groupBox)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_password.setObjectName("line_password")
        self.horizontalLayout_2.addWidget(self.line_password)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cb_post = QtWidgets.QComboBox(parent=self.groupBox)
        self.cb_post.setObjectName("cb_post")
        self.horizontalLayout_3.addWidget(self.cb_post)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_add = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        self.btn_reset = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_reset.setObjectName("btn_reset")
        self.verticalLayout.addWidget(self.btn_reset)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tw_user_list = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tw_user_list.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tw_user_list.setAlternatingRowColors(True)
        self.tw_user_list.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tw_user_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tw_user_list.setObjectName("tw_user_list")
        self.tw_user_list.setColumnCount(4)
        self.tw_user_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_user_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_user_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_user_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_user_list.setHorizontalHeaderItem(3, item)
        self.tw_user_list.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_4.addWidget(self.tw_user_list)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_delete = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btn_delete.setObjectName("btn_delete")
        self.verticalLayout_3.addWidget(self.btn_delete)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список пользователей"))
        self.groupBox.setTitle(_translate("MainWindow", "Пользователь"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.label_3.setText(_translate("MainWindow", "Должность"))
        self.btn_add.setText(_translate("MainWindow", "Добавить"))
        self.btn_reset.setText(_translate("MainWindow", "Отмена"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Список пользователей"))
        item = self.tw_user_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tw_user_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Время регистрации"))
        item = self.tw_user_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Логин"))
        item = self.tw_user_list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Должность"))
        self.btn_delete.setText(_translate("MainWindow", "Удалить"))