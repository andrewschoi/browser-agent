from automation.llm.llm import LLM
from automation.action.action import Action
from html_parser.context_maker.semantics.base_semantic import Semantic


class Judge:
    def __init__(self, task):
        self.task = task

    def should_interact(self, semantic, url):
        assert isinstance(semantic, Semantic)
        action = Action(semantic=semantic, task=self.task, url=url)
        prompt = action.should_interact().yes_or_no().build()
        print(prompt)
        response = LLM().ask(prompt)
        print(response)
        return response
    
    def should_click(self, semantic, url):
        assert isinstance(semantic, Semantic)
        action = Action(semantic=semantic, task=self.task, url=url)
        prompt = action.should_click().yes_or_no().build()
        print(prompt)
        response = LLM().ask(prompt)
        print(response)
        return response

    def what_value(self, semantic, url):
        assert isinstance(semantic, Semantic)
        action = Action(semantic=semantic, task=self.task, url=url)
        prompt = action.what_value().answer_only().build()
        print(prompt)
        response = LLM().ask(prompt)
        print(response)
        return response
