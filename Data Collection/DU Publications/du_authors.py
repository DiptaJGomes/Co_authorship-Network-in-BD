import csv
import re

# Input data (replace this block with actual input if reading from a file)
text = """
1	Md Samiullah, Ann E Nicholson and David W Albrecht iOOBN: An Object-Oriented Bayesian Network Modelling Framework with Inheritance. Melbourne: Monash University Thesis Archive, 2020 .
View More
2	Md Samiullah and CF Ahmed An efficient approach to mine correlated graphs. Dhaka: Department of Computer Science and Engineering, University of Dhaka, 2012 .
View More
3	Dr. Md. Haider Ali and Ahmed Samsul Arefin Fundamentals of Computer and Information Technology. Dhaka, Bangladesh: Gyankosh Prokashoni, ISBN 984-70277-0041-1, 2009 .
4	Md. Rezaul Karim Straight-Line Grid Drawings of Planar Graphs with Sub-Quadratic Area,. Germany: VDM Verlag, 2009 .
5	Hafiz Md. Hasan Babu “VLSI Circuits and Embedded Systems”. Florida, USA: CRC Press, 2021 .
6	Hafiz Md. Hasan Babu “Quantum Computing: A Pathway to Quantum Logic Design”. Bristol, UK: IOP Publishers, 2020 .
7	Hafiz Md. Hasan Babu “Reversible and DNA Computing”. UK: Wiley Publishers, 2020 .
8	Hafiz Md. Hasan Babu VLSI Circuits and Embedded Systems. USA: CRC Press, 2022 .
9	Hafiz Md. Hasan Babu “One Dream One Country: Digital Bangladesh”. Bangladesh: Nabarag Prokashani Publishers, 2018 .
1	Kashob Kumar Roy, Md Hasibul Haque Moon, Md Mahmudur Rahman, Chowdhury Farhan Ahmed and Carson K. Leung "Mining Sequential Patterns in Uncertain Databases Using Hierarchical Index Structure." Advances in Knowledge Discovery and Data Mining. Springer, 2021 29-41 .
View More
2	Shaily Kabir and Christian Wagner "A Bidirectional Subsethood Based Fuzzy Measure for Aggregation of Interval-Valued Data." Communications in Computer and Information Science book series ( CCIS, volume 1238). Springer, Cham, 2020 .
3	Md Mofijul Islam, Sk Shariful Islam Arafat, Md Shakil Hossain, Md Mahmudur Rahman, Md Mahmudul Hasan, SM Al-Hossain Imam, Swakkhar Shatabda and Tamanna Islam Juthi "RAiTA: Recommending Accepted Answer Using Textual Metadata." Emerging Technologies in Data Mining and Information Security. Springer, Singapore, 2018 119-131 .
View More
4	Karishma Mohiuddin, Mirza Mohtashim Alam, Amit Kishor Das, Md. Tahsir Ahmed Munna, Shaikh Muhammad Allayear and Md. Haider Ali "Haar Cascade Classifier and Lucas–Kanade Optical Flow Based Realtime Object Tracker with Custom Masking Technique." Advances in Information and Communication Networks, ISBN 978-3-030-03404-7. Kohei Arai, Supriya Kapoor and Rahul Bhatia Springer, Cham, 2018 .
View More
5	Muhammad Ibrahim and Manzur Murshed "From Tf-Idf to Learning-to-Rank: An Overview." Handbook of Research on Innovations in Information Retrieval, Analysis, and Management (SCOPUS Indexed). Jorge Tiago Martins (The University of Sheffield, UK) and Andreea Molnar (University of Portsmouth, UK) IGI Global, USA, 2016 62-109 .
View More
6	Shabbir Ahmed and Salil S. Kanhere "Message Dissemination in Vehicular Networks." Delay Tolerant Networks: Protocols and Applications. CRC Press, 2011 .
7	Shabbir Ahmed and Farzana Mithun "A Tutorial on Random Number Generators in Discrete Event Simulators." Simulation Technologies in Networking and Communications: Selecting the Best Tool for the Test. CRC Press, 2014 .
8	Shabbir Ahmed and Salil S. Kanhere "UNSW Technical Report UNSW-CSE-TR-1009 (2010)." Sydney: University of New South Wales, 2010 .
1	Md Mehedi Hasan, Muhammad Ibrahim and Md Sawkat Ali : Selecting Update Blocks of Convolutional Neural Networks using Genetic Algorithm in Transfer Learning (Accepted), Machine Graphics and Vision , vol.33 , no.2 Institute of Information Technology, Warsaw University of Life Sciences, Poland , pp.1-16 , 2024 .
2	Farhana Huq, Nahar Sultana, Palash Roy, Md. Abdur Razzaque, Shamsul Huda and Mohammad Mehedi Hassan : Cross Regional Online Food Delivery: An E-business Framework, Service Quality Optimization, and Real-time Order Assignment, Computers and Operations Research (impact factor:4.1) Elsevier , 2024 .
3	Sakib Al Jobaid, Upama Kabir and Mosarrat Jahan : Scalable data management in global health crises: Leveraging blockchain technology, IET Blockchain , 2024 .
4	Nahar Sultana, Farhana Huq, Palash Roy, Md. Abdur Razzaque, MM Rahman, T. Akter and MM Hassan : Context Aware Clustering and Meta Heuristic Resource Allocation for NB-IoT D2D Devices in Smart Healthcare Applications, Future Generation Computer System (impact factor:6.2) Elsevier , 2024 .
View More
5	Sudip CG, M. Maruf Hossain, BC Das, Palash Roy, Md. Abdur Razzaque, Saiful Azad, MM Hassan, C Savaglio and G Fortino : VESBELT: An Energy-Efficient and Low-Latency Aware Task Offloading in Maritime Internet-of-Things Networks Using Ensemble Neural Networks, Future Generation Computer System (impact factor:6.2) Elsevier , 2024 .
6	Mohd Sayemul Haque, Md Fahim and Muhammad Ibrahim : An Exploratory Study on Simulated Annealing for Feature Selection in Learning-to-Rank, International Journal of Intelligent Systems and Applications (Scopus Indexed) , vol.16 , no.4 MECS Press, Hong Kong , pp.86-103 , 2024 .
View More
7	Nafis Sajid, Md Rashidul Hasan and Muhammad Ibrahim : Feature Engineering in Learning-to-Rank for Community Question Answering Task, International Journal of Computers and Applications (Scopus Indexed) , vol.46 , no.7 Taylor and Francis, UK , pp.1-23 , 2024 .
View More
8	Nazifa Hia, Ishrat Emu, Muhammad Ibrahim and Sumon Ahmed : A Differential Evolution-based Pseudotime Estimation Method for Single-cell Data, International Journal of Advanced Computer Science and Applications (SCI and Scopus Indexed), SAI Publishers, UK , vol.15 , no.6 The SAI Publishers, UK , pp.1504-1513 , 2024 .
View More
9	Safiqul Islam, Mahadi Ahammed, N. A. Siddiquee, Palash Roy, Md. Abdur Razzaque, MM Hassan and Kashif Saleem : QoE Aware Service Placement Scheme in Mobile Edge Computing Exploiting Hyper-Heuristic Approach, IEEE Access (impact factor:3.9) IEEE , 2024 .
10	Sujan Sarker, Md. Tanvir Arafat, Aiman Lameesa, Mahbuba Afrin, Redowan Mahmud, Md. Abdur Razzaque and Tariq Iqbal : FOLD: Fog-Dew Infrastructure-aided Optimal Workload Distribution for Cloud Robotic Operations, Internet of Things (impact factor:5.9) Elsevier , 2024 .
11	Shamyo Brotee, Farhan Kabir, Md. Abdur Razzaque, Palash Roy, Md. Mamun-Or-Rashid, M.R. Hassan and M.M. Hassan : Optimizing UAV-UGV Coalition Operations: A Hybrid Clustering and Multi-Agent Reinforcement Learning Approach for Path Planning in Obstructed Environment, AdHoc Networks (impact factor:4.8) Elsevier , 2024 .
12	Nishat Tasnim Mim, Md Eusha Kadir, Suravi Akhter and Muhammad Asif Hossain Khan : An Overlapping Conscious Relief-based Feature Subset Selection Method, International Journal of Electrical and Computer Engineering (IJECE) , vol.14 , no.2 Institute of Advanced Engineering and Science (IAES) , pp.2068-2075 , 2024 .
View More
13	Md Ashraful Islam, Chowdhury Farhan Ahmed, Md Tanvir Alam and Carson Kai-Sang Leung : Graph-based substructure pattern mining with edge-weight, Applied Intelligence , vol.54 , no.5 Springer , pp.3756--3785 , 2024 .
14	Saiful Azad, Mufti Mahmud, Kamal Z. Zamli, Sobhana Jahan, Shamim Kaiser and Md. Abdur Razzaque : iBUST: An intelligent behavioral trust model for securing industrial cyber-physical systems, Expert Systems with Applications (impact factor:8.5) , vol.238 Elsevier , 2024 .
View More
15	Abdur Razzak, Md. Tariqul Islam, Palash Roy, Md. Abdur Razzaque and MM Hassan : Leveraging Deep Q-Learning to Maximize Consumer Quality of Experience in Smart Grid, Energy (impact factor:9.0) , vol.290 Elsevier , 2024 .
View More
16	Shabab Murshed, Abu Shaikh Nibir, Md. Abdur Razzaque, Palash Roy, Ahmed Z. E., MR Hassan and MM Hassan : Weighted Fair Energy Transfer in a UAV Network: A Multi-Agent Deep Reinforcement Learning Approach, Energy (impact factor:9.0) , vol.282 , no.1 Elsevier , 2024 .
View More
17	Pranjal K. Nandi, Md. Reajul Islam, Sujan Sarker, Palash Roy and Md. Abdur Razzaque : Task Offloading to Edge Cloud Balancing Utility and Cost for Energy Harvesting IoT, Journal of Network and Computer Applications (impact factor:8.7) , vol.221 Elsevier , 2024 .
View More
18	Nujhat Nawmi, F. Shanta, Palash Roy, M. Rashid, Sujan Sarker, Md. Abdur Razzaque and MM Hassan : Task Execution Exploiting Grey Wolf Optimization in Collaborative Edge Computing, Journal of Cloud Computing (impact factor:4.4) , vol.13 , no.1 Springer , 2024 .
View More
19	Zhang Wenhua, Mohammad Kamrul Hasan, Ahmad Fadzil Ismail, Zhang Yanke, Md Abdur Razzaque, Shayla Islam and Budati Anil Kumar : Data security in smart devices: Advancement, constraints and future recommendations, IET Networks (impact factor:1.4) , vol.2 , no.6 Wiley , 2023 .
View More
20	Md. Shafiqul Islam, Muntaha Tasnim, Upama Kabir and Mosarrat Jahan : Securing Smart Home against Sinkhole Attack using Weight-based IDS Placement Strategy, IET Wireless Sensor Systems , pp.1-19 , 2023 .
21	Md. Mahmudul Hasan, Mosarrat Jahan and Shaily Kabir : A Trust Model for Edge-Driven Vehicular Ad Hoc Networks Using Fuzzy Logic, IEEE Transactions on Intelligent Transportation Systems IEEE , pp.1-14 , 2023 .
View More
22	Mosarrat Jahan, Fatema Tuz Zohra, Md. Kamal Parvez, Upama Kabir, Abdul Mohaimen Al Radi and Shaily Kabir : An end-to-end authentication mechanism for Wireless Body Area Networks, Smart Health , vol.29 Elsevier , pp.100413 , 2023 .
View More
23	Md. Mahmudul Hasan, Mosarrat Jahan and shaily Kabir : A Trust Model for Edge-Driven Vehicular Ad Hoc Networks using Fuzzy Logic, IEEE Transactions on Intelligent Transportation Systems , vol.24 , no.12 IEEE , pp.1-14 , 2023 .
View More
24	Syeda Nabila Akter, Afsana Kabir Sinthia, Palash Roy, Md. Abdur Razzaque and MM Hassan : Reputation Aware Optimal Team Formation for Collaborative Software Crowdsourcing in Industry 5.0, Computers and Industrial Engineering (impact factor:7.18) , vol.35 , no.8 Elsevier , 2023 .
View More
25	Hasin Rehana, Muhammad Ibrahim and Md. Haider Ali : Plant Disease Detection using Region-Based Convolutional Neural Network, Preprint submitted to Elsevier , 2023 .
26	Muhammad Aminur Rahaman, Md. Haider Ali and Md. Hasanuzzaman : Real-time computer vision-based gestures recognition system for bangla sign language using multiple linguistic features analysis, Multimedia Tools and Applications , vol.83 , no.8 Springer Nature , pp.22261-22294 , 2023 .
View More
27	Mosarrat Jahan, Fatema Tuz Zohra, Md. Kamal Parvex, Upama Kabir, Abdul Mohaimen Al Radi and Shaily Kabir : An end-to-end authentication mechanism for wireless body area networks, Smart Health , vol.29 , no.100413 Elsevier , pp.1-16 , 2023 .
View More
28	Raihan Dewon Eman, Mosarrat Jahan and Upama Kabir : A multi-device user authentication mechanism for Internet of Things, IET Networks , vol.12 , no.5 John Wiley & Sons, Inc. , pp.1--21 , 2023 .
29	Sarder Iftekhar Ahmed, Muhammad Ibrahim, Md Nadim, Md Mizanur Rahman, Maria Mehjabin Shejunti, Taskeed Jabid and Md Sawkat Ali : MangoLeafBD: A Comprehensive Image Dataset to Classify Diseased and Healthy Mango Leaves, Data-in-Brief , vol.47 , no.4 Elsevier Inc. , pp.1-12 , 2023 .
View More
30	Afsana Mimi, Sayeda Fatema Tuj Zohura, Muhammad Ibrahim, Riddho Ridwanul Haque, Omar Farrok, Taskeed Jabid and Md Sawkat Ali : Identifying Selected Diseases of Leaves using Deep Learning and Transfer Learning Models, Machine Graphics and Vision , vol.32 , no.1 Institute of Information Technology, Warsaw University of Life Sciences, Poland , pp.55-71 , 2023 .
View More
31	Tashreef Muhammad, Anika Bintee Aftab, Muhammad Ibrahim, Md. Mainul Ahsan, Maishameem Meherin Muhu, Shahidul Islam Khan and Mohammad Shafiul Alam : Transformer-Based Deep Learning Model for Stock Price Prediction: A Case Study on Bangladesh Stock Market, International Journal of Computational Intelligence and Applications , vol.22 , no.1 World Scientific Publishing Europe Ltd. , pp.1-24 , 2023 .
View More
32	Anika Tahsin, Palash Roy, Md. Abdur Razzaque, Md. Mamun-Or-Rashid and MM Hassan : Energy Cooperation among Sustainable Base Stations in Multi-Operator Cellular Networks, IEEE Access (impact factor:3.9) , vol.11 IEEE , pp.19405-19417 , 2023 .
View More
33	Shaily Kabir, Christian Wagner and Zack Ellerby : Towards Handling Uncertainty-at-Source in AI – A Review and Next Steps for Interval Regression, IEEE Transactions on Artificial Intelligence IEEE , pp.1-19 , 2023 .
View More
34	Mohammad Kamrul Hasan, AKM Ahasan Habiba, Zarina Shukur, Fazil Ibrahim, Shayla Islam and Md. Abdur Razzaque : Review on cyber-physical and cyber-security system in smart grid: Standards, protocols, constraints, and recommendations, Journal of Network and Computer Applications (Elsevier) (impact factor:6.281) , 2022 .
View More
35	Nadia Motalib Laboni, Sadia Jahangir Safa, Selina Sharmin, Md. Abdur Razzaque, Md. Mustafizur Rahman and MM Hassan : A Hyper Heuristic Algorithm for Efficient Resource Allocation in 5G Mobile Edge Clouds, IEEE Transactions on Mobile Computing (impact factor:5.577) IEEE , 2022 .
36	Jesan Ahammed Ovi, Md. Ashraful Islam and Md. Rezaul Karim : BaNeP: An End-to-End Neural Network Based Model for Bangla Parts-of-Speech Tagging, IEEE Access (impact factor:3.367) , vol.10 IEEE , pp.102753-102769 , 2022 .
View More
37	M. Shahjalal, Nusrat Farhana, Palash Roy, Md. Abdur Razzaque, Kuljeet Kaur and MM Hassan : A Binary Gray Wolf Optimization algorithm for deployment of Virtual Network Functions in 5G hybrid cloud, Computer Communications (impact factor:3.167) , vol.193 , no.9 Elsevier , pp.63-74 , 2022 .
View More
38	Jesan Ahammed Ovi, Md Ashraful Islam and Md Rezaul Karim : BaNeP: An End-to-End Neural Network Based Model for Bangla Parts-of-Speech Tagging, IEEE Access IEEE , 2022 .
39	Md Tanvir Alam, Chowdhury Farhan Ahmed, Md Samiullah and Carson Kai-Sang Leung : Discovering Interesting Patterns from Hypergraphs, ACM Transactions on Knowledge Discovery from Data ACM New York, NY , 2022 .
View More
40	Ekram Hossain, Md. Rezaul Karim, Mir Hasan, Syeed Abrar Jaoad, Tauhid Tanjim and Md. Mosadek Khan : SPaFE : A Crowdsourcing and Multimodal Recommender System to Ensure Travel Safety in a City, IEEE Access (impact factor:3.367) , vol.10 IEEE , pp.12 , 2022 .
View More
41	Farhana Huq, Nahar Sultana, Sujan Sarker, Md. Abdur Razzaque and MM Hassan : Profit and Satisfaction Aware Order Assignment for Online Food Delivery Systems Exploiting Water Wave Optimization, IEEE Access (impact factor:3.476) , vol.10 IEEE , pp.71194-71208 , 2022 .
View More
42	Md Rabiul Haque, Mohammad Shariful Islam, Md Khalid Hasan, Md Salim Hossain, Muhammad Asif Hossain Khan and Farhin Islam : Determinants of anxiety and depression among Bangladeshi adults during COVID-19 lockdown: An online survey, Heliyon (impact factor:4) , vol.8 , no.5 Elsevier Ltd. , 2022 .
View More
43	Dewan Tariq Hasan, Md Mosaddek Khan, Muhammad Ibrahim and Ibrahem Almansour : On Evaluation of Patrolling and Signalling Schemes to Prevent Poaching in Green Security Games, Intelligent Systems with Applications , vol.14 , no.1 Elsevier B.V. , pp.1-15 , 2022 .
View More
44	Md Tanvir Alam, Amit Roy, Chowdhury Farhan Ahmed, Md Ashraful Islam and Carson K Leung : UGMINE: utility-based graph mining, Applied Intelligence , vol.53 , no.1 Springer , pp.49--68 , 2022 .
45	Jargis Ahmed, Md. Abdur Razzaque, Md. Mustafizur Rahman, Salman A. AlQahtani and MM Hassan : A Stackelberg Game-Based Dynamic Resource Allocation in Edge Federated 5G Network, IEEE Access (impact factor:3.476) , vol.10 IEEE , pp.10460-10471 , 2022 .
View More
46	Md. Ashraful Islam, Md Towhiduzzaman, Md Bhuiyan, Tauhidul Islam, Abdullah Al Maruf and Jesan Ahammed Ovi : BaNeL: an encoder-decoder based Bangla neural lemmatizer, SN Applied Sciences , vol.4 , no.5 Springer International Publishing , pp.1--15 , 2022 .
47	Md. Tanvir Alam, Amit Roy, Chowdhury Farhan Ahmed, Md. Ashraful Islam and Carson K. Leung : UGMINE: Utility Based Graph Mining, Applied Intelligence Springer , 2022 .
48	Muhammad Ibrahim : Evolution of Random Forest from Decision Tree and Bagging: A Bias- Variance Perspective, Dhaka University Journal of Applied Science and Engineering (DUJASE) , vol.7 , no.1 Faculty of Engineering and Technology, University of Dhaka, Bangladesh , pp.66-71 , 2022 .
View More
49	Md Tanvir Alam, Chowdhury Farhan Ahmed and Md Samiullah : A Vertex-extension based Algorithm for Frequent Pattern Mining from Graph Databases, Dhaka University Journal of Applied Science and Engineering , vol.7 , no.1 , pp.58--65 , 2022 .
50	Muhammad Ibrahim : Understanding Bias and Variance of Learning-to-Rank Algorithms: An Empirical Framework, Applied Artificial Intelligence (impact factor:2.78) , vol.36 , no.1 Taylor and Francis, UK , pp.1-34 , 2021 .
View More
51	Muhammad Ibrahim : Sampling Non-Relevant Documents of Training Sets for Learning-to-Rank Algorithms, International Journal of Machine Learning and Computing (Singapore) , vol.10 , no.3 , pp.406-415 , 2020 .
View More
52	M. W. Allvi, M. Hasan, L. Rayan, M. Shahabuddin, Md. Mosaddek Khan and Muhammad Ibrahim : Feature Selection for Learning-to-Rank using Simulated Annealing, International Journal of Advanced Computer Science and Applications (SCI and Scopus Indexed), SAI Publishers, UK , vol.11 , no.3 , pp.699-706 , 2020 .
View More
53	Muhammad Ibrahim : An Empirical Comparison of Random Forest-Based and Other Learning-to-Rank Algorithms, Pattern Analysis and Applications (Springer, Germany; part of Springer-Nature) (impact factor:2.31) , vol.23 , no.3 Springer Nature , pp.1133-1155 , 2020 .
View More
54	Md. Abdul Mannan Mondal and Mohammad Haider Ali : Self-Guided Stereo Correspondence Estimation Algorithm, International Journal of Image and Graphics, World Scientific Publishing Company, USA , vol.21 , 2020 .
View More
55	Shaily Kabir, Christian Wagner, Timothy C. Havens and Derek T. Anderson : A Similarity Measure Based on Bidirectional Subsethood for Intervals, IEEE Transactions on Fuzzy Systems (TFS) (impact factor:8.759) , 2020 .
View More
56	Md. Abdul Mannan Mondal and Mohammad Haider Ali : Disparity of Stereo Images by Self-Adaptive Algorithm, International Journal of Advanced Computer Science and Applications (IJACSA) , vol.11 , no.5 , pp.441-454 , 2020 .
View More
57	Md. Abdul Mannan Mondal and Mohammad Haider Ali : Stereo Correspondence Estimation by Two Dimensional Real Time Spiral Search Algorithm, International Journal of Engineering and Advanced Technology (IJEAT) , vol.9 , no.5 , pp.96-103 , 2020 .
View More
58	Muhammad Ibrahim : Reducing Correlation of Random Forest-Based Learning-to-Rank Algorithms Using Sub-Sample Size, Computational Intelligence (Wiley Publishers, USA) (impact factor:1.4) , vol.35 , no.4 Wiley Publishers, USA , pp.774-798 , 2019 .
View More
59	Maliha Momtaz, Abu Ahmed Ferdaus, Chowdhury Farhan Ahmed and Mohammad Samiullah : Maximal and closed frequent itemsets mining from uncertain database and data stream, International Journal of Data Science , vol.4 , no.3 Inderscience Publishers (IEL) , pp.237--259 , 2019 .
60	M. Momtaz, A.A. Ferdaus, C.F. Ahmed and M. Samiullah : Maximal and closed frequent itemsets mining from uncertain database and data stream, International Journal of Data Science , vol.4 , no.3 , pp.237-259 , 2019 .
61	Sadia Sharmin, Mohammad Shoyaib, Amin Ahsan Ali, Muhammad Asif Hossain Khan and Oksam Chae : Simultaneous Feature Selection and Discretization based on Mutual Information, Pattern Recognition (impact factor:3.965) , vol.91 , pp.162-174 , 2019 .
62	Tahira Alam, Chowdhury Farhan Ahmed, Sabit Anwar Zahin, Muhammad Asif Hossain Khan and Maliha Tashfia Islam : An Effective Recursive Technique for Multi-Class Classification and Regression for Imbalanced Data, IEEE Access (impact factor:4.098) , vol.7 , no.1 , pp.127615 - 127630 , 2019 .
63	Md Mahmudur Rahman, Chowdhury Farhan Ahmed and Carson Kai-Sang Leung : Mining weighted frequent sequences in uncertain databases, Information Sciences , vol.479 , pp.76-100 , 2019 .
View More
64	Muhammad Aminur Rahaman, Mahmood Jasim, Md Haider Ali and Md Hasanuzzaman : Bangla Language Modeling Algorithm for Automatic Recognition of Hand-Sign-Spelled Bangla Sign Language, Front. Comput. Sci., (Higher Education Press and Springer-Verlag GmbH Germany, part of Springer Nature, 2019) , vol.14 , no.3 , 2019 .
View More
65	Md Mahmudur Rahman, Chowdhury Farhan Ahmed and Carson Kai-Sang Leung : Mining weighted frequent sequences in uncertain databases., Information Sciences (impact factor:5.524) , vol.479 , no.April 2019 , pp.76-100 , 2019 .
View More
66	S Akther, MR Karim, Md Samiullah and CF Ahmed : Mining non-redundant closed flexible periodic patterns, Engineering Applications of Artificial Intelligence (Elsevier) (impact factor:4.201) , vol.69 , pp.1-23 , 2018 .
67	Md Mofijul Islam, Sanjay Saha, Md Mahmudur Rahman, Swakkhar Shatabda, Dewan Md Farid and Abdollah Dehzangi : iProtGly-SS: Identifying Protein Lysine Glycation Sites Using Sequence and Structure Based Features, Proteins Journal , 2018 .
View More
68	Mubin Ul Haque, Zarrin Tasnim Sworna, Hafiz Md Hasan Babu, and Ashis Kumar Biswas : A Fast FPGA-Based BCD Adder, Circuits, Systems, and Signal Processing, Springer, New York, United States , vol.37 , no.10 , pp.4384-4408 , 2018 .
View More
69	Minhas Kamal, Amin Ahsan Ali, Muhammad Asif Hossain Khan and Mohammad Shoyaib : Braille to Text Translation for Bengali Language: A Geometric Approach, JahangirNagar University Journal of Information Technology (JJIT) , pp.93-111 , 2018 .
70	Muhammad Asif Hossain Khan, Anindya Sundar Paul and Muhammad Jawad Iqbal : Printed Bangla Character Image Segmentation: A Font Invariant Approach, IUT Journal of Engineering and Technology (JET) , 2018 .
View More
71	Md. Ahsan Habib, Sajeeb Saha, Md. Abdur Razzaque, Md. Mamun-Or-Rashid, Giancarlo Fortino and Mohammad Mehedi Hassan : Starfish routing for sensor networks with mobile sink, Journal of Network and Computer Applications , vol.123 , pp.11-22 , 2018 .
72	Sayma Akther, Md. Rezaul Karim, Md. Samiullah and Chowdhury Farhan Ahmed : Mining non-redundant closed flexible periodic patterns, Journal of Engineering Applications of Artificial Intelligence (impact factor:3.526) , vol.69 , pp.1-23 , 2018 .
73	Maheen Islam, Md. Abdur Razzaque, Md. Mamun Or Rashid, Mohammad Mehedi Hasan and Abdulhameed Alelaiwi : Traffic Engineering in Cognitive Mesh Networks: Joint Link-Channel Selection and Power Allocation, Journal of Computer Communications , vol.116 , pp.212-224 , 2018 .
View More
74	Md Mofijul Islam, Sanjay Saha, Md Mahmudur Rahman, Swakkhar Shatabda, Dewan Md Farid and Abdollah Dehzangi : iProtGly‐SS: Identifying protein glycation sites using sequence and structure based features, Proteins: Structure, Function, and Bioinformatics , vol.86 , no.7 , pp.777-789 , 2018 .
View More
75	Muhammad Aminur Rahaman, Mahmood Jasim, Md Haider Ali, Tao Zhang and Md Hasanuzzaman : A real-time hand-signs segmentation and classification system using fuzzy rule based RGB model and grid-pattern analysis, Front. Comput. Sci., (Higher Education Press and Springer-Verlag GmbH Germany, part of Springer Nature) , vol.12 , no.6 , pp.1258-1260 , 2018 .
View More
76	Mosarrat Jahan, Suranga Seneviratne, Partha Sarathi Roy, Kouichi Sakurai, Aruna Seneviratne and Sanjay Jha : Light Weight and fine-grained Access Mechanism for Secure Access to Outsourced Data, Concurrency and Computation: Practice and Experience , 2018 .
77	Mosarrat Jahan, Mohsen Rezvani, Qianrui Zhao, Partha Sarathi Roy, Kouichi Sakurai, Aruna Seneviratne and Sanjay Jha : Light Weight Write Mechanism for Cloud Data, IEEE Transactions on Parallel and Distributed System , vol.29 , no.5 , pp.1131-1146 , 2018 .
78	Mubin Ul Haque, Zarrin Tasnim Sworna, Hafiz Md Hasan Babu, and Ashis Kumar Biswas. : A Fast FPGA-Based BCD Adder, Circuits, Systems, and Signal Processing, Springer, New York, United States , vol.37 , no.10 , pp.4384-4408 , 2018 .
79	Partha Protim Ghosh, Rezvi Shahariar and Muhammad Asif Hossain Khan : A Rule Based Extractive Text Summarization Technique for Bangla News Documents, International Journal of Modern Education and Computer Science (IJMECS) (impact factor:0.669 (2015)) , vol.10 , no.12 , pp.44-53 , 2018 .
80	Khalid Hussain, Shanto Rahman, Md. Mostafijur Rahman, Shah Mostafa Khaled, M. Abdullah-Al Wadud, Muhammad Asif Hossain Khan and Mohammad Shoyaib : Histogram Specification Technique for Dark Image Enhancement Using a Local Transformation Method, IPSJ Transactions on Computer Vision and Applications, (Springer Berlin Heidelberg) , vol.10 , no.3 , 2018 .
81	Sabit Anwar Zahin, Chowdhury Farhan Ahmed and Tahira Alam : An effective method for classification with missing values., Applied Intelligence (impact factor:2.882) , vol.48 , no.Number 1, January 2018 , pp.3209-3230 , 2018 .
View More
82	Sayma Akther, Md. Rezaul Karim, Md. Samiullah and Chowdhury Farhan Ahmed : Mining non-redundant closed flexible periodic patterns., Engineering Applications of Artificial Intelligence (impact factor:3.526) , vol.69 , no.March 2018 , pp.1-23 , 2018 .
View More
83	Md. Rezaul Karim, Michael Cochez, Oya Deniz Beyan, Chowdhury Farhan Ahmed and Stefan Decker : Mining maximal frequent patterns in transactional databases and dynamic data streams: A spark-based approach., Information Sciences (impact factor:5.524) , vol.432 , no.March 2018 , pp.278-300 , 2018 .
View More
84	AK Chanda, CF Ahmed, Md Samiullah and CK Leung : A new framework for mining weighted periodic patterns in time series databases, Expert System with Applications (impact factor:5.452) , vol.79 , pp.207-224 , 2017 .
85	S. Halder, Md Samiullah and Y-K Lee : Supergraph based periodic pattern mining in dynamic social networks, Expert System with Applications (Elsevier) (impact factor:5.452) , vol.72 , pp.430-442 , 2017 .
86	T. Hashem, M. R. Karim, Md Samiullah and C. F. Ahmed : An efficient dynamic superset bit-vector approach for mining frequent closed itemsets and their lattice structure, Expert System with Applications (impact factor:5.452) , vol.67 , pp.252-271 , 2017 .
87	M. M. Haque, Suraiya Pervin and Zerina Begum : An Innovative Approach of Bangla text summarization by introducing pronoun replacement and improved sentence ranking, Journal of Information Processing Systems , vol.13 , no.4 , 2017 .
88	Md. Haider Ali, Israt Rahman Sami, Mahzabeen Islam and Mohammad Shahiduzzaman : Mathematical Morphology Based Automated Control Point Detection from Human Facial Image, International Journal of Machine GRAPHICS and VISION (MGV), Institute of Fundamental Technological Research, Poland Academy of Science, Warsaw, Poland , vol.16 , no.1/2 , pp.153-170 , 2017 .
View More
89	Md Mofijul Islam, Md. Abdur Razzaque, Mohammad Mehedi Hassan, Walaa Nagy and Biao Song : Mobile Cloud-Based Big Healthcare Data Processing in Smart Cities, IEEE Access Journal , 2017 .
View More
90	Tahrima Hashem, Md. Rezaul Karim, Md. Samiullah and Chowdhury Farhan Ahmed : An efficient dynamic superset bit-vector approach for mining frequent closed item sets and their lattice structure, Journal of Expert Systems with Applications (impact factor:4.292) , vol.67 , pp.252-271 , 2017 .
91	Muhammad Aminur Rahaman, Mahmood Jasim, Md. Haider Ali and Md. Hasanuzzaman : A Real-Time Appearance-Based Bengali Alphabet and Numeral Signs Recognition System, Dhaka University Journal of Applied Science & Engineering , vol.4 , no.1 , pp.19-26 , 2017 .
92	Selina Sharmin, Fernaz Narin Nur, Md. Abdur Razzaque, Md. Mustafizur Rahman, A. Almogren and MM Hassan : Tradeoff Between Sensing Quality and Network Lifetime for Heterogeneous Target Coverage Using Directional Sensor Nodes, IEEE Access (impact factor:4.098 (2018)) , vol.5 , pp.15490 - 15504 , 2017 .
View More
93	Md. Abdul Mannan Mondal and Md. Haider Ali : Performance Review of the Stereo Matching Algorithms, American Journal of Computer Science and Information Engineering , vol.4 , no.1 , pp.7-17 , 2017 .
View More
94	Muntasir Wahid, M. Abid Naziri, Mohammad Shoyaib and Muhammad Asif Hossain Khan : Bangla Spell Checker: A Distance and Prior Probability based Approach, JahangirNagar University Journal of Information Technology (JJIT) , vol.6 , pp.87-108 , 2017 .
95	Tahrima Hashem, Md. Rezaul Karim, Md. Samiullah and Chowdhury Farhan Ahmed : An efficient dynamic superset bit-vector approach for mining frequent closed itemsets and their lattice structure., Expert Systems with Applications (impact factor:4.292) , vol.67 , no.January 2017 , pp.252-271 , 2017 .
View More
96	Ashis Kumar Chanda, Chowdhury Farhan Ahmed, Md. Samiullah and Carson K. Leung : A new framework for mining weighted periodic patterns in time series databases., Expert Systems with Applications (impact factor:4.292) , vol.79 , no.August 2017 , pp.207-224 , 2017 .
View More
97	Muhammad Ibrahim and Mark Carman : Comparing Pointwise and Listwise Objective Functions for Random Forest Based Learning-to-Rank, ACM Transactions on Information Systems (ACM, USA) (impact factor:2.3) , vol.34 , no.4 ACM, USA , pp.1-43 , 2016 .
View More
98	José Hernández-Orallo, Adolfo Martínez Usó, Ricardo B. C. Prudêncio, Meelis Kull, Peter A. Flach, Chowdhury Farhan Ahmed and Nicolas Lachiche : Reframing in context: A systematic approach for model reuse in machine learning., AI Communications (impact factor:0.765) , vol.29 , no.5 , pp.551-566 , 2016 .
View More
99	Md. Abdul Mannan Mondal and Md. Haider Ali : Disparity Estimation by a Real Time Approximation Algorithm, International Journal of Image Processing (IJIP) , vol.10 , no.3 , 2016 .
View More
100	Akiz Uddin Ahmed, Chowdhury Farhan Ahmed, Md. Samiullah, Nahim Adnan and Carson Kai-Sang Leung : Mining interesting patterns from uncertain databases., Information Sciences (impact factor:5.524) , vol.354 , no.1 August 2016 , pp.60-85 , 2016 .
View More
101	Tasnim Rahman, Hasnain Heickal, Shamira Tabrejee, Md Miraj Kobad Chowdhury, Sheikh Muhammad Sarwar and Mohammad Shoyaib : SeqDev: An Algorithm for Constructing Genetic Elements Using Comparative Assembly, Plant Tissue Culture and Biotechnology , vol.26 , no.1 , pp.105-121 , 2016 .
View More
102	A. U. Ahmed, CF Ahmed, Md Samiullah, N. Adnan and CKS LEUNG : Mining interesting patterns from uncertain databases, Information Sciences (Elsevier) (impact factor:5.524) , vol.354 , pp.60–85 , 2016 .
103	Zarrin Tasnim Sworna, Mubin Ul Haque, Nazma Tara, Hafiz Md Hasan Babu and Ashis Kumar Biswas : Low-power and area effcient binary coded decimal adder design using a look up table-based eld programmable gate array, IET Circuits,Devices & Systems (United Kingdom) , vol.10 , no.3 , pp.1-10 , 2016 .
View More
104	Md. Rezaul Karim, Md. Jawaherul Alam and Md. Saidur Rahman : On some properties of doughnut graphs, AKCE International Journal of Graph Algorithms and Combinatorics , vol.13 , no.2 , pp.130-139 , 2016 .
105	Zarrin Tasnim Sworna, Mubin Ul Haque, Nazma Tara, Hafiz Md Hasan Babu and Ashis Kumar Biswas : Low-power and area effcient binary coded decimal adder design using a look up table-based eld programmable gate array, IET Circuits,Devices & Systems (United Kingdom) , vol.10 , no.3 , pp.163-172 , 2016 .
106	Maheen Islam, Md. Abdur Razzaque, Md. Mamun Or Rashid, Mohammad Mehedi Hasan, Ahmad Almogren and Abdulhameed Alelaiwi : Dynamic traffic engineering for high-throughput data forwarding in wireless mesh networks, Elsevier Journal of Computers and Electrical Engineering , vol.56 , pp.130-144 , 2016 .
107	Umme Hafsa Billah and Muhammad Asif Hossain Khan : A Systematic Literature Review on Segmentation and Recognition of Printed Bangla Characters, IUT Journal of Engineering and Technology (JET) , vol.13 , no.1 , pp.1-8 , 2016 .
View More
108	Ashin Ara Bithi and Abu Ahmed Ferdaus : Mining Sequential Patterns from mFUSP-Tree, Int. J. Inf. Technol. Comput. Sci.(IJITCS) , vol.7 , no.7 , pp.77--89 , 2015 .
109	Ashis Kumar Chanda, Swapnil Saha, Manziba Akanda Nishi, Md. Samiullah and Chowdhury Farhan Ahmed : An efficient approach to mine flexible periodic patterns in time series databases., Engineering Applications of Artificial Intelligence (impact factor:3.526) , vol.44 , no.September 2015 , pp.46-63 , 2015 .
View More
110	Anna Fariha, C. F. Ahmed, C. K. Leung, Md. Samiullah and Suraiya Pervin : A new framework for mining frequent interaction patterns gor meeting databases, Engineering Applications of Artificial Intelligence , vol.45 , pp.103-118 , 2015 .
111	Anna Fariha, Chowdhury Farhan Ahmed, Carson K. Leung, Md. Samiullah, Suraiya Pervin and Longbing Cao : A new framework for mining frequent interaction patterns from meeting databases., Engineering Applications of Artificial Intelligence (impact factor:3.526) , vol.45 , no.October 2015 , pp.103-118 , 2015 .
View More
112	Chowdhury Farhan Ahmed, Nicolas Lachiche, Clément Charnay, Soufiane El Jelali and Agnès Braud : Flexible propositionalization of continuous attributes in relational data mining., Expert Systems with Applications (impact factor:4.292) , vol.42 , no.Number 1, January 2015 , pp.7698-7709 , 2015 .
View More
113	A. Fariha, C. F. Ahmed, CKS Leung, M. Samiullah, S. Pervin and L Cao : A New Framework for Mining Frequent Interaction Patterns from Meeting Databases, Engineering Applications of Artificial Intelligence (Elsevier) (impact factor:4.201) , vol.45 , pp.103–118 , 2015 .
114	A K Chanda, S Saha, M A Nishi, Md. Samiullah and C F Ahmed : An efficient approach to mine flexible periodic patterns in time series databases, Engineering Applications of Artificial Intelligence (Elsevier) (impact factor:4.201) , vol.44 , pp.44–63 , 2015 .
115	Md Mofijul Islam, Md. Ahasanuzzaman, Md. Abdur Razzaque, M. M. Hassan, Abdulhameed Alelaiwi and Yang Xian : Target coverage through distributed clustering in directional sensor networks, EURASIP J. Wireless Communications and Networking , 2015 .
View More
116	Rasel Kabir, Shaily Kabir and M. Shamiul Amin : Isolating Informative Blocks from Large Web Pages Using HTML Tag Priority Assignment Based Approach, International Journal of Electrical & Computer Engineering (ISSN 2088-8708) , vol.4 , no.3 , pp.61-72 , 2015 .
117	M. Shamiul Amin, Shaily Kabir and Rasel kabir : A Score based Web Page Ranking Algorithm, International Journal of Computer Applications (ISSN 0975-8887) , vol.110 , no.12 , pp.11-15 , 2015 .
118	Salma-Tuz Jakirin, Abu Ahmed Ferdaus and Mehnaj Afrin Khan : A Genetic Algorithm Approach using Improved Fitness Function for Classification Rule Mining, International Journal of Computer Applications , vol.97 , no.23 Foundation of Computer Science , pp.12--18 , 2014 .
119	Ashin Ara Bithi, Tareq Shahriar and Abu Ahmed Ferdaus : Incremental Sequential Pattern Tree Mining, IOSR Journal of Computer Engineering (IOSR-JCE) , vol.16 , no.1 , pp.110--116 , 2014 .
120	Manira Akhter, Ashin Ara Bithi and Abu Ahmed Ferdaus : Mining Web Access Patterns using Root-set of Suffix Trees, International Journal of Computer Applications , vol.94 , no.9 Foundation of Computer Science , 2014 .
121	Md Samiullah, CF Ahmed, A Fariha, MR Islam and N. Lachiche : Mining frequent correlated graphs with a new measure, Expert Systems with Applications (Elsevier) (impact factor:5.452) , vol.41 , pp.1847–1863 , 2014 .
122	T. Hashem, CF Ahmed, M. Samiullah, S Akther, BS Jeong and S Jeon : An efficient approach for mining cross-level closed itemsets and minimal association rules using closed itemset lattices, Expert Systems with Applications (Elsevier) (impact factor:5.452) , vol.41 , pp.2914–2938 , 2014 .
123	Md. Samiullah, Chowdhury Farhan Ahmed, Anna Fariha, Md. Rafiqul Islam and Nicolas Lachiche : Mining frequent correlated graphs with a new measure., Expert Systems with Applications (impact factor:4.292) , vol.41 , no.Number 1, January 2014 , pp.1847-1863 , 2014 .
View More
124	Tahrima Hashem, Chowdhury Farhan Ahmed, Md. Samiullah, Sayma Akther, Byeong-Soo Jeong and Seokhee Jeon : An efficient approach for mining cross-level closed itemsets and minimal association rules using closed itemset lattices., Expert Systems with Applications (impact factor:4.292) , vol.41 , no.Number 1, January 2014 , pp.2914-2938 , 2014 .
View More
125	Shihab Rahman, Dolon Chapa and Shaily Kabir : A New Weighted Keyword Based Similarity Measure for Clustering Webpages, International Journal of Computer and Information Technology (ISSN 2279-0764) , vol.3 , no.5 , pp.929-933 , 2014 .
126	Rifatul Islam, Umama Tasnim, Mosarrat Jahan and Shaily Kabir : Modified Centralized Set Cover based Approximation(CSCA) for Duty-Cycled Wireless Sensor Networks, IRACST – International Journal of Computer Networks and Wireless Communications (IJCNWC) , vol.4 , no.2 , pp.150-156 , 2014 .
127	Md. Sajidul Islam, Imtiaz Rahim and Mosarrat Jahan : An Energy-Efficient Data Aggregation Tree Construction Algorithm for Wireless Sensor Networks, IRACST – International Journal of Computer Networks and Wireless Communications (IJCNWC) , vol.4 , no.5 , pp.264-269 , 2014 .
128	Rifatul Islam, Umama Tasnim, Mosarrat Jahan and Shaily Kabir : Modiﬁed Centralized Set Cover based Approximation (CSCA) for Duty-Cycled Wireless Sensor Networks, International Journal of Computer Networks and Wireless Communications (ISSN 2076-0930) , vol.4 , no.2 , pp.150-156 , 2014 .
129	Shahnila Zaman, Sabiha Salma and Shaily Kabir : Eﬃcient Grouping of Tourism Webpages Considering Ratings and Reviews, International Journal of Computer Science, Information Technology, and Security (ISSN 2249-9555) , vol.4 , no.3 , pp.55-60 , 2014 .
130	Maheen Islam, M. Lutfar Rahman and Md. Mamun Or Rashid : Traffic Priority Based Adaptive and Responsive Congestion and Rate Control for Wireless Mesh Networks, Journal of Computer and Information Science , vol.7 , no.2 , pp.99-116 , 2014 .
131	Maeen Islam, M. Lutfar Rahman and Md. Mamun Or Rashid : An Efficient Traffic- Load and Link-Interference Aware Routing Metric for Multi Radio Multi Channel Wireless Mesh Networks Based on Link's Effective Capacity Estimation, Journal of Computer and Information Science (impact factor:wireless mesh networks, routing metric, interference domain, congestion degree, link load) , vol.7 , no.4 , pp.129-142 , 2014 .
132	Ashin Ara Bithi and Abu Ahmed Ferdaus : Sequential Pattern Tree Mining, IOSR Journal of Computer Engineering (IOSR-JCE) , vol.15 , no.5 , pp.79--89 , 2013 .
133	Emon Kumar Dey, Mohsin Khan and Md. Haider Ali : Computer Vision-Based Gender Detection from Facial Image, International Journal of Advanced Computer Science , vol.3 , no.8 , pp.428-433 , 2013 .
View More
134	Sheikh Mohammad Sarwar, Md. Mustafizur Rahman, Md. Haider Ali and Ashique Mahmood Adnan : A Scalable Image Snippet Extraction Framework for Integration with Search Engines, Computer and Information Science (Published by Canadian Center of Science and Education) , vol.6 , no.1 , pp.89-99 , 2013 .
View More
135	M. M. Haque, Suraiya Pervin and Zerina Begum : Literature review of automatic single documents text summarization using NLP, International Journal of Innovation and Applied Studies , vol.3 , no.3 , pp.857-865 , 2013 .
136	M. A. Nishi, C. F. Ahmed, Md Samiullah and B. S. Jeong : Effective periodic pattern mining in time series databases, Expert Systems with Applications (Elsevier) (impact factor:5.452) , vol.40 , pp.3015–3027 , 2013 .
137	Manziba Akanda Nishi, Chowdhury Farhan Ahmed, Md. Samiullah and Byeong-Soo Jeong : Effective periodic pattern mining in time series databases., Expert Systems with Applications (impact factor:4.292) , vol.40 , no.Number 1, January 2013 , pp.3015-3027 , 2013 .
View More
138	Md. Manzurul Hasan, Md. Saidur Rahman and Md. Rezaul Karm : Box-rectangular drawing of planar graphs, Journal of Graph Algorithms and Applications. , vol.17 , no.6 , pp.629-646 , 2013 .
139	M Haque, Suraiya Pervin and Zerina Begum : Literature review of automatic multiple documents text summarization, International Journal of Innovation and Applied Studies , vol.3 , no.1 , pp.121-129 , 2013 .
140	Muhammad Asif Hossain Khan, Danushka Bollegala, Guangwen Li and Kaoru Sezaki : Delineating Real-Time Events by Identifying Relevant Tweets with Popular Discussion Points, ASE Human Journal , vol.2 , no.3 , pp.136-150 , 2013 .
141	Muhammad Asif Hossain Khan, Masayuki Iwai and Kaoru Sezaki : An Improved Classification Strategy for Filtering Relevant Tweets Using Bag-of-Word Classifiers, Journal of Information Processing , vol.21 , no.3 , pp.507-516 , 2013 .
142	Md. Ashrafuddin and Md. Mamun Or Rashid : Energy Efficient Fitness based Routing Protocol for Underwater Sensor Network, International Journal of Intelligent Systems and Applications (IJISA) , vol.6 , pp.61-69 , 2013 .
143	Ashin Ara Bithi, Manira Akhter and Abu Ahmed Ferdaus : Tree Based Sequential Pattern Mining, IRACST-International Journal of Computer Science and Information Technology & Security (IJCSITS), ISSN , vol.2 , no.6 , pp.2249--9555 , 2012 .
144	Muhammad Ibrahim, Nasimul Noman and Hitoshi Iba : Finding perfect and imperfect biclusters from gene expression data: A Heuristic and a meta-heuristic approach, International Journal of Applied Chemistry (SCOPUS Indexed) , vol.8 , no.3 , pp.225-242 , 2012 .
View More
145	Shabbir Ahmed and Salil S. Kanhere : On the Characterization of Vehicular Mobility in a Large-Scale Public Transport Network, International Journal of Ad Hoc and Ubiquitous Computing (IJAHUC) , vol.11 , no.2/3 Inderscience Publisher , pp.68-81 , 2012 .
146	Muhammad Ibrahim and Ahsan Raja Chowdhury : An Improved Heuristic Algorithm to Minimize Complete Test Set of K-CNOT Circuits for Single and Multiple Stuck-at Fault Model, Journal of Computing , vol.4 , no.2 , pp.137-146 , 2012 .
147	Md. Safiuddin Sheikh and Md. Haider Ali : Straight Polygon Simplification of 3D Graphical Models, International Journal of Pure and Applied Sciences and Technology , vol.13 , no.2 , pp.26-31 , 2012 .
View More
148	Nurul Ahad Tawhid, Nasir Uddin Laskar and Md. Haider Ali : A Vision-based Facial Expression Recognition and Adaptation System from Video Stream, International Journal of Machine Learning and Computing , vol.2 , no.5 , pp.535-539 , 2012 .
View More
149	Shuvra Chakraborty and Md. Haider Ali : Iris Texture Recognition with DCT Compression for Small Scale System, Journal of Computing , vol.4 , no.11 , pp.20-27 , 2012 .
View More
150	Md. Aktaruzzaman, Bulbul Ahmed and Md. Haider Ali : Rotation Invariant Object Detection Using Circular Features, Jahangirnagar University Journal of Science , vol.35 , no.1 , pp.23-39 , 2012 .
151	Chowdhury Farhan Ahmed, Syed Khairuzzaman Tanbeer, Byeong-Soo Jeong, Young-Koo Lee and Ho-Jin Choi : Single-pass incremental and interactive mining for weighted frequent patterns., Expert Systems with Applications (impact factor:4.292) , vol.39 , no.Number 1, January 2012 , pp.7976-7994 , 2012 .
View More
152	Chowdhury Farhan Ahmed, Syed Khairuzzaman Tanbeer, Byeong-Soo Jeong and Ho-Jin Choi : Interactive mining of high utility patterns over data streams., Expert Systems with Applications (impact factor:4.292) , vol.39 , no.Number 1, January 2012 , pp.11979-11991 , 2012 .
View More
153	Shabbir Ahmed and Salil S. Kanhere : HUBCODE: hub-based forwarding using network coding in delay tolerant networks, The Journal of Wireless Communications and Mobile Computing John Wiley & Sons, Ltd. , 2011 .
154	A S Md. Mokarrom Hossain, Shaily Kabir and Md. Haider Ali : Video Conferencing over Very Narrow Band Internet Using Image Metamorphosis, Dhaka University Journal of Applied Science & Engineering, University of Dhaka , vol.1 , no.2 , pp.147-150 , 2011 .
155	Imran Ahmed, S. Sadeque and Suraiya Pervin : Margin adaptivre resource allocation for multiuser OFDM systems by particle swarm optimization and differential evolution, International Journal of Engineering And Technology , 2011 .
156	Chowdhury Farhan Ahmed, Syed Khairuzzaman Tanbeer, Byeong-Soo Jeong and Young-Koo Lee : HUC-Prune: an efficient candidate pruning technique to mine high utility patterns., Applied Intelligence (impact factor:2.882) , vol.34 , no.Number 1, February 2011 , pp.181-198 , 2011 .
View More
157	Chowdhury Farhan Ahmed, Syed Khairuzzaman Tanbeer, Byeong-Soo Jeong and Ho-Jin Choi : A framework for mining interesting high utility patterns with a strong frequency affinity., Information Sciences (impact factor:5.524) , vol.181 , no.Number 1, January 2011 , pp.4878-4894 , 2011 .
View More
158	Md. Rezaul Karm, Md. Jawaherul Alam and Md. Saidur Rahman : Straight-line grid drawings of label-constrained outerplanar graphs with O(n logn) area, Journal of Graph Algorithms and Applications, , vol.15 , no.3 , pp.437-456 , 2011 .
159	S. Md. Mukarram Hossain, Shaily Kabir and Md. Haider Ali : Video Conferencing Over Very Narrow Band Internet Using Image Metamorphosis, Dhaka University Journal of Applied Science & Engineering (ISSN 2218-7413) , vol.1 , no.2 , pp.147-150 , 2011 .
160	Faisal Sikder and Abu Ahmed Ferdaus : Data Mining Based Motif Detection in Biological Sequences, Dhaka University Journal of Engineering & Technlogy , vol.1 , no.1 , pp.45-49 , 2010 .
161	Computer Engineering, Dhaka, Bangladesh Nazia Zaman, Kazi Chandrima Rahman, Syed Faisal Hasan : Explicit Rate-based Congestion Control for Multimedia Streaming over Mobile Ad hoc Networks,, international Journal of Electrical and Computer Sciences (IJECS-IJENS) , vol.10 , no.4 , 2010 .
162	Md. Mustafizur RAHMAN, Choong Seon HONG, Sungwon LEE, JangYeon LEE and Jin Woong CHO : IP-MAC: A Distributed MAC for Spatial Reuse in Wireless Networks, IEICE Transaction on Communications (impact factor:1.090 (2017)) , vol.E93.B (2010) , no.6 , pp.1534-1546 , 2010 .
View More
163	Md. Jawaherul Alam, Mashfiqui Rabbi, Md. Saidur Rahman and Md. Rezaul Karim : Upright drawings of graphs on three layers, Journal of Applied Mathematics and Informatics , vol.28 , no.5-6 , pp.1347-1358 , 2010 .
164	Md. Mustafizur Rahman, Choong Seon Hong and Sungwon Lee : A High Throughput On-Demand Routing Protocol for Multirate Ad Hoc Wireless Networks, IEICE TRANSACTIONS on Communications (impact factor:1.09 (2017)) , vol.E93-B , no.1 , pp.29 - 39 , 2010 .
View More
165	Mosarrat Jahan, Shaily Kabir and Mohammad Asif Hossain Khan : A Modified Approach to Improve the Performance of Lazy Release Consistency (LRC) Model, The Dhaka University Journal of Science , vol.58 , no.1 , pp.49-53 , 2010 .
166	Ahmedul Kabir and Shaily Kabir : Human Facial Expression Recognition Using Region based Motion Estimation, Dhaka University Journal of Science (ISSN 24088528) , vol.58 , no.2 , pp.175-182 , 2010 .
167	Mosarrat Jahan, Shaily Kabir and Mohammad Asif Hossain Khan : A Modiﬁed Approach to Improve the Performance of Lazy Release Consistency (LRC) Model, Dhaka University Journal of Science (ISSN 2408-8528) , vol.58 , no.1 , pp.49-55 , 2010 .
168	Md. Saiful Islam and Md. Haider Ali : A Miniature-Based Image Retrieval System, Dhaka University Journal of Science, University of Dhaka , vol.57 , no.2 , pp.187-191 , 2009 .
169	Md. Alamgir Hossain and Md. Haider Ali : Three-Dimensional Shape Reconstruction in Medical Imaging, Dhaka University Journal of Science, University of Dhaka , vol.57 , no.1 , pp.7-10 , 2009 .
170	Chowdhury Farhan Ahmed, Syed Khairuzzaman Tanbeer, Byeong-Soo Jeong and Young-Koo Lee : An Efficient Algorithm for Sliding Window-Based Weighted Frequent Pattern Mining over Data Streams., IEICE Transactions (impact factor:0.63) , vol.92-D , no.Number 1, January 2009 , pp.1369-1381 , 2009 .
View More
171	Syed Khairuzzaman Tanbeer, Chowdhury Farhan Ahmed, Byeong-Soo Jeong and Young-Koo Lee : Efficient single-pass frequent pattern mining using a prefix-tree., Information Sciences (impact factor:5.524) , vol.179 , no.Numbers 1-2, January 2009 , pp.559-583 , 2009 .
View More
172	Syed Khairuzzaman Tanbeer, Chowdhury Farhan Ahmed, Byeong-Soo Jeong and Young-Koo Lee : Sliding window-based frequent pattern mining over data streams., Information Sciences (impact factor:5.524) , vol.179 , no.Numbers 1-2, January 2009 , pp.3843-3865 , 2009 .
View More
173	Chowdhury Farhan Ahmed, Syed Khairuzzaman Tanbeer, Byeong-Soo Jeong and Young-Koo Lee : Efficient Tree Structures for High Utility Pattern Mining in Incremental Databases., IEEE Transactions on Knowledge and Data Engineering (impact factor:2.775) , vol.21 , no.Number 1, January 2009 , pp.1708-1721 , 2009 .
View More
174	Md. Rezaul Karim and Md. Saidur Rahman : On a class of planar graphs with straight-line grid drawing with linear area, Journal of Graph Algorithms and Applications , vol.13 , no.2 , pp.153-177 , 2009 .
175	Md. Rezaul Karim, Md. Nahiduzzaman and Md. Saidur Rahman : A linear-lime algorithm for k-partitioning doughnut graphs, INFOCOMP- Journal of Computer Science , vol.8(1) , pp.8-13 , 2009 .
176	Kamrul Abedin Tarafder, Shah Mostafa Khaled, Mohammad Ashraful Islam, Khandakar Rafiqual Islam, Hasnain Feroze, Mohammad Khalaquzzaman and Abu Ahmed Ferdaus : Reverse Apriori Algorithm for Frequent Pattern Mining, Asian Journal of Information Technology , vol.7 , no.12 , pp.524--530 , 2008 .
177	Shaily Kabir and Md. Haider Ali : A Heuristic Approach of Establishing the Relationship between Full Width Half Maximum (FWHM) and Human Facial Shape Distortion in Image Metamorphosis, Dhaka University Journal of Science, University of Dhaka , vol.56 , no.1 , pp.51-56 , 2008 .
178	Md. Haider Ali : Optimized Camera Positioning Technique in Human Facial Texture Mapping, Dhaka University Journal of Science, University of Dhaka , vol.56 , no.1 , pp.39-44 , 2008 .
179	Syed Khairuzzaman Tanbeer, Chowdhury Farhan Ahmed, Byeong-Soo Jeong and Young-Koo Lee : Mining Regular Patterns in Transactional Databases., IEICE Transactions (impact factor:0.63) , vol.91-D , no.Number 1, January 2008 , pp.2568-2577 , 2008 .
View More
180	Chowdhury Farhan Ahmed, Syed Khairuzzaman Tanbeer, Byeong-Soo Jeong and Young-Koo Lee : Handling Dynamic Weights in Weighted Frequent Pattern Mining., IEICE Transactions (impact factor:0.63) , vol.91-D , no.Number 1, January 2008 , pp.2578-2588 , 2008 .
View More
181	Shah Mostafa Khaled, Md. Rezaul Karim and Md. Akhtaruzzaman : Security system based on embedded internet control,, Dhaka University Journal of Science , vol.56 , no.2 , pp.147-152 , 2008 .
182	Suraiya Pervin and Subrata Kr. Aditya : A Pipelined Architecture for Computing Eigenvectors, Dhaka University Journal of Science , vol.56 , no.1 , pp.17-22 , 2008 .
183	Shaily Kabir and Md. Haider Ali : A Heuristic Approach of Establishing the Relationship between Full Width Half Maximum (FWHM) and Human Facial Shape Distortion in Image Metamorphosis, Dhaka University Journal of Science (ISSN 2408-8528) , vol.56 , no.1 , pp.51-54 , 2008 .
184	Pushpita Nomani Tumpi, Wahid Raihanur Rahman and Md. Haider Ali : An Efficient Facial Expression Detection System, International Journal of Machine GRAPHICS and VISION (MGV), Institute of Fundamental Technological Research, Poland Academy of Science, Warsaw, Poland , vol.16 , no.3/4 , pp.377-399 , 2007 .
View More
185	Md. Saiful Islam and Md. Haider Ali : Content Based Image Indexing for Sub-Image Retrieval, Journal of Computer Science, Faculty of Computer Science, IBAIS University of Bangladesh , vol.1 , no.2 , pp.67-76 , 2007 .
186	S.M. Ashraful Kadir, Tazrian Khan and Md. Haider Ali : Human Facial Soft-Tissue Modeling using Finite Element Method, Dhaka University Journal of Science, University of Dhaka , vol.55 , no.2 , pp.237-242 , 2007 .
187	Syed Monowar Hossain and Md. Haider Ali : A Hybrid Method of Data Hiding into Digital Images, Dhaka University Journal of Science, University of Dhaka , vol.55 , no.2 , pp.203-210 , 2007 .
188	Muhammad Asif Hossain Khan, Mohammad Shafkat Amin, Mohammed Shafiul Alam Khan and Fahima Amin Bhuyan : AFS: An improved file system with reduced file storage overhead, The Dhaka University Journal of Science , vol.55 , pp.43-51 , 2007 .
189	Rony Hasinur Rahman, Nusrat Nowsheen, Mahbubul Azam Khan and Muhammad Asif Hossain Khan : Wireless LAN Security: An In-Depth Study of the Threats and Vulnerabilities, Asian Journal of Information and Technology , vol.6 , no.4 , pp.441-446 , 2007 .
190	Muhammad Asif Hossain Khan, Shah Mustafa Khaled, Md. Touhidul Islam and Md. Sanaul Karim : Extending Mobile Phone SMS Capacity into Email, The Dhaka University Journal of Science , vol.55 , no.2 , pp.167 – 170 , 2007 .
191	Rony Hasinur Rahman, Nusrat Nowsheen, Mahbubul Azam Khan and Muhammad Asif Hossain Khan : Locating Mobile Phones on a City Map Using SMS Technology, The Dhaka University Journal of Science , vol.55 , no.2 , pp.211 – 213 , 2007 .
192	Suraiya Pervin : A Hyperbolic Formulation of the LMS Algorithm., The Dhaka University Journal of Science. , vol.55 , no.1 , pp.71-74 , 2007 .
193	Suraiya Pervin, and Subta Kr. Aditya : A Pipelined Architecture to Compute Eigenvalues of Data Covariance Matrix., The Dhaka University Journal of Science. , vol.55 , no.1 , pp.75-79 , 2007 .
194	Shah Mostafa Khaled, Md. Rezaul Karim, Ashis Kumer Biswas and M. A. Qayum : Optimization of reliability in a real time security system controlled by embedded internet technology, Asian Journal of Information Technology , vol.6 , no.10 , pp.1050-1056 , 2007 .
195	Hafiz Md. Hasan Babu, Md. Rafiqul Islam, Mosarrat Jahan and Mohammad Abdullah-Al-Wadud : A Heuristic Approach to Minimize the Multiple-Output Functions, The Dhaka University Journal of Science , vol.54 , no.5 , pp.7-10 , 2006 .
196	Meher Nigar, Md. Mahmudul Hasan, Rashed Mazumder and Suraiya Pervin : Computation of DFT using CORDIC algorithm., The Journal of the Bangladesh Electronics Society. 6(2): 33-40 (2006) , vol.6 , no.2 , pp.33-40 , 2006 .
197	Suraiya Pervin and Subrata Kumar Aditya : Cordic Realization of the Karhunen-Loeve Transform Based LMS Adaptive Equalizer., The Dhaka University Journal of Science. , vol.54 , no.1 , pp.39-42 , 2006 .
198	Shabbir Ahmed and Farzana Mithun : An Improved Way to Retrieve Emails on Slow Communication Links, Dhaka University Journal of Science , vol.52 , no.3 Dhaka University , pp.281-286 , 2005 .
199	Shabbir Ahmed and Farzana Mithun : Modifying RED Packet Drop/Mark Probability Function For Improved Performance, Dhaka University Journal of Science , vol.53 , no.2 Dhaka University , pp.95-102 , 2005 .
200	Muhammad Asif Hossain Khan, Md. Minhajul Abedin and Quazi Ashfaqur Rahman : An Efficient Huffman Encoding and Decoding Algorithm Using Improved Header Compression, Jahangir Nagar Physics Studies , vol.11 , pp.39-48 , 2005 .
201	Suraiya Pervin and Subrata Kr. Aditya : An Area Efficient Adaptive Equalizer., Journal of Bangladesh Electronics Society. , vol.5 , no.2 , pp.45-50 , 2005 .
202	Suraiya Pervin and Subrata Kr. Aditya : A Cordic Realization of the Complex LMS Based Adaptive Equalizer., The Dhaka University Journal of Science. , vol.53 , no.2 , pp.25-32 , 2005 .
203	M. Shamim Kaiser, Suraiya Pervin, S. K. Aditya and R. K. Mazumder : A Predictive Digital Filter based Zero Crossing Detection Technique for PV Inverter., Journal of Bangladesh Electronics Society. , vol.5 , no.1 , pp.127-130 , 2005 .
204	Suraiya Pervin, Taslim Taher and Tariqul Islam : CORDIC Realization of the ADFE., Journal of Bangladesh Electronics Society. , vol.5 , no.1 , pp.49-54 , 2005 .
205	Suraiya Pervin,, Kaniz Fatema and Nasrin Akhter : A Time Efficient Architecture for the CTLMS based Adaptive Equalizer., Journal of Bangladesh Electronics Society , vol.5 , no.1 , pp.9-16 , 2005 .
206	Shabbir Ahmed and Farzana Mithun : Modified Huffman Compression algorithm for improved reliability, Dhaka University Journal of Science , vol.52 , no.2 Dhaka University , pp.125-131 , 2004 .
207	Shabbir Ahmed and Farzana Mithun : Word Stemming Technique against SPAM, Journal of PUB , vol.1 , no.1 , pp.120-126 , 2004 .
208	S. K. Aditya, D. Das and Suraiya Pervin : Load Frequency Controller Design of Multi-Turbine Generator System Using Genetic Algorithm., Journal of Bangladesh Electronics Society. , vol.4 , no.1 , pp.34-39 , 2004 .
209	Suraiya Pervin and Subrata Kumar Aditya : A Real Time Architecture for KLT Based Adaptive Equalizer., The Dhaka University Journal of Science. , vol.52 , no.2 , pp.207-213 , 2004 .
210	Muhammad Asif Hossain Khan and Mosaddek Hossain Kamal : FLRC: An Improved Cache Coherence Protocol for Software DSM, The Dhaka University Journal of Science , vol.52 , no.2 , pp.133-140 , 2004 .
211	Suraiya Pervin and Subrata K. Aditya : A Latency Free Pipelined Architecture of VSLMS based Equalizer, The Dhaka University Journal of Science. 52(3): 309-316 , vol.52 , no.3 , pp.309-316 , 2004 .
212	Shabbir Ahmed and Farzana Mithun : Binary Tree Structure – A Novel Interconnection Structure for Distributed Matrix Multiplication, Dhaka University Journal of Science, , vol.51 , no.1 , pp.127-133 , 2003 .
213	Suraiya Pervin and M. Chakroborty : Pipelining the Adaptive Decision Feedback Equalizer., International Journal of Signal Processing, Elseviar. 83: 2675–2681 (2003) , vol.83 , pp.2675-2681 , 2003 .
214	Suraiya Pervin and Subrata Kumar Aditya : A Very High Throughput Architecture for the Trigonometric LMS Based Adaptive Equalizer, The Dhaka University Journal of Science. , vol.51 , no.2 , pp.221-226 , 2003 .
215	Suraiya Pervin and Subrata Kumar Aditya : A Hardware Efficient Systolic Architecture for Adaptive Decision Feedback Equalizer., The Dhaka University Journal of Science. , vol.51 , no.1 , pp.117-125 , 2003 .
216	Suraiya Pervin and S. K. Aditya : A Pipelined Architecture for Updating Normalized Covariance Matrix in Real Time Signal Processing., The Dhaka University Journal of Science. , vol.51 , no.1 , pp.109-115 , 2003 .
217	Md. Mamun-or-Rashid and Md. Rezaul Karim : Predictive item pruning FP-Tree algorithm, Dhaka University Journal of Science , vol.52 , no.1 , pp.39-43 , 2003 .
218	Lutful Karim and Md. Rezaul Karim : , Reliability, Availability, and Serviceability (RAS) enhancement of supercomputers, especially in RS/6000 SP, Dhaka University Journal of Science, , vol.51 , no.1 , pp.59-65 , 2003 .
219	Md. Rafiqul Islam and Md. Rezaul Karim : Improved techniques for query optimization using eliminating duplicates generated in transformation-based join enumeration, Dhaka University Journal of Science , vol.51 , no.1 , pp.67-75 , 2003 .
220	Shaily Kabir, Mahmud Karim and Haﬁz Md. Hasan Babu : The Use of Optimal Ordering of Input Variables for Simpliﬁcation of Single Output Logic Functions, Dhaka University Journal of Science (ISSN 2408-8528) , vol.51 , no.1 , pp.101-108 , 2003 .
221	Lutful Karim and Md. Rezaul Karim : Complexity analysis of symmetrical multiprocessor and multi-purpose parallel computers, Dhaka University Journal of Science , vol.51 , no.1 , pp.51-57 , 2003 .
222	Md. Haider Ali and Toyohisa Kaneko : Automated 3D-2D Projective Registration of Human Facial Images Using Edge Features, International Journal of Pattern Recognition and Artificial Intelligence (IJPRAI), World Scientific Publishing Company, USA , vol.15 , no.8 , pp.1203-1276 , 2001 .
View More
223	Md. Haider Ali and Toyohisa Kaneko : Reconstruction of Human Hair Shape from Video Captured Images and CT Data, International Journal of Machine GRAPHICS and VISION, Institute of Fundamental Technological Research, Poland Academy of Science, Warsaw, Poland , vol.10 , no.1 , pp.3-14 , 2001 .
View More
224	M. Tariqul Islam, M. Atiqur Rahman, Zahid Hasan Mahmood, Md. Rezaul Karim, Mashur Rafique and Shahida Rafique : , An approach to solve real-time problem applying semaphore, Dhaka University Journal of Science , vol.49 , no.2 , pp.117-121 , 2001 .
225	Suraiya Pervin, and M. Chakroborty : A Systolic Array Realization of the Adaptive Decision Feedback Equalizer., International Journal of Signal Processing, Elseviar. , vol.80 , pp.2633-2640 , 2000 .
226	Md. Haider Ali and Toyohisa Kaneko : Automatic Reconstruction of 3D Human Face from CT and Color Photographs, IEICE transactions on Information and Systems, The Institute of Electronics, Information and Communication Engineers, Japan , vol.E82-D , no.9 , pp.1287-1293 , 1999 .
View More
227	Md. Haider Ali, Eiji Takahashi and Toyohisa Kaneko : A 3D Face Reconstruction Method from CT Image and Color Photographs, IEICE transactions on Information and Systems, The Institute of Electronics, Information and Communication Engineers, Japan , vol.E81-D , no.10 , pp.1095-1102 , 1998 .
View More
228	Md. Imam Hossain, Abu Taher and Md. Haider Ali : Design and Development of a Timing Channel Analyzer, SUST STUDIES, Shah Jalal University of Science and Technology, Sylhet, Bangladesh, , vol.1 , no.1 , pp.7-16 , 1996 .
229	Suraiya Pervin, S. K. Ghafoor, M. Lutfor Rahman and Farruk Ahmed : Design of a Microprocessor Based Function Generator., The Dhaka University Journal of Science. , vol.44 , no.2 , pp.235-242 , 1996 .
230	Mohammad Habibullah Rakib, Showkot Hossain, Mosarrat Jahan and Upama Kabir : A Blockchain-Enabled Scalable Network Log Management System, Journal of Computer Science , vol.18 , no.6 , pp.496--508 , 2022 .
231	Md Ashraful Islam, Mahfuzur Rahman Rafi, Al-amin Azad and Jesan Ahammed Ovi : Weighted frequent sequential pattern mining, Applied Intelligence Springer , pp.1--28 , 2021 .
232	Md. Mustafizur Rahman, Choong Seon Hong, Sungwon Lee, Jaejo Lee, Md. Abdur Razzaque and Jin Hyuk Kim : Medium Access Control in Powerline Communication: An Overview of the IEEE 1901 and ITU G.hn standards, IEEE Communications Magazine (impact factor:10.356) , vol.49 , no.6 , pp.183 - 191 , June 2011 .
View More
233	Mosaddek Hossain Kamal Tushar, Chadi Assi, Martin Maier and Mohammad Faisal Uddin : Smart Microgrids: Optimal Joint Scheduling for Electric Vehicles and Home Appliances, IEEE Transactions on Smart Grid , vol.5 , no.1 , pp.239-250 , 2014 .
View More
234	Mosaddek Hossain Kamal Tushar, Adel W. Zeineddine and Chadi Assi : Demand-Side Management by Regulating Charging and Discharging of the EV, ESS, and Utilizing Renewable Energy, IEEE Transactions on Industrial Informatics , vol.14 , no.1 , pp.117-126 , 2018 .
View More
235	Mosaddek H. K. Tushar, Chadi Assi and Martin Maier : Distributed Real-Time Electricity Allocation Mechanism for Large Residential Microgrid, IEEE Transactions on Smart Grid , vol.6 , no.3 , pp.1353-1363 , 2014 .
View More
236	Mosaddek Hossain Kamal Tushar and Chadi Assi : Volt-VAR Control Through Joint Optimization of Capacitor Bank Switching, Renewable Energy, and Home Appliances, IEEE Transactions on Smart Grid , vol.9 , no.5 , pp.4077-4086 , 2017 .
View More
237	Mosaddek Hossain Kamal Tushar and Chadi Assi : Optimal Energy Management and Marginal-Cost Electricity Pricing in Microgrid Network, IEEE Transactions on Industrial Informatics , vol.13 , no.6 , pp.3286-3298 , 2017 .
View More
238	Ribal F. Atallah, Chadi M. Assi, Wissam Fawaz, Mosaddek Hossain Kamal Tushar and Maurice Jose Khabbaz : Optimal Supercharge Scheduling of Electric Vehicles: Centralized Versus Decentralized Methods, IEEE Transactions on Vehicular Technology , vol.67 , no.9 , pp.7896-7909 , 2018 .
View More
239	Mohammad Ekramul Kabir, Chadi Assi, Mosaddek Hossain Kamal Tushar and Jun Yan : Optimal Scheduling of EV Charging at a Solar Power-Based Charging Station, IEEE Systems Journal , vol.14 , no.3 , pp.4221-4231 , 2020 .
View More
240	Reem Kateb, Parisa Akaber, Mosaddek H. K. Tushar, Abdullah Albarakati, Mourad Debbabi and Chadi Assi : Enhancing WAMS Communication Network Against Delay Attacks, IEEE Transactions on Smart Grid , vol.10 , no.3 , pp.2738-2751 , 2019 .
View More
241	MubinUlHaque, ZarrinTasnimSworna, Hafiz Md. Hasan Babu and AsishKumer Biswas : “A Fast FPGA-Based BCD Adder”, Journal of Circuit, System and Signal Processing (CSSP) , vol.37 Springer , pp.4384-4408. , 2018 .
242	Nazma Tara, Hafiz Md. Hasan Babu and Lafifa Jamal : “Power Efficient Optimum Design of the Reversible Plessey Logic Block of a Field Programmable Gate Array”, Elsevier Journal of Sustainable Computing: Informatics and Systems , vol.16 , pp.76-92 , 2017 .
243	Reem Kateb, Mosaddek Hossain Kamal Tushar, Chadi Assi and Mourad Debbabi : Optimal Tree Construction Model for Cyber-Attacks to Wide Area Measurement Systems, IEEE Transactions on Smart Grid , vol.9 , no.1 , pp.25-34 , 2018 .
View More
244	Hafiz Md. Hasan Babu : “Cost-efficient design of a quantum multiplier–accumulator unit”, Springer Journal of Quantum Information Processing , pp.30 , 2017 .
245	Hafiz Md. Hasan Babu, Md. Solaiman Mia and AshisKumer Biswas : “Efficient Techniques for Fault Detection and Correction of ReversibleCircuits”, Springer Journal of Electronic Testing , pp.1-15 , 2017 .
246	Hyame Assem Alameddine, Mosaddek Hossain Kamal Tushar and Chadi Assi : Scheduling of Low Latency Services in Softwarized Networks, IEEE Transactions on Cloud Computing , vol.9 , no.3 , pp.1220-1235 , 2019 .
View More
247	Nazma Tara and Hafiz Md. Hasan Babu : “Synthesis of Reversible PLA Using Products Sharing”, Springer Journal of Computational Electronics. Journal of Computational Electronics , vol.20 , pp.420-428 , 2016 .
248	ZarrinTasnimSworna, Mubin-Ul-Haque, Nazma Tara, Hafiz Md. HasanBabu and Ashis Kumar Biswas : “Low-power and area efficient binary coded decimal adder design using a look up table-based field programmable gate array”, of Institute of Engineering and Technology’s Circuit, Devices and Systems (IET CDS) , vol.10 , pp.163-172 , 2016 .
249	Rossi Kamal, Mosaddek Hossain Kamal, Muhammad Mostafa Monowar and Choong Seon Hong : A mobile middleware to solve interoperability problems in VOIP streaming session, International Journal of Communication Networks and Distributed Systems , vol.8 , no.1-2 InderScience , pp.1-12 , 2011 .
View More
250	Hafiz Md. HasanBabu and Solaiman Mia : “Design of a Compact Reversible Fault Tolerant Division Circuit”, Elsevier Journal of Microelectronics , vol.51 , pp.15-29 , 2016 .
251	NazmaTaraandHafiz Md. HasanBabu : “Synthesis of reversible PLA using products sharing”, Journal of Computational Electronics , pp.1-9 , 2015 .
252	AnkurSarker, Hafiz Md. HasanBabu and S. M. Mahbubur Rashid : “Design of a DNA-based Reversible Arithmetic and Logic Unit”, IETNanobiotechnology , vol.9 , pp.226-238 , 2015 .
253	Hafiz Md. HasanBabu, NazirSaleheen, Lafifa Jamal, Sheikh Muhammad Sarwar and Tsutomu Sasao : “Approach to design a compact reversible low power binary comparator”, IET Computers & Digital Techniques , vol.8 , no.3 , pp.129-139 , 2014 .
254	Lafifa Jamal, Hafiz Md. HasanBabuand Md. Masbaul Alam : “An EfficientApproach to Design a Reversible Control Unit of a Processor”, Elsevier Journal of Sustainable Computing: Informatics and Systems , vol.3 , pp.286-294 , 2013 .
255	Md. Shamsujjoha, Hafiz Md. Hasan Babu and Lafifa Jamal : “Design of a Compact Reversible Fault Tolerant Field Programmable Gate Array: A Novel Approach in Reversible Logic Synthesis”, Elsevier Journal of Microelectronics , vol.44 , pp.519-537 , 2013 .
256	Lafifa Jamal, Farah Sharmin, Md. Abdul Mottalib, Hafiz Md. HasanBabu : “Design and Minimization of Reversible Circuits for a Data Acquisition and Storage System”, The International Journal of Engineering and Technology , vol.2 , pp.9-15 , 2012 .
257	Lafifa Jamal, Md. Shamsujjoha, Hafiz Md. Hasan Babu : “Design of Optimal Reversible Carry Look-Ahead Adder with Optimal Garbage and Quantum Cost”, The International Journal of Engineering and Technology , vol.2 , pp.44-50 , 2012 .
258	Rubaia Rahman, Lafifa Jamal, Hafiz Md. Hasan Babu : “Design of Reversible Fault Tolerant Programmable Logic Arrays with Vector Orientation”, International Journal of Information and Communication Technology Research , vol.1 , pp.337-343 , 2011 .
259	NaimulHuda, Shahed Anwar, Lafifa Jamal, Hafiz Md. HasanBabu : Design of a Reversible Random Access Memory”, Dhaka University Journal of Applied Science & Engineering , vol.2(1) 31-38 , 2011 .
260	Mohammod Akbar Kabir, Hafiz Md. HasanBabu, LiakotAli, Lafifa Jamal : “Design of a High Performance Low Cost IC Tester - A Conceptual View”, DhakaUniversity Journal of Science , vol.58(1): 63-66 , 2010 .
261	Noor MuhammedNayeem, Lafifa Jamal, Hafiz Md. HasanBabu : “Efficient Reversible Montgomery Multiplier and Its Application to Hardware Cryptography”, Journal of Computer Science (Science Publications, USA) , vol.5 (1): 49-56 , 2009 .
262	Ashis Kumar Biswas, Md. MahmudulHasan, Ahsan Raja Chowdhury and Hafiz Md. Hasan Babu : “Efficient Approaches for Designing Reversible Binary Coded Decimal Adders”, Elsevier Journal of Microelectronics , vol.39 , pp.1693–1703 , 2008 .
263	Hafiz Md. HasanBabu : “Logic Synthesis and Minimization of Multiple-Valued Input TANT Networks”, The Dhaka University Journal of Science , vol.56 , pp.05-10 , 2008 .
264	Hafiz Md. HasanBabu, Md. Saiful Islam, Md. Rafiqul Islam, Lafifa Jamal, Muhammad RezaulKarim, Abdullah Al Mahmud : “Building Toffoli Network for Reversible Logic Synthesis Based on Swapping Bit Strings”, The Dhaka University Journal of Science , vol.55(2): 153-156 , 2007 .
265	Hafiz Md. HasanBabu and Ahsan Raja Chowdhury : “Design of a Compact Reversible Binary Coded Decimal Adder Circuit”, Elsevier Journal of Systems Architecture 52 , pp.272-282 , 2006 .
266	Hafiz Md. Hasan Babu and Moinul Islam Zaber : “An Approach to Minimize the Multiple-Valued Input Binary-Valued Output functions Using Local Covering”, Weases Transaction on Computers , vol.10 , no.2 , pp.2381-2389 , 2006 .
267	Hafiz Md. HasanBabu, Abdur Rahim Mustafa, Md. SumonShahriar, Lafifa Jamal, Md.HamidullahAhmad : “An Improved Approach of Minimization of Multi-Valued Multi-Output Logic Expressions”, The Dhaka University Journal of Science , vol.54(2) , pp.141-144 , 2006 .
268	Hafiz Md. HasanBabu, TanzeemIqbal, ChowdhuryFarhan Ahmed, RaquibulHasan, Moinul Islam Zaber, Lafifa Jamal, Shahed Anwar, Mohammad Hamidullah Ahmad : “An Optimal Design Method of a Multi-Valued PLA”, The Dhaka University Journal of Science , pp.149-152 , 2006 .
269	Hafiz Md. HasanBabu : “An Improved Method for Minimization of Circuit Using TANT Network”, The Dhaka University Journal of Science , vol.54 , pp.49-54 , 2006 .
270	Hafiz Md. HasanBabu : “Reversible Logic Decomposition to Minimize Full-Adder Circuit”, The Dhaka University Journal of Science , vol.54 , pp.137-139 , 2006 .
271	Hafiz Md. HasanBabu, AhmedulKabir and A.S.M. Fazle Rabbi : “On the modified technique for better data compression”, Bangladesh Journal of Scientific and Industrial Research (BJSIR) , 2003 .
272	Hafiz Md. HasanBabuand Md. Rafiqul Islam : “Minimization of multilevel AND-EXOR expressions using Pseudo-Kronecker decision diagrams”, The Dhaka University Journal of Science , 2003 .
273	Md. Rafiqul Islam and Hafiz Md. HasanBabu : “An improved technique to create lattice index of materialized views for query optimization”, The Dhaka University Journal of Science , 2003 .
274	Md. Rafiqul Islam and Hafiz Md. Hasan Babu : “An improved algorithm for query optimization using materialized view”, The Dhaka University Journal of Science , 2003 .
275	Md. Rafiqul Islam and Hafiz Md. Hasan Babu : “A hybrid approach for efficient shortest path algorithm in neural networks”, The Dhaka University Journal of Science , 2003 .
276	Hafiz Md. HasanBabu and T. Sasao : “Upper bound on the size of the shared binary decision diagram for an n-bit adder”, Journal of Bangladesh Academy of Sciences , vol.26 , pp.119-121 , 2002 .
277	ShailyKabir, M. Karim and Hafiz Md. HasanBabu : “The use of optimal ordering of input variables for simplification of single-output logic functions”, The Dhaka University Journal of Science , vol.50 , pp.101-108 , 2002 .
278	Hafiz Md. HasanBabu and M.L. Rahman : “Multiple-valued pseudo-Kronecker decision diagrams: A compact representation of multiple-output functions”, The Dhaka University Journal of Science , vol.50 , pp.187-196 , 2002 .
279	Hafiz Md. HasanBabu and T. Sasao : “Heuristics to Minimize Multiple-Valued Decision Diagrams”, IEICE Trans. Fundamentals , vol.E83-A, no. 12 , pp.2498-2504 , 2000 .
280	Hafiz Md. Hasan Babu and T. Sasao : “Representations of Multiple-Output Functions Using Binary Decision Diagrams for Characteristic Functions”, IEICE Trans. Fundamentals , vol.E82-A, no. 11 , pp.2398-2406 , 1999 .
281	Hafiz Md. Hasan Babu and T. Sasao : “Time-Division Multiplexing Realizations of Multiple-Output Functions Based on Shared Multi-Terminal Multiple-Valued Decision Diagrams”, IEICE Trans. Information & Systems , pp.925-932 , 1999 .
282	Hafiz Md. Hasan Babu and T.Sasao : “Time Shared Multi-Terminal Binary Decision Diagrams for Multiple-Output Functions”, IEICE Trans. Fundamentals , pp.2545-2553 , 1998 .
283	Hafiz Md. HasanBabu and M.A. Mottalib : “Design of minimized logic networks using EXOR & AND gates by a computer with small memory space”, Bangladesh Journal of Scientific and Industrial Research (BJSIR , vol.xxx, no. 2-3 , pp.211-218 , 1995 .
284	Md. Rafiqul Islam and Hafiz Md. HasanBabu : “A study on the performance of variations of heapsort”, Journal of the Bangladesh Academy of Sciences , vol.18 , pp.201-207 , 1994 .
285	Md. Rafiqul Islamand Hafiz Md. HasanBabu : “HeapsortUsing Binary Insertion”, The Dhaka University Journal of Science , pp.185-193 , 1994 .
286	Hafiz Md. HasanBabu and M.A. Mottalib : “A technique for the design of microprocessor memory systems”, Dhaka University Journal of Science , vol.42, no.2 , pp.185-193 , 1994 .
287	M.A. Mottalib, M.H. Rahman and Hafiz Md. HasanBabu : “A logic minimization technique using Reed-Muller canonic expansion with software implementation”, Journal of the Bangladesh Electronics Society , vol.3, no. 1 , pp.9-1 , 1993 .
288	Hafiz Md. HasanBabu and M. Kaykobad : “An algorithm for designing Boolean functions with Exclusive-OR (EXOR) & AND logic elements”, Journal of the Bangladesh Computer Society , pp.49-51 , 1993 .
289	Nahar Sultana, Farhana Huq, Md. Abdur Razzaque and Md. Mustafizur Rahman : User Utility Maximization in Narrowband Internet of Things for Prioritized Healthcare Applications, Sensors (impact factor:3.847) , vol.22 , no.3 MDPI , 2022 .
View More
290	Shaikhum Monira, Upama Kabir, Mosarrat Jahan and Uchswas Paul : An Efficient Handover Mechanism for SDN-Based 5G HetNets, Dhaka University Journal of Applied Science and Engineering , vol.6 , no.2(2021) , pp.49 -- 58 , 2022 .
1	Prodipta S. Amartya, Shaily Kabir, Sagar C. K. Babu and Mosarrat Jahan "An Interval Creation Approach to Construct Interval Type-2 Fuzzy Sets." 2024 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE) , pp. 1-9. IEEE, 2024 .
2	Jingda Ying, Shaily Kabir and Christian Wagner "A Restricted Parametrized Model for Interval-Valued Regression." IEEE International Conference on Fuzzy Systems Songdo Incheon, Korea: IEEE, 2023 .
3	Shaily Kabir and Christian Wagner "Visualization of Interval Regression for Facilitating Data and Model Insight." IEEE World Congress on Computational Intelligence Padova, Italy: IEEE, 2022 .
4	Md Tanvir Alam, Amit Roy, Chowdhury Farhan Ahmed, Md Ashraful Islam and Carson K Leung "Mining High Utility Subgraphs." 2021 International Conference on Data Mining Workshops (ICDMW) , pp. 566--573. IEEE: 2021 .
5	Md. Tanvir Alam, Amit Roy, Chowdhury Farhan Ahmed, Md. Ashraful Islam and Carson K. Leung "Mining High Utility Subgraphs." 2021 International Conference on Data Mining Workshops (ICDMW) , pp. 566-573. 2021 .
6	Shaily Kabir and Christian Wagner "Interval-Valued Regression ─ Sensitivity to Data Set Features." IEEE International Conference on Fuzzy Systems Luxembourg: IEEE, 2021 .
7	Mahmudul Hasan, Mosarrat Jahan and Shaily Kabir "A Fuzzy Logic-Based Trust Estimation in Edge-Enabled Vehicular Ad Hoc Networks." IEEE International Conference on Fuzzy Systems Luxembourg: IEEE, 2021 .
8	Md. Tanvir Alam, Chowdhury Farhan Ahmed, Md. Samiullah and Carson K. Leung "Mining Frequent Patterns from Hypergraph Databases." Pacific-Asia Conference on Knowledge Discovery and Data Mining 2021 .
9	Md. Tanvir Alam, Chowdhury Farhan Ahmed, Md. Samiullah and Carson K. Leung "Discriminating Frequent Pattern Based Supervised Graph Embedding for Classification." Pacific-Asia Conference on Knowledge Discovery and Data Mining 2021 .
10	Md. Ashaduzzaman, Shanto Roy, Shihabuz Zaman and Abu Ahmed Ferdaus "Anomaly Detection in Admission or Selection Examinations using Data Mining Techniques." 2020 2nd International Conference on Sustainable Technologies for Industry 4.0 (STI) , pp. 1-6. 2020 .
11	Saif Mahmud, M Tanjid Hasan Tonmoy, Kishor Kumar Bhaumik, A K M Mahbubur Rahman, M Ashraful Amin, Mohammad Shoyaib, Muhammad Asif Hossain Khan and Amin Ahsan Ali "Human Activity Recognition from Wearable Sensor Data Using Self-Attention." 24th European Conference on Artificial Intelligence (ECAI) Santiago de Compostela, Spain: 2020 .
12	Mohammad Habibullah Rakib, Showkot Hossain, Mosarrat Jahan and Upama Kabir "Towards Blockchain-Driven Network Log Management System." 2020 IEEE 8th International Conference on Smart City and Informatization (iSCI) , pp. 73-80. 2020 .
13	Md. Saidur Rahman and Md. Rezaul Karim "Drawing Planar Graphs." WALCOM 2020 , pp. 3-14. Singapore: LNCS, 2020 .
14	Shaily Kabir and Christian Wagner "A Bidirectional Subsethood Based Fuzzy Measure for Aggregation of Interval-Valued Data." 18th International Conference on Information Processing and Management of Uncertainty in Knowledge-Based Systems (IPMU 2020) , pp. 603-617. Lisbon, Portugal: Springer, Cham, 2020 .
View More
15	Md Asiful Haque, Shamima Sultana, Md Jayedul Islam, Md Ashraful Islam and Jesan Ahammed Ovi "Factoid Question Answering over Bangla Comprehension." International Symposium on Multidisciplinary Studies and Innovative Technologies Tokat, Turkey: IEEE, 2020 .
16	Shah Mohammed Nuruddin, Md Didarul Islam, Md Shafiqul Alam, Jesan Ahammed Ovi and Md Ashraful Islam "An Efficient Approach for Sequential Pattern Mining on GPU Using CUDA Platform." International Symposium on Multidisciplinary Studies and Innovative Technologies Tokat, Turkey: IEEE, 2020 .
17	Kamal Parvez, Fatema Tuz Zohra and Mosarrat Jahan "A secure and lightweight user authentication mechanism for wireless body area network." 6th International Conference on Networking, Systems and Security , pp. 139-143. Dhaka: 2019 .
18	Md. Nazmul Haque, M. Tanjid Hasan Tonmoy, Saif Mahmud, Amin Ahsan Ali, Muhammad Asif Hossain Khan and Mohammad Shoyaib "GRU-based Attention Mechanism for Human Activity Recognition." 1st International Conference on Advances in Science, Engineering and Robotics Technology (ICASERT) , pp. 1-6. Dhaka, Bangladesh: IEEE, 2019 .
View More
19	Md Mofijul Islam, Amar Debnath, Tahsin Al Sayeed, Md Mahmudur Rahman, Md. Mosaddek Khan, Swakkhar Shatabda and Anik Islam "d-DeVIS: A Gray Box Interpretable Debugging Approach for Deep Sequence Learning Model." IEEE TENSYMP-2019 Kolkata, India: IEEE, 2019 .
View More
20	Sabrina Zaman Ishita, Chowdhury Farhan Ahmed, Carson K. Leung and Calvin H. S. Hoi "Mining Regular High Utility Sequential Patterns in Static and Dynamic Databases.." 13th IMCOM 2019 , pp. 897-916. Phuket, Thailand: Springer, 2019 .
View More
21	Jesan Ahammed Ovi, Chowdhury Farhan Ahmed, Carson K. Leung and Adam G. M. Pazdor "Mining Weighted Frequent Patterns from Uncertain Data Streams.." 13th IMCOM 2019 , pp. 917-936. Phuket, Thailand: Springer, 2019 .
View More
22	Abu Kalam, Md Enamul Haque, Mohammad Jashem, Mahamudul Hasan, Muhammad Ibrahim and Taskeed Jabid "Facial Expression Recognition Using Local Composition Pattern." The 7th International Conference on Computer and Communications Management , pp. 63-67. Thailand: ACM, USA, 2019 .
View More
23	Fariha Moomtaheen Upoma, Salsabil Ahmed Khan, Chowdhury Farhan Ahmed, Tahira Alam, Sabit Anwar Zahin and Carson K. Leung "Discovering Correlation in Frequent Subgraphs.." 13th IMCOM 2019 , pp. 1045-1062. Phuket, Thailand: Springer, 2019 .
View More
24	Shaily Kabir, Christian Wagner, Timothy C. Havens and Derek T. Anderson "Measuring Similarity between Discontinuous Intervals - Challenges and Solutions." 2019 IEEE International Conference on Fuzzy Systems (Fuzz-IEEE) , pp. 1-7. New Orleans, Louisiana, USA: IEEE, 2019 .
View More
25	Nahian Ashraf, Riddho Ridwanul Haque, Md Ashraful Islam, Chowdhury Farhan Ahmed, Carson K. Leung, Jiaxing Jason Mai and Bryan H. Wodi "WeFreS: Weighted Frequent Subgraph Mining in a Single Large Graph." Industrial Conference on Data Mining ibai publishing, 2019 .
26	Imran Hossain, M M Hasan, S. Faisal Hasan and Md. Rezaul Karim "A study of security awareness in Dhaka city using a portable WiFi pentesting device." 2nd International Conference on Innovation in Engineering and Technology (ICIET) 2019 .
27	Mahbuba Maliha Mourin, Abu Ahmed Ferdaus and Md Jakir Hossain "Landslide Susceptibility Mapping in Chittagong District of Bangladesh using Support Vector Machine integrated with GIS." 2018 International Conference on Innovation in Engineering and Technology (ICIET) , pp. 1--5. 2018 .
28	Md Tanvir Alam and Md Mofijul Islam "BARD: Bangla Article Classification Using a New Comprehensive Dataset." 2018 International Conference on Bangla Speech and Language Processing (ICBSLP) , pp. 1-5. 2018 .
29	Karishma Mohiuddin, Mirza Mohtashim Alam, Amit Kishor Das, Md Tahsir Ahmed Munna, Shaikh Muhammad Allayear and Md Haider Ali "Haar Cascade Classifier and Lucas–Kanade Optical Flow Based Realtime Object Tracker with Custom Masking Technique." Future of Information and Communication Conference (FICC-2018) , pp. 398-410. Singapore: 2018 .
30	Tanzir Islam Pial, Shahreen Selim Aunti, Sabbir Ahmed and Hasnain Heickal "End-to-End Speech Synthesis for Bangla with Text Normalization.." 5th International Conference on Computational Science/ Intelligence and Applied Informatics (CSII) , pp. 66-71. Yonago, Japan: IEEE, 2018 .
View More
31	Md.Tanvir Alam and Md Mofijul Islam "BARD: Bangla Article Classification using a New Comprehensive Dataset." nternational Conference on Bangla Speech and Language Processing (ICBSLP) IEEE, 2018 .
32	Amar Debnath, Redoan Rahman, Md Mofijul Islam and Md Abdur Razzaque "A Hierarchical Learning Model for Claim Validation." International Joint Conference on Computational Intelligence (IJCCI) Dhaka, Bangladesh: Springer, 2018 .
33	Zarrin Tasnim Sworna, Mubin Ul Haque and D. M. Anisuzzaman "High-Speed and Area-Effcient LUT-Based BCD Multiplier Design." WIECON-ECE IEEE, 2018 .
View More
34	Zarrin Tasnim Sworna, Mubin Ul Haque and Shahedur Rahman "An FPGA-Based Divider Circuit Using Simulated Annealing Algorithm." 18th International Symposium on Communications and Information Technologies (ISCIT2018) 2018 .
View More
35	Md Mahmudur Rahman, Chowdhury Farhan Ahmed, Carson Kai-sang Leung and Adam GM Pazdor "Frequent Sequence Mining with Weight Constraints in Uncertain Databases." Proceedings of the 12th International Conference on Ubiquitous Information Management and Communication Langkawi, Malaysia: ACM, 2018 .
View More
36	Md Shadman Rafid, Mohammad Mazedul Islam, Md Naimul Hoque and Chowdhury Farhan Ahmed "Reframing for Non-Linear Dataset Shift.." 18th EGC 2018 , pp. 131-142. Paris, France: Hermann-Éditions, 2018 .
View More
37	Tahira Alam, Chowdhury Farhan Ahmed, Sabit Anwar Zahin, Muhammad Asif Hossain Khan and Maliha Tashfia Islam "An Effective Ensemble Method for Multi-class Classification and Regression for Imbalanced Data." 18th Industrial Conference on Data Mining , pp. 59-74. Springer, New York, USA: 2018 .
38	Md Mahmudur Rahman, Chowdhury Farhan Ahmed, Carson K. Leung and Adam G. M. Pazdor "Frequent Sequence Mining with Weight Constraints in Uncertain Databases.." 12th IMCOM 2018 , pp. 48:1-48:8. Langkawi, Malaysia: ACM, 2018 .
View More
39	Mohammad Fahim Arefin, Maliha Tashfia Islam and Chowdhury Farhan Ahmed "Mining Sequential Correlation with a New Measure.." 18th Industrial Conference on Data Mining 2018 , pp. 29-43. New York, NY, USA: Springer, 2018 .
View More
40	Abeda Sultana, Hosneara Ahmed and Chowdhury Farhan Ahmed "A New Approach for Mining Representative Patterns.." 18th Industrial Conference on Data Mining 2018 , pp. 44-58. New York, NY, USA: Springer, 2018 .
View More
41	Tahira Alam, Chowdhury Farhan Ahmed, Sabit Anwar Zahin, Muhammad Asif Hossain Khan and Maliha Tashfia Islam "An Effective Ensemble Method for Multi-class Classification and Regression for Imbalanced Data.." 18th Industrial Conference on Data Mining 2018 , pp. 59-74. New York, NY, USA: Springer, 2018 .
View More
42	Rutba Aman and Chowdhury Farhan Ahmed "Mining Cross-Level Closed Sequential Patterns.." 18th Industrial Conference on Data Mining 2018 , pp. 199-214. New York, NY, USA: Springer, 2018 .
View More
43	Sabrina Zaman Ishita, Faria Noor and Chowdhury Farhan Ahmed "An Efficient Approach for Mining Weighted Sequential Patterns in Dynamic Databases.." 18th Industrial Conference on Data Mining 2018 , pp. 215-229. New York, NY, USA: Springer, 2018 .
View More
44	Md. Ashraful Islam, Chowdhury Farhan Ahmed, Carson K. Leung and Calvin S. H. Hoi "WFSM-MaxPWS: An Efficient Approach for Mining Weighted Frequent Subgraphs from Edge-Weighted Graph Databases.." 22nd PAKDD 2018 , pp. 664-676. Melbourne, VIC, Australia: Springer, 2018 .
View More
45	Nasid Habib Barna, Tisa Islam Erana, Shabbir Ahmed and Hasnain Heickal "Segmentation of Heterogeneous Documents into Homogeneous Components using Morphological Operations." 2018 IEEE/ACIS 17th International Conference on Computer and Information Science (ICIS) , pp. 513-518. Singapore: IEEE, 2018 .
View More
46	Shaily Kabir, Christian Wagner, Timothy C. Havens and Derek T. Anderson "A Bidirectional Subsethood Based Similarity Measure for Fuzzy Sets." IEEE World Congress on Computational Intelligence (WCCI 2018) , pp. 1-7. Rio de Janeiro, Brazil: IEEE, 2018 .
View More
47	Md Ashraful Islam, Chowdhury Farhan Ahmed, Carson K Leung and Calvin SH Hoi "WFSM-MaxPWS: an efficient approach for mining weighted frequent subgraphs from edge-weighted graph databases." Pacific-Asia Conference on Knowledge Discovery and Data Mining , pp. 664--676. Melbourne, VIC, Australia: Springer, 2018 .
48	Mirza Mohtashim Alam, Md. Kabirul Islam, Karishma Mohiuddin, Md. Shamsul Kaonain, Amit Kishor Das and Md. Haider Ali "A Reduced Feature Based Neural Network Approach to Classify the Category of Students." Proceedings of the 2nd International Conference on Innovation in Artificial Intelligence, ICIAI '18 , pp. 28-32. Shanghai, China: 2018 .
49	Mahbuba Maliha Mourin, Abu Ahmed Ferdaus and Md Jakir Hossain "Landslide Susceptibility Assessment in Chittagong District of Bangladesh Using Adaptive Neuro Fuzzy Inference System (ANFIS) and GIS." Proceedings of the International Conference on Disaster Risk Mitigation, Dhaka, Bangladesh , pp. 23--24. 2017 .
50	M Samiullah, TX Hoang, D Albrecht, A Nicholson and K Korb "iOOBN: A Bayesian Network Modelling Tool Using Object Oriented Bayesian Networks with Inheritance." ICTAI , pp. 1218-122. Boston: IEEE, 2017 .
51	T Alam, SA Zahin, M Samiullah, and CF Ahmed "An Efficient Approach for Mining Frequent Subgraphs." International Conference on Pattern Recognition and Machine Intelligence , pp. 486-492. Springer, 2017 .
52	Md Shakil Hossain, Sk. Shariful Islam Arafat, S M Al-Hossain Imam, Md. Mahmudul Hasan, Md Mofijul Islam, Sanjay Saha, Swakkhar Shatabda and Tamanna Islam Juthi "VIM: A Big Data Analytics Tool for Data Visualization and Knowledge Mining." IEEE WIECON-ECE Dehradun, India: IEEE, 2017 .
View More
53	Md Mofijul Islam, Sk. Shariful Islam Arafat, Md Shakil Hossain, Md Mahmudur Rahman, S M Al-Hossain Imam, Md. Mahmudul Hasan, Swakkhar Shatabda and Tamanna Islam Juthi "RAiTA: Recommending Accepted Answer using Textual Metadata." IEMIS Kolkata, India: Springer, 2017 .
View More
54	Muhammad Ibrahim "Scalability and Performance of Random Forest based Learning-to-Rank for Information Retrieval." ACM SIGIR Forum , pp. 73-74. Japan: ACM, USA, 2017 .
View More
55	Sadia Sharmin, Amin Ahsan Ali, Muhammad Asif Hossain Khan and Mohammad Shoyaib "BFSp: A Feature Selection Method for Bug Severity Classification." 5th IEEE Region 10 Humanitarian Technology Conference (IEEE R10HTC) Dhaka, Bangladesh: 2017.12 .
56	Tahira Alam, Sabit Anwar Zahin, Md. Samiullah and Chowdhury Farhan Ahmed "An Efficient Approach for Mining Frequent Subgraphs.." 7. PReMI 2017 , pp. 486-492. Kolkata, India: Springer, 2017 .
View More
57	Sadia Sharmin, Amin Ahsan Ali, Muhammad Asif Hossain Khan and Mohammad Shoyaib "Feature Selection and Discretization based on Mutual Information." 2017 IEEE International Conference on Imaging, Vision & Pattern Recognition (icIVPR) Dhaka, Bangladesh: 2017.2 .
58	Mosarrat Jahan, Suranga Seneviratne, Ben Chu, Aruna Seneviratne and Sanjay Jha "Privacy preserving data access scheme for IoT devices." IEEE NCA 2017 , pp. 217-226. 2017 .
59	Mosarrat Jahan, Aruna Seneviratne and Sanjay Jha "Access Mechanism for Outsourced Data by Preserving Data Owner’s Preference." IEEE LCN 2017 , pp. 611-614. 2017 .
60	Mosarrat Jahan, Partha Sarathi Roy, Kouichi Sakurai, Aruna Seneviratne and Sanjay Jha "Secure and Light Weight Fine-grained Access Mechanism for Outsourced Data." IEEE TrustCom/BigData/ICESS 2017 , pp. 201- 209. 2017 .
61	Zarrin Tasnim Sworna, Mubin Ul Haque, Hafiz Md Hasan Babu, and Lafa Jamal "A Cost-Efficient LUT-Based BCD Adder Design." IEEE Future Technologies Conference (FTC) , pp. 874-882. Vancuover, Canada: IEEE, 2017 .
62	Zarrin Tasnim Sworna, Mubin Ul Haque, Hafiz Md Hasan Babu, Lafa Jamal, and Ashis Kumer Biswas "An Efficient Design of an FPGA-Based Multiplier Using LUT Merging Theorem." IEEE Computer Society Annual Symposium on VLSI (ISVLSI) , pp. 116-121. Bochum, Germany: IEEE, 2017 .
63	Shaily Kabir, Christian Wagner, Timothy C. Havens, Derek T. Anderson and Uwe Aickelin "Novel Similarity Measure for Interval-Valued Data Based on Overlapping Ratio." 2017 IEEE International Conference on Fuzzy Systems (Fuzz-IEEE) , pp. 1-6. Naples, Italy: IEEE, 2017 .
64	Direnc Pekaslan, Shaily Kabir, Jonathan M. Garibaldi and Christian Wagner "Determining Firing Strengths Through A Novel Similarity Measure to Enhance Uncertainty Handling in Non-Singleton Fuzzy Logic Systems." 9th International Joint Conference on Computational Intelligence (IJCCI 2017) , pp. 83-90. Funchal, Madeira, Portugal: SciTePress, 2017 .
View More
65	Nahid Quader, Md. Osman Goni, Dipankar Chaki and Md. Haider Ali "A Machine Learning Approach to Predict Movie Box-Office Success." Proceedings of 20th International Conference on Computer and Information Technology (ICCIT2017) University of Asia Pacific, 74A Green Road, Dhaka-1215, Bangladesh: 2017 .
66	Nusrat Jahan Suha, Tabib Ibne Mazhar, Dipankar Chaki and Md. Haider Ali "Spinal Cord Injured (SCI) Patients' Length of Stay (LOS) Prediction Based on Hospital Admission Data." 3rd International Conference on Electrical Information and Communication Technology (EICT2017) Khulna, Bangladesh: 2017 .
67	Tahjid Ashfaque Mostafa, Jia Uddin and Md. Haider Ali "Abnormal Event Detection in Crowded Scenarios." 3rd International Conference on Electrical Information and Communication Technology (EICT2017) Khulna, Bangladesh: 2017 .
68	H M Mahedi Hasan, Falguni Sanyal, Dipankar Chaki and Md. Haider Ali "An Empirical Study of Important Keyword Extraction Techniques from Documents." International Conference on Intelligent Systems and Information Management (ICISIM 2017), At Department of CSEIT, MGM's Jawaharlal Nehru Engineering College, Aurangabad- 431003, MS, India: 2017 .
69	Erfan Ahmed, Md. Asad Uzzaman Sazzad, Md. Tanzim Islam, Muhitun Azad and Md. Haider Ali "Challenges, Comparative Analysis and a Proposed Methodology to Predict Sentiment from Movie Reviews Using Machine Learning." International Conference on Big Data Analytics and Computational Intelligence (ICBDACI – 2017) Andhra Pradesh, India: 2017 .
70	M. M. Haque, Suraiya Pervin and Zerina Begum "Enhancement of keyphrase based approach of automatic Bangla text summarizartion." IEEE Region 10 conference Singapore: 2016 .
71	M B Sajib, Md Samiullah, C F Ahmed and CKS Leung "An efficient approach for mining frequent patterns over uncertain data streams." ICTAI , pp. 980-984. IEEE, 2016 .
72	Md Mofijul Islam, Md. Abdur Razzaque and Md. Jahidul Islam "A Genetic Algorithm for Virtual Machine Migration in Heterogeneous Mobile Cloud Computing." 2nd International Conference on Networking Systems and Security (NSysS-2016) Dhaka, Bangladesh: IEEE, 2016 .
View More
73	Md Naimul Hoque, Chowdhury Farhan Ahmed, Nicolas Lachiche, Carson K. Leung and Hao Zhang "Reframing in Clustering.." 28th ICTAI 2016 , pp. 350-354. San Jose, CA, USA: IEEE Computer Society, 2016 .
View More
74	Md. Badi-Uz-Zaman Shajib, Md. Samiullah, Chowdhury Farhan Ahmed, Carson K. Leung and Adam G. M. Pazdor "An Efficient Approach for Mining Frequent Patterns over Uncertain Data Streams.." 28th ICTAI 2016 , pp. 980-984. San Jose, CA, USA: IEEE Computer Society, 2016 .
View More
75	Zarrin Tasnim Sworna, Mubin Ul Haque and Hafiz Md Hasan Babu "A LUT-based matrix multiplication using neural networks." IEEE International Symposium on Circuits and Systems (ISCAS) , pp. 1982-1985. Montreal, Canada: IEEE, 2016 .
76	Zarreen Naowal Reza, Faiza Nuzhat, Nuzhat Ashfat Mahsa and Md. Haider Ali "Detecting Jute Plant Disease Using Image Processing and Machine Learning." 3rd ICEEICT 2016 (This paper is a content of IEEE Xplore Digital Library. Republication/redistribution is prohibited.) MIST, Dhaka, Bangladesh: 2016 .
77	Muhammed Islam, Sabbir Ahmed, Syed Hasan, Alexander Blom, Suraiya Pervin, Shabbir Ahmed "Open Internet: An End-to-End Framework for Detecting Protocol Blocking and Content Shaping." NETAPPS 2015, the 4th International Conference on Internet Applications, Protocols and Services, Kuala Lumpur Malaysia.: 2015 .
78	M. M. Haque, Suraiya Pervin and Zerina Begum "Automatic Bengali news documents summarization by introducing sentence frequency and clustering." 18th International Conference on computers and information technology , pp. 156-160. Dhaka: 2015 .
79	C F Ahmed, Md Samiullah, N Lachiche, M Kull and P. A. Flach "Reframing in Frequent Pattern Mining." ICTAI , pp. 799-806. IEEE, 2015 .
80	Muhammad Aminur Rahaman, Mahmood Jasim, Tao Zhang, Md Haider Ali and Md Hasanuzzaman "Real-time Bengali and Chinese numeral signs recognition using contour matching." IEEE International Conference on Robotics and Biomimetics (ROBIO) , pp. 1215-1220. Zhuhai, China: 2015 .
View More
81	Mosarrat Jahan, Mohsen Rezvani, Aruna Seneviratne and Sanjay Jha "Method for Providing Secure and Private Fine-grained Access to Outsourced Data." IEEE LCN 2015 , pp. 406-409. 2015 .
82	Amit Mandal, Mehedi Hasan, Anna Fariha and Chowdhury Farhan Ahmed "GSCS - Graph Stream Classification with Side Information.." 17. APWeb 2015 , pp. 389-400. Guangzhou, China: Springer, 2015 .
View More
83	Chowdhury Farhan Ahmed, Md. Samiullah, Nicolas Lachiche, Meelis Kull and Peter A. Flach "Reframing in Frequent Pattern Mining.." 27th ICTAI 2015 , pp. 799-806. Vietri sul Mare, Italy: IEEE Computer Society, 2015 .
View More
84	Quazi Marufur Rahman, Anna Fariha, Amit Mandal, Chowdhury Farhan Ahmed and Carson K. Leung "A Sliding Window-Based Algorithm for Detecting Leaders from Social Network Action Streams.." WI-IAT 2015 , pp. 133-136. Singapore: IEEE Computer Society, 2015 .
View More
85	Muhammad Aminur Rahman, Mahmood Jasim, Md. Haider Ali and Md. Hasanuzzaman "Computer Vision Based Bengali Sign Language Recognition using Contour Analysis." Proceedings of 18th International Conference on Computer and Information Technology (ICCIT2015) Dhaka, Bangladesh: 2015 .
86	R Sultana, D Showkat, Md Samiullah and A.R. Chowdhury "Reconstructing Gene Regulatory Network with Enhanced Particle Swarm Optimization." ICONIP , pp. 229–236. Sydney: Spriniger, 2014 .
87	Md Mofijul Islam, Md. Ahasanuzzaman, Md. Abdur Razzaque, Mohammad Mehedi Hassan and Atif Alamri "A Distributed Clustering Algorithm for Target Coverage in Directional Sensor Network." IEEE Asia Pacific Conference on Wireless and Mobile Bali, Indonesia: IEEE, 2014 .
View More
88	Muhammad Ibrahim and Mark Carman "Undersampling Techniques to Re-balance Training Data for Large Scale Learning-to-Rank." The 10th Asia Information Retrieval Society Conference (AIRS 2014) , pp. 444-457. Malaysia: Springer International Publishing, Germany, 2014 .
View More
89	Muhammad Ibrahim and Mark Carman "Improving Scalability and Performance of Random Forest Based Learning-to-Rank Algorithms by Aggressive Subsampling." The 12th Australasian Data Mining Conference (AusDM 2014) , pp. 91-99. Australia: CRPIT, Australia, 2014 .
View More
90	Guangwen Liu, Muhammad Asif Hossain Khan, Masayuki Iwai, Masaki Ito, Yoshito Tobe, Kaoru Sezaki and Dunstan Matekenya "Beyond Horizontal Location Context: Measuring Elevation using Smartphone's Barometer." UbiComp , pp. 459-468. Seattle, USA: 2014.9 .
91	Muhammad Aminur Rahman, Mahmood Jasim, Md. Haider Ali and Md. Hasanuzzaman "Real-Time Computer Vision Based Bengali Sign Language Recognition." Proceedings of 17th International Conference on Computer and Information Technology (ICCIT2014) , pp. 159-163. Daffodil International University, Sukrabad, Dhaka-1207, Bangladesh: 2014 .
92	Md Samiullah, C. F. Ahmed, M. A. Nishi, A. Fariha, S M Abdullah and M. R. Islam "Correlation Mining in Graph Databases with a New Measure." APWEB Sydney: Springer, 2013 .
93	Md. Manzurul Hasan, Md. Saidur Rahman and Md. Rezaul Karim "Box-rectangular drawing of planar graphs(Extended Abstract)." WALCOM 2013 , pp. 334-345. Kharagpur, Westbengal: Lecture Notes in Computer Science, 7748, Springer, 2013 .
94	Mosarrat Jahan and Lata Narayanan "Minimum Energy Broadcast in Duty Cycled Wireless Sensor Networks." IEEE WCNC, 2013 , pp. 980-985. 2013 .
95	Muhammad Asif Hossain Khan, Danushka Bollegala, Guangwen Liu and Kaoru Sezaki "Multi-Tweet Summarization of Real-Time Events." ASE/IEEE International Conference on Social Computing , pp. 128-133. Washington D.C., USA: 2013.9 .
96	Muhammad Asif Hossain Khan, Masayuki Iwai and Kaoru Sezaki "A Robust and Scalable Framework for Detecting Self-Reported Illness from Twitter." 14th IEEE International Conference on E-Health Networking, Application and Services (IEEE Healthcom) , pp. 303-308. Beijing, China: 2012.10 .
97	Muhammad Asif Hossain Khan, Masayuki Iwai and Kaoru Sezaki "Towards Urban Phenomenon Sensing by Automatic Tagging of Tweets." 9th International Conference on Networked Sensing Systems (INSS) , pp. 1-8. Antwerp, Belgium: 2012.6 .
98	Joy Rahman, Sajeeb Saha, and Syed Faisal Hasan, "A New Congestion Control Algorithm for Datagram Congestion Control Protocol (DCCP) Based Real-time Multimedia Applications." ICECE 2012, the 7th International Conference on Electrical and Computer Engineering, Dhaka, Bangladesh Dhaka: 2012 .
99	Shaily Kabir, Sudhir P. Mudur and Nematollaah Shiri "Capturing Browsing Interests of Users into Web Usage Proﬁles." Association for the Advancement of Artificial Intelligence (AAAI) Workshop on Intelligent Techniques for Web Personalization and Recommender Systems , pp. 18-25. Toronto, Canada: AAAI, 2012 .
View More
100	S. Halder, M. Samiullah, A.M. J Sarkar and YK Lee "MovieSwarm: Information Mining technique for Movie Recommendation System." International Conference on Electrical and Computer Engineering (ICECE) , pp. 20 – 22. Dhaka: IEEE, 2012 .
101	M. Samiullah, S.M. Abdullah, AFM I.H. Bappi and S Anwar "Queue Management Based Congestion Control in Wireless Body Sensor Network." International Conference on Informatics, Electronics & Vision (ICIEV) Dhaka: IEEE, 2012 .
102	Md. Rezaul Karm, Md. Jawaherul Alam and Md. Saidur Rahman "On some properties of doughnut graphs (Extended Abstract)." IWOCA , pp. 60-64. Bangalore: Lecture Notes in Computer Science, 7643, Springer, 2012 .
103	Imran Ahmed, Sonia Sadeque and Suraiya Pervin "Margin adaptive resource allocation for multiuser OFDM systems by modified particle swarm optimization and differential evolution." 21st International Conference of Electrical communications and Computers, ieeexplore.ieee.org , pp. 227-231. USA: 2011 .
104	Kaeser Md. Sabrin and Md. Haider Ali "An Intelligent Pixel Replication Technique by Binary Decomposition for Digital Image Zooming." Proceedings of the 26th Image and Vision Computing New Zealand Conference (IVCNZ 2011) , pp. 547 - 552. Auckland, New Zealand: 2011 .
View More
105	Md. Abdul Mannan Mondal and Md. Haider Ali "Disparity Estimation by Reverse Fuzzyfication." International Conference on Signal and Information Processing (ICSIP 2010), IEEE Catalog Number: CFP1095L-ART , pp. 234-237. Changsha, China: 2010 .
106	Muhammad Ibrahim, Nasimul Noman and Hitoshi Iba "On the Complexity and Completeness of Robust Biclustering Algorithm (ROBA)." The 4th International Conference on Bioinformatics and Biomedical Engineering (ICBBE) Chengdu, China: IEEE, 2010 .
View More
107	Muhammad Ibrahim, Nasimul Noman and Hitoshi Iba "Introducing Flexibility in Robust Biclustering Algorithm (ROBA) to Find Imperfect Biclusters." The 2010 International Conference on Bioinformatics and Biomedical Technology (ICBBT) (Accepted) Chengdu, China: IEEE, 2010 .
108	Md. Abdul Mannan Mondal and Md. Haider Ali "On Stereo Correspondence Estimation: A Spiral Search Algorithm." International Conference on Signal and Information Processing (ICSIP 2010), IEEE Catalog Number: CFP1095L-ART , pp. 204-207. Changsha, China: 2010 .
109	Kaeser Md. Sabrin, T. Zhang, S. Chen, M.N.A. Tawhid, Md. Hasanuzzaman, Md. Haider Ali and H. Ueno "An Intensity and Size Invariant Real Time Face Recognition Approach." International Conference on Image Analysis and Recognition (6th ICIAR) , pp. 502-511. Halifax, Canada: 2009 .
View More
110	Muhammad Ibrahim, Nasimul Noman and Hitoshi Iba "Time and Space Efficient Implementation of Robust Biclustering Algorithm (ROBA)." The 20th International Conference on Genome Informatics, Posters and Software Demonstrations, 2009 , pp. 1-2. Japan: University of Tokyo, 2009 .
111	Sifatur Rahim and Syed Hasan "Performance Evaluation of Fast-TCP and TCP-Westwood+ for Multimedia Streaming in Wireless Network." ICCIT 2009, in the 12th International Conference on Computer and Information Technology Dhaka: 2009 .
112	Iffat Sharmin Chowdhury, Jutheka Lahiry and Syed Hasan "Performance Evaluation of Datagram Congestion Contro Protocol (DCCP)." 12th International Conference on Computer and Information Technology 2009 .
113	Md. Rezaul Karm, Md. Jawaherul Alam and Md. Saidur Rahman "Straight-line grid drawings of label-constrained outerplanar graphs with O(n logn) area (Extended Abstract)." WALCOM , pp. 310-321. Kolkata: Lecture Notes in Computer Science, 5431, Springer, 2009 .
114	Muhammad Ibrahim, A. R. Chowdhury and H. M. H. Babu "On the Minimization of Complete Test Set of Reversible K-CNOT Circuits for Stuck at Fault Model." International Conference on Computer and Information Technology (ICCIT) , pp. 7-12. KUET, Khulna, Bangladesh: IEEE, 2008 .
View More
115	Muhammad Ibrahim, A. R. Chowdhury and H. M. H. Babu "Minimization of Complete Test Set of k-CNOT Circuits for Single and Multiple Stuck-at Fault Model." The 23rd IEEE International Symposium on Defect and Fault tolerance in VLSI Systems, 2008, , pp. 290-298. Cambridge (MA), USA: IEEE, 2008 .
View More
116	Syed Hasan, Laurent Lefevre, Zhiyi Huang, and Paul Werstein "Cross Layer Protocol Support for Live Streaming Media”." AINA 20008, the IEEE 22nd International Conference on Advanced Information Networking and Applications Okinawa, Japan: 2008 .
117	Syed Hasan, Laurent Lefevre, Zhiyi Huang, and Paul Werstein. "Supporting Large Scale eResearch Infrastructures with Adapted Live Streaming Capabilities”,." AusGrid 2008, the 6th Australasian Symposium on Grid Computing and e-Research Wollongong, Australia: 2008 .
118	Md. Rezaul Karim and Md. Saidur Rahman "Four-connected spanning subgraphs of doughnut graphs, Proc. of WALCOM 2008,." WALCOM , pp. 132-143. Dhaka: Lecture Notes in Computer Science, 4921, Springer, 2008 .
119	Md. Haider Ali "Volume Preserving Deformation Modelling of Human Facial Soft-Tissue." ASIAGRAPH-2007 , pp. 167-178. Akhihabara, Tokyo, Japan: 2007 .
View More
120	Md. Haider Ali, Masum Billah and Soheli Farhana "Pedestrian Navigation Simulation in Virtual Environment." Proceedings of the 2nd International Conference on Asian Simulation and Modeling (ASIMMOD) Chiang Mai, Thailand: 2007 .
View More
121	Syed Hasan, Zhiyi Huang, and Paul Werstein "Dynamic Buffer Active Tuning for Low Latency Streaming Media." ATNAC 2007, the 5th Australasian Telecommunication Networks and Applications conference Christchurch, New Zealand: 2007 .
122	Syed Hasan "Congestion Control for Data Limited Flows." NZCSRSC 2007, the 5th New Zealand computer science research students conference Hamilton, New Zealand: 2007 .
123	Md. Rezaul Karim and Md. Saidur Rahman "Straight-line grid drawings of planar graphs with linear area." Asia-Pacific Symposium on Visualization (APVIS) , pp. 109-112. Sydney, Australia: IEEE, 2007 .
124	A. Hossain, M. L. Rahman, F. Ahmed and Suraiya Pervin "New Approach to Automatic Segmentation of Bangla Speech.." 1st International Conference on Computer Processing of Bangla (ICCPB). 2006 .
125	Shaily Kabir and Md. Haider Ali "A Heuristic Approach of Establishing the Relationship between Full Width Half Maximum (FWHM) and Human Facial Shape Distortion in Image Metamorphosis." Proceedings of 8th International Conference on Computer and Information Technology (ICCIT2005) , pp. 159-163. Islamic University of Technology, Gazipur – 1704, Bangladesh: 2005 .
126	Md. Haider Ali, Md. Akteruzzaman and Mohammad Abu Nawar Siddique "Three-Dimensional Shape Reconstruction in Medical Imaging." Proceedings of 8th International Conference on Computer and Information Technology (ICCIT2005) , pp. 170-174. Islamic University of Technology, Gazipur – 1704, Bangladesh: 2005 .
127	Shaily Kabir and Md. Haider Ali "A Heuristic Approach of Establishing the Relationship between Full Width Half Maximum (FWHM) and Human Facial Shape Distortion in Image Metamorphosis." 8th International Conference on Computer and Information Technology (ICCIT) , pp. 159-163. Dhaka, Bangladesh: IEEE, 2005 .
128	S. M. Khaled, A. K. Biswas, M. L. Rahman and Suraiya Pervin "An Analysis on Human Resource Development in the ICT Sector of Bangladesh.." International Conference on Computer and Information Technology (ICCIT 2005). Dhaka: 2005 .
129	Suraiya Pervin and Subrata Kr. Aditya "A Pipelined Architecture for Computing Eigenvectors.." International Conference on Computer and Information Technology (ICCIT 2005). Dhaka: 2005 .
130	Suraiya Pervin and Subrata Kr. Aditya "An Area-efficient Equalizer based on the Complex TLMS.." International Conference on Computer and Information Technology (ICCIT 2005). Dhaka: 2005 .
131	S.M. Ashraful Kadir, Tazrian Khan and Md. Haider Ali "Fasial Soft-Tissue Modeling using Finite Element Method." Proceedings of 7th International Conference on Computer and Information Technology (ICCIT2004) BRAC University Dhaka, Bangladesh: 2004 .
132	Md, Haider Ali and Mohammad Abu Nawar Siddique "Motion Capturing Tool for Realistic Character Animation." The Proceedings of the 10th International Conference on Virtual System and MultiMedia (VSMM2004) , pp. 899-908. Softopia-Japan, Ogaki, Gifu-500-8727, Japan: 2004 .
View More
133	Md, Haider Ali, Md. Alamgir Hossain and Mohammad Abu Nawar Siddique "Prediction of the Missing Part of Human Face." The Proceedings of the 10th International Conference on Virtual System and MultiMedia (VSMM2004) , pp. 962-969. Softopia-Japan, Ogaki, Gifu-500-8727, Japan: 2004 .
View More
134	Md. Saiful Islam, Lutfar Rahman, Muhammad Asif Hossain Khan, B.M. Mainul Hossain, Muhammad Rezaul Karim and Abdullah Al Mahmud "Digital Signature: Does It Really Work for Electronic Documents?." 8th IEEE International Multi-topic Conference (INMIC) , pp. 473–479. Lahore, Pakistan: 2004.12 .
135	Muhammad Asif Hossain Khan, Mohammad Abu Nawar Siddique, Mohammad Asad-uz-zaman, Safwan Mahmud Khan and Syed Shahed Kabir Robin "A Different Approach to Barrier Synchronization Mechanism for the BSP Model on Message Passing Architecture." 10th International Conference on Virtual Systems and Multimedia (VSMM) , pp. 584–592. Ogaki City, Japan: 2004.11 .
136	Hafiz Md. Hasan Babu, Mosarrat Jahan and Mohammad Abdullah-Al-Wadud "A Modified Approach of Quine-McClusky Method to Minimize the Multiple-Output Functions." 7th ICCIT 2004 , pp. 389- 391. 2004 .
137	Muhammad Asif Hossain Khan, Redwan Zakariah, Mohammed Shafiul Alam Khan, Md. Iftekharul Amin and Khan Monirul Alam "Cache Coherency: The Supreme Influencing Sphere for Maintaining Memory Consistency in Shared Memory Multiprocessors." 7th International Conference on Computer and Information Technology (ICCIT) , pp. 203–207. Dhaka, Bangladesh: 2004.12 .
138	Muhammad Asif Hossain Khan, Mohammad Abu Nawar Siddique, Mohammad Asad-uz-zaman, Safwan Mahmud Khan and Syed Shahed Kabir Robin "A better-reliable faster barrier synchronization mechanism for the BSP model." 7th International Conference on Computer and Information Technology (ICCIT) , pp. 564–568. Dhaka, Bangladesh: 2004.12 .
139	Muhammad Asif Hossain Khan, Ahammad Shafi, Mahbubul Azam Khan, Md. Minhajul Abedin, Mohammad Shahiduzzaman, Pushpita Nomani, Quazi Ashfaq-ur Rahman and Wahid Raihanur Rahman "OS71: An Instructional Operating System with a Perspicuous and Painless Design." 7th International Conference on Computer and Information Technology (ICCIT) , pp. 849 – 854. Dhaka, Bangladesh: 2004.12 .
140	Suraiya Pervin, and Subrata Kr. Aditya "A CORDIC Realization of the Complex LMS based Adaptive Equalizer.." Conference of Bangladesh Electronics Society. Dhaka: 2003 .
141	Suraiya Pervin, Taslim Taher and Tariqul Islam "CORDIC Realization of the ADFE.." International Conference on Computer and Information Technology (ICCIT 2003). Dhaka: 2003 .
142	Suraiya Pervin and Subrata Kr. Aditya "A High Speed Architecture for Computing Eigenvalues of Data Covariance Matrix.." International Conference on Computer and Information Technology (ICCIT 2003). Dhaka: 2003 .
143	Shaily Kabir, Mahmud Karim and Hafiz Md. Hasan Babu "A Heuristic Method for Simplification of Single Output Logic Functions Using Optimal Ordering of Input Variables." 2nd International Conference on Electrical Engineering (ICEE) , pp. 66-73. Dhaka, Bangladesh: Electrical Engineering Division, Institution of Engineers, Bangladesh, 2002 .
144	Md. Haider Ali and Ms. Maria Wahid Chowdhury "IT Sector in Bangladesh: Infrastructure and Investment." The BISS Young Scholars Seminar on Information Technology and Youth Enterprises in Bangladesh, Organized by the Bangladesh Institute of International and Strategic Studies (BISS) Dhaka, Bangladesh: 2002 .
145	Suraiya Pervin and Subrata Kr. Aditya "A Latency Free Architecture for VSLMS based Adaptive Equalizer.." International Conference on Computer and Information Technology (ICCIT 2002). (2002) Dhaka: 2002 .
146	Suraiya Pervin, A. S. Dhar and M. Chakraborty "An Area-efficient Pipelined Architecture for the Trigonometric LMS based Adaptive Equalizer.." International Conference on Communications and Information Technology (ICCIT 2001). Dhaka: 2001 .
147	Suraiya Pervin, A. S. Dhar and M. Chakraborty "A High Speed CORDIC based Architecture for the Complex Adaptive Equalizer.." International Conference on Energy, Automation and Information Technology (EAIT 2001). IIT, Kharagpur, India: 2001 .
148	Suraiya Pervin, M. Chakraborty and T. S. Lamba "A Hyperbolic LMS Algorithm for CORDIC based Realization.." IEEE workshop on Statistical Signal Processing (SSP 2001). Singapore: 2001 .
149	Suraiya Pervin, M. Chakraborty and A. S. Dhar "A Trigonometric Formulation of the LMS Algorithm." National conference on Communication (NCC 2001). Kanpur, India: 2001 .
150	Suraiya Pervin, M. Chakraborty and A. S. Dhar "CORDIC Realization of the Transversal Adaptive Filter using a Trigonometric LMS Algorithm.." IEEE Conference on Acoustics, Speech and Signal Processing (ICASSP 2001). USA: 2001 .
151	Suraiya Pervin, A. S. Dhar and M. Chakraborty "Pipelining of VSLMS Based Adaptive Equalizer with Minimum Output Latency.." International conference on Image and Signal Processing (ICISP 2001). Morocco: 2001 .
152	Suraiya Pervin, A. S. Dhar and M. Chakraborty "CORDIC Realization of the LMS based Complex Adaptive Equalizer.." IEEE symposium on Signal, Circuits and Systems (SCS 2001) Romania: 2001 .
153	Suraiya Pervin, A. S. Dhar and M. Chakraborty "A Systolic Architecture for VSLMS based Adaptive Equalizer.." IEEE conference on Recent Trend in Communication (EUROCON 2001). Slovakia: 2001 .
154	Syed Miraj Momin, Md. Rafiqul Islam and Md. Rezaul Karim "An Approved Algorithm for Query Optimization using Generalized Outer-Join and Operator Selection in Bottom-up Trees,." International Conference on Computer and Information Technology (ICCIT) , pp. 77-82. Dhaka: 2001 .
155	Saifuddin Md. Tareeq, Md. Rafiqul Islam and Md. Rezaul Karim "Improved techniques for query optimization using eliminating duplicates generated in transformation-based join enumeration." International Conference on Computer and Information Technology (ICCIT) , pp. 83-88. Dhaka: 2001 .
156	Ali Md. Haider and Toyohisa Kaneko "Realistic 3D Head Modeling from Video Captured Images and CT Data." The Proceedings of IEEE EMBS International Conference on Information Technology Applications in Bio-Medicine , pp. 238-243. Virginia, USA: 2000 .
View More
157	Ali Md. Haider and Toyohisa Kaneko "Hair Shape Modeling from Video Captured Images and CT Data." The Proceedings of ICAT2000 , pp. 52-57. Taipei, Taiwan: 2000 .
View More
158	Suraiya Pervin, A. S. Dhar and M. Chakraborty "A Pipelined Architecture for KLT based LMS Adaptive Equalizer.." International Conference on Communications, Computers and Devices (ICCCD 2000). IIT, Kharagpur, India: 2000 .
159	Suraiya Pervin,, M. Chakraborty and A. S. Dhar "Systolizing the Adaptive Decision Feedback Equalizer using a Symbolic State Space Formulation.." European Conference of Signal Processing (EUSIPCO 2000) Finland: 2000 .
160	Suraiya Pervin, M. Chakraborty and A. S. Dhar "Pipelining the Adaptive Decision Feedback Equalizer with Zero Latency. National Conference on Communication (NCC 2000). (2000)." National Conference on Communication (NCC 2000). IIT, Delhi, India: 2000 .
161	Ali Md. Haider and Toyohisa Kaneko "Automatic Reconstruction of 3D Human Face from CT and Color Photographs." The Proceedings of MVA-98 , pp. 127-130. Chiba, Japan: 1998 .
162	Md. Rezaul Karim, Pallab Dasgupta, P. P. Chakraborty and Dipankar Sarkar "A Prolog Program for Sliding Window Protocol Analysis." National Conference on Computer and Information Technology , pp. 198-2003. Dhaka: 1997 .
163	M. A. Hussain, M. O. Tokhi and Suraiya Pervin "Genetic Algorithms and Conventional Identification Schemes for Adaptive Active Control.." International conference on Control, Automation, Robotics and vision (ICARCV’ 96). Singapore: 1996 .
164	Arnab Paul Joy, Mosarrat Jahan, Upama Kabir and Sanjoy Kumar Mahato "Precise Estimation of Local Probabilities for Bayesian Attack Graph Analysis." IEEE IEMCON'2021 , pp. 80-85. 2021 .
165	Muhammad Aminur Rahaman, Md Mahin, Md Haider Ali and Md Hasanuzzaman "BHCDR: Real-Time Bangla Handwritten Characters and Digits Recognition using Adopted Convolutional Neural Network." 1st International Conference on Advances in Science, Engineering and Robotics Technology (ICASERT) , pp. 1-6. Dhaka, Bangladesh: May 2019 .
View More
166	Sofiul Azam Sony, Tasfi Zaman, Md Kamrul Islam, Jesan Ahammed Ovi and Md Ashraful Islam "eLearn++: An effective Incremental Learning Approach for Brain Tumor Detection." 2021 2nd International Conference for Emerging Technology (INCET) , pp. 1--8. IEEE: 2021 .
167	Jesan Ahammed Ovi, Md Ashraful Islam and Jannatul Ferdosh Nima "An Efficient Approach for Mining Weighted Frequent Patterns from Data Stream." 2021 2nd International Conference for Emerging Technology (INCET) , pp. 1--10. IEEE: 2021 .
168	Abu Naser, Nusrat Sultana, Md Ashraful Islam and Jesan Ahammed Ovi "Weighted Clickstream Mining Using Pre-order Linked Web-Access Pattern Tree." 2021 2nd International Conference for Emerging Technology (INCET) , pp. 1--11. IEEE: 2021 .
169	Hyame Assem Alameddine, Chadi Assi, Mosaddek Hossain Kamal Tushar and Jia Yuan Yu "Low-Latency Service Schedule Orchestration in NFV-based Networks." 2019 IEEE Conference on Network Softwarization (NetSoft) , pp. 378-386. 2019 .
View More
170	Sajib Kumar Mistry, Mosaddek Hossain Kamal and Dilip Mistry "Semantic Discovery of Web Services through Social Learning." The 2012 Iberoamerican Conference on Electronics Engineering and Computer Science , pp. 167-177. 2012 .
View More
171	Nazma Tara, Md. Kamal IbneSufian, and Hafiz Md. Hasan Babu "“Nanotechnology-Based Efficient Fault Tolerant Decoder in Reversible Logic”." IEEE International WIE Conference on Electrical and Computer Engineering (WIECON-ECE) , pp. 60-63. Dehradun, India: 2017 .
172	Sheikh Muhammad Sarwar and Mosaddek Hossain Kamal "Integration of Novel Image Based Features into Markov Random Field Model for Information Retrieval." 2012 26th International Conference on Advanced Information Networking and Applications Workshops , pp. 827-832. 2012 .
View More
173	ZarrinTasnimSworna, Mubin Ul Haque, Hafiz Md. Hasan Babu and Lafifa Jamal "“A Cost-Efficient LUT-Based BCD Adder Design”." Future Technologies Conference 2017 (FTC 2017) Canada: 2017 .
174	Mohammad Shahidul Hasan, Mosaddek Hossain Kamal and M Lutfar Rahman "A NEW ADAPTIVE HYBRID ROUTING STRATEGY FOR DATAGRAM SERVICE." Int. Conf. on Computer and Information Technology (ICCIT2001) , pp. 4. Dhaka: 2001 .
View More
175	Hafiz Md. Hasan Babu, Lafifa Jamal, SayantonVhaduriDibbo and Ashis Kumar Biswas "“Area and Delay Efficient Design of a Quantum Bit String Comparator”." IEEE Computer Society Annual Symposium on VLSI (ISVLSI 2017) , pp. 51-56. Bochum, Germany: 2017 .
176	Reem Kateb, Parisa Akaber, Mosaddek H. K. Tushar, Mourad Debbabi and Chadi Assi "Delay aware measurements gathering in WAMS communication network." 2017 IEEE Global Conference on Signal and Information Processing (GlobalSIP) , pp. 1090-1094. 2017 .
View More
177	ZarrinTasnimSworna, Mubin Ul Haque, Hafiz Md. Hasan Babu, Lafifa Jamal and AshisKumer Biswas "“An Efficient Design of an FPGA-Based Multiplier Using LUT Merging Theorem”." IEEE Computer Society Annual Symposium on VLSI (ISVLSI 2017) , pp. 116-121. Bochum, Germany: 2017 .
178	Mosaddek Hossain Kamal Tushar and Chadi Assi "Volt-VAR optimization by using electric vehicle, renewable energy and residential load-shifting." 2016 IEEE International Conference on Smart Grid Communications (SmartGridComm) , pp. 460-465. Dallas: 2016 .
View More
179	Mosaddek Hossain Kamal Tushar and Chadi Assi "Optimal electricity pricing in a microgrid network." 2016 IEEE/PES Transmission and Distribution Conference and Exposition (T D) , pp. 1-5. 2016 .
View More
180	Md. Mahmudul Hasan, Mosarrat Jahan, Shaily Kabir and Christian Wagner "A Fuzzy Logic-Based Trust Estimation in Edge-Enabled Vehicular Ad Hoc Networks." 2021 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE) , pp. 1--8. IEEE, 2021 .
181	Shaikhum Monira, Upama Kabir, Mosarrat Jahan and Uchswas Paul "An Efficient and Secure Handover Mechanism for SDN-Enabled 5G HetNet." IEEE BlackSeaCom , pp. 1-6. IEEE, 2021 .
"""

# Regular expression to capture authors and titles
pattern = r"^\d+\s+([\w.,\s]+?)\s+(“?.+?\.?)\s+[A-Z][a-z]+:.*?,\s*\d{4}\s*\."
matches = re.findall(pattern, text, re.MULTILINE)

# Write the data to a CSV file
csv_filename = "_title_authors_DU.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Authors", "Title"])
    for authors, title in matches:
        writer.writerow([authors.strip(), title.strip()])

print(f"Data successfully written to {csv_filename}")
