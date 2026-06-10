import pandas as pd 
df = pd.read_excel("C:/projects/apartments.xlsx")
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

print("What are you looking for?")
city = input("City: ")
bedrooms = int(input("Bedrooms: "))
max_price = int(input("Max Price: "))
isFurnished = input("Furnished (yes/no/partially): ").strip().lower()
print(df["Furnished (Y/N)"].unique())
matches = df[(df["City"] == city) & 
             (df["Bedrooms"] >= bedrooms) & 
             (df["Price"] <= max_price) &
             (df["Furnished (Y/N)"].str.strip().str.lower() == isFurnished)]

add_optional = input("\nAdd optional filters? (yes/no): ").strip().lower() == "yes"

if add_optional:
    parking = input("Parking required (yes/no): ").strip().lower() == "yes"
    elevator = input("Elevator required (yes/no): ").strip().lower() == "yes"
    balcony = input("Balcony required (yes/no): ").strip().lower() == "yes"
    divided = input("Must be dividable (yes/no): ").strip().lower() == "yes"
    special_keywords = input("Any special traits required? (leave blank for none): ").strip().lower()

    if parking:
        matches = matches[matches["Parking (Y/N)"].str.strip().str.lower() == "yes"]
    if elevator:
        matches = matches[matches["Elevator (Y/N)"].str.strip().str.lower() == "yes"]
    if balcony:
        matches = matches[matches["Balcony (Y/N)"].str.strip().str.lower() == "yes"]
    if divided:
        matches = matches[matches["Divided"].str.strip().str.lower() == "yes"]
    if special_keywords:
        matches = matches[matches["Special"].str.lower().str.contains(special_keywords, na=False)]

matches = matches.sort_values("Price")        
print(f"\nFound {len(matches)} apartments:")
print(matches.to_string(index=False))