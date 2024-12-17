import pandas as pd

#read csv file
df=pd.read_csv("data//iris-flower-data.csv")

#filter and format cells
#sepal_length

#sepal_width
#petal_length
#petal_width
#species

# Define validation functions
def validate_numeric(column):
    """Check if all values in the column are numeric."""
    return pd.to_numeric(df[column], errors='coerce').notna().all()

def validate_species():
    """Check if all species values are valid."""
    valid_species = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    return df['species'].isin(valid_species).all()

# Perform validations
numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
numeric_validations = {col: validate_numeric(col) for col in numeric_columns}
species_validation = validate_species()

# Print results
print("Validation Results:")
for col, is_valid in numeric_validations.items():
    print(f"{col}: {'Valid' if is_valid else 'Invalid'}")
print(f"species: {'Valid' if species_validation else 'Invalid'}")

# Handle invalid data
if not all(numeric_validations.values()) or not species_validation:
    print("\nIssues detected with the data. Invalid rows:")
    # Identify rows with invalid numeric data
    invalid_numeric_rows = df[~df[numeric_columns].apply(pd.to_numeric, errors='coerce').notna().all(axis=1)]
    # Identify rows with invalid species
    invalid_species_rows = df[~df['species'].isin(["Iris-setosa", "Iris-versicolor", "Iris-virginica"])]
    invalid_rows = pd.concat([invalid_numeric_rows, invalid_species_rows]).drop_duplicates()
    print(invalid_rows)
else:
    print("\nAll data is valid.")

