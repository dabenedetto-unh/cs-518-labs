
    @ui.page('/')
    def dashboard():

        if not logic.current_user:
            ui.navigate.to('/login')
            return

        with ui.header().classes('items-center'):
            
            '''HEADER
            header has logout button'''

        with ui.tabs() as tabs:
            profile_tab = ui.tab('My Profile')
            if logic.current_user.role == 'admin':
                admin_tab = ui.tab('Admin Panel')

        with ui.tab_panels(tabs, value=profile_tab).classes('w-full'):
            with ui.tab_panel(profile_tab):
                ui.label('Your Information').classes('text-h6')
                with ui.card().classes('w-full max-w-sm'):

                    '''PROFILE / UPDATE FORM'''

            if logic.current_user.role == 'admin':
                with ui.tab_panel(admin_tab):
                    ui.label('User Directory').classes('text-h6')
                    
                    ''' USER LISTING TABLE
                    Each row has a DELETE USER button'''

                    ui.separator().classes('my-4')
                    ui.label('Create New User').classes('text-h6')
                    
                    ''' CREATE NEW USER FORM'''
