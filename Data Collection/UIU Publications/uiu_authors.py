import re
import csv

# Provided text
text = """
Kazi Tamzid Akhter Md Hasib, Ixion Chowdhury, Saadman Sakib, Mohammad Monirujjaman Khan et al., , "Electronic Health Record Monitoring System and Data Security using Blockchain Technology," Security and Communication Networks, Impact Factor 1.791, Scopus Indexed. Accepted and due for Publication. , 2022

Mohammad Monirujjaman Khan,  Nishat Tasnim Roza et al.,, "Revolutionizing E-Commerce using Blockchain Technology and Implementing Smart Contract," Security and Communication Networks, Impact Factor 1.791, Scopus Indexed., 2022

Farjana Khanam Nishi, Zebin Mahi, Mohammad Monirujjaman Khan et al.,, "Electronic Healthcare Data Record Security Using Blockchain and Smart Contract," Journal of Sensors, Volume 2022 |Article ID 7299185 | https://doi.org/10.1155/2022/7299185. Impact Factor 2.137, 2022

AKM Bahalul Haque, Bharat Bhushan, "Emergence of Blockchain Technology: A Reliable and Secure Solution for IoT Systems," Blockchain Technology for Data Privacy Management ; Edition: 1. Chapter: 8. Publisher: CRC Press, Taylor & Francis, USA, 2021

AKM Bahalul Haque, Bharat Bhushan, "Security Attacks and Countermeasures in Wireless Sensor Network," Integration of WSNs into Internet of Things: A Security Perspective. Edition: 1st. Chapter: 2. Publisher: CRC Press, Taylor & Francis Group, USA, 2021

Tahmid Hasan Pranto​, Abdulla All Noman, Atik Mahmud, AKM Bahalul Haque​​, "Blockchain and smart contract for IoT enabled smart agriculture," PeerJ Computer Science, USA, 2021

Minhaj Uddin Chowdhury, Khairunnahar Suchana, Syed Md Eftekhar Alam, Mohammad Monirujjaman Khan, "Blockchain Application in Banking System," Journal of Software Engineering and Applications, 14, 298-311. doi: 10.4236/jsea.2021.147018. (Google Scholar)., 2021

Manoshi Das Turjo, Mohammad Monirujjaman Khan et al., , "Smart Supply Chain Management Using Blockchain and Smart Contract," Scientific Programming, vol. 2021, Article ID 6092792, 12 pages, 2021. https://doi.org/10.1155/2021/6092792, (Impact Factor 1.025 and Scopus indexed). , 2021

Mohammad Nafis Ul Islam, Ahmed Fahmin, Md Shohrab Hossain, Mohammed Atiquzzaman, "Denial-of-Service Attacks on Wireless Sensor Network and Defense Techniques," Wireless Personal Communications, 2021

Abid Hassan, MD. Iftekhar Ali, Rifat Ahammed and Mohammad Monirujjaman Khan , "Secured Insurance Framework Using Blockchain and Smart Contract," Scientific Programming, (Impact Factor 1.025 and Scopus indexed)., 2021

Lianying Zhao, Muhammad Shafayat Oshman, Mengyuan Zhang, Fereydoun Farrahi Moghaddam, Shubham Chander, Makan Pourzandi, "Towards 5G-ready Security Metrics," ICC 2021 - IEEE International Conference on Communications, 2021

AKM Bahalul Haque, Mahbubur Rahman, "Blockchain Technology: Methodology, Application and Security Issues," International Journal of Computer Science and Network Security, (WoS; ESCI Indexed), 2020

Koushik Roy , Nur Islam , Tarango Khan, Mohammad Monirujjaman Khan, "A novel Approach to Data Storage Using Blockchain Technology," 2019 International Conference on Information Technology (ICIT), 2019

Moniruz Zaman, Delwar Alam, Touhid Bhuiyan, Tanjila Farah , "A Study of the Effects of Heartbleed Vulnerability in Bangladesh," International Journal of Cyber-Security and Digital Forensics (IJCSDF), 2018

T. Farah, D. Alam, M. Zaman, and T. Bhuiyan, "A case study of Blockchain Technology," International Conference on Cyber Security and Computer Science (ICONCS 2018), 2018

10. M. S. Hossain, Sazzad Hosain, Tanjila Farah, "A Study of Cyber security threats in core banking system of Bangladesh," 7th International Conference on Software and Computing Technologies (ICSCT 2018), 2018

Rafiya Hossain, Moonmoon Ahmed, Md. Mozadded Alfasani and Hasan U. Zaman, "An Advanced Security System Integrated With RFID Based Automated Toll Collection System," Proceedings of the 3rd Asian Conference on Defence Technology (IEEE ACDT 2017), pp. 71-76, Phuket, Thailand, 18-20 January, 2017

Hasan. U. Zaman, Tarafder Elmi Tabassum, Tanha Islam, Nadia Mohammad, "Low Cost Multi-level Home Security System For Developing Countries," Proceedings of the International Conference on Intelligent Computing and Control Systems (IEEE ICICCS 2017), pp. 549-554, Madurai, India, 15-16 June, 2017

Hasan U. Zaman, Jannatul Siffat Hossain, Tasnim Tamanna Anika, Deboshree Choudhury, "RFID Based Attendance System," Proceedings of the 8th International Conference on Computing, Communication And Networking Technologies (IEEE 8th ICCCNT 2017), Delhi, India, 3-5 July, 2017

Rafiya Hossain, Moonmoon Ahmed, Hasan Uz Zaman, "A Cost Effective Security Technology Integrated with RFID Based Automated Toll Collection System," Advances in Engineering Systems, Advances in Science, Technology and Engineering Systems Journal (ASTESJ), Volume 2, Issue 3, Page No 1777-1783, 2017

Iftekharul Mobin, Nabeel Mohammed, Sifat Momen, "Optimal range estimation for energy efficient dynamic packet size," International Conference on Electrical, Computer and Communication Engineering (ECCE 2017, IEEE), 2017

Nova Ahmed, Minhaz Ahmed Syrus, Arshad Chowdhury, "Simple Group Photo Sharing Using Facesense," Computer Software and Applications Conference (COMPSAC), 2017 IEEE 41st Annual, 2017

Tanjila Farah, Rashed Shelim, Moniruz Zaman, Delwar Alam, "Study of Race Condition: A Privilege Escalation Vulnerability," Journal of Systemics, Cybernetics and Informatic (JSCI), 2017

11. D. Alam, M. Zaman, T. Farah, R. Rahman and M. S. Hosain, "Study of the Dirty Copy on Write, a Linux Kernel memory allocation vulnerability," 2017 International Conference on Consumer Electronics and Devices (ICCED), 2017

Ahmed Fahmin, Yuan-Cheng Lai, Md Shohrab Hossain, Ying-Dar Lin, Dipon Saha, "Performance modeling of sdn with nfv under or aside the controller," 2017 5th International Conference on Future Internet of Things and Cloud Workshops (FiCloudW), 2017

Md. Redwanul Hamid and Hasan U. Zaman, "A Novel Method of Identifying Errors with the Analysis of Alarms in IGW Transmission," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 98, May 13-14, 2016

Farhana Atuyar Saleh, Sadia Afrin Shopno, Hasan U. Zaman, "A Cost-effective SMS Based Tracking System Using GPS-GSM-GPRS Modules with Arduino and Smartphone," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 110, May 13-14, 2016

Tanjila Farah, Moniruzzaman Shojol, Md. Maruf Hassan, Delwar Alam, "Assessment of vulnerabilities of web applications of Bangladesh: A case study of XSS & CSRF," The Sixth International Conference on Digital Information & Communication Technology & its Applications (DICTAP2016), 2016

Iftekharul Mobin, Sifat Momen, Nabeel Mohammed, "A packet level simulation study of adhoc network with Network Simulator-2 (NS-2)," 3rd International Conference on Electrical Engineering and Information & Communication Technology (ICEEiCT-2016, IEEE), 2016

Md. Mahfuzur Rahman, Mohammad Shorfuzzaman, and Mehedi Masud, "Characterizing End-to-End Delay Performance of Randomized TCP Using an Analytical Model," In International Journal of Advanced Computer Science and Applications (IJACSA), 2016

Ahmed, N., Syrus, M.A., Chowdhury, A., "Softsense: sensing at software level," Proceedings of the 2016 ACM International Joint Conference on Pervasive and Ubiquitous Computing, 2016

S. W. Tanzid, M. H. M. Iqbal, K. M. A. Salam, and H. U. Zaman, "PSTN Connected With Wireless Multi Hop Radio Relay – A Solution for Disaster Aftermath Communication," Journal of Modern Science and Technology, vol. 3, no. 1, pp. 251 – 262, 2015

S. W. Tanzid, M. H. M. Iqbal, K. M. A. Salam and H. U. Zaman, "PSTN Connected with Wireless Multi Hop Radio Relay – A Solution for Disaster Aftermath Communication," Proceedings of 10th Global Engineering, Science and Technology Conference, BIAM Foundation, Dhaka, Bangladesh, ISBN: 978-1-922069-69-6, 2015

T. Farah, D. Alam, M. A. Kabir, T. Bhuiyan, "SQLi Penetration Testing of Financial Web Applications: Investigation of Bangladesh Region," World Congress on Internet Security (WorldCIS-2015), 2015

T. Farah, D. Alam, M. A. Kabir, T. Bhuiyan, "SQLi Penetration Testing of Financial Web Applications: Investigation of Bangladesh Region," World Congress on Internet Security (WorldCIS-2015), 2015

D. Alam, T. Farah, M. A. Kabir, "Exploring the SQL injection vulnerabilities of .bd domain web applications," 3rd International Conference on Advances in Computing, Electronics and Communication (ACEC 2015), 2015

D. Alam, T. Bhuiyan, M. A. Kabir, T. Farah, "SQLi Vulnerabilty in Education Sector Websites of Bangladesh," The Second International Conference on Information Security and Cyber Forensics (InfoSec2015), 2015

Tanjila Farah, Delwar Alam, Md. Nadir Bin Ali, Md. Alamgir Kabir, "Investigation of Bangladesh Region Based Web Applications: A Case Study of 64 Based, Local, and Global SQLi Vulnerability," IEEE International Women in Engineering (WIE) Conference on Electrical and Computer Engineering (WIECON), 2015

Touhid Bhuiyan, Delwar Alam, Tanjila Farah, "Evaluating the Readiness of Cyber Resilient Bangladesh," Journal of Internet Technology and Secured Transactions (JITST), Volume 4, Issue 1, ISSN 2046-3723, 2015

T. Farah and Lj. Trajkovic, "Anonym: a tool for anonymization of the Internet traffic," Proc. 2013 IEEE International Conference on Cybernetics (CYBCONF 2013), 2013

Iftekharul Mobin, Mohammad Monirujjaman Khan, "Energy Efficient Transmission Power Estimation for WLAN VoIP," 4th Computer Science and Electronic Engineering Conference, (CEEC), 12th-13th September 2012, University of Essex, UK. , 2012

T. Farah, S. Lally, R. Gill, N. Al-Rousan, R. Paul, D. Xu, and Lj. Trajkovic, "Collection of BCNET BGP traffic," Proc. 23rd International Teletraffic Congress, 2011

S. Lally, T. Farah, R. Gill, R. Paul, N. Al-Rousan, and Lj. Trajkovic, "Collection and characterization of BCNET BGP traffic," Proc. 2011 IEEE Pacific Rim Conference on Communications, Computers and Signal Processing, 2011

R. Gill, T. Farah, and Lj. Trajkovic, "Comparison of WiMAX and ADSL performance when streaming audio and video content," OPNETWORK 2011, 2011

Tarif Riyad Rahman, "A Dynamic Encryption Algorithm for Multicast/Broadcast Streaming Applications," 2010 Fourth Asia International Conference on Mathematical/Analytical Modelling and Computer Simulation, Kota Kinabalu, Malaysia, 2010

Tahmid Hasan Pranto​, Abdulla All Noman, Atik Mahmud, AKM Bahalul Haque​​, "Blockchain and smart contract for IoT enabled smart agriculture," PeerJ Computer Science, USA, 2021

Tousif Osman, Shahreen Shahjahan Psyche, Tonmoay Deb, Adnan Firoze, Rashedur M. Rahma, "An algorithmic approach to estimate cognitive aesthetics of images relative to ground truth of human psychology through a large user study," Journal of Information Telecommunication 3(2): 156-179, Taylor and Francis., 2019

Shuvashish Paul, Pinku Deb Nath, Naseef M. Abdus Sattar, Hasan U. Zaman, "A Web Application for Traffic Status Update using Crowd-Sourced Data Acquisition and Real-Time Modification," Journal of Theoretical and Applied Information Technology (JTAIT), 2018

M. M. Tanzim Nawaz, Mahadi Hassan, Mir Golam Rasul and Hasan U. Zaman, "Web and Mobile Based Solution to Lost and Found Items in North South University," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Hasan U. Zaman, Tawsif Ur Rahman Choudhury and Nafis Imtiaz Ahme, "A User-Friendly and Efficient Design of a Unified Online Survey and Quizzing System," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Adnan Firoze, Tonmoay Deb, Rashedur M Rahman, "Deep Learning and Data Balancing Approaches in Mining Hospital Surveillance Data," Handbook of Research on Emerging Perspectives on Healthcare Information Systems and Informatics, 2018

A. Rahman and T. Motahar, "Big Graph Analytics," Invited Chapter in "Data Analytics: Concepts, Techniques and Applications", CRC Press, USA, 2018

Kazi Toyebul Haque, M.K. Robin, Mohammad Ashraful Anam, Hasan U. Zaman, "MediPro – A Cost Effective and User-Friendly Medical Information System," Proceedings of the International Conference on Intelligent Computing and Control Systems (IEEE ICICCS 2017), pp. 919-924, Madurai, India, 15-16 June, 2017

Hasan U. Zaman, Jannatul Siffat Hossain, Tasnim Tamanna Anika, Deboshree Choudhury, "RFID Based Attendance System," Proceedings of the 8th International Conference on Computing, Communication And Networking Technologies (IEEE 8th ICCCNT 2017), Delhi, India, 3-5 July, 2017

Shuvashish Paul, Pinku Deb Nath, Naseef M. Abdus Sattar and Hasan U. Zaman, "rTraffic – A Realtime Web Application for Traffic Status Update in the Streets of Bangladesh," Proceedings of the 2017 International Conference on Research and Innovation in Information Systems (IEEE ICRIIS), pp. 1-6, Langkawi Island, Malaysia, DOI: 10.1109/ICRIIS.2017.8002457, 16-17 July, 2017

Rafiya Hossain, Moonmoon Ahmed, Hasan Uz Zaman, "A Cost Effective Security Technology Integrated with RFID Based Automated Toll Collection System," Advances in Engineering Systems, Advances in Science, Technology and Engineering Systems Journal (ASTESJ), Volume 2, Issue 3, Page No 1777-1783, 2017

Adnan Firoze, Rashedur M Rahman, "Critical condition classification of patients from ICCDR, B hospital surveillance data," International Journal of Advanced Intelligence Paradigms, 2017

Romasa Qasim, G. M. Sayedur Rahman, Nahid Hasan and M. Shazzad Hosain, "An In-silico Pharmacophore-Based Anti-Viral Drug Development for Hepatitis C Virus," ICDDPR 2017: International Conference on Drug Discovery and Preclinical Research, Melbourne, Australia, Feb 02-03, 2017

Syed Emdad Ullah, Tania Alauddin and Hasan U. Zaman, "Developing an E-Commerce Website," Proc. of Intl. Conference on Microelectronics, Computing and Communication (IEEE MicroCom 2016), Durgapur, India, January 23-25, 2016

A. Rahman, S. Jan, H. Kim, B. A. Prakash, and T. M. Murali, "Unstable Communities in Network Ensembles," 16th SIAM conference on Data Mining (SDM), 2016

M. Arabi Hasan Sakib, Fakhrul Islam, Sabbir Samiul Haque, Hasan U. Zaman, "Doctor Locator: A Web Application to Improve Online Doctor Directories in Bangladesh," 5th International Conference on Informatics, Electronics & Vision (IEEE ICIEV), Dhaka, Bangladesh, paper no. 118, May 13-14, 2016

Faridur Rahman Hridoy, Kallal Das, Rifayat Hossain Arko and Hasan U. Zaman, "Development of an Online Bus Ticket Booking System for Transportation Services in Bangladesh," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 33, May 13-14, 2016

Syed Naffiz Hasan, Arka Basak, Sheefta Naz and Hasan U. Zaman, "The Online Laundry System," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 31, May 13-14, 2016

Hasan U. Zaman, Tawsif Ur Rahman Choudhury, Nafis Imtiaz Ahmed, "A Unified Online Survey and Quizzing System," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 109, May 13-14, 2016

Umme Hafsa Billah, Sheikh Muhammad Sarwar, Abdullah-Al-Mamun, "Personalized Language Models for Computer-mediated Communication," In Proceedings of 3rd International Workshop on Concept Discovery in Unstructured Data (workshop co-located with the 13th International Conference on Concept Lattices and Their Applications), p. 2-12, 2016

Shareen Mahmud, Nabila Rezwana Mirza and Md. Shazzad Hosain, "Tapping the Power of Social Network Analysis for One Bank Limited Bangladesh," 3rd European Conference on Social Media Research, Caen, France, Jul 12 – 13, 2016

Sayed Mahmudul Alam, Nahid Islam and Shazzad Hosain, "Most Central Actors of an Unknown Network Using Friendship Paradox," International Conference on Informatics and Computing (ICIC 2016), Lombok, Indonesia, Oct 28 – 29, 2016

Moinul Hossain, Nova Ahmed, Mahfuzur Rahman Siddique, Refaya Karim, Mohsina Zaman, Rifat Monzur, "Map Matching on Sparse GPS Data: A Perspective of a Developing City," Eastern Asia Society for Transportation Studies, 2015

Syed Jishan, Raisul Rashu, Naheena Haque, Rashedur M Rahman, "Improving accuracy of students’ final grade prediction model using optimal equal width binning and synthetic minority over-sampling technique," Decision Analytics, 2:1, pp.1-25, Springer, 2015

Shayanton Aurkaw, Rudraneel Chakraborty, Shazzad Hosain, "Autonomous Data Integration Model Using Integra Data Model," International Conference on Materials, Electronics & Information Engineering (ICMEIE-2015), Rajshahi, Bangladesh, June , 2015

Syed Akib Anwar Hridoy, M Tahmid Ekram, Mohammad Samiul Islam, Faysal Ahmed, Rashedur M Rahman, "Localized twitter opinion mining using sentiment analysis," Decision Analytics, 2:8, pp.1-19, Springer, 2015

Md Mahfuzur Rahman Siddiquee, Md. Saifur Rahman, Naimul Haider, Rashedur M. Rahman, Shahnewaz Ul Islam Chowdhury, Sharnendu Banik, "A personalized music discovery service based on data mining," 14th IEEE/ACIS International Conference on Computer and Information Science, ICIS 2015,USA, June 28 - July 1, pp.253-258, 2015

Mohammed Rashid Chowdhury, Mohammad Raihan Mahmud, Rashedur M. Rahman, "Clustered based VM placement strategies," 14th IEEE/ACIS International Conference on Computer and Information Science, ICIS 2015,USA, June 28 - July 1, pp.247-252, 2015

Ruhul Amin Dicken, S. A. M. Fazle Rubby, Sheefta Naz, A. M. Arefin Khaled, Shuvo Ashish Rahman, Sharmina Rahman, Rashedur M. Rahman, "Analysis and classification of respiratory health risks with respect to air pollution levels," 16th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2015, Takamatsu, Japan, June 1-3, 2015

Fahim Jawad, Tawsif Ur Rahman Choudhury, Ahmad Najeeb, Mohammed Faisal, Fariha Nusrat, Rubaiya Chamon Shamita, Rashedur M. Rahman, "Data mining techniques to analyze the reason for home birth in Bangladesh," 16th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2015, Takamatsu, Japan, June 1-3, pp.225-231, 2015

Adnan Firoze, Rashedur M Rahman, "Mining ICDDR, B Hospital Surveillance Data Using Locally Linear Embedding Based SMOTE Algorithm and Multilayer Perceptron," 7th Asian Conference on Intelligent Information and Database Systems, Lecture Notes in Computer Science 9011, pp.398-407, Springer, 2015

Adnan Firoze, Rashedur M. Rahman, "Mining ICDDR, B Hospital Surveillance Data and Exhibiting Strategies for Balancing Large Unbalanced Datasets," International Journal of Healthcare Information Systems and Informatics (IJHISI), 2015

Adnan Firoze, Rashedur M Rahman, "Mining ICDDR, B Hospital Surveillance Data Using Locally Linear Embedding Based SMOTE Algorithm and Multilayer Perceptron," Lecture Notes in Computer Science (Springer), 2015

A. Rahman, S. Jan, H. Kim, B. A. Prakash, and T. M. Murali, "Mining Unstable Communities from Network Ensembles," 5th IEEE Workshop on Data Mining in Networks, 2015

Mridul Khan, A. K. M. Zahiduzzaman, Mohammad Nahyan Quasem, Rashedur M. Rahman, "Geospatial Data Mining on Education Indicators of Bangladesh," I. J. Comput. Appl. 20(1): 10-22, 2013

Mohammad Alaul Haque Monil, Romasa Qasim, Rashedur M. Rahman, "Speed and direction based fuzzy handover system," 22nd IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), 2013

A. Rahman, C. L. Poirel, D. J. Badger, C. Estep, T. M. Murali, "Reverse Engineering Molecular Hypergraphs," IEEE/ACM Transactions on Computational Biology and Bioinformatics (TCBB), 2013

C. L. Poirel, A. Rahman, R. Rodrigues, A. Krishnan, J. R. Addesa, T. M. Murali, "Reconciling Gene Expression Data with Molecular Interaction Networks," Bioinformatics, 2013

Shamsul Arifin, Adnan Firoze, M. Ashraful Amin, Hong Yan, "Dermatological Disease Diagnosis using Color-skin Images," International Conference on Machine Learning and Cybernetics (ICMLC), 2012

A. Rahman, C. L. Poirel, D. J. Badger, and T. M. Murali, "Reverse Engineering Molecular Hypergraphs," ACM Conference on Bioinformatics, Computational Biology and Biomedicine (ACM BCB), Orlando, FL, 2012., 2012

Rashedur M Rahman, Fazle R. Hasan, "Using and Comparing Different Decision Tree Classification Techniques for Mining ICDRR,B Hospital Surveillance Data," Expert Systems with Applications: 38(9), pp. 11421-11436, Elsevier Science (IF:6.954), 2011

Ehtesham Choudhury, Mahmud Ridwan, M Abdul Awal, Shazzad Hosain, "A Web-based Land Management System for Bangladesh," 14th International Conference on Computer and Information Technology (ICCIT 2011), Dhaka, Bangladesh, December, 2011

Rudraneel Chakraborty, Faiyaz Ahmed, Shazzad Hosain, "CASM: Coherent Automated Schema Matcher," International Conference on Data Engineering and Internet Technology, Bali, Indonesia, March, 2011

M Sultan Mahmud, Saad Abdullah, Shazzad Hosain, "GWDL: A Graphical Workflow Definition Language for Business Workflows," International Conference on Data Engineering and Internet Technology, Bali, Indonesia, March , 2011

Shazzad Hosain and Hasan Jamil, "An Algebraic Language for Semantic Data Integration on the Hidden Web," 3rd IEEE International Conference on Semantic Computing, Berkeley, California, United States, September, 2009

Shazzad Hosain and Hasan Jamil, "OWL that can Choose to Inherit and Hide it Too," 3rd IEEE International Conference on Semantic Computing, Berkeley, California, United States, September, 2009

Shazzad Hosain, Hasan Jamil, "Algebraic Operator Support for Semantic Data Fusion in Extended SQL," 8th IEEE International Conference on Cybernetic Intelligent Systems (UK and Ireland Chapter), University of Birmingham, Birmingham, UK, September , 2009

Anupam Bhattacharjee, Aminul Islam, Mohammad Shafkat Amin, Shahriyar Hossain, Shazzad Hosain, Hasan Jamil and Leonard Lipovich, "On-the-fly Integration and ad hoc Querying of Life Sciences Databases using LifeDB," 20th International Conference on Database and Expert Systems Applications, Linz, Austria, 2009

Shazzad Hosain and Hasan Jamil, "Empowering OWL with Overriding Inheritance, Conflict Resolution and Non-monotonic Reasoning," AAAI-SSS-09: Social Semantic Web: Where Web 2.0 Meets Web 3.0, pp. 53 - 58, Stanford, CA, USA, 2009

Anupam Bhattacharjee, Aminul Islam, Mohammad Shafkat Amin, Shahriyar Hossain, Shazzad Hosain and Hasan M. Jamil, "LifeDB: An Autonomous System for Semantic Integration of Life Science Data on Hidden Web," Semantic Web Applications and Tools for Life Sciences, 2008

Munirul Islam, Shazzad Hosain, Hasan M. Jamil, Morris Goodman and Derek E. Wildman, "Phoenix: A Tool for Estimating Species Divergence Times," OCCBIO, Ohio Collaborative Conference on Bioinformatics, 2008

Md. Shazzad Hosain and Md. Shamsul Alam, "Single Action Reliability Model for Application Software System," International Conference on Computing and Informatics, Kuala Lumpur, Malaysia, June , 2006

Md. Shazzad Hosain and Muhammad Abdul Hakim Newton, "Multi-Key Index for Distributed Database System," International Journal of Software Engineering and Knowledge Engineering, 2005

Rashik Iram Chowdhury, Jareen Anjom, Md. Ishan Arefin Hossain, "A novel edge intelligence-based solution for safer footpath navigation of visually impaired using computer vision," Journal of King Saud University - Computer and Information Sciences, 2024

Kazi Atique Moula Nabil, Md. Ariful Islam, Abdullah Al Noman and Mohammad Monirujjaman Khan, "Development of A Smart Non-Invasive Glucose Monitoring System With SpO2 and BPM for Diabetic Patient," The IEEE 13th Annual Computing and Communication Workshop and Conference (CCWC), 8-11 March, 2022., 2023

Balwinder Raj, B Gupta, B Gupta Shalendra Singh and Mohammad Monirujjaman Khan, "Distributed Intelligent Circuits and Systems," World Scientific, https://doi.org/10.1142/13505, ISBN: 978-981-127-952-2 , 2023

Md. Ishan Arefin Hossain, Anika Tabassum, Zia Ush Shamszaman, "Deep edge intelligence-based solution for heart failure prediction in ambient assisted living," Discover Internet of Things, 2023

Md. Ishan Arefin Hossain, Ahmed Kiser, Israt Jahan Mitu, Syeda Mahin Binta Haque, "Intelligent IoT-based Combined Crop-type and Disease Prediction System with Different Machine Learning & Deep Learning Techniques," 10th International Conference on Electrical Engineering, Computer Science and Informatics (EECSI), 2023

Md. Amdadul Bari and Mohammad Monirujjaman Khan, "Development of an IoT Based Health Monitoring System for e-Health," The 12th Annual Computing and Communication Workshop and Conference (CCWC), 26-29 January 2022, USA. Accepted and due for publication., 2022

Ajan Ahmed and Mohammad Monirujjaman Khan, "Smart Helmet With Rear View and Accident Detection System for Increased Safety," The 12th Annual Computing and Communication Workshop and Conference (CCWC), 26-29 January 2022, USA, 2022

Md. Khairul Islam,  Md. Farabi Alam,  AbidIbna Zahid, Mohammad Monirujjaman Khan et al.,, "Internet of Things (IoT) Based Real-time Vital Physiological Parameters Monitoring System for Remote Asthma Patients," Wireless Communications and Mobile Computing, Impact Factor 2.336. Accepted and due for publication. , 2022

Ajan Ahmed, Mohammad Monirujjaman Khan, Parminder Singh, Ranbir Singh Batth et al.,, "IoT-Based Real-Time Patients Vital Physiological Parameters Monitoring System Using Smart Wearable Sensors," Neural Computing and Applications, Springer, Impact Factor 5.606. Journal Ranking Q1. Accepted and due for publication., 2022

Abdur Rab Dhruba, Kazi Nabiul Alam, Md Shakib Khan, Mohammad Monirujjaman Khan et al.,, "IoT Based Water Quality Assessment System for Industrial Waste Water: Healthcare Perspective," Journal of Healthcare Engineering, Hindawi, Impact Factor 2.682, Scopus Indexed. Accepted and due for publication., 2022

Mohammad Monirujjaman Khan et al., , "IoT Based Health Monitoring System Development and Analysis," Security and Communication Networks, Impact Factor 1.791, Scopus Indexed. Accepted and due for Publication, 2022

Md. Shovon Uz Zaman Siddique, Siddhartha Mohammad, Tapesh Bhowmick, and Mohammad Monirujjaman Khan , "Development of Low-cost GPS Tracker System for Coastal Area of Bangladesh," 6th International Conference on Computing Methodologies and Communication (ICCMC), 29-31 March 2022, pp. 1534-1539, doi: 10.1109/ICCMC53470.2022.9754036., 2022

Md. Fahim Inzamam Ul Haque, Sadia Sabina, Mohammad Monirujjaman Khan, "Arduino based Smart Design of a Cheaper and Portable Automated Cardiopulmonary Resuscitation (CPR) Device," 2022 6th International Conference on Computing Methodologies and Communication (ICCMC), 2022, pp. 1098-1105, doi: 10.1109/ICCMC53470.2022.9754034., 2022

Mehedi Hasan Anik, Mozammal Haque, Fazla Rabbi Sajid, Mohammad Monirujjaman Khan, "Design of IoT based Weather Monitoring System," 2022 6th International Conference on Computing Methodologies and Communication (ICCMC), 2022, pp. 1-7, doi: 10.1109/ICCMC53470.2022.9753911., 2022

Md. MobinHossain, Nazira Mukta, Nelima Akter, Tahia Tazin, Faria Soroni, Mohammad Monirujjaman Khan, "Microcontroller and Mobile App based Garments Environment Monitoring System for Workers," 2022 6th International Conference on Computing Methodologies and Communication (ICCMC), 2022, pp. 616-622, doi: 10.1109/ICCMC53470.2022.9754110., 2022

Md. Tanvir Hossain, Mohammad Ismail Hossain, K. M. Shihab Hossain, Mohammad Monirujjaman Khan, "Development of Wireless Electrocardiogram, Body Temperature and Blood Oxygen Level Monitoring System," 2022 6th International Conference on Computing Methodologies and Communication (ICCMC), 2022, pp. 394-399, doi: 10.1109/ICCMC53470.2022.9753852., 2022

Nafisa Shamim Rafa,  Basma Binte Azmal,  Abdur Rab Dhruba, Mohammad Monirujjaman Khan et al.,, "IoT Based Remote Health Monitoring System Employing Smart Sensors for Asthma Patients During COVID-19 Pandemic," Wireless Communications and Mobile Computing, Impact Factor 2.336, 2022

Ferdaus Ahmed, Zarin Tasnim, Masud Rana and Mohammad Monirujjaman Khan, "Development of Low Cost Smart Cane with GPS," IEEE World AI IoT Congress 2022, Seattle USA, 6-9 June, 2022., 2022

Asif Rahman, Safiyatul Hoque, Md. Sakibe Ullah, Abdur Rab Dhruba and Mohammad Monirujjaman Khan, "IoT Based Postoperative Heart Disease Patient Monitoring System," 2022 IEEE 12th Annual Information Technology, Electronics and Mobile Communication Conference (IEEE IEMCON), 12-15 October, Vancouver, Canada. Scopus Indexed. Accepted and due for publication., 2022

AKM Bahalul Haque, Bharat Bhushan, "Emergence of Blockchain Technology: A Reliable and Secure Solution for IoT Systems," Blockchain Technology for Data Privacy Management ; Edition: 1. Chapter: 8. Publisher: CRC Press, Taylor & Francis, USA, 2021

AKM Bahalul Haque, Bharat Bhushan, "Security Attacks and Countermeasures in Wireless Sensor Network," Integration of WSNs into Internet of Things: A Security Perspective. Edition: 1st. Chapter: 2. Publisher: CRC Press, Taylor & Francis Group, USA, 2021

Mohammad Monirujjaman Khan, Nazifa Tasneem and Yakut Marzan, "Fastest Finger First – Educational Quiz Buzzer’ Using Arduino and Seven Segment Display for Easier Detection of Participants," IEEE 11th Annual Computing and Communication Workshop and Conference (IEEE CCWC), 27th-30th January 2021, USA. pp. 1093-1098, doi: 10.1109/CCWC51732.2021.9376139., 2021

AKM Bahalul Haque; Ayman Muniat; Parisha Rafiq Ullah; Shimin Mushsharat, "An Automated Approach towards Smart Healthcare with Blockchain and Smart Contracts," 2021 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS), 2021

Tahmid Hasan Pranto​, Abdulla All Noman, Atik Mahmud, AKM Bahalul Haque​​, "Blockchain and smart contract for IoT enabled smart agriculture," PeerJ Computer Science, USA, 2021

A K M Bahalul Haque, Md Rifat Hasan, Md. Oahiduzzaman Mondol Zihad , "SmartOil: Blockchain and Smart Contract-based Oil Supply Chain Management," IET Blockchain, The Institution of Engineering and Technology, UK, 2021

Md. Talat Mahmud, Md. Mujtabir Alam, Md. Ashik Amin et a., , "Design of a Low-Cost Wearable Heart and Respiratory Rate Measurement Device Using an Arduino and Bluetooth Module," The 12th International Conference On Computing, Communication and Networking Technologies (ICCCNT), July 6 - 8, IIT - Kharagpur, West Bengal, India. Conditional acceptance. , 2021

Syeda Ramisa Masum, Syed Hasan Selim, Faria Soroni, Zubair Hossain, Mohammad Monirujjaman Khan et al., , "‘BACHAO’ A One Click Personal Safety Device," The 12th International Conference On Computing, Communication and Networking Technologies (ICCCNT), July 6 – 8, IIT – Kharagpur, West Bengal, India. (Accepted)., 2021

Md. Talat Mahmud, Faria Soroni, Mohammad Monirujjaman Khan et al., , "Development of Smart Height Measuring Scale," The 12th International Conference On Computing, Communication and Networking Technologies (ICCCNT), July 6 – 8, IIT – Kharagpur, West Bengal, India. (Accepted)., 2021

Dipta Voumick, Prince Deb, Mohammad Monirujjaman Khan, "Operation and Control of Microgrids using IoT (Internet of Things)," Journal of Software Engineering and Applications, 14, 418-441. doi: 10.4236/jsea.2021.148025., (Google Scholar). , 2021, 2021

Abu Taher Tamim1, Halima Begum, Sumaiya Ashfaque Shachcho, Mohammad Monirujjaman Khan et al., , "Development of IoT Based Fish Monitoring System for Aquaculture," Intelligent Automation & Soft Computing, Tech Science Press. (Accepted and due for publication). (Impact Factor 1.647, Scopus Indexed), , 2021

Sifat Azad, Saddatul Alam, Md.Moniruzzaman, Tahia Tazin and Mohammad Monirujjaman Khan, "Metro Rail Tracking System in Bangladesh," 2021 IEEE 12th Annual Information Technology, Electronics and Mobile Communication Conference (IEEE IEMCON), 27-30 October, Vancouver, Canada. Scopus Indexed. Accepted and due for publication. , 2021

Faria Soroni and Mohammad Monirujjaman Khan et al.,, "Development of a Toxic Food Ingredients Detector," 2021 IEEE 12th Annual Information Technology, Electronics and Mobile Communication Conference (IEEE IEMCON), 27-30 October, Vancouver, Canada. Scopus Indexed. Accepted and due for publication. , 2021

Md. Talat Mahmud, Faria Soroni, Saikat Chandra Das, Md Shahadat Bhuiyan, Md. Shariful Islam, Mohammad Monirujjaman Khan, Ratil H. Ashique , "Development of a Smart Automatic Gas Leakage Detector and Alarming System," 2021 IEEE 12th Annual Information Technology, Electronics and Mobile Communication Conference (IEEE IEMCON), 27-30 October, Vancouver, Canada. Scopus Indexed. Accepted and due for publication.,, 2021

Anika Khanom, Mohammad Rezaul Islam, Md. Saiful Isalm, Md. Rezaul Kawser Talukder, SM Tanmoy Rahman Khan, Mohammad Monirujjaman Khan, "Electronic iDrop Aid: Servo Motor Based Arduino Controlled Automated Solution for Disposal of iDrop," 2021 IEEE 12th Annual Information Technology, Electronics and Mobile Communication Conference (IEEE IEMCON), 27-30 October, Vancouver, Canada. Scopus Indexed. Accepted and due for publication., 2021

Abdur Rab Dhruba, Kazi Nabiul Alam, Md Shakib Khan, Sami Bourouis and Mohammad Monirujjaman Khan, "Development of an IoT Based Sleep Apnea Monitoring System for Healthcare Applications," Computational and Mathematical Methods in Medicine (Scopus Indexed and Impact Factor 2.238). Accepted and due for publication., 2021

Safia Mehnaz ,  Antu Shaha,  Md. Nayem, Sami Bourouis and Mohammad Monirujjaman Khan , "IoT Based Smart Health Monitoring System for COVID-19 Patients," Computational and Mathematical Methods in Medicine (Scopus Indexed and Impact Factor 2.238). Accepted and due for publication., 2021

Tanjir Arafat, MD Anisur Zaman and Mohammad Monirujjaman Khan , "A Voltage Producing Smart Wheelchair Development With Heartbeat Monitoring System," 2021 IEEE 12th Annual Ubiquitous Computing, Electronics and Mobile Communication Conference (IEEE UEMCON), 1-4 December, New York, USA. Accepted and due for publication., 2021

Md. Ibtida Fahim, Nowshin Tabassum, Abrar Ahamed Habibullah, Aritra Sarker and Mohammad Monirujjaman Khan , "Design of an IoT Based Gas Wastage Monitoring, Leakage Detecting and Alerting System," 2021 IEEE 12th Annual Ubiquitous Computing, Electronics and Mobile Communication Conference (IEEE UEMCON), 1-4 December, New York, USA Accepted and due for publication., 2021

Md Abu Obaidah, Sayeda Islam Nahid and Mohammad Monirujjaman Khan, "Research and Development of Wireless Smart Temperature and Humidity Monitoring System via Bluetooth Module and Mobile Application," 2021 IEEE 12th Annual Ubiquitous Computing, Electronics and Mobile Communication Conference (IEEE UEMCON), 1-4 December, New York, USA Accepted and due for publication., 2021

Md. Abu Obaidah, Faria Soroni and Mohammad Monirujjaman Khan, "Development of a Hybrid Power Generation System," 2021 IEEE 12th Annual Ubiquitous Computing, Electronics and Mobile Communication Conference (IEEE UEMCON), 1-4 December, New York, USA. Scopus Indexed. Accepted and due for publication., 2021, 2021

Syed Safiul Arman, Md. Amdadul Bari and Mohammad Monirujjaman Khan, "Development of Security System for Ready Made Garments (RMG) Industry in Bangladesh," 2021 IEEE 12th Annual Ubiquitous Computing, Electronics and Mobile Communication Conference (IEEE UEMCON), 1-4 December, New York, USA Accepted and due for publication, 2021

S.M. Shahidur Harun Rumy, Md. Ishan Arefin Hossain, forji Jahan, Tanijna Tanvin, "An IoT based System with Edge Intelligence for Rice Leaf Disease Detection using Machine Learning," IEEE International IOT, Electronics and Mechatronics Conference (IEMTRONICS), 2021

Mariha Afroz, Nazia Hasan, Md. Ishan Arefin Hossain, "IoT Based Two Way Safety Enabled Intelligent Stove with Age Verication Using Machine Learning," International Conference on Computer Communication and Informatics (ICCCI), 2021

Rezowana Akter, Jahid Khandaker, Shakil Ahmed, Muhtasim Munem Mugdho, A K M Bahalul Haque, "RFID Based Smart Transportation System With Android Application," International Conference on Innovative Mechanisms for Industry Applications (ICIMIA 2020), IEEE & Scopus Indexed, 2020

A K M Bahalul Haque, Shawan Shurid, Afsana Tasnim, Md. Shadman Sadique, Abu Sayem Mohammad Asaduzzaman, "A Novel Design of Gesture and Voice Controlled Solar-Powered Smart Wheel Chair with Obstacle Detection," IEEE International Conference on Informatics, IoT, and Enabling Technologies (ICIoT’20), 2020

Mohammad Monirujjaman Khan, Tahia Tazin, Tabia Hossain, "Development of Wireless Monitoring System for Pulse Rate: A New Approach," 1st International Electronic Conference on Applied Sciences, 10－30 November 2020, Multidisciplinary Digital Publishing Institute (MDPI). Proceedings 2020, 67(1), 13, 2020. https://www.mdpi.com/2504-3900/67/1/13, 2020

Mohammad Monirujjaman Khan, Md. Mujtabir Alam, "Research and Development of A Low Cost Smart Cardio Pulmonary Resuscitation (CPR) Device Using Locally Available Raw Materials for Cardiac Arrest Patients," 1st International Electronic Conference on Applied Sciences, 15－30 November 2020, Multidisciplinary Digital Publishing Institute (MDPI). Proceedings 2020, 67(1), 10,2020. https://www.mdpi.com/2504-3900/67/1/10, 2020

Mohammad Monirujjaman Khan, Md. Ibtida Fahim, Abrar Ahamed Habibullah, Nowshin Tabassum, Aritra Sarker, "Research and Development of Smart Internet of Things Based System to Monitor and Prevent House Hold Gas Wastage," 1st International Electronic Conference on Applied Sciences, 15－30 November 2020, Multidisciplinary Digital Publishing Institute (MDPI). Proceedings 2020, 67(1), 11 , 2020. https://www.mdpi.com/2504-3900/67/1/11, 2020

Mohammad Monirujjaman Khan, "IoT Based Smart Healthcare Services for Rural Unprivileged People in Bangladesh: Current Situation and Challenges," 1st International Electronic Conference on Applied Sciences, 15－30 November 2020, Multidisciplinary Digital Publishing Institute (MDPI). (doi:10.3390/ASEC2020-07535)https://sciforum.net/paper/view/7535, 2020

Mohammad Monirujjaman Khan, "Sensor Based Gas Leakage Detector System," 7th Electronic Conference on Sensors and Applications, 15－30 November 2020, Multidisciplinary Digital Publishing Institute (MDPI). Eng. Proc. 2020, 2(1), 28, 2020. https://www.mdpi.com/2673-4591/2/1/28, 2020

Mohammad Monirujjaman Khan, Tahia Tazin, Fazle Rabbi Mithun, Tasnova Tabassum, Md Adnan Chowdhury, "Wireless Sensor Network Based Epileptic Seizure Detector," the 7th Electronic Conference on Sensors and Applications, 15－30 November 2020. Multidisciplinary Digital Publishing Institute (MDPI) Eng. Proc. 2020, 2, 89., 2020. https://www.mdpi.com/2673-4591/2/1/89, 2020

Mohammad Monirujjaman Khan, "An IoT Based Smart Water Monitoring System for Fish Firming in Bangladesh," the 5th International Electronic Conference on Water Sciences (ECWS-5) 16－30 November 2020, Multidisciplinary Digital Publishing Institute (MDPI). (doi:10.3390/ECWS-5-08044)., 2020

AKM Bahalul Haque, Sonia Tasmin, "Security Threats and Research Challenges of IoT – A Review," Journal of Engineering Advancements, 2020

Ahmed Rohani Islam, Kajol Bhowmick, Debalina Sikder, Hasan U. Zaman, "A Multifarious Design of a Microcontroller Based Home Security and Automation System," IEEE International Conference on Computational Intelligence and Communication Networks (CICN-2019), Hawaii, USA, 3-6 January, 2019

Rafaeal Hossain Rakin, Asad Siam, Md. Rafayet Hossain, Hasan U. Zaman, "A Low-Cost and Portable Electrocardiogram (ECG) Machine for Preventive Diagnosis," International Conference on Robotics, Electrical and Signal Processing Techniques (ICREST), Dhaka, Bangladesh, 10-12 January, 2019

Md. Aowrongajab Uaday, Md. Nazmul Islam Shuzan, Saffan Shanewaze, Rakibol Islam Rakib and Hasan U Zaman, "The Design of a Novel Multi-Purpose Fire Fighting Robot with Video Streaming Capability," IEEE Sponsored 2019 5th International Conference for Convergence in Technology (IEEE 5th I2CT 2019 Pune), Pune, India, 29 -31 March, 2019

Ekra Bin Syed Mojib, AKM Bahalul Haque, Md. Nafis Raihan, Mahbubur Rahman , Fahad Bin Alam, "A Novel Approach for Border Security; Surveillance Drone with Live Intrusion Monitoring," 2019 IEEE International Conference on Robotics, Automation, Artificial-intelligence and Internet-of-Things (RAAICON), 2019

Md. Mujtabir Alam ; Md. Ashik Amin ; Mahamud Hussain ; Rokibul Hasan Bhuiyan ; Mohammad Monirujjaman Khan, "Design of Piston-Driven Automated Cardiopulmonary Resuscitation Device with Patient Monitoring System," International Conference on Robotics,Electrical and Signal Processing Techniques (ICREST), 2019

Md. Ishan Arefin Hossain, Mridul Banik, Ismail Hossain, Md. Ashraful Alam, "IOT based Autonomous Class Attendance System using Non-Biometric Identification," Joint 7th International Conference on Informatics, Electronics & Vision (ICIEV) and 2nd International Conference on Imaging, Vision & Pattern Recognition (icIVPR), 2019

Md. Yousuf Hossain, Ismail Hossain, Mridul Banik, Md. Ishan Arefin Hossain, Amitabha Chakrabarty, "Embedded System based Bangla Intelligent Social Virtual Robot with Sentiment Analysis," Joint 7th International Conference on Informatics, Electronics & Vision (ICIEV) and 2nd International Conference on Imaging, Vision & Pattern Recognition (icIVPR), 2019

Mohd. Tahsin Bin Mostafa, Shah Md. Tanzim Alam Choudhury, Md. Shazzad Hosain, "Design and performance Analysis of a Dual Axis Solar Tracker," IEEE 1st International Conference on Energy, Systems and Information Processing (ICESIP), Chennai, India, July 04 - 06, 2019

Hasan U. Zaman, Rafiunnisa, Arafat Muhammad Shams, "A User-Friendly Low-Cost Mobile App Based Home Appliance Control And Circuit Breaker," 2nd International Conference on Computing Methodologies and Communication (IEEE ICCMC 2018), Erode, India, 2018

Mohammad Abu Sayed, Nusrat Jahan Prithee, Md Al Imran, Hossain M. Mahbub and Hasan U. Zaman, "A Prominent Robotic Mechanism for Agricultural Inspection," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Mohammad Abu Sayed, Nusrat Shams and Hasan U. Zaman, "An IoT Based Robotic System for Irrigation Notifier," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Hasan U. Zaman, Raihanul Haque and Abdur Rahman, "A Low Cost DC Powered Three Wheeled Electric Scooter," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Hasan U. Zaman, Khalida Sultana Shuravi, Muntasir Kabir Sakib and Mohammad Wasee Sarwar, "A Low Cost Wireless Braille System Hand Glove for Real Time Communication," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Sanita Rahman, Emdadul Haque, Mahmudur Rahman and Hasan U. Zaman, "A Web-based Appliance Control and Gas Safety System with Security," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Md. Waliur Rahman, M. Farhanul Ihsan and Hasan U. Zaman, "A Framework for Wireless Remote Control of Power System Substations based on Sensor Data using GSM Networks," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Nazmul Islam, Rakibul Islam, Juwel Rana and Hasan U Zaman, "Dual-Powered Automatic Peltier Effect Cooler," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Mohammad Abu Sayed, Nusrat Jahan Prithee, Hasan U. Zaman, "Robotic Helping Hand: A New Mechanism for Helping Disabled People," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

T Farah, R Shelim, M Zaman, MM Hassan, D Alam, "Study of a Privilege Escalation Vulnerability in UNIX like system: Race Condition," Journal of Systemics, Cybernetics and Informatics, JSCI (scopus indexed), 2018

Mohammad Abdul Hye, Md Manjurul Akter, Atiq Mohammad Jahangir and Hasan U. Zaman, "A Novel Design and Implementation of Automated Feeding Mechanism in Fish Aquariums," 2nd International Conference on Electronics, Materials Engineering and Nano-Technology (IEEE IEMENTech 2018), Kolkata, India, 4-5 May, 2018

Kazi Kowshin Raihana, Md. Sabbir Hossain, Md. Tahsan Dewan, Hasan U. Zaman, "Auto-Moto Shoes: An Automated Walking Assistance for Arthritis Patients," 2nd International Conference on Electronics, Materials Engineering and Nano-Technology (IEEE IEMENTech 2018), Kolkata, India, 4-5 May, 2018

Md. Rezaul Islam Md. Didarul Islam Sujon, Rumman Nasir, Mahbube Mozammel Ibne Habib, Majedul Islam Nomaan, Jayasree Baidya, "Agribot: Arduino Controlled Autonomous Multi-Purpose Farm Machinery Robot for Small to Medium Scale Cultivation," 2018 International Conference on Intelligent Autonomous Systems, 2018

Nixon Dutta, Joyeta Saha, Faysal Sarker and Hasan U. Zaman, "A Novel Design of a Multi-DOF Mobile Robotic Helping Hand for Paralyzed Patients," 2018 International Conference on Advances in Computing, Communications and Informatics (IEEE ICACCI 2018), Bangalore, Karnataka, India, 19-22 September, 2018

Sarfaraz Ahmed, Tahsin Sadia, Mahir Ashab Ahmed Kushal, Tanzilur Rahman, "Cost and Energy Efficient Solution for Solid Waste Bin Monitoring and Analysis," IEEE SiPS'18, 2018

Saadman Shahid Chowdhury, Atiar Talukdar,Ashik Mahmud, Tanzilur Rahman,, "Domain Specific Intelligent Personal Assistant with Bilingual Voice Command Processing," IEEE TENCON'18, 2018

M. Mubarak Hossain, Tanzilur Rahman, , "Cost Effective Micro Milling Machine for Prototyping Plastic Microfluidic Devices," Eurosensors 2018, 2018

Saadman Shahid Chowdhury, Atiar Talukdar,Ashik Mahmud, Tanzilur Rahman,, "Domain Specific Intelligent Personal Assistant with Bilingual Voice Command Processing," IEEE TENCON'18, 2018

Hasan U. Zaman, Saif Mahmood, Sadat Hossain and Iftekharul Shovon, "Python based Portable Virtual Text Reader," 4th International Conference on Advances in Computing, Communication and Automation (IEEE ICACCA-2018), Subang Jaya, Selangor,, Malaysia, October 26-28, 2018

Hasan U. Zaman, Tarek Ahmed Khan, Shakila Reza Falgunee, GM Shaheedur Rashid and Fahim Hossain Talukder, "Autonomous Firefighting Robot with Optional Bluetooth Control," 4th IEEE International Conference on Computing Communication and Automation (ICCCA-2018), Greater Noida, India, 14-15 December, 2018

Md. Solaiman Chowdhury, Md. Abu Osman, Md. Mahfuzur Rahman, "Preference-Aware Public Transport Matching," International Conference on Innovation in Engineering and Technology (IEEE ICIET 2018), 2018

Sifat Rezwan, Wasit Ahmed, Mahrin Alam Mahia, Mohammad Rezaul Islam, "IoT Based Smart Inventory Management System for Kitchen Using Weight Sensors, LDR, LED, Arduino Mega and NodeMCU (ESP8266) Wi-Fi Module with Website and App," 2018 Fourth International Conference on Advances in Computing, Communication & Automation (ICACCA), 2018

Nusrat Jahan Prithee Mohammad Rezaul Islam, Yesin Iqbal Asif, Jahir Rahman, Saurav Das Shuvo, Al Imran, "A Prominent Smart Gas Meter," 2018 2nd International Conference on Electronics, Materials Engineering & Nano-Technology (IEMENTech), 2018

Md. Mujtabir Alam ; Mahamud Hussain ; Md. Ashik Amin ; Mohammad Monirujjaman Khan, "Design of a Low-cost Automated Cardiopulmonary Resuscitation Device with Piston-Driven Chest Compression System," 4th International Conference on Electrical Engineering and Information & Communication Technology (iCEEiCT), 2018

Tousif Osman, Shahreen Shahjahan Psyche, J. M. Shafi Ferdous, Hasan U. Zaman, "Intelligent Traffic Management System for Cross Section of Roads Using Computer Vision," 7th IEEE Annual Computing and Communication Workshop and Conference (IEEE CCWC 2017), Las Vegas, USA, 9-11 January, 2017

Hasan U. Zaman, Chowdhury, Nahian, Ghani,Uddin, Baized, Islam, S. M. Hasibul Hoq, "Design & Feasibility Analysis of Free to Walk: A User Friendly Mobile Application for Handicapped People," 2017 International Conference on Electonics, Information, and Communication (ICEIC 2017), Phuket, Thailand, 11-14 January, 2017

Hasan U. Zaman, Sharmina Zaman, A S M Baized Shuvo, Fatin Hasnath Chowdhury, Taki Uddin, Mohammad Jawad Ibne Ishaque, Tamim, S. M. Hasibul Hoq, Saad Akash, Saifullah Basher Shohel, Swapnil Sayan Saha, Nazia Nawar Hassan, "Design, Control & Performance Analysis of Baby Bot: An Android & Transmitter Controlled Multipurpose Robot," 2017 International Conference on Electonics, Information, and Communication (ICEIC 2017), Phuket, Thailand, 11-14 January, 2017

Sanita Rahman, Emdadul Haque, Mahmudur Rahman and Hasan U. Zaman, "Web-based Automated Appliance Control System with Security and Gas Safety Systems," Proceedings of International Conference on Electrical, Computer and Communication Engineering (ECCE 2017), Cox's Bazar, Bangladesh, 16-18 February, 2017

Rafiya Hossain, Moonmoon Ahmed, Md. Mozadded Alfasani and Hasan U. Zaman, "An Advanced Security System Integrated With RFID Based Automated Toll Collection System," Proceedings of the 3rd Asian Conference on Defence Technology (IEEE ACDT 2017), pp. 71-76, Phuket, Thailand, 18-20 January, 2017

Hasan U. Zaman, Chowdhury Erfan Shourov, Abdullah Al Mahmood and Noor E Alam Siddique, "Conversion of Wasted Heat Energy into Electrical Energy Using TEG," Proceedings of the 7th IEEE Annual Computing and Communication Workshop and Conference (IEEE CCWC 2017), Las Vegas, USA, 9-11 January, 2017

Ali Adib Arnab, Sheikh Sadia Afrin, F.M. Fahad and Hasan U. Zaman, "A Cost Effective Way to Build a Web Controlled Search and CO Detector Rover," Proceedings of the 7th IEEE Annual Computing and Communication Workshop and Conference (IEEE CCWC 2017), Las Vegas, USA, 9-11 January, 2017

Tousif Osman, Shahreen Shahjahan Psyche, J. M. Shafi Ferdous, Hasan U. Zaman, "Intelligent Traffic Management System for Cross Section of Roads Using Computer Vision," Proceedings of the 7th IEEE Annual Computing and Communication Workshop and Conference (IEEE CCWC 2017), Las Vegas, USA, 9-11 January, 2017

Hasan U. Zaman, Asif Alam Joy, Khan Mohammed Akash and Safwan Talukder Fayad, "A Simple and Effective Way of Controlling a Robot by Hand Gesture," Proceedings of the International Conference on Intelligent Computing and Control Systems (IEEE ICICCS 2017), pp. 330-333, Madurai, India, 15-16 June, 2017

Hasan. U. Zaman, Tarafder Elmi Tabassum, Tanha Islam, Nadia Mohammad, "Low Cost Multi-level Home Security System For Developing Countries," Proceedings of the International Conference on Intelligent Computing and Control Systems (IEEE ICICCS 2017), pp. 549-554, Madurai, India, 15-16 June, 2017

Hasan U. Zaman, Jannatul Siffat Hossain, Tasnim Tamanna Anika, Deboshree Choudhury, "RFID Based Attendance System," Proceedings of the 8th International Conference on Computing, Communication And Networking Technologies (IEEE 8th ICCCNT 2017), Delhi, India, 3-5 July, 2017

Mehal Zaman Talukder, Sheikh Shadab Towqir, Arifur Rahman Remon, Hasan U. Zaman, "An IoT Based Automated Traffic Control System With Real-Time Update Capability," Proceedings of the 8th International Conference on Computing, Communication And Networking Technologies (IEEE 8th ICCCNT 2017), Delhi, India, 3-5 July, 2017

Sariat Sultana Nova, Aaphsaarah Rahman, Fyaz Hasan Chowdhury, Hasan U. Zaman, "A Novel Braille Pad with Dual Text-to-Braille and Braille-to-Text capabilities with an integrated LCD Display," Proceedings of the 2017 International Conference on Intelligent Computing, Instrumentation and Control Technologies (IEEE ICICICT2017), Kerala, India, 6-7 July, 2017

Hasan U. Zaman, Naushaba Zerin, Md. Hasin Jamal, Joytu Khisha, "Speech Responsive Mobile Robot for Transporting Objects of Different Weight Categories," Proceedings of the 18th International Conference on Advanced Robotics (IEEE ICAR 2017), Hong Kong Science and Technology Park, Honk Kong, 10-12 July, 2017

Rafiya Hossain, Moonmoon Ahmed, Hasan Uz Zaman, "A Cost Effective Security Technology Integrated with RFID Based Automated Toll Collection System," Advances in Engineering Systems, Advances in Science, Technology and Engineering Systems Journal (ASTESJ), Volume 2, Issue 3, Page No 1777-1783, 2017

Tanzilur Rahman, Takanori Ichiki, "Fabrication and Characterization of a Stabilized Thin Film Ag/AgCl Reference Electrode Modified with Self-Assembled Monolayer of Alkane Thiol Chains for Rapid Biosensing Applications," Sensors 17(10):2326 , 2017

Farah, T., Shelim, R., Zaman, M., Hassan, M. M., & Alam, D, "Study of race condition: A privilege escalation vulnerability," WMSCI 2017 - 21st World Multi- Conference on Systemics, Cybernetics and Informatics (Scopus Indexed), 2017

Md Ehtesham Adnan, Noor Muhammad Dastagir, Jafrina Jabin, Ahmed Masud Chowdhury, Mohammad Rezaul Islam, "A cost effective electronic braille for visually impaired individuals," Humanitarian Technology Conference (R10-HTC), 2017 IEEE Region 10, 2017

Mohammad Rezaul Islam, Fatin Hasnath Chowdhury, Sifat Rezwan, Mohammed Jawad Ishaque, Jamir Uddin Akanda, Abu Shaid Tuhel, Benazir Bashar Riddhe, "Novel design and performance analysis of a Mars exploration robot: Mars rover mongol pothik," Third International Conference on Research in Computational Intelligence and Communication Networks (ICRCICN), 2017

Monirul Islam, ASM Rashedul Huq, Rezwan Bin Kashem, Nadil Hassan, Mohammad Rezaul Islam, K. M. A. Salam, "GPS based Automatic Antenna Management System and Satellite Tracking," Journal of Modern Science and Technology, 2017

Fatin Hasnath Chowdhury, Baized Shuvo, Mohammad Rezaul Islam, Tasfiqul Ghani, Saad Ahmed Akash, Rakib Ahsan, Nazia Nawar Hassan, "Design, control & performance analysis of secure you IoT based smart security system," 8th International Conference on Computing, Communication and Networking Technologies (ICCCNT), 2017

Hasan U Zaman, Fatin Hasnath Chowdhury, Rashik Ishrak Nahian, Tasfiqul Ghani, Baized Shuvo, Mohammad Rezaul Islam, SM Hasibul Hoq, "Design & Feasibility Analysis of Free to Walk," ICEIC 2017 International Conference on Electronics, Information, and Communication, 2017

Nova Ahmed, Shuvashis Ghosh, Rifat Ahmed Hassan, Sian Iftekher Galib, AK Azad, Minhaz Ahmed Syrus, "A gradient sensing middleware to handle flash flood," Computers & Electrical Engineering, 2017

Fatin Hasnath Chowdhury ; Rashik Nahian ; Taki Uddin ; Sifat Rezwan ; Monirujjaman Khan ; Abu Sufian ; Nazmul Hassan, Jawad Ishaque, Saad Ahmed Akash, Nazia Nawar Hassan, "Design, control & performance analysis of forecast junction IoT and swarm robotics based system for natural disaster monitoring," 8th International Conference on Computing, Communication and Networking Technologies (ICCCNT), 2017

Mohammad Sakib Mahmud, Mahbub Arab Majumder, Abdul Kawsar Tushar, Md. Mahtab Kamal, Akm Ashiquzzaman, Md. Rashedul Islam, "Real-time feedback-centric nurse calling system with archive monitoring using Raspberry Pi," 2017 4th International Conference on Networking, Systems and Security (NSysS), 2017

Karima Haque, Mahmudur Rahman Khan, Narisha Nowrin and Hasan U. Zaman, "Smart Street Lights using Piezoelectric Materials," Proc. of Intl. Conference on Microelectronics, Computing and Communication (MicroCom2016), Durgapur, India, January 23-25, 2016

Hasan U. Zaman, Majidul Haque Bhuiyan, Montashir Ahmed and S.M Tarek Aziz, "A Novel Design of Line Following Robot with Multifarious Function ability," Proc. of Intl. Conference on Microelectronics, Computing and Communication (IEEE MicroCom2016), Durgapur, India, January 23-25, 2016

Tania Alauddin, Md. Tamzid Islam, and Hasan U. Zaman, "Efficient Design of a Metal Detector Equipped Remote-Controlled Robotic Vehicle," Proc. of Intl. Conference on Microelectronics, Computing and Communication (IEEE MicroCom2016), Durgapur, India, January 23-25, 2016

Rafiya Hossain, Moonmoon Ahmed, Md. Mozadded Alfasani, Hasan U. Zaman, and Mohammad Rezaul Islam, "Automated Toll Collection System," Proc. 8th Intl. Conference on Electrical, Electronics and Civil Engineering (ICEECE'16), pp. 41-44, Dubai (UAE), Jan. 12-13, 2016

Rafiya Hossain, Moonmoon Ahmed, Md. Mozadded Alfasani, Hasan U. Zaman, Mohammad Rezaul Islam, "Automated T oll Collection System," 8th International Conference on Electrical, Electronics and Civil Engineering (ICEECE'2016) Jan. 12-13, 2016 Dubai (UAE), 2016

Hasan U. Zaman, Chowdhury Tahirina Saara, Segufta Khondker, Tahsin Kamal, "Rescue Robot," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 104, May 13-14, 2016

Farhana Atuyar Saleh, Sadia Afrin Shopno, Hasan U. Zaman, "A Cost-effective SMS Based Tracking System Using GPS-GSM-GPRS Modules with Arduino and Smartphone," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 110, May 13-14, 2016

Mahmud M. Milton, Kazi Rizvan Hossain, Nahin Ahmed and Hasan U. Zaman, "Cost Effective Home Automation," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 119, May 13-14, 2016

Nahid Islam, A.S.M. Nesar Uddin, Sami Rahman, Hasan U. Zaman, "Universal MP controller," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 120, May 13-14, 2016

Md. Waliur Rahman, M. Farhanul Ihsan, Hasan U. Zaman, "A Novel Method of Remote Control of Power System Substations Based On Sensor Data Using GSM Networks," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 530, May 13-14, 2016

Hasan U. Zaman, A S M Muktadiru Baized Shuvo, Fatin Hasnath Chowdhury, Taki Uddin, Mohammed Jawad Ibne Ishaque, Nazia Nawar Hassan, S. M. Hasibul Hoq, Swapnil Sayan Saha, Saad A Akash, Sifat Rezwan, "Design, Control & Performance Analysis of Muktibot," The 7th IEEE Annual Information Technology, Electronics and Mobile Communication Conference (IEEE IEMCON 2016), Vancouver, Canada, October 13 - 15, 2016

S. M. Hasibul Hoq, Hasan U. Zaman, A S M Muktadiru Baized Shuvo, Fatin Hasnath Chowdhury, Abrar Ahnaf Abid, Taki Uddin, Mohammed Jawad Ibne Ishaque, "Design, Control & Performance Analysis of a Smart Wheelchair," 2016 IEEE 5th Global Conference on Consumer Electronics (IEEE GCCE 2016), Kyoto, Japan, October 11-14, 2016

Maofic Farhan Karin, Khandaker Sharif Noor and Hasan U. Zaman, "Hardware Based Design and Implementation of a Bottle Recycling Machine using FPGA," 2016 IEEE Conference on Systems, Process and Control (IEEE ICSPC 2016), Melaka, Malaysia, 16-17 December, 2016

S. M. Hasibul Hoq, Hasan U. Zaman, Shuvo, Chowdhury, Abid, Uddin, Ishaque, "Design, Control & Performance Analysis of a Smart Wheelchair: An android & joystick controlled user-friendly wheelchair," Proceedings of 12th Global Engineering, Science and Technology Conference, Dhaka, Bangladesh, 23–24 December, 2016

Salahuddin Fahim, Rahman T.R., "A Fuzzy Based Low-Cost Monitoring Module Built with Raspberry Pi-Python-Java Architecture," 2015 International Conference on Smart Sensors and Application, Kuala Lumpur, Malaysia, 2015

Mohammad Rezaul Islam, Hasib Iqbal Mamun, "Energy Understanding Device (EUD): An Innovative Energy Metering and Monitoring Solution: Perspective Bangladesh," Journal of Modern Science and Technology, Vol. 3. No. 1. March 2015 Issue. Pp.47-63, 2015

Nazmul Hossain, Mohammad Tanzir Kabir, Tarif Riyad Rahman, Mohamed Sajjad Hossen, Fahim Salauddin, "‘A Real-time Surveillance Mini-rover Based on OpenCV-Python-JAVA Using Raspberry Pi 2: An Application of Internet of Things (IoT)," 5th IEEE International Conference on Control Systems, Computing and Engineering (ICCSCE 2015), 2015

Hasan U. Zaman, Anika Zaman, A S M Faruk Abdullah, Tamina Islam Khan, "GSM and GPS Based Intelligent Method to Track Movement and Detect Collision and Rollover of Wheelchairs," Proc. 2nd Intl. Conference Electrical Information and Communication Technology (IEEE EICT'15), pp. 79-83, Khulna, Dhaka, December 10-12, 2015

Hasan U. Zaman, Md. Shahriar Hossain, Mohammad Wahiduzzaman, Mohammad Shahariar Asif,, "A Novel Design of a Robotic Vehicle for Rescue Operation," 18th International Conference on Computer and Information Technology (IEEE ICCIT 2015), Dhaka, Bangladesh, 22-23 December, 2015

Michael Klaiber, Donald G. Bailey, Silvia Ahmed, Yousef Baroud, Sven Simon, "A high-throughput FPGA architecture for parallel connected components analysis based on label reuse.," FPT, 2013

M. Klaiber, S. Ahmed, Z. Wang, L. Rockstroh, Y. Gera, S. Simon, "Online imaging analysis of spray processes based on a reconfigurable embedded system," 10th Workshop über Sprays, Techniken der Fluidzerstäubung und Untersuchungen von Sprühvorgängen, 2012

Rony, R. J., Ahmed, M. S., Sarcar, S., & Ahmed, N. , "Understanding Driving Stress in Urban Bangladesh: An Exploratory Study, Wearable Development and Experiment.," ACM Journal on Computing and Sustainable Societies., 2024

Ahmed, M. S., Rony, R. J., Hadi, M. A., Hossain, E., & Ahmed, N., "A Minimalistic Approach to Predict and Understand the Relation of App Usage with Students’ Academic Performance. Proceedings of the ACM on Human-Computer Interaction," Proceedings of the ACM on Human-Computer Interaction, 7(MHCI), 1-2, 2024

Sinha, A., Ahmed, N., Ahmed, S., Abeer, I. A.,, "Roles of Technology for Risk Communication and Community Engagement in Bangladesh during COVID-19 Pandemic," ACM Journal on Computing and Sustainable Societies., 2024

Manoshi Das Turjo, Khushboo Suchit Mundada, Nuzhat Jabeen Haque, Nova Ahmed, "Predicting the Transition From Depression to Suicidal Ideation Using Facebook Data Among Indian-Bangladeshi Individuals: Protocol for a Cohort Study," JMIR Research Protocol, 2024

N Ahmed, A Khuda, SJ Chowdhury, T Rezwana, MSU Islam, S Sajjad, "Youth-Driven, Community-Engaged Waste Management," The Journal of Community Informatics, 2024

MS Ahmed, T Hasan, S Islam, N Ahmed, "Investigating Rhythmicity in App Usage to Predict Depressive Symptoms: Protocol for Personalized Framework Development and Validation Through a Countrywide Study," JMIR Research Protocol, 2024

M Wong-Villacres, C Kutay, S Lazem, N Ahmed, C Abad, C Collazos, "Making ethics at home in Global CS Education: Provoking stories from the Souths," ACM Journal on Computing and Sustainable Societies., 2024

Ifti Azad Abeer, Anik Sinha, Anik Saha, Syeda Shabnam Khan, Nova Ahmed, "A Platform for Connectivity and Synergy between Parents and Teachers of Children with Autism," ACM Journal on Computing and Sustainable Societies., 2024

Shaikh Shawon Arefin Shimon, Ali Neshati, Junwei Sun, Qiang Xu, Jian Zhao, "Exploring Uni-manual Around Ear Off-Device Gestures for Earables," Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Volume 8, Issue 1, 2024

Mohammad Rayed, Tawfique Elahi, SHAIKH SHAWON AREFIN SHIMON, Nova Ahmed, "MFS Design in Appstore-enabled Smart Featurephones for Low-literate, Marginalized Communities," CHI2023, 2023

Ahmed, M. S., & Ahmed, N, "A Fast and Minimal System to Identify Depression Using Smartphones: Explainable Machine Learning–Based Approach," JMIR Formative Research, 7, e28848., 2023

Ahmed, N., Chowdhury, A. M., Urmi, T., & Jamal, L. , "Impact of socio-economic factors on female students’ enrollments in science, technology, engineering and mathematics and workplace challenges in Bangladesh.," American Behavioral Scientist, , 2023

Mohammad Monirujjaman Khan, Samsun Nahar Safa, Minhazul Hoque Ashik, Mehedi Masud, and Mohammed A. AlZain , "Research and Development of Brain Control Wheel Chair for Paralyzed Patients," Intelligent Automation & Soft Computing, Tech Science Press. Vol. 30, no.1, pp. 49-64, doi:10.32604/iasc.2021.016077. (Impact Factor 1.647, Scopus Indexed). , 2021

Mohammad Fahim , Niloy Biswas, Sudipta Barman, A K M Bahalul Haque, "Professional Information Visualization Using Augmented Reality; AR Visiting Card," 2020 2nd International Conference on Sustainable Technologies for Industry 4.0 (STI), 2021

Sadman Chowdhury Siam; Abrar Faisal; Niazi Mahrab; AKM Bahalul Haque; Md. Naimul Islam Suvon, "Automated Student Review System with Computer Vision and Convolutional Neural Network," 2021 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS), 2021

Mohammad Fahim Hossain; Sudipta Barman; Niloy Biswas; A K M Bahalul Haque, "Augmented Reality in Medical Education: AR Bones," 2021 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS), 2021

AKM Bahalul Haque; Ayman Muniat; Parisha Rafiq Ullah; Shimin Mushsharat, "An Automated Approach towards Smart Healthcare with Blockchain and Smart Contracts," 2021 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS), 2021

Tahmid Hasan Pranto​, Abdulla All Noman, Atik Mahmud, AKM Bahalul Haque​​, "Blockchain and smart contract for IoT enabled smart agriculture," PeerJ Computer Science, USA, 2021

A K M Bahalul Haque, Bharat Bhushan, "Blockchain in a Nutshell: State-of-the-Art Applications and Future Research Directions," Blockchain and AI Technology in the Industrial Internet of Things, IGI Global, Pennsylvania, United States, 2021

A K M Bahalul Haque, Md Rifat Hasan, Md. Oahiduzzaman Mondol Zihad , "SmartOil: Blockchain and Smart Contract-based Oil Supply Chain Management," IET Blockchain, The Institution of Engineering and Technology, UK, 2021

Rezowana Akter, Jahid Khandaker, Shakil Ahmed, Muhtasim Munem Mugdho, A K M Bahalul Haque, "RFID Based Smart Transportation System With Android Application," International Conference on Innovative Mechanisms for Industry Applications (ICIMIA 2020), IEEE & Scopus Indexed, 2020

A K M Bahalul Haque, Shawan Shurid, Afsana Tasnim, Md. Shadman Sadique, Abu Sayem Mohammad Asaduzzaman, "A Novel Design of Gesture and Voice Controlled Solar-Powered Smart Wheel Chair with Obstacle Detection," IEEE International Conference on Informatics, IoT, and Enabling Technologies (ICIoT’20), 2020

Ahmed Rohani Islam, Kajol Bhowmick, Debalina Sikder, Hasan U. Zaman, "A Multifarious Design of a Microcontroller Based Home Security and Automation System," IEEE International Conference on Computational Intelligence and Communication Networks (CICN-2019), Hawaii, USA, 3-6 January, 2019

Rafaeal Hossain Rakin, Asad Siam, Md. Rafayet Hossain, Hasan U. Zaman, "A Low-Cost and Portable Electrocardiogram (ECG) Machine for Preventive Diagnosis," International Conference on Robotics, Electrical and Signal Processing Techniques (ICREST), Dhaka, Bangladesh, 10-12 January, 2019

Sadia Chowdhury, Farhan Rahman Wasee, Md Shafiqul Islam and Hasan U. Zaman, "Bengali Handwriting Recognition and Conversion to Editable Text," 2018 Second International Conference on Advances in Electronics, Computers and Communications (IEEE ICAECC-2018), Bangalore, India, 2018

Hasan U. Zaman, Khalida Sultana Shuravi, Muntasir Kabir Sakib and Mohammad Wasee Sarwar, "A Low Cost Wireless Braille System Hand Glove for Real Time Communication," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Hasan U. Zaman, Tawsif Ur Rahman Choudhury and Nafis Imtiaz Ahme, "A User-Friendly and Efficient Design of a Unified Online Survey and Quizzing System," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Sheefta Naz, Syed Naffiz Hasan, Arka Basak and Hasan U. Zaman, "The Design of an Online Laundry System," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Nova Ahmed , Tamanna Motahar, "Enabling Undergraduate Female Students in Hands on Learning through Programming Contests," The European Conference on Education (ECE2018), 2018

Nova Ahmed, Tamanna Motahar, Sharmin Kabir ,Munir Hasan, "Supporting Missing Daughters," HCI across Borders, (CHI 2018) /** Best Poster Award**/, 2018

Kazi Kowshin Raihana, Md. Sabbir Hossain, Md. Tahsan Dewan, Hasan U. Zaman, "Auto-Moto Shoes: An Automated Walking Assistance for Arthritis Patients," 2nd International Conference on Electronics, Materials Engineering and Nano-Technology (IEEE IEMENTech 2018), Kolkata, India, 4-5 May, 2018

Nixon Dutta, Joyeta Saha, Faysal Sarker and Hasan U. Zaman, "A Novel Design of a Multi-DOF Mobile Robotic Helping Hand for Paralyzed Patients," 2018 International Conference on Advances in Computing, Communications and Informatics (IEEE ICACCI 2018), Bangalore, Karnataka, India, 19-22 September, 2018

Nithya Sambasivan, Garen Checkley, Amna Batool, Laura Sanely Gaytán-Lugo, Tara Matthews, Sunny Consolvo, Elizabeth Churchill, "“Privacy is not for me, it’s for those rich women”: Performative Privacy Practices on Mobile Phones by Women in South Asia," Fourteenth Symposium on Usable Privacy and Security ({SOUPS} 2018), Best Paper Award, 2018

Mohammad Sorowar Hossain, Md Mahbub Hasan, Muhammad Sougatul Islam, Salequl Islam, Miliva Mozaffor, Md Abdullah Saeed Khan, Nova Ahmed, Waheed Akhtar, Shahanaz Chowdhury, SM Yasir Arafat, Md Abdul Khaleque, Zohora Jameela Khan, Tashmim Farhana Dipta, Shah Md Zahurul Haque Asna, Md Akram Hossain, KM Sultanul Aziz, Abdullah Al Mosabbir, Enayetur Raheem, "Chikungunya outbreak (2017) in Bangladesh: Clinical profile, economic impact and quality of life during the acute phase of the disease," PLoS neglected tropical diseases, 2018

Edited by Jan Servaes, "Handbook of Communication for Development and Social Change," Springer, 2018

Saadman Shahid Chowdhury, Atiar Talukdar,Ashik Mahmud, Tanzilur Rahman,, "Domain Specific Intelligent Personal Assistant with Bilingual Voice Command Processing," IEEE TENCON'18, 2018

Saadman Shahid Chowdhury, Atiar Talukdar,Ashik Mahmud, Tanzilur Rahman,, "Domain Specific Intelligent Personal Assistant with Bilingual Voice Command Processing," IEEE TENCON'18, 2018

Adnan Firoze, Tousif Osman, Shahreen Shahjahan Psyche, Tonmoay Deb, Rashedur M Rahman, "A synthetic approach to estimate cognitive aesthetic of framed images and improvements taking human’s psychology into account," Journal of Information and Telecommunication - Taylor & Francis. V(4,3), 2018

Adnan Firoze, Shahreen Shahjahan Psyche, Tonmoay Deb, Tousif Osman, Rashedur M Rahman, "Differential Color Harmony: A robust approach for extracting Harmonic Color features and perceive aesthetics in a large dataset," International Conference on Big Data and Cloud Computing (ICBDCC'18). Springer., 2018

Adnan Firoze, Tousif Osman, Shahreen Shahjahan Psyche, Rashedur M Rahman, "Scoring Photographic Rule of Thirds in a Large MIRFLICKR Dataset: A Showdown Between Machine Perception and Human Perception of Image Aesthetics," Springer Lecture Notes in Computer Science book series (LNCS, volume 10751), 2018

Hasan U. Zaman, Saif Mahmood, Sadat Hossain and Iftekharul Shovon, "Python based Portable Virtual Text Reader," 4th International Conference on Advances in Computing, Communication and Automation (IEEE ICACCA-2018), Subang Jaya, Selangor,, Malaysia, October 26-28, 2018

Hasan U. Zaman, Asif Alam Joy, Khan Mohammed Akash and Safwan Talukder Fayad, "A Simple and Effective Way of Controlling a Robot by Hand Gesture," Proceedings of the International Conference on Intelligent Computing and Control Systems (IEEE ICICCS 2017), pp. 330-333, Madurai, India, 15-16 June, 2017

Sariat Sultana Nova, Aaphsaarah Rahman, Fyaz Hasan Chowdhury, Hasan U. Zaman, "A Novel Braille Pad with Dual Text-to-Braille and Braille-to-Text capabilities with an integrated LCD Display," Proceedings of the 2017 International Conference on Intelligent Computing, Instrumentation and Control Technologies (IEEE ICICICT2017), Kerala, India, 6-7 July, 2017

Hasan U. Zaman, Naushaba Zerin, Md. Hasin Jamal, Joytu Khisha, "Speech Responsive Mobile Robot for Transporting Objects of Different Weight Categories," Proceedings of the 18th International Conference on Advanced Robotics (IEEE ICAR 2017), Hong Kong Science and Technology Park, Honk Kong, 10-12 July, 2017

Rokhsana Titlee, Ashfaq Ur Rahman, Hasan U. Zaman, and Hafiz Abdur Rahman, "A Novel Design of an Intangible Hand Gesture Controlled Computer Mouse using Vision Based Image Processing," 2017 3rd International Conference on Electrical Information and Communication Technology (IEEE EICT), Khulna, Bangladesh, 2017

Nithya Sambasivan, Garen Checkley, Nova Ahmed, Amna Batool, "Gender equity in technologies: considerations for design in the global south," ACM Interact, 2017

Jasmine Hentschel, Syed Ishtiaque Ahmed, Faheem Hussain, Nova Ahmed, Neha Kumar, "Working with Women in ICTD," Proceedings of the Ninth International Conference on Information and Communication Technologies and Development, 2017

Nova Ahmed, Minhaz Ahmed Syrus, Arshad Chowdhury, "Simple Group Photo Sharing Using Facesense," Computer Software and Applications Conference (COMPSAC), 2017 IEEE 41st Annual, 2017

Nova Ahmed, Mahfuzur Rahman Siddiquee, Refaya Karim, Mohsina Zaman, Sayed Mahmudul Alam, Syed Fahim Ashram, "Crazy Crowd Sourcing to Mitigate Resource Scarcity," Distributed Computing Systems (ICDCS), 2017 IEEE 37th International Conference on, 2017

Syed Emdad Ullah, Tania Alauddin and Hasan U. Zaman, "Developing an E-Commerce Website," Proc. of Intl. Conference on Microelectronics, Computing and Communication (IEEE MicroCom 2016), Durgapur, India, January 23-25, 2016

M. Arabi Hasan Sakib, Fakhrul Islam, Sabbir Samiul Haque, Hasan U. Zaman, "Doctor Locator: A Web Application to Improve Online Doctor Directories in Bangladesh," 5th International Conference on Informatics, Electronics & Vision (IEEE ICIEV), Dhaka, Bangladesh, paper no. 118, May 13-14, 2016

Faridur Rahman Hridoy, Kallal Das, Rifayat Hossain Arko and Hasan U. Zaman, "Development of an Online Bus Ticket Booking System for Transportation Services in Bangladesh," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 33, May 13-14, 2016

Syed Naffiz Hasan, Arka Basak, Sheefta Naz and Hasan U. Zaman, "The Online Laundry System," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 31, May 13-14, 2016

Hasan U. Zaman, Tawsif Ur Rahman Choudhury, Nafis Imtiaz Ahmed, "A Unified Online Survey and Quizzing System," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 109, May 13-14, 2016

Nahid Islam, A.S.M. Nesar Uddin, Sami Rahman, Hasan U. Zaman, "Universal MP controller," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 120, May 13-14, 2016

S. M. Hasibul Hoq, Hasan U. Zaman, A S M Muktadiru Baized Shuvo, Fatin Hasnath Chowdhury, Abrar Ahnaf Abid, Taki Uddin, Mohammed Jawad Ibne Ishaque, "Design, Control & Performance Analysis of a Smart Wheelchair," 2016 IEEE 5th Global Conference on Consumer Electronics (IEEE GCCE 2016), Kyoto, Japan, October 11-14, 2016

S. M. Hasibul Hoq, Hasan U. Zaman, Shuvo, Chowdhury, Abid, Uddin, Ishaque, "Design, Control & Performance Analysis of a Smart Wheelchair: An android & joystick controlled user-friendly wheelchair," Proceedings of 12th Global Engineering, Science and Technology Conference, Dhaka, Bangladesh, 23–24 December, 2016

Shaikh Shawon Arefin Shimon , Courtney Lutton , Zichun Xu ,Sarah Morrison-Smith , Christina Boucher , Jaime Ruiz, "Exploring Non-touchscreen gestures for smartwatches," CHI '16 , 2016

Moinul Hossain, Nova Ahmed, Mahfuzur Rahman Siddique, Refaya Karim, Mohsina Zaman, Rifat Monzur, "Map Matching on Sparse GPS Data: A Perspective of a Developing City," Eastern Asia Society for Transportation Studies, 2015

Lamia Iftekhar, Nova Ahmed, Fahima Chowdhury, Ridita Rahman, "Electrical and Computer Engineering Laboratory Education for Female Undergraduate Students," The 10th International Conference on Computer Science & Education, ICCSE, 2015

Nova Ahmed, Luke Doyle, Masudul Haque, "Enterring the Dream World of Computers," International Conference for Informatin and Communication Technologies and Development, ICTD, 2015

Rahat Yasir, Md. Shariful Islam Nibir, Zarmeen Ahmed Chadni and Nova Ahmed,, "Telemedicine System for Financially Unstable People of Bangladesh," Journal of Modern Science and Technology, 2015

Natasha Mounota, Mike Brayshaw, "Personalizing your social computing world: A case study using Twitter," Science and Information Conference (SAI), 2015

Hasan U. Zaman, Md. Shahriar Hossain, Mohammad Wahiduzzaman, Mohammad Shahariar Asif,, "A Novel Design of a Robotic Vehicle for Rescue Operation," 18th International Conference on Computer and Information Technology (IEEE ICCIT 2015), Dhaka, Bangladesh, 22-23 December, 2015

Nova Ahmed, Lamia Iftekhar, Silvia Ahmed, Ridwan Rahman, Tanveer Reza, Sarah Shoilee, Charisma F. Choudhury, "Bap re Bap!: Driving Experiences through Multimodal Unruly Traffic on Bumpy Roads," ACM DEV, 2015

Shaikh Shawon Arefin Shimon , Sarah Morrison-Smith , Noah John , Ghazal Fahimi , Jaime Ruiz, "Exploring User-Defined Back-Of-Device Gestures for Mobile Devices," MobileHCI'15, 2015

Arman Kamal, Md. NuruddinMonsur, Syed Tanveer Jishan and Nova Ahmed, "ChaScript: Breaking Language Barrier Using a Bengali Programming System," , 8th International Conference of Electrical and Computer Engineering, ICECE, 2014

Syed Ishtiaque Ahmed, Steven J. Jackson, Nova Ahmed, Hasan S. Ferdous, Md. R. Rifat, Abu S. Rizvi, Shamir Ahmed, Rifat S. Mansur, "Protibadi: A Platform for Fighting Sexual Harassment in Urban Bangladesh," ACM Conference on Human Factors in Computing Systems, CHI, 2014

Fajilatun Nahar, A. M. Masudul Haque, Nova Ahmed, "ifreePhony: A touchscreen user interface for people with eye disability," Grace Hopper Conference, India, 2014

Shamsul Arifin, Adnan Firoze, M. Ashraful Amin, Hong Yan, "Dermatological Disease Diagnosis using Color-skin Images," International Conference on Machine Learning and Cybernetics (ICMLC), 2012

Mahfuz Rahman, Sean Gustafson, Pourang Irani, and Sriram Subramanian, "Tilt Techniques: Investigating the Dexterity of Wrist-based Input," In Proceedings of the ACM SIGCHI Conference on Human Factors in Computing Systems (CHI '09), 1943-1952, 2009

Nabeel Hassan, Md. Mahfuzur Rahman, Pourang Irani and Peter Graham, "Chucking: A One-handed Document Sharing Technique," In Proceedings of the 12th IFIP International Conference on Human-Computer Interaction (INTERACT '09), 264-278, 2009

Md. Mahfuzur Rahman, Pourang Irani, and Peter Graham, "Natural Gesture-Based Techniques for sharing Documents from a Private to a Public Display," In Proceedings of the Workshop on designing multi-touch interaction techniques for coupled Public and Private Displays (PPD 2008), 2008
Dipta Voumick, Sreyasi Sen, Nusher Jamil Kazi, Homaira Islam Parisa and Mohammad Monirujjaman Khan , "Development A Web Application for Lawyer and Client Virtual Communication," The 12th Annual Computing and Communication Workshop and Conference (CCWC), 26-29 January 2022, USA. Accepted and due for publication., 2022

Ajan Ahmed and Mohammad Monirujjaman Khan, "Development of Smart Telemedicine System," The 12th Annual Computing and Communication Workshop and Conference (CCWC), 26-29 January 2022, USA., 2022

Nazifa Tasneem, Yakut Marzan,Md Anik Hasan, Mohammad Monirujjaman Khan, "My Diary: A Web Application to Accumulate Necessary Files," The 12th Annual Computing and Communication Workshop and Conference (CCWC), 26-29 January 2022, USA. Accepted and due for publication., 2022

Mohammed Farabi Alam, Abid Ibna Zahid, Mohammed Khairul Islam, and Mohammad Monirujjaman Khan, "Homies–An Online Web-based Platform to Find Cheap Accommodation for Travelers," 6th International Conference on Computing Methodologies and Communication (ICCMC), 29-31 March, pp. 1540-1545, doi: 10.1109/ICCMC53470.2022.9753715., 2022

Md. Taufiq Al Hasib Sadi, Md. Ishtiaq Kadir, Md. Shiblee Rahman, Mohammad Monirujjaman Khan, "Development of a Voice Controlled Web based E-Commerce," 2022 6th International Conference on Computing Methodologies and Communication (ICCMC), 2022, pp. 1-8, doi: 10.1109/ICCMC53470.2022.9753691., 2022

S. Mohammad, T. Bhowmick, M. S. Zaman Siddique and M. Monirujjaman Khan, "Garment Stock Trading Digital System Development with PHP Laravel and Bootstrap Frameworks," 2022 6th International Conference on Computing Methodologies and Communication (ICCMC), 2022, pp. 1559-1562, doi: 10.1109/ICCMC53470.2022.9753845., 2022

Ajan Ahmed, Priyanka Dixit, Mohammad Monirujjaman Khan, "Development of an Online Mental Well-being Mobile Application for Covid-19 Pandemic," 2022 6th International Conference on Computing Methodologies and Communication (ICCMC), 2022, pp. 1553-1558, doi: 10.1109/ICCMC53470.2022.9754112., 2022

Ajan Ahmed, Md. Talat Mahmud, Mohammad Monirujjaman Khan, "Info Hospital: Web/Mobile Application based Health Care System," 2022 6th International Conference on Computing Methodologies and Communication (ICCMC), 2022, pp. 1546-1552, doi: 10.1109/ICCMC53470.2022.9753895., 2022

Nazmul Kaonine, Shafee Chowdhury, Farhan Mohd. Fokrul Alam, Mohammad Monirujjaman Khan, "Development of Android Application and Website to Combat Criminal Activities," 2022 6th International Conference on Computing Methodologies and Communication (ICCMC), 2022, pp. 1522-1527, doi: 10.1109/ICCMC53470.2022.9754156., 2022

Mostaqim Hossain, MubassirHabib, Mainuddin Hassan, FariaSoroni and Mohammad Monirujjaman Khan, "Research and Development of an E-commerce with Sales Chatbot," IEEE World AI IoT Congress 2022, Seattle USA, 6-9 June, 2022

Mohammad Monirujjaman Khan, Md. Rabbi Amin, Abdullah Al Mamun, Ahsan Ahmed Sajib, "Development of Web Based Online Medicine Delivery System for Covid-19 Pandemic," Journal of Software Engineering and Applications. Vol. 14 No. 1, pp. 26-43, 2021, DOI: 10.4236/jsea.2021.141003 ,(Google Scholar)., 2021

Mohammad Monirujjaman Khan, SM Tahsinur Rahman and Sabik Tawsif Anjum Islam , "The Use of Telemedicine in Bangladesh during COVID-19 Pandemic," E-Health Telecommunication Systems and Networks. Vol. 10, No. 1, pp. 1-19, 2021. (Google Scholar). , 2021

Mohammad Monirujjaman Khan, Tahia Tazin, Md.Redwanul Islam, Md.Ishtiaq Kadir, Amena Nasrin, Samia Chowdhury, "Online Store for Local Small and Medium Business," IEEE 11th Annual Computing and Communication Workshop and Conference (IEEE CCWC 2020), 27th-30th January 2021, USA. pp. 0536-0541, doi: 10.1109/CCWC51732.2021.9376012., 2021

Khondoker Aminuzzaman, Md. Junayed Miah, Md. Anisur Rahman, "Development of Online Home Sharing Web Application," IEEE 11th Annual Computing and Communication Workshop and Conference (IEEE CCWC 2020), 27th-30th January, USA, pp. 0550-0553, doi: 10.1109/CCWC51732.2021.9375965., 2021

Rabbani Rasha, Mohammad Monirujjaman Khan, Mehedi Masud Mohammed and A. AlZain, "Investigain: A Productive Asset Management Web Application," Computer Systems Science and Engineering, Tech Science Press, Vol. 38, No. 2, pp.151-164, 2021, doi:10.32604/csse.2021.015314, (Impact Factor 1.486, Scopus Indexed). , 2021

Md. Hafizur Rahman, Eshan Barua, Samanta Afrin, Md. Ashikur Rahman, Mohammad Monirujjaman Khan, "Bid & Buy: An Effective Online Based Platform for Client and Vendor," 5th International Conference on Computing Methodologies and Communication (ICCMC 2021), 08-10, April 2021, DOI: 10.1109/ICCMC51019.2021.9418467, 2021

Sadman Ahmed, Mohammad Monirujjaman Khan, Roobaea Alroobaea and Mehedi Masud, "Development of A Multifeatures Web Based Physiotherapy Service System," Intelligent Automation & Soft Computing, Tech Science Press. Vol.29, No.1, 2021, pp.43-54, doi:10.32604/iasc.2021.015914 . (Impact Factor 1.647 and Scopus Indexed)., 2021

Md. Sajjad Mahmud Khan, Sajjad Kashem and Mohammad Monirujjaman Khan, "Development of A Comparison Based Hotel and Resort Booking System in Bangladesh," Journal of Software Engineering and Applications. Vol. 14 No. 5, pp. 133-149, 2021, DOI: 10.4236/jsea.2021.145009 .(Google Scholar)., 2021

Md. Talat Mahmud, Faria Soroni and Mohammad Monirujjaman Khan, "Development of A Mobile Application for Patient’s Medical Record and History," 2021 IEEE World AI IoT Congress (AIIoT), 2021, pp. 0081-0085, doi: 10.1109/AIIoT52608.2021.9454227., 2021

HM Tamim, Fahema Sultana, Nazifa Tasneem, Yakut Marzan, Mohammad Monirujjaman Khan, "Class Insight: A Student Monitoring System With Real-Time Updates Using Face Detection and Eye Tracking," 2021 IEEE World AI IoT Congress (AIIoT), 2021, pp. 0213-0220, doi: 10.1109/AIIoT52608.2021.9454176., 2021

Faria Soroni, Md.Talat Mahmud, Sajal Chowdhury and Mohammad Monirujjaman Khan , "RentBd-An Exclusive Fashion Rental Service," 2021 IEEE World AI IoT Congress (AIIoT), 2021, pp. 0132-0136, doi: 10.1109/AIIoT52608.2021.9454243., 2021

Faria Soroni, Md. Amdadul Bari and Mohammad Monirujjaman Khan, "GERAM BAZAR, A Mobile Application and Website Interface E-Commerce," 2021 IEEE World AI IoT Congress (AIIoT), 2021, pp. 0077-0080, doi: 10.1109/AIIoT52608.2021.9454245., 2021

Intiser Zaman, Tasdid Rahman, Md. Sahidur Rahman, Mohammad Monirujjaman Khan, "An Interactive Web Platform and Android Application Based on Room Sharing Service for Students," 2021 IEEE World AI IoT Congress (AIIoT), 2021, pp. 0127-0131, doi: 10.1109/AIIoT52608.2021.9454175., 2021

Sudman Bin Manjur, Nahian Noshin Nur, Md. Mushfiqur Rahman, Md. Hashibur Rahman Khan, Rohimul Basunia and Mohammad Monirujjaman Khan, "Educational Web Application for Young People to Raise Awareness on Menstruation," 2021 IEEE World AI IoT Congress (AIIoT), 2021, pp. 0165-0169, doi: 10.1109/AIIoT52608.2021.9454177., 2021

Nazifa Tasneem, Md Anik Hasan, Sumaiya Binte Akther and Mohammad Monirujjaman Khan, "An Interactive Android Application to Share Rides With NSUers," 2021 IEEE World AI IoT Congress (AIIoT), 2021, pp. 0121-0126, doi: 10.1109/AIIoT52608.2021.9454178., 2021

Mohammad Fahim , Niloy Biswas, Sudipta Barman, A K M Bahalul Haque, "Professional Information Visualization Using Augmented Reality; AR Visiting Card," 2020 2nd International Conference on Sustainable Technologies for Industry 4.0 (STI), 2021

Mohammad Fahim Hossain; Sudipta Barman; Niloy Biswas; A K M Bahalul Haque, "Augmented Reality in Medical Education: AR Bones," 2021 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS), 2021

Morshedul Bari Antor, A. H. M. Shafayet Jamil, Maliha Mamtaz, Mohammad Monirujjaman Khan, Mehedi Masud et al. , "Development of A Web-Based Online Telemedicine System for Covid-19 Patients," Intelligent Automation & Soft Computing, Tech Science Press, Vol.30, No.3, 2021, pp.899-915, doi: 10.32604/iasc.2021.018914, (Impact Factor 1.647, Scopus Indexed), , 2021

Mohammad Monirujjaman Khan, "An Online Law Library Database for Legal Cases of Bangladesh for Study Purpose for Lawyer and Law Students," 2021 IEEE Symposium on Industrial Electronics & Applications (ISIEA), 2021, pp. 1-5, doi: 10.1109/ISIEA51897.2021.9509994., 2021

Zubaer Ahmed, Mustafizur Rahman Cornel, Mohammad Monirujjaman Khan et al., , "Development of Lawyer Finding Web Application for Bangladesh," 2021 IEEE Symposium on Industrial Electronics & Applications (ISIEA), 2021, pp. 1-6, doi: 10.1109/ISIEA51897.2021.9509976., 2021

Dipta Voumick, Prince Deb, Sourav Sutradhar, Mohammad Monirujjaman Khan, "Development of Online Based Smart House Renting Web Application," Journal of Software Engineering and Applications, 14, 312-328. doi: 10.4236/jsea.2021.147019, (Google Scholar),, 2021

Md Sifat Yasir Mustafiz, Mamun Bin Harun Hriday, Jannatul Ferdous Oyeshe, Mohammad Monirujjaman Khan, "Development of A Novel Integrated Web-based System for Advertisement Service," Journal of Software Engineering and Applications, 14, 329-343. doi: 10.4236/jsea.2021.148020,(Google Scholar), 2021

Mohammad Monirujjaman Khan, Talat mahmud et al., , "Development of Re-commerce Online Web-based Platform," 2021 IEEE International Conference on Computing, Power and Communication Technologies, September 24-26, 2021, Wilayah Persekutuan Kuala Lumpur, Malaysia. (Accepted), 2021

Raktim Raihan Prova, A S M Rayhan, Rafia Sultana Shilon and Mohammad Monirujjaman Khan, "A Web and Mobile Based Approach to Redistribute Consumable Food Waste," The 12th International Conference On Computing, Communication and Networking Technologies (ICCCNT), July 6 – 8, IIT – Kharagpur, West Bengal, India. (Accepted), 2021, 2021

Amir Hamza Soyeb, Md.Farhad Gazi and Mohammad Monirujjaman Khan, "Mobile Application for Online Divorce Counseling Due to Mental Pressure During Covid-19 Pandemic," Journal of Software Engineering and Applications. Accepted and due for publication, (Google Scholar). , 2021

Khairunnahar Suchana,Syed Md EftekharAlam,Mohammad Monirujjaman Khan, "Development of User-Friendly Web-Based Lost and Found System," Journal of Software Engineering and Applications. Accepted and due for publication, (Google Scholar). 2021, 2021

Mohammad Monirujjaman Khan and Amdadul Bari, "Development of a Web-based Corona Emergency Portal," International Conference on Computational Techniques and Applications – ICCTA, 9-10 October, 2021. Accepted and due for publication, 2021

Md. Talat Mahmud, Faria Soroni and Mohammad Monirujjaman Khan et al.,, "Web and Mobile Application Based Missing Query Platform (Lost and Found BD)," 2021 IEEE 12th Annual Information Technology, Electronics and Mobile Communication Conference (IEEE IEMCON), 27-30 October, Vancouver, Canada. Scopus Indexed. Accepted and due for publication., 2021

Taslima Akter Tamanna, Choudhury Turna, and Afsana Meem and Mohammad Monirujjaman Khan, "Mobile Application Based Teli-Nutrition System for Covid-19 Pandemic," 2021 IEEE 12th Annual Information Technology, Electronics and Mobile Communication Conference (IEEE IEMCON), 27-30 October, Vancouver, Canada. Scopus Indexed. Accepted and due for publication., 2021

Mohammad Monirujjaman Khan, Araf Noor and Fatin Anjum Khan , "Development of A Web Based Covid Portal and Marketplace," 2021 IEEE 12th Annual Information Technology, Electronics and Mobile Communication Conference (IEEE IEMCON), 27-30 October, Vancouver, Canada. Scopus Indexed. Accepted and due for publication., 2021, 2021

Mohammad Monirujjaman Khan, Md. Hafizur Rahman and Eshan Barua, "Development of Web-Based System for Essential Services During the COVID-19 Pandemic," 24th International Conference on Computer and Information Technology (ICCIT 2021) NSU, December 18-20,2021, Dhaka, Bangladesh. (Accepted and due for publication), 2021

Md. Nahid Hasan, Mahedi Hassan Pranto, Istiaqqe Azad, Shariar Mahmud Duke, Md. Talat Mahmud and Mohammad Monirujjaman Khan , "Towards the Development of a Common Platform for Pharmacists and Medicine Companies," 24th International Conference on Computer and Information Technology (ICCIT 2021) NSU, December 18-20,2021, Dhaka, Bangladesh. (Accepted and due for publication), 2021, 2021

Sayeda Islam Nahid and Mohammad Monirujjaman Khan, "Toxic Gas Sensor and Temperature Monitoring in Industries using Internet of Things (IoT)," 24th International Conference on Computer and Information Technology (ICCIT 2021) NSU, December 18-20,2021, Dhaka, Bangladesh. (Accepted and due for publication)., 2021

Ihfaz Tahmid Morshed, Mohammad Monirujjaman Khan, Saife Shuhaib Md. Enan and Fahim Tanzil Takin, "Development of Web Based Online One Stop Platform to Fight Covid-19," 2021 IEEE 12th Annual Ubiquitous Computing, Electronics and Mobile Communication Conference (IEEE UEMCON), 1-4 December, New York, USA. Scopus Indexed. Accepted and due for publication., 2021

Sheikh Elhum Uddin Quadery, Mehedi Hasan and Mohammad Monirujjaman Khan, "Consumer Side Economic Perception of Telemedicine During COVID-19 Era: A Survey on Bangladesh’s Perspective," Informatics in Medicine Unlocked, Elsevier, (Scopus Indexed.), 2021

Kayser Ahmed, Dewan Shakil, Farhan Amar Tanve, Rahat Anwar and Mohammad Monirujjaman Khan, "Development of Cable Operator Management System," IEEE 12th Annual Ubiquitous Computing, Electronics and Mobile Communication Conference (IEEE UEMCON), 1-4 December, New York, USA. Scopus Indexed. Accepted and due for publication., 2021

Kayser Ahmed, Dewan Shakil, Farhan Amar Tanve, Rahat Anwar and Mohammad Monirujjaman Khan, "Development of Cable Operator Management System," 2021 IEEE 12th Annual Ubiquitous Computing, Electronics and Mobile Communication Conference (IEEE UEMCON), 1-4 December, New York, USA Accepted and due for publication, 2021

Rezowana Akter, Jahid Khandaker, Shakil Ahmed, Muhtasim Munem Mugdho, A K M Bahalul Haque, "RFID Based Smart Transportation System With Android Application," International Conference on Innovative Mechanisms for Industry Applications (ICIMIA 2020), IEEE & Scopus Indexed, 2020

A. Sultana, M. M. Khan, "Design of UWB Band Notch Textile Antenna for Body-Centric Wireless Network with the Comparison of Five Different Textile Substrate," International Journal on Communications Antenna and Propagation Vol. 10, No 5, 2020. (Scopus Indexed, Cite Score 2.5, Q2), 2020

Mohammad Monirujjaman Khan, Rezaul Karim, "Development of Smart e-Health System for COVID-19 Pandemic," The 23rd International Conference on Computer and Information Technology (ICCIT-2020), December 19-21, 2020. pp. 1-6, doi: 10.1109/ICCIT51783.2020.9392743., 2020

Mohammad Monirujjaman Khan, Mahizbin Shams-E-Mofiz, Zerin anan Sharmin, "Development of E-Commerce Based Online Web Application for Covid-19 Pandemic," iBusiness, 12, 113-126, 2020. (Google Scholar). , 2020

Ahmed Rohani Islam, Kajol Bhowmick, Debalina Sikder, Hasan U. Zaman, "A Multifarious Design of a Microcontroller Based Home Security and Automation System," IEEE International Conference on Computational Intelligence and Communication Networks (CICN-2019), Hawaii, USA, 3-6 January, 2019

Md. Aowrongajab Uaday, Md. Nazmul Islam Shuzan, Saffan Shanewaze, Rakibol Islam Rakib and Hasan U Zaman, "The Design of a Novel Multi-Purpose Fire Fighting Robot with Video Streaming Capability," IEEE Sponsored 2019 5th International Conference for Convergence in Technology (IEEE 5th I2CT 2019 Pune), Pune, India, 29 -31 March, 2019

Md. Amanat Khan Shishir, Shahariar Rashid Fahim, Fairuz Maesha Habib, Tanjila Farah, "EYE ASSISTANT:Using mobile application to help the visually impaired," 1st International Conference on Advances in Science, Engineering and Robotics Technology (ICASERT-2019), 2019

Mohammad Fahim Hossain, Sudipta Barman, AKM Bahalul Haque, "Augmented Reality for Education; AR Children’s Book," IEEE TENCON 2019, 2019

Shuvashish Paul, Pinku Deb Nath, Naseef M. Abdus Sattar, Hasan U. Zaman, "A Web Application for Traffic Status Update using Crowd-Sourced Data Acquisition and Real-Time Modification," Journal of Theoretical and Applied Information Technology (JTAIT), 2018

Hasan U. Zaman, Rafiunnisa, Arafat Muhammad Shams, "A User-Friendly Low-Cost Mobile App Based Home Appliance Control And Circuit Breaker," 2nd International Conference on Computing Methodologies and Communication (IEEE ICCMC 2018), Erode, India, 2018

Mohammad Abu Sayed, Nusrat Shams and Hasan U. Zaman, "An IoT Based Robotic System for Irrigation Notifier," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

M. M. Tanzim Nawaz, Mahadi Hassan, Mir Golam Rasul and Hasan U. Zaman, "Web and Mobile Based Solution to Lost and Found Items in North South University," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Hasan U. Zaman, Tawsif Ur Rahman Choudhury and Nafis Imtiaz Ahme, "A User-Friendly and Efficient Design of a Unified Online Survey and Quizzing System," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Sheefta Naz, Syed Naffiz Hasan, Arka Basak and Hasan U. Zaman, "The Design of an Online Laundry System," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Mohammad Abu Sayed, Nusrat Jahan Prithee, Hasan U. Zaman, "Robotic Helping Hand: A New Mechanism for Helping Disabled People," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Mohammad Abdul Hye, Md Manjurul Akter, Atiq Mohammad Jahangir and Hasan U. Zaman, "A Novel Design and Implementation of Automated Feeding Mechanism in Fish Aquariums," 2nd International Conference on Electronics, Materials Engineering and Nano-Technology (IEEE IEMENTech 2018), Kolkata, India, 4-5 May, 2018

Sifat Rezwan, Wasit Ahmed, Mahrin Alam Mahia, Mohammad Rezaul Islam, "IoT Based Smart Inventory Management System for Kitchen Using Weight Sensors, LDR, LED, Arduino Mega and NodeMCU (ESP8266) Wi-Fi Module with Website and App," 2018 Fourth International Conference on Advances in Computing, Communication & Automation (ICACCA), 2018

Tasfiqul Ghani ; Nusrat Jahan ; Sadman Hossain Ridoy ; Abu Talha Khan ; Saif Khan ; Mohammad Monirujjaman Khan , "Amar Bangladesh – A Machine Learning Based Smart Tourist Guidance System," 2nd International Conference on Electronics, Materials Engineering & Nano-Technology (IEMENTech), 2018

Sanita Rahman, Emdadul Haque, Mahmudur Rahman and Hasan U. Zaman, "Web-based Automated Appliance Control System with Security and Gas Safety Systems," Proceedings of International Conference on Electrical, Computer and Communication Engineering (ECCE 2017), Cox's Bazar, Bangladesh, 16-18 February, 2017

Ali Adib Arnab, Sheikh Sadia Afrin, F.M. Fahad and Hasan U. Zaman, "A Cost Effective Way to Build a Web Controlled Search and CO Detector Rover," Proceedings of the 7th IEEE Annual Computing and Communication Workshop and Conference (IEEE CCWC 2017), Las Vegas, USA, 9-11 January, 2017

Tousif Osman, Shahreen Shahjahan Psyche, J. M. Shafi Ferdous, Hasan U. Zaman, "Intelligent Traffic Management System for Cross Section of Roads Using Computer Vision," Proceedings of the 7th IEEE Annual Computing and Communication Workshop and Conference (IEEE CCWC 2017), Las Vegas, USA, 9-11 January, 2017

Kazi Toyebul Haque, M.K. Robin, Mohammad Ashraful Anam, Hasan U. Zaman, "MediPro – A Cost Effective and User-Friendly Medical Information System," Proceedings of the International Conference on Intelligent Computing and Control Systems (IEEE ICICCS 2017), pp. 919-924, Madurai, India, 15-16 June, 2017

Mehal Zaman Talukder, Sheikh Shadab Towqir, Arifur Rahman Remon, Hasan U. Zaman, "An IoT Based Automated Traffic Control System With Real-Time Update Capability," Proceedings of the 8th International Conference on Computing, Communication And Networking Technologies (IEEE 8th ICCCNT 2017), Delhi, India, 3-5 July, 2017Shuvashish Paul, Pinku Deb Nath, Naseef M. Abdus Sattar and Hasan U. Zaman, "rTraffic – A Realtime Web Application for Traffic Status Update in the Streets of Bangladesh," Proceedings of the 2017 International Conference on Research and Innovation in Information Systems (IEEE ICRIIS), pp. 1-6, Langkawi Island, Malaysia, DOI: 10.1109/ICRIIS.2017.8002457, 16-17 July, 2017

Rokhsana Titlee, Ashfaq Ur Rahman, Hasan U. Zaman, and Hafiz Abdur Rahman, "A Novel Design of an Intangible Hand Gesture Controlled Computer Mouse using Vision Based Image Processing," 2017 3rd International Conference on Electrical Information and Communication Technology (IEEE EICT), Khulna, Bangladesh, 2017

Fatin Hasnath Chowdhury, Baized Shuvo, Mohammad Rezaul Islam, Tasfiqul Ghani, Saad Ahmed Akash, Rakib Ahsan, Nazia Nawar Hassan, "Design, control & performance analysis of secure you IoT based smart security system," 8th International Conference on Computing, Communication and Networking Technologies (ICCCNT), 2017

Hasan U Zaman, Fatin Hasnath Chowdhury, Rashik Ishrak Nahian, Tasfiqul Ghani, Baized Shuvo, Mohammad Rezaul Islam, SM Hasibul Hoq, "Design & Feasibility Analysis of Free to Walk," ICEIC 2017 International Conference on Electronics, Information, and Communication, 2017

Syed Emdad Ullah, Tania Alauddin and Hasan U. Zaman, "Developing an E-Commerce Website," Proc. of Intl. Conference on Microelectronics, Computing and Communication (IEEE MicroCom 2016), Durgapur, India, January 23-25, 2016

M. Arabi Hasan Sakib, Fakhrul Islam, Sabbir Samiul Haque, Hasan U. Zaman, "Doctor Locator: A Web Application to Improve Online Doctor Directories in Bangladesh," 5th International Conference on Informatics, Electronics & Vision (IEEE ICIEV), Dhaka, Bangladesh, paper no. 118, May 13-14, 2016

Faridur Rahman Hridoy, Kallal Das, Rifayat Hossain Arko and Hasan U. Zaman, "Development of an Online Bus Ticket Booking System for Transportation Services in Bangladesh," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 33, May 13-14, 2016

Syed Naffiz Hasan, Arka Basak, Sheefta Naz and Hasan U. Zaman, "The Online Laundry System," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 31, May 13-14, 2016

Hasan U. Zaman, Tawsif Ur Rahman Choudhury, Nafis Imtiaz Ahmed, "A Unified Online Survey and Quizzing System," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 109, May 13-14, 2016

Farhana Atuyar Saleh, Sadia Afrin Shopno, Hasan U. Zaman, "A Cost-effective SMS Based Tracking System Using GPS-GSM-GPRS Modules with Arduino and Smartphone," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 110, May 13-14, 2016

Mahmud M. Milton, Kazi Rizvan Hossain, Nahin Ahmed and Hasan U. Zaman, "Cost Effective Home Automation," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 119, May 13-14, 2016

Nahid Islam, A.S.M. Nesar Uddin, Sami Rahman, Hasan U. Zaman, "Universal MP controller," Student Conference on Informatics, Electronics & Vision (SCIEV), Dhaka, Bangladesh, paper no. 120, May 13-14, 2016

Hasan U. Zaman, Chowdhury, Rashik Ishrak Nahian, Ghani, S. M. Hasibul Hoq, Nazia Nawar Hassan, "Design & performance Analysis of Medimax: An android mobile application for patients," Proceedings of 12th Global Engineering, Science and Technology Conference, Dhaka, Bangladesh, 23–24 December 2016, 2016

S. M. Hasibul Hoq, Hasan U. Zaman, Shuvo, Chowdhury, Abid, Uddin, Ishaque, "Design, Control & Performance Analysis of a Smart Wheelchair: An android & joystick controlled user-friendly wheelchair," Proceedings of 12th Global Engineering, Science and Technology Conference, Dhaka, Bangladesh, 23–24 December, 2016

Shakil Ahmed, Nafis Farhan, Alimuddin Ahmed Ashfaq, Mohammad Monirujjaman Khan, "Development of Smart Communication System for the Autistic and the Disabled," 19th International Conference on Computer and Information Technology (ICCIT), 2016

Rahat Yasir, Md. Ashiqur Rahman, Nova Ahmed, "A Skin Disease Detection System for Financially Unstable People in Developing Countries," Global Science and Technology Journal, 2015

Rahat Yasir, Md. Shariful Islam Nibir, Zarmeen Ahmed Chadni and Nova Ahmed,, "Telemedicine System for Financially Unstable People of Bangladesh," Journal of Modern Science and Technology, 2015

Mohammad Monirujjaman Khan, Ratil Hasnat Ashique, et al. , "New Wavelet Thresholding Algorithm in Dropping Ambient Noise from Underwater Acoustic Signals," Journal of Electromagnetic Analysis and Applications, Vol. 7, No. 3, pp. 53-60, 2015

Mohammad Monirujjaman Khan , "Experimental Study of Dynamic Ultra Wideband On-Body Radio Propagation Channel for Medical Applications," Global Science and Technology Journal, Australia, Vol. 3, No.1, March 2015 Issue, pp. 94-106. , 2015

Rakibull Hasan, Mohammad Monirujjaman Khan, Asaduzzaman Ashek, "Microcontroller Based Home Security System with GSM Technology," Open Journal of Safety Science and Technology, Vol. 5, No 2, 2015

Mohammad Monirujjaman Khan, "Dynamic Ultra Wideband Radio Propagation Channel Study for Healthcare Applications," 10th Global Engineering, Science and Technology Conference, 2-3 January, 2015. Received Best Paper Award., 2015

Natasha Mounota, Mike Brayshaw, "Personalizing your social computing world: A case study using Twitter," Science and Information Conference (SAI), 2015

Nazmul Hossain, Mohammad Tanzir Kabir, Tarif Riyad Rahman, Mohamed Sajjad Hossen, Fahim Salauddin, "‘A Real-time Surveillance Mini-rover Based on OpenCV-Python-JAVA Using Raspberry Pi 2: An Application of Internet of Things (IoT)," 5th IEEE International Conference on Control Systems, Computing and Engineering (ICCSCE 2015), 2015

Neaz Md. Morshed, G M Muid Ur Rahman, Md. Rezaul Karim, Hasan U. Zaman, "Microcontroller Based Home Automation System Using Bluetooth, GSM, Wi-Fi and DTMF," Proc. 3rd Intl. Conference Advances in Electrical Engineering (IEEE ICAEE'15), pp. 124-127, Dhaka, Bangladesh, December 17-19, 2015

Hamdan Kaiser, Mumin Az Zahira Maria, Fatiha Jahan, Tanjila Farah, "QUEBO," International Journal of Engineering, Applied and Management Sciences Paradigms (IJEAM), 2015

Rahat Yasir, Md. Ashiqur Rahman and Nova Ahmed, "Dermatological Disease Detection usinG Image Processing and Artificial Neural Network," 8th International Conference of Electrical and Computer Engineering, ICECE, 2014

Syed Ishtiaque Ahmed, Steven J. Jackson, Nova Ahmed, Hasan S. Ferdous, Md. R. Rifat, Abu S. Rizvi, Shamir Ahmed, Rifat S. Mansur, "Protibadi: A Platform for Fighting Sexual Harassment in Urban Bangladesh," ACM Conference on Human Factors in Computing Systems, CHI, 2014

Fajilatun Nahar, A. M. Masudul Haque, Nova Ahmed, "ifreePhony: A touchscreen user interface for people with eye disability," Grace Hopper Conference, India, 2014

Mohammad Monirujjaman Khan, A. K. M Monsurul Alam, Prodip Kumer, "Investigation of a Compact Ultra Wideband Antenna for Wearable Applications," International Journal on Communications Antenna and Propagation, Vol. 4, No 4, pp. 124-129, 2014

Mohammad Monirujjaman Khan, "Study of Ultra Wideband Wireless Sensors for Body Area Networks," 1st International Conference on Electrical Engineering and Information & Communication Technology (ICEEICT), 10-12 April, 2014. Received Best Poster Paper Award (First Position). , 2014

Mohammad Monirujjaman Khan, "Comprehensive Study of On-Body Radio Channels at 2.45 GHz for Different Human Test Subjects," 1st International Conference on Electrical Engineering and Information & Communication Technology (ICEEICT), 10-12 April, 2014

Mohammad Monirujjaman Khan, "Comparison of Narrowband and Ultrawide Band Subject-Specific On-Body Radio Channel Studies for Healthcare Applications," 2nd International Conference on Green Energy and Technology, 5-6 September , 2014

International Conference on Computer and Information Technology ICCIT, "Beetles: A Mobile Application to Detect Crop Disease for Farmers in Rural Area," Rahat Yasir, Nova Ahmed, 2013

Rubaiat Bin Sattar, Nova Ahmed, Miftaur Rahman, "An Adaptive Approach for Video Streaming and Evaluation over Bluetooth Network," 8th International Conference on Wireless Communications, Networking and Mobile Computing (WiCOM), 2012

Md Kamrul Hasan, Saifur Rahman, Nova Ahmed, "Android Mobile Application: Remote Monitoring of Blood Pressure," International Conference on Computer and Information Technology , ICCIT, 2012

Rahat Yasir, Nova Ahmed , "Application of Mobile technology for diabetic test and health care monitoring system of Diabetic Patients," ICERIE, 2012

Qammer H Abbasi, Mohammad Monirujjaman Khan, Akram Alomainy and Yang Hao, "Ultra Wideband Off-Body Radio Channel Characterisation for Different Environments," 7th International Conference on Electrical and Computer Engineering (ICECE), 20-22 December , 2012

Mohammad Monirujjaman Khan, Qammer H. Abbasi, Akram Alomainy and Yang Hao, "Investigation of Body Shape Variations Effect on the Ultra Wideband On-Body Radio Propagation Channel," International Conference in Electromagnetics in Advanced Applications (ICEAA), September 12-17, 2011, Torino, Italy, 2011

Qammer H. Abbasi, Mohammad Monirujjaman Khan, Akram Alomainy and Yang Hao, "Characterization and Modelling of Ultra Wideband Radio Links For Optimum Performance Of Body Area Network in Health Care Applications," IEEE International Workshop on Antenna Technology (IWAT), 7-9 March, 2011, Hong Kong. (Shortlisted for best paper award)., 2011

Nusrat Tanzim, Khandkar M. Rashid, Shazzad Hosain, "Measurement and Prediction of Indoor Signal Propagation for ISM Band," International Conference on Advances in Electrical Engineering (ICAEE 2011), Dhaka, Bangladesh, December, 2011`

Mohammad Monirujjaman Khan, Akram Alomainy and Yang Hao, "Off-Body Radio Channel Characterisation Using Ultra Wideband Wireless Tags," International Conference on Body Sensor Networks (BSN), June 7 - 9, 2010, Biopolis, Singapore., 2010

S.S. Sami, T. Rahman, K.S. Hasan, J. Siddique, , "“An application program interface for vBulletin,”," The 11th International Conference on Computer and Information Technology,(ICCIT 2008), Khulna, Bangladesh, pp.36-39, 4-27 Dec. 2008., 2008

Md. Ashraf Uddin Bhuiyan and Md. Shazzad Hosain, "Performance Analysis of cdma2000 Wireless Standard Error Correcting Codes," International Conference on Computer and Information Technology (ICCIT) 2005, Islamic University of Technology (IUT), Dhaka, Bangladesh, pp. 1127-1132, December, 2005

Mohammad Rayed, Tawfique Elahi, SHAIKH SHAWON AREFIN SHIMON, Nova Ahmed, "MFS Design in Appstore-enabled Smart Featurephones for Low-literate, Marginalized Communities," CHI2023, 2023

Suvodeep Mazumdar, Sukaina Ehdeed, Andrea Jimenez, Faisal Ahmed, Sifat Momen, Mirza Rasheduzzaman , "Understanding the information landscape in agricultural communities in rural Bangladesh," The Electronic Journal of Information Systems in Developing Countries (EJISDC), 2022

Mohammad Monirujjaman Khan, SM Tahsinur Rahman and Sabik Tawsif Anjum Islam, "Online Education System in Bangladesh During COVID-19 Pandemic," Creative Education (CE). Vol. 12, No. 2, PP. 441-452, 2021, DOI: 10.4236/ce.2021.122031, (Google Scholar), 2021

Nazifa Tasneem, Md Anik Hasan, Sumaiya Binte Akther and Mohammad Monirujjaman Khan, "An Automatic Soil Testing Machine for Accurate Fertilization," 2021 IEEE World AI IoT Congress (AIIoT), 2021, pp. 0325-0331, doi: 10.1109/AIIoT52608.2021.9454248., 2021

Asif Zaman, Hasanul Banna, Mohammad Arshadul Alam Rakib, Shakil Ahmed, and Mohammad Monirujjaman Khan, "Impacts of Covid-19 on University Final Year Internship Students," Journal of Software Engineering and Applications, 14, 363-388. doi: 10.4236/jsea.2021.148022., (Google Scholar). , 2021

Md. Riazul Alam, Abrar Raiyan, Shabab Rahman,Tahmina Akter Taniaand and Mohammad Monirujjaman Khan , "Effect of COVID-19 on Medical Intern Students: Bangladesh Perspective," 2021 IEEE 12th Annual Information Technology, Electronics and Mobile Communication Conference (IEEE IEMCON), 27-30 October, Vancouver, Canada. Scopus Indexed. Accepted and due for publication.,, 2021

Mohammad Monirujjaman Khan, "Compact Printed Ultrawide Band Antenna for Body-Centric Wireless Communications," International Conference on Physics for Energy and Environment, 06-08 March, 2014, Atomic Energy Centre. Session Innovative Technology (Invited Talk) , 2014

Mohammad Monirujjaman Khan, Abdullah-Al-Mamun, Rifat Afroze, and Akram Alomainy, "Study of Two Different Receiver Antennas for Ultra Wideband Off-body Radio Propagation Channels," International Conference on Electrical, Computer and Telecommunication Engineering (ICECTE-2012), 01-02 December , 2012

Balwinder Raj, B Gupta, B Gupta Shalendra Singh and Mohammad Monirujjaman Khan, "Distributed Intelligent Circuits and Systems," World Scientific, https://doi.org/10.1142/13505, ISBN: 978-981-127-952-2 , 2023

Jeetendra Singh, Balwant Raj Balwant Raj and Mohammad Monirujjaman Khan, "Role of High-Performance VLSI in the Advancement of Healthcare Systems," In book: Advanced Circuits and Systems for Healthcare and Security Applications, 1st Edition, CRC Press, eBook ISBN9781003189633, July 2022., 2022

Mehedi Hasan, Md. Jobayer Hossein, Mainul Hossain, Hasan U. Zaman, Sharnali Islam, "Design of a Scalable Low-Power 1-bit Hybrid Full Adder for Fast Computation," IEEE Transactions on Circuits and Systems II: Express Briefs, PP(99):1-1, DOI: 10.1109/TCSII.2019.2940558, September, 2019

Syed Ahsanul Karim and Hasan U. Zaman, "Implementation of Digital Circuits from Truth Tables using MIGFETs," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Syed Ahsanul Karim and Hasan U. Zaman, "Qualitative Analysis of an Equivalent Full Adder Circuit Using MIGFET," Proc. of Intl. Conference on Microelectronics, Computing and Communication (IEEE MicroCom2016), Durgapur, India, January 23-25, 2016

Syed Ahsanul Karim and Hasan U. Zaman, "Simulation and Visualization of Carrier Trajectories in Distributed MIGFET Devices," 19th International Conference on Computer and Information Technology (IEEE ICCIT2016), Dhaka, 18-20 December, 2016

Maofic Farhan Karin, Khandaker Sharif Noor and Hasan U. Zaman, "Hardware Based Design and Implementation of a Bottle Recycling Machine using FPGA," 2016 IEEE Conference on Systems, Process and Control (IEEE ICSPC 2016), Melaka, Malaysia, 16-17 December, 2016

Sharmin Abdullah, Nusrat Sharmin, Nafisha Alam, "Multi Cycle Implementation Scheme for 8 bit Microprocessor by VHDL," International Journal of Engineering Research & Technology (IJERT), 2014

Michael Klaiber, Donald G. Bailey, Silvia Ahmed, Yousef Baroud, Sven Simon, "A high-throughput FPGA architecture for parallel connected components analysis based on label reuse.," FPT, 2013

M. Klaiber, S. Ahmed, M. Najmabadi, Y. Baroud, W. Li, S. Simon, "Imaging Sensor with integrated feature extraction using connected component labeling," SENSOR, 2013

S. Ahmed, Z. Wang, M. Klaiber, S. Wahl, M. Wroblewski, S. Simon, "Parallel hardware architecture for JPEG-LS basen on domain decomposition.," SPIE Volume 8499, 2012

J. Laackmaan, S. Ahmed, R. Sedelmayer, M. Klaiber, W. Pauer, S. Simon, and H.-U. Moritz, "Investigation of polymerization and drying of polyvinylpyrrolidone in an acoustic levitator using a smart camera for online process measurement," ICLASS, 2012

M. Klaiber, S. Ahmed, Z. Wang, L. Rockstroh, Y. Gera, S. Simon, "Online imaging analysis of spray processes based on a reconfigurable embedded system," 10th Workshop über Sprays, Techniken der Fluidzerstäubung und Untersuchungen von Sprühvorgängen, 2012

Hasan Zaman, "Process Compilation Methods for Thin Film Devices," LAP Lambert Academic Publishing (ISBN: 978-3-8383-8231-9), 2010

H. U. Zaman, J. Shen, and P. Krivacek, "Achieving 130MHz in 0.16um in a TD-SCDMA Coprocessor Chip," Analog Devices General Technical Conference (GTC), MA, USA, 2007

H. U. Zaman, E. T. Carlen, and C. H. Mastrangelo, "Automatic Generation of Thin Film Process Flows — Part I: Basic Algorithms," IEEE Transactions on Semiconductor Manufacturing, vol. 12, no. 1, pp. 116-128, 1999

H. U. Zaman, E. T. Carlen, and C. H. Mastrangelo, "Automatic Generation of Thin Film Process Flows — Part II: Recipe Generation, Flow Evaluation, and System Framework," IEEE Transactions on Semiconductor Manufacturing, vol. 12, no. 1, pp. 129-138, 1999

H. U. Zaman and C. H. Mastrangelo, "Process compilation of thin film microdevices," IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 15, no. 7, pp. 745-764, 1996

H. U. Zaman and C. H. Mastrangelo, "MISTIC 1.1: A process compiler for micro-machined devices," Proc. 8th Intl. Conference Solid-State Sensors and Actuators (Transducers'95), vol. 1, pp. 38-42, Stockholm, Sweden, 1995

Mohammad Monirujjaman Khan, Alvee Morsele Kabir, Abul Mohammed Raihanul Alam, Sharaban Tahura Nisa, "A Virtual Reality (VR) Based Interactive and Educative Experience of Hajj and Umrah for the People of Bangladesh," IEEE 11th Annual Computing and Communication Workshop and Conference (IEEE CCWC 2020), 27th-30th January 2021, USA. pp. 0170-0173, doi: 10.1109/CCWC51732.2021.9375915., 2021

Sadman Chowdhury Siam; Abrar Faisal; Niazi Mahrab; AKM Bahalul Haque; Md. Naimul Islam Suvon, "Automated Student Review System with Computer Vision and Convolutional Neural Network," 2021 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS), 2021

Mohammad Fahim Hossain; Sudipta Barman; Niloy Biswas; A K M Bahalul Haque, "Augmented Reality in Medical Education: AR Bones," 2021 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS), 2021

AKM Bahalul Haque; Ayman Muniat; Parisha Rafiq Ullah; Shimin Mushsharat, "An Automated Approach towards Smart Healthcare with Blockchain and Smart Contracts," 2021 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS), 2021

A K M Bahalul Haque, Bharat Bhushan, "Blockchain in a Nutshell: State-of-the-Art Applications and Future Research Directions," Blockchain and AI Technology in the Industrial Internet of Things, IGI Global, Pennsylvania, United States, 2021

Nuerrennisahan Aimaiti, Shahadat Hossain, Mohammad Sakib Mahmud, "Computational Experience with Diagonally Structured Linear Algebra in Java," HP3C 2020: Proceedings of the 2020 4th International Conference on High Performance Compilation, Computing and Communications, 2020

Mohammad Fahim Hossain, Sudipta Barman, AKM Bahalul Haque, "Augmented Reality for Education; AR Children’s Book," IEEE TENCON 2019, 2019

Shahadat Hossain, Mohammad Sakib Mahmud, "On Computing with Diagonally Structured Matrices," 2019 IEEE High Performance Extreme Computing Conference (HPEC), 2019

Shuvashish Paul, Pinku Deb Nath, Naseef M. Abdus Sattar, Hasan U. Zaman, "A Web Application for Traffic Status Update using Crowd-Sourced Data Acquisition and Real-Time Modification," Journal of Theoretical and Applied Information Technology (JTAIT), 2018

Sayma Shammi, Sayeed Islam, Hafiz Abdur Rahman, Hasan U. Zaman, "An Automated Way of Vehicle Theft Detection in Parking Facilities by Identifying Moving Vehicles in CCTV Video Stream," International Conference on Communication, Computing & Internet of Things (IEEE IC3IoT 2018), Chennai, India, 2018

Sadia Chowdhury, Farhan Rahman Wasee, Md Shafiqul Islam and Hasan U. Zaman, "Bengali Handwriting Recognition and Conversion to Editable Text," 2018 Second International Conference on Advances in Electronics, Computers and Communications (IEEE ICAECC-2018), Bangalore, India, 2018

M. M. Tanzim Nawaz, Mahadi Hassan, Mir Golam Rasul and Hasan U. Zaman, "Web and Mobile Based Solution to Lost and Found Items in North South University," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Hasan U. Zaman, Tawsif Ur Rahman Choudhury and Nafis Imtiaz Ahme, "A User-Friendly and Efficient Design of a Unified Online Survey and Quizzing System," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Sheefta Naz, Syed Naffiz Hasan, Arka Basak and Hasan U. Zaman, "The Design of an Online Laundry System," International Conference on Electrical, Electronics, Computers, Communication, Mechanical and Computing (IEEE EECCMC-2018), Tamil Nadu, India, 2018

Kazi Toyebul Haque, M.K. Robin, Mohammad Ashraful Anam, Hasan U. Zaman, "MediPro – A Cost Effective and User-Friendly Medical Information System," Proceedings of the International Conference on Intelligent Computing and Control Systems (IEEE ICICCS 2017), pp. 919-924, Madurai, India, 15-16 June, 2017

Shuvashish Paul, Pinku Deb Nath, Naseef M. Abdus Sattar and Hasan U. Zaman, "rTraffic – A Realtime Web Application for Traffic Status Update in the Streets of Bangladesh," Proceedings of the 2017 International Conference on Research and Innovation in Information Systems (IEEE ICRIIS), pp. 1-6, Langkawi Island, Malaysia, DOI: 10.1109/ICRIIS.2017.8002457, 16-17 July, 2017

Rokhsana Titlee, Ashfaq Ur Rahman, Hasan U. Zaman, and Hafiz Abdur Rahman, "A Novel Design of an Intangible Hand Gesture Controlled Computer Mouse using Vision Based Image Processing," 2017 3rd International Conference on Electrical Information and Communication Technology (IEEE EICT), Khulna, Bangladesh, 2017

Md. Hasan Mahmood and Md. Shazzad Hosain, "Improving test case prioritization based on practical priority factors," 8th IEEE International Conference on Software Engineering and Service Science (ICSESS), Beijing, China, Nov 24 – 26, 2017

Natasha Mounota, Mike Brayshaw, "Personalizing your social computing world: A case study using Twitter," Science and Information Conference (SAI), 2015

Syed Akib Anwar Hridoy, Faysal Ahmed and Md. Shazzad Hosain, "Regression Testing based on Hamming Distance and Code Coverage," International Journal of Computer Applications, 2015

Adnan Firoze, Rashedur M. Rahman, "Mining ICDDR, B Hospital Surveillance Data and Exhibiting Strategies for Balancing Large Unbalanced Datasets," International Journal of Healthcare Information Systems and Informatics (IJHISI), 2015

Adnan Firoze, Rashedur M Rahman, "Mining ICDDR, B Hospital Surveillance Data Using Locally Linear Embedding Based SMOTE Algorithm and Multilayer Perceptron," Lecture Notes in Computer Science (Springer), 2015

David D. Pokrajac, Abdullah-Al-Zubaer Imran and Predrag R. Bakic, "Monte Carlo testing and verification of numerical algorithm implementations," International Conference on Advanced Technologies, Systems, and Services in Telecommunications - TELSIKS, Nis, Serbia, October, 2015

Sukanta Basak and Md. Shazzad Hosain, "Software Testing Process Model from Requirement Analysis to Maintenance," International Journal of Computer Applications, 2014

Saniat Javid Sohrawardi, Iftekhar Azam, Shazzad Hosain, "A Comparative Study of Text Classification Algorithms on User Submitted Bug Reports," IEEE International Workshop on Data Management (IWDM 2014), Bangkok, Thailand, Sep - Oct , 2014

Md. Safaet Hossain, Md. Shazzad Hosain, "Web Test Integration and Performance Evaluation of E-Commerce Web Sites," International Journal of Computer Science and Information Security, 2012

Bushra Hoq, Samia Jafrin, Shazzad Hosain, "Dependency Cognizant Test Case Prioritization," Conference on Computational Intelligence and Software Engineering (CiSE 2011), Wuhan, China, December , 2011

Adnan Firoze, M. Shamsul Arifin, Ryana Quadir, Rashedur M. Rahman, "BANGLA Isolated Word Speech Recognition," International Conference on Enterprise Information Systems (ICEIS) , 2011

M. A. Rahman and M. A. Sattar, "A New Approach to Sort Unicode Bengali Text," International Conference on Electrical and Computer Engineering (ICECE), 2008

Md. Shazzad Hosain and Md. Shamsul Alam, "Software Reliability Using Markov Chain Usage Model," 3rd International Conference on Electrical & Computer Engineering (ICECE), Dhaka, Bangladesh, pp. 621 - 624, December , 2004

Fariha Zannat, Mohammad MonirujjamanKhan and Saif Al Sohad, "Automated System For Features Extraction From PCG Signal," 5th International Conference on Computing Methodologies and Communication (ICCMC 2021), 08-10, April 2021, DOI: 10.1109/ICCMC51019.2021.9418229, 2021

Shahriar Rahman1, Shazzadur Rahman1 and A K M Bahalul Haque1, "Prediction of Solar Radiation Using Artificial Neural Network," Journal of Physics: Conference Series, 2021

Mohammad Monirujjaman Khan et al., , "Research and Development of Virtual Reality Application for Teaching Medical Students," The 12th International Conference On Computing, Communication and Networking Technologies (ICCCNT), July 6 – 8, IIT – Kharagpur, West Bengal, India. (Accepted). , 2021

Mohammad Monirujjaman Khan, Zobayda Hossain Arshie, Tahia Tazin, Saima Islam, Mahmudur Khan Tanzid and Ratil H. Ashique, "Development of Home Automation System by Using Brain Wave," 2nd International Conference on Sustainable Technology for Industry 4.0 (STI 2020), 19-20 December 2020.pp. 1-5, doi: 10.1109/STI50764.2020.9350509., 2020

F. Haque, V. Dehghanian, A. O. Fapojuwo and J. Nielsen, "A Sensor Fusion-Based Framework for Floor Localization," IEEE Sensors Journal, 2019

Sayma Shammi, Sayeed Islam, Hafiz Abdur Rahman, Hasan U. Zaman, "An Automated Way of Vehicle Theft Detection in Parking Facilities by Identifying Moving Vehicles in CCTV Video Stream," International Conference on Communication, Computing & Internet of Things (IEEE IC3IoT 2018), Chennai, India, 2018

Md. Jamilur Rahman, Deb Prosad Das, Ohidul Islam and Hasan U. Zaman, "A Novel Design of A Robotic Object Sorter Based on Color Differences Using Image Processing Techniques," International Conference on Computer, Communication, Chemical, Materials and Electronic Engineering (IEEE IC4ME2-2018), Rajshahi, Bangladesh, 2018

Adnan Firoze, Tonmoay Deb, "Face Recognition Time Reduction Based on Partitioned Faces without Compromising Accuracy and a Review of state-of-the-art Face Recognition Approaches," Proceedings of the 2018 International Conference on Image and Graphics Processing (ACM), 2018

Adnan Firoze, Tousif Osman, Shahreen Shahjahan Psyche, Rashedur M Rahman, "Scoring Photographic Rule of Thirds in a Large MIRFLICKR Dataset: A Showdown Between Machine Perception and Human Perception of Image Aesthetics," Springer Lecture Notes in Computer Science book series (LNCS, volume 10751), 2018

Abu Talha Khan, Sadia Afrin, Tanzilur Rahman, "Comparison of Principal Component Analysis and Partial Least Square Discriminant Analysis in the classification of EEG signals," IEEE SiPS'18, 2018

Tashreque Mohammed Haq, Safkat Arefin, Shamiur Rahman, Tanzilur Rahman, "Extraction of Fetal ECG from Maternal Abdominal Record in the 3rd trimester of gestation using R-R interval windowing technique," IEEE SiPS'18, 2018

Tashreque Mohammed Haq, Safkat Arefin, Shamiur Rahman, Tanzilur Rahman, "Extraction of Fetal Heart Rate from Maternal ECG— Non Invasive Approach for Continuous Monitoring during Labor," Eurosensors 2018, 2018

Mahbubur Rahman Mishal, Tanvir Tazul Islam, Shahadat Hossain Antor, Tanzilur Rahman, "A Quantitative Analysis of Glucose from Enhanced NIR Spectra through Linear Regression Model Coupled with Optimized Bandpass Filtering," Eurosensors 2018, 2018

Adam J. Kuperavage, Abdullah-Al-Zubaer Imran, Predrag R. Bakic, Andrew D.A. Maidment and David D. Pokrajac, "Validation of Cooper’s ligament thickness in software breast phantoms," SPIE Medical Imaging: Physics of Medical Imaging, Orlando, Florida, USA, March, 2017

Hasan U. Zaman, Naushaba Zerin, Md. Hasin Jamal, Joytu Khisha, "Speech Responsive Mobile Robot for Transporting Objects of Different Weight Categories," Proceedings of the 18th International Conference on Advanced Robotics (IEEE ICAR 2017), Hong Kong Science and Technology Park, Honk Kong, 10-12 July, 2017

Syed Samiullah Al Mashrur, Md. Mahmudul Alam Nirjhor, Md. Saiful Islam, Hasan U. Zaman, "A Novel Way of 3D Map Making Using A Laser Rangefinder for Plane Surfaces," 2017 IEEE Region 10 Conference (IEEE TENCON), Penang, Malaysia, 5-8 November, 2017

Mithun Biswas, Gautam Kumar Shom, Rafiqul Islam, Md. Shopon, Nabeel Mohammed, Sifat Momen, Anowarul Abedin, "BanglaLekha-Isolated: A multi-purpose comprehensive dataset of Handwritten Bangla Isolated characters," Data in Brief, 2017

F. Haque, V. Dehghanian and A. O. Fapojuwo, "Sensor fusion for floor detection," 2017 8th IEEE Annual Information Technology, Electronics and Mobile Communication Conference (IEMCON), 2017

Lesley Cockmartin, Hilde Bosmans, Kristina Bliznakova, David D. Pokrajac, Abdullah-Al-Zubaer Imran, Nicholas Marshall, Andrew D.A. Maidment and Predrag R. Bakic, "Creation of realistic structured backgrounds using adipose compartment models in a test object for breast imaging performance analysis," Radiological Society of North America (RSNA): Scientific Assembly and Annual Meeting, Chicago, Illinois, November, 2016

Abdullah-Al-Zubaer Imran, David D. Pokrajac, Andrew D.A. Maidment and Predrag R. Bakic, "Estimation of adipose compartment volumes in CT images of a mastectomy specimen," SPIE Medical Imaging: Physics of Medical Imaging, San Diego, California, March, 2016

Adam J. Kuperavage, Abdullah-Al-Zubaer Imran, Predrag R. Bakic, and David D. Pokrajac, "Validation of simulated Coopers’ ligaments in anthropomorphic breast phantoms using three-dimensional watershed method," DE IDeA Conference, Newark, Delaware USA, February, 2016

Abdullah-Al-Zubaer Imran, "Estimation of breast anatomical descriptors from mastectomy CT images," MS Thesis: School of Graduate Studies and Research, Delaware State University, Dover, Delaware USA, August, 2016

S.M.A. Sharif, Nabeel Mohammed, Nafees Mansoor, Sifat Momen, "A hybrid deep model with HOG features for Bangla handwritten numeral classification," 9th International Conference on Electrical and Computer Engineering (ICECE-2016, IEEE), 2016

Tasnim Sami, Nabeel Mohammed, Sifat Momen, "Learning “initial feature weights” for CBIR using query augmentation," International Journal of Multimedia Information Retrieval, 2016

M Maksud Alam, Zahidul Amin, and Md. Serajul Abrar, "Performance Analysis Of Reed Muller Coded OFDM On Nakagami−m Fading Environment," Proc. 4th IEEE/CIC International Conference on Communications in China, ICCC, Shenzhen, China, 2015

M Maksud Alam, Farabi Hasan Chadni and Saiful Ahmed Papon, "Performance Analysis of MIMO-COFDM under Rayleigh Fading Channel," Proc. 7th IEEE International Conference on Wireless Communications and Signal Processing, WCSP, Nanjing, China, 2015

Abdullah-Al-Zubaer Imran, Predrag R. Bakic and David D. Pokrajac, "Spatial distribution of adipose compartments size, shape, and orientation in a CT breast image of a mastectomy specimen," IEEE Signal Processing in Medicine and Biology Symposium (SPMB), Philadelphia, Pennsylvania USA, December, 2015

Abdullah-Al-Zubaer Imran and David D. Pokrajac, "Qualitative improvement of CT breast image for screening and analysis of segmented compartments for classification," DSU Graduate Research Symposium, Dover, Delaware USA, April, 2015

Rabiul Islam Jony, Nabeel Mohammed, Ahsan Habib, Sifat Momen, Rakibul Islam Rony, "An Evaluation of Data Processing Solutions Considering Preprocessing and “Special” Features,," 11th International Conference on Signal Image Technology & Internet Based Systems (SITIS-2015, IEEE), 2015

M Maksud Alam, Nusrat J. Disha, Md. Ataur Rahman and Besma Smida, "Maximum PEP and ICI Over Coset Representatives for 32 Subcarriers Reed- Muller Coded OFDM," Proc. 8th IEEE International Conference on Electrical & Computer Engineering, ICECE, Dhaka, Bangladesh, 2014

Abdullah-Al-Zubaer Imran, Tomasz G. Smolinski, and David D. Pokrajac, "Classification of magnetic resonance brain images using feature extraction and adaptive neuro-fuzzy inference," Delaware Center for Neuroscience Research: Annual Neuroscience Research Symposium, Newark, Delaware USA, December, 2014

M Maksud Alam and Besma Smida, "PAPR and ICI Reduction of OFDM Signals," Proc. 1st International Conference on Control, Engineering and Information Technology, ICCEIT, Tunisia, 2013

M Maksud Alam, "A coding technique to reduce PAPR and interference of OFDM systems, M. S. Thesis," ProQuest, UMI Dissertations Publishing, Ann Arbor, MI, USA, 2013

S. Rahman, M. Booth, "Direct wavefront sensing in adaptive optical microscopy using backscattered light," Applied Optics, 2013

S. M. Sarwar, I. Hossain, "A Novel Reduced Reference Image Quality Analysis Metric for JPEG Compressed Images Based on Image Segmentation," International Conference on Informatics, Electronics and Vision (ICIEV), 2013

Michael Klaiber, Donald G. Bailey, Silvia Ahmed, Yousef Baroud, Sven Simon, "A high-throughput FPGA architecture for parallel connected components analysis based on label reuse.," FPT, 2013

M. Klaiber, S. Ahmed, M. Najmabadi, Y. Baroud, W. Li, S. Simon, "Imaging Sensor with integrated feature extraction using connected component labeling," SENSOR, 2013

Adnan Firoze, M. Shamsul Arifin, Rashedur M. Rahman, "Bangla User Adaptive Word Speech Recognition – Approaches and Comparisons," International Journal of Fuzzy System Applications (IJFSA), 2013

I. Hossain, M. El-Sakka, "Prediction with Partial Match Using Two-dimensional Approximate Contexts," Picture Coding Symposium (PCS), 2012

Zhe Wang, Sven Simon, Michael Klaiber, Silvia Ahmed, Thomas Richter, "SSPQ – spatial domain perceptual image codec based on subsampling and perceptual quantization.," ICIP, 2012

S. Ahmed, Z. Wang, M. Klaiber, S. Wahl, M. Wroblewski, S. Simon, "Parallel hardware architecture for JPEG-LS basen on domain decomposition.," SPIE Volume 8499, 2012

J. Laackmaan, S. Ahmed, R. Sedelmayer, M. Klaiber, W. Pauer, S. Simon, and H.-U. Moritz, "Investigation of polymerization and drying of polyvinylpyrrolidone in an acoustic levitator using a smart camera for online process measurement," ICLASS, 2012

M. Klaiber, S. Ahmed, Z. Wang, L. Rockstroh, Y. Gera, S. Simon, "Online imaging analysis of spray processes based on a reconfigurable embedded system," 10th Workshop über Sprays, Techniken der Fluidzerstäubung und Untersuchungen von Sprühvorgängen, 2012

Shamsul Arifin, Adnan Firoze, M. Ashraful Amin, Hong Yan, "Dermatological Disease Diagnosis using Color-skin Images," International Conference on Machine Learning and Cybernetics (ICMLC), 2012

M.I. Alamgir, A.U.H. Gulib, K.M.U. Ahmed, "Performance Analysis of Dg MOSFETs With High -K Stack On Top & Bottom Gate," International Journal of Scientific & Technology Research, Vol-1, Issue-5, June 2012, 2012

Adnan Firoze, M. Shamsul Arifin, Ryana Quadir, Rashedur M. Rahman, "BANGLA Isolated Word Speech Recognition," International Conference on Enterprise Information Systems (ICEIS) , 2011
"""

# Regular expression to extract authors and titles
pattern = r"(.+?),\s*\"(.+?)\""

matches = re.findall(pattern, text)

# Save to CSV
with open('research_authors_titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Authors', 'Title'])  # Header row
    for match in matches:
        writer.writerow(match)

print("Data saved to research_authors_titles.csv")
