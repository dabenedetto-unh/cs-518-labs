from nicegui import ui

class CounterApp:
    def __init__(self):
        self.value = 0
        
    def increment(self):
        self.value += 1
        self.label.set_text(f'Total: {self.value}')
        
    def reset(self):
        self.value = 0
        self.label.set_text('Total: 0')
        ui.notify('Counter Reset', type='warning')

app = CounterApp()

with ui.column().classes('items-center mt-10'):
    ui.icon('analytics', size='lg').classes('text-primary')
    app.label = ui.label('Total: 0').classes('text-2xl font-bold')
    
    with ui.row():
        ui.button('Increment', on_click=app.increment).props('elevated')
        ui.button('Reset', on_click=app.reset, color='red').props('outline')

ui.run(title='My Counter App')