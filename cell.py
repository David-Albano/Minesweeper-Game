import random
from tkinter import Button
import settings
import ctypes

class Cell:

    all_cells = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    cell_marked_count = settings.MINES_COUNT
    marked_cell_count_label_object = None

    points = 0
    points_count_label_object = None



    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_clicked = False
        self.is_marked = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all_cells.append(self)

    def create_btn_object(self, location, width, height):

        btn = Button(
            location,
            bg='#B2B2B2',
            width=width,
            height=height
        )
        # Event button
        btn.bind('<Button-1>', self.left_click_action) # Left click
        btn.bind('<Button-3>', self.right_click_action) # Right click
        self.cell_btn_object = btn

    def left_click_action(self, event):
        if not self.is_marked:
            if self.is_mine:
                self.show_mines()
            else:
                if self.count_cells_are_mines == 0:
                    for cell in self.get_cells_around:
                        cell.show_cell()
                        cell.cell_btn_object.configure(bg='#465881')
                        if cell.count_cells_are_mines == 0:
                            for cell in cell.get_cells_around:
                                cell.show_cell()
                                cell.cell_btn_object.configure(bg='#465881')
                                if cell.count_cells_are_mines == 0:
                                    for cell in cell.get_cells_around:
                                        cell.show_cell()
                                        cell.cell_btn_object.configure(bg='#465881')
                                        if cell.count_cells_are_mines == 0:
                                            for cell in cell.get_cells_around:
                                                cell.show_cell()
                                                cell.cell_btn_object.configure(bg='#465881')

                self.show_cell()

                if Cell.cell_count == settings.MINES_COUNT:
                    ctypes.windll.user32.MessageBoxW(0, 'Congrats! You are a great minsweeper!', 'YOU WIN!', 0)

    def get_cells(self, x, y):
        # Return a cell object based on the value of x, y
        for cell in Cell.all_cells:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def get_cells_around(self):
        cells_around = [
            self.get_cells(self.x - 1, self.y - 1),
            self.get_cells(self.x, self.y - 1),
            self.get_cells(self.x + 1, self.y - 1),
            self.get_cells(self.x - 1, self.y),
            self.get_cells(self.x + 1, self.y),
            self.get_cells(self.x - 1, self.y + 1),
            self.get_cells(self.x, self.y + 1),
            self.get_cells(self.x + 1, self.y + 1)
        ]

        cells_around = [cell for cell in cells_around if cell is not None]
        return cells_around

    @property
    def count_cells_are_mines(self):
        num_cell_mines_around = 0
        for cell in self.get_cells_around:
            if cell.is_mine:
                num_cell_mines_around += 1

        return num_cell_mines_around

    def show_cell(self):
        if not self.is_clicked:
            Cell.cell_count -= 1
            Cell.points += 1
            self.cell_btn_object.configure(bg='#465881')
            self.cell_btn_object.configure(text=self.count_cells_are_mines)
            # Replace the text of the cell clunt label with the newer counter
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f'Cells Left: {Cell.cell_count}'
                )
                Cell.points_count_label_object.configure(
                    text=f'Points: {Cell.points}'
                )
        # Mark the cell as clicked (Use it as the last line of this method)
        self.is_clicked = True

    def show_mines(self):
        for cell in Cell.all_cells:
            cell.cell_btn_object.unbind('<Button-1>')
            cell.cell_btn_object.unbind('<Button-3>')
            if cell.is_mine:
                cell.cell_btn_object.configure(bg='red', text='💣')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)

    def right_click_action(self, event):
        if not self.is_clicked:
            if not self.is_marked:
                if Cell.cell_marked_count > 0:
                    Cell.cell_marked_count -= 1
                    if Cell.marked_cell_count_label_object:
                        Cell.marked_cell_count_label_object.configure(text=f'Marking Clicks: {Cell.cell_marked_count}')
                    self.cell_btn_object.configure(bg='#FCC314', text='🏴')
                    self.is_marked = True
            else:
                if Cell.cell_marked_count >= 0:
                    Cell.cell_marked_count += 1
                    if Cell.marked_cell_count_label_object:
                        Cell.marked_cell_count_label_object.configure(text=f'Marking Clicks: {Cell.cell_marked_count}')
                    self.cell_btn_object.configure(bg='#B2B2B2', text='')
                    self.is_marked = False

    @staticmethod
    def randomize_mines():
        cell_are_mines = random.sample(Cell.all_cells, settings.MINES_COUNT)
        for cell_is_mine in cell_are_mines:
            cell_is_mine.is_mine = True

    @staticmethod
    def restart_game():
        for cell in Cell.all_cells:
            cell.cell_btn_object.configure(bg='#B2B2B2', text='')
            cell.is_mine = False
            cell.is_clicked = False
            cell.is_marked = False
            cell.cell_btn_object.bind('<Button-1>', cell.left_click_action)
            cell.cell_btn_object.bind('<Button-3>', cell.right_click_action)
        Cell.randomize_mines()
        Cell.cell_count = settings.CELL_COUNT
        Cell.cell_count_label_object.configure(text=f'Cells Left: {Cell.cell_count}')
        Cell.cell_marked_count = settings.MINES_COUNT
        Cell.marked_cell_count_label_object.configure(text=f'Marking Clicks: {Cell.cell_marked_count}')
        Cell.points = 0
        Cell.points_count_label_object.configure(text=f'Points: {Cell.points}')

    def __repr__(self):
        return f'Cell({self.x},{self.y})'

