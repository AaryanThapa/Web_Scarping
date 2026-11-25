from seleniumbase import SB
with SB(uc=True, demo=True) as sb:
    sb.driver.get("https://seleniumbase.io/simple/login")
    sb.type("#username","demo_user")
    sb.type("#password","secret_pass")
    sb.click('a:contains("Sign in")')
    sb.assert_exact_text("Welcome!","h1")
    sb.assert_element("img#image1")
    sb.highlight("image1")
    sb.click_link("Sign out")
    sb.assert_text("signed out","#top_message")


from seleniumbase import BaseCase
BaseCase.main(__name__, __file__, "--uc")
