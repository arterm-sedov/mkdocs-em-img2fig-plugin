# plugin.py

import re

from mkdocs.plugins import BasePlugin

class Image2FigurePlugin(BasePlugin):

    def on_page_markdown(self, markdown, **kwargs):
      
        pattern = re.compile(r'\*!\[(.*?)\]\((.*?)\)\*', flags=re.IGNORECASE)
        
        markdown = re.sub(pattern,
            r'<figure class="figure-image">\n' + \
            r'  ![\1](\2)\n' + \
            r'  <figcaption>\1</figcaption>\n' + \
            r'</figure>',                        
            markdown)            

        return markdown
