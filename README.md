# exploratory-data-analysis---online-shopping-in-retail309

## 1. Description
During this data analysis, a dataset of online shopping website activity (each row representing details about one user while being on the website) will be extracted from RDS database, cleaned using various statistical methods, then will be analysed to answer some questions which will contribute to make informed decisions about changes to the website and marketing strategies.

## 2. Installation
Following libraries to be installed:
- pandas
- SQLAlchemy
- PyYAML
- Matplotlib
- statsmodels
- Numpy
- seaborn
- scipy

## 3. Usage
Data dictionary for online customer activity:

- **administrative**: Columns which indicates which administrative activity the user was performing on their account
- **administrative_duration**: How long a user performed administrative tasks in that session
- **informational**: Indicates which informational activity the user was performing on the website
- **informational_duration**: How long a users performed informational tasks in seconds during that session
- **product_related**: Indicates which product the user was viewing on the website
- **product_related_duration**: How long a user browsed products during that session 
- **bounce_rates**: Historical bounce rate of that particular page for all users. They visited directly and immediately exited
- **exit_rates**: Historical exit rate of the users from that particular page
- **page_values**: The average value contribution of a page to a customer sale
- **month**: Month the users activity took place
- **operating_systems**: Operating system the user was using
- **browser**: The browser used by the user
- **region**: The region the user originated from
- **traffic_type**: How the user was redirected to the site
- **visitor_type**: Whether a customer was new/returning or other
- **weekend**: Whether the activity only took place during the weekend
- **revenue**: Whether the customer purchased anything that session

## 4. File Structure
This repository contains following files:
- customer_activity.csv: data extracted from the database
- dataframe_info.py: contains class methods required to get information from data
- dataframe_transform.py: contains class methods for transforming data during data clearning process to make the data ready for analysis
- plotter.py: contains class methods to visualise data to gain insights
- db_utils.py: contains class methods to extract data from the database
- retail_EDA_report.ipynb: main report for this data analysis 
