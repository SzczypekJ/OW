# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1582, 861)
        self.menuFile = QAction(MainWindow)
        self.menuFile.setObjectName(u"menuFile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.criteriaEditor = QGroupBox(self.tab)
        self.criteriaEditor.setObjectName(u"criteriaEditor")
        self.gridLayout_3 = QGridLayout(self.criteriaEditor)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buttonAddCriteria = QPushButton(self.criteriaEditor)
        self.buttonAddCriteria.setObjectName(u"buttonAddCriteria")

        self.gridLayout_3.addWidget(self.buttonAddCriteria, 1, 0, 1, 1)

        self.buttonRemoveCriteria = QPushButton(self.criteriaEditor)
        self.buttonRemoveCriteria.setObjectName(u"buttonRemoveCriteria")

        self.gridLayout_3.addWidget(self.buttonRemoveCriteria, 1, 1, 1, 1)

        self.criteriaTable = QTableWidget(self.criteriaEditor)
        if (self.criteriaTable.columnCount() < 2):
            self.criteriaTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.criteriaTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.criteriaTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.criteriaTable.rowCount() < 2):
            self.criteriaTable.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.criteriaTable.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.criteriaTable.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.criteriaTable.setItem(1, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.criteriaTable.setItem(1, 1, __qtablewidgetitem5)
        self.criteriaTable.setObjectName(u"criteriaTable")

        self.gridLayout_3.addWidget(self.criteriaTable, 0, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.criteriaEditor)

        self.generationGroup = QGroupBox(self.tab)
        self.generationGroup.setObjectName(u"generationGroup")
        self.gridLayout = QGridLayout(self.generationGroup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonGenerate = QPushButton(self.generationGroup)
        self.buttonGenerate.setObjectName(u"buttonGenerate")

        self.gridLayout.addWidget(self.buttonGenerate, 3, 0, 1, 1)

        self.spinBoxObjectCount = QSpinBox(self.generationGroup)
        self.spinBoxObjectCount.setObjectName(u"spinBoxObjectCount")
        self.spinBoxObjectCount.setMinimum(2)
        self.spinBoxObjectCount.setMaximum(999999999)
        self.spinBoxObjectCount.setValue(10)

        self.gridLayout.addWidget(self.spinBoxObjectCount, 1, 2, 1, 1)

        self.buttonSort = QPushButton(self.generationGroup)
        self.buttonSort.setObjectName(u"buttonSort")

        self.gridLayout.addWidget(self.buttonSort, 3, 1, 1, 1)

        self.spinBoxSort2 = QSpinBox(self.generationGroup)
        self.spinBoxSort2.setObjectName(u"spinBoxSort2")
        self.spinBoxSort2.setMinimum(1)

        self.gridLayout.addWidget(self.spinBoxSort2, 3, 2, 1, 1)

        self.label = QLabel(self.generationGroup)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.distributionComboBox = QComboBox(self.generationGroup)
        self.distributionComboBox.addItem("")
        self.distributionComboBox.addItem("")
        self.distributionComboBox.addItem("")
        self.distributionComboBox.setObjectName(u"distributionComboBox")

        self.gridLayout.addWidget(self.distributionComboBox, 0, 1, 1, 1)

        self.spinBoxDistributionParam2 = QDoubleSpinBox(self.generationGroup)
        self.spinBoxDistributionParam2.setObjectName(u"spinBoxDistributionParam2")
        self.spinBoxDistributionParam2.setSingleStep(0.500000000000000)
        self.spinBoxDistributionParam2.setValue(0.500000000000000)

        self.gridLayout.addWidget(self.spinBoxDistributionParam2, 1, 1, 1, 1)

        self.spinBoxDistributionParam1 = QDoubleSpinBox(self.generationGroup)
        self.spinBoxDistributionParam1.setObjectName(u"spinBoxDistributionParam1")
        self.spinBoxDistributionParam1.setSingleStep(0.500000000000000)
        self.spinBoxDistributionParam1.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.spinBoxDistributionParam1, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.generationGroup)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.valuesEditor = QGroupBox(self.tab)
        self.valuesEditor.setObjectName(u"valuesEditor")
        self.gridLayout_4 = QGridLayout(self.valuesEditor)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.valuesTable = QTableWidget(self.valuesEditor)
        if (self.valuesTable.columnCount() < 2):
            self.valuesTable.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.valuesTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.valuesTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        if (self.valuesTable.rowCount() < 10):
            self.valuesTable.setRowCount(10)
        self.valuesTable.setObjectName(u"valuesTable")
        self.valuesTable.setShowGrid(True)
        self.valuesTable.setRowCount(10)
        self.valuesTable.setColumnCount(2)

        self.gridLayout_4.addWidget(self.valuesTable, 0, 0, 1, 2)


        self.verticalLayout.addWidget(self.valuesEditor)

        self.actionsGroup = QGroupBox(self.tab)
        self.actionsGroup.setObjectName(u"actionsGroup")
        self.gridLayout_2 = QGridLayout(self.actionsGroup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.actionsGroup)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.buttonSolve = QPushButton(self.actionsGroup)
        self.buttonSolve.setObjectName(u"buttonSolve")

        self.gridLayout_2.addWidget(self.buttonSolve, 1, 0, 1, 1)

        self.buttonBenchmark = QPushButton(self.actionsGroup)
        self.buttonBenchmark.setObjectName(u"buttonBenchmark")

        self.gridLayout_2.addWidget(self.buttonBenchmark, 1, 1, 1, 1)

        self.algorithmComboBox = QComboBox(self.actionsGroup)
        self.algorithmComboBox.addItem("")
        self.algorithmComboBox.addItem("")
        self.algorithmComboBox.addItem("")
        self.algorithmComboBox.setObjectName(u"algorithmComboBox")

        self.gridLayout_2.addWidget(self.algorithmComboBox, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.actionsGroup)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.outputText = QPlainTextEdit(self.tab_2)
        self.outputText.setObjectName(u"outputText")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setItalic(False)
        self.outputText.setFont(font)
        self.outputText.setReadOnly(True)

        self.gridLayout_5.addWidget(self.outputText, 1, 1, 1, 1)

        self.plotButton = QPushButton(self.tab_2)
        self.plotButton.setObjectName(u"plotButton")

        self.gridLayout_5.addWidget(self.plotButton, 0, 1, 1, 1)

        self.mpl_widget = MplWidget(self.tab_2)
        self.mpl_widget.setObjectName(u"mpl_widget")

        self.gridLayout_5.addWidget(self.mpl_widget, 0, 0, 2, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1582, 33))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Optymalizacja Wielokryterialna lab3", None))
        self.menuFile.setText(QCoreApplication.translate("MainWindow", u"Plik", None))
        self.criteriaEditor.setTitle(QCoreApplication.translate("MainWindow", u"Edytor kryteri\u00f3w", None))
        self.buttonAddCriteria.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.buttonRemoveCriteria.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144", None))
        ___qtablewidgetitem = self.criteriaTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nazwa", None));
        ___qtablewidgetitem1 = self.criteriaTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Kierunek", None));

        __sortingEnabled = self.criteriaTable.isSortingEnabled()
        self.criteriaTable.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.criteriaTable.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kryt1", None));
        ___qtablewidgetitem3 = self.criteriaTable.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Min", None));
        ___qtablewidgetitem4 = self.criteriaTable.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Kryt2", None));
        ___qtablewidgetitem5 = self.criteriaTable.item(1, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Min", None));
        self.criteriaTable.setSortingEnabled(__sortingEnabled)

        self.generationGroup.setTitle(QCoreApplication.translate("MainWindow", u"Generacja", None))
        self.buttonGenerate.setText(QCoreApplication.translate("MainWindow", u"Generuj", None))
        self.spinBoxObjectCount.setSuffix(QCoreApplication.translate("MainWindow", u" Liczba obiekt\u00f3w", None))
        self.buttonSort.setText(QCoreApplication.translate("MainWindow", u"Sortuj", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rozk\u0142ad", None))
        self.distributionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Gaussa", None))
        self.distributionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Eksponencjalny", None))
        self.distributionComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Poissona", None))

        self.valuesEditor.setTitle(QCoreApplication.translate("MainWindow", u"Edytor warto\u015bci", None))
        ___qtablewidgetitem6 = self.valuesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Kryt1", None));
        ___qtablewidgetitem7 = self.valuesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kryt2", None));
        self.actionsGroup.setTitle(QCoreApplication.translate("MainWindow", u"Akcje", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Algorytm", None))
        self.buttonSolve.setText(QCoreApplication.translate("MainWindow", u"Rozwi\u0105\u017c", None))
        self.buttonBenchmark.setText(QCoreApplication.translate("MainWindow", u"Benchmark", None))
        self.algorithmComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Bez filtracji", None))
        self.algorithmComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Z Filtracja", None))
        self.algorithmComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Punkt idealny", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Wprowadzanie danych", None))
        self.outputText.setPlainText(QCoreApplication.translate("MainWindow", u"Tutaj b\u0119d\u0105 wyniki", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Poka\u017c wykres", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Wyniki", None))
    # retranslateUi

