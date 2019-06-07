
from .read_whitespace import read_whitespace
from peco.template import SentenceNode, Evaluatable, JoinNode


def read_join(preread, stream, parser):
    read_whitespace("", stream, parser)  # trim whitespace!
    sourcenode = None
    sentencenode = SentenceNode()
    while True:
        node = parser.read(stream)
        if isinstance(node, Evaluatable):
            sourcenode = node
            break
        sentencenode.add(node)
    return JoinNode(sentencenode.trim(), sourcenode)
