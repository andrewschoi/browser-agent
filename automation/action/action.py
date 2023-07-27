class Action:
    def __init__(self, url, semantic, task):
        self.url = url
        self.semantic = semantic
        self.task = task
        self.action = f"""
        we are trying to '{self.task}' in the browser:
        we on this url {self.url}
        we see the html element {str(self.semantic)}
        """

    def should_interact(self):
        self.action += f"\ndo we need to interact with this to accomplish {self.task}"
        return self

    def yes_or_no(self):
        self.action += f"\nyour response should be a one letter lowercase letter y or n"
        return self

    def answer_only(self):
        self.action += f"\nyour response should only include the value that should go in the field"
        return self

    def what_value(self):
        self.action += f"\nwhat value should go in this HTML field"
        return self

    def should_click(self):
        self.action += f"\nshould we click this element?"
        return self

    def build(self):
        return self.action
