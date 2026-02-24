from nicegui import ui, app
from class_demo.user_app.logic import AppLogic
from class_demo.user_service.service_exceptions import AuthenticationError, UnauthorizedError, ServiceError

# IMPORTS OMITTED

# Initialize app logic
logic = AppLogic()
logic.seed_admin()

def init_gui():
    """Build the GUI layout."""

    @ui.page('/login')
    def login_page():
        ''' code omitted '''

    @ui.page('/')
    def dashboard():
        ''' code omitted '''

    # Auto-redirect to login if not logged in
    ''' code omitted '''

if __name__ in {"__main__", "class_demo.user_app.gui"}:
    init_gui()
