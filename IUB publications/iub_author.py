import csv
import re

# Text content
text = """
Md. Tarek Habib, Abdullah Al-Mamun, Md. Sadekur Rahman, Shah Md. Tanvir Siddiquee, Farruk Ahmed

 , "An Exploratory Approach to Find a Novel Metric Based Optimum Language Model for Automation Bangla Word Prediction", International Journal of Intelligent Systems and Applications (IJISA), vol.10, no.2, pp.47-54, Hong Kong, ISSN: 2074-904X (Print); 2074-9058 (Online) , 2018
Md. Aminur Islam, Faisal Bin Abul Kashem, Sakib-Uz-Zaman Khan, Md. Tarek Habib, Farruk Ahmed

 , "Cloud Computing in Education: Potentials and Challenges for Bangladesh", International Journal of Computer Science, Engineering and Applications (IJCSEA), vol.7, no.5, pp.11-21, India, ISSN: 2231-0088 (Print); 2230-9616 (Online) , 2017
Mohammad Noor Nabi, Md. Shafiul Alam, Farruk Ahmed

 , "Instruction Set Usage and Performance Analysis of Elliptic Curve Cryptography and other Network Security Algorithms", Journal of the Bangladesh Electronics Society , Bangladesh , 2016
Zakaria Farah Ahmed, Mohammad Noor Nabi, Farruk Ahmed

 , "Implementation and Analysis of Ethernet Switch Protocols", Journal of the Bangladesh Electronics Society, Bangladesh , 2016
Md. Tarek Habib, Shaon Bhatta Shuvo, Mohammad Shorif Uddin, Farruk Ahmed

 , "Automated Textile Defect Classification by Bayesian Classifier Based on Statistical Features", Proceedings of International Workshop on Computational Intelligence (IWCI), pp.103-107, Bangladesh , 2016
Md. Aziz Ul Haque, Farruk Ahmed

 , "Design and Implementation of a One Way Digital Delay Circuit Useable in a Bridge Inverter to Drive Power Devices of a Same Leg in Toggling Stage", Journal of the Bangladesh Electronics Society , Bangladesh , 2016
M. U. Kabir, M Noor Nabi, Farruk Ahmed, M A Sobhan, M. Kamrul Alam Khan

 , "Dispensation of Commons Radio Spectrum Management Framework Issues in Implementation: Challenges and Opportunities", Journal of the Bangladesh Electronics Society, Bangladesh , 2016
Md. Mozaharul Mottalib, Mokhlesur Rahman, Md. Tarek Habib, Farruk Ahmed

 , "Detection of the Onset of Diabetes Mellitus by Bayesian Classifier Based Medical Expert System", Transaction on Machine Learning and Artificial Intelligence, vol.4, no.4, pp.1-8, UK, ISSN: 2054-7390 , 2016
Md. Mozaharul Mottalib, Md. Tarek Habib, M. Rokonuzzaman, Farruk Ahmed

 , "Fabric Defect Classification with Geometric Feature Using Bayesian Classifier", Proceedings of International Conference on Advances in Electrical Engineering (ICAEE), pp.160-163, Bangladesh , 2015
Sonia Sadeque, Imran Ahmed, Imtiaz Ahmed, Farruk Ahmed

 , "Asymptotic Performance of Spatial Modulation under Generalized Fading Channels", IUB Journal of Engineering and Computer Science, Bangladesh , 2015
M. U. Kabir, Mohammad Noor Nabi, Farruk Ahmed, M Abdus Sobhan, M Kamrul Alam Khan

 , "A concept of Radio Spectrum Administration Following Executive Incentive Pricing (EIP) Paradigm", IUB Journal of Engineering and Computer Science, Bangladesh , 2015
Subrata Kumar Dey, M Abdus Sobhan, Ali Shihab Sabbir, Farruk Ahmed

 , "Grid/Cloud-Based e-Governance Framework for Higher Education Institute and Perception Thereof: Bangladesh Perspective", IUB Journal of Engineering and Computer Science, Bangladesh , 2015
Md. Kabir Uddin, Mohammad Noor Nabi, Farruk Ahmed and M Abdus Sobhan

 , "A Potential Framework and Canons to Understand Next Generation Radio Spectrum Management Issues in South Asian Countries", IUB Journal of Engineering and Computer Science, Bangladesh , 2015
Md. Tarek Habib, Rahat Hossain Faisal, M. Rokunuzzaman and Farruk Ahmed

 , "Automation Fabric Defect Inspection: A Survey of Classifiers", International Journal in Foundations of Computer Science & Technology, vol.4, no.1, pp.17-25 , India, ISSN: 1839-7662 , 2014
Subrata Kumar Dey, Mohammad Noor Nabi, Mohammed Anwer, Farruk Ahmed

 , "Implementation and Performance Evaluation of Proposed Iterative Parallel Algorithm to Solve Large System of Linear Equations (LSLE)", Journal of Bangladesh Electronics Society , Bangladesh , 2013
Md. Tarek Habib, Rahat Hossain Faisal, M Rokonuzzaman, Farruk Ahmed

 , "A Survey of Classifiers for Automated Textile Defect Inspection System", Proceedings of Bangladesh Electronics Society Conference, pp.218-223, Bangladesh , 2012
Rahat Hossain Faisal, A. N. M. T Islam, Md. Tarek Habib and Farruk Ahmed

 , "Performance Analysis of Mobile Ad-Hoc Network Routing Protocols over UDP", Proceedings of Bangladesh Electronics Society Conference, pp.49-55, Bangladesh , 2012
Rahat Hossain Faisal, A. N. M. T. Islam, Md. Tarek Habib and Farruk Ahmed

 , "A Comparative Study on Different Routing Protocols of Ad-Hoc Network over User Datagram Protocol", Journals of the Bangladesh Electronics Society, vol.12, no.1-2, Bangladesh, ISSN: 1816-1510 , 2012
Md. Aziz Ul Huq, Farruk Ahmed

 , "Design and Implementation of an Interfacing Technique between the Microcomputer and A Three-Phase Induction Motor Control System", Journal of the Bangladesh Electronics Society, Bangladesh , 2011
Md. Tarek Habib, Abdul Halim Miah, Farruk Ahmed

 , "A Rigorous Taxonomy Based Survey of Location Systems for Ubiquitous Computing", Proceedings of International Conference on Advances in Electrical Engineering (ICAEE), Bangladesh , 2011
Ahmed Lutful Kabir, Rajeeb Saha, Md. Arman Khan, Munawwar M Sohul, Farruk Ahmed

 , "Locating Mobile Station Using Received Signal Parameters", Journal of the Bangladesh Electronics Society, Bangladesh , 2011
N. M. Shafiul Kabir Chowdhury, Md. Shahriar Hussain, Afroza Sultana, Farruk Ahmed

 , "Distance Dependent Service Differentiation of the IEEE 802.11e EDCA on Single Access Point Based WLAN Systems", Journal of the Bangladesh Electronics Society, Bangladesh , 2011
Md. Amir Ali Hasan, Amith Khandaker, Faiza Nabita, Sayeed Islam, Imtiaz Ahmed, Imran Ahmed, Farruk Ahmed, Mohammad Abdullah Al Zobaiba

 , "Estimation of Timing Offset Error in OFDM System and Selection of Modulation Technique for Best Performance", Journal of the Bangladesh Electronics Society, Bangladesh , 2011
Md. Tarek Habib, Abdul Halim Miah and Farruk Ahmed

Md Abrar Istiaq, M. M. Mahbubul Syeed, Md Shakhawat Hossain, Mohammad Faisal Uddin, Mahady Hasan and Razib Hayat Khan, Adoption of Unmanned Aerial Vehicle (UAV) Imagery in Agricultural Management: A Systematic Literature Review, Ecological Informatics, Elsevier. DOI: https://doi.org/10.1016/j.ecoinf.2023.102305, vol. , no., pp. . 2023. [Rank: Q1.  IF: 5.1 CiteScore: 6.1]

	
Md Shakhawat Hossain, Md. Mahmudur Rahman, M. M. Mahbubul Syeed, Mohammad Faisal Uddin, Md Aulad Hossain, Md Abdus Samad, DeepPoly: Deep Learning based Polyps Segmentation and Classification for Autonomous Colonoscopy Examination, IEEE Access, DOI:https://doi.org/10.1109/ACCESS.2023.3310541, vol. , no., pp. . 2023.                     [Rank: Q1.  IF: 3.614]


Razib Hayat Khan, Ankan Shahriar, Md. Ahosan Hossain, M. M. Mahbubul Syeed, Mohammad Faisal Uddin and Md Shakhawat Hossain, Augmented Scope Based E-Commerce Business Model for Emerging Markets, Journal of Computer Science, Science Publications, 19(12), 1410-1422. https://doi.org/10.3844/jcssp.2023.1410.1422. 2023.                [Rank: Q4.  IF: .94]


Md Shakhawat Hossain, Galib Mohammad Shahriar, M. M. Mahbubul Syeed, Mohammad Faisal Uddin, Mahady Hasan, Shingla Shivam, Suresh Advani. "Region of Interest (ROI) Selection using Visiion Transformer for Automatic Analysis using Whole Slide Images", Nature Scientific Reports, 13, 11314 (2023). https://doi.org/10.1038/s41598-023-38109-6, July 2023.  [Rank: Q1     IF: 5.51]

	
M. M. Mahbubul Syeed, Md Shakhawat Hossain, Razaul Karim, Mohammad Faisal Uddin, Mahady Hasan, Razib Hayat Khan, 2023. "Surface Water Quality Profiling using the Water Quality Index, Pollution Index and Statistical Methods: A Critical Review", Environmental and Sustainability Indicators, Elsevier, Volume 18, 2023, 100247, ISSN 2665-9727,


Md Shakhawat Hossain, Galib Muhammad Shahriar, M. M. Mahbubul Syeed, Mohammad Faisal Uddin, Mahady Hasan, Md. Sakir Hossain, Rubina Bari, 2023. "Tissue Artifact Segmentation and Severity Assessment for Automatic Analysis using WSI ", IEEE Access, https://doi.org/10.1109/ACCESS.2023.3250556  [Rank: Q1     IF: 3.614]


M. M. Mahbubul Syeed, ASM Shihavuddin, Mohammad Faisal Uddin, Mahady Hasan, Razib Hayat Khan, 2022. "Outcome Based Education (OBE): Defining the Process and Practice for Engineering Education", IEEE Access, https://doi.org/10.1109/ACCESS.2022.3219477    [Rank: Q1     IF: 3.467]



Hossain, Md Shakhawat, M. M. Mahbubul Syeed, Kaniz Fatema, and Mohammad Faisal Uddin. 2022. "The Perception of Health Professionals in Bangladesh toward the Digitalization of the Health Sector" International Journal of Environmental Research and Public Health, MDPI 19, no. 20: 13695. https://doi.org/10.3390/ijerph192013695   [Rank: Q1     IF: 4.614]


Hossain, Md Shakhawat, M. M. Mahbubul Syeed, Kaniz Fatema, Md Sakir Hossain, and Mohammad Faisal Uddin. 2022. "Singular Nuclei Segmentation for Automatic HER2 Quantification Using CISH Whole Slide Images" Sensors, MDPI 22, no. 19: 7361. https://doi.org/10.3390/s22197361     [Rank: Q1     IF: 3.847]


Haque, Rakib Ul, Razib Hayat Khan, A. S. M. Shihavuddin, M. M. Mahbubul Syeed, and Mohammad Faisal Uddin. 2022. "Lightweight and Parameter-Optimized Real-Time Food Calorie Estimation from Images Using CNN-Based Approach" Applied Sciences, MDPI 12, no. 19: 9733. https://doi.org/10.3390/app12199733   [Rank: Q2     IF: 2.838]


Hossain, M.S.; Raihan, M.E.; Hossain, M.S.; Syeed, M.M.M.; Rashid, H.; Reza, M.S. Aedes Larva Detection Using Ensemble Learning to Prevent Dengue Endemic. BioMedInformatics, MDPI 2022, 2, 405-423. https://doi.org/10.3390/biomedinformatics2030026


Syeed M.M., Razib Hayat Khan, Jonayet Miah, Agile Fitness of Software Companies in Bangladesh- An Empirical Investigation.  (IJACSA) International Journal of Advanced Computer Science and Applications, Vol. 12, No. 2, 2021. [Rank: Q3     IF: 1.09]


Syeed M.M., Md. Asiful Islam, Kaniz Fatema, Precision Agriculture in Bangladesh: Need and Opportunities. International Journal of Advanced Science and Technology (IJAST). Vol. 29, No. 04, 2020, pp.6782-6800 [SCOPUS Indexed].


Kaniz Fatema, Syeed M.M., Razib Hayat, Comprehending relationship between Contribution and Career development in OSS Ecosystem, International Journal of Advanced Trends in Computer Science and Engineering (IJATCSE) Vol. 9 No 3. Pp. 3000-3009, 2020. [SCOPUS Indexed].


Nasrin Islam, Syeed M.M., Kaniz Fatema, An Empirical Investigation on Quality Assurance Practices in Software Industries- Bangladesh Perspective.   International Journal of Software Engineering and Computer Systems, Vol.6, ISSUE 2, pages 52 – 61, 2020.

Kaniz Fatema, Syeed M.M., M. Saef Ullah Miah, Demography of Startup Software Companies: An Empirical Investigation on the Success and Failure, International Journal of Computer Applications (IJCA), vol 176, no. 29, pp. 1-8. 2020. [EBSCO indexed].


K. Fatema and Syeed M.M, A Privacy Protected Platform to Aggrandize Micro-Business, Journal of Computer Science, Science Publications, vol. 15, no.11, pp. 1595-1606. 2019. [Rank: Q4.  IF: .94]


Syeed, M.M., Hammouda, I., Tarja, S., Prediction Models and Techniques in Open Source Software Projects, International Journal of Open Source Software and Processes (IJOSSP), IGI Global, Accepted in September 2014. [Rank: Q4     IF: 1.17]


Syeed, M.M., Hammouda, I., Socio-Technical Dependencies in Forked OSS Projects: Revealing Evidence from BSD Family, Journal of Software, Academy Publisher, Accepted in May 2014. [SCOPUS Indexed].


Syeed, M.M., Hammouda, I., Tarja, S., The Evolution of Open Source Software Projects: a systematic literature review, Journal of Software, Vol 8, No 11, Pages 2815-2829, Publisher: Academy Publisher, Nov 2013. [SCOPUS Indexed].


Syeed, M.M., Altonen, T., Hammouda, I., Tarja, S., Tool Assisted Analysis of Open Source Projects: A Multi-facet Challenge, International Journal of Open Source Software and Processes (IJOSSP), Vol: 3 Issue: 2, Pages 43-78, Publisher: IGI Global, 2011. [Rank: Q4     IF: 1.17]


Demography of Open Source Software Prediction models and techniques, published in Optimizing Contemporary Application and Processes in Open Source Software, IGI Global book, February 2018.


Introduction to Cloud Computing Technologies, Developing Cloud Software: Algorithms, Applications, and Tools, TUCS General Publication, TUCS, 2013.

Ashifur Rahman, Md. Shakhawat Hossain, M M Mahbubul Syeed, Kaniz Fatema, Md Faisal Uddin, Razib Hayat Khan, Mahady Hasan, Forecasting Surface Water Qulaity Using Spatiotemporal Multi-Head Attention-Based LSTM Model, 5th Euro-Mediterranean Conference for Environmental Integration (EMCEI-2023), ITALY (ACCEPTED) [Scopus Indexed, Springer]
	
Razib Hayat Khan; Rakib Ul Haque; M M Mahbubul Syeed and Mohammad Faisal Uddin. Utilization of Data Fedaration for Ensuring Interoperability in Mobile Financial Services. Proc. of The Seventh Edition of the World Conference on Smart Trends in Systems, Security and Sustainability (WorldS4), Springer LNNS series, August 21 - 24, 2023, London, UK. [Scopus Indexed, Springer]

M M Mahbubul Syeed, Md. Rajaul Karim, Md. Shakhawat Hossain, Kaniz Fatema, Md Faisal Uddin, Razib Hayat Khan, An IoT Intensive AI-integrated System for Optimized Surface Water Quality Profiling, IEEE 20th International Joint Conference on Computer Science and Software Engineering, Naresuan University, Phitsanulok, THAILAND, 28th June, 2023. [Scopus, IEEE]

Md. Shakhawat Hossain, Mahmudur Rahman, M M Mahbubul Syeed, Ummae Hamida Hannan, Md Faisal Uddin, Sahria Bakar Mumu, CaViT: Early Stage Dental Caries Detection from Smartphone-image using Vision Transformer, IEEE 4th International Conference on Artificial Intelligence, Robotics and Control (AIRC 2023), Cairo, Egypt, 5th May, 2023. [Scopus, IEEE]

shakhawat Hossain, Umme Sadia Salsabil, M M Mahbubul Syeed, Mahmudur Rahman, Kaniz Fatema, Md Faisal Uddin, SmartPoultry: Early Detection of Poultry Disease from Smartphone Captured Fecal Image, IEEE 20th International Joint Conference on Computer Science and Software Engineering, Naresuan University, Phitsanulok, THAILAND, 28th June, 2023. [Scopus, IEEE]

Razib Hayat Khan; ASM Shihavuddin; M M Mahbubul Syeed; Mohammad Faisal Uddin and Rakib Ul Haque. Improved Fake News Detection Method based on Deep Learning and Comparative Analysis with other Machine Learning approaches, Proc. of the 8th International Conference on Engineering and Emerging Technologies (ICEET), 27- 28 October 2022, Kuala Lumpur, Malaysia.

Sakib Ahmed, Sajib Hossain, Nazmul Hoque, Mahbubul Syeed, Saaduzzaman, Hasan Maruf, ASM Shihavuddin,  MRI Based Automated Detection of Brain Tumor using sequence of DWT, PCA, SVM, and PNN in Sequence. MIET, 2022. Lecture Notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering (LNICST), Volume 490, pp 267-279, Springer, 2023, http://dx.doi.org/10.1007/978-3-031-34619-4_22.


M Caspersen, Md. Sayed Tanveer, ASM Shihavuddin, Mahbubul Syeed, Md. Hasan Maruf, A Amin, Md Faisal Uddin, Cascaded DNNs for detecting the position and orientation of Left Ventricle from 3D CT Scans, 2022 IEEE 14th Image, Video, and Multidimensional Signal Processing Workshop (IVMSP 2022), Greece.


Mahbubul Syeed, ASM Shihavuddin,  Md Faisal Uddin, Mahady Hasan, Arifa Rahman, Impact study of data-driven automated system for maintaining Equality in Outcome Based Education, 6th International Conference on Equity and Inclusion in Education 19-21 May 2022, Bangladesh.


Arifa Rahman, ASM Shihavuddin,  Muhammad Hafiz Sikder, Mahbubul Syeed, Impact Study of Online Assessment Methods Facilitating Blended Learning towards Inclusion and Equity, 6th International Conference on Equity and Inclusion in Education 19-21 May 2022, Bangladesh.


Asiful Islam, Razib Hayat Khan and Syeed M.M., A Smart and Integrated Surface Water Monitor System Architecture: Bangladesh Perspective, International Conference on Computing Advancements, 2020, ACM.


Syeed, M.M., Hammouda I., Lindman, J., Measuring Perceived Trust in Open Source Software Communities, Proceedings of 13th. International Conference of Open Source Systems (OSS), Springer, 2017.


R. E. Guinness, H. Kuusniemi, J. Vallet, T. Sarjakoski, J. Oksanen, M. Islam, Syeed M.M., H-M. Halkosaari, P. Kettunen, M. Laakso, M. Rönneberg,  MyGeoTrust: A platform for trusted crowdsourced geospatial data,  ION GNSS+, The institute of Navigation, Florida, USA 2015.


Syeed, M.M., Alexander Lokman, Imed Hammouda, Tommi Mikkonen, Pluggable Systems as Architectural Pattern: An Ecosystemability Perspective, 7th Workshop on Software Ecosystems (IWSECO), ACM, 2015.


Syeed, M.M., Hammouda I., Who Contributes to What? Exploring Hidden Relationships Between FLOSS Projects, Proceedings of 10th. IFIP International Conference of Open Source Systems (OSS), Springer, 2014.


Syeed, M.M., Hansen K.M., Hammouda I., Konstantinos M., Socio-Technical congruence in the Ruby Ecosystem, in 10th OPENSYM conference, ACM, 2014.


Syeed, M.M., Hammouda, I., Socio-Technical congruence in OSS Projects: Exploring Conway’s law in FreeBSD OSS evolution, 9th International Conference of Open Source Systems (OSS), Springer, 2013.

Syeed, M.M., Hammouda I, Exploring Socio-Technical Dependencies in Open Source Software Projects - Towards an Automated Data-driven Approach, Academic Mindtrek Conference, ACM, 2013.


Syeed, M.M., Binoculars: Comprehending Open Source Projects through graphs, Proceedings of 8th. IFIP International Conference of Open Source Systems (OSS), Springer, 2012.

Syeed, M.M., Comprehending co-evolution of OSS projects: Analytical methods and tool support, Proceedings of 8th. IFIP International Conference of Open Source System (OSS), Springer, DC, 2012.


Syeed, M.M., Siddiqui, F.H., Al-Mamun, A.S.A., Tanbeer, S.K., Mottalib, M.A, Bengali Character recognition using Bidirectional Associative Memories (BAM) Neural Network, Proceedings of 5th ICCIT, 2002, pp.247-251.


Syeed, M.M., Fatema, K., Scheming On-Line adaptation of a Prototype-Based Classifier for Handwritten characters, Proceedings of 8th ICCIT, 2005, pp. 690-693.

Siddiqui, F.H., Syeed, M.M., Fatema, K., A Proposed Architecture for Efficient Implementation of Large-scale Hopfield Neural Network using CDMA Communication Technology, Proceedings of 8th ICCIT, 2005, pp. 580-584.


Syeed, M.M., Fatema, K., An Enhanced Approach of Face Recognition using Moving Window Classifier, Proceedings of 8th ICCIT, 2005, pp. 634-639.

Syeed, M.M., Siddiqui, F.H., Fatema, K., A combinational approach of neural and fuzzy logic to recognize handwritten Bengali character, Proceedings of 7th ICCIT, 2004, pp. 606-609.

Syeed, M.M., Fatema, K., An enhanced system for face recognition using Hidden Markov Models and Wavelets, Proceedings of 7th ICCIT, 2004, pp. 575-579.
F. Faisal, B. Mondal, M. F. Monir, T. Ahmed, and M. Z. Alam

 , "WNetMon: An ML approach for real-time DoS attack detection in wireless networks", Proc. IEEE Int. Telecommunication Networks and Applications Conf. (ITNAC), Sydney, NSW, Australia, Oct. 2024, pp. 1-7. [Indexed by Scopus and DBLP] , 2024
K. Alam, M. H. Bhuiyan, I. U. Haque, M. F. Monir, and T. Ahmed

 , "Enhancing Stock Market Prediction: A Robust LSTM-DNN Model Analysis on 26 Real-Life Datasets", IEEE Access, Vol. 12, Jul. 2024, pp. 122757-122768. , 2024
M. F. Monir, M. J. Hossain, M. Barkatullah, M. M. Hoque, Z. Hassan, and T. Ahmed

 , "Enhanced vehicle detection by optimized image compression in NextG wireless network autonomous vehicles system", Proc. IEEE Vehicular Technology Conference (VTC2024-Fall), Washington, DC, USA, Oct. 2024, pp. 1-5. [Indexed by Scopus and DBLP] , 2024
I. A. Toke, M. F. Monir, M. Z. Hassan, and T. Ahmed

 , "Blockchain-enabled rental system for agricultural asset management using hyperledger fabric", Proc. IEEE Vehicular Technology Conference (VTC2024-Fall), Washington, DC, USA, Oct. 2024, pp. 1-5. [Indexed by Scopus and DBLP] , 2024
M. F. Monir, A. Fawad Hasan, M. M. Hoque, T. Ahmed, and F. Granelli

 , "Benchmarking network functionality: Performance evaluation of SDN controllers on different network functions", Proc. IEEE Vehicular Technology Conference (VTC2024-Fall), Washington, DC, USA, Oct. 2024, pp. 1-5. [Indexed by Scopus and DBLP] , 2024
M. O. Azhar, F. Jabin Oyshee, M. F. Monir, R. Hayat Khan, T. Ahmed, and K. Alam

 , "Comparative analysis of machine learning models: Ransomware severity prediction using MITRE cyber analytics repository", Proc. IEEE Vehicular Technology Conference (IEEE VTC2024-Fall), Washington, DC, USA, Oct. 2024, pp. 1-5. [Indexed by Scopus and DBLP] , 2024
S. Rahman, M. F. Monir, M. Z. Alam, and T. Ahmed

 , "Optimizing signal transmission in underground WSN: Addressing multipath fading with Random Walk Kalman Filter and Diffusion LMS", Proc. IEEE Vehicular Technology Conference (IEEE VTC-Fall), Washington, DC, USA, Oct. 2024, pp. 1-6. [Indexed by Scopus and DBLP] , 2024
N. Khatun, N. Halder, S. Rashid, A. Islam, M. Z. Alam and T. Ahmed

 , "Performance evaluation of machine learning and deep learning models for predicting type-2 diabetes on balanced and imbalanced data", Proc. Advances in Science and Engineering Technology International Conferences (ASET), Abu Dhabi, United Arab Emirates, Jun. 2024, pp. 1--9. [Indexed by Scopus] , 2024
I. A. Toke, M. F. Monir, and T. Ahmed

 , "Blockchain in agriculture: A scalable solution for crop quality assessment and data integrity", Proc. IEEE Int. Black Sea Conf. on Communications and Networking (IEEE BLACKSEACOM), Tbilisi, Georgia, Jun. 2024, pp. 205-210. [Indexed by Scopus and DBLP] , 2024
A. Saha, L. Ali, R. Rahman, M. F. Monir and T. Ahmed

 , "Exploring Federated Learning: The framework, applications, security & privacy", Proc. IEEE Int. Black Sea Conf. on Communications and Networking (IEEE BLACKSEACOM), Tbilisi, Georgia, Jun. 2024, pp. 272-275. [Indexed by Scopus and DBLP] , 2024
N. Masrur, N. Halder, S. Rashid, J. H. Setu, A. Islam and T. Ahmed

 , "Performance analysis of ensemble and DNN models for decoding mental stress utilizing ECG-based wearable data fusion", Proc. IEEE Int. Black Sea Conf. on Communications and Networking (IEEE BLACKSEACOM), Tbilisi, Georgia, Jun. 2024, pp. 276-279. [Indexed by Scopus and DBLP] , 2024
S. Saheel, A. Alvi, A. R. Ani, T. Ahmed, and M. F. Uddin

 , "Semi-supervised, Neural Network based approaches to face mask and anomaly detection in surveillance networks", Elsevier Journal of Network and Computer Applications (JNCA), Vol 222, Article 103786, Feb. 2024. [Indexed by ISI, Scopus and DBLP] , 2024
A. Rahman, F. Jahura, M. J. Hasan, A. Hossain, M. F. Monir, and T. Ahmed

 , "Intelligent road safety: IoT-enabled drunk driving and accident detection system", Proc. IEEE Int. Conf. on Smart Technologies (IEEE EUROCON), Turin, Italy, Jul. 2023, pp. 48-53. [Indexed by Scopus and DBLP] , 2023
A. R. Ani, S. Saheel, T. Ahmed, and M. F. Uddin

 , "Neural network based unsupervised face and mask detection in surveillance networks", Proc. IEEE Int. Conf. on Computing, Networking and Communications (ICNC), Honolulu, HI, USA, Feb. 2023, pp 30-34. [Indexed by Scopus and DBLP] , 2023
B. Mondal, F. Faisal, Z. T. Towshi, M. F. Monir, and T. Ahmed

 , "A gradient boosted ML approach to feature selection for wireless intrusion detection", Proc. IEEE Vehicular Technology Conf. (IEEE VTC2023-Spring), Florence, Italy, Jun. 2023, pp. 1-5 [Indexed by Scopus and DBLP] , 2023
J. Bhowmik, M. F. Monir, S. A. A. Naiyem, M. A. Rahman, B. Bhowmik, and T. Ahmed

 , "Design and development of a low-cost automated parking system for developing countries", Proc. IEEE Int. Conf. on Smart Technologies (IEEE EUROCON), Turin, Italy, Jul. 2023, pp. 30-35. [Indexed by Scopus and DBLP] , 2023
M. H. Bhuiyan, R. K. Ahad, A. J. Haque, M. F. Monir, and T. Ahmed

 , "An affordable and effective IoT-based home automation and security system for everyone", Proc. IEEE Int. Conf. on Smart Technologies (IEEE EUROCON), Turin, Italy, Jul. 2023, pp. 325-330. [Indexed by Scopus and DBLP] , 2023
M. J. Hossain, M. Barkatullah, M. F. Monir, and T. Ahmed

 , "Repercussion of image compression on satellite image classification using deep learning models", Proc. IEEE Vehicular Technology Conf. (IEEE VTC2023-Fall), Hong Kong, China, Oct. 2023, pp. 1-5. [Indexed by Scopus and DBLP] , 2023
S. Rahman, M. Z. Alam, A. Islam, M. T. Habib, E. Ahmed, M. Hasan, and T. Ahmed

 , "Low-cost relay selection in multihop cooperative networks", Journal of King Saud University – Computer and Information Sciences, Vol. 35, Article 101760, Oct. 2023 , 2023
I. A. Toke, M. M. F. Rahman, M. F. Monir, T. Ahmed, and K. A. Rabbani

 , "IoT driven smart greenhouse: A cost-effective and user-centric automation solution for agriculture", Proc. IEEE Int. Conf. on Advanced Networks and Telecommunications Systems (IEEE ANTS), Jaipur, India, Dec. 2023, pp. 1-6. [Indexed by Scopus and DBLP] , 2023
M. A. Hossain, F. Jahura, M. A. Rahman, and T. Ahmed

 , "IoT-based drunk driving detection and engine locking system with real-time location in app", Proc. IEEE Region 10 Conf. (IEEE TENCON), Hong Kong, China, Nov. 2022, pp. 1-5. [Indexed by Scopus and DBLP] , 2022
R. A. Urmee, N. S. Prome, and T. Ahmed

 , "Hand gesture-based home automation system", Proc. IEEE Region 10 Conf. (IEEE TENCON), Hong Kong, China, Nov. 2022, pp. 1-5. [Indexed by Scopus and DBLP] , 2022
A. Alvi, T. Ahmed, and M. F. Uddin

 , "Comparative study of traditional techniques for unsupervised autonomous intruder detection", Proc. Springer Int. Conf. on Advanced Information Networking and Applications (AINA), Toronto, ON, Canada, May 2021, pp. 519-530. [Indexed by Scopus and DBLP] , 2021
S. Daneshgadeh, T. Kemmerich, T. Ahmed, and N. Baykal

 , "Online DDoS attack detection using Mahalanobis distance and kernel-based learning algorithm", Elsevier Journal of Network Computer Applications (JNCA), Vol. 168, Paper 102756, Oct. 2020. [Indexed by ISI, Scopus and DBLP] , 2020
M. S. A. Khan, T. Ahmed, and M. F. Uddin,

 , "Multi-robot search algorithm using timed random switching of exploration approaches", Proc. IEEE Region 10 Symposium (IEEE TENSYMP), Dhaka, Bangladesh, Jun. 2020, pp. 1–4. [Indexed by Scopus] , 2020
S. Daneshgadeh, T. Ahmed, and A.-S. K. Pathan

 , "The Kernel-Based Online Anomaly Detection Algorithm: Detailed Derivation and Development", Security Analytics for the Internet of Everything, M. Ahmed, A. Ullah and A.-S. K. Pathan Eds. USA: CRC Press, Feb. 2020, pp. 155-192. , 2020
S. Daneshgadeh, T. Kemmerich, T. Ahmed, and N. Baykal

 , "An empirical investigation of DDoS and Flash Event detection using Shannon Entropy, KOAD and SVM combined", Proc. IEEE Int. Conf. on Computing, Networking and Communications (ICNC), Honolulu, HI, USA, Feb. 1019, pp.658-662. [Indexed by Scopus and DBLP] , 2019
S. Daneshgadeh, T. Ahmed, T. Kemmerich, and N. Baykal

 , "Detection of DDoS attacks and Flash Events using Shannon Entropy, KOAD and Mahalanobis Distance", Proc. IEEE Conf. on Innovation in Clouds, Internet and Networks and Workshops (ICIN), Paris, France, Feb. 2019, pp. 222-229. [Indexed by Scopus and DBLP] , 2019
H. Islam and T. Ahmed

 , "Anomaly clustering based on correspondence analysis", Proc. IEEE Int. Conf. on Advanced Information Networking and Applications (IEEE AINA), Krakow, Poland, May 2018, pp. 1019-1025. [Indexed by Scopus and DBLP] , 2018
M. S. A. Khan, M. S. Hasan, and T. Ahmed

 , "A new multi-robot search algorithm using Probabilistic Finite State Machine and Lennard-Jones potential function", Proc. IEEE Int. Conf. on Robotics and Biomimetics (IEEE ROBIO), Kuala Lumpur, Malaysia, Dec. 2018, pp. 850-855. [Indexed by Scopus and DBLP] , 2018
S. Daneshgadeh, T. Kemmerich, T. Ahmed, and N. Baykal

 , "A hybrid approach to detect DDoS attacks using KOAD and the Mahalanobis distance", Proc. IEEE Int. Symposium on Network Computing and Applications (IEEE NCA), Cambridge, MA, USA, Nov. 2018, pp. 341–345. [Indexed by Scopus and DBLP] , 2018
M. S. A. Khan, S. S. Chowdhury, N. R. Niloy, F. T. Z. Aurin, and T. Ahmed

 , "Sonar-based SLAM using occupancy grid mapping and dead reckoning", Proc. IEEE Region 10 Conf. (IEEE TENCON), Jeju, Republic of Korea, Oct. 2018, pp. 1–6. [Indexed by Scopus] , 2018
M. Lushan, M. Bhattacharjee, T. Ahmed, M. A. Rahman, and S. Ahmed

 , "Supervising vehicle using pattern recognition: detecting unusual behavior using machine learning algorithms", Proc. IEEE Region 10 Symposium (IEEE TENSYMP), Sydney, NSW, Australia, Jul. 2018, pp. 1–5. [Indexed by Scopus] , 2018
 A. Anika, K. Karim, R. Muntaha, F. Shahrear, S. Ahmed, and T. Ahmed

 , "Multi image retrieval for kernel-based automated intruder detection", Proc. IEEE Region 10 Symposium (IEEE TENSYMP), Kochi, India, Jul. 2017, pp. 1–5. [Indexed by Scopus] , 2017
T. Ahmed

 , "Kernel-based online anomaly detection and its applications to video analysis", Erasmus+ Visiting Scholar seminar series, Department of Electrical and Electronics Engineering, Middle East Technical University, Ankara, Turkey, Apr. 2017. , 2017 , (Link)
T. Ahmed, S. Ahmed, and F. E. Chowdhury

 , "Taking Meredith out of Grey's Anatomy: Automating hospital ICU emergency signaling", Proc. IEEE Int. Conf. on Acoustics, Speech and Signal Processing (IEEE ICASSP), Shanghai, China, Mar. 2016, pp. 1886–1890. [Indexed by Scopus and DBLP] , 2016
N. Ahmadullah, S. Islam, and T. Ahmed

 , "RouteFinder: Real-time optimum vehicle routing using mobile phone network", Proc. IEEE Region 10 Conf. (IEEE TENCON), Macau, China, Nov. 2015, pp. 1–7. [Indexed by Scopus] , 2015
T. Ahmed, A.-S. K. Pathan, and S. Ahmed

 , "Learning algorithms for anomaly detection from images", IGI Global Int. J. of System Dynamics Applications (IJSDA), vol. 4, issue 3, Jul. 2015, pp. 43–69. [Indexed by ACM Digital Library and DBLP] , 2015
T. Ahmed, A.-S. K. Pathan, and S. Ahmed

 , "Adaptive algorithms for automated intruder detection in surveillance networks", Proc. IEEE Int. Conf. on Advances in Computing, Communications and Informatics (ICACCI), Delhi, India, Sep. 2014, pp. 2775–2780. [Indexed by Scopus and DBLP] , 2014
T. Ahmed, S. Ahmed, and A.-S. K. Pathan

 , "Automated surveillance in distributed, visual networks: An empirical comparison of recent algorithms", SERSC Int. J. of Control and Automation, vol. 7, issue 3, Mar. 2014, pp. 389–400. [Indexed by Scopus] , 2014
A.-S. K. Pathan and T. Ahmed

 , "An innovative approach of blending security features in energy-efficient routing for a crowded network of wireless sensors", The State of the Art in Intrusion Prevention and Detection, A.-S. K. Pathan Ed. USA: CRC Press, Jan. 2014, pp. 449-472. , 2014
T. Ahmed, X. Wei, S. Ahmed, and A.-S. K. Pathan

 , "Efficient and effective automated surveillance agents using kernel tricks", SIMULATION: Trans. of The Society for Modeling and Simulation Int., vol. 89, issue 5, May 2013, pp. 562–577. [Indexed by ISI, Scopus, ACM Digital Library and DBLP] , 2013
T. Ahmed, X. Wei, S. Ahmed, and A.-S. K. Pathan

 , "Automated visual surveillance using kernel tricks", poster, ENS/INRIA Computer Vision and Machine Learning Summer School (CVML), École Normale Supérieure (ENS), Paris, France, Jul. 2013. , 2013
X. Wei, J. Fan, M. Chen, T. Ahmed, and A.-S. K. Pathan

 , "SMART: A subspace based malicious peers detection algorithm for P2P systems", Int. J. of Communication Networks and Information Security (IJCNIS), vol. 5, no. 1, Apr. 2013, pp. 1–9. [Indexed by Scopus] , 2013
T. Ahmed

 , "Efficient and Effective Automatic Surveillance Approaches", Ph.D. thesis, International Islamic University Malaysia (IIUM), Kuala Lumpur, Malaysia, Sep. 2013. Advisor: A.-S. K. Pathan, Department of Computer Science. External Examiner: J. Abawajy, School of Information Technology, Deakin University, Melbourne, Vic, Australia. , 2013
T. Ahmed and A.-S. K. Pathan

 , "Automated surveillance approaches", abstract, poster and presentation, International Islamic University Malaysia (IIUM) Postgraduate Students Colloquium, Kuala Lumpur, Malaysia, Oct. 2013. , 2013
T. Ahmed, S. Ahmed, and A.-S. K. Pathan

 , "Automated surveillance in distributed visual networks: A comparative study", Int. Workshop on Mobile and Wireless (WMobileWireless), Jeju, Republic of Korea. Advanced Science and Technology Letters, vol. 42 (Mobile and Wireless 2013), Dec. 2013, pp. 1-4. , 2013
T. Ahmed and A.-S. K. Pathan

 , "An effective automated surveillance system", abstract, paper, poster and presentation, International Islamic University Malaysia (IIUM) Postgraduate Students Colloquium, Kuala Lumpur, Malaysia, Dec. 2012. , 2012
T. Ahmed, X. Wei, S. Ahmed, and A.-S. K. Pathan

 , "Automated intruder detection from image sequences using minimum volume sets", Int. J. of Communication Networks and Information Security (IJCNIS), vol. 4, no. 1, Apr. 2012, pp. 11–17. [Indexed by Scopus] , 2012
T. Ahmed and A.-S. K. Pathan

 , "Towards automated surveillance systems", abstract, poster and presentation, International Islamic University Malaysia (IIUM) Postgraduate Students Colloquium, Kuala Lumpur, Malaysia, Feb. 2012. , 2012
X. Wei, T. Ahmed, M. Chen, and A.-S. K. Pathan

 , "PeerMate: A malicious peer detection algorithm for P2P Systems based on MSPCA", Proc. IEEE Int. Conf. on Computing, Networking and Communications (ICNC), Lahaina, HI, USA, Feb. 2012, pp. 815-819. [Indexed by Scopus and DBLP] , 2012
T. Ahmed, X. Wei, S. Ahmed, and A.-S. K. Pathan

 , "Intruder detection in camera networks using the one-class neighbor machine", Proc. American Telecommunications Systems Management Association (ATSMA) Networking and Electronic Commerce Research Conf., Riva del Garda, Italy, Oct. 2011, pp. 115-118. , 2011
T. Ahmed

 , "Online anomaly detection using adaptive, learning algorithms", poster and presentation, Traffic Monitoring and Analysis (TMA) PhD School, University of Naples Federico II , Naples, Italy, Jun. 2011. [Won organizers’ travel grant award] , 2011
T. Ahmed and R. Rahman

 , "Survey of anomaly detection algorithms: toward self-learning networks", Security of Self-Organizing Networks: MANET, WSN, WMN, VANET, A.-S. K. Pathan Ed. USA: CRC Press, Oct. 2010, pp. 65-90. , 2010
T. Ahmed

 , "Flow vector prediction using EM algorithms", Proc. IEEE Int. Conf. on Communications (IEEE ICC), Cape Town, South Africa, May 2010, pp. 1-6. [Indexed by Scopus and DBLP] , 2010
T. Ahmed, Sabrina Ahmed, Supriyo Ahmed, and M. Motiwala

 , "Real-time intruder detection in surveillance systems using adaptive kernel methods", Proc. IEEE Int. Conf. on Communications (IEEE ICC), Cape Town, South Africa, May 2010, pp. 1-5. [Indexed by Scopus and DBLP] , 2010
T. Ahmed

 , "Flow vector prediction in large IP networks", Proc. IEEE Int. Conf. on Advanced Information Networking and Applications (IEEE AINA), Perth, WA, Australia, Apr. 2010, pp. 342-349. [Indexed by Scopus and DBLP] , 2010
T. Ahmed

 , "Online anomaly detection using KDE", Proc. IEEE Global Communications Conf. (IEEE GLOBECOM), Honolulu, HI, USA, Dec. 2009, pp. 1-8. [Indexed by Scopus and DBLP] , 2009
R. Rahman, T. Ahmed, A. Alam, and K. Kobra

 , "Mobile phone and 3G technology: opening possibilities", cover story, CNEWS, May 2009, pp. 19-25. [In Bengali] , 2009 , (Link)
M. Coates, T. Ahmed, Y. Pointurier, N. Saberi, and F. Thouin

 , "AAPN research summary: monitoring, control and VoD", presentation, Agile All-Photonic Networks (AAPN) Annual Research Review, Ottawa, ON, Canada, Jun. 2007. , 2007
T. Ahmed, M. Coates, and A. Lakhina

 , "Multivariate online anomaly detection using kernel recursive least squares", Proc. IEEE Conf. on Computer Communications (IEEE INFOCOM), Anchorage, AK, USA, May 2007, pp. 625-633. [Indexed by Scopus and DBLP] , 2007
T. Ahmed, B. Oreshkin, and M. Coates

 , "Traffic incident detection from road camera networks", abstract and poster, Centre for Advanced Systems and Technologies in Communications (SYTACom) Research Workshop, Quebec City, QC, Canada, May 2007. [Nominated for award] , 2007
T. Ahmed and M. Coates

 , "Machine learning algorithms for anomaly detection in optical networks", abstract and poster, Workshop on Optimization of Optical Networks (OON), Montreal, QC, Canada, May 2007. , 2007
T. Ahmed, B. Oreshkin, and M. Coates

 , "Machine learning approaches to network anomaly detection", Proc. ACM/USENIX Workshop on Tackling Computer Systems Problems with Machine Learning Techniques (SysML), Cambridge, MA, USA, Apr. 2007. [Selected for reading list of “263-3503-00: Advanced Topics in Cyber-physical Systems,” Dept of Computer Science, ETH Zurich, Autumn 2011 (https://www.vs.inf.ethz.ch/edu/HS2011/CPS/), indexed by ACM Digital Library] , 2007
T. Ahmed and M. Coates

 , "Machine learning algorithms for anomaly detection in agile all-photonic networks", abstract and poster, Agile All-Photonic Networks (AAPN) Annual Research Review, Ottawa, ON, Canada, Jun. 2007. [Won runner-up award] , 2007
M. Coates, T. Ahmed, N. Saberi, and F. Thouin

 , "AAPN research summary", presentation, Agile All-Photonic Networks (AAPN) Annual Research Review, Ottawa, ON, Canada, Jun. 2006. , 2006
T. Ahmed and M. Coates

 , "Online anomaly detection for optical networks", abstract and poster, Workshop on Optimization of Optical Networks (OON), Montreal, QC, Canada, Apr. 2006. , 2006
T. Ahmed and M. Coates

 , "Multivariate online anomaly detection using kernel recursive least squares", technical report, Department of Electrical and Computer Engineering, McGill University, Montreal, QC, Canada, Aug. 2006. , 2006 , (Link)
T. Ahmed and M. Coates

 , "Online anomaly detection for optical networks", abstract and poster, Agile All-Photonic Networks (AAPN) Annual Research Review, Ottawa, ON, Canada, Jun. 2006., [Nominated for award] , 2006
T. Ahmed, N. Saberi, and M. Coates

 , "Time-slot reservation in all-photonic networks based on flow prediction", abstract and presentation, Workshop on Optimization of Optical Networks (OON), Montreal, QC, Canada, Apr. 2005. , 2005
M. Coates, N. Saberi, T. Ahmed, F. Thouin, and G. Ing

 , "AAPN network monitoring and scheduling", presentation, Agile All-Photonic Networks (AAPN) Annual Research Review, Ottawa, ON, Canada, Jun. 2005. , 2005
T. Ahmed and M. Coates

 , "Flow vector prediction", technical report, Department of Electrical and Computer Engineering, McGill University, Montreal, QC, Canada, Sep. 2005. , 2005 , (Link)
T. Ahmed and M. Coates

 , "Predicting flow rate densities", abstract and poster, Agile All-Photonic Networks (AAPN) Annual Research Review, Ottawa, ON, Canada, Jun. 2005. , 2005
T. Ahmed

 , "Low temperature (8K) spectroscopy of the Uranyl (UO_{2}^{2+}) ion in the mineral autunite", Bachelor’s thesis, Middlebury College, Middlebury, VT, USA, May 1999. Advisors: J. Dunham and R. Prigo, Department of Physics. , 1999 , (Link)
T. Ahmed

 , "A robotic tadpole: design and construction", report, presentation and demonstration, U.S. National Science Foundation (NSF) Summer Undergraduate Fellowship in Sensor Technologies (SUNFEST), University of Pennsylvania, Philadelphia, PA, USA, Aug. 1998. Advisor: J. Ostrowski, General Robotics, Automation, Sensing and Perception (GRASP) Laboratory. , 1998 , (Link)
T Zia, A Datta, MR Noor, MA Amin, AA Ali, A K M M Rahman, "A Study into the Limitations of CNN Recognition on Isolated Bengali Compound Characters". Presented at International Conference on Data Mining and Knowledge Discovery (ICDMKD-2023, China), published in Telematique, Vol22, Issue01, pp 2508-2523, Oct 2023
Qianwei Cheng*, Moinul Zaber*, A K M M Rahman*, Haoran Zhang, Zhiling Guo, Akiko Okabe, Ryosuke Shibasaki, "Understanding the urban environment of developing countries from satellite images", MDPI Sustainability, (Impact factor: 3.251,  Scimago Journal  Rank: Q1), 2022; *Equal Contribution
A K M M Rahman, Moinul Zaber, Qianwei Cheng,  Abu Bakar Siddik Nayem, Anis Sarker, Ovi Paul, and Ryosuke Shibasaki, "Applying State-of-the-Art Deep-Learning Methods to Classify Urban Cities of the Developing World",  Special Issue: Urban Information Sensing for Sustainable Development, MDPI Sensors (Impact factor: 3.57,  Scimago Journal  Rank: Q1 ), 2021
A K M M. Rahman, ASM. I. Anam, and M. Yeasin, "Robust Modeling of Epistemic Mental States”, Special Issue: Socio-Affective Technology, Journal of Multimedia Tools and Applications (Impact factor: 2.10,  Scimago Journal  Rank: Q1 ), 2020.
Arif, M. Zaber, Amin A. Ali, M. Ashraful Amin, and A K M M Rahman, "Visual Attention Based Comparative Study on Disaster Detection from Social Media Images",  Innovations in Systems and Software Engineering,  (Impact factor: 0.94,  Scimago Journal  Rank: Q3 ), 2020.  
A K M M. Rahman, ASM. I. Anam, and M. Yeasin, “ A Unified Framework for Dividing and Predicting a Large Set of Action Units”, IEEE Transaction of Affective Computing (Impact factor: 6.29, Scimago Journal  Rank: Q1), August, 2015.
A K M M. Rahman, ASM. I. Anam, and M. Yeasin, "EmoAssist: A Social Interaction Tool to assist the Visually Impaired in real world environment”, Journal of Multimedia Tools and Applications (Impact factor: 2.10, Scimago Journal  Rank: Q1),  2015. 
A K M M. Rahman, M. B. Khan, A. Bhuiyan, “Implication of Fuzzy Logic in Genetic Algorithm for Solving Mathematical Problems”, Journal of Science and Technology, Daffodil International University, Dhaka, 
   Book Chapter:

Abu Bakar Siddik Nayem, Anis Sarker, Ovi Paul, Amin Ali, Md. Ashraful, Amin, A K M M Rahman, "LULC Segmentation of RGB Satellite Image Using FCN-8", 3rd SLAAI-International Conference on Artificial Intelligence, Springer,  Srilanka, 2019 
Arif, Abdullah Omar, Sabah Ashraf, A K M M Rahman, Amin Ahsan Ali, M Ashraful Amin, “A Comparative Study on Disaster Detection from Social Media Images using Deep Learning",  Proceedings of the Global AI Congress (GAIC 2019),  Kolkata, India, 2019
Md Wahidul Hasan, Akil Hamid Chowdhury, Md Mehedi Hasan, Arup Ratan Datta, A K M M Rahman, M Ashraful Amin, “IoT Based Smart Application System to Prevent Sexual Harassment in Public Transport”, Book Chapter, AISC, Bangkok, Thailand, Springer, 2019
Dehan Noor, Md Fahim, A K M M Rahman, Amin Ahsan Ali, “TinyLLM Efficacy in Low-Resource Language: An Experiment on Bangla Text Classification Task”, 27th International Conference on Pattern Recognition (ICPR 2024), (Core Rank: B) 
Mir Sazzat Hossain, A K M M Rahman, Md. Ashraful Amin, Amin Ahsan Ali, "Lightweight Recurrent Neural Network for Image Super-resolution", IEEE International Conference on Image Processing (ICIP 2024), October 2024, Abu Dhabi, United Arab Emirates, (Core Rank: B) 
Fahim Ahmed, Md Fahim, Md Ashraful Amin, Amin Ahsan Ali, and A K M M Rahman, “Improving The Performance of Transformer-based Models Over Classical Baselines in Multiple Transliterated Languages”, 27th European Conference on Artificial Intelligence (ECAI 2024), October 2024, Spain, (Core Rank: A) 
Md Fahim, Amin Ahsan Ali, M Ashraful Amin, A K M M Rahman, "Contextual Bangla Neural Stemmer: Finding Contextualized RootWord Representations for BanglaWords", EMNLP 2023 Workshop BLP, Singapore
Nabilah Tabassum Oshin, Syed Mohaiminul Hoque, Md Fahim, Amin Ahsan Ali, M Ashraful Amin, A K M M Rahman, "BaTEClaCor: A Novel Dataset for Bangla Text Error Classification and Correction", EMNLP 2023 Workshop BLP, Singapore
Farhan Noor Dehan, Md Fahim, Amin Ahsan Ali, M Ashraful Amin, A K M M Rahman, "Investigating the Effectiveness of Graph-based Algorithm for Bangla Text Classification", EMNLP 2023 Workshop BLP, Singapore
Md Fahim, Dr. Amin Ahsan Ali, Md Ashraful Amin and A K M M Rahman,  "EDAL: Entropy based Dynamic Attention Loss for HateSpeech Classification",  The 37th Pacific Asia Conference on. Language, Information and Computation  PACLIC 2023), Hongkong, 2023 (Average acceptance rate: 28.7%)
Mir Sazzat Hossain, Sugandha Roy, K. M. B. Asad, Arshad Momen, Amin Ahsan Ali, M “Ashraful Amin, A K M M Rahman, “Morphological Classification of Radio Galaxies Using Semi-Supervised Group Equivariant CNNs”, International Neural Network Society Workshop on Deep Learning Innovations and Applications (INNS DLIA 2023) associated with IJCNN, Elsevier, 2023
Tahmid Alavi Ishmam, Amin Ahsan Ali, M Ashraful Amin, and  A K M M Rahman, "Automatic Detection of Natural Disaster Effect on Paddy Field from Satellite Images using Deep Learning Techniques", 8th International Conference on Control and Robotics Engineering (ICCRE 2023),  Niigata, Japan
Tonmoay Deb, Akib Sadmanee, Kishor Kumar Bhaumik, Amin Ahsan Ali, M Ashraful Amin, and  A K M M Rahman, “Variational Stacked Local Attention Networks for Diverse Video Captioning”, Winter Conference on Applications of Computer Vision (WACV 2022), Hawaii, USA, (Core Rank: A) 
Hasnain Hossain, Tahmid Bin Mahmud, A K M M Rahman, M Ashraful Amin, Amin Ahsan Ali, "Comparing recent Swarm Algorithms with Information Theoretic Filter criterion for Feature Selection", International Conference on Electrical, Computer and Energy Technologies (ICECET), 2021, IEEE, Capetown. South Africa
Shehzan Haider Chowdhury, Murshed Al Amin, A K M M Rahman, M Ashraful Amin, Amin Ahsan Ali, "Assessment of Rehabilitation Exercises from Depth Sensor Data", 24th International Conference on Computer and Information Technology (ICCIT), IEEE, 2021, Dhaka
F.F. Niloy, M.A. Amin, A.A. Ali,  and A K M M Rahman, "Attention toward Neighbors: A Context Aware Framework for High Resolution Image Segmentation", The 28th IEEE International Conference on Image Processing (IEEE - ICIP 2021), Anchorage, USA, (H Index: 52)
Amit Roy, Kashob Kumar Roy, Amin Ahsan Ali, M Ashraful Amin and A K M  Rahman,  "Unified Spatio-Temporal Modeling for Traffic Forecasting  using Graph Neural Network",  The International Joint Conference on Neural Network, 2021, (Core Rank: A)
Kashob Kumar Roy, Amit Roy, A K M M Rahman, M Ashraful Amin and Amin Ahsan Ali, "Structure-Aware Hierarchical Graph Pooling using Information Bottleneck",  The International Joint Conference on Neural Network, 2021, (Core Rank: A)
Kashob Kumar Roy, Amit Roy, A K M M Rahman, M Ashraful Amin and Amin Ahsan Ali, "Node Embedding using Mutual Information and Self-Supervision based Bi-level Aggregation",  The International Joint Conference on Neural Network, 2021, (Core Rank: A)
S. Mahmud, M.T.H. Tonmoy, A K M M  Rahman, M A. Amin,  and A.A. Ali,, "Hierarchical Self Attention Based Autoencoder for Open-Set Human Activity Recognition", 25th Pacific-Asia Conference on Knowledge Discovery and Data Mining25th Pacific-Asia Conference on Knowledge Discovery and Data Mining (Core Rank: A, acceptance rate: 20%)
Amit Roy, Kashob Roy, M A. Amin, A.A. Ali, and A K M M  Rahman, "SST-GNN: Simplified Spatio-temporal Traffic forecasting model using Graph Neural Network", 25th Pacific-Asia Conference on Knowledge Discovery and Data Mining25th Pacific-Asia Conference on Knowledge Discovery and Data Mining (Core Rank: A, acceptance rate: 20%)
F.F. Niloy, Arif, A.B.S. Nayem, A Sarker, O Paul, M.A. Amin, A.A. Ali, M.I. Zaber, and A K M M Rahman, “A Novel Disaster Image Data-set and Characteristics Analysis using Attention Model”, 25th International Conference on Pattern Recognition (ICPR 2020) (Core Rank: B, acceptance rate: 43.4%)
Md. Saif Hassan Onim, Aiman Rafeed Ehtesham, Amreen Anbar, A. K. M. Nazrul Islam and A K M M Rahman, "LULC classification by semantic segmentation of satellite images using FastFCN", 2nd International Conference on Advanced Information and Communication Technology (ICAICT), IEEE Xplore, Dhaka, 2020
Md. A. Pramanik, Md M. Rahman,  ASM I Anam, Amin A Ali, Md A Amin, and A K M M  Rahman, " Modeling Traffic Congestion in Developing Countries using Google Map Data", Future of Information and Communication Conference (FICC) 2021, Springer,  Vancouver, Canada, 2021
Qianwei Cheng, A K M M Rahman, Anis Sarker, Abu Bakar Siddik Nayem, Ovi Paul, Amin Ahsan Ali, M Ashraful Amin, Ryosuke Shibasaki, Moinul Zaber, "Deep-learning coupled with novel categorization method to classify the urban environment of the developing world", 2nd International Conference on Signal Processing and Machine Learning (SIGML 2021), Switzerland, 2021
S. Mahmud, M.T.H. Tonmoy, K.K. Bhaumik, A K M M  Rahman, M A. Amin, M. Shoyaib, A.H Khan and A.A. Ali, “Human Activity Recognition from Wearable Sensor Data using Self-Attention”, ECAI, Spain, 2020, (Core Rank: A, acceptance rate: 26.8%)
 

A K M M. Rahman, ASM. I. Anam, M. I. Tanveer, and M. Yeasin, “EmoAssist: A Real-time Social Interaction Tool to assist the Visually Impaired", In Proceedings of the 15th  International Conference on Human-Computer Interaction (HCII 2013), Las Vegas, NV.
A K M M. Rahman, M. I. Tanveer, ASM. I. Anam, and M. Yeasin, "IMAPS: A Smart Phone Based Real-Time Framework For Prediction Of Affect In Natural Dyadic Conversation", In Proceedings of the conference of Visual Communications and Image Processing (VCIP 2012) , San Diego, CA (acceptance rate = 22.3% oral).
A K M M. Rahman, M. I. Tanveer, and M. Yeasin. "A spatio-temporal probabilistic framework for dividing and predicting facial action units". In Proceedings of the 4th international conference on Affective computing and intelligent interaction - Volume Part II, ACII’11. 
M. I. Tanveer, A.S.M. I. Anam, S. Ghosh, A K M M. Rahman, and M. Yeasin, “FEPS: A Sensory Substitution System for the Blind to Perceive Facial Expressions”, In Proceedings of the ASSETS 2012, Boulder, Colorado.
R. Azevedo, R. Landis, R. F. Behnagh, M. Duffy, G. Trev., J. Harley, F. Bouchet, J. Burlison, M. Taub, N. Pacam., M. Yeasin, A K M M. Rahman, M. I. Tanveer, and G. Hossain, “The Effectiveness of Pedagogical Agents’ Prompting and Feedback in Facilitating Co-Adapted Learning with MetaTutor”, Intelligent Tutoring Systems (ITS), LNCS, Vol. 7315/2012, 2012.
A K M M. Rahman, Sidney D’Mello, “Tracking Facial behavior from Video”,  IIS, May, 2010
	
Aunnoy K Mutasim, Ali Shihab Sabbir, M Ashraful Amin

 , "Devising a Strategy for Playing Bangla Hangman (Jhulonto Manob) Based on Character Frequency Distribution", 5th International Conference on Informatics, Electronics & Vision (ICIEV’16)., , 2016
Shabnam Shahreen Sifat, Ali Shihab Sabbir

 , "Virtual ATM: A Low Cost Secured Alternative to Conventional Mobile Banking", International Journal of Interactive Mobile Technologies, Volume 9; iJIM 9(2): 44-49, , 2015 , (Link)
Rakibul Alam, Ali Shihab Sabbir

 , "Web Application for Generating Dynamic Surveys Deployable Over Mobile Devices", Journal of Bangladesh Electronic Society, Vol. 13 (1-2), 109-114, , 2015
Kaliappa Ravindran, Supratik Mukhopadhyay, Subhajit Sidhanta, Ali Sabbir

 , "Managing shared contexts in distributed multi-player game systems", COMSNETS 2014: 1-8, , 2014 , (Link)
Chaklader S., Alam J., Islam M., Ali Shihab Sabbir

 , "Black Box: An emergency rescue dispatch system for road vehicles for instant notification of road accidents and post-crash analysis", 3rd International Conference on Informatics, Electronics & Vision (ICIEV'14), Dhaka 23-24 May, 2014, IEEExplore ISBN :978-1-4799-5179-6 , 2014 , (Link)
Subrata Kumar Dey, M. Abdus Sobhan, Ali Shihab Sabbir

 , "Grid/cloud-based e-Governance of higher education institutes and perception thereof: Bangladesh perspective", ICEGOV 2014: 330-33, , 2014 , (Link)
Sayem Chakladar, Junaed Alam, Monirul Islam, Ali Shihab Sabbir

 , "Bridging Digital Divide: 'Village Wireless LAN', A Low Cost Infrastructure Solution for Digital Communication", Information Dissemination and Education in Rural Bangladesh. International Conference on Advances in Electrical Engineering (ICAEE), 2013, Dhaka, Bangladesh, IEEExplore ISBN : 978-1-4799-2463-9 , 2013 , (Link)
Ali S Sabbir, M Omar Rahman, Khosru M. Salim, Raihan Bin Rafique, Syed Ishtiaque Ahmed, Md Hasanuzzaman Bhuiyan, Md. Mustafizur Rahman, Hasan Shahid Ferdous

 , "Birth Record Communicator: A Pathway to Automated Health Data Acquisition System", Workshop on Interactive Systems in Healthcare (WISH 2011) at AMIA 2011 Annual Symposium, Washington, DC, USA. , 2011
Ali Shihab Sabbir, Kaliappa Ravindran

 , "A Context Driven Framework for Distributed Collaboration", DSRT 2009 (Distributed Simulation and Real-Time Applications), Singapore , 2009 , (Link)
Kaliappa Ravindran, Ali Sabbir, Balachandran Ravindran

 , "Impact of Network Loss/Delay Characteristics on Consistency Control in Real-time Multi-player Games", Fifth IEEE Consumer Communications & Networking Conference IEEECCNC 2008, Las Vegas, Nevada , 2008 , (Link)
Kaliappa Nadar Ravindran, Jiang Wu, Kevin A. Kwiat, Ali Sabbir

 , "Adaptive Voting Algorithms for Reliable Dissemination of Data in Sensor Networks", ARES 2008 Pp:1234-1239, Barcelona, Spain , 2008 , (Link)
K. Ravindran, J. Wu, M. Rabby, K. Kwiat, A. Sabbir

 , "Performance Engineering of Replica Voting Protocols for High Assurance Data Collection Systems", Communication Systems Software and Middleware COMSWARE'08, Bangalore, IEEExplore , 2008 , (Link)
Sabbir, A. Ravindran, K. Kwiat, K.A.

 , "Secure Distributed Agreement Protocols for Information Assurance Applications", Communication Systems Software and Middleware COMSWARE’07, Bangalore, Jan.2007., IEEE , 2007 , (Link)
Jiang Wu, Kaliappa Nadar Ravindran, Ali Sabbir, Kevin A. Kwiat

 , "Engineering of Replica Voting Protocols for Energy-Efficiency in Data Delivery.", WOWMOM 2006, 456-458., , 2006 , (Link)
K. Ravindran, K. Kwiat, A. Sabbir and B. Cao

 , "Replica Voting: a Distributed Middleware Service for Real-time Dependable Systems", COMSWARE’06 (First International Conference on Communication Systems Software and Middleware) IEEE-ComSoc/ACM- Sigmobile, New Delhi, India , 2006 , (Link)
A. Sabbir and K. Ravindran

 , "Concurrency Control Frameworks for Interactive Sharing of Data Spaces in Real-time Distributed Collaborations", DSRT 2005 (Distributed Simulation and Real-Time Applications), Montreal, Canada , 2005 , (Link)
K. Ravindran, A. Sabbir and K. Kwiat

 , "Timed Publish-Subscribe Communications for Distributed Embedded Systems", DSRT 2005 (Distributed Simulation and Real-Time Applications), Montreal, Canada , 2005 , (Link)
K. Ravindran and A. Sabbir

 , "Integration of Message Ordering and Flow of Real-time: A Specification Framework for Timed Media Data Presentation", IASTED-IMSA’04 (Internet and Multimedia Systems and Applications), Kauai, USA , 2004 , (Link)
K. Ravindran, K. Kwiat and A. Sabbir

 , "Adapting Distributed Voting Algorithms for Secure Real-time Embedded Systems", IEEE DARES’04 (Distributed Auto-adaptive and Re-configurable Systems) Workshop –in conjunction with ICDCS’04, Tokyo, Japan, IEEE , 2004 , (Link)
Ali Sabbir and K. Ravindran

 , "User Assisted Tools for Concurrency Control in Distributed Multimedia Collaborations", ACM MM’2004 (ACM Multimedia), New York, NY , 2004 , (Link)
K. Ravindran, A. Sabbir and K. Kwiat

 , "Timed Atomic Write: A Programming Primitive for Real-time Distributed Embedded Systems", IEEE GLOBECOM’03, San Francisco, CA, IEEE , 2003 , (Link)
 A. Sabbir, K. Ravindran and K. Kwiat

 , "Secure Atomic Multicast Primitives for Distributed Information Assurance Applications", IEEE MILCOM’03 (Intl. Conf. on Military Communications), Boston, MA, IEEE , 2003 , (Link)
K.Kwiat, K. Ravindran, A. Sabbir and P. Hurley

 , "Communication Asynchrony and Timeliness Issues for Voting in Distributed Information Assurance Application", SCS-SPECTS’03 (Intl. Symposium on Performance Evaluation of Computer and Telecommunication Systems), Montreal, Canada , 2003
K. Kwiat, K. Ravindran, C.Liu and A. Sabbir

 , "Performance and Correctness Issues in Secure Voting for Distributed Sensor Systems", SPECTS 2002 (Intl. Symposium on Performance Evaluation of Computer and Telecommunication Systems), San Diego , 2002
K. Ravindran, A. Sabbir, D. Loguinov, and G. Bloom

 , "Cost-optimal Multicast Trees for Multi-source Data Flows", IEEE INFOCOM’01, Anchorage, AK, IEEE , 2001 , (Link)
 Aunnoy K Mutasim, Ali Shihab Sabbir, M Ashraful Amin

 , "Devising a Strategy for Playing Bangla Hangman (Jhulonto Manob) Based on Character Frequency Distribution", 5th International Conference on Informatics, Electronics & Vision (ICIEV’16)., , 2016
Shabnam Shahreen Sifat, Ali Shihab Sabbir

 , "Virtual ATM: A Low Cost Secured Alternative to Conventional Mobile Banking", International Journal of Interactive Mobile Technologies, Volume 9; iJIM 9(2): 44-49, , 2015 , (Link)
Rakibul Alam, Ali Shihab Sabbir

 , "Web Application for Generating Dynamic Surveys Deployable Over Mobile Devices", Journal of Bangladesh Electronic Society, Vol. 13 (1-2), 109-114, , 2015
Kaliappa Ravindran, Supratik Mukhopadhyay, Subhajit Sidhanta, Ali Sabbir

 , "Managing shared contexts in distributed multi-player game systems", COMSNETS 2014: 1-8, , 2014 , (Link)
Chaklader S., Alam J., Islam M., Ali Shihab Sabbir

 , "Black Box: An emergency rescue dispatch system for road vehicles for instant notification of road accidents and post-crash analysis", 3rd International Conference on Informatics, Electronics & Vision (ICIEV'14), Dhaka 23-24 May, 2014, IEEExplore ISBN :978-1-4799-5179-6 , 2014 , (Link)
Subrata Kumar Dey, M. Abdus Sobhan, Ali Shihab Sabbir

 , "Grid/cloud-based e-Governance of higher education institutes and perception thereof: Bangladesh perspective", ICEGOV 2014: 330-33, , 2014 , (Link)
Sayem Chakladar, Junaed Alam, Monirul Islam, Ali Shihab Sabbir

 , "Bridging Digital Divide: 'Village Wireless LAN', A Low Cost Infrastructure Solution for Digital Communication", Information Dissemination and Education in Rural Bangladesh. International Conference on Advances in Electrical Engineering (ICAEE), 2013, Dhaka, Bangladesh, IEEExplore ISBN : 978-1-4799-2463-9 , 2013 , (Link)
Ali S Sabbir, M Omar Rahman, Khosru M. Salim, Raihan Bin Rafique, Syed Ishtiaque Ahmed, Md Hasanuzzaman Bhuiyan, Md. Mustafizur Rahman, Hasan Shahid Ferdous

 , "Birth Record Communicator: A Pathway to Automated Health Data Acquisition System", Workshop on Interactive Systems in Healthcare (WISH 2011) at AMIA 2011 Annual Symposium, Washington, DC, USA. , 2011
Ali Shihab Sabbir, Kaliappa Ravindran

 , "A Context Driven Framework for Distributed Collaboration", DSRT 2009 (Distributed Simulation and Real-Time Applications), Singapore , 2009 , (Link)
Kaliappa Ravindran, Ali Sabbir, Balachandran Ravindran

 , "Impact of Network Loss/Delay Characteristics on Consistency Control in Real-time Multi-player Games", Fifth IEEE Consumer Communications & Networking Conference IEEECCNC 2008, Las Vegas, Nevada , 2008 , (Link)
Kaliappa Nadar Ravindran, Jiang Wu, Kevin A. Kwiat, Ali Sabbir

 , "Adaptive Voting Algorithms for Reliable Dissemination of Data in Sensor Networks", ARES 2008 Pp:1234-1239, Barcelona, Spain , 2008 , (Link)
K. Ravindran, J. Wu, M. Rabby, K. Kwiat, A. Sabbir

 , "Performance Engineering of Replica Voting Protocols for High Assurance Data Collection Systems", Communication Systems Software and Middleware COMSWARE'08, Bangalore, IEEExplore , 2008 , (Link)
Sabbir, A. Ravindran, K. Kwiat, K.A.

 , "Secure Distributed Agreement Protocols for Information Assurance Applications", Communication Systems Software and Middleware COMSWARE’07, Bangalore, Jan.2007., IEEE , 2007 , (Link)
Jiang Wu, Kaliappa Nadar Ravindran, Ali Sabbir, Kevin A. Kwiat

 , "Engineering of Replica Voting Protocols for Energy-Efficiency in Data Delivery.", WOWMOM 2006, 456-458., , 2006 , (Link)
K. Ravindran, K. Kwiat, A. Sabbir and B. Cao

 , "Replica Voting: a Distributed Middleware Service for Real-time Dependable Systems", COMSWARE’06 (First International Conference on Communication Systems Software and Middleware) IEEE-ComSoc/ACM- Sigmobile, New Delhi, India , 2006 , (Link)
A. Sabbir and K. Ravindran

 , "Concurrency Control Frameworks for Interactive Sharing of Data Spaces in Real-time Distributed Collaborations", DSRT 2005 (Distributed Simulation and Real-Time Applications), Montreal, Canada , 2005 , (Link)
K. Ravindran, A. Sabbir and K. Kwiat

 , "Timed Publish-Subscribe Communications for Distributed Embedded Systems", DSRT 2005 (Distributed Simulation and Real-Time Applications), Montreal, Canada , 2005 , (Link)
K. Ravindran and A. Sabbir

 , "Integration of Message Ordering and Flow of Real-time: A Specification Framework for Timed Media Data Presentation", IASTED-IMSA’04 (Internet and Multimedia Systems and Applications), Kauai, USA , 2004 , (Link)
K. Ravindran, K. Kwiat and A. Sabbir

 , "Adapting Distributed Voting Algorithms for Secure Real-time Embedded Systems", IEEE DARES’04 (Distributed Auto-adaptive and Re-configurable Systems) Workshop –in conjunction with ICDCS’04, Tokyo, Japan, IEEE , 2004 , (Link)
Ali Sabbir and K. Ravindran

 , "User Assisted Tools for Concurrency Control in Distributed Multimedia Collaborations", ACM MM’2004 (ACM Multimedia), New York, NY , 2004 , (Link)
K. Ravindran, A. Sabbir and K. Kwiat

 , "Timed Atomic Write: A Programming Primitive for Real-time Distributed Embedded Systems", IEEE GLOBECOM’03, San Francisco, CA, IEEE , 2003 , (Link)
 A. Sabbir, K. Ravindran and K. Kwiat

 , "Secure Atomic Multicast Primitives for Distributed Information Assurance Applications", IEEE MILCOM’03 (Intl. Conf. on Military Communications), Boston, MA, IEEE , 2003 , (Link)
K.Kwiat, K. Ravindran, A. Sabbir and P. Hurley

 , "Communication Asynchrony and Timeliness Issues for Voting in Distributed Information Assurance Application", SCS-SPECTS’03 (Intl. Symposium on Performance Evaluation of Computer and Telecommunication Systems), Montreal, Canada , 2003
K. Kwiat, K. Ravindran, C.Liu and A. Sabbir

 , "Performance and Correctness Issues in Secure Voting for Distributed Sensor Systems", SPECTS 2002 (Intl. Symposium on Performance Evaluation of Computer and Telecommunication Systems), San Diego , 2002
K. Ravindran, A. Sabbir, D. Loguinov, and G. Bloom

 , "Cost-optimal Multicast Trees for Multi-source Data Flows", IEEE INFOCOM’01, Anchorage, AK, IEEE , 2001 , (Link)
	
M.E. Kadir, P.S. Akash, S. Sharmin, A.A. Ali, M. Shoyaib

 , "A Proximity Weighted Evidential k Nearest Neighbor Classifier for Imbalanced Data", Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD), Singapore , 2020
P. Roy, S. Sharmin, A.A. Ali, M. Shoyaib

 , "Discretization and Feature Selection Based on Bias Corrected Mutual Information Considering High-Order Dependencies", Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD), Singapore , 2020
S. Mahmud, M.T.H Tonmoy, K.K. Bhaumik, AKM Rahman, M.A. Amin, M. Shoyaib, A.H.K and A.A. Ali

 , "Human Activity Recognition from Wearable Sensor Data using Self-Attention", 24th European Conference on Artificial Intelligence (ECAI), Spain , 2020
J Anowar, A.A. Ali and M.A. Amin

 , "A Low-Cost Wearable Rehabilitation Device", 12th International Conference on Computer and Automation Engineering (ICCAE 2020), Australia , 2020
A.B.S Nayeem, A Sarkar, A.A Ali, M.A. Amin, A.K.M Rahman

 , "LULC Segmentation of RGB Satellite Image Using FCN-8", 3rd SLAAI International Conference on Artificial Intelligence, Sri Lanka , 2019
N. Sadman, A. Sadmanee, M.I. Tanveer, M.A. Amin, A.A. Ali

 , "Intrinsic Evaluation of Bangla Word Embeddings", International Conference on Bangla Speech and Language Processing(ICBSLP), Sylhet, Bangladesh, 27-28 September , 2019
Arif, Abdullah Omar, Sabah Ashraf, AKM Mahhubur Rahman, M Ashraful Amin, Amin Ahsan Ali

 , "A Comparative Study on Disaster Detection from Social Media Images using Deep Learning", Global AI Congress, Kolkata, India , 2019
MD Sazzad Hossain, Amin Ahsan Ali, M Ashraful Amin

 , "Eye-Gaze to Screen Location Mapping for UI Evaluation of Webpages", 3rd International Conference on Graphics and Signal Processing, Hong Kong , 2019
M.N. Hoque, M. Mahbub, M.H. Tarek, L.N. Lata, A.A. Ali

 , "Nurse Care Activity Recognition: A GRU-based approach with attention mechanism", HASCA 2019: 7th International Workshop on Human Activity Sensing Corpus and Applications in conjunction with ACM UbiComp, London, UK , 2019
 M.E. Kadir, P.S. Akash, S. Sharmin, A.A. Ali, M. Shoyaib

 , "Can a Simple Approach Identify Complex Nurse Care Activity?", HASCA 2019: 7th International Workshop on Human Activity Sensing Corpus and Applications in conjunction with ACM UbiComp, London, UK , 2019
P.S. Akash, M.E. Kadir, A.A. Ali, M. Shoyaib

 , "A new splitting criterion for Decision tree using Hellinger distance", 28th International Joint Conference on Artificial Intelligence, Macao, China, August 10-16 , 2019
M. E. Kadir, P. S. Akash, A. A. Ali, M. Shoyaib and Z. Begum

 , "Evidential SVM for binary classification", 1st International Conference on Advances in Science, Engineering and Robotics Technology (ICASERT-2019), Dhaka, Bangladesh, May 3-5 , 2019
M. N. Haque, M.T.H. Tonmoy, S. Mahmud, A. A. Ali, M.A.H. Khan and M. Shoyaib

 , "GRU-based Attention Mechanism for Human Activity Recognition", 1st International Conference on Advances in Science, Engineering and Robotics Technology (ICASERT-2019), Dhaka, Bangladesh, May 3-5 , 2019
Sadia Sharmin, Mohammad Shoyaib, Amin Ahsan Ali, Muhammad Asif Hossain Khan, and Oksam Chae
 , "Simultaneous Feature Selection and Discretization based on Mutual Information", Pattern Recognition, vol 91, 2019, pp 162-174, Elsevier , 2019
P. Akash, M. Kadir, A. Ali, M.Tawhid, M. Shoyaib

 , "Introducing Confidence as a Weight in Random Forest", International Conference on Robotics,Electrical and Signal Processing Techniques (ICREST), Dhaka , 2019
M. Rahman, M. Shuvo, M. Zaber, A. Ali

 , "Traffic Pattern Analysis from GPS Data: A Case Study of Dhaka City", IEEE International Conference on Electronics, Computing and Communication Technologies (IEEE CONECCT), Bangalore, India , 2018
S. Islam, A. Ali, M. Zaber

 , "A Smart Grid Prerequisite: Survey on Electricity Demand Forecasting Models and Scope Analysis of Demand Forecasting in Bangladesh", IEEE Region 10 (Asia Pacific) Humanitarian Technology Conference (R10HTC), Dhaka, Bangladesh [Best paper award] , 2017
S. Sharmin, F. Aktar, A. Ali, M. Khan, M. Shoyaib

 , "BFSp: A feature selection method for bug severity classification", IEEE Region 10 (Asia Pacific) Humanitarian Technology Conference (R10-HTC), Dhaka, Bangladesh , 2017
M. Sayed, M. Rahman, M. Zaber, A. Ali

 , "Understanding Dhaka City Traffic Intensity and Traffic Expansion Using Gravity Model", 20th International Conference of Computer and Information Technology (ICCIT), Dhaka, Bangladesh , 2017
M. Sayed, M. Zaber, A. Ali, P. Mosharaf

 , "Enumerating the obstacles of accelerating the use of digital classroom: Lessons from Bangladesh", Communication Policy Research South, Yangon, Myanmar , 2017
D. Chaki, M. Zaber, A. Ali

 , "Understanding Complex Social Network of Government Officials in Decision Making", Communication Policy Research South, Yangon, Myanmar , 2017
S. Sharmin, A. Ali, M. A. Hossain, M. Shoyaib

 , "Feature Selection and Discretization based on Mutual Information", IEEE International Conference on Image, Vision and Pattern Recognition, Dhaka, Bangladesh [Best paper award] , 2017
S. Saha, A. Mahmud, A. Ali, M. A. Amin

 , "Classifying Digital X-ray images into Different Human Body Parts", 5th International Conference on Information, Electronics and Vision, Dhaka, Bangladesh , 2016
E. Hossain, S. M. S. Islam, A. Ali, M. A. Amin

 , "Fish Activity Tracking and Species Identification in Underwater Video", 5th International Conference on Information, Electronics and Vision, Dhaka, Bangladesh , 2016
S. Debnath, P. P. Roy, A. Ali, M. A. Amin

 , "Identification of Bird Species from their Singing", 5th International Conference on Information, Electronics and Vision, Dhaka, Bangladesh , 2016
N. Saleheen, A. Ali, S. Hossain, H. Sarker, S. Chaterjee, B. Marlin, E. Ertin, M. al'Absi, S. Kumar

 , "puffMarker: A Multi-Sensor Approach for Pinpointing the Timing of First Lapse in Smoking Cessation", ACM UbiComp, Osaka, Japan , 2015
A Kennedy, D Epstein, M Jobes, K Phillips, D Agage, M Tyburski, A Ali,  R Bari,  S Hossain, K Hovsepian,  M Rahman,  E Ertin, S Kumar, K Preston

 , "Continuous In-The-Field Measurement of Heart Rate: Correlates of Drug Use, Craving, Stress, and Mood in Polydrug Users", Drug and Alcohol Dependence, vol.151, Elsevier , 2015
S. Vhaduri, A. Ali, M. Sharmin, K. Hovsepian, and S. Kumar

 , "Estimating Drivers’ Stress from GPS Traces", Automotive UI, , 2014
M. Rahman, R. Bari, A. Ali, M. Sharmin, A. Raij, K. Hovsepian, S. Hossain, E. Ertin, A. Kennedy, D. Epstein, K. Preston, M. Jobes, S. Kedia, K. Ward, M. al’Absi, and S. Kumar

 , "Are We There Yet? Feasibility of Continuous Stress Assessment via Wireless Physiological Sensors", ACM BCB, , 2014
H. Sarker, M. Sharmin, A. Ali, M. Rahman, R. Bari, M. Hossain, and S. Kumar

 , "Assessing the Availability of Users to Engage in Just-in-Time Intervention in the Natural Environment", ACM UbiComp, Seattle, WA , 2014
S. Hossain, A. Ali, M. Rahman, E. Ertin, D. Epstein, A. Kennedy, K. Preston, A. Umbricht, Y. Chen, and S. Kumar

 , "Identifying Drug (Cocaine) Intake Events from Acute Physiological Response in the Presence of Free-living Physical Activity", ACM IPSN, Berlin, Germany , 2014
A. Ali, S. Hossain, K. Hovsepian, M. Rahman, K. Plarre, and S. Kumar

 , "mPuff: Automated Detection of Cigarette Smoking Puffs from Respiration Measurements", ACM IPSN, Beijing, China , 2012
M. Rahman, A. Ali, K. Plarre, M. al'Absi, E. Ertin, and S. Kumar

 , "mConverse: Inferring Conversation Episodes from Respiratory Measurements Collected in the Field", ACM Wireless Health, San Diego, CA , 2011
K. Plarre, A. Raij, S. Hossain, A. Ali, M. Nakajima, M. al'Absi, E. Ertin, et al.

 , "Continuous Inference of Psychological Stress from Sensory Measurements Collected in the Natural Environment", ACM IPSN, Chicago, IL [Nominated for Best Paper Award] , 2011
M. Rahman, A. Ali, Andrew Raij, Emre Ertin, Mustafa al’Absi, Santosh Kumar

 , "Online Detection of Speaking from Respiratory Measurement Collected in the Natural Environment", 10th ACM/IEEE International Conference on Information Processing in Sensor Networks (IPSN), Chicago, IL , 2011
S. Masum, M. Akbar, A. Ali, M. Rahman

 , "A Consensus based ℓ-Exclusion Algorithm for Mobile Ad Hoc Networks", Ad Hoc Networks, 8(1), pp.30-45, Elsevier , 2010
A. Raij, P. Blitz, A. Ali, S. Fisk, et. al.

 , "mstress: Supporting continuous collection of objective and subjective measures of psychosocial stress on mobile devices", Tech. Report No. CS-10-004, Dept. of Computer Science, Univ. of Memphis , 2010
H. Babu, A. Wadud, A. Ali

 , "A Method for Designing Decoded PLAs using Genetic Algorithms", Dhaka University Journal of Science, Bangladesh , 2006
M. R. Amin, A. A. Ali and M. L. Rahman

 , "Web-Enabled Exam Preparation and Evaluation Services for Secondary Level Objective Tests with Bangla Language Interface", International Conference on Computer Processing of Bangla (ICCPB), pp. 85-92, , 2006
A K M Fazlul Haque, Amin Ahasan Ali, M Shamim Kaiser

 , "Analysis and Investigation of a High Performance Intelligent Network using a UNIX-based tool", Journal of the Bangladesh Electronics Society Vol 5(2), ISSN: 1816-1510, , 2006
H. Babu, A. Ali, A. Chowdhury

 , "Realization of Digital Fuzzy Operations using Multi-Valued Fredkin Gates", International Conference on Computer Design (CDES’06), Las Vegas, USA , 2006
S. Masum, A. Ali

 , "Distributed Allocation of Identical Resources in Mobile Ad Hoc Networks", IEEE international Symposium on Modeling and Optimization in Mobile, Ad Hoc and Wireless Networks, pp.1-10, , 2006
S. Masum, A. Ali

 , "Asynchronous Leader Election in Mobile Ad Hoc Networks", IEEE 20th International Conference on Advanced Information Networking and Applications (AINA’06), pp.832-836, Vienna, Austria , 2006
S. Masum, A. Ali

 , "Maintaining a Binary Tree Structure for Mobile Ad Hoc Networks", 11th IEEE Symposium on Computers and Communications (ISCC'06), pp.201-206, Pula–Cagliari, Sardinia, Italy , 2006
S. Masum, A. Ali

 , "Asynchronous l-Exclusion in Mobile Ad Hoc Networks", IEEE 20th International Conference on Advanced Information Networking and Applications (AINA’06), pp.832-836, Vienna, Austria , 2006
S. Masum, A. Ali, M. Akbar

 , "A Fault-Resilient l–Exclusion Algorithm for Mobile AD HOC Networks", IEEE Pacific Rim Conference on Communications, Computers and Signal Processing (PacRim 2005), pp. 586–589, Victoria, B.C., Canada , 2005
H. Babu, M. Islam, A. Ali, M. Akon, M. Rahaman, M. Islam

 , "A Technique for Logic Design of Voltage-Mode Pass Transistor Based Multi-Valued Multiple-Output Logic Circuits", IEEE International Symposium of Multi-valued Logic, Japan , 2003
Ahmed Al Mansur, Md Ruhul Amin, Mohammad Asif ul Haq, Md Hasan Maruf, Md Mozaharul Mottalib, Ratil H Ashique, ASM Shihavuddin

 , "Mitigation of mismatch power loss in aged photovoltaic arrays following a comparative investigation into module rearrangement techniques", Energy Reports, Elsevier , 2022 , (Link)
Md Rasidul Islam, Md Rayid Hasan Mojumder, Biazid Kabir Moghal, ASM Jannatul Islam, Mohammad Raza Miah, Sourav Roy, Anuj Kumar, ASM Shihavuddin, Ratil H Ashique

 , "Impact of strain on the electronic, phonon, and optical properties of monolayer transition metal dichalcogenides XTe2 (X= Mo and W)", Physica Scripta, IOP Publishing , 2022 , (Link)
Ratil H Ashique, Zainal Salam, Md Hasan Maruf, ASM Shihavuddin, Md Tariqul Islam, Md Fayzur Rahman, Panos Kotsampopoulos, Hady H Fayek

 , "A Comparative Analysis of Soft Switching Techniques in Reducing the Energy Loss and Improving the Soft Switching Range in Power Converters", Electronics, MDPI , 2022 , (Link)
Md Ashiqur Rahman, Mamun Rabbani, Md Hasan Maruf, Aminul Islam, ASM Shihavuddin

 , "Characterizing the Aging Process of the Human Eye: Tear Evaporation, Fluid Dynamics, Blood Flow, and Metabolism-Based Comparative Study", BioMed Research International, Hindawi , 2022 , (Link)
Md Touhidul Imam, Md Hasan Maruf, Ahmed Al Mansur, ASM Shihavuddin

 , "Reducing levelized cost of energy using gas generator in off-grid wind-PV hybrid system", 2021 3rd International Conference on Sustainable Technologies for Industry 4.0 (STI), IEEE , 2021 , (Link)
Ratil H Ashique, ASM Shihavuddin, Mohammad Monirujjaman Khan, Aminul Islam, Jubaer Ahmed, M Arif, Md Hasan Maruf, Ahmed Al Mansur, Ashraf Siddiquee

 , "An Analysis and Modeling of the Class-E Inverter for ZVS/ZVDS at Any Duty Ratio with High Input Ripple Current", Electronics, MDPI , 2021 , (Link)
Ratil H Ashique, Md Hasan Maruf, Kazi Md Shahnawaz Habib Sourov, Md Mahadul Islam, Aminul Islam, Mamun Rabbani, Md Rasidul Islam, Mohammad Monirujjaman Khan, ASM Shihavuddin

 , "A Comparative Performance Analysis of Zero Voltage Switching Class E and Selected Enhanced Class E Inverters", Electronics, MDPI , 2021 , (Link)
Xiao Chen, Martin A Eder, Shihavuddin Asm, Dan Zheng

 , "A Human-Cyber-Physical System toward Intelligent Wind Turbine Operation and Maintenance", Sustainability, MDPI , 2021 , (Link)
Mia SN Siemon, ASM Shihavuddin, Gitte Ravn-Haren

 , "Sequential transfer learning based on hierarchical clustering for improved performance in deep learning based food segmentation", Scientific Reports, Nature , 2021 , (Link)
Wasif Arman Haque, Samin Arefin, ASM Shihavuddin, Muhammad Abul Hasan

 , "DeepThin: A novel lightweight CNN architecture for traffic sign recognition without GPU requirements", Expert Systems with Applications, Elsevier , 2021 , (Link)
Xiao Chen, ASM Shihavuddin, Steen Hjelm Madsen, Kenneth Thomsen, Steffen Rasmussen, Kim Branner

 , "AQUADA: Automated quantification of damages in composite wind turbine blades for LCOE reduction", Wind Energy, WILEY , 2021 , (Link)
Shahriar Mahmud Kabir, Mohammed IH Bhuiyan, Md Sayed Tanveer, ASM Shihavuddin

 , "RiIG Modeled WCP Image-Based CNN Architecture and Feature-Based Approach in Breast Tumor Classification from B-Mode Ultrasound", Applied Sciences, MDPI , 2021 , (Link)
Anis Ahmed, Mohammad Nurunnabi Mollah, ASM Shihavuddin

 , "Tumor Detection by Rectangular Microstrip Patch Antenna", 2021 3rd International Conference on Sustainable Technologies for Industry 4.0 (STI), IEEE , 2021 , (Link)
ASM Shihavuddin, Mohammad Kamrozzaman Kiron, Md Imamul Islam, Md Hasan Maruf, Ratil H Ashique, Shahriar Mahmud Kabir

 , "Cascaded 3-Stage Nuclei Segmentation Using U-net, Faster-RCNN and SegNet for Higher Precision", 2021 3rd International Conference on Sustainable Technologies for Industry 4.0 (STI), IEEE , 2021 , (Link)
Shahriar Mahmud Kabir, Md Sayed Tanveer, ASM Shihavuddin, Mohammed Imamul Hassan Bhuiyan

 , "Statistical Model Based Breast Tumor Classification in Contourlet Transform Domain", GUB Journal of Science and Engineering, GUB , 2021 , (Link)
Md Hasan Maruf, Md Shakib Ibne Ashrafi, ASM Shihavuddin, Syed Iftekhar Ali

 , "Design and comparative analysis of memristor-based transistor-less combinational logic circuits", International Journal of Electronics, Taylor & Francis , 2021 , (Link)
Md Tariqul Islam, Md Fayzur Rahman, Sourav Barua, ASM Shihavuddin, Md Hasan Maruf, Ratil H Ashique

 , "Harmonic Reduction of Cascaded H-Bridge Multilevel Inverter Using Advanced Level Shifted Pulse Width Modulation Technique", 2021 International Conference on Electronics, Communications and Information Technology (ICECIT), IEEE , 2021 , (Link)
ASM Shihavuddin, Mohammad Rifat Ahmmad Rashid, Md Hasan Maruf, Muhammad Abul Hasan, Mohammad Asif ul Haq, Ratil H Ashique, Ahmed Al Mansur

 , "Image based surface damage detection of renewable energy installations using a unified deep learning approach", Energy Reports, Elsevier , 2021 , (Link)
Md Tariqul Islam, Md Hasan Maruf, Asm Shihavuddin, Ratil H Ashique, Sourav Barua, Md Fayzur Rahman

 , "Modeling and Analysis of High Frequency Magnetic Link-Based 11kVAsymmetric 21 level Inverter for Solar Photovoltaic Systems", 2021 IEEE Industrial Electronics and Applications Conference (IEACon), IEEE , 2021 , (Link)
Md Hasan Maruf, Mamun Rabbani, Ratil H Ashique, Md Tariqul Islam, Murad Kabir Nipun, Mohammad Asif Ul Haq, Ahmed Al Mansur, ASM Shihavuddin

 , "Exergy based evaluation of power plants for sustainability and economic performance identification", Case Studies in Thermal Engineering, Elsevier , 2021 , (Link)
Mohammad Asif ul Haq, Aminul Islam, ASM Shihavuddin, Md Hasan Maruf, Ahmed Al Mansur, Mohammad Yusri Hassan

 , "Enhanced Energy Savings in Indoor Environments with Effective Daylight Utilization and Area Segregation", Symmetry, MDPI , 2020 , (Link)
Marni Tausen, Marc Clausen, Sara Moeskjær, ASM Shihavuddin, Anders Bjorholm Dahl, Luc Janss, Stig Uggerhøj Andersen

 , "Greenotyper: Image-based plant phenotyping using distributed computing and deep learning", Frontiers in plant science, Frontiers Media SA , 2020 , (Link)
Md Hasan Maruf, Mohammad Asif ul Haq, Suman Kumar Dey, Ahmed Al Mansur, ASM Shihavuddin

 , "Adaptation for sustainable implementation of Smart Grid in developing countries like Bangladesh", Energy Reports, Elsevier , 2020 , (Link)
Md Sayed Tanveer, Shahriar Mahmud Kabir, ASM Shihavuddin

 , "Determination of Initial Projectile Velocity in the Presence of Static Fields Using Deep Actor Critic Method", 2020 11th International Conference on Electrical and Computer Engineering (ICECE), IEEE , 2020 , (Link)
Shahriar Mahmud Kabir, ASM Shihavuddin, Md Sayed Tanveer, Mohammed Imamul Hassan Bhuiyan

 , "Parametric Image-based Breast Tumor Classification Using Convolutional Neural Network in the Contourlet Transform Domain", 2020 11th International Conference on Electrical and Computer Engineering (ICECE), IEEE , 2020 , (Link)
Ratil H Ashique, Mohammad Monirujjaman Khan, ASM Shihavuddin, Md Hasan Maruf, Ahmed Al Mansur, Mohammad Asif ul Haq

 , "A Novel Family of Class EFnm and E/Fnm Inverter for Improved Efficiency", 2020 2nd International Conference on Sustainable Technologies for Industry 4.0 (STI), IEEE , 2020 , (Link)
Ahmed Al Mansur, Md Imamul Islam, Mohammad Asif ul Haq, Md Hasan Maruf, ASM Shihavuddin, Md Ruhul Amin

 , "Investigation of PV Modules Electrical Characteristics for Laboratory Experiments using Halogen Solar Simulator", 2020 2nd International Conference on Sustainable Technologies for Industry 4.0 (STI), IEEE , 2020 , (Link)
Ratil H Ashique, Mohammad Monirujjaman Khan, ASM Shihavuddin

 , "A Class E/F3 based 10W LED Driver with ZVS Capability", 2020 2nd International Conference on Sustainable Technologies for Industry 4.0 (STI), IEEE , 2020 , (Link)
Anabel Gómez-Ríos, Siham Tabik, Julián Luengo, ASM Shihavuddin, Francisco Herrera

 , "Coral species identification with texture or structure images using a two-level classifier based on Convolutional Neural Networks", Knowledge-Based Systems, Elsevier , 2019 , (Link)
Gonzalo Ortiz-Álvarez, Marie Daclin, Asm Shihavuddin, Pauline Lansade, Aurélien Fortoul, Marion Faucourt, Solène Clavreul, Maria-Eleni Lalioti, Stavros

 , "Adult neural stem cells and multiciliated ependymal cells share a common lineage regulated by the geminin family members", Neuron, Cell Press , 2019 , (Link)
Anabel Gómez-Ríos, Siham Tabik, Julián Luengo, ASM Shihavuddin, Bartosz Krawczyk, Francisco Herrera

 , "Towards highly accurate coral texture images classification using deep convolutional neural networks and data augmentation", Expert Systems with Applications, Pergamon , 2019 , (Link)
Ahmed Al Mansur, Mohammad Asif ul Haq, Md Hasan Maruf, ASM Shihavuddin, Md Ruhul Amin, Kazi Khairul Islam

 , "Experimental investigation of PV array interconnection topologies at nonuniform aging condition for power maximization", GUB Journal of Science and Engineering (GUBJSE), GUB , 2019 , (Link)
DMS Zaman, Md Hasan Maruf, Md Ashiqur Rahman, Jannatul Ferdousy, ASM Shihavuddin

 , "Food Depth Estimation Using Low-Cost Mobile-Based System for Real-Time Dietary Assessment", GUB Journal of Science and Engineering, GUB , 2019 , (Link)
ASM Shihavuddin, Xiao Chen, Vladimir Fedorov, Anders Nymark Christensen, Nicolai Andre Brogaard Riis, Kim Branner, Anders Bjorholm Dahl, Rasmus Reinhold Paulsen

 , "Wind turbine surface damage detection by deep learning aided drone inspection analysis", Energies, MDPI , 2019 , (Link)
Alice Ahlem Othmani, Sreetama Basu, Amulya Nidhi Shrivastava, Sinem Aslan, Francesco De Carli, Amesefe Delase Afua, ASM Shihavuddin, Amine Nait-Ali

 , "Biometrics from Cellular Imaging", Biometrics under Biomedical Considerations, Springer , 2019 , (Link)
 R. Revichandran, A. K. M. Mohiuddin and M. F. Uddin

 , "Experimental Investigation of Straight Shape Thermosyphon Filled with R410A Refrigerant", International Journal of Engineering and Advanced Technology (IJEAT), Volume-8, Issue-2S2, pp. 271-278, , 2019
A. K. M. Mohiuddin, A. Osman and M. F. Uddin

 , "Development and investigation of a cooling system for a parked vehicle using solar energy", International Journal of Recent Technology and Engineering (IJRTE), Volume-7, Issue-6S, pp. 87-92, March , 2019 , (Link)
R. Revichandran, A. K. M. Mohiuddin, M. F. Uddin

 , "Factors affecting thermosyphon performance A review of studies", International Journal of Recent Technology and Engineering (IJRTE), Volume-7, Issue-6S, pp. 124-133, March , 2019 , (Link)
M. H. K. Tushar, C. Assi, M. Maier and M. F. Uddin

 , "Smart Microgrids: Optimal Joint Scheduling for Electric Vehicles and Home Appliances", IEEE Transactions on Smart Grid, vol. 5(1), pp. 239-250, January , 2014
M. F. Uddin, C. Assi and A. Ghrayeb

 , "Joint optimal AF relay assignment and power allocation in wireless cooperative networks", Computer Networks, vol. 58, pp. 58-69, January , 2014
M. F. Uddin and C. Assi

 , "Joint Routing and Scheduling in WMNs with Variable-Width Spectrum Allocation", IEEE Transactions on Mobile Computing, vol. 12(11), pp. 2178-2192, November , 2013
H. M. K. Alazemi and M. F. Uddin

 , "Fair Resource Allocation and DF Relay Selection for Multiuser OFDMA-based Cooperative Networks", Springer Wireless Networks, vol. 19(6), pp. 1485-1496, August , 2013
M. F. Uddin

 , "Design methods for optimal resource allocation in wireless networks", PhD thesis,, Concordia University , 2012 , (Link)
M. F. Uddin, C. Assi and A. Ghrayeb

 , "Joint Optimal Relay Selection and Power Allocation in Multicast Cooperative Networks", In Proc. IEEE International Conference on Communications (ICC '12), pp- 1-6, May , 2012
M. F. Uddin, C. Assi and A. Ghrayeb

 , "Joint Relay Assignment and Power Allocation for Multicast Cooperative Networks", IEEE Communications Letters, vol. 16(3), pp.368-371, March , 2012
M. F. Uddin, H. M. K. Alazemi and C. Assi

 , "Optimal Flexible Spectrum Access in Wireless Networks with Software Defined Radios", IEEE Transactions on Wireless Communications, vol. 10(1), pp. 314-324, January , 2011
M. F. Uddin, M. Nurujjaman and C. Assi

 , "Joint Scheduling and Spectrum Allocation in Wireless Networks with Frequency-Agile Radios", In Proc. LNCS ADHOC-NOW. pp. 95 – 108, August , 2010
M. F. Uddin, H. M. K. Alazemi and C. Assi

 , "Optimal Flexible Spectrum Partitioning in Multihop Software Defined Radio Networks", In Proc. ACM International Conference on Modeling, Analysis and Simulation of Wireless and Mobile Systems (MSWIM), pp. 355-359, October , 2010
M. F. Uddin, H. M. K. Alazemi and C. Assi

 , "Joint Routing, Scheduling and Variable-Width Channel allocation for Multi-hop WMNs", In Proc. IEEE International Conference on Communications (ICC '10), pp- 1-6, May , 2010
M. F. Uddin and A. M. Youssef

 , "Cryptanalysis of Pointcheval's Identification Scheme Using Ant Colony Optimization", In Proc. IEEE Congress on Evolutionary Computation (CEC '07), pp. 2942 – 2947, September , 2007 , (Link)
M. F. Uddin and A. M. Youssef

 , "Cryptanalysis of Simple Substitution Ciphers Using Particle Swarm Optimization", In Proc. IEEE Congress on Evolutionary Computation (CEC '06), pp. 677-680, July , 2006 , (Link)
Z. Saber, M. F. Uddin and A. M. Youssef

 , "On Some Resilient Functions Constructions using PSO-based Spectral Inversion", In Proc. 2006 IEEE on Swarm Intelligence Symposium (SIS’06), pp.38-42, May , 2006
M. F. Uddin and A. M. Youssef

 , "An Artificial Life Technique for Cryptanalysis of Simple Substitution Ciphers", In Proc. IEEE Canadian Conference on Electrical and Computer Engineering (CCECE 2006), Ottawa, pp. 1582-1585, May , 2006 , (Link)
Z. Saber, M. F. Uddin and A. M. Youssef

 , "On the Existence of (9, 3, 5, 240) Resilient Functions", IEEE Transactions on Information Theory, vol. 52(5), pp. 2269-2270, May , 2006 , (Link)
M. F. Uddin

 , "Artificial life techniques for cryptology", Masters thesis,, Concordia University , 2006 , (Link)
 V. Mishra, S. Smith, L. Liu, F. Zahid, Y. Zhu, H. Guo, and S. Salahuddin

 , "Screening in Ultrashort (5 nm) Channel MoS2 Transistors: A Full-Band Quantum Transport Study", IEEE Transactions of Electron Devices, vol. 62, No. 8, p. 2457 , , 2015
D. Wickramaratne, R. Lake, and F. Zahid

 , "Electronic and thermoelectric properties of van der Waals materials with ring-shaped valence bands", Journal of Applied Physics, vol. 118, p. 075101, , 2015
D. Wickramaratne, F. Zahid, and R. Lake

 , "The thermoelectric performance of few-layer transition metal dichalcogenides", Journal of Chemical Physics, vol. 140, p.124710, , 2014
M. Habib, F. Zahid, and R. Lake

 , "Multi-state current switching by the voltage controlled quantum interference of standing electronic waves in crossed graphene nanoribbons", Journal of Applied Physics, vol. 114, p.153710, , 2013
L. Zhang, F. Zahid, Y. Zhu, L. Lei, J. Wang, H. Guo, P. Chan, and M. Chan

 , "First principles simulations of nanoscale Si devices with uniaxial strain", IEEE Transactions of Electron Devices, vol. 60, No. 10, p.3527, , 2013
F. Zahid, L. Liu, Y. Zhu, J. Wang, and H. Guo

 , "A generic tight-binding model for monolayer, bilayer and bulk MoS2", AIP Advances, vol. 3, p. 052111 , , 2013
Y. Wang, H. Yin, R. Cao, F. Zahid, Y. Zhu, L. Lei, J. Wang, and H. Guo

 , "Electronic structure of III-V zinc-blende semiconductors from first principles", Phys. Rev. B, vol. 87, p. 235203, , 2013
Y. Wang, F. Zahid, Y. Zhu, L. Lei, J. Wang, and H. Guo

 , "Band offset of GaAs/AlxGa1-xAs heterojunctions from atomistic first principles", Appl. Phys. Lett, vol. 102, p. 132109 , , 2013
D. Li, M. Li, F. Zahid, J. Wang, and H. Guo

 , "Oxygen vacancy filament formation in TiO2: a kinetic Monte Carlo study", J of Appl. Phys. vol. 112, p. 073512 , , 2012
Y. Wang, F. Zahid, J. Wang, and H. Guo

 , "Structure and dielectric properties of amorphous high-κ oxides: HfO2, ZrO2 and their alloys", Phys. Rev. B, vol. 85, p. 224110 , , 2012
M. Habib, F. Zahid, and R. Lake

 , "Negative differential resistance in bilayer graphene nanoribbons", Appl. Phys. Lett, vol. 98, p. 192112 , , 2011
M. Smeu, F. Zahid, W. Ji, H. Guo, M. Jaidann, and H. Abou-Rachid

 , "Energetic molecules encapsulated inside carbon nanotubes and between grapheme layers: DFT calculations", J. of Phys. Chem. C, vol. 115, p. 10985 , , 2011
F. Zahid, Youqi Ke, D. Gall, and H. Guo

 , "Resistance of thin Cu films coated with Ta, Ti, Ru, Al, and Pd barrier layers from First principles", Phys. Rev. B, vol. 81, p. 045406 , , 2010
J.S. Chawla, F. Zahid, H. Guo, and D. Gall

 , "Effect of O2 adsorption on electron scattering at Cu(001) surfaces", Appl. Phys. Lett, vol. 97, p. 132106 , , 2010
F. Zahid and R. Lake

 , "Thermoelectric properties of Bi2Te3 atomic quintuple thin films", Appl. Phys. Lett, vol. 97, p. 212102 , , 2010
J. Maassen, F. Zahid, and H. Guo

 , "Effects of Dephasing in Molecular Transport Junctions using atomistic First principles", Phys. Rev. B, vol. 80, p. 125423 , , 2009
Youqi Ke, F. Zahid, V. Timoshevskii, D. Gall, and H. Guo

 , "Resistivity of thin Cu films with Surface Roughness", Phys. Rev. B, vol. 79, p. 155406 , , 2009
F. Zahid, M. Paulsson, E. Polizzi, A. W. Ghosh, L. Siddiqui, and S. Datta

 , "A Self-consistent Transport Model for Molecular Conduction based on Extended Hückel Theory with Full 3-D Electrostatics", J. Chem. Phys., vol. 123, p. 064707 , , 2005
F. Zahid, A. W. Ghosh, M. Paulsson, E. Polizzi, and S. Datta

 , "Charging-induced Asymmetry in Molecular Conductors", Phys. Rev. B, Vol. 70, p. 245317, , 2004
B. Kasibhatla, A. Labonte, F. Zahid, R. Reifenberger, S. Datta, and C. Kubiak

 , "Reversibly Altering Electronic Conduction through a Single Molecule by a Chemical Binding Event", J. Phys. Chem. B, vol. 107, p. 12378 , , 2003
F. Zahid, M. Paulsson, and S. Datta

 , "Electrical Conduction through Molecules", Advanced Semiconductor and Organic Nano-techniques (III), H. Morkoc (Ed.), Academic Press , 2003
A. W. Ghosh, F. Zahid, S. Datta, and R. Birge

 , "Charge transfer in molecular conductors-oxidation or reduction?", Chem. Phys., vol. 281, p. 225 (2002), Special issue on Molecular Nanoelectronics, Ed. Mark Ratner, , 2002
M. A. Khaleque, F. Zahid, G. M. Bhuiyan, and R. I. M. A. Rashid

 , "Calculations of thermodynamic and transport properties of less simple metals", Ind. J. Phys. vol. 76A, p. 293, , 2002
M. Paulsson, F. Zahid, and S. Datta

 , "Resistance of a Molecule", Nanoscience, Engineering and Technology Handbook, Edited by D. Brenner, S. Lyshevski and G. Iafrate, CRC Press, Boca Roton, FL , 2002
F. Zahid, G. M. Bhuiyan, S. Sultana, M. A. Khaleque, R. I. M. A. Rashid, and S. M. M. Rahman

 , "Investigation of the static and dynamic properties of liquid less simple metals", Phys. Stat. Sol. B, vol. 215, p. 987 , , 1999
F. Zahid, G. M. Bhuiyan, M. A. Khaleque, and R. I. M. A. Rashid

 , "Calculations of structure and shear viscosity for less simple liquid metals", J. Non-Cryst. Solids, vol. 250-52, p.107, , 1999
F. Zahid, G.M. Bhuiyan, and M. A. Khaleque

 , "Calculations of S(q) and g(r) for Less Simple Liquid Metals", Dhaka Univ. J. Sci. vol. 46, p. 343 , , 1998
	
Islam, Md Saiful, Tanhim Islam, and Mahady Hasan

 , "Approaching Deep Convolutional Neural Network for Biometric Recognition Based on Fingerprint Database", Intelligent Computing, Springer , 2021 , (Link)
Alam, Samiul, Tahsin Reasat, Asif Shahriyar Sushmit, Sadi Mohammad Siddique, Fuad Rahman, Mahady Hasan, and Ahmed Imtiaz Humayun

 , "A Large Multi-target Dataset of Common Bengali Handwritten Graphemes", International Conference on Document Analysis and Recognition (ICDAR), Springer , 2021 , (Link)
Towsif Zahin Khan, Shairil Hossain Tusher, Mahady Hasan, and M. Rokonuzzaman

 , "Designing and Developing a Game with Marketing Concepts", Advances in Intelligent Systems and Computing, Springer , 2019 , (Link)
M. S. Kaysar, M. A. B. Khaled, Mahady Hasan, and M. I. Khan

 , "Word Sense Disambiguation of Bengali Words using FP-Growth Algorithm", International Conference on Electrical, Computer and Communication Engineering (ECCE), IEEE , 2019 , (Link)
A. K. M. Wasimul, Hossain, Laila Nushrat, Raha, Tahmid Faiyaz, Mahady Hasan, Nuzhat Nahar, and M. Rokonuzzaman

 , "Sustainable Management Strategy for Software Firms to Reduce Employee Turnover due to Freelancing", Advances in Intelligent Systems and Computing, Springer , 2019 , (Link)
Feroz Nowaz, Mahady Hasan, Nuzhat Nahar, and M. Rokonuzzaman

 , "Sustainable IPR practices to address risk capital finance in software industries in developing countries", Advances in Intelligent Systems and Computing, Springer , 2019 , (Link)
Towsif Zahin Khan, Shairil Hossain Tusher, Mahady Hasan, and M. Rokonuzzaman

 , "Tailoring Scrum Methodology for Game Development", Advances in Intelligent Systems and Computing, Springer , 2019 , (Link)
Mohammad Rejwan Uddin, Wanas Uddin Ahmed, Mahady Hasan and Khosru M. Salim

 , "Design, Fabrication and Performance Analysis of a Vertical Axis Wind Turbine (VAWT) with a Proposed Grid Tie Topology Appropriate for the Coastal Region of Bangladesh", International Conference on Developments in Renewable Energy Technology (ICDRET), IEEE , 2018 , (Link)
Mohammad Rejwan Uddin, Wanas Uddin Ahmed, Mahady Hasan and Khosru M. Salim

 , "Design, Fabrication and Performance Analysis of a Vertical Axis Wind Turbine (VAWT) with a Proposed Grid Tie Topology Appropriate for the Coastal Region of Bangladesh", International Conference on Developments in Renewable Energy Technology (ICDRET), IEEE , 2018 , (Link)
Tahsin, Sarah, Abdul Munim, Mahady Hasan, Nuzhat Nahar, and M. Rokonuzzaman

 , "Market Analysis as a possible activity of Software Project Management", 16th International Conference on Software Engineering Research, Management and Applications (SERA), IEEE , 2018 , (Link)
Raha, Laila Nushrat, AKM Wasimul Hossain, Tahmid Faiyaz, Mahady Hasan, Nuzhat Nahar, and M. Rokonuzzaman

 , "A Guide for Building the Knowledgebase for Software Entrepreneurs, Firms, and Professional Students", 16th International Conference on Software Engineering Research, Management and Applications (SERA), IEEE , 2018 , (Link)
Mahady Hasan, Ahmed Latif Shahriar, Nuzhat Nahar, and M Rokonuzzaman

 , "Rational Decision Making Framework for Implementing Information System", International Conference on Innovations in Engineering, Technology and Sciences (ICIETS), IEEE , 2018 , (Link)
Md Monzur Morshed, Mahady Hasan, and M. Rokonuzzaman

 , "Software Architecture Decision-Making Practices and Recommendations", Advances in Intelligent Systems and Computing, Springer , 2018 , (Link)
Sourajit Saha, Md. Asif Bin Khaled, Md. Saiful Islam, Nisha Saha Puja and Mahady Hasan

 , "Detecting Sex From Handwritten Examples", ICSCAN- 2018 , , 2018
Aninda Saha, Shuvo Kumar Paul, Mahady Hasan, M. Ashraful Amin , "Android Based Autonomous ArduinoBot", CEET, SEEK , 2015 , (Link)
Hossain M. Z., M. A Wahid, Mahady Hasan and M Ashraful Amin , "Spatial Subdivision of Gabriel Graph", ICSI-CCI, Springer Lecture Notes in Computer Science (LNCS) , 2015 , (Link)
M Ashraful Amin, M S Shahriar  Faruque, Shourav  Banik, M Kazi  Mohammed, Mahady  Hasan

 , "Teaching & learning system for dianostic imaging phase I: x-ray image analysis & retrieval", International Conference on Computer Supported Education (CSEDU), , 2015 , (Link)
Husain Ashish M., Shajib Yusuf, Tazrin Hassan Rini, Mahady Hasan , "Noise Pollution in Major Places in Dhaka and Proposing a Device to Keep Noise Log", Journal Of Modern Science And Technology, Vol. 3 No. 1. March 2015 Issue. Pp.20-30 April 2015 , 2015 , (Link)
Hossain M. Z., Mahady Hasan and M Ashraful Amin , "Efficient Construction of Uncertain Voronoi Diagram", ICSI-CCI, Springer Lecture Notes in Computer Science (LNCS) , 2015 , (Link)
Paul S K, M. S. Q. Zulkar Nine, Mahady Hasan, and M. Ashraful Amin , "Cognitive Task Classificaiton from Wireless EEG", BHI, Springer Lecture Notes in Computer Science (LNCS) , 2015 , (Link)
Hasan, Mahady, Md Rakibul Alam, and Muhammad Aamir Cheema , "Performance evaluation of furthest k neighbors queries in spatial databases", Advances in Electrical Engineering (ICAEE), ieee Explore , 2013 , (Link)
Hasan, Mahady, and Muhammad Aamir Cheema , "Furthest k neighbors queries in spatial databases", Advances in Electrical Engineering (ICAEE), ieee Explore , 2013 , (Link)
Hasan Mahady, Muhammad Aamir Cheema, Xuemin Lin, and Wenjie Zhang , "A unified algorithm for continuous monitoring of spatial queries", Database Systems for Advanced Applications, Springer Lecture Notes in Computer Science (LNCS) , 2011 , (Link)
Hasan Mahady, Muhammad Aamir Cheema, Wenyu Qu, and Xuemin Lin , "Efficient algorithms to monitor continuous constrained k nearest neighbour queries", Database Systems for Advanced Applications, Springer Lecture Notes in Computer Science (LNCS) , 2010 , (Link)
Hasan, Mahady, Muhammad Aamir Cheema, Xuemin Lin, and Ying Zhang , "Efficient construction of safe regions for moving knn queries over dynamic datasets", Advances in Spatial and Temporal Databases, Springer Berlin Heidelberg , 2009 , (Link)
Dey, Subrata Kumar, Sabbir Mahmud, Mohammad Noor Nabi, Mahady Hasan, Indrani Haque, Bibhuti Roy , "Complexities in Developing Educational Software and a Proposed Curriculum to Mitigate Them", International Conference on Computer and Information Technology (ICCIT), ieee Explore , 2005
Ullah ASSM Barkat, Mahady Hasan, Khosru M. Salim , "Enhancement Conventional Voting System by using Micro controller based Electronic Voting Machine", In International Conference on Computer and Information Technology (ICCIT), ieee Explore , 2005
Hasan Mahady, Sabbir Mahmud, Subrata Kumar Dey, Noor nabi, Indrani Haque, Bibhuti Roy , "Analysis of Didactical Characteristics and Design Components of Educational Software in Bangladesh", International Conference on Computer and Information Technology (ICCIT), ieee Explore , 2005
Khosru M. Salim, Mahady Hasan, ASSM Barkat Ullah, T. Hoshino , "Performance evaluation of rectifier type superconducting fault current limiter (SFCL) by using short-circuited trigger coil", International Conference on Electrical and Computer Engineering (ICECE), Bangladesh , 2004
Hasan Mahady, Abu Saleh Shah Muhammad Barkat Ullah, Khosru M. Salim, Indrani Haque , "Micro-processor based low cost wireless system to automate multiple choice questions (MCQ) based exams", International Conference on Computer and Information Technology (ICCIT), ieee Explore , 2004
Hossain M. Shakhawat, Galib. M.S., Syeed, M. M., Uddin, M. F., Hasan. M., S. Shivam., & S. Advani. (2023). Region of Interest (ROI) Selection using Vision Transformer for Automatic Analysis using Whole Slide Images. Scientific Reports (Nature), vol. 13, 2023, 1038/s41598-023-38109-6.

Hossain M. Shakhawat, Galib. M.S., Syeed, M. M., Uddin, M. F., Hasan. M., Hossain. M.S., & Bari.  R. (2023). Tissue Artifact Segmentation and Severity Assessment for Automatic Analysis using WSI. IEEE Access, vol. 11, pp. 21977-21991, 2023, doi: 10.1109/ACCESS.2023.3250556.

Hossain M. Shakhawat, Mahmudur R., Syeed, M. M., Uddin, M. F., Hasan. M., Hossain. M.S., & others (2023). DeepPoly: Deep Learning-based Polyps Segmentation and Classification for Autonomous Colonoscopy Examination. IEEE Access, vol. 11, pp. 95889-95902, 2023, doi:10.1109/ACCESS.2023.3310541.

Hossain M. Shakhawat, Matthew Hanna, Naohiro Uraoka, Tomoya Nakamura, Marcia Edelweiss, Edi Brogi, Meera R. Hameed, Masahiro Yamaguchi, Dara S. Ross, Yukako Yagi (2019). Automatic  quantification of HER2 gene amplification in invasive breast cancer from chromogenic in situ hybridization whole slide images. SPIE Journal of Medical Imaging, 6(4), 047501, https://doi.org/10.1117/1.JMI.6.4.047501, PubMed PMID: 31763355

Hossain M. Shakhawat, Tomoya Nakamura, Fumikazu Kimura, Yukako Yagi, Masahiro Yamaguchi (2020). Automatic quality evaluation of whole slide images for the practical use of whole slide imaging scanner. ITE Trans. On MTA Vol. 8, No.4, pp. 252-268. https://doi.org/10.3169/mta.8.252

Hossain M. Shakhawat, Syeed, M. M., Fatema, K., Hossain, M. S., & Uddin, M. F. (2022). Singular Nuclei Segmentation for Automatic HER2 Quantification Using CISH Whole Slide Images. Sensors, 22(19), 7361, doi: 10.3390/s22197361. PubMed PMID: 36236459

Hossain M. Shakhawat, Syeed, M. M., Fatema, K., & Uddin, M. F. (2022). The Perception of Health Professionals in Bangladesh toward the Digitalization of the Health Sector. International Journal of Environmental Research and Public Health, 19(20), 13695, doi: 10.3390/ijerph192013695, PubMed PMID: 36294274

Hossain M. S., Hasan. N., Samad, M. A., & Hossain M. Shakhawat, Karmoker J., Ahmed. F., Fuad. N., Choi. K. (2022). Android Ransomware Detection from Traffic Analysis Using Metaheuristic Feature Selection", IEEE Access, , vol. 10, pp. 128754-128763, 2022, doi: 10.1109/ACCESS.2022.3227579.

Hossain M. Shakhawat, Raihan, M. E., Hossain, M. S., Syeed, M. M., Rashid, H., & Reza, M. S. (2022). Aedes Larva Detection using Ensemble Learning to Prevent Dengue Endemic. BioMedInformatics, Vol2,3,pp.405-423

Syed M. M. M.,Hossain M. Shakhawat, Karim, M. R., Uddin, M. F., Hasan. M., & R. H. Khan.  R. (2023). Surface water quality profiling using the water quality index, pollution index and statistical methods: A critical review. Environmental and Sustainability Indicators, vol. 18, pp. 100247, 2023, https://doi.org/10.1016/j.indic.2023.100247.

Hossain M.S. et al. (2023), Adoption of Unmanned Aerial Vehicle (UAV) imagery in agricultural management: A systematic literature review, Ecological Informatics (Elsevier)
	
Md Zahangir Alam and Abbas Jamalipour

 , "Multi-Agent DRL-based Hungarian Algorithm (MADRLHA) for Task Offloading in Multi-Access Edge Computing Internet of Vehicles (IoVs)", IEEE Trans on Wireless communications, vol. 21, no. 9, pp. 7641-7652, Sept. 2022, , 2022
Md Zahangir Alam, Iwan Adhicandra, Ko

 , "SDP-IGD: An iterative power allocation technique for cluster-based multihop vehicular communications", IEEE Trans on Vech. Tech, vol. 69, no. 7, pp. 7908-7915, July 2020, , 2020
Md Zahangir Alam, Forough S. Abkenar,

 , "Low-delay Path Selection for Cluster-Based Buffer-Aided Vehicular Communications", IEEE Trans on Vech. Tech, vol. 69, no. 9, pp. 9356-9363, Sept., 2020, , 2020
F. S. Abkenar, M. Z. Alam and A. Jamalipour

 , "Transaction Throughput Maximization under Delay and Energy Constraints in Fog-IoT Networks", GLOBECOM 2020 , Taipei, Taiwan, 2020, pp. 1-6, , 2020
Md Zahangir Alam, Iwan Adhicandra, an

 , "Optimal Best Path Selection Algorithm for Cluster-Based Multi-Hop MIMO Cooperative Transmission for Vehicular Communications", IEEE Trans on Vech. Tech, vol. 68, no. 9, pp. 8314-8321, Sept. 2019. , , 2019
"""
# Function to extract titles and authors
def extract_authors_and_titles(data):
    pattern = r"(?<=\n)(.+?)\n(.+?)\n"
    matches = re.findall(pattern, data)
    return matches

# Extract data
extracted_data = extract_authors_and_titles(text)

# Define output file name
output_csv = "cu_authors.csv"

# Write extracted data to CSV
with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Authors"])  # CSV header
    for title, authors in extracted_data:
        writer.writerow([title.strip(), authors.strip()])

print(f"Data successfully written to {output_csv}.")