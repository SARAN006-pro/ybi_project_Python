import pandas as pd
import matplotlib.pyplot as plt

# Load election data
df = pd.read_csv("election_results.csv")

# Sample Data for README
sample_data = {
    "State": ["State A", "State B", "State C"],
    "Candidate": ["Candidate X", "Candidate Y", "Candidate Z"],
    "Votes": [5000, 7000, 6000]
}
sample_df = pd.DataFrame(sample_data)
sample_df.to_csv("election_results.csv", index=False)

# Calculate total votes
total_votes = df["Votes"].sum()

# Calculate vote percentage
df["Vote Percentage"] = (df["Votes"] / total_votes) * 100

# Find the winner
winner = df.loc[df["Votes"].idxmax(), "Candidate"]

# Print results
print("Total Votes Cast:", total_votes)
print("Election Results:")
print(df)
print("Winner of the Election:", winner)

# Plot vote distribution
plt.figure(figsize=(10, 5))
plt.bar(df["Candidate"], df["Votes"], color=['blue', 'red', 'green', 'orange'])
plt.xlabel("Candidates")
plt.ylabel("Number of Votes")
plt.title("Election Results")
plt.xticks(rotation=45)
plt.show()
'''
import pandas as pd

# Define data
data = {
    "State": ["State A", "State B", "State C"],
    "Candidate": ["Candidate X", "Candidate Y", "Candidate Z"],
    "Votes": [5000, 7000, 6000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("election_results.csv", index=False)

print("election_results.csv file created successfully!")
'''
