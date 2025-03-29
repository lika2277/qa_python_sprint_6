class Accordion:
    def __init__(self, items = [], panels = []):
        self.items = items
        self.panels = panels

    def click(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError
        self.items[index].click()

    def is_panel_visible(self, index):
        if index < 0 or index >= len(self.panels):
            raise IndexError
        return self.panels[index].is_visible()