# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmAddDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from helpers import connectionDB, test

class confirmationDialog(QDialog):

    def __init__(self, updateRefs, ingID=None):
        if ingID is None:
            pass
        super(confirmationDialog, self).__init__()
        self.updateRefs = updateRefs
        self.setupUi(self)
        self.setupFromSearchResultsDialog(ingID)
        self.setupUiObjects()
        self.setupSignals()
       
    def setupUi(self, confirmationDialog):
        if not confirmationDialog.objectName():
            confirmationDialog.setObjectName(u"confirmationDialog")
        confirmationDialog.resize(500, 333)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(confirmationDialog.sizePolicy().hasHeightForWidth())
        confirmationDialog.setSizePolicy(sizePolicy)
        confirmationDialog.setMaximumSize(QSize(500, 333))
        confirmationDialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(confirmationDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(confirmationDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.HLine)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headerLabel = QLabel(self.frame_3)
        self.headerLabel.setObjectName(u"headerLabel")
        self.headerLabel.setAutoFillBackground(True)
        self.headerLabel.setAlignment(Qt.AlignCenter)
        self.headerLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.headerLabel)

        self.containerFrame = QFrame(self.frame_3)
        self.containerFrame.setObjectName(u"containerFrame")
        self.containerFrame.setAutoFillBackground(True)
        self.formLayout = QFormLayout(self.containerFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(self.containerFrame)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nameLabel)

        self.namePlaceholderLabel = QLabel(self.containerFrame)
        self.namePlaceholderLabel.setObjectName(u"namePlaceholderLabel")
        

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.namePlaceholderLabel)

        self.specificNameLabel = QLabel(self.containerFrame)
        self.specificNameLabel.setObjectName(u"specificNameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.specificNameLabel)

        self.specificNamePlaceholderLabel = QLabel(self.containerFrame)
        self.specificNamePlaceholderLabel.setObjectName(u"specificNamePlaceholderLabel")
        

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.specificNamePlaceholderLabel)

        self.supplierLabel = QLabel(self.containerFrame)
        self.supplierLabel.setObjectName(u"supplierLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.supplierLabel)

        self.supplierPlaceholderLabel = QLabel(self.containerFrame)
        self.supplierPlaceholderLabel.setObjectName(u"supplierPlaceholderLabel")
        

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.supplierPlaceholderLabel)

        self.supplierCodeLabel = QLabel(self.containerFrame)
        self.supplierCodeLabel.setObjectName(u"supplierCodeLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.supplierCodeLabel)

        self.supplierCodePlaceholderLabel = QLabel(self.containerFrame)
        self.supplierCodePlaceholderLabel.setObjectName(u"supplierCodePlaceholderLabel")
        

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.supplierCodePlaceholderLabel)

        self.label_7 = QLabel(self.containerFrame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.weightLineEdit = QLineEdit(self.containerFrame)
        self.weightLineEdit.setObjectName(u"weightLineEdit")
        self.weightLineEdit.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.weightLineEdit.setPlaceholderText("Numbers only")
        self.weightLineEdit.setFocusPolicy(Qt.StrongFocus)
       

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.weightLineEdit)

        self.label_6 = QLabel(self.containerFrame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.unitComboBox = QComboBox(self.containerFrame)
        self.unitComboBox.setObjectName(u"unitComboBox")
        self.unitComboBox.setMaxVisibleItems(15)
        self.unitComboBox.setEditable(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.unitComboBox)


        self.verticalLayout_2.addWidget(self.containerFrame)


        self.verticalLayout.addWidget(self.frame_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelPushBtn = QPushButton(confirmationDialog)
        self.cancelPushBtn.setObjectName(u"cancelPushBtn")
        self.cancelPushBtn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.cancelPushBtn)

        self.okPushBtn = QPushButton(confirmationDialog)
        self.okPushBtn.setObjectName(u"okPushBtn")
        self.okPushBtn.setFocusPolicy(Qt.StrongFocus)

        self.horizontalLayout.addWidget(self.okPushBtn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.setTabOrder(self.weightLineEdit, self.unitComboBox)
        self.setTabOrder(self.unitComboBox, self.cancelPushBtn)
        self.setTabOrder(self.cancelPushBtn, self.okPushBtn)
        
        self.retranslateUi(confirmationDialog)

        QMetaObject.connectSlotsByName(confirmationDialog)
    # setupUi

    def retranslateUi(self, confirmationDialog):
        confirmationDialog.setWindowTitle(QCoreApplication.translate("confirmationDialog", u"Confirm", None))
        self.headerLabel.setText(QCoreApplication.translate("confirmationDialog", u"Please confirm the ingredient and specify the weight added to the formula", None))
        self.nameLabel.setText(QCoreApplication.translate("confirmationDialog", u"Ingredient Name", None))
        self.namePlaceholderLabel.setText("")
        self.specificNameLabel.setText(QCoreApplication.translate("confirmationDialog", u"Specific Name", None))
        self.specificNamePlaceholderLabel.setText("")
        self.supplierLabel.setText(QCoreApplication.translate("confirmationDialog", u"Supplier", None))
        self.supplierPlaceholderLabel.setText("")
        self.supplierCodeLabel.setText(QCoreApplication.translate("confirmationDialog", u"Supplier Code", None))
        self.supplierCodePlaceholderLabel.setText("")
        self.label_7.setText(QCoreApplication.translate("confirmationDialog", u"Weight", None))
        self.label_6.setText(QCoreApplication.translate("confirmationDialog", u"Unit", None))
        self.cancelPushBtn.setText(QCoreApplication.translate("confirmationDialog", u"Cancel", None))
        self.okPushBtn.setText(QCoreApplication.translate("confirmationDialog", u"Ok", None))
    # retranslateUi

    def setupFromSearchResultsDialog(self, ingID):
        with connectionDB('FormulaSchema').cursor() as cursor:
            try:
                # (ing_common_name, ing_specific_name, supplier_name, supplier_ing_item_code, is_standard)
                cursor.execute('SELECT ing_common_name, ing_specific_name, supplier_name, supplier_ing_item_code, is_standard FROM ingredient INNER JOIN supplier ON ingredient.supplier_id = supplier.supplier_id WHERE ing_id = %s',(ingID,))
            except Exception:
                print('There was an error in the query')
                exit(1)
            ing = cursor.fetchone()

            self.namePlaceholderLabel.setText(ing[0])
            
            # if no specific name is given
            if ing[1] is None:
                if ing[4] is True:
                    self.specificNamePlaceholderLabel.setText('Standard Ingredient')
                else:
                    self.specificNamePlaceholderLabel.setText('N/A')
            else:
                self.specificNamePlaceholderLabel.setText(ing[1])

            if ing[2] is None:
                self.supplierPlaceholderLabel.setText('N/A')
            else:
                self.supplierPlaceholderLabel.setText(ing[2])

            if ing[3] is None:
                self.supplierCodePlaceholderLabel.setText('N/A')
            else:
                self.supplierCodePlaceholderLabel.setText(ing[3])
        
    def setupUiObjects(self):
        with connectionDB('FormulaSchema').cursor() as cursor:
            cursor.execute('SELECT unit_id, unit_name, unit_symbol, base_unit_factor, conversion_offset FROM unit_conversion WHERE unit_class = "mass" ORDER BY base_unit_factor DESC')
            uoms = cursor.fetchall()
            completionList = []
            for uom in uoms:
                text = "{unitName} ({unitSymbol})".format(unitName=uom[1], unitSymbol = uom[2])
                completionList.append(text)
                self.unitComboBox.addItem(text, uom)
            self.unitComboBox.setCurrentIndex(-1)

        completer = QCompleter(completionList)
        completer.setCompletionMode(QCompleter.InlineCompletion)
        self.unitComboBox.setCompleter(completer)
    
    def setupSignals(self):
        self.okPushBtn.clicked.connect(self.submit)
        self.cancelPushBtn.clicked.connect(self.cancelEvent)
    
    def setupEvent(self):
        self.keyPressEvent(Qt.Key_Enter).connect(self.submit)

    def submit(self):
        if self.validateUserInput() is False:
            pass
        else:
            rowCount = self.updateRefs.ingTabFormulaTableWidget.rowCount()
            rowIndex = self.updateRefs.ingTabFormulaTableWidget.rowCount() - 1
            if rowCount == 0:
                rowIndex = 0

            self.updateRefs.ingTabFormulaTableWidget.insertRow(rowIndex)
            ###just to see that it works. Need to fix
            self.updateRefs.ingTabFormulaTableWidget.setItem(rowIndex,0,QTableWidgetItem(self.namePlaceholderLabel.text()))
            self.updateRefs.ingTabFormulaTableWidget.setItem(rowIndex, 2,QTableWidgetItem(self.weightLineEdit.text()))
            self.updateRefs.ingTabFormulaTableWidget.setItem(rowIndex, 3, QTableWidgetItem(self.unitComboBox.currentText()))
            self.updateRefs.ingTabFormulaTableWidget.setItem(rowIndex, 4, QTableWidgetItem(self.supplierPlaceholderLabel.text()))
            self.updateRefs.ingTabFormulaTableWidget.update()
            self.updateRefs.update()
            self.close()
            ##

    def validateUserInput(self):
        try:
            weight = float(self.weightLineEdit.text()) #TODO error handling
            return True 
        except ValueError:
            msg = QMessageBox()
            msg.setText("Weight of ingredient must be a number")
            msg.exec_()
            return False
        else:
            if (self.unitComboBox.currentIndex() == -1):
                msg = QMessageBox()
                msg.setText("Must choose a unit")
                msg.exec_()
                return False
    
    def cancelEvent(self):
        confirm = QMessageBox().question(self, 'Confirm cancellation', 'Are you sure you want to cancel?', QMessageBox.Yes|QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()
    
'''
if __name__ == '__main__':
    confirmationDialog()

app = QApplication(sys.argv)
gui = confirmationDialog(1)
gui.show()
sys.exit(app.exec_())

'''