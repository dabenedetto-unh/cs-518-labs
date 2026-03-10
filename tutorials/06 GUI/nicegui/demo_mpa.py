from nicegui import ui

# --- Page 1: The Table ---
@ui.page('/')
def table_page():
    
    rows = [
        {'name': 'New York', 'lat': 40.7119, 'lon': -74.0027},
        {'name': 'London', 'lat': 51.5074, 'lon': -0.1278},
        {'name': 'Tokyo', 'lat': 35.6863, 'lon': 139.7722},
    ]

    ui.label('Select a city to view on the map:').classes('text-h6')
    
    # We use ui.navigate.to to move between pages
    # columns=columns, 
    ui.table(rows=rows, row_key='name').on(
        'rowClick', 
        lambda e: ui.navigate.to(f'/map/{e.args[1]["lat"]}/{e.args[1]["lon"]}')
    )

# --- Page 2: The Map ---
@ui.page('/map/{lat}/{lon}')
def map_page(lat: float, lon: float):
    ui.label(f'Location: {lat}, {lon}').classes('text-h6')
    
    # Initialize the map
    ui.leaflet(center=(lat, lon), zoom=10).classes('h-64 w-full')
    
    ui.link('Back to table', '/').classes('mt-4 inline-block')

ui.run()