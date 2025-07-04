from shiny import App, render, ui
import pandas as pd
from pathlib import Path
from shinywidgets import output_widget, register_widget, reactive_read

# Import dataset
temperatures = pd.read_csv(Path(__file__).parent / "temperatures.csv")

# Define values for drop-down menu
countries = temperatures['Country'].unique().tolist()

# Define values for slider
temp_years = temperatures['Year'].unique()
temp_year_min = temp_years.min()
temp_year_max = temp_years.max()

# CSS defs
font_style = 'font-wight: 100'

app_ui = ui.page_fluid(
    ui.h2("Climate Change", style=font_style),
    ui.row(
        ui.column(
            6, ui.input_select(
                id='country',
                label='Choose a country',
                choices=countries
            )
        ),
        ui.column(
            6, 
            ui.row(
                ui.input_slider(
                    id='year',
                    label='Choose a year',
                    min=temp_year_min,
                    max=temp_year_max,
                    value=temp_year_min,
                    step=1,
                    animate=False
                ),
                ui.column(6, ui.output_ui('color_map'))
            )
        )
    ),
    ui.row(
        ui.column(6, ui.output_plot('graph_country')),
        ui.column(6, output_widget('map')),
    ),
    ui.br(),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        pass


app = App(app_ui, server)
