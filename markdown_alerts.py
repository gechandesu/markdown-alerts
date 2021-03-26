"""Python-Markdown Admonition alternative extension
with a shortened syntax.
"""

__version__ = '0.1'

import re
import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor


# Patterns
alerts = {
    'info': r'::: *info',
    'note': r'::: *note',
    'tip': r'::: *tip',
    'success': r'::: *success',
    'warning': r'::: *warning',
    'danger': r'::: *danger'
}

default_config = {
    'info' : ['alert info', 'CSS class for Info block.'],
    'note' : ['alert note', 'CSS class for Note block.'],
    'tip' : ['alert tip', 'CSS class for Tip block.'],
    'success' : ['alert success', 'CSS class for Success block.'],
    'warning' : ['alert warning', 'CSS class for Warning block.'],
    'danger' : ['alert danger', 'CSS class for Danger block.'],
}

class AlertsBlockProcessor(BlockProcessor):

    def __init__(self, parser, alert, alert_css_class):
        self.parser = parser
        self.tab_length = parser.md.tab_length
        self.alert = alert
        self.alert_css_class = alert_css_class

    def test(self, parent, block):
        return re.match(alerts[self.alert], block)

    def run(self, parent, blocks):
        original_block = blocks[0]
        blocks[0] = re.sub(alerts[self.alert], '', blocks[0])

        for block_num, block in enumerate(blocks):
            if re.search(r' *\n?$', block):
                e = etree.SubElement(parent, 'div')
                e.set('class', self.alert_css_class)
                self.parser.parseBlocks(e, blocks[0:block_num + 1])
                for i in range(0, block_num + 1):
                    blocks.pop(0)
                return True
        blocks[0] = original_block
        return False

class AlertsExtension(Extension):

    def __init__(self, **kwargs):
        self.config = default_config
        super(AlertsExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        priority = 105
        for alert in alerts.keys():
            priority += 10
            md.parser.blockprocessors.register(
                AlertsBlockProcessor(md.parser, alert, self.getConfig(alert)),
                alert + '-alert',
                priority
            )

def makeExtension(**kwargs):
    return AlertsExtension(**kwargs)

if __name__ == '__main__':
    pass