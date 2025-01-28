import csv

# List of publications
publications = [
    "Rumana Yasmin, Aparna Das, Liton Jude Rozario, Md. Ezharul Islam, \"Butterfly detection and classification techniques: A review,\" Intelligent Systems with Applications, Volume 18, 2023, 200214, ISSN 2667-3053, https://doi.org/10.1016/j.iswa.2023.200214   Available online 15 March 2023  ( https://www.sciencedirect.com/science/article/pii/S266730532300039X )",
    "Shahnaj Parvin, Md. Ezharul Islam, and Liton Jude Rozario, \"Nighttime Vehicle Detection Methods Based on Headlight Feature: A Review,\" IAENG International Journal of Computer Science, vol. 49, no.1, pp79-93, March 2022.",
    "Shahnaj Parvin, Liton Jude Rozario, Md. Ezharul Islam, “Vehicle Number Plate Detection and Recognition Techniques: A Review,” Advances in Science, Technology and Engineering Systems Journal (ASTESJ), Volume 06, Issue no 02, PP. 423-438, 17 March 2021.",
    "Shahnaj Parvin, Liton Jude Rozario, Md. Ezharul Islam, “Vision-based On-Road Nighttime Vehicle Detection and Tracking Using Taillight and Headlight Features,” Journal of Computer and Communications (JCC), Volume 09, Issue no 03, PP. 29-53, 09 March 2021.",
    "Shahnaj Parvin, Md. Ezharul Islam, Liton Jude Rozario, “Nighttime Vehicle Detection Methods based on Brake Light/Taillight Features: A Review,\" International Journal of Computer Science and Information Security (IJCSIS), Volume 18, Issue no 12, PP. 61-72, 31 December 2020.",
    "Bulbul Ahammad, Liton Jude Rozario, Anup Majumder, Md. Imdadul Islam, \"Combination of SVM, LDA, PCA and linear regression under fuzzy system in human face recognition,\" International Journal of Engineering & Technology, 7 (4) (2018) pp. 6970-6976.",
    "Liton Jude Rozario, Tanzila Rahman, Mohammad Shorif Uddin, “Segmentation of the Region of Defects in Fruits and Vegetables,” International Journal of Computer Science and Information Security, Vol. 14, No. 5, pp. 399-406, (May 2016)."
]

# Initialize an empty list to store the extracted data
extracted_data = []

# Iterate over the publications and extract authors and titles
for publication in publications:
    parts = publication.split(',"')
    if len(parts) > 1:
        authors = parts[0].strip()
        title = parts[1].split(',"')[0].strip()
        extracted_data.append({"authors": authors, "title": title})
    else:
        authors = publication.strip()
        title = ""
        extracted_data.append({"authors": authors, "title": title})

# Define the CSV file name
csv_file = 'extracted_publications.csv'

# Write the extracted data to a CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Authors", "Title"])
    for data in extracted_data:
        writer.writerow([data["authors"], data["title"]])

print(f"The authors and titles have been successfully extracted and written to {csv_file}.")