__author__ = 'andrew.sielen'

from bs4 import BeautifulSoup
from selenium import webdriver

from EmailModuleClass import EmailModule


class Playlist(EmailModule):
    module_class = "playlist"
    letter = "p"

    class Image___(EmailModule):
        module_class = "playlist-image"
        html = """
                <tr> <!--Begin [{CLASS} {COUNT}]-->
                    <td align="center" valign="top" style="border:1px solid lightgrey; box-shadow: 3px 3px 3px #888888;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                        <tr>
                            <td align="left" valign="middle">
                                <a href="{URL}">
                                    <img src="{IMAGE}" style="width:100%; display:block"/>
                                </a>
                            </td>
                        </tr>
                    </table>
                    </td>
                </tr> <!--End [{CLASS} {COUNT}]-->
        """

        def __init__(self, card_soup):
            super().__init__()
            self.c_vars['URL'] = "http://www.thismoment.com"
            self.c_vars['IMAGE'] = "https://thismoment-a.akamaihd.net/media/tmupload/e61d5bf067c613f6/LogoTitlecard.png"

    class NewsCard(EmailModule):
        module_class = "playlist-news"
        html = """
                <tr><!--Begin [{CLASS} {COUNT}]-->
                    <td align="center" valign="top" style="border:1px solid lightgrey; background:#ffffff; box-shadow: 3px 3px 3px #888888; ">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%">

                        <tr>
                            <td height="20" colspan="3"></td>
                        </tr>

                        <tr>
                            <td width="20">&nbsp;</td>
                            <td align="left" valign="top" style="background: #FFFFFF;">
                                <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif;">
                                    <span style="font-size:16px; line-height:18px; font-weight:bold; color:#333333;">
                                        {TITLE}
                                    </span>
                                </div>
                            </td>
                            <td width="20">&nbsp;</td>
                        </tr>

                        <tr>
                            <td align="center" valign="top" style="padding-top:20px; padding-left:20px; padding-right:20px; min-height:236px; max-height:295px;" colspan="3" >
                                <a href="{URL}">
                                    <img style="width: 100%; margin-bottom: 20px;" src="{IMAGE}" alt="{TITLE}" >
                                </a>
                            </td>
                        </tr>

                        <tr>
                            <td width="15">&nbsp;</td>
                            <td align="left" valign="top" style="background: #ffffff;">
                                <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif;">
                                    <div style="font-size:14px; line-height:15px; color:#555555;">
                                        <p>{COPY}</p>
                                    </div>
                                </div>
                            </td>
                            <td width="15">&nbsp;</td>
                        </tr>

                        <tr>
                            <td width="10">&nbsp;</td>
                            <td>
                                <div align="left">
                                    <a style="padding-top: 10px; font-size: 16px; color: #c4c6c7; font-family: 'Helvetica Neue','Helvetica', sans-serif; text-decoration: none; display: block;" href="{URL}">Read Article</a>
                                </div>
                            </td>
                            <td width="10">&nbsp;</td>
                        </tr>

                        <tr>
                            <td height="20" colspan="3"></td>
                        </tr>
                    </table>
                    </td>
                </tr> <!--End [{CLASS} {COUNT}]-->
        """

        def __init__(self, card_soup):
            super().__init__()

            # Get title
            card_text_tag = card_soup.find("div", {"class": "headline"})
            self.c_vars['TITLE'] = card_text_tag.find("h1").text

            #Get content
            card_copy_tag = card_soup.find("div", {"class": "row"})

            #Get image details
            card_image_tag = card_copy_tag.find("div", {"class": "tm-media"})
            self.c_vars['URL'] = card_image_tag.find("a")["href"]
            self.c_vars['IMAGE'] = card_image_tag.find("img")["src"]

            #Get Copy
            card_text_tag = card_copy_tag.find("div", {"class": "meta"})
            self.c_vars['COPY'] = card_text_tag.find("p").text

    class PromoCard(EmailModule):
        module_class = "playlist-image-promo"
        html = """
                <tr><!--Begin [{CLASS} {COUNT}]-->
                    <td align="center" valign="top" style="border:1px solid lightgrey; background:#ffffff; box-shadow: 3px 3px 3px #888888;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%">

                        <tr>
                            <td align="center" valign="top" colspan="3" style="min-height:236px; max-height:295px;" >
                                <a href="{URL}">
                                    <img style="width: 100%; display:block;" src="{IMAGE}">
                                </a>
                            </td>
                        </tr>

        """

        html_copy_segment = """
                        <!--Start Optional Text block-->
                        <tr><td height="10" colspan="3"></td></tr>
                        <tr>
                            <td width="10">&nbsp;</td>
                            <td align="left" valign="top" style="background: #FFFFFF;">
                                <div id="primary-1-story" style="font-family: 'Helvetica Neue', Helvetica, sans-serif;">
                                    <span style="font-size:16px; line-height:20px;  color:#333333; font-weight:bold;">
                                        {TITLE}
                                    </span>
                                    <div style="font-size:14px; line-height:16px; color:#555555;">
                                        <p>{COPY}</p>
                                    </div>
                                </div>
                            </td>
                            <td width="10">&nbsp;</td>
                        </tr>
                        <tr><td height="10" colspan="3"></td></tr>
                        <!--End Optional Text block-->
        """

        html_end = """
                    </table>
                    </td>
                </tr> <!--[{CLASS} {COUNT}]-->
        """

        def __init__(self, card_soup):
            super().__init__()
            # Get image details
            card_image_tag = card_soup.find("div", {"class": "tm-media"})
            if card_image_tag is None: raise ResourceWarning
            self.c_vars['IMAGE'] = card_image_tag.find("img")["src"]
            self.c_vars['URL'] = card_image_tag.find("a")["href"]

            #Get text if there is any
            card_text_tag = card_soup.find("div", {"class": "meta"})
            if card_text_tag is None:
                self.html += self.html_end
                return
            else:
                self.html += self.html_copy_segment  # Add the html for the copy part of the card
                self.html += self.html_end
            temp_tag = card_text_tag.find("h1")
            self.c_vars['TITLE'] = card_text_tag.find("h1").text
            self.c_vars['COPY'] = card_text_tag.find("p", {"class": "full-text"}).text

    class TwitterCard(EmailModule):
        pass

    class SeeLiveCard(EmailModule):
        module_class = "see-it-live"
        html = """
                <tr> <!--Begin [{CLASS} {COUNT}]-->
                    <td align="center" valign="top" style="border:1px solid lightgrey; box-shadow: 3px 3px 3px #888888; background: #ffffff;">

                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td colspan="2" height="30" style="background:#4b4353;"></td>
                                <td rowspan="2" width="60" height="60" align="center" valign="top" >
                                    <img src="https://info.thismoment.com/rs/thismoment/images/email-playlist-phone.jpg" style="height:60px; width:60px;"/>
                                </td>
                                <td colspan="2" height="30" style="background:#4b4353;"></td>
                            </tr>
                            <tr>
                                <td colspan="2" height="30" style="background:#ffffff;"></td>
                                <td colspan="2" height="30" style="background:#ffffff;"></td>
                            </tr>
                        </table>

                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td width="20"></td>
                                <td align="center" valign="bottom" style="font-family: sans-serif; font-size:16px; line-height:18px; color:#555555;">
                                    {TITLE}
                                </td>
                                <td width="20"></td>
                            </tr>
                            <tr><td colspan="3" height="10"></td></tr>
                            <tr>
                                <td width="20"></td>
                                <td ><div style="font-size:19px; line-height:24px; font-family:'Helvetica Neue', Helvetica, Arial, sans-serif; " ><a style="padding-top: 15px; padding-bottom: 15px; font-size: 18px; background: #6bc048; color: #fefefe; font-family: 'Helvetica Neue','Helvetica','Arial',sans-serif; text-decoration: none; height: 100%; width: 100%; display: block; text-align: center;" href="{URL}">{CTA}</a></div></td>
                                <td width="20"></td>
                            </tr>
                            <tr><td colspan="3" height="10"></td></tr>
                        </table>

                    </td>
                </tr> <!--End [{CLASS} {COUNT}]-->
        """

        def __init__(self, url):
            super().__init__()
            self.c_vars['TITLE'] = "Like what you see?"
            self.c_vars['CTA'] = "See this playlist live!"
            self.c_vars['URL'] = url

    class Header(EmailModule):
        module_class = "playlist-header"
        html = """
            <tr> <!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT} mktEditable" id="{CLASS}-{COUNT}">
                    <tr>
                        <td align="center" valign="top" height="5" style="background: #999999;" >
                        </td>
                    </tr>
                    <tr>
                        <td align="left" valign="center" height="40"  style="background: #FAFAFA; padding-top: 10px; padding-left: 10px;" >
                            <p style="margin-bottom:7px; font-size:16pt; color:#555555; font-family: Lato, Helvetica, Arial, sans-serif">{TITLE}</p>
                        </td>
                    </tr>
                </table>
                </td>
            </tr> <!--End [{CLASS} {COUNT}]-->

            <tr> <!--Start playlist-->
            <td align="center" valign="top" style="background: #FAFAFA">
            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:400px; min-width:300; border-spacing:15px; border-colapse:separate; background: #FAFAFA; ">
        """


    class Footer(EmailModule):
        module_class = "playlist-footer"
        html = """
            </table>
            </td>
            </tr>

                <tr> <!--Begin [{CLASS} {COUNT}]-->
                    <td align="center" valign="top">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT} mktEditable" id="{CLASS}-{COUNT}">
                        <tr>
                            <td height="40"  style="background: #FAFAFA;" ></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" height="5" style="background: #999999;" >
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
        self.c_vars['TITLE'] = "Check out our playlist: "
        self.num_cards = num_cards  # The number of cards to render. 0 is all
        self.cards = {}
        self.html = """"""
        self.playlist_html = []  # List of all the "article" tags in the html. To make it easy to rebuild
        self.scrape_playlist()
        self.parse_playlist()

    def scrape_playlist(self):
        """
            Open the playlist and do a base scrape to get the playlist html
        :return: The html of the playlist
        """
        print("Scraping the playlist")
        source_url = soupify(self.c_vars['URL'])
        self.playlist_html = source_url.find_all("article")

    def parse_playlist(self):
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
        for idx, card_soup in enumerate(self.playlist_html):
            class_string = get_first_three_words(card_soup['class'])
            try:
                working_class = self.card_types[class_string]
            except KeyError:
                continue  # If the class isn't in the list. We are not going to add it to the 'playlist', continue to the next

            working_list.append(
                working_class(card_soup))  # Build the card, how to build each card is defined in the card class itself
        self.cards = working_list


    def __str__(self):
        html = self.build_playlist()
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
        see_live = self.SeeLiveCard()
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
        pass

    card_types = {
        "card app tm-sxswpromo": PromoCard,
        "card photo publish-this": NewsCard,
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


def test_playlist_creator():
    url = input("What playlist url? ")
    playlist = Playlist(url)


test_playlist_creator()