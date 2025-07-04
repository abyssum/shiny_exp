from shiny import App, render, ui, reactive

app_ui = ui.page_fluid(
    ui.h2("Reacitvity"),
    ui.input_slider(id="n",
                    label="N",
                    min=0,
                    max=100,
                    value=20),
    ui.output_text_verbatim("result1"),
    ui.output_text_verbatim("result2"),
)


def server(input, output, session):
    @reactive.Calc
    def reactive_n():
        return input.n()

    def reactive_result(mult):
        return f"n*{mult} is {reactive_n() * mult}"

    @output
    @render.text
    def result1():
        return reactive_result(2)
    
    @output
    @render.text
    def result2():
        return reactive_result(5)


app = App(app_ui, server)
