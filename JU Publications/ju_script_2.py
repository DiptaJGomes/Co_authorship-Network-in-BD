import re
import csv

# Provided text
text = """
Tanjim Taharat AURPA; Samiha Maisha Jeba; Md Shoaib Ahmed; Mohammad Aman Ullah; Maria Mehzabin; Md Musfique Anwar. Bangla_MER: A Unique Dataset for Bangla Mathematical Entity Recognition. Data in Brief, 2024 (Accepted). (Journal Rank: Q2, SCI). 

Tabia Tanzin Prama, Md. Saiful Islam, Md Musfique Anwar, Ifrat Jahan. AI-Enabled Deep Depression Detection and Evaluation Informed by DSM-5-TR. IEEE Transactions on Computational Social Systems. 2024 (Accepted) (Journal Rank: Q1, SCI, IF: 5.0).  

Sarmistha Sarna Gomasta, Aditi Dhali, Tahlil Tahlil, Md Musfique Anwar, ABM Shawkat Ali. PharmaChain: Blockchain-based Drug Supply Chain Provenance Verification System. Heliyon, Volume , Issue , 2023 (Accepted). (Journal Rank: Q1, SCI, IF: 3.776). DOI:

Tanjim Taharat Aurpa, Md Shoaib Ahmed, Richita Khandakar Rifat, Md Musfique Anwar, ABM Shawkat Ali. UDDIPOK: A reading comprehension based question answering dataset in Bangla language. Data in Brief, Volume 47, 2023. (Journal Rank: Q2, SCI). DOI: https://www.sciencedirect.com/science/article/pii/S2352340923000513

Mahmuda Ferdous, Md Musfique Anwar. Identification of Influential Users in Online Social Network: A brief overview. Journal of Computer and Communications, Volume 11, Issue: 7, 2023.
DOI:
 
Rukaiya Habib, Mahmuda Ferdous, Md Musfique Anwar. Creating Bengali Freebase Using Wikidata. Journal of Computer and Communications, Volume 11, Issue: 5, 2022.
DOI: https://www.scirp.org/journal/paperinformation.aspx?paperid=125244 

Tanjim Taharat Aurpa, Richita Khandakar Rifat, Md Shoaib Ahmed, Md Musfique Anwar, ABM Shawkat Ali. Reading comprehension based question answering system in Bangla language with transformer-based learning. Heliyon, Volume 8, Issue 10, 2022. (Journal Rank: Q1, SCI, IF: 3.776). DOI: https://www.sciencedirect.com/science/article/pii/S2405844022023404

Sarmistha Sarna Gomasta, Aditi Dhali, Md Musfique Anwar, Iqbal H Sarker. Query-oriented topical influential users detection for top-k trending topics in twitter. Applied Intelligence, 2022. (Journal Rank: Q2, SCI, IF: 5.019). DOI: https://link.springer.com/article/10.1007/s10489-022-03582-5

Khandaker Tayef Shahriar, Muhammad Nazrul Islam, Md. Musfique Anwar, Iqbal H. Sarker. COVID-19 analytics: Towards the effect of vaccine brands through analyzing public sentiment of tweets. Informatics in Medicine Unlocked, Volume 31, 2022. (Journal Rank: Q2, SCI, IF: 2.11). DOI: https://www.sciencedirect.com/science/article/pii/S2352914822001149 

Debjany Chakraborty, Md. Musfique Anwar. Framework Development using Data Mining Techniques to Predict Mortality Risk during Pandemic.  Journal of Computer and Communications, 2022. 

Badhan  Chandra  Das, Md. Musfique Anwar, Md. Al-Amin Bhuiyan, Iqbal H. Sarker, Salem A. Alyami, and Mohammad Ali Moni. Attribute Driven Temporal Active Online Community Search.  IEEE Access, Volume 9, pp. 93976 - 93989 (Journal Rank: Q1, SCI, IF:3.745). DOI: https://ieeexplore.ieee.org/document/9467368 

Md Shoaib Ahmed, Tanjim Taharat Aurpa, and Md. Musfique Anwar. Detecting Sentiment Dynamics and Clusters of Twitter Users for Trending Topics in COVID-19 Pandemic. PLoS ONE, Volume: 16, Issue: 8. (Journal Rank: Q1, SCI, IF:3.24). DOI: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0253300

Iqbal Sarker, Rony Ripan, Minhaz Hossain, Md Musfique Anwar. An Optimal K-Means Clustering based Anomaly Detection Model for Effectively Predicting Heart Disease. In SN Computer Science (Springer), SN COMPUT. SCI. 2, 112 (2021). DOI: https://link.springer.com/article/10.1007%2Fs42979-021-00518-7

Md. Habibur Rahman, Tabia Tanzin Prama and Md Musfique Anwar. Modeling Information Credibility in Time-Specific Online Social Media based on Structural and Attribute Properties. Accepted to International Journal of Computer Information Systems and Industrial Management Applications, 2021. (Journal Rank: Q3/Q4)

Tasnim Siraj, Md. Musfique Anwar and Md. Al-Amin Bhuiyan.  Inferring And Tracking User Interest In Web-based Social Network. Accepted to the International Journal of Scientific & Technology Research. (Journal Rank: Q3), 2021.

Md. Masum Bhuiyan, Kamrul Hasan, Ahmed Ashfaq Hamid Fardin and Md. Musfique Anwar. Dynamic Multilevel Clustering for Two-Dimensional Cutting and Packing Problems. Submitted to Computers and Operations Research. (Journal Rank: Q1, SCI, IF:3.424)

Badhan Chandra Das, Md Musfique Anwar, and Iqbal Sarker. Location-based Temporal Sentiment Analysis to Predict Election Outcome. Submitted to Springer International Journal of Data Science and Analytics. 

Shifat Jahan Setu, Tahmina Islam, Md. Musfique Anwar, Md. Al-Amin Bhuiyan. TTRank: A Temporal Model to Rank Online Twitter Users. Accepted to International Journal of Automation, AI and Machine Learning, 2020.

Arnab Shanta Anu, Md Shovon, Md. Musfique Anwar. Survey on Sentiment Analysis in Bangla Language. Submitted to International Journal of Automation, AI and Machine Learning. 
 
Rukaiya Habib, and Md. Musfique Anwar. Finding out noisy patterns for relation extraction of Bangla sentences. International Journal on Natural Language Computing (IJNLC) Vol.9, No.1, February 2020. ISSN 2319 - 4111. DOI: https://aircconline.com/ijnlc/V9N1/9120ijnlc02.pdf 

Badhan Chandra Das, and Md. Musfique Anwar. Predicting election outcome from social media data. International Journal on Natural Language Computing (IJNLC) Vol.9, No.1, February 2020. ISSN 2319 - 4111. DOI: https://aircconline.com/ijnlc/V9N1/9120ijnlc03.pdf

Swarna Das, and Md. Musfique Anwar. Discovering Topic Oriented Highly Interactive Online Community. Frontiers in Big Data, Vol. 2, May 2019. ISSN 1573-1413. (Frontiers Journal Rank: Q2, SCI) DOI: https://www.frontiersin.org/articles/10.3389/fdata.2019.00010/full

Md. Musfique Anwar, Chengfei Liu, and Jianxin Li. Discovering and tracking query oriented active online social groups in dynamic information network. World Wide Web, Vol. 22(4) pp. 1–36, August 2018. ISSN 1573-1413. (Journal Rank: Q1/Q2, SCI, IF:1.815). DOI: https://doi.org/10.1007/s11280-018-0627-5

Md. Musfique Anwar. Measuring the Future Popularity of a Tweet containing Novel Topics. IJCSIS International Journal of Computer Science and Information Security, VOL.16 No.11, November 2018, pp. 166–173.

Md. Musfique Anwar. Bangla to English Machine Translation using Fuzzy Logic. IJCSIS International Journal of Computer Science and Information Security, VOL.16 No.11, November 2018, pp. 156–165.

Shibli Syeed Ashrafi, Md. Humayun Kabir, Md. Musfique Anwar, and A. K. M. Noman. English to Bangla Machine Translation System Using Context-Free Grammars. IJCSI International Journal of Computer Science Issues (Impact Factor 0.242), Vol. 10, Issue 3, No 2, May 2013, pp. 144–153.

Md. Musfique Anwar, Nasrin Sultana Shume, and Md. Al-Amin Bhuiyan. Structural Analysis of Bangla Sentences of Different Tenses for Automatic Bangla Machine Translator. IJCSIS Inter-national Journal of Computer Science and Information Security, VOL.8 No.9, December 2010, pp. 70–75.

Tahmina Khatoon, Md. Musfique Anwar, Nasrin Sultana Shume, Md. Mizanur Rahman. Parcel Management System using GPS Tracking Unit. IJCSIS International Journal of Computer Science and Information Security, VOL.8 No.9, December 2010, pp. 183–189.

Md. Musfique Anwar, Nasrin Sultana Shume, PKM Moniruzzaman and Md. Al-Amin Bhuiyan. Recognition of Printed Bangla Document from Textual Image Using Multi-Layer Perceptron (MLP) Neural Network. IJCSIS International Journal of Computer Science and Information Se-curity, VOL.8 No.1, April 2010, pp. 254–259.

Md. Musfique Anwar, Mohammad Zabed Anwar, and Md. Al-Amin Bhuiyan. “Syntax Anal-ysis and Machine Translation of Bangla Sentences”. IJCSNS International Journal of Computer Science and Network Security, VOL.9 No.8, August 2009, pp. 317–326.

Md. Musfique Anwar and Md. Mizanur Rahman. Offline Divisible E-Cash. Journal of Com-puter Science, IBAIS University, June 2007: Volume-1, Number-1, pp. 48–52
CONFERENCE PAPER
Serajum Monira, Nurun Nahar Fiha, Md Musfique Anwar. Deep Learning Based Bangladeshi Currency Coin Recognition. 4th International Conference on Robotics, Electrical and Signal Processing Techniques (ICREST), 2025, Bangladesh.
 
Md Habibur Rahman, Nabilah Hossain Sarker, Md Musfique Anwar, Mufti Mahmud, David Brown, Muhammad Arifur Rahman. A Gaussian Process Framework for Prognostication and Visualization in Dermatological Oncology. 31st International Conference on Neural Information Processing (ICONIP), 2024, Auckland, New Zealand.
 
Alif Al Hasan, Md Musfique Anwar. Redefining POI Popularity: Integrating User Preferences and Recency for Enhanced Recommendations. 2nd International Conference on Machine Intelligence and Emerging Technologies (MIET), 2024, Bangladesh.
 
Khandoker Nosiba Arifin, Sayma Rupa, Md Musfique Anwar, Israt Jahan. Lemon and Orange Disease Classification using CNN-Extracted Features and Machine Learning Classifier. 3rd International Conference on Computing Advancements 2024 (ICCA 2024), Bangladesh.
 
Nishat Tasnim, Asraf Ullah Rahat, Md Musfique Anwar. Retrieving Top k% Relevant Patterns for Relation Extraction in Bangla using Distant Supervision. 3rd IEEE International Conference on Signal Processing, Information, Communication and Systems, 2024, Bangladesh.
 
Umme Faria Moon, MD Ahsan Rasel, Md Musfique Anwar. Modeling The Sharing and Diffusion of Fake News in Social Media. 3rd IEEE International Conference on Signal Processing, Information, Communication and Systems, 2024, Bangladesh.
 
Tanjina Camelia, Faizur Fahim, Md Musfique Anwar. A Regularized LSTM Method for Detecting Fake News Articles. 3rd IEEE International Conference on Signal Processing, Information, Communication and Systems, 2024, Bangladesh.
 
Tabia Tanzin Prama, Md Musfique Anwar. SobdoKrom: An Unsupervised Bengali Keyword Extraction Model using Pre-trained Large Language Model. 23nd International Conference on Hybrid Intelligent Systems (HIS 2023).

 
Tabia Tanzin Prama, Md Musfique Anwar. Sylheti to Standard Bangla Neural Machine Translation: A Deep Learning-Based Dialect Conversion Approach. 23nd International Conference on Hybrid Intelligent Systems (HIS 2023).

 
Tabia Tanzin Prama, Al Amin Biswas, Md Musfique Anwar. Deep Learning-Based Classification of Conference Paper Reviews: Accept or Reject?. International Conference on Intelligent Systems Design and Applications (ISDA 2023).

 
Sajjad Hossain, Md Mahfuzur Rahman and Md Musfique Anwar. Interference-aware VM Placement in Cloud (Poster Paper). In 43rd IEEE International Conference on Distributed Computing Systems, 2023. DOI: https://ieeexplore.ieee.org/document/10272542

 
Md Mahbubur Rahman, Badhan Chandra Das, Al Amin Biswas, Md Musfique Anwar. Predicting Participants' Performance in Programming Contests using Deep Learning Techniques. 22nd International Conference on Hybrid Intelligent Systems (HIS 2022). 
DOI: https://link.springer.com/chapter/10.1007/978-3-031-27409-1_15

 
Nowshin Tasnim, Md Musfique Anwar, Iqbal H Sarker. A Stacked Ensemble Spyware Detection Model Using Hyper-Parameter Tuned Tree Based Classifiers. Machine Intelligence and Emerging Technologies (MIET), 2022. DOI: https://link.springer.com/chapter/10.1007/978-3-031-34622-4_32

 
Khandaker Tayef Shahriar, Md Musfique Anwar, Iqbal H Sarker. Aspect Based Sentiment Analysis of COVID-19 Tweets Using Blending Ensemble of Deep Learning Models. Machine Intelligence and Emerging Technologies (MIET), 2022. 
DOI: https://link.springer.com/chapter/10.1007/978-3-031-34619-4_31

 
Tanjim Taharat Aurpa, Md Shoaib Ahmed, Rifat Sadik, Sabbir Anwar, Md Abdul Mazid Adnan and Md Musfique Anwar. Progressive Guidance Categorization Using Transformer-Based Deep Neural Network Architecture. Accepted to the 21st International Conference on Hybrid Intelligent Systems (HIS 2021). DOI: https://link.springer.com/chapter/10.1007/978-3-030-96305-7_32

 
Raihan Jamil, Mohammad Abdullah Al Nayeem Khan and Md Musfique Anwar. Topic Oriented Hate Speech Detection. Accepted to the 21st International Conference on Hybrid Intelligent Systems (HIS 2021). DOI: https://link.springer.com/chapter/10.1007/978-3-030-96305-7_34

 
Nusrat Jahan Euna, Syed Md Minhaz Hossain, Md. Musfique Anwar, Iqbal H Sarker. Content-based Spam Email Detection Using N-gram Machine Learning Approach. Taylor & Francis, 2021. DOI: https://www.preprints.org/manuscript/202109.0236/v1

 
Nazifa Mosharrat, Iqbal H. Sarker, Md Musfique Anwar, Muhammad Nazrul Islam, Paul Watters, and Mohammad Hammoudeh. Automatic Malware Categorization based on K-Means Clustering Technique. In Lecture Notes on Data Engineering and Communications Technologies , Publisher: Springer, 2021. DOI: https://link.springer.com/chapter/10.1007/978-981-16-6636-0_49

 
Sourav Adhikary, Md Musfique Anwar, Mohammad Jabed Morshed Chowdhury and Iqbal H. Sarker. Genetic Algorithm-based Optimal Deep Neural Network for Detecting Network Intrusions. Accepted in International Conference on Machine Intelligence and Data Science Applications (MIDAS) 2021, Bangladesh.

 
Md. Habibur Rahman, Tabia Tanzin Prama and Md Musfique Anwar. Modeling Topic Specific Credibility in Twitter based on Structural and Attribute Properties (Poster paper). Accepted to the 6th International Conference on Engineering Research, Innovation and Education (ICERIE 2021), Sylhet, Bangladesh.

 
Tabia Tanzin Prama and Md Musfique Anwar. Modeling Topic Specific Credibility in Twitter based on Structural and Attribute Properties (Poster paper). Accepted to the Biosciences Symposium, Biochemistry and Cell Biology Society, Jacobs University Bremen, Germany, 2021.

 
Md. Habibur Rahman, Tabia Tanzin Prama and Md Musfique Anwar. Modeling Topic Specific Credibility in Twitter based on Structural and Attribute Properties. Proceedings of the 20th International Conference on Hybrid Intelligent Systems (HIS 2020), pp. 580–589, 14-16 December, 2020, USA. DOI: https://link.springer.com/chapter/10.1007%2F978-3-030-73050-5_57

 
Rony Chowdhury Ripan, Iqbal H. Sarker, Md. Hasan Furhad, Md Musfique Anwar, and Mohammed Moshiul Hoque. An Effective Heart Disease Prediction Model based on Machine Learning Techniques. Proceedings of the 20th International Conference on Hybrid Intelligent Systems (HIS 2020), pp. 280–288, 14-16 December, 2020, USA. DOI: https://link.springer.com/chapter/10.1007%2F978-3-030-73050-5_28

 
Rony Chowdhury Ripan, Iqbal H. Sarker, Md Musfique Anwar, Fazle Rahat, Moshiul Hoque and Muhammad Sarfraz. An Isolation Forest Learning Based Outlier Detection Approach for Effectively Classifying Cyber Anomalies. Proceedings of the 20th International Conference on Hybrid Intelligent Systems (HIS 2020), pp. 270–279, 14-16 December, 2020, USA. DOI: https://link.springer.com/chapter/10.1007/978-3-030-73050-5_27

 
Badhan Chandra Das , Md Musfique Anwar and Iqbal H. Sarker. Reducing Social Media Users’ Biases to Predict the Outcome of Australian Federal Election 2019. Proceedings of 7th IEEE CSDE 2020, the Asia-Pacific Conference on Computer Science and Data Engineering, 14-16 December, 2020, Gold Coast, Australia. (Developing Country Researcher Award) DOI: https://ieeexplore.ieee.org/document/9411633

 
Tanzim Mahfuz, Tasneem Farhana Suha and Md Musfique Anwar. Reducing Wrong Labels using Conflict Score in Distant Supervision for Relation Extraction in Bangla Language. Proceedings of the 7th IEEE CSDE 2020, the Asia-Pacific Conference on Computer Science and Data Engineering, 14-16 December, 2020, Gold Coast, Australia. DOI: https://ieeexplore.ieee.org/document/9411604

 
Aditi Dhali, Sarmistha Sarna Gomasta, Md Musfique Anwar and Iqbal H. Sarker. Attribute-driven Topical Influential Users Detection in Online Social Networks. Proceedings of the 7th IEEE CSDE 2020, the Asia-Pacific Conference on Computer Science and Data Engineering, 14-16 December, 2020, Gold Coast, Australia. DOI: https://ieeexplore.ieee.org/document/9411637

 
Murad Hossen, Tamanna Afrose Tamanna, Atashi Ghosh and Md Musfique Anwar. Classification of Social Media Users Based on Temporal Behaviors and Interests. Accepted to the 2nd International Conference on Communication and Intelligent Systems (ICCIS 2020), India. DOI: https://link.springer.com/chapter/10.1007%2F978-981-16-1089-9_72

 
Tanjim Taharat Aurpa, Md. Shoaib Ahmed and Md. Musfique Anwar. Online Topical Clusters Detection for Top-k Trending Topics in Twitter. Accepted to IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM) 2020, pp. 573–577, 7-10 December, 2020, Hague, Netherlands. DOI: https://ieeexplore.ieee.org/document/9381305

 
Badhan Chandra Das, Md Musfique Anwar and Md. Al-Amin Bhuiyan. Attribute Driven Temporal Local Active Online Community Detection. Accepted to IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM) 2020, pp. 619–622, 7-10 December, 2020, Hague, Netherlands. DOI: https://ieeexplore.ieee.org/document/9381442

 
Md. Akib Zabed Khan, Saif Mahmud Parvez, Md. Mahbubur Rahman and Md. Musfique Anwar. Efficient Advertisement Slogan Detection and Classification Using a Hierarchical BERT and BiLSTM-BERT Ensemble Model. Accepted to The 3rd International Conference on Intelligent Computing and Optimization (ICO’2020), pp. 964–975, 17-18 December, 2020, Hua Hin, Thailand. DOI: https://link.springer.com/chapter/10.1007%2F978-3-030-68154-8_81

 
Tanjim Taharat Aurpa, Md. Shoaib Ahmed and Md. Musfique Anwar. Clustering Active Users in Twitter Based on Top-k Trending Topics. (Extended Abstract - 3 pages) Accepted to The 9th International Conference on Complex Networks and their Applications, 1-3 December, 2020, Madrid, Spain.

 
Badhan Chandra Das, Md Musfique Anwar and Md. Al-Amin Bhuiyan.  Query Oriented Temporal Active Community Search. (Extended Abstract - 3 pages) Accepted to The 9th International Conference on Complex Networks and their Applications, 1-3 December, 2020, Madrid, Spain. 

 
Humayra Ferdous, Tasnim Siraj, Shifat Jahan Setu, Md Musfique Anwar and Muhammad Arifur Rahman.  Machine Learning Approach Towards Satellite Image Classification. Proceedings of the 2nd International Conference on Trends in Computational and Cognitive Engineering(TCCE-2020), pp. 627-637, 17-18 December, 2020, Dhaka, Bangladesh. DOI: https://link.springer.com/chapter/10.1007/978-981-33-4673-4_51

 
Md. Shoaib Ahmed, Tanjim Taharat Aurpa, and Md. Musfique Anwar. Query Oriented Topical Clusters Detection for Top-k Trending Topics in Twitter. Accepted to IEEE 8th R10 Humanitarian Technology Conference (R10-HTC) 2020, 5-7 December, 2020, Sarawak, Malaysia. DOI: https://ieeexplore.ieee.org/abstract/document/9357047

 
Tanjim Taharat Aurpa, Fatema Khan and Md. Musfique Anwar. Discovering and Tracking Query Oriented Topical Clusters in Online Social Networks. Proceedings of the IEEE Region 10 Symposium (TENSYMP) 2020, pp. 1054-1057, 5-7 June, 2020, Dhaka, Bangladesh. (Best Paper Award) DOI: https://ieeexplore.ieee.org/document/9230994

 
Sudeepto Mohanta, Sarmistha Sarna, Aditi Dhali and Md Musfique Anwar. Identification of Query-Oriented Influential Users in Online Social Platform. Proceedings of the IEEE Region 10 Symposium (TENSYMP) 2020, pp. 973-976, 5-7 June, 2020, Dhaka, Bangladesh. DOI: https://ieeexplore.ieee.org/document/9230644

 
Md Musfique Anwar. Query-oriented Temporal Active Intimate Community Search. Accepted in 31st Australasian Database Conference (ADC 2020), pp. 206–215, 4-7 February, 2020, Melbourne, Australia. Lecture Notes in Computer Science 10837, Springer. DOI: https://link.springer.com/chapter/10.1007/978-3-030-39469-1_17

 
Tanjim Taharat Aurpa, Fatema Khan and Md. Musfique Anwar. Topical Cluster Detection and Tracking from Mining Social User Interest (short paper). Accepted to the International Conference on Innovation in Engineering and Technology (ICIET), 23-24 December, 2019, Dhaka, Bangladesh.

 
Tasnim Siraj, Md. Enamul Haque and Md Musfique Anwar. Analyzing User Interest in Online Social Network (short paper). Accepted to the International Conference on Innovation in Engineering and Technology (ICIET), 23-24 December, 2019, Dhaka, Bangladesh.

 
Shifat Jahan Shetu, Tahmina Islam and Md Musfique Anwar. TTRank: A Temporal Twitter Ranking of Influential Twitter Users (short paper). Accepted to the International Conference on Innovation in Engineering and Technology (ICIET), 23-24 December, 2019, Dhaka, Bangladesh.

 
Tanjim Taharat Aurpa, Fatema Khan and Md. Musfique Anwar. Discovering and Tracking Query Oriented Topical Clusters in Online Social Networks (Poster paper). 6th International Conference on Networking, Systems and Security (6th NSysS 2019), 17-19 December, 2019, Dhaka, Bangladesh.

 
Shifat Jahan Shetu, Tahmina Islam and Md Musfique Anwar. TTRank: A Temporal Toipcal Model to Rank Twitter Users (Poster paper). 6th International Conference on Networking, Systems and Security (6th NSysS 2019), 17-19 December, 2019, Dhaka, Bangladesh.

 
Aditi Dhali, Sarmistha Sarna, Sudeepto Mohanta and Md Musfique Anwar. Finding Query-oriented Influential Social Users. (Poster paper) 6th International Conference on Networking, Systems and Security (6th NSysS 2019), 17-19 December, 2019, Dhaka, Bangladesh.

 
Tasnim Siraj, Md. Enamul Haque and Md Musfique Anwar. Inferring and Tracking Users Interests in Online Social Networks (Poster paper). 6th International Conference on Networking, Systems and Security (6th NSysS 2019), 17-19 December, 2019, Dhaka, Bangladesh.

 
Swarna Das and Md Musfique Anwar. Finding Topic-Aware Intimate Online Social Groups. Proceedings of the 5th International Conference on Computer, Communication, Chemical, Materials & Electronic Engineering (IC4ME2), 11-12 July, 2019, Rajshahi, Bangladesh. DOI: https://ieeexplore.ieee.org/document/9036676

 
Md. Shoaib Ahmed, Badhan Chandra Das and Md Musfique Anwar. Attribute-Driven Active Local Community Detection (short paper). Accepted to the International Conference on Innovation in Engineering and Technology (ICIET), 27-28 December, 2018, Dhaka, Bangladesh.

 
Badhan Chandra Das, Md. Shoaib Ahmed and Md Musfique Anwar. Attribute-Driven Active Community Search (Poster paper). 5th International Conference on Networking, Systems and Security (5th NSysS 2018) , 18-20 December, 2018, Dhaka, Bangladesh.

 
Badhan Chandra Das, Md. Shoaib Ahmed and Md Musfique Anwar. Query Oriented Active Community Search. International Joint Conference on Computational Intelligence (IJCCI 2018), 14-15 December, 2018, Dhaka, Bangladesh. DOI: https://link.springer.com/chapter/10.1007/978-981-13-7564-4_42

 
Md Musfique Anwar, Chengfei Liu and Jianxin Li. Uncovering Attribute-Driven Active Intimate Community. Proceedings of the 29th Australasian Database Conference (ADC 2018), pp. 109–122, 23-25 May, 2018, Gold Coast, Australia. Lecture Notes in Computer Science 10837, Springer (Best Student Paper Award). DOI: https://link.springer.com/chapter/10.1007/978-3-319-92013-9_9

 
Md Musfique Anwar, Chengfei Liu, Jianxin Li and Tarique Anwar. Discovering and Tracking Active Online Social Groups. Proceedings of the 18th International Conference on Web Information System Engineering (WISE 2017), pp. 59–74, October 7-11, 2017, Puschino, Russia. DOI: https://link.springer.com/chapter/10.1007/978-3-319-68783-4_5

 
Md Musfique Anwar, Jianxin Li and Chengfei Liu. Predicting the Spread of a New Tweet in Twitter. Proceedings of the 26th Australasian Database Conference (ADC 2015), pp. 104–116, 4-7 June, 2015, Melbourne, Australia. Lecture Notes in Computer Science 9093, Springer (Best Poster Award). DOI: https://link.springer.com/chapter/10.1007/978-3-319-19548-3_9

 
Md Musfique Anwar, Jianxin Li and Chengfei Liu. Predicting the Spread of a New Tweet in Twitter. Proceedings of the 26th Australasian Database Conference (ADC 2015), 4-7 June, 2015, Melbourne, Australia. (Best Poster Award).

 
Md. Musfique Anwar, Nasrin Sultana and Md. Al-Amin Bhuiyan. English Translation of Bangla Simple Sentences Using Bilingual Corpus. Proceedings of ICCIA 2011, Second International Conference On Computational Intelligence Applications, February 2011, India, pp. 50–53.

 
Md. Musfique Anwar, Mohammad Zabed Anwar and Md. Al-Amin Bhuiyan. Structural Analysis of Bangla Sentences for Machine Translation10 Proceedings of ICCIA 2010, International Conference On Computationalligence Applications, 03-05 March 2010, India, pp. 230–237.

 
Tahmina Khatoon and Md. Musfique Anwar. Web-based Parcel Managemen.System using Mobile Station. Proceedings of NCCIS 2009, 3rd National Conference on Communication and Information Security, Dhaka, Bangladesh, 4th February 2009, pp. 43–47.

"""

# Regular expression to extract authors and titles
pattern = r"(.+?),\s*\"(.+?)\""

matches = re.findall(pattern, text)

# Save to CSV
with open('authors_titles_ju_11.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Authors', 'Title'])  # Header row
    for match in matches:
        writer.writerow(match)

print("Data saved to research_authors_titles.csv")
