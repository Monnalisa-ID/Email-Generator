__author__ = 'andrew.sielen'

from Elements.EmailModuleClass import EmailModule

class Intro(EmailModule):
    module_class = "intro"
    char = "%"
    html = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"><html>
    <head>
    <!--<style type="text/css">
        p {margin-bottom:0; margin:0}
    </style>-->
    <title></title>
    </head>
    <body>
    <table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="body-table" style="background: #FFFFFF;">
        <tr>
        <td align="center" valign="top">
        <table border="0" cellpadding="0" cellspacing="0" width="100%" id="current_email-container" style="background: #FFFFFF; max-width:600px; min-width:320px">
    """

class End(EmailModule):
    module_class = "end"
    char = "%"
    html = """
        </table>
        </td>
        </tr>
    </table>
    </body>
    </html>
    """

class Header(EmailModule):
    module_class = "header"
    char = "H"
    html = """
            <tr> <!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT}">
                    <tr>
                        <td align="center" valign="top" height="5px" colspan="2" style="background: #6bc048;" >
                        </td>
                    </tr>
                    <tr>
                        <td align="left" valign="top" height="47px" width="5%"  style="background: #FFFFFF;">&nbsp;</td>
                        <td align="left" valign="middle" height="47px" style="background: #FFFFFF;">
                            <img src="https://info.thismoment.com/rs/thismoment/images/TMTESTFOREMAILLogo.png"  height="21" width="152"/>
                        </td>
                    </tr>
                </table>
                </td>
            </tr> <!--End header [{CLASS} {COUNT}]-->
            """

class ImageHeader(EmailModule):
    module_class = "image-header"
    char = "I"
    html = """
            <tr> <!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="current_email-title">
                    <tr>
                        <td align="left" valign="middle" id="{CLASS}-{COUNT}-image" class="mktEditable">
                            <a href="{CTA LINK}{UTM}">
                                <img src="{IMAGE URL}" style="width:100%; display:block" />
                            </a>
                        </td>
                    </tr>
                </table>
                </td>
            </tr> <!--End [{CLASS} {COUNT}]-->
            """

    def __init__(self):
        super().__init__()
        self.c_vars['IMAGE URL'] = "http://placehold.it/600x200"
        self.c_vars['CTA LINK'] = "http://www.thismoment.com"

class NewsHeader(EmailModule):
    module_class = "news-header"
    char = "N"
    html = """
            <tr> <!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT}">
                    <tr>
                        <td align="center" valign="top" height="5" colspan="4" style="background: #6bc048;" >
                        </td>
                    </tr>
                    <tr>
                        <td align="left" valign="top" height="47" width="5%"  style="background: #FFFFFF;">&nbsp;</td>
                        <td align="left" valign="middle" height="47" style="background: #FFFFFF;">
                            <img src="https://info.thismoment.com/rs/thismoment/images/TMTESTFOREMAILLogo.png"  height="21" width="152"/>
                        </td>
                        <td align="right" valign="bottom">
                            <p style="margin-bottom:9px; font-size:10pt; color:#a4a8a8; font-weight:bold; font-family: 'Helvetica Neue','Helvetica', sans-serif" id="{CLASS}-Date-{COUNT}" class="mktEditable">{DATE}</p>
                        </td>
                        <td align="right" width="3%">
                        </td>
                    </tr>
                </table>
                </td>
            </tr> <!--End [{CLASS} {COUNT}]-->
            """

    def __init__(self):
        super().__init__()
        self.c_vars['DATE'] = "In The Know"

class Hero(EmailModule):
    module_class = "primary"
    char = "1"
    html = """
            <tr><!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT}">
                    <tr><td align="center" valign="top" width="100%" colspan="5" height="1" style="background-color:#d8dddd"></td></tr>
                    <tr>
                        <td align="center" valign="top" style="min-height:236px; max-height:295px; " colspan="5" id="email-hero-0" class="mktEditable" >
                            <a href="{CTA LINK}{UTM}"><!-- max 600 min 480-->
                                <img style="width: 100%; margin-bottom: 20px;" src="{IMAGE URL}" alt="{TITLE}">
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td width="7%">&nbsp;</td>
                        <td width="86%" align="center" valign="top" style="background: #FFFFFF;" colspan="3">
                            <div id="{CLASS}-{COUNT}-story" class="mktEditable" style="font-family: 'Helvetica Neue', Helvetica, sans-serif;">
                                <span style="font-size:24px; line-height:28px;  color:#252829;">
                                    {TITLE}
                                </span>
                                <div style="font-size:18px; line-height:25px; color:#666666;">
                                    {COPY}
                                </div>
                            </div>
                        </td>
                        <td width="7%">&nbsp;</td>
                    </tr>
                    <tr>
                        <td width="15%" colspan="2">&nbsp;</td>
                        <td width="70%" colspan="1" height="70">
                            <div align="center" id="{CLASS}-{COUNT}-cta" class="mktEditable" >
                                <a style="padding-top:15px; padding-bottom:15px; font-size: 18px; background: #6bc048; color: #fefefe; font-family: 'Helvetica Neue','Helvetica', sans-serif; text-decoration: none; height: 100%; width: 100%; display: block; text-align: center;" href="{CTA LINK}{UTM}">READ MORE</a>
                            </div>
                        </td>
                        <td width="15%"  colspan="2">&nbsp;</td>
                    </tr>
                    <tr>
                    <td width="100%" colspan="5" height="25">&nbsp;</td>
                    </tr>
                </table>
                </td>
            </tr> <!--End [{CLASS} {COUNT}]-->
        """
    def __init__(self):
        super().__init__()
        self.c_vars['IMAGE URL'] = "http://placehold.it/600x295"
        self.c_vars['TITLE'] = "The Rewards and Risks of UGC"
        self.c_vars['COPY'] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent varius hendrerit gravida. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aenean diam ipsum, volutpat at risus porta, tincidunt rhoncus lectus."
        self.c_vars['CTA LINK'] = "http://www.thismoment.com"

class Tips(EmailModule):
    module_class = "tips"
    char = "T"
    tip_html = """
                    <tr>
                    <td width="100%" colspan="5" height="35">&nbsp;</td>
                    </tr>
                    <tr> <
                        <td width="7%">&nbsp;</td>
                        <td width="86%" align="center" valign="top" style="background: #FFFFFF;" colspan="3">
                            <div id="{CLASS}-{COUNT}-{TIPCOUNT}" class="mktEditable" style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">
                                <div style="margin-bottom:25px">
                                    <img src="{TIP IMAGE {TIPCOUNT}}" alt="{TIP TITLE {TIPCOUNT}}" style="width:133px; height:133px;"/>
                                </div>
                                <span style="display:block; margin-bottom:17px; font-size:24px; line-height:28px; color:#252829;">
                                    {TIP TITLE {TIPCOUNT}}
                                </span>
                                <div style="font-size:18px; margin:0px; line-height:25px; color:#666666;">
                                    {TIP COPY {TIPCOUNT}}
                                </div>
                            </div>
                        </td>
                        <td width="7%">&nbsp;</td>
                    </tr> <!--Tip {TIPCOUNT}-->
    """

    html = """
            <tr><!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="current_email-tips">
                    <tr><td align="center" valign="top" width="100%" colspan="5" height="1px" style="background-color:#d8dddd"></td></tr>
                    {TIPS}
                    <tr>
                        <td colspan="3" height="35">
                        </td>
                    </tr>
                </table>
                </td>
            </tr> <!--End [{CLASS} {COUNT}]-->
    """

    def __init__(self):
        super().__init__()
        num_of_tips = int(input("How many tips? "))
        tips = ""
        for n in range(num_of_tips):
            tips += self.tip_html.replace("{TIPCOUNT}", str(n))
            self.c_vars['TIP IMAGE {}'.format(str(n))] = "http://placehold.it/133x133"
            self.c_vars['TIP TITLE {}'.format(str(n))] = "UGC Brand Marketing"
            self.c_vars['TIP COPY {}'.format(str(n))] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent varius hendrerit gravida."
        self.html = self.html.replace("{TIPS}", tips)

class CTA(EmailModule):
    module_class = "cta"
    char = "C"
    html = """
            <tr><!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top" style="background: #f4f6f7;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="current_email-cta">
                    <tr>
                        <td width="7%">&nbsp;</td>
                        <td width="86%" align="center" valign="top" colspan="3">
                            <div id="{CLASS}-{COUNT}" class="mktEditable" style="padding-top:25px; font-size:24px; line-height:30px; margin:0px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color:#828a8f;">
                                {COPY}
                            </div>
                        </td>
                        <td width="7%">&nbsp;</td>
                    </tr>
                    <tr>
                        <td width="15%" colspan="2">&nbsp;</td>
                        <td width="70%" colspan="1" height="70">
                            <div align="center" id="{CLASS}-{COUNT}-cta" class="mktEditable" >
                                <a style="padding-top:15px; padding-bottom:15px; font-size: 18px; background: #6bc048; color: #fefefe; font-family: 'Helvetica Neue','Helvetica','Arial',sans-serif; text-decoration: none; height: 100%; width: 100%; display: block; text-align: center;" href="{CTA LINK}{UTM}">READ MORE</a>
                            </div>
                        </td>
                        <td width="15%"  colspan="2">&nbsp;</td>
                    </tr>
                    <tr>
                    <td width="100%" colspan="5" height="35">&nbsp;</td>
                    </tr>
                </table>
                </td>
            </tr><!--End [{CLASS} {COUNT}]-->
        """
    def __init__(self):
        super().__init__()
        self.c_vars['COPY'] = "Find out how thismoment can help your team lorem ipsum dolor amet sit."
        self.c_vars['CTA LINK'] = "http://www.thismoment.com"

class Secondary(EmailModule):
    module_class = "story"
    char = "2"
    html = """
            <tr> <!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT}">
                    <tr><td align="center" valign="top" width="100%" colspan="5" height="1" style="background-color:#d8dddd"></td></tr> <!--hrule-->
                    <tr>
                        <td width="7%">&nbsp;</td>
                        <td width="86%" align="center" valign="top" style="background: #FFFFFF;" colspan="3">
                            <div id="{CLASS}-{COUNT}-copy" class="mktEditable" style="padding-top: 25px; font-family: Lato, Helvetica, Arial, sans-serif;">
                                <p style="margin-bottom:10px; font-size:24px; line-height:28px; margin:0px; color:#252829;">{TITLE}</p>
                                <div style="font-size:18px; line-height:25px; color:#666666; margin-bottom: 10px;">
                                    <p>{SCOPY} <br/><a style=" color: #3cc2d1; text-decoration: none;" href="{CTA LINK}{UTM}">Check it out.</a></p>


                                </div>
                                <div>
                                    <a href="{CTA LINK}{UTM}"><img src="{IMAGE URL}" style="border:1px solid #cccccc; width:260px; height:190px;"/></a>
                                </div>
                            </div>
                        </td>
                        <td width="7%">&nbsp;</td>
                    </tr>

                    <tr>
                        <td colspan="3" height="35">
                        </td>
                    </tr>
                </table>
                </td>
            </tr> <!--End [{CLASS} {COUNT}]-->
        """
    def __init__(self):
        super().__init__()
        self.c_vars['SCOPY'] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent varius hendrerit gravida. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."
        self.c_vars['TITLE'] = "The Future of Brand Engagement"
        self.c_vars['IMAGE URL'] = "http://placehold.it/260x190"
        self.c_vars['CTA LINK'] = "http://www.thismoment.com"

class Ternary(EmailModule):
    module_class = "ternary"
    char = "3"
    html = """
            <tr> <!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT}">
                    <tr><td align="center" valign="top" width="100%" colspan="5" height="1" style="background-color:#d8dddd"></td></tr> <!--hrule-->
                    <tr>
                        <td width="7%">&nbsp;</td>
                        <td width="86%" align="center" valign="top" style="background: #FFFFFF;" colspan="3">
                            <div id="{CLASS}-{COUNT}-copy" class="mktEditable" style="padding-top:35px; font-family: 'Helvetica Neue', Helvetica, sans-serif;">
                                <span style="font-size:24px; line-height:28px;  color:#252829;">
                                    {TITLE}
                                </span>
                                <div style="font-size:18px; line-height:25px; color:#666666;">
                                    {COPY}
                                </div>
                            </div>
                        </td>
                        <td width="7%">&nbsp;</td>
                    </tr>
                    <tr>
                        <td width="15%" colspan="2">&nbsp;</td>
                        <td width="70%" colspan="1" height="70">
                            <div align="center" id="{CLASS}-{COUNT}-cta" class="mktEditable" >
                                <a style="padding-top:15px; padding-bottom:15px; font-size: 18px; background: #6bc048; color: #fefefe; font-family: 'Helvetica Neue','Helvetica', sans-serif; text-decoration: none; height: 100%; width: 100%; display: block; text-align: center;" href="{CTA LINK}{UTM}">READ MORE</a>
                            </div>
                        </td>
                        <td width="15%"  colspan="2">&nbsp;</td>
                    </tr>
                    <tr>
                    <td width="100%" colspan="5" height="35">&nbsp;</td>
                    </tr>
                </table>
                </td>
            </tr> <!--End [{CLASS} {COUNT}]-->
        """
    def __init__(self):
        super().__init__()
        self.c_vars['TITLE'] = "Stay In The Know. Signup for Our Content Marketing Blog"
        self.c_vars['COPY'] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent varius hendrerit gravida. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."
        self.c_vars['CTA LINK'] = "http://www.thismoment.com"

class Copy(EmailModule):
    module_class = "copy"
    char = "A"
    html = """
            <tr> <!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT}">
                    <tr><td align="center" valign="top" width="100%" colspan="5" height="1" style="background-color:#d8dddd"></td></tr> <!--hrule-->
                    <tr>
                    <td width="100%" colspan="3" height="35">&nbsp;</td>
                    </tr>
                    <tr>
                        <td width="7%">&nbsp;</td>
                        <td align="left" valign="top">
                            <div id="{CLASS}-{COUNT}-copy" class="mktEditable" style="font-size:19px; line-height:24px; font-family: 'Helvetica Neue', Helvetica, sans-serif; color:#666666;">
                                <p style="font-size:22px; margin:0px; color:#252829;">
                                    Hi there {{lead.First Name}},
                                </p>
                                <p>
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent varius hendrerit gravida. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aenean diam ipsum, volutpat at risus porta, tincidunt rhoncus lectus.
                                </p>
                                <p>
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent varius hendrerit gravida. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aenean diam ipsum, volutpat at risus porta, tincidunt rhoncus lectus.
                                </p>
                                <p>Regards,</p>
                            </div>
                            <div class="mktEditable" id="{CLASS}-{COUNT}-sig" style="font-size: 19px; line-height: 24px; font-family: 'Helvetica Neue', Helvetica, sans-serif;">
                                <div style="color: #252829;">
                                    <p>Keith Abbey</p>
                                    <div><span style="font-style: italic; color: #666666;">Solutions Expert</span></div>
                                        <img src="https://info.thismoment.com/rs/thismoment/images/SmallLogoForTestEmail.png" style="margin-bottom: 10px; width:90px; height:13px; display:block;"/>
                                    <div style="font-size: 16px; line-height: 19px"><span style="color: #666666; font-weight:500;">E&nbsp;</span><a style="color: #3cc2d1; text-decoration: none;" href="mailto:keith.abbey@thismoment.com">&nbsp;keith.abbey@thismoment.com</a></div>
                                    <div style="font-size: 16px; line-height: 19px"><span style="color: #666666; font-weight:500;">P&nbsp;</span><a style=" color: #3cc2d1; text-decoration: none;" href="tel:14156847040">&nbsp;14156847040</a></div>
                                </div>
                            </div>

                        </td>
                        <td width="7%">&nbsp;</td>
                    </tr>
                    <tr>
                    <td width="100%" colspan="3" height="35">&nbsp;</td>
                    </tr>
                </table>
                </td>
            </tr> <!--End [{CLASS} {COUNT}]-->
        """

class Footer(EmailModule):
    module_class = "footer"
    char = "F"
    html = """
            <tr><!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT}">
                    <tr><td align="center" valign="top" width="100%" colspan="5" height="7" style="background-color:#d5dcdc"></td></tr>
                    <tr>
                        <td align="center" valign="top">
                            <div style="padding: 23px 0 18px 0">
                                <a href="https://www.facebook.com/Thismoment"><img style="margin: 0 5px 0 5px; height:34px; width:34px;" src="https://info.thismoment.com/rs/thismoment/images/2015-Email-Facebook.png" /></a>
                                <a href="https://twitter.com/Thismoment"><img style="margin: 0 5px 0 5px; height:34px; width:34px;" src="https://info.thismoment.com/rs/thismoment/images/2015-Email-Twitter.png" /></a>
                                <a href="https://www.linkedin.com/company/thismoment"><img style="margin: 0 5px 0 5px; height:34px; width:34px;" src="https://info.thismoment.com/rs/thismoment/images/2015-Email-Linkedin.png" /></a>
                            </div>
                        </td>
                    </tr>
                </table>
                </td>
            </tr><!--End [{CLASS} {COUNT}]-->
            """

class Legal(EmailModule):
    module_class = "legal"
    char = "L"
    html = """
            <tr> <!--Begin [{CLASS} {COUNT}]-->
                <td align="center" valign="top">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="{CLASS}-{COUNT}">
                    <tr>
                        <td align="center" valign="top">
                            <div style="font-size:12px; line-height: 16px; color:#252829; font-family: Lato, Helvetica, Arial, sans-serif;">
                                <div>
                                    Questions? <a style="color: #3cc2d1; text-decoration: none;" href="https://info.thismoment.com/contact-us.html">Contact Us.</a>
                                </div>
                                <div>
                                    Thismoment, 222 Kearny Street, Suite 500
                                </div>
                                <div>
                                    San Francisco, CA 94108
                                </div>
                                <div>
                                    <a style="color: #3cc2d1; text-decoration: none;" href="https://info.thismoment.com/Unsubscribe-Page.html">Unsubscribe</a> | <a style="color: #3cc2d1; text-decoration: none;" href="https://www.thismoment.com/privacy-policy/">Privacy Policy</a>
                                </div>
                            </div>
                        </td>
                    </tr>
                </table>
                </td>
            </tr> <!--End [{CLASS} {COUNT}]-->
    """

# class TEMP(EmailModule):
#     module_class = "temp"
#     html = """
#
#     """
#     def __init__(self):
# super().__init__()!--Tip {TIPCOUNT}-->


