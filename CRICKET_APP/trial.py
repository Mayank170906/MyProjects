import pandas as pd

# Sample data for CSK vs MI 2024 match scorecard
data = {
    'PlayerName': [
        # CSK players
        "Ruturaj Gaikwad", "Devon Conway", "Shivam Dube", "Moeen Ali", "MS Dhoni", 
        "Ravindra Jadeja", "Deepak Chahar", "Tushar Deshpande", "Maheesh Theekshana", "Matheesha Pathirana", "Ajinkya Rahane",
        
        # MI players
        "Rohit Sharma", "Ishan Kishan", "Suryakumar Yadav", "Cameron Green", "Tilak Varma", 
        "Tim David", "Hrithik Shokeen", "Piyush Chawla", "Jason Behrendorff", "Jofra Archer", "Arjun Tendulkar"
    ],
    'Team': [
        "CSK", "CSK", "CSK", "CSK", "CSK", 
        "CSK", "CSK", "CSK", "CSK", "CSK", "CSK",
        
        "MI", "MI", "MI", "MI", "MI", 
        "MI", "MI", "MI", "MI", "MI", "MI"
    ],
    'Runs': [
        # CSK players
        45, 60, 35, 10, 25, 
        15, 0, 0, 0, 0, 5, 
        
        # MI players
        30, 55, 40, 10, 20, 
        15, 0, 0, 0, 0, 5
    ],
    '4s': [
        # CSK players
        4, 6, 3, 1, 2, 
        1, 0, 0, 0, 0, 1,
        
        # MI players
        3, 5, 4, 1, 2,
        1, 0, 0, 0, 0, 1
    ],
    '6s': [
        # CSK players
        1, 2, 2, 0, 1,
        0, 0, 0, 0, 0, 0,
        
        # MI players
        1, 3, 2, 0, 1,
        1, 0, 0, 0, 0, 0
    ],
    'Wickets': [
        # CSK players
        0, 0, 0, 1, 0,
        1, 2, 1, 3, 2, 0,
        
        # MI players
        0, 0, 0, 1, 0,
        0, 1, 2, 1, 2, 1
    ]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save the data to an Excel file
file_path = './csk_vs_mi_2024_match.xlsx'
df.to_excel(file_path, index=False)

file_path
