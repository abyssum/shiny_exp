from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Input Widgets"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.h2("Output Widgets"),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)
