


with ui.card().classes('absolute-center w-80 items-stretch'):

    # SETUP UI ELEMENTS
    ui.label('Login').classes('text-h5 self-center')
    email = ui.input('Email'
                     ).on('keydown.enter', lambda: login())
    password = ui.input('Password', password=True, password_toggle_button=True
                        ).on('keydown.enter', lambda: login())
    
    # DEFINE LOGIN FUNCTION
    async def login():
            '''omitted here'''

    # login function needs to be defined before this line
    ui.button('Login', on_click=login).classes('w-full')


#-----------------------------------------------------------

    # DEFINE LOGIN FUNCTION
    async def login():
        if logic.login(email.value, password.value):
            ui.notify(f'Welcome, {logic.current_user.name}!', color='positive')
            ui.navigate.to('/')
        else:
            ui.notify('Invalid email or password', color='negative')