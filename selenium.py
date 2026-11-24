from seleniumbase import SB

# Start browser using SeleniumBase
with SB(uc=True, test=True, guest=True) as sb:

    # TikTok profile URL
    url = "https://www.tiktok.com/@startrek?lang=en"

    # Activate CDP mode and open TikTok
    sb.activate_cdp_mode(url)

    # Wait for the website to load
    sb.sleep(2.5)

    # Close popup if visible
    sb.click_if_visible('button[data-close-button="true"]')

    sb.sleep(0.3)

    # Extract TikTok profile bio
    print("*** " + sb.get_text('h2[data-e2e="user-bio"]'))

    # Click Refresh button if visible
    sb.click_if_visible('button:contains("Refresh")')

    sb.sleep(0.3)

    # Scroll down 33 times to load more content
    for i in range(33):
        sb.scroll_down()
        sb.sleep(0.03)

    # Find all image elements inside picture elements
    items = sb.find_elements("picture img")

    # Extract and print the alt attribute of each image
    for i, item in enumerate(items):
        print(" * %s: %s" % (i, str(item.get_attribute("alt"))))

    # Print total number of images found
    print("*** %s total items found!" % len(items))

    sb.sleep(1)
