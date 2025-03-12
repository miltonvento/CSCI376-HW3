from nicegui import ui

ui.colors(
      primary='#FF9601',
      secondary='#E2C896',
      accent='#D49E56',
      positive='#a2e0b0',
      negative='#f26676',
      info='#91c2cc',
      warning='#F2C037'
)

DEFAULT_VALUE = 32

def convert_card1():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result1_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result1_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result1_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: sets the text color to the one described by the hex code assigned to "positive" in ui.colors
    except ValueError:
        result1_label.set_text("Please enter a valid number.")
        result1_label.classes("text-lg font-semibold !text-negative mt-4")
        # text-negative: sets the text color to the one described by the hex code assigned to "negative" in ui.colors

def convert_card2():

    try: 
        temp = float(slider_value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result2_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result2_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result2_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: sets the text color to the one described by the hex code assigned to "positive" in ui.colors
    except ValueError:
        result2_label.set_text("Please enter a valid number.")
        result2_label.classes("text-lg font-semibold !text-negative mt-4")
        # text-negative: sets the text color to the one described by the hex code assigned to "negative" in ui.colors

slider_value = DEFAULT_VALUE
def on_slider_change(event):
    global slider_value 
    slider_value = event.value
    value_label.set_text(slider_value)

with ui.row().classes("mx-auto"):
    with ui.card().classes("w-150 h-200 py-6 px-8 shadow-xl mx-auto mt-10 rounded-xl border border-orange-200 hover:shadow-2xl bg-purple-50"):
        # w-100: Set element width to be fixed at 100
        # p-6: sets an element's padding on all four sides to 6
        # shadow-xl: set's the element's shadow to extra large
        # mx-auto: sets the left and right margin automatically (usually resulting in the element being placed in the middle)
        # mt-10: sets the element's top margin to 10
        # rounded-xl: sets the element's corner radius extra large
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
        # text-2xl: sets font size to extra extra large
        # font-bold: sets font weight to bold
        # text-accent: text-negative: sets the text color to the one described by the hex code assigned to "accent" in ui.colors 
        # mb-4: sets the bottom margin to 4
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
        # w-full: sets the width to its maximum length
        # border: adds a border to the element
        # rounded: makes the element's corners rounded
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert_card1).classes("text-white font-bold py-2 px-4 mx-auto rounded")
        # text-white: sets text color to white
        # py-2: sets the top and bottom margins to 2
        # px-4: sets the left and right margins to 4
        result1_label = ui.label("").classes("text-lg mt-4")

    with ui.card().classes("w-150 py-6 px-8 shadow-xl mx-auto mt-10 rounded-xl border border-orange-200 hover:shadow-2xl bg-red-50"):
        # w-100: Set element width to be fixed at 100
        # p-6: sets an element's padding on all four sides to 6
        # shadow-xl: set's the element's shadow to extra large
        # mx-auto: sets the left and right margin automatically (usually resulting in the element being placed in the middle)
        # mt-10: sets the element's top margin to 10
        # rounded-xl: sets the element's corner radius extra large
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
        # text-2xl: sets font size to extra extra large
        # font-bold: sets font weight to bold
        # text-accent: text-negative: sets the text color to the one described by the hex code assigned to "accent" in ui.colors 
        # mb-4: sets the bottom margin to 4
        # w-full: sets the width to its maximum length
        # border: adds a border to the element
        # rounded: makes the element's corners rounded

        value_label = ui.label(slider_value).classes("mx-auto text-xl pb-3")
        slider = ui.slider(min=-30, max=110, value=32, on_change= on_slider_change).classes("mb-1")

        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert_card2).classes("text-white font-bold py-2 px-4 mx-auto rounded")
        # text-white: sets text color to white
        # py-2: sets the top and bottom margins to 2
        # px-4: sets the left and right margins to 4
        result2_label = ui.label("").classes("text-lg mt-4")

ui.run()