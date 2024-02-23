<|toggle|theme|>
<|navbar|lov={[("/insights", "🌏 Insights"), ("/country_overview", "🎄 Country Population"), ("/top_countries_in_continent", "💯 Top Countries in Continent"), ("/compare_countries", "⚡ Compare Countries"), ("/pie_charts", "🥧 Pie Charts"), ("/total_population", "➕ Total"), ("/dataset", "📅 Explore Dataset")]}|>
<|container|

# ⚡ Compare **Countries**{: .color-primary} Population!

<|1 1|layout|

### Choose **1st**{: .color-primary} Country!

<|{country1}|selector|lov={COUNTRIES}|dropdown|on_change=choose_country1|>

### Choose **2nd**{: .color-primary} Country!

<|{country2}|selector|lov={COUNTRIES}|dropdown|on_change=choose_country2|>
|>
<br />
<|{country1}|>
<|{country2}|>
<|{DATA}|chart|>
|>
