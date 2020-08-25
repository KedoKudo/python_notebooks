from __code.table_handler import TableHandler
from __code.bragg_edge.bragg_edge_peak_fitting_gui_utility import GuiUtility
from qtpy import QtGui


class MarchDollase:

	def __init__(self, parent=None):
		self.parent = parent
		self.table_ui = self.parent.ui.march_dollase_user_input_table

	def table_clicked(self, row=None, column=None):
		nbr_row = self.table_ui.rowCount()

		enabled_up_button = True
		enabled_down_button = True

		if row == 0:
			enabled_up_button = False
		if row == (nbr_row - 1):
			enabled_down_button = False

		self.parent.ui.march_dollase_user_input_up.setEnabled(enabled_up_button)
		self.parent.ui.march_dollase_user_input_down.setEnabled(enabled_down_button)
		self.parent.ui.march_dollase_user_input_table.setFocus()

	def get_row_selected(self):
		o_table = TableHandler(table_ui=self.parent.march_dollase_user_input_table)
		row_selected = o_table.get_row_selected()
		return row_selected

	def move_row_up(self):
		self.move_table_row(to_row_offset=-1)

	def move_row_down(self):
		self.move_table_row(to_row_offset=+1)

	def move_table_row(self, to_row_offset=-1):
		"""
		:param to_row_offset: +1 means moving row to the next row, -1 means moving up by one row
		"""
		row_selected = self.get_row_selected()
		march_dollase_fitting_history_table = self.parent.march_dollase_fitting_history_table
		row_to_move = march_dollase_fitting_history_table.pop(row_selected)

		new_row = row_selected + to_row_offset

		march_dollase_fitting_history_table.insert(new_row, row_to_move)
		self.parent.march_dollase_fitting_history_table = march_dollase_fitting_history_table

		o_gui = GuiUtility(parent=self.parent)
		o_gui.fill_march_dollase_table(list_state=self.parent.march_dollase_fitting_history_table,
		                               list_initial_parameters=self.parent.march_dollase_fitting_initial_parameters)

		# keep current selection on new row
		o_table = TableHandler(table_ui=self.parent.march_dollase_user_input_table)
		o_table.select_row(row=new_row)
		self.table_clicked(row=new_row)

	def table_right_clicked(self):

		table_is_empty = False
		list_state = self.parent.march_dollase_fitting_history_table
		if not list_state:
			table_is_empty = True

		menu = QtGui.QMenu(self.parent)

		insert_row = None

		insert_above = None
		insert_below = None
		duplicate_row = None
		delete_row = None

		if table_is_empty:
			insert_row = menu.addAction("Insert Row")

		else:
			insert_above = menu.addAction("Insert Row Above")
			insert_below = menu.addAction("Insert Row Below")
			menu.addSeparator()
			duplicate_row = menu.addAction("Duplicate Row")
			menu.addSeparator()
			delete_row = menu.addAction("Remove Row")

		action = menu.exec_(QtGui.QCursor.pos())

		if action == insert_above:
			self.insert_row_above()
		elif action == insert_below:
			self.insert_row_below()
		elif action == duplicate_row:
			self.duplicate_row()
		elif action == delete_row:
			self.delete_row()
		elif action == insert_row:
			self.insert_row()

	def insert_row(self):
		march_dollase_fitting_history_table = list()
		new_entry = self.parent.march_dollase_fitting_history_table_default_new_row
		march_dollase_fitting_history_table.insert(0, new_entry)
		self.parent.march_dollase_fitting_history_table = march_dollase_fitting_history_table
		self.update_table_after_changing_row(changing_row=0)

	def insert_row_above(self):
		o_table = TableHandler(table_ui=self.parent.ui.march_dollase_user_input_table)
		row_selected = o_table.get_row_selected()
		march_dollase_fitting_history_table = self.parent.march_dollase_fitting_history_table
		new_entry = [False for _entry in march_dollase_fitting_history_table[0]]
		march_dollase_fitting_history_table.insert(row_selected, new_entry)
		self.parent.march_dollase_fitting_history_table = march_dollase_fitting_history_table
		self.update_table_after_changing_row(changing_row=row_selected+1)

	def insert_row_below(self):
		o_table = TableHandler(table_ui=self.parent.ui.march_dollase_user_input_table)
		row_selected = o_table.get_row_selected()
		march_dollase_fitting_history_table = self.parent.march_dollase_fitting_history_table
		new_entry = [False for _entry in march_dollase_fitting_history_table[0]]
		march_dollase_fitting_history_table.insert(row_selected+1, new_entry)
		self.parent.march_dollase_fitting_history_table = march_dollase_fitting_history_table
		self.update_table_after_changing_row(changing_row=row_selected+2)

	def duplicate_row(self):
		o_table = TableHandler(table_ui=self.parent.ui.march_dollase_user_input_table)
		row_selected = o_table.get_row_selected()
		march_dollase_fitting_history_table = self.parent.march_dollase_fitting_history_table
		new_entry = march_dollase_fitting_history_table[row_selected]
		march_dollase_fitting_history_table.insert(row_selected, new_entry)
		self.parent.march_dollase_fitting_history_table = march_dollase_fitting_history_table
		self.update_table_after_changing_row(changing_row=row_selected+1)

	def delete_row(self):
		o_table = TableHandler(table_ui=self.parent.ui.march_dollase_user_input_table)
		row_selected = o_table.get_row_selected()
		march_dollase_fitting_history_table = self.parent.march_dollase_fitting_history_table
		march_dollase_fitting_history_table.pop(row_selected)
		self.parent.march_dollase_fitting_history_table = march_dollase_fitting_history_table
		self.update_table_after_changing_row(changing_row=row_selected)

	def update_table_after_changing_row(self, changing_row=-1):
		o_gui = GuiUtility(parent=self.parent)
		o_gui.fill_march_dollase_table(list_state=self.parent.march_dollase_fitting_history_table,
		                               list_initial_parameters=self.parent.march_dollase_fitting_initial_parameters)

		# keep current selection on new row
		o_table = TableHandler(table_ui=self.parent.march_dollase_user_input_table)
		o_table.select_row(row=changing_row-1)
		self.table_clicked(row=changing_row)