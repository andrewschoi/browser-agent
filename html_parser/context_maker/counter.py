class AttemptFailureException(Exception):
    pass


class Counter:
    """
    A simple representation of progress.

    Example usage:
        counter = Counter(tasks_remaining=1)

        @counter.attempt
        def click_submit():
            <some code...>

        click_submit()

        #if click_submit() is successful (no exception is thrown)
        print(counter.is_finished()) # should print True, otherwise False

    """

    def __init__(self, tasks_remaining):
        self._tasks_remaining = tasks_remaining

    @property
    def tasks_remaining(self):
        return self._tasks_remaining

    def is_finished(self):
        return self._tasks_remaining == 0

    def attempt(self, func):
        def raise_exception_if_fail(*args, **kwargs):
            try:
                self._tasks_remaining -= 1
                return func(*args, **kwargs)
            except Exception as e:
                self._tasks_remaining += 1
                raise AttemptFailureException()

        return raise_exception_if_fail
