import requests
import urllib
import re
from bs4 import BeautifulSoup

class JavaCopyrightsParser:
    def read_copyrigths(self, input_copyrights_url):
        if len(input_copyrights_url) > 10:
            url = urllib.request.urlopen(input_copyrights_url).read()
            soup = BeautifulSoup(url, 'html.parser')
            page_content = soup.get_text()
            pattern = '([[:space:]]|\*)*Copyright.*|^[[:space:]]*All rights reserved.*'

            finding = re.search(pattern, page_content)
            if finding != None:
                txt_start = finding.start()
                txt_end = finding.end()
                copyright = page_content[txt_start:txt_end]
                copyright_split = copyright.split(",")
                join_string = ""
                try:
                    copyright = join_string.join(copyright_split)
                except:
                    copyright = copyright
            else:
                copyright = "Copyright: Unknown."

        else:
            copyright = 'Copyright: Unknown.'

        return copyright



