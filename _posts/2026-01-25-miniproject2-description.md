---
title: "Government and service dilivery"
excerpt_separator: "<!--more-->"
categories:
  - project2
tags:
  - experiments
  - tests
image: images/my-image.jpg

---

# Access to electricity and drinking water in Pakistan (Urban, Rural).

This project investigates the question: Why is access to electricity significantly higher than access
to drinking water,especially safely managed water,in both urban and rural areas of Pakistan?
While both electricity and water are essential public services and central to sustainable development, 
Pakistan has made noticeably faster progress in expanding electricity access than in improving drinking water services.
The project examines 35 years, from 1990 to 2025, to show changes over time and trends in access to electricity and water,
disaggregated by urban and rural populations, to understand what these differences reveal about infrastructure development,
policy priorities, and service delivery challenges in Pakistan.
   




# Project Context
Access to electricity and safe drinking water is used here as a case to analyse public policies,
governance, and development in Pakistan. Both electricity and drinking water services are the basic rights
of the public and are also core to the United Nations Development Program (UNDP). But the Pakistan government 
faces challenges in delivering these. The purpose of this project is to examine the evolution over these three decades.
According to World Bank Group data,private investment in the energy sector, especially in electricity, is the highest. 


# Data collection
 
Several indicators related to access to infrastructure across countries and years are included in the dataset,
which was downloaded in CSV format. Only records related to Pakistan were kept from this dataset.
To distinguish between urban and rural populations, indicators related to drinking water and electricity access were further filtered. 
Each year was represented as a separate column in the initial wide format of the data. These data were cleaned by removing missing or incorrect entries, 
collecting numeric year values, converting access figures into numeric form, and converting them into a long format.
Year-by-year percentage values for various service indicators make up the final cleaned dataset, which is useful for visualisation.


# Methodology
I downloaded the data from world bank database World Development Indicators (WDI), as mentioned above.
The data contains several indicators and country names, but my need was only for Pakistan, its rural and urban areas.
For that, Python was used to work with. I transformed the data at the start of the analysis, mainly utilising the pandas and NumPy libraries.
The indicators were classified into meaningful groups according to service type (electricity, basic water, safely managed water) and
area (urban or rural) following the dataset's cleaning and restructuring. This classification made it possible to compare services and locations consistently. 
To ensure clarity and comparability, values were aggregated using yearly averages when there were multiple observations for the same indicator and year.
Plotly, an interactive visualisation library, was used to visualise the processed data in order to look at trends over time.
To show how access levels changed between 1995 and 2025, line charts with distinct facets for every service-area combination were made. 
This approach made it possible to compare data over time and visually examine differences in access to water and electricity, 
as well as between urban and rural populations. Cleaned and aggregated data tables were among the intermediate outputs, 
and interactive time-series visualisations that amply demonstrate long-term trends and service delivery gaps made up the final analytical output.


# Findings
Over the course of the study, access to electricity has grown faster and reached higher levels than access to drinking water,
according to the analysis. While rural areas also saw significant advancements over time, urban areas attained nearly universal access to electricity earlier.
On the other hand, access to drinking water, especially safely managed drinking water, has risen more slowly and is still much less common, particularly in rural areas.
When it comes to water, the gap between urban and rural areas is greater than that of electricity.
These results imply that efforts to enhance water quality and dependability have not been as successful as electricity.


![a random image]({{site.baseurl}}images/filename.png)


# Reflection
It was an exciting and interesting project to work on. In the beginning, I spent a lot of time learning all the skills and
digital tools needed for data analysis and visualization. Processes such as data cleaning, wide format to long format transformations,
filtering certain indicators and managing missing/inconsistent values were confusing at first. Learning to utilize Python libraries like pandas,
NumPy and Plotly involved trial and error, especially given that I hadn’t worked with actual datasets of this size before. That being said,
learning these tools was worth it. They enabled me to structure the processing and cleaning of World Development 
Indicators dataset in a systematic manner, group indicators by service type and geography, 
analyze long-term trends with regard to access to electricity and water in Pakistan.Using interactive visualizations showing it,
I could demonstrate the gaps in accessibility to electricity and drinking water,in urban and rural areas of pakistan to proof my
dissertation about governance,development and government policies.


