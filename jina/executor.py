from jina import DocumentArray, Executor, requests


class neura(Executor):
    """"""
    @requests
    def foo(self, docs: DocumentArray, **kwargs):
        pass