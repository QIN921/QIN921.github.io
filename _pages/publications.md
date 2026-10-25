---
title: "📝 Publications"
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

<h2>💡 Patents</h2>

- **失真-感知权衡可控的图像压缩方法、系统、介质及设备**  
  Granted patent · **CN119211548B** · First student inventor
- **面向机器视觉的端-边协同视频编码方法及视频传输系统**  
  Granted patent · **CN115767098B** · First inventor
- **历史目标识别方法及系统、端-边协同边界框过滤方法**  
  Granted patent · **CN115909131B**
- **一种视频传输配置模型的构建方法及应用**  
  Granted patent · **CN115357379B**
