__author__ = 'andrew.sielen'

from bs4 import BeautifulSoup
from selenium import webdriver

from Elements.playlist_modules import *


class Playlist(EmailModule):
    module_class = "playlist"
    char = "p"

    class Header(EmailModule):
        module_class = "playlist-header"
        html = """
            <tr> <!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT} mktEditable" id="{CLASS}-{COUNT}">
                    <tr>
                        <td align="center" valign="top" height="3" style="background: #999999;" >
                        </td>
                    </tr>
                    <tr>
                        <td align="left" valign=" middle" height="40"  style="background: #FAFAFA; padding-bottom: 10px; padding-left:10px;" >
                            <p style="margin-bottom:7px; font-size:16pt; color:#555555; font-family: Lato, Helvetica, Arial, sans-serif">{TITLE}</p>
                        </td>
                    </tr>
                </table>
                </td>
            </tr> <!--End [{CLASS} {COUNT}]-->

            <tr> <!--Start playlist-->
            <td align="center" valign="top" style="background: #FAFAFA;">
            <div style="max-width:{MAXWIDTH}; min-width:300px; /*overflow-y:scroll; height:480px;*/ border-radius: 22px; border-bottom: 30px solid #333333; border-top: 30px solid #333333; border-left: 5px solid #333333; border-right: 5px solid #333333;">
            <table border="0" cellpadding="0" cellspacing="0" width="100%" style=" border-spacing:15px; border-colapse:separate; background: #FAFAFA;">
        """


    class Footer(EmailModule):
        module_class = "playlist-footer"
        html2 = """
            </table>
            </td>
            </tr>
        """
        html = """
            </table>
            </div>
            </td>
            </tr>

                <tr> <!--Begin [{CLASS} {COUNT}]-->
                    <td align="center" valign="top">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT} mktEditable" id="{CLASS}-{COUNT}">
                        <tr>
                            <td height="20" style="background: #FAFAFA;" ></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" height="3" style="background: #999999;" >
                            </td>
                        </tr>
                    </table>
                    </td>
                </tr> <!--End [{CLASS} {COUNT}]-->
        """

    def __init__(self, url=None, num_cards=0):
        super().__init__()
        if url is None:
            url = input("What is the playlist url? ")
        self.c_vars['URL'] = url
        self.c_vars['TITLE'] = "Check out our latest playlist: "
        self.c_vars['MAXWIDTH'] = '400px'
        self.c_vars['SCREENHEIGHT'] = '480px'
        self.num_cards = num_cards  # The number of cards to render. 0 is all

        self.html = ""
        self.setup_playlist()

    def setup_playlist(self):
        self.parse_playlist(self.scrape_playlist())

    def scrape_playlist(self):
        """
            Open the playlist and do a base scrape to get the playlist html
        :return: The html of the playlist
        """
        print("Scraping the playlist")
        source_url = soupify(self.c_vars['URL'])
        return source_url.find_all("article")

    def parse_playlist(self, playlist_html):
        """
            Take the html from scrape playlist and turn it into a list of cards with data
        :return: A dictionary in the format [1={cardtype=TYPE,var1=VAR1..
        """
        print("Parsing the playlist")

        def get_first_three_words(string):
            """Simply returns the first three words, using it to match with the card/class type"""
            return " ".join(string[:3])

        working_list = []
        working_class = None
        for idx, card_soup in enumerate(playlist_html):
            class_string = get_first_three_words(card_soup['class'])
            try:
                working_class = self.card_types[class_string]
            except KeyError:
                continue  # If the class isn't in the list. We are not going to add it to the 'playlist', continue to the next

            working_list.append(
                working_class(card_soup))  # Build the card, how to build each card is defined in the card class itself
        self.cards = working_list


    def __str__(self):
        self.html = self.build_playlist()
        html = super().__str__()
        return html

    def build_playlist(self):
        """
            Take the list and build email modules from it
        :return: the playlsit with modules
        """
        print("Building the playlist")
        working_html = ""
        working_html += self.Header.html
        for card in self.cards:
            working_html += card.get_html()
        see_live = PL_SeeLiveCard()
        working_html += see_live.get_html()
        working_html += self.Footer.html
        return working_html

    def get_html(self):
        return self.__str__()

    def edit(self):
        """
            Rebuild the playlist by scraping the url
        :return:
        """
        super().edit()
        self.setup_playlist()

    card_types = {
        "card app tm-sxswpromo": PL_PromoCard,
        "card photo publish-this": PL_NewsCard,
    }


def soupify(url):
    """
        Take the url and return the source code. Need to use webdrive because the playlists are dynamically generated by javascript
    """
    driver = webdriver.Firefox()
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page)
    return soup


if __name__ == "__main__":
    def test_playlist_creator():
        url = input("What playlist url? ")
        playlist = Playlist(url)


    test_playlist_creator()