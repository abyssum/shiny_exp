# %% Package import
from shiny import App, render, ui
import pandas as pd
import numpy as np
from pathlib import Path

# %% Data prep
languages = pd.read_csv(Path(__file__).parent /'MostPopularProgrammingLanguages.csv')
# print(languages)
languages['dateTime'] = pd.to_datetime(languages['Date'])
languages.drop(axis=1,
               columns=['Date'],
               inplace=True)

languages_long = languages.melt(id_vars='dateTime',
                                value_name='popularity',
                                var_name='language').reset_index(drop=True)
languages_long

data_range_start = np.min(languages_long['dateTime'])
data_range_end = np.max(languages_long['dateTime'])

language_names = languages_long['language'].unique()
language_names_dict = {l:l for l in language_names}

# %% Front-end
app_ui = ui.page_fluid(
    ui.panel_title("Most Popular Proggramming Languages"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_selectize(id="language",
                            label="Languages",
                            choices=language_names_dict,
                            selected='Python',
                            multiple=2),
            ui.input_date_range(id='dateRange',
                                label='Date Range',
                                start=data_range_start,
                                end=data_range_end),
        ),
        ui.panel_main(
            ui.output_plot("plottimeseries"),
        )
    ),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)

# %%
