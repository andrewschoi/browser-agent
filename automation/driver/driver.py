from automation.browser.browser import BrowserSingleton
from automation.judge.judge import Judge
import time


class Driver:
    def __init__(self, browser, judge, entry_point):
        assert isinstance(browser, BrowserSingleton)
        assert isinstance(judge, Judge)

        self.browser = browser
        self.judge = judge
        self.entry_point = entry_point

    def start(self):
        self.browser.go(self.entry_point)
        while True:
            self.browser.refresh_page()
            page = self.browser.page()
            url = self.browser.url()
            try:
                interactables = page.interactables
                for semantic in interactables:
                    y_or_n_should_interact = self.judge.should_interact(semantic=semantic, url=url)
                    if y_or_n_should_interact == "n":
                        continue

                    if semantic.clickable:
                        y_or_n_should_click = self.judge.should_click(
                            semantic=semantic, url=url
                        )
                        if y_or_n_should_click == "y":
                            self.browser.click(semantic=semantic)
                    if semantic.typeable:
                        value = self.judge.what_value(semantic=semantic, url=url)
                        self.browser.type(semantic=semantic, content=value)
            except KeyboardInterrupt:
                self.stop()
                break
            except Exception as e:
                print(e)
                time.sleep(5)
                continue

    def stop(self):
        self.browser.close()
