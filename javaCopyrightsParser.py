import requests
import urllib
import re
from bs4 import BeautifulSoup

class JavaCopyrightsParser:
    def read_copyrigths(self, input_copyrights_url):
        if input_copyrights_url != 'empty2':
            url = urllib.request.urlopen(input_copyrights_url).read()
            soup = BeautifulSoup(url, 'html.parser')
            page_content = soup.get_text()
            wzor = '([[:space:]]|\*)*Copyright.*|^[[:space:]]*All rights reserved.*'

            dopas = re.search(wzor, page_content)
            if dopas != None:
                txt_start = dopas.start()
                txt_end = dopas.end()
                copyright = page_content[txt_start:txt_end]
                copyright_split = copyright.split(",")
                join_string = ""
                try:
                    copyright = join_string.join(copyright_split)
                except:
                    copyright = copyright
            else:
                copyright = "No copyrights"

        else:
            copyright = 'Copyright: Unknown.'

        return copyright



