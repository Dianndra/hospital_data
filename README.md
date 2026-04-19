# 🏥 Lagos State Hospital Data Analysis

![Python](https://img.shields.io/badge/Python-Data%20Scraping-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-Data%20Cleaning-orange?logo=postgresql)
![Power BI](https://img.shields.io/badge/Power%20BI-Data%20Visualization-yellow?logo=powerbi)

## 📸 Dashboard Preview

<p align="center">
  <img src="visualization/overview.png" width="45%"/>
  <img src="visualization/overview_2.png" width="45%"/>
</p>

## 📌 Project Overview
This project focuses on building a structured dataset and analytical dashboard of hospitals in Lagos State, Nigeria. The goal was to transform publicly available but unstructured healthcare data into actionable insights that can support planning, accessibility analysis, and healthcare decision-making.

## 🎯 Objectives
- Extract and compile a dataset of **Primary, Secondary, and Tertiary hospitals in Lagos State**

### Analyse:
- Distribution of **Private vs Government-owned hospitals**
- **Average time in operation**
- Breakdown by **Healthcare Tier**
- Distribution across **Local Government Areas (LGA)**

## 📊 Data Source
- **Source:** Federal Ministry of Health Facility Registry  
- **Link:** https://hfr.health.gov.ng/facilities/hospitals-list?page=1356  

### Dataset Fields:
- Facility Name  
- Facility Type  
- Address / Location  
- Tier (Primary, Secondary, Tertiary)  
- Start Date  
- Ownership (Private/Government)  
- Facility ID  

## 🛠 Tools & Technologies
- **Python (Selenium, WebDriver)** – Data scraping  
- **SQL** – Data cleaning and transformation  
- **Power BI** – Data visualization and dashboard creation  

## ⚙️ Methodology

### 1. Data Collection
The data was scraped from the official health facility registry website using **Selenium** due to dynamic page loading and pagination. WebDriver was used to automate navigation across multiple pages.

### 2. Data Cleaning
Using SQL:
- Removed duplicates and inconsistencies  
- Standardised categorical fields (e.g., ownership, tier)  
- Handled missing or incomplete values  
- Structured date fields for analysis  

### 3. Data Analysis & Visualization
The cleaned dataset was imported into Power BI to create an interactive dashboard highlighting key healthcare distribution patterns.

## 📈 Key Insights
- A significant proportion of hospitals are **privately owned**, indicating reliance on private healthcare services  
- **Primary healthcare facilities** make up the largest share, while tertiary institutions are limited  
- Certain LGAs show **higher concentration of facilities**, suggesting uneven healthcare distribution  
- The **average operational age of hospitals** highlights a mix of long-established and relatively new facilities  

## 📊 Dashboard

🔗 **View Interactive Dashboard:**  
https://www.novypro.com/project/hosppital-dashboard  

## 📄 Documentation
- Detailed Report: *(Attach PDF in repo instead of local file path)*  
- Implementation Plan:  
https://crimson-answer-17d.notion.site/HEALTH-TRUSS-PROJECT-d5d9da2a8e4f42ba88109536a28772d2  

## 🚀 Potential Impact
This analysis can support:
- Healthcare resource planning  
- Identification of underserved areas  
- Policy and investment decisions  
- Improved accessibility to healthcare services  

## ⚠️ Challenges & Limitations
- Website structure required dynamic scraping (not API-based)  
- Some records had incomplete or inconsistent data  
- Analysis limited to available public data  

## 🔮 Future Improvements
- Integrate population data for deeper accessibility analysis  
- Add geospatial mapping of facilities  
- Build predictive models for healthcare demand  
