# plugin.py

import re

from mkdocs.plugins import BasePlugin

class Image2FigurePlugin(BasePlugin):

    def on_page_markdown(self, markdown, **kwargs):
      
        pattern = re.compile(r'((_)|\*)!\[(.*?)\]\((.*?)\)(?(2)_|\*)', flags=re.IGNORECASE)
        
        markdown = re.sub(pattern,
            r'<figure markdown>![\3](\4)<figcaption>\3</figcaption></figure>',                        
            markdown)            

        return markdown
