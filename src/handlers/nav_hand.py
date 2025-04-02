from views import home, completed
def nav(page, selected_index):
    if selected_index == 0:
        home.home_view(page)
    elif selected_index == 1:
        completed.completed_view(page)
    page.update()
