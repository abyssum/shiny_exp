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

# %%
app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)

# %%
