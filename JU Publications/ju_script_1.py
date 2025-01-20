import csv
import re

# Provided text
text = """
[1]     Tania Khatun, Md. Asraful Sharker Nirob, Prayma Bishshash, Morium Akter, Mohammad Shorif Uddin, "A comprehensive dragon fruit image dataset for detecting the maturity and quality grading of dragon fruit," Data in Brief (Elsevier), Vol. 51, December 2023, https://doi.org/10.1016/j.dib.2023.109936  (WoS, Scopus, Q2)

[2]     Morium Akter, Mohammad Abu Baker and Mohammad Shorif Uddin, “Smart Home Security System”, Transactions on Engineering and Computing Sciences - Vol. 11, No. 4 Publication Date: August 25, 2023  htps://doi.org/10.14738/tecs.114.14975

[3]     Nusrat Sultana, Sumaita Binte Shorif, Morium Akter, Mohammad Shorif Uddin, "A dataset for successful recognition of cucumber diseases," Data in Brief (Elsevier), vol. 49, August 2023, https://doi.org/10.1016/j.dib.2023.109320 (WoS, Scopus, Q2)

[4]        Md. Al Mamun, Md. Solaiman Kabir, Morium Akter, Mohammad Shorif Uddin, "Recognition of human skin diseases using inception-V3 with transfer learning," International Journal of Information Technology, (Springer), August 2022, https://doi.org/10.1007/s41870-022-01050-4  (Scopus, Q2)

[5]      Sk. Fahmida Islam, Md. Iqramul Hasan, Morium Akter, Mohammad Shorif Uddin, "Implementation and Analysis of an IoT-Based Home Automation Framework," Journal of Computer and Communications, vol. 9, no. 3, pp. 143-157, March 2021. https://doi.org/10.4236/jcc.2021.93011

[6]     Sk. Fahmida Islam, Morium Akter, Mohammad Shorif Uddin, "Design and implementation of an internet of things based low-cost smart weather prediction system," International Journal of Information Technology, (Springer)  July 2021 https://doi.org/10.1007/s41870-021-00732-9 (Scopus, Q2)

[7]     Md. Tarek Habib, Anup Majumder, A.Z.M. Jakaria, Morium Akter, Mohammad Shorif Uddin, Farruk Ahmed, “Machine vision-based papaya disease recognition,” Journal of King Saud University – Computer and Information Sciences 32 (2020) 300–309 (Elsevier), https://doi.org/10.1016/j.jksuci.2018.06.006  (WoS, Scopus, Q1)

[8]     Md. Al Mamun, Morium Akter, Mohammad Shorif Uddin, "A Survey on Matching of Shoeprint with Reference Footwear in Forensic Study," Journal of Computer and Communications, Vol. 7, pp. 1-5, September 2019, https://doi.org/10.4236/jcc.2019.79002

[9]     Umme Sara, Morium Akter, Mohammad Shorif Uddin, “Image quality assessment through FSIM, SSIM, MSE and PSNR- A comparative study,” Journal of Computer and Communications, Vol. 7, pp. 8-18, March 2019, https://doi.org/10.4236/jcc.2019.73002

[10]  Aditi Sarker, Morium Akter and Mohammad Shorif Uddin, “Simulation of Hazy Image and Validation of Haze Removal Technique,” Journal of Computer and Communications (JCC), vol. no.7, pp. 62-72, February, 2019

[11]   Morium Akter, Liton Jude Rozario, Mohammad Shorif Uddin, “Gait Recognition for Security and Surveillance System- A Review,” International Journal of Computer Science and Information Security (Thomson Reuters Indexed), Vol. 16, no. 6, pp. 143-149, June 2018

[12] Md. Tarek Habib, Anup Majumder, A.Z.M. Jakaria, Morium Akter, Mohammad Shorif Uddin, Farruk Ahmed, “Machine Vision Based Papaya Disease Recognition,” Journal of King Saud University - Computer and Information Sciences (Elsevier), 2018

[13]  Morium Akter, “Detection of Microaneurysm in Diabetic Retinopathy,” International Journal of Computer Science and Information Security (Thomson Reuters Indexed), Vol. 15, No. 8, pp. 200-203, August 2017

[14] Morium Akter and Mohammad Shorif Uddin, “Android-Based Diabetes Management System”,  International Journal of Computer Applications, vol. 110,  No. 10, January 2015, pp. 5-9

[15]  Morium Akter, Mohammad Shorif  Uddin and Md. Atiqul Islam, “A Mobile-Based System for Management of Hypertension with Diabetes”, Journal of Computer Science and Software Application, Volume 1, Number 2, December 2014, pp. 98-107

[16] Morium  Akter and Mohammad Shorif Uddin,  “Morphology-Based Exudates Detection in Diabetic Retinopathy”, International Journal of Advances in Biomedical Science and Engineering, Volume 1, Number 1, September 2014, pp. 43-53

[17]  Morium Akter and Mohammad Shorif Uddin, “A Review on Automated diagnosis of Diabetic Retinopathy”, An International Journal of Advanced Computer Technology, Volume 3, Issue 10, pp. 1161-1166

[18] Mohammad Shorif Uddin and Morium Akter, “Development of a knowledge-based diagnosis and management system for diabetes mellitus through web-based technique”, ULAB Journal of Science and Engineering, vol.1, 2010, pp.37-41

[1]      Mohammad Reduanul Haque, Rubaiya Hafiz, Mohammad Zahidul Islam, Amina Khatun, Morium Akter, Mohammad Shorif Uddin, "Handwritten Indic Digit Recognition using Deep Hybrid Capsule Network," Proc. of International Joint Conference on Advances in Computational Intelligence (IJCACI 2020), 20-21 November 2020, Dhaka, Bangladesh, (Algorithms for Intelligent Systems, Springer), pp. 539-547. https://doi.org/10.1007/978-981-16-0586-4_43

[2]      Rabeya Basri, M. Reduanul Haque, Morium Akter, Mohammad Shorif Uddin, "Bangla Handwritten Digit Recognition Using Deep Convolutional Neural Network," International Conference Computing Advancements (ICCA 2020), ACM, January 10-12, 2020, Dhaka, Bangladesh (ACM Digital Library). https://doi.org/10.1145/3377049.3377077

[3]      Morium Akter,  Jannatul Ferdous, Mahmuda Najnin Eva, Sumaita Binte Shorif, Sk. Fahmida Islam and M. Shorif Uddin, "Vehicle Detection and Its Speed Measurement," Proc. of International Conference on Advances in Energy Management (ICAEM 2019), 20-21 December 2019, Jodhpur, India, (Algorithms for Intelligent Systems, Springer), https://doi.org/10.1007/978-981-15-8820-4_9

[4]      Md. Sabab Zulfiker, Nasrin Kabir, Hafsa Moontari Ali,  M. Reduanul Haque, Morium Akter and M. Shorif Uddin, “Sentiment Analysis Based on Users' Emotional Reactions about Ride-sharing Services on Facebook and Twitter,” Proc. of International Joint Conference on Computational Intelligence (IJCCI 2019), 25-26 October 2019, Dhaka, Bangladesh, (Algorithms for Intelligent Systems, Springer), pp. 397-408, https://doi.org/10.1007/978-981-15-3607-6_32

[5]      Nusrat Jahan Farin, Morium Akter and Mohammad Shorif Uddin, "Data Mining Techniques for Predicting User Interest in Facebook Pages: A Comparison," International Conference on Advances in Science, Engineering and Robotics Technology (ICASERT 2019), May 3-5, 2019, Dhaka, Bangladesh (IEEE Xplore), https://doi.org/10.1109/ICASERT.2019.8934618

[6]      Mohammad Shorif Uddin, Bishal Gautam, Aditi Sarker, Morium Akter and Mohammad Reduanul Haque, “Image-Based Automated Haze Removal Using Dark Channel Prior”, 2017 IEEE Region 10 Humanitarian Technology Conference (R10-HTC), 21 Dec - 23 Dec 2017, Dhaka, Bangladesh

[7]      Morium Akter, Mohammad Shorif Uddin and Mahmudul Hasan Khan, “Morphology-based exudates detection from color fundus images in diabetic retinopathy”, International Conference on Electrical Engineering and Information & Communication Technology (ICEEICT) 2014, ©2014 IEEE, Dhaka, Bangladesh

[8]      Morium Akter, Mohammad Shorif Uddin and Aminul Haque, “A Knowledge-Based System for Diagnosis and Management of Diabetes Mellitus”, 13th International Conference on Biomedical Engineering (ICBME2008), Singapore, pp.1000-1003 (Published  as springer lecture notes)

[9]      Morium Akter, Mohammad Shorif Uddin, Aminul Haque " Design of an Expert System for the Management of Hypertension in Patients with Diabetes Mellitus "  International Conference on Electronics, Computer and Communication (ICECC 2008) University of Rajshahi, Bangladesh, pp.523-527

[10]  Mushfeq-Us-Saleheen Shameem, Syed Foysol Islam, M. M. Rajib Billah, Morium Akter  "An efficient technique for Speech Enhancement using an Analog Electronic Circuit for Voice over Internet"  International Conference on Electronics, Computer and Communication (ICECC 2008) University of Rajshahi, Bangladesh, 188-192

[11]  Mushfeq-Us-Saleheen Shameem, Syed Foysol Islam, M. M. Rajib Billah, Morium Akter  "Performance Analysis Design of Gold Codes and Walsh Codes  for Application Layer Correlation Techniques in CDMA technology"  International Conference on Electronics, Computer and Communication (ICECC 2008) University of Rajshahi, Bangladesh, 193-197
"""

# Regex pattern to extract authors and titles
pattern = r"\[\d+\]\s*(.*?),\s*“(.*?)”"

# Extract matches
matches = re.findall(pattern, text)

# Save to CSV
with open('authors_titles_ju_9.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Authors'])  # Write header
    for title, authors in matches:
        writer.writerow([title.strip(), authors.strip()])

print("research_data_ju.csv")