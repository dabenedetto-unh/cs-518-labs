from nicegui import ui

def example2():
    '''
    ## 2. The "Hello World" (The Basics)

    NiceGUI uses a declarative style. You define elements, and they appear in the order they are called.
    '''

    ui.label('Hello, NiceGUI!')
    ui.button('Click Me', on_click=lambda: ui.notify('Button Pressed!'))


def example3():
    '''
    ## 3. Core Concepts: Layout & Styling

    NiceGUI uses **Tailwind CSS** for styling. You don't need to write CSS files; you just pass classes directly to the elements.
    '''

    with ui.row().classes('w-full justify-center'):
        with ui.card().classes('p-8 bg-blue-50'):
            ui.label('User Profile').classes('text-h4')
            ui.input(label='Username', placeholder='Enter name')
            ui.checkbox('Remember Me')
            ui.button('Save', color='green')

def ex4():
    '''
    ## 4. Interactivity: Data Binding

    This is where NiceGUI shines. You can bind UI elements directly to Python variables or dictionaries. When the variable changes, the UI updates automatically.
    '''


    # A simple data object
    data = {'name': 'Gemini', 'count': 0}

    ui.label().bind_text_from(data, 'name', backward=lambda n: f'Hello, {n}!')

    with ui.row():
        ui.input(label='Edit Name').bind_value(data, 'name')
        
        # Increment counter
        ui.button('Add', on_click=lambda: (setitem(data, 'count', data['count'] + 1)))
        ui.label().bind_text_from(data, 'count', backward=lambda c: f'Count: {c}')

    # Helper for the lambda
    def setitem(d, k, v): d[k] = v

# example2()
# example3()
ex4()
ui.run()
