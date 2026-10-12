import dearpygui.dearpygui as dpg
import itertools


class Table:
    def __init__(
            self,
            width:int,
            height:int,
            columns: list[str],
            columns_width: list[float],
            data: list[list[str]],
            data_font:str,
            header_color:tuple[int],
            row_type:str 
            ):
            #row_type """selectable_row,selectable_col,readonly"""

        with dpg.theme() as table_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg,(0,0,0,0))
                dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg,header_color)

        with dpg.table(clipper = True,width=width,height=height,row_background=True,scrollY = True,resizable = True,freeze_rows = 1) as table:
            for column, col_width in zip(columns,columns_width):
                dpg.add_table_column(label = column, init_width_or_weight= col_width)

            if row_type == "selectable_row":
                for rows in data :
                    with dpg.table_row():
                        for column in rows:
                            dpg.add_selectable(label=column,span_columns=True)

            elif row_type == "selectable_row":
                for rows in data :
                    with dpg.table_row():
                        for column in rows:
                            dpg.add_input_text(default_value=column, readonly = True, width = 1000,auto_select_all = True)

            elif row_type == "readonly":
                for rows in data :
                    with dpg.table_row():
                        for column in rows:
                            dpg.add_text(default_value=column)

            for rows in data :
                with dpg.table_row():
                    for column in rows:
                        dpg.add_input_text(default_value=column, readonly = True, width = 1000,auto_select_all = True)

        dpg.bind_item_theme(table,table_theme)
        dpg.bind_item_font(table,data_font)

 
  