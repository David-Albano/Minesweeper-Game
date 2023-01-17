import math

from cell import Cell
from tkinter import *
from utils import *
import settings
import sys

root = Tk()
# Anular as difinições da janela
root.configure(bg='#243763')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

# Altura y largura adaptáveis

top_frame_width_percentagem = 97
top_frame_height_percentagem = 14

top_frame_width = width_set(top_frame_width_percentagem)
top_frame_height = height_set(top_frame_height_percentagem)

top_frame = Frame(
    root,
    bg='#495579',
    width=top_frame_width,
    height=top_frame_height
)
x_top_frame = width_set(100-top_frame_width_percentagem) / 2
y_top_frame = 10
top_frame.place(x=x_top_frame, y=y_top_frame)

game_title = Label(
    top_frame,
    bg='#495579',
    fg='#fff',
    text='Minessweeper Game',
    font=('', 30)
)

game_title.place(
    x=top_frame_width / 3, y=top_frame_height // 5
)

# Altura y largura adaptáveis

left_frame_width_percentagem = 15
left_frame_height_percentagem = height_set(100-top_frame_height_percentagem - y_top_frame / 2)

left_frame_width = width_set(left_frame_width_percentagem)
left_frame_height = left_frame_height_percentagem

left_frame = Frame(
    root,
    bg='#B2B2B2',
    width=left_frame_width,
    height=left_frame_height
)

y_left_frame = height_set(top_frame_height_percentagem) + y_top_frame * 2
left_frame.place(x=x_top_frame, y=y_left_frame)


center_frame_width_percentagem = 100 - left_frame_width_percentagem - x_top_frame / 3
center_frame_height_percentagem = left_frame_height_percentagem

center_frame_width = math.ceil(width_set(center_frame_width_percentagem))
center_frame_height = math.ceil(center_frame_height_percentagem)

center_frame = Frame(
        root,
        bg='#243763',
        width=center_frame_width,
        height=center_frame_height
    )

x_center_frame = (x_top_frame * 2) + width_set(left_frame_width_percentagem)
center_frame.place(x=x_center_frame, y=y_left_frame)

for row in range(settings.NUM_ROWS):
    for column in range(settings.NUM_COLUMNS):

        c = Cell(column, row)
        c.create_btn_object(center_frame, 6, 2)
        c.cell_btn_object.grid(
            column=column,
            row=row
        )

Cell.randomize_mines()

lbl = Label(
            left_frame,
            text=f'Cells Left: {settings.CELL_COUNT}',
            bg='#243763',
            fg='#fff',
            font=('', 10),
            width=14,
            height=3
        )
Cell.cell_count_label_object = lbl
Cell.cell_count_label_object.place(x=9, y=10)

lbl_marked_cells = Label(
            left_frame,
            text=f'Marking Clicks: {settings.MINES_COUNT}',
            bg='#243763',
            fg='#fff',
            font=('', 10),
            width=14,
            height=3
        )
Cell.marked_cell_count_label_object = lbl_marked_cells
Cell.marked_cell_count_label_object.place(x=9, y=100)

lbl_points_cells = Label(
            left_frame,
            text=f'Points: {Cell.points}',
            bg='#0B8457',
            fg='#fff',
            font=('', 10),
            width=14,
            height=3
        )
Cell.points_count_label_object = lbl_points_cells
Cell.points_count_label_object.place(x=9, y=220)

btn_restart = Button(
        left_frame,
        bg='#1C4B82',
        text='Reiniciar',
        width=14,
        height=2,
        command=Cell.restart_game
    )
btn_restart.place(x=13, y=340)

btn_quit = Button(
    left_frame,
    bg='orange',
    text='Quit',
    width=14,
    height=2,
    command=sys.exit
)
btn_quit.place(x=13, y=430)

# Executar a janela
root.mainloop()
