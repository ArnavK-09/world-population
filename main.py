# Imports 
from taipy.gui import Gui, Markdown
from taipy import Core

# All pages
from pages.insights import insights_page
from pages.dataset import dataset_page
from pages.pie import pie_page
from pages.top_countries_in_continent import top_countries_in_continent
from pages.country_overview import country_overview_page

# Configuring Routes 
ROUTES = {
    'insights': insights_page,
    'country_overview': country_overview_page,
    'top_countries_in_continent': top_countries_in_continent,
    'pie_charts': pie_page,
    'dataset': dataset_page,
}

# Running Application
if __name__ == '__main__':
    Core().run()  
    app = Gui()
    app.add_pages(ROUTES)
    app.run(use_reloader=True,title="World Population Exploration!", watermark="Explore World Data!", favicon="https://emojifavicon.dev/favicons/1f30e.png")