from shiny import App, render, ui
import pandas as pd
from pathlib import Path

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
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)
