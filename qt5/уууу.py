import googletrans

# from googletrans import Translator
#
# translator = Translator()
#
# result = translator.translate('ПРИВЕТ',dest='pl')
tabl = 'tabl'
lll = {'f': 1, 'h': 3, 'l': 'l'}
lll.setdefault('d', 'r')
print(lll)

# для формирования динамической таблицы
# def tabl_gen(self, flag):
#     if flag == 'FIO':
#         config = fio_dict
#         try:
#             self.tableWidget.setColumnCount(config.colum)
#             for x in range(config.colum):
#                 item = QtWidgets.QTableWidgetItem()
#                 self.tableWidget.setVerticalHeaderItem(x, item)
#             self.tableWidget.setRowCount(config.row)
#             for r in range(config.row):
#                 item = QtWidgets.QTableWidgetItem()
#                 self.tableWidget.setHorizontalHeaderItem(0, item)
#             return True
#         except Exception as f:
#             return f



# print(result.dest)
# print(result.origin)
# print(result.text)
# print(result.pronunciation)
# print(googletrans.LANGUAGES)c

# def func_(self):
#     text_new = self.textEdit.toPlainText()
#     if self.checkBox_3.isChecked():
#         trans_text = translator.translate(text_new, dest='pl')
#         self.lineEdit.setText(trans_text.text)
#     elif self.checkBox_2.isChecked():
#         trans_text = translator.translate(text_new, dest='pl')
#         self.lineEdit.setText(trans_text.text)
#     else:
#         self.lineEdit.setText(text_new)
#     if self.r
#         print('Start')
#
# self.pushButton.clicked.connect(self.func_)
