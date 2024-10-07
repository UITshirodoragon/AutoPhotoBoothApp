

class TemplateMenuModel:
    def __init__(self) -> None:
        self.template_path_list = []
        for i in range(1, 9):
            self.template_path_list.append(f"Data/Template/template{i}.png")

