import re
import csv

# Input text
data = """
6. A. Aziz*, M. M. Suzon and R. Hasan, "A fuzzy logic-based risk evaluation and precaution level estimation of explosive, flammable, and toxic chemicals for preventing damages," Heliyon , Elsevier BV, vol. 11, no.1, DOI:https://doi.org/10.1016/j.heliyon.2024.e41216, 2025 .
[Impact Factor: 3.4, SJR: Q1]
5. M. Ashikuzzaman, A. Aziz* and A. A. Fime, "DangerDet: A mobile application-based danger detection platform for women and children using deep learning," SoftwareX , ISBN:2352-7110, Elsevier B.V., vol. 29, DOI:https://doi.org/10.1016/j.softx.2024.101983, 2024 .
[Impact Factor: 2.4, SJR: Q2]
4. A. A. Rafi, M. M. A. Nihal and A. Aziz*, "ShopiRound: An Android application-based e-commerce system to find products nearby using travelling salesman problem," SoftwareX , ISBN:2352-7110, Elsevier B.V., vol. 29, DOI:https://doi.org/10.1016/j.softx.2024.101973, 2024 .
[Impact Factor: 2.4, SJR: Q2]
3. A. Aziz*, M. A. Golap, R. A. Porosh, M. T. K. Tousif and M. S. Sadi, "Multi-bit error detection and correction technique using HVDK (Horizontal-Vertical-Diagonal-Knight) parity," Integration , ISBN:1872-7522, Elsevier BV, vol. 100, pp.102297, DOI:https://doi.org/10.1016/j.vlsi.2024.102297, 2024 .
[Impact Factor: 2.2, SJR: Q3]
2. F. Shama, A. Aziz* and L. B. M. Deya, "CitySolution: A complaining task distributive mobile application for smart city corporation using deep learning," SoftwareX , ISBN:2352-7110, Elsevier BV, vol. 27, DOI:https://doi.org/10.1016/j.softx.2024.101829, 2024 .
[Impact Factor: 2.4, SJR: Q2]
1. A. A. Fime*, M. Ashikuzzaman and A. Aziz, "Audio signal based danger detection using signal processing and deep learning," Expert Systems with Applications , ISBN:1873-6793, Elsevier BV, vol. 237, pp.121646, DOI:https://doi.org/10.1016/j.eswa.2023.121646, 2024 .
[Impact Factor: 8.5, SJR: Q1]
Conference
9. L. B. M. Deya, A. Aziz* and F. Shama, "Deep Learning-Based Complaining Task Distribution towards Smart City," 27th International Conference on Computer and Information Technology (ICCIT), IEEE, Cox's Bazar, Bangladesh, 2024 .
[Accepted in Press}
8. S. S. Sakib, M. J. Nayeem, A. Aziz*, A. Z. M. N. Abir and J. Rabbi, "Sentiment Analysis of Bangla Text Using Transformer Based Model," Proc. of 2nd International Conference on Big Data, IoT, and Machine Learning: BIM 2023, Taylor and Francis, Dhaka, Bangladesh, 2023 .
[Accepted in Press and Camera Ready version is Submitted]
7. M. M. Suzon, R. Hasan, A. Aziz* and A. Z. M. N. Abir, "Risk Evaluation of Explosive and Flammable Chemicals Using Fuzzy Inference System," Lecture Notes in Networks and Systems, Springer Nature Singapore, Dhaka, Bangladesh, vol. 867, 2024 , pp.911–921, DOI:https://doi.org/10.1007/978-981-99-8937-9_60.
6. A. Aziz* and M. M. A. Hashem, "Fuzzy Logic-Based Assessment of Students Learning Outcome in Implementing Outcome-Based Education," Proceedings of the International Conference on Big Data, IoT, and Machine Learning: BIM 2021, Springer Singapore, Cox’s Bazar, Bangladesh, 23-25 September 2021 , pp.745-759.
5. M. Ashikuzzaman, A. A. Fime, A. Aziz and T. Tasnima, "Danger Detection for Women and Child Using Audio Classification and Deep Learning," 2021 5th International Conference on Electrical Information and Communication Technology (EICT), IEEE, 17-19 December 2021 , pp.1-6.
4. T. Tithy, S. Chakraborty, R. Islam and A. Aziz, "A Deep Learning based Approach for Real Time Face Recognition System," 2021 International Conference on Electronics, Communications and Information Technology (ICECIT), IEEE, 14-16 September 2021 , pp.1-4.
3. A. R. M. J. U. Jamali, M. A. Alam and A. Aziz, "Statistical Analysis of Various Optimal Latin Hyper-cube Designs," Data Science and SDGs Challenges, Opportunities and Realities, Springer, Singapore, Rajshahi, Bangladesh, 18-19 December 2019 , pp.155-163, DOI:https://doi.org/10.1007/978-981-16-1919-9_13.
2. A. Aziz*, M. A. Golap and M. M. A. Hashem, "Student's Academic Performance Evaluation Method Using Fuzzy Logic System," 2019 1st International Conference on Advances in Science, Engineering and Robotics Technology (ICASERT), IEEE, Dhaka, Bangladesh, 3-5 May 2019 , pp.1-6.
1. A. Aziz*, M. M. A. Masba, M. A. Golap and M. Hashem, "An IoT Based Approach for Very Low Cost Real Time Vehicle Tracking System," 14th Global Engineering and Technology Conference, BIAM Foundation, 63 Eskaton, Dhaka, Bangladesh, February 2018 , pp.1-6.
"""

# Regex pattern to extract authors and titles
pattern = r"\d+\.\s([^,]+(?:,\s[^,]+)*),\s\"(.*?)\""

# Extract matches
matches = re.findall(pattern, data)

# Prepare data for CSV
csv_data = [(authors.strip(), title.strip()) for authors, title in matches]

# Output file
output_file = "KUET_author_list.csv"

# Write to CSV
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Authors", "Title"])
    writer.writerows(csv_data)

print(f"Data extracted and saved to {output_file}.")
