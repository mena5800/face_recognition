import pickle

# Load the list from the file using pickle
with open("output_file.pkl", "rb") as f:
    my_list = pickle.load(f)

# Use the list in your code
print(my_list)