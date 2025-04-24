# Premier League Team Performance Explorer

An interactive web‐based visualisation that exposes multivariate patterns in Premier League team performance (2015–2024). It combines a Parallel Coordinates Plot and Small Multiples of goal‐scored trends to answer the question:

-  Analyse the correlation of key match statistics with overall success. Do certain match statistics strongly correlate with final league position, and have these correlations changed over time?


# Features

- **Parallel Coordinates Plot**  
  – One vertical axis per metric (shots, goals, corners, yellow cards, points, position).  
  – Polylines coloured by team using a perceptually distinct palette.  
  – Interactive brushing on any axis to filter.  

- **Small Multiples**  
  – Trend charts of goals scored over time for selected teams.  
  – Automatic linear‐trend overlays highlight long-term patterns.  

- **Dropdown Filters & Legend**  
  – Season and Team selectors for quick subsetting.  
  – “Pick teams for trends” panel with checkboxes and “Clear All” button.  
  – Clickable legend entries to isolate a single team in the parallel plot.  

- **Tooltips & Annotations**  
  – Hover on any polyline to see exact values.  
  – Annotated championship seasons and outlier performances.

# Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Edge)  
- A static file server (e.g. [http-server](https://www.npmjs.com/package/http-server) or Python’s built-in server)

All the visualisation code can be found in index.html. The combined finalised dataset is in final_dataset_2015-2024.csv. The code to create this dataset is in create_final_dataset.py. Intermediary code to create aggregated datasets and the aggregated datasets themselves are also included, as are the original datasets. 
