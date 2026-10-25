---
title: "Publications"
permalink: /publications/
---

See my [Google Scholar profile](https://scholar.google.com/citations?user=eA17fngAAAAJ&hl=en) for the latest list.

{% assign years = site.data.publications | map: "year" | compact | uniq | sort | reverse %}
{% for year in years %}
<h2>{{ year }}</h2>
{% assign numeric_year = year | plus: 0 %}
{% assign papers = site.data.publications | where: "year", numeric_year %}
{% for paper in papers %}{% include publication.html paper=paper %}{% endfor %}
{% endfor %}

<h2>Year not specified</h2>
{% for paper in site.data.publications %}{% unless paper.year %}{% include publication.html paper=paper %}{% endunless %}{% endfor %}
