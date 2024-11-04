from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys
from gui_main_window import Ui_MainWindow  # Import the generated UI class

import numpy as np
import utils

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the UI from the generated class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Populate the main window with the UI elements
        
        self.connect_ui_elements()

        # Access UI elements
        # self.ui.myButton.clicked.connect(self.on_button_click)

    # def on_button_click(self):
    #     print("Button clicked!")
    def connect_ui_elements(self):
        # Connect buttons to functions
        self.ui.plotButton.clicked.connect(self.refresh_plot)
        self.ui.buttonGenerate.clicked.connect(self.generate_data)

        # Connect button signals to the methods
        self.ui.buttonAddCriteria.clicked.connect(self.add_criteria)
        self.ui.buttonRemoveCriteria.clicked.connect(self.remove_criteria)


    def add_criteria(self):
        """Add a new row to the criteria table with name 'KrytN' and default value 'Min'."""
        # Get the current row count to determine the next criteria number
        row_count = self.ui.criteriaTable.rowCount()

        # Insert a new row at the end of the table
        self.ui.criteriaTable.insertRow(row_count)

        # Set the name and default direction
        criterion_name = f"Kryt{row_count + 1}"  # Kryt1, Kryt2, ...
        criterion_direction = "Min"  # Default value

        # Add the new items to the table
        self.ui.criteriaTable.setItem(row_count, 0, QTableWidgetItem(criterion_name))
        self.ui.criteriaTable.setItem(row_count, 1, QTableWidgetItem(criterion_direction))

        # Update valuesTable columns based on removed criteria
        self.update_values_table_columns()


    def remove_criteria(self):
        """Remove the last row from the criteria table if there is more than one row."""
        row_count = self.ui.criteriaTable.rowCount()
        
        # Only remove a row if there's more than two left
        if row_count > 2:
            self.ui.criteriaTable.removeRow(row_count - 1)

            # Update valuesTable columns based on removed criteria
            self.update_values_table_columns()
            

    def update_values_table_columns(self):
        """Synchronize the columns of valuesTable with the criteria names from criteriaTable."""
        # Get the number of rows in criteriaTable to know how many columns we need
        criteria_count = self.ui.criteriaTable.rowCount()

        # Set the number of columns in valuesTable to match the number of criteria
        self.ui.valuesTable.setColumnCount(criteria_count)

        # Update column headers in valuesTable to match criteria names
        for i in range(criteria_count):
            criterion_name_item = self.ui.criteriaTable.item(i, 0)  # Fetch criterion name from criteriaTable
            if criterion_name_item:
                criterion_name = criterion_name_item.text()
            else:
                criterion_name = f"Kryt{i + 1}"  # Fallback name in case of missing data
            self.ui.valuesTable.setHorizontalHeaderItem(i, QTableWidgetItem(criterion_name))


    def generate_data(self):
        # Get the number of rows in criteriaTable to know how many columns we need
        criteria_count = self.ui.criteriaTable.rowCount()
        # Get the number of rows in valuesTable to know how many rows we need
        object_count = self.ui.spinBoxObjectCount.value()

        distribution_type = self.ui.distributionComboBox.currentText()
        param1 = self.ui.spinBoxDistributionParam1.value()
        param2 = self.ui.spinBoxDistributionParam2.value()

        if distribution_type == "Gaussa":
            self._data = utils.Gauss(criteria_count, object_count, param1, param2)
        elif distribution_type == "Eksponencjalny":
            self._data = utils.Exponential(criteria_count, object_count, param1)
        elif distribution_type == "Poissona":
            self._data = utils.Poisson(criteria_count, object_count, param1)

        print(self._data)

    def refresh_plot(self):
        self.ui.mpl_widget.axis.clear()  # Clear any existing plot
        self.ui.mpl_widget.axis.plot(self._data)  # Plot new data
        self.ui.mpl_widget.canvas.draw()  # Render the updated plot

    def output_text(self, output_text):
        self.ui.outputText.setPlainText(output_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())