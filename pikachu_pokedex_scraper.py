import pandas as pd
from seleniumbase import SB

PIKACHU_IMG = 'img[src*="img/pokedex/detail/025.png"]'

with SB(uc=True, test=True, locale="en", ad_block=True) as sb:
    sb.activate_cdp_mode()
    sb.goto("https://www.pokemon.com/us/pokedex")
    sb.sleep(2)
    sb.click_if_visible("#onetrust-accept-btn-handler",
                        timeout=2)  # cookie popup
    sb.sleep(1.5)

    # scroll down until Pikachu's card is on the page
    for _ in range(30):
        if sb.is_element_present(PIKACHU_IMG):
            break
        sb.scroll_down(30)
        # "Load more" button, if shown
        sb.click_if_visible("a#loadMore", timeout=1)
        sb.sleep(1)
    else:
        raise Exception("Pikachu was not found on the page")

    sb.scroll_into_view(PIKACHU_IMG)
    sb.sleep(1)
    sb.click(PIKACHU_IMG)

    # now on Pikachu's detail page
    sb.wait_for_element("div.pokemon-ability-info")
    sb.scroll_into_view("div.pokemon-ability-info")
    sb.sleep(1)

    data = {"Name": sb.get_text('div[class*="title"]').replace("\n", " ")}

    titles = sb.select_all("div.pokemon-ability-info span.attribute-title")
    values = sb.select_all("div.pokemon-ability-info span.attribute-value")
    for t, v in zip(titles, values):
        data.setdefault(t.text.strip(), v.text.strip())

    data["Version"] = sb.get_text("label.styled-select")
    data["Description"] = sb.get_text("div.version-descriptions p.active")

df = pd.DataFrame([data])
df.to_csv("pikachu.csv", index=False, encoding="utf-8-sig")
print(df.T)
