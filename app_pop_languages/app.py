# %% Package import
from shiny import App, render, ui, reactive
import pandas as pd
import numpy as np
from pathlib import Path
from plotnine import ggplot, aes, geom_line, theme, element_text, labs

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
            ui.output_plot("plotTimeseries"),
        )
    ),
)


def server(input, output, session):
    
    @reactive.Calc
    def lang_filt():
        data_selected_start = pd.to_datetime(input.dateRange()[0])
        data_selected_end = pd.to_datetime(input.dateRange()[1])
        lang_filt = languages_long.loc[(languages_long['language'].isin(list(input.language()))) &
                                       (languages_long['dateTime'] >= data_selected_start) &
                                       (languages_long['dateTime'] <= data_selected_end)].reset_index(drop=True)
        return lang_filt

    @output
    @render.plot
    def plotTimeseries():
        g = ggplot(lang_filt()) + aes(x = 'dateTime',
                                    y = 'popularity',
                                    color = 'language') + geom_line() + theme(
                                        axis_text_x=element_text(
                                            rotation=90,
                                            hjust=1
                                        )
                                    ) + labs(
                                        x='Date',
                                        y='Popularity [%]',
                                        title='Language Popularity over Time'
                                    )
        return g


app = App(app_ui, server)

