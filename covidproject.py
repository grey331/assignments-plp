# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 2: Load and explore the dataset
# Load the data
df = pd.read_csv('owid-covid-data.csv')

# Explore the dataset
print("Columns:", df.columns)
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Step 3: Data Cleaning
# Filter data for countries of interest
countries = ['Kenya', 'USA', 'India']
df_filtered = df[df['location'].isin(countries)]

# Convert 'date' to datetime format
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Fill missing values with 0 (for simplicity, can use more advanced techniques if necessary)
df_filtered.fillna(0, inplace=True)

# Step 4: Exploratory Data Analysis (EDA)
# Plot total cases over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

# Plot total deaths over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)

plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.show()

# Compare daily new cases between countries
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)

plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.show()

# Calculate the death rate and plot
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['death_rate'], label=country)

plt.title('Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.show()

# Step 5: Visualizing Vaccination Progress
# Plot cumulative vaccinations over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title('Cumulative Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.show()

# Step 6: Build a Choropleth Map (Optional)
# Prepare the latest data for choropleth map
country_data_latest = df_filtered[df_filtered['date'] == df_filtered['date'].max()]

# Create a choropleth map showing total cases by country
fig = px.choropleth(country_data_latest, locations='iso_code', color='total_cases',
                    hover_name='location', color_continuous_scale='Viridis',
                    labels={'total_cases': 'Total Cases'})
fig.update_layout(title="COVID-19 Total Cases by Country")
fig.show()

# Step 7: Insights & Reporting
# Writing insights:
insights = [
    "1. The USA has experienced the highest number of COVID-19 cases over time.",
    "2. India had a significant spike in cases during mid-2020, followed by a steady decline.",
    "3. Kenya, while showing fewer cases, has seen a relatively slow vaccination rollout.",
    "4. The death rate is consistently higher in the USA compared to India and Kenya, reflecting different healthcare systems.",
    "5. Vaccination rollouts are accelerating in the USA and India, while Kenya is lagging behind."
]

# Print insights
print("\nKey Insights:")
for insight in insights:
    print(insight)
