import csv
import re

# Input text
text = """
[1] Sai Peck Lee and Mohammad Zahidur Rahman. E-Commerce Services and Applications: A Practical Guide. University of Malaya Press, 2003.
[2] Md Rakib Hasan Mohammad Rabiul Alam, Sarker Md Firoz-Ul-Amin Mohammad, and Zahidur Rahman. “A Low Cost ECG Monitoring System with ECG Data Filtering”. In: International Journal of Computer Science and Information Security (IJCSIS) 16.4 (2018).
[3] Amita Chakraborty et al. “Security and Privacy of Online Sealed Bid Auction”. In: International Journal of Computer Applications 61.12 (2013).
[4] Subrata Kumar Das and Mohammad Zahidur Rahman. “A middleware architecture to integrate and share health data from heterogeneous and diverse data sources”. In: Iran Journal of Computer Science 5.3 (2022), pp. 267–277.
[5] Subrata Kumar Das and Mohammad Zahidur Rahman. “A secured compression technique based on encoding for sharing electronic patient data in slow-speed networks”. In: Heliyon 8.10 (2022), e10788.
[6] Toufik Ahmed Emon et al. “Improving security of the telemedicine system for the rural people of Bangladesh”. In: International Journal of Advanced Computer Science and Applications 9.1 (2018).
[7] Toufik Ahmed Emon et al. “Telemedicine and IoMT: Its importance regarding healthcare in Bangladesh”. In: Int J sci eng res 9.2 (2018), p. 5.
[8] Sayed MD Fahim Fahad, Md Abdur Rafi Ibne Mahmood, and Mohammad Zahidur Rahman. “Reform Based Version Management System for XML Data”. In: International Journal of Computer and Information Technology 3 (2014), pp. 1299–1304.
[9] Dewan Md Farid and Mohammad Zahidur Rahman. “Attribute weighting with adaptive NBTree for reducing false positives in intrusion detection”. In: arXiv preprint arXiv:1005.0919 (2010).
[10] Dewan Md Farid, Mohammad Zahidur Rahman, and Chowdhury Mofizur Rahman. “An ensemble approach to classifier construction based on bootstrap aggregation”. In: International Journal of Computer Applications 25.5 (2011), pp. 30–34.
[11] Dewan Md Farid et al. “Attacks Classification in Adaptive Intrusion Detection using Decision Tree
„International Journal of Computer”. In: Electrical, Automation, Control and Information Engineering 4.3 (2010).
[12] Dewan Md. Farid, Nouria Harbi, and Mohammad Zahidur Rahman. “Combining Naive Bayes and Decision Tree for Adaptive Intrusion Detection”. In: CoRR abs/1005.4496 (2010). arXiv: 1005.4496. URL: http://arxiv.org/abs/1005.4496.
[13] Dewan Md. Farid and Mohammad Zahidur Rahman. “Anomaly Network Intrusion Detection Based on Improved Self Adaptive Bayesian Algorithm”. In: JOURNAL OF COMPUTERS 5.1 (2010), pp. 23–31.
[14] Dewan Md. Farid, Mohammad Zahidur Rahman, and Chowdhury Mofizur Rahman. “Adaptive Intrusion De- tection based on Boosting and Naïve Bayesian Classifier”. In: nternational Journal of Computer Applications 24.3 (2011).
[15] Dewan Md. Farid et al. “Attacks Classification in Adaptive Intrusion Detection using Decision Tree”. In:
International Journal of Computer and Information Engineering 4.3 (2010).
[16] Israt Jahan and Mohammad Zahidur Rahman. “A realistic divisible transferable electronic cash for general use”. In: Journal of Discrete Mathematical Sciences and Cryptography 10.1 (2007), pp. 125–150.
[17] Israt Jahan et al. “Divisible Transferable Anonymous Electronic Cash System for General Use”. In: ().
[18] Yew Kok Meng, Mohammad Zahidur Rahman, and Sai Peck Lee. “Object-oriented approach to specify secret sharing protocol in security critical system using formal method”. In: Malaysian Journal of Computer Science 13.1 (2000), pp. 76–83.
[19] Uzzal Kumar Prodhan, Mohammad Zahidur Rahman, and Israt Jahan. “A survey on the assessment of the present states and opportunities of telemedicine in Bangladesh”. In: International Journal of Computer Science and Information Security 15.1 (2017).
[20] Uzzal Kumar Prodhan, Mohammad Zahidur Rahman, and Israt Jahan. “Design and implementation of an advanced telemedicine model for the rural people of Bangladesh”. In: Technology and Health Care 26.1 (2018), pp. 175–180.
[21] Uzzal Kumar Prodhan et al. “Implementation of Low Cost Remote Primary Healthcare Services through Telemedicine: Bangladesh Perspectives”. In: International Journal of Advanced Computer Science and Applications 11.11 (2020).
[22] Mohammad Zahidur Rahman and Sai Peck Lee. “Sealed-Bid Auction Protocol Implementation Over Corba Architecture”. In: Malaysian Journal of Computer Science 14.2 (2001), pp. 95–105.
[23] Fauzia Yasmeen Tani, Dewan Md Farid, and Mohammad Zahidur Rahman. “Ensemble of decision tree classifiers for mining web data streams”. In: International Journal of Applied Information Systems 1.2 (2012), pp. 30–36.
[24] Farzana Islam Adiba and Mohammad Zahidur Rahman. “Machine Learning Models to Analyze the Effect of Drugs on Neonatal-ICU Length of Stay”. In: Applied Intelligence and Informatics: Second International Conference, AII 2022, Reggio Calabria, Italy, September 1–3, 2022, Proceedings. Springer. 2023, pp. 186– 204.
[25] Farzana Islam Adiba, Sharmin Nahar Sharwardy, and Mohammad Zahidur Rahman. “Multivariate time series prediction of pediatric ICU data using deep learning”. In: 2021 International Conference on Innovative Trends in Information Technology (ICITIIT). IEEE. 2021, pp. 1–6.
[26] Suman Ahmmed et al. “Computational intelligence approach to load forecasting-a practical application for the desert of Saudi Arabia”. In: 2009 12th International Conference on Computers and Information Technology. IEEE. 2009, pp. 290–296.
[27] Suman Ahmmed et al. “STLF using Neural Networks and Fuzzy for anomalous load scenarios-A case study for Hajj”. In: International Conference on Electrical & Computer Engineering (ICECE 2010). IEEE. 2010, pp. 722–725.
[28] Tahmid Tanzi Alam, Ahmad Naquib Chowdhury, and Mohammad Zahidur Rahman. “AN intelligent road traffic management system using NVIDIA GPU”. In: 2016 19th International Conference on Computer and Information Technology (ICCIT). IEEE. 2016, pp. 419–424.
[29] Umme Sayma Busra and Mohammad Zahidur Rahman. “Mobile phone based telemedicine service for rural Bangladesh: ECG”. In: 16th Int’l Conf. Computer and Information Technology. IEEE. 2014, pp. 203–208.
[30] Partha Chakraborty et al. “How can a robot calculate the level of visual focus of human’s attention”. In: Proceedings of International Joint Conference on Computational Intelligence: IJCCI 2019. Springer. 2020, pp. 329–342.
[31] Subrata Kumar Das and Mohammad Zahidur Rahman. “A compression technique for electronic health data through encoding”. In: 2021 International Conference on Electrical, Communication, and Computer Engineering (ICECCE). IEEE. 2021, pp. 1–6.
[32] Subrata Kumar Das and Mohammad Zahidur Rahman. “A new watermarking approach for ensuring patient data authentication over a low-quality communication environment”. In: 2021 24th International Conference on Computer and Information Technology (ICCIT). IEEE. 2021, pp. 1–6.
[33] Subrata Kumar Das and Mohammad Zahidur Rahman. “A simplified architecture to integrate and interop- erate heterogeneous and distributed healthcare data”. In: 2020 23rd International Conference on Computer and Information Technology (ICCIT). IEEE. 2020, pp. 1–6.
[34] Subrata Kumar Das and Mohammad Zahidur Rahman. “A Watermarking Approach to Communicate Patient Data Securely from Distributed Sources”. In: Proceedings of the 9th International Conference on Networking, Systems and Security. 2022, pp. 23–29.
[35] Subrata Kumar Das and Mohammad Zahidur Rahman. “Middleware to Integrate Patient Data from Heterogeneous Distributed Databases and Its Efficacy”. In: 2021 International Conference on Computational Science and Computational Intelligence (CSCI). IEEE. 2021, pp. 1241–1245.
[36] Dewan Md Farid and Mohammad Zahidur Rahman. “Anomaly detection model for network intrusion detection using conditional probabilities”. In: 6th International Conference on Information Technology in Asia (CITA). 2009, pp. 104–110.
[37] Dewan Md Farid and Mohammad Zahidur Rahman. “Learning intrusion detection based on adaptive bayesian algorithm”. In: 2008 11th International Conference on Computer and Information Technology. IEEE. 2008, pp. 652–656.
[38] Dewan Md Farid et al. “Adaptive Network Intrusion Detection Learning: Attribute Selection and Classifi- cation”. In: International Conference on Computer Systems Engineering (ICCSE 2009). Ed. by WASET. Bangkok, Thailand, Dec. 2009, TH60000. URL: https://hal.science/hal-00503951.
[39] Dewan Md Farid et al. “Scaling up detection rates and reducing false positives in intrusion detection using nbtree”. In: International Conference on Data Mining and Knowledge Engineering (ICDMKE 2010). 2010, pp. 1–5.
[40] Md Rakib Hasan et al. “Reliable identity management system using Raspberry Pi”. In: 2020 2nd International Conference on Sustainable Technologies for Industry 4.0 (STI). IEEE. 2020, pp. 1–6.
[41] Mehedee Hassan and Mohammad Zahidur Rahman. “Crime news analysis: Location and story detection”. In: 2017 20th International Conference of Computer and Information Technology (ICCIT). IEEE. 2017, pp. 1–6.
 [42] Md Nazrul Islam and Mohammad Zahidur Rahman. “Electronic commerce adoption small and medium scale industry in Bangladesh”. In: 2007 10th international conference on computer and information technology. IEEE. 2007, pp. 1–5.
[43] Md Nazrul Islam and Mohammad Zahidur Rahman. “Secure online sealed bid Auction”. In: 2008 11th International Conference on Computer and Information Technology. IEEE. 2008, pp. 593–598.
[44] Md Aktaruzzaman Pramanik et al. “Performance Analysis of Classification Algorithms for Outcome Predic- tion of T20 Cricket Tournament Matches”. In: 2022 International Conference on Computer Communication and Informatics (ICCCI). IEEE. 2022, pp. 01–07.
[45] Uzzal Kumar Prodhan, Muhammad Zahidur Rahman, and Israt Jahan. “A systematic analysis on the telemedicine services in Bangladesh”. In: 1ST international conference on advanced information and communication technology. 2016.
[46] Uzzal Kumar Prodhan et al. “Development of a portable telemedicine tool for remote diagnosis of telemedicine application”. In: 2017 International Conference on Computing, Communication and Automation (ICCCA). IEEE. 2017, pp. 287–292.
[47] Uzzal Kumar Prodhan et al. “Development of a telemedicine model with low cost portable tool kit for remote diagnosis of rural people in Bangladesh”. In: 2016 International Conference on Innovations in Science, Engineering and Technology (ICISET). IEEE. 2016, pp. 1–4.
[48] Ratna R Sarkar, Amitabha Chakrabarty, and Mohammad Zahidur Rahman. “Low-End Hand Held Commu- nication Devices in a Post-Disaster Scenario”. In: 2022 14th International Conference on Computational Intelligence and Communication Networks (CICN). IEEE. 2022, pp. 595–599.
[49] Ratna R Sarkar, Amitabha Chakrabarty, and Mohammad Zahidur Rahman. “VANET Routing Protocols in Real-World Mobility Tracing”. In: 2021 13th International Conference on Computational Intelligence and Communication Networks (CICN). IEEE. 2021, pp. 96–101.
[50] Kaafi Mahmud Sarker, Israt Jahan, and Mohammad Zahidur Rahman. “Secure e-cash model using Java based smartcard”. In: 2009 12th International Conference on Computers and Information Technology. IEEE. 2009, pp. 626–631.
[51] Sharmin Nahar Sharwardy, Mohammad Zahidur Rahman, and Hasan Sarwar. “ICU Patient Status Predic- tion Using Markov Chain Model”. In: 2022 5th International Conference on Information and Computer Technologies (ICICT). IEEE. 2022, pp. 215–218.
[52] Shakila Mahjabin Tonni et al. “Securing big data efficiently through microaggregation technique”. In: 2017 IEEE 37th International Conference on Distributed Computing Systems Workshops (ICDCSW). IEEE. 2017, pp. 125–130.
[53] Kok Meng Yew, M. Zahidur Rahman, and Sai Peck Lee. “Formal Verification of Secret Sharing Protocol Using Coq”. In: Advances in Computing Science - ASIAN’99, 5th Asian Computing Science Conference, Phuket, Thailand, December 10-12, 1999, Proceedings. Ed. by P. S. Thiagarajan and Roland H. C. Yap. Vol. 1742. Lecture Notes in Computer Science. Springer, 1999, pp. 381–382. DOI: 10.1007/3-540-46674- 6\_36. URL: https://doi.org/10.1007/3-540-46674-6 5C_36.
[54] Kok Meng Yew, M. Zahidur Rahman, and Sai Peck Lee. “Mean Time Offset Protocol for Cluster of Auction Servers over TCP/IP Network”. In: Internet Applications, 5th International Computer Science Conference, ICSC’99, Hong Kong, China, December 13-15, 1999, Proceedings. Ed. by Lucas Chi Kwong Hui and Dik Lun Lee. Vol. 1749. Lecture Notes in Computer Science. Springer, 1999, pp. 323–328. DOI: 10.1007/978-3-540-46652-9\_33. URL: https://doi.org/10.1007/978-3-540-46652-9 5C_33.
"""

# Regular expression to match author list and title
pattern = r"\[\d+\]\s*(.+?)\.\s*“(.+?)”"

# Extract matches
matches = re.findall(pattern, text)

# Save data to a CSV file
with open('author_title_list_ju_3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Authors', 'Title'])  # Write the header
    for authors, title in matches:
        writer.writerow([authors.strip(), title.strip()])

print("Data saved to author_title_list.csv")
