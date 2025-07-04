from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Password"),
    # ui.input_slider(id="n",
    #                 label="N",
    #                 min=0,
    #                 max=100,
    #                 value=[20, 30],
    #                 animate=True),
    # ui.input_checkbox(id = "check", 
    #                   label = "Check", value=True),
    # ui.input_numeric(id = "num", 
    #                   label = "Num",
    #                   min=10, max=30, value=25, step=5),
    # ui.input_radio_buttons(id="ch_grp",
    #                         label="Choice Boxes",
    #                         choices=["Choise1", "Choise2"], selected="Choise1"),
    ui.input_date_range(id="date",
                  label="Choice Date"),
    # ui.input_password(id="txt_inp",
    #              label="TXT input"),
    ui.h2("Show password"),
    ui.input_checkbox(id="ch_bx",
                      label="Show password"),
    ui.output_text_verbatim("txt")
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"{input.txt_inp()}"


app = App(app_ui, server)
