import dearpygui.dearpygui as dpg
from custom.Table import Table
import pandas as pd

dpg.create_context()

dpg.create_viewport(title='My App', width=600, height=400)

df = pd.read_feather("sort.feather")
column_widths = [120,400,30,50,50,30,30,30,30,30]


with dpg.font_registry():
    #bold
    dpg.add_font('font/Helvetica-Bold.ttf', 13, tag = 'small_x_bold')
    dpg.add_font('font/Helvetica-Bold.ttf', 15, tag = 'small_bold')
    dpg.add_font('font/Helvetica-Bold.ttf', 24, tag = 'medium_y_bold')
    dpg.add_font('font/Helvetica-Bold.ttf', 27, tag = 'medium_bold')
    dpg.add_font('font/Helvetica-Bold.ttf',30, tag = 'large_bold')
    dpg.add_font('font/Helvetica-Bold.ttf', 35, tag = 'large_x_bold')

    #normal
    dpg.add_font('font/Helvetica.ttf', 13, tag = 'small_x')
    dpg.add_font('font/Helvetica.ttf', 15, tag = 'small')
    dpg.add_font('font/Helvetica.ttf', 24, tag = 'medium_y')
    dpg.add_font('font/Helvetica.ttf', 27, tag = 'medium')
    dpg.add_font('font/Helvetica.ttf',30, tag = 'large')
    dpg.add_font('font/Helvetica.ttf', 35, tag = 'large_x')

    #combo
    dpg.add_font('font/Helvetica-Bold.ttf', 15, tag = 'combo_font')

with dpg.window(tag = "main",label="Example Window"):
    Table(
        width= 985,
        height= 500,
        columns= df.columns.tolist(),
        columns_width= column_widths,
        data= df.values.tolist(),
        data_font='small_x',
        header_color= (33, 17, 247),
        row_type= "readonly"
    ) #

dpg.set_primary_window("main", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
