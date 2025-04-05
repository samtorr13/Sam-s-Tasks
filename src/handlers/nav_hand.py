from views import home, completed, settings
def nav(page, selected_index):
    if selected_index == 0:
        home.home_view(page)
    elif selected_index == 1:
        completed.completed_view(page)
    elif selected_index == 2:
        settings.settings_view(page)
    page.update()
