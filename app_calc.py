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
    # Here we denonstrat how to load in some data (eg. user input from range)
    # and perform calculation without the need to re-load the same data several times.
    @reactive.Calc
    def reactive_n():
        return input.n() # reactive expression that updates when input.n() changes.

    def reactive_result(mult): #  function that performs the calculation we want, based on the latest reactive_n() value
        return f"n*{mult} is {reactive_n() * mult}"

    @output
    @render.text
    def result1(): # output that calls reactive_result with specific n (here 2)
        return reactive_result(2)
    
    @output
    @render.text
    def result2(): # 2nd output that calls reactive_result with specific n (here 5)
        return reactive_result(5)


app = App(app_ui, server)
