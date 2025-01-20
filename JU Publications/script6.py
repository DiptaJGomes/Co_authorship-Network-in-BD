import csv

# List of publications
publications = [
    "Md. Golam Moazzam and Md. Al-Amin Bhuiyan, “A Novel Approach for Human Face Detection Using Genetic Algorithm”, Journal of Electronics and Computer Science, Vol. 10, June 2009.",
    "Md. Golam Moazzam, Ms. Rubayat Parveen, and Md. Al-Amin Bhuiyan, “Human Face Detection under Complex Lighting Conditions”, International Journal of Advanced Computer Science and Applications, Special Issue on Image Processing and Analysis, ISSN: 2156-5570, Special Issue 1, pp. 85-90, June 2011.",
    "Amita Chakraborty, Md. Golam Moazzam, Shamima Nasrin, Mohammad Zahidur Rahman “A Novel Approach for Efficient and Convenient E-Auction”, Journal of Computer Engineering, Vol. 3, Issue 4, pp. 01-06, April 2013.",
    "Mahbuba Begum, Md. Golam Moazzam, Mohammad Shorif Uddin, “Quantitative Analysis on Robustness of FLD and PCA-Based Face Recognition Algorithms”, International Journal of Computer Applications, Vol. 99, No. 19, pp. 10-14, August 2014.",
    "Israt Jahan, Md. Golam Moazzam, KM Akkas Ali, Mujiba Shaima and Abu Tayeb Muhammad Alimuzzaman, “Purity Analysis of Pulse Crops using Machine Vision System”, Canadian Journal of Pure and Applied Sciences, Vol. 9, No. 2, pp. 3423-3430, June 2015.",
    "Md. Golam Moazzam, Tanzila Rahman and Mohammad Shorif Uddin, “Effective Techniques for Reduction of Impulse, Gaussian and Speckle Noises”, International Journal of Computer Science and Information Security, ISSN: 1947-5500, Vol. 14, No. 7, pp. 45-51, July 2016.",
    "Mahbuba Begum, Jannatul Ferdush and Md. Golam Moazzam, “A Hybrid Cryptosystem Using DNA, OTP and RSA”, International Journal of Computer Applications, Vol. 172, No. 8, pp. 30-33, August 2017.",
    "Md. Golam Moazzam, Mohammad Reduanul Haque and Mohammad Shorif Uddin, “Image-Based Vehicle Recognition using Neural Network”, International Journal of Computer Sciences and Engineering, Vol.7, Issue 5, pp.948-954, May 2019.",
    "Md. Golam Moazzam, Mohammad Reduanul Haque and Mohammad Shorif Uddin, “Image-Based Vehicle Speed Estimation”, Journal of Computer and Communications, Vo. 7, pp.1-5, May 2019.",
    "Md. Saddam Hossain, Amina Khatun, SM Khiroul Bashar and Md. Golam Moazzam, “Automatic Image Stitching Using Feature Based Approach”, International Journal of Engineering and Science Invention, Vol. 9, Issue 7, Series II, pp. 21-30, July 2020.",
    "Mahbub Alam, Osman Goni, Abu Shameem, Shamimul Islam, Nayan Kumar Datta, Shakil Ahmed, and Golam Moazzam, “An Approach for the Normalization of Short Message Service to Detect Shorter Form of Words and Find out Actual Word”, International Journal of Electronics and Information Engineering, Vol.13, No.3, pp.111-118, Sept. 2021."
]

# Initialize an empty list to store the extracted data
extracted_data = []

# Iterate over the publications and extract authors and titles
for publication in publications:
    parts = publication.split('“')
    authors = parts[0].strip()
    title = parts[1].split('”')[0].strip()
    extracted_data.append({"authors": authors.strip(), "title": title.strip()})

# Define the CSV file name
csv_file = 'extracted_publications.csv'

# Write the extracted data to a CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Authors", "Title"])
    for data in extracted_data:
        writer.writerow([data["authors"], data["title"]])

print(f"The authors and titles have been successfully extracted and written to {csv_file}.")