XPATH = '/html/body/pre'
driver_path = "chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

LIMIT = 5000
TEMPLATE = "cricketer"

page_db_links = [f"https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/Template:Infobox_{TEMPLATE}&limit={LIMIT}",
f"https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/Template:Infobox_{TEMPLATE}&limit={LIMIT}&offset=0%7C10772761&dir=next",
f"https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/Template:Infobox_{TEMPLATE}&limit={LIMIT}&offset=0%7C31908654&dir=next",
f"https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/Template:Infobox_{TEMPLATE}&limit={LIMIT}&offset=0%7C47194264&dir=next",
f"https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/Template:Infobox_{TEMPLATE}&limit={LIMIT}&offset=0%7C52685839&dir=next",
f"https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/Template:Infobox_{TEMPLATE}&limit={LIMIT}&offset=0%7C61362839&dir=next",
f"https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/Template:Infobox_{TEMPLATE}&limit={LIMIT}&offset=0%7C67121666&dir=next"]