__author__ = 'andrew.sielen'

from Elements.EmailModuleClass import EmailModule


class PL_NewsCard(EmailModule):
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

        # Get content
        card_copy_tag = card_soup.find("div", {"class": "row"})

        #Get image details
        card_image_tag = card_copy_tag.find("div", {"class": "tm-media"})
        self.c_vars['URL'] = card_image_tag.find("a")["href"]
        self.c_vars['IMAGE'] = card_image_tag.find("img")["src"]

        #Get Copy
        card_text_tag = card_copy_tag.find("div", {"class": "meta"})
        self.c_vars['COPY'] = card_text_tag.find("p").text


class PL_PromoCard(EmailModule):
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

        # Get text if there is any
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


class PL_TwitterCard(EmailModule):
    pass


class PL_SeeLiveCard(EmailModule):
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

    def __init__(self):
        super().__init__()
        self.c_vars['TITLE'] = "Like what you see?"
        self.c_vars['CTA'] = "See this playlist live!"

