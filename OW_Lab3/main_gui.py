from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys

import numpy as np
import matplotlib.pyplot as plt

from gui_main_window import Ui_MainWindow  # Import the generated UI class
import utils
import algorithms

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the UI from the generated class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Populate the main window with the UI elements
        
        self.connect_ui_elements()

        # Create a comparison counter
        self._compariser = utils.ComparisonCounter()

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

        # Connect buttons to methods
        self.ui.buttonSolve.clicked.connect(self.run_solve)
        self.ui.buttonBenchmark.clicked.connect(self.run_benchmark)


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
            self._data_X = utils.Gauss(criteria_count, object_count, param1, param2)
        elif distribution_type == "Eksponencjalny":
            self._data_X = utils.Exponential(criteria_count, object_count, param1)
        elif distribution_type == "Poissona":
            self._data_X = utils.Poisson(criteria_count, object_count, param1)

        print(self._data_X)

        # Call the method to display the generated data in valuesTable
        self.display_data_in_values_table()


    def display_data_in_values_table(self):
        """Display the generated data in the valuesTable."""
        # Clear existing data in valuesTable
        self.ui.valuesTable.setRowCount(0)  # Clear any existing rows
        self.ui.valuesTable.setColumnCount(self._data_X.shape[1])  # Set the column count based on data

        # Populate the table with the data
        for row_idx in range(self._data_X.shape[0]):
            self.ui.valuesTable.insertRow(row_idx)  # Insert a new row for each data point
            for col_idx in range(self._data_X.shape[1]):
                item = QTableWidgetItem(f"{self._data_X[row_idx, col_idx]:.4f}")  # Convert the data to string
                self.ui.valuesTable.setItem(row_idx, col_idx, item)  # Set the item in the table


    def run_solve(self):
        """
        Handles the solve button click event.
        Executes the selected algorithm from the combo box.
        """
        selected_algorithm = self.ui.algorithmComboBox.currentText()  # Get the selected algorithm from comboBox
        
        # Prepare data for the algorithm
        data = self._data_X  # Assuming _data is defined and contains the necessary points

        if selected_algorithm == "Bez filtracji":
            result_dict, out_text = utils.run_algorithm(data, algorithms.naive_nondominated_sort, compariser=self._compariser, algorithm_name="Bez filtracji")
        elif selected_algorithm == "Z Filtracja":
            result_dict, out_text = utils.run_algorithm(data, algorithms.nondominated_sort_with_filtering, compariser=self._compariser, algorithm_name="Z Filtracja")
        elif selected_algorithm == "Punkt idealny":
            result_dict, out_text = utils.run_algorithm(data, algorithms.ideal_point_algorithm, compariser=self._compariser, algorithm_name="Punkt idealny")
        else:
            print("Unknown algorithm selected.")
            return
        self._results = [result_dict]
        self.output_text(out_text)
        
    
    def run_benchmark(self):
        """
        Handles the benchmark button click event.
        Executes all three algorithms and measures their performance.
        """
        data = self._data_X  # Assuming _data is defined and contains the necessary points
        algorithm_list = [
            (algorithms.naive_nondominated_sort, "Bez filtracji"),
            (algorithms.nondominated_sort_with_filtering, "Z Filtracja"),
            (algorithms.ideal_point_algorithm, "Punkt idealny"),
        ]
        
        self._results = []
        out_text_all  = f"Liczba punktów:   {len(data)}\n"
        out_text_all += f"Liczba kryteriów: {len(data[0])}\n\n"

        for algorithm, name in algorithm_list:
            self._compariser.reset_counters()  # Reset comparison counter for each algorithm
            result_dict, out_text = utils.run_algorithm(data, algorithm, compariser=self._compariser, algorithm_name=name)
            self._results.append(result_dict)
            # Add results of one algorithm to output
            out_text_all += out_text + "\n"
            
        # Add comparison table
        out_text_all += utils.algorithm_summary_table_string(self._results)
        # Display all results in outputText
        self.output_text(out_text_all)
        


    def refresh_plot(self):
        self.ui.mpl_widget.axis.clear()  # Clear any existing plot
        
        X = np.array(self._data_X)
        P_nondominated = np.array(self._results[0]["nondominated_points"])
        
        num_criteria = X.shape[1]
        
        if num_criteria == 2:
            # Plotowanie 2D
            self.ui.mpl_widget.set_projection_2D()
            self.ui.mpl_widget.axis.scatter(X[:, 0], X[:, 1], c='skyblue', label='Zbiór punktów')
            self.ui.mpl_widget.axis.scatter(P_nondominated[:, 0], P_nondominated[:, 1], c='red', label='Punkty niezdominowane', s=100, edgecolor='k')
            
            self.ui.mpl_widget.axis.set(xlabel='Kryt. 1',
                                        ylabel='Kryt. 2',
                                        title='Wizualizacja punktów z zaznaczonymi punktami niezdominowanymi (2D)')
            self.ui.mpl_widget.axis.legend()
            self.ui.mpl_widget.axis.grid()
        elif num_criteria == 3:
            # Plotowanie 3D
            self.ui.mpl_widget.set_projection_3D()
            self.ui.mpl_widget.axis.scatter(X[:, 0], X[:, 1], X[:, 2], c='skyblue', label='Zbiór punktów')
            self.ui.mpl_widget.axis.scatter(P_nondominated[:, 0], P_nondominated[:, 1], P_nondominated[:, 2], c='red', label='Punkty niezdominowane', s=100, edgecolor='k')
            
            self.ui.mpl_widget.axis.set(xlabel='Kryt. 1',
                                        ylabel='Kryt. 2',
                                        zlabel='Kryt. 3',
                                        title='Wizualizacja punktów z zaznaczonymi punktami niezdominowanymi (3D)')
            self.ui.mpl_widget.axis.legend()
        else:
            self.ui.mpl_widget.set_projection_2D()
            self.ui.mpl_widget.axis.text(0.5, 0.5, "Brak możliwości wykresu przy wymiarach większych od 3D", ha='center', va='center')
        
        self.ui.mpl_widget.canvas.draw()  # Render the updated plot

    def output_text(self, text):
        self.ui.outputText.setPlainText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())