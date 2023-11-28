import pandas as pd

data = {
    'Property_ID': [1, 2, 3, 4, 5],
    'Location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'Bedrooms': [3, 4, 2, 5, 3],
    'Area_sqft': [1500, 1800, 1200, 2200, 1600],
    'Listing_Price': [250000, 320000, 200000, 420000, 280000]
}
property_data = pd.DataFrame(data)

# 1. 
average_price_per_location = property_data.groupby('Location')['Listing_Price'].mean()
print("Average listing price of properties in each location:")
print(average_price_per_location)

# 2.
num_properties_more_than_four_bedrooms = property_data[property_data['Bedrooms'] > 4].shape[0]
print(f"\nNumber of properties with more than four bedrooms: {num_properties_more_than_four_bedrooms}")

# 3.
property_largest_area = property_data.loc[property_data['Area_sqft'].idxmax()]
print("\nProperty with the largest area:")
print(property_largest_area)
