import csv  
import re  

# Provided text  
text = """  
Md Farhan Ishmam
Md Fahim, Fariha Tanjim Shifat, Fabiha Haider, Deeparghya Dutta Barua, MD Sakib Ul Rahman Sourove, Md Farhan Ishmam, and Md Farhad Alam Bhuiyan. 2024. BanglaTLit: A Benchmark Dataset for Back-Transliteration of Romanized Bangla. In Findings of the Association for Computational Linguistics: EMNLP 2024, pages 14656–14672, Miami, Florida, USA. Association for Computational Linguistics.
Tanjila Alam Sathi
Tanjila Alam Sathi, Rafsan Jany, Razia Zaman Ela, AKM Azad, Salem Ali Alyami, Md Azam Hossain, Iqram Hussain,“An interpretable electrocardiogram-based model for predicting arrhythmia and ischemia in cardiovascular disease”, Results in Engineering, Volume 24, 2024,103381,ISSN 2590-1230.https://doi.org/10.1016/j.rineng.2024.103381.(Q1)
Md Farhan Ishmam
Barua, D.D., Sourove, M.S.U.R., Ishmam, M.F., Haider, F., Shifat, F.T., Fahim, M. and Alam, M.F., 2024. ChitroJera: A Regionally Relevant Visual Question Answering Dataset for Bangla. arXiv preprint arXiv:2410.14991. (https://arxiv.org/2410.14991)
Md Farhan Ishmam
Haider, F., Shifat, F.T., Ishmam, M.F., Barua, D.D., Sourove, M.S.U.R., Fahim, M., & Alam, M.F., 2024. BANTH: A Multi-label Hate Speech Detection Dataset for Transliterated Bangla. arXiv. https://arxiv.org/abs/2410.13281.
Md Farhan Ishmam
Al Imran, A. and Ishmam, M.F., FourierKAN outperforms MLP on Text Classification Head Fine-tuning. In NeurIPS 2024 Workshop on Fine-Tuning in Modern Machine Learning: Principles and Scalability (Accepted).
Dr. Hasan Mahmud
Mohsinul Kabir, Faria Binte Kader, Nafisa Hossain Nujat, Tasmia Binte Sogir, Fatin Abrar Shams, Hasan Mahmud & Kamrul Hasan, "Unveiling Depression on Social Media: Active Learning with Human-in-the-Loop Labeling for Mental Health Data Annotation and Analysis", In: Rapp, A., Di Caro, L., Meziane, F., Sugumaran, V. (eds) Natural Language Processing and Information Systems. NLDB 2024. Lecture Notes in Computer Science, vol 14762. Springer, Cham. https://doi.org/10.1007/978-3-031-70239-6_6
Md Farhan Ishmam
Saadat, A., Asad, N.I., & Ishmam, M.F., 2024. Contextual Breach: Assessing the Robustness of Transformer-based QA Models. arXiv PrePrint. https://arxiv.org/abs/2409.10997
Md Farhan Ishmam
Shifat, F.T., Haider, F., Sourove, M.S.U.R., Barua, D.D., Ishmam, M.F., Fahim, M. and Bhuiyan, F.A., 2024. Penta-nlp at EXIST 2024 Task 1–3: Sexism Identification, Source Intention, Sexism Categorization In Tweets. Working Notes of CLEF. (https://ceur-ws.org/Vol-3740/paper-114.pdf)
Md Farhan Ishmam
Barua, D.D., Sourove, M.S.U.R., Haider, F., Shifat, F.T., Ishmam, M.F., Fahim, M. and Bhuiyan, F.A., 2024. Penta ML at EXIST 2024: Tagging Sexism in Online Multimodal Content With Attention-enhanced Modal Context. Working Notes of CLEF. (https://ceur-ws.org/Vol-3740/paper-90.pdf)
Md Farhan Ishmam
Alam, S., Ishmam, M.F., Alvee, N.H., Siddique, M.S., Hossain, M.A. & Kamal, A.R.M., 2024. BnSentMix: A Diverse Bengali-English Code-Mixed Dataset for Sentiment Analysis. arXiv PrePrint. https://arxiv.org/abs/2408.08964
Dr. Md. Hasanul Kabir
S. Ivan, T. Ahmed, S. Ahmed and M. H. Kabir, "A Vision-Language Multimodal Framework for Detecting Hate Speech in Memes," in IEEE Canadian Conference on Electrical and Computer Engineering (CCECE), August 2024. [Accepted]
Dr. Kamrul Hasan
BdSLW60: A Word-Level Bangla Sign Language Dataset. https://arxiv.org/abs/2402.08635 (Under Review in Multimedia Tools and Applications).
Dr. Kamrul Hasan
Unveiling Depression on Social Media: Active Learning with Human-in-the-Loop Labeling for Mental Health Data Annotation and Analysis. NLDB 2024, June 25-26-27, 2024, in Turin, Italy (Accepeted)
Dr. Rafsanjany Kushol
Kushol, Rafsanjany, Sanjay Kalra, and Yee-Hong Yang. "DeepDSMRI: Deep Domain Shift Analyzer for MRI." In Annual Conference on Medical Image Understanding and Analysis, pp. 81-95. Cham: Springer Nature Switzerland, 2024.
Md Farhan Ishmam
Ishmam, M.F., Tashdeed, I., Saadat, T.A., Ashmafee, M.H., Kamal, D.A.R.M. and Hossain, D.M.A., 2024. Visual Robustness Benchmark for Visual Question Answering (VQA). (https://arxiv.org/abs/2407.03386)
Faisal Hussain
F Hussain , MA Khan, M Moniruzzaman, MM Alam, MS. Hossen Efficient Power Control and Resource Allocation for LTE-D2D Communication: A Multi-Objective Optimization Approach. IEEE Access.
Dr. Md. Hasanul Kabir
Z. Sultana, M. N. Islam and M. H. Kabir, "A Hybrid Deep Learning Framework for Estimating Human 3D Pose from 2D Joint Positions," in International Conference on Advances in Computing, Communication, Electrical, and Smart Systems (iCACCESS), March 2024, pp. 1–6.
Dr. Hasan Mahmud
Husne Ara Rubaiyeat, Hasan Mahmud, Ahsan Habib, Md. Kamrul Hasan, "BdSLW60: A Word-Level Bangla Sign Language Dataset", Multimedia Tools and Applications, Springer, February 2024. [Web of Science/SCIE/Scopus, IF: 3.6] [Q1: Media Technology, Computer Science] [Submitted]
Md Farhan Ishmam
Md. Farhan Ishmam, Md. Sakib Hossain Shovon, M.F. Mridha, Nilanjan Dey, From image to language: A critical analysis of Visual Question Answering (VQA) approaches, challenges, and opportunities, Information Fusion, 2024, 102270, ISSN 1566-2535, https://doi.org/10.1016/j.inffus.2024.102270. (https://www.sciencedirect.com/science/article/pii/S1566253524000484)
Ishmam Tashdeed
R. S. M. Wahidur, I. Tashdeed, M. Kaur and H. -N. Lee, "Enhancing Zero-Shot Crypto Sentiment With Fine-Tuned Language Model and Prompt Engineering," in IEEE Access, vol. 12, pp. 10146-10159, 2024, doi: 10.1109/ACCESS.2024.3350638.
2023 (72)
Dr. Hasan Mahmud
Md. Tariquzzaman, Md Wasif Kader, Audwit Anam, Naimul Haque, Mohsinul Kabir, Hasan Mahmud, and Md Kamrul Hasan. 2023. the_linguists at BLP-2023 Task 1: A Novel Informal Bangla Fasttext Embedding for Violence Inciting Text Detection. In Proceedings of the First Workshop on Bangla Language Processing (BLP-2023), EMNLP 2023, pages 214–219, Singapore. Association for Computational Linguistics, https://doi.org/10.18653/v1/2023.banglalp-1.26 [Best Paper award]
Mueeze Al Mushabbir
Dialog Generation with Conversational Agent in Task-Oriented Context using a Transformer Architecture (ICCIT) [DOI: 10.1109/ICCIT60459.2023.10441070]
Dr. Hasan Mahmud
Faysal Petouo, Yaya Arafat, Mueeze Mushabbir, Dr. Kamrul Hasan and Hasan Mahmud, " Dialog Generation with Conversational Agent in Task-Oriented Context using a Transformer Architecture", 26th International Conference on Computer and Information Technology (ICCIT), 13-15 December, 2023, Cox's Bazar, Bangladesh. https://doi.org/10.1109/ICCIT60459.2023.10441070
Dr. Md. Azam Hossain
M. S. Islam, I. Hussain, M. M. Rahman, S. J. Park, and M. A. Hossain, “Explainable artificial intelligence model for stroke prediction using eeg signal”, Sensors, vol. 22, no. 24, 2022, issn: 1424-8220, (SCIE)
Dr. Md. Hasanul Kabir
S. Aziz, N. H. Arif, S. Ahbab, S. Ahmed, T. Ahmed and M. H. Kabir, "Improved Speech Emotion Recognition in Bengali Language using Deep Learning," in 26th International Conference on Computer and Information Technology (ICCIT), December 2023, pp. 1–6.
Dr. Md. Hasanul Kabir
M. H. Rafi, M. Ratul Mahjabin, M. S. Rahman, M. H. Kabir and S. Ahmed, "A Critical Analysis of Deep Learning Applications in Crop Pest Classification: Promising Pathways and Limitations," in 26th International Conference on Computer and Information Technology (ICCIT), December 2023, pp. 1-6.
Sabbir Ahmed
Alvi Khan, Fida Kamal, Nuzhat Nower, Tasnim Ahmed, Sabbir Ahmed, and Tareque Chowdhury. "NERvous About My Health: Constructing a Bengali Medical Named Entity Recognition Dataset." EMNLP Findings (2023), ACL, Singapore
Sabbir Ahmed
Ridwan Mahbub, Ifrad Khan, Samiha Anuva, Md Shihab Shahriar, Md Tahmid Rahman Laskar, and Sabbir Ahmed. "Unveiling the Essence of Poetry: Introducing a Comprehensive Dataset and Benchmark for Poem Summarization." EMNLP Main (2023), ACL, Singapore
Sabbir Ahmed
Alvi Khan, Fida Kamal, Mohammad Abrar Chowdhury, Tasnim Ahmed, Md Tahmid Rahman Laskar, and Sabbir Ahmed. "BanglaCHQ-Summ: An Abstractive Summarization Dataset for Medical Queries in Bangla Conversational Speech." EMNLP BLP workshop (2023), ACL, Singapore
Dr. Hasan Mahmud
Ramisha Baki, Afnan Mumu, Riyadil Zannat, Mouneeta Rahman, Hasan Mahmud, and Muhammad Nazrul Islam, Usability Analysis of Augmented Reality-Based Learning Applications for Kids: Insights from SUS and Heuristic Evaluation. In: Martins, N., Brandão, D. (eds) Advances in Design and Digital Communication IV. DIGICOM 2023. Springer Series in Design and Innovation , vol 35. Springer, Cham. https://doi.org/10.1007/978-3-031-47281-7_10
Dr. Kamrul Hasan
Faysal Petouo, Yaya Arafat, Mueeze Mushabbir, Dr. Kamrul Hasan and Hasan Mahmud, " Dialog Generation with Conversational Agent in Task-Oriented Context using a Transformer Architecture", 26th International Conference on Computer and Information Technology (ICCIT), 13-15 December 2023, Cox’s Bazar, Bangladesh.
Dr. Md. Hasanul Kabir
T. Tajwar, M. Rahman, T. A. Chowdhury, S. Ahmed, M. Farazi and M. H. Kabir, "Improving Zero-Shot Semantic Segmentation using Dynamic Kernels," in International Conference on Digital Image Computing: Techniques and Applications (DICTA), December 2023, pp. 395--402.
Sabbir Ahmed
Tauseef Tajwar, Muftiqur Rahman, Taukir Azam Chowdhury, Sabbir Ahmed, Moshiur Farazi, and Md Hasanul Kabir. "Improving Zero-Shot Semantic Segmentation using Dynamic Kernels." In DICTA (2023), IEEE, Australia.
Dr. Rafsanjany Kushol
Kuan, Li-Hao, Pedram Parnianpour, Rafsanjany Kushol, Neeraj Kumar, Tanushka Anand, Sanjay Kalra, and Russell Greiner. "Accurate personalized survival prediction for amyotrophic lateral sclerosis patients." Scientific Reports 13, no. 1 (2023): 20713.
Dr. Hasan Mahmud
S M Rayeed, Sidratul Tamzida Tuba, Hasan Mahmud, Mumtahin Habib Ullah Mazumder, Saddam Hossain Mukta, Kamrul Hasan, "BdSL47: A complete depth-based Bangla sign alphabet and digit dataset", Data in Brief, Volume 51, 2023, 109799, ISSN 2352-3409, https://doi.org/10.1016/j.dib.2023.109799. (https://www.sciencedirect.com/science/article/pii/S2352340923008612) [Web of Science/ESCI/Scopus, IF: 1.2] [Q2: Multidisciplinary, Computer Science]
Md. Jubair Ibna Mostafa
Maliha Noushin Raida, Zannatun Naim Sristy, Nawshin Ulfat, Sheikh Moonwara Anjum Monisha, Md. Jubair Ibna Mostafa, and Md. Nazmul Haque. “A study on classifying stack overflow questions based on difficulty by utilizing contextual features” in Journal of Systems and Software, Volume: 208:111884, 2024. Elsevier
Dr. Kamrul Hasan
A Novel Informal Bangla Fasttext Model for Violence Inciting Text Detection. EMNLP 2023 Workshop BLP. (Best Paper)
Dr. Hasan Mahmud
Mohammad Ridwan Kabir, Hasan Mahmud, Md. Kamrul Hasan, "Acceptability of a head-mounted assistive mouse controller for people with upper limb disability: An empirical study using the technology acceptance model". PLoS ONE 18(10): e0293608. https://doi.org/10.1371/journal.pone.0293608, 31 October 2023 [Web of Science/SCIE/Scopus, IF: 3.752] [Q1: Multidisciplinary, Computer Science]
Ridwan Kabir
M. R. Kabir, H. Mahmud, and M. K. Hasan, "Acceptability of a head-mounted assistive mouse controller for people with upper limb disability: An empirical study using the technology acceptance model," in PLOS ONE, vol. 18(10), e0293608, 2023, doi: 10.1371/journal.pone.0293608.
Dr. Kamrul Hasan
Mohammad Ridwan Kabir, Hasan Mahmud, Md Kamrul Hasan. Acceptability of a head-mounted assistive mouse controller for people with upper limb disability: an empirical study using the technology acceptance model. PLoS One. 2023; 18(10).
Ali Abir Shuvro
A. A. Arnab, K. Ma, A. A. Shuvro and H. Leung, "Comparison of 4G LTE and 5G NR in UAV Networks: A Simu5G-Based Performance Evaluation," 2023 IEEE 9th World Forum on Internet of Things (WF-IoT), Aveiro, Portugal, 2023, pp. 1-6, doi: 10.1109/WF-IoT58464.2023.10539559.
Ali Abir Shuvro
A. A. Arnab, A. A. Shuvro, K. Ma and H. Leung, "A Deep Learning Approach for a QoS Prediction System in Cellular Networks," 2023 IEEE 9th World Forum on Internet of Things (WF-IoT), Aveiro, Portugal, 2023, pp. 1-6, doi: 10.1109/WF-IoT58464.2023.10539507.
Dr. Rafsanjany Kushol
Kushol, Rafsanjany, Richard Frayne, Simon J. Graham, Alan H. Wilman, Sanjay Kalra, and Yee-Hong Yang. "Domain adaptation of MRI scanners as an alternative to MRI harmonization." In MICCAI Workshop on Domain Adaptation and Representation Transfer, pp. 1-11. Cham: Springer Nature Switzerland, 2023.
Dr. Rafsanjany Kushol
Kushol, Rafsanjany, Pedram Parnianpour, Alan H. Wilman, Sanjay Kalra, and Yee-Hong Yang. "Effects of MRI scanner manufacturers in classification tasks with deep learning models." Scientific Reports 13, no. 1 (2023): 16791.
Dr. Rafsanjany Kushol
Huo, Dong, Abbas Masoumzadeh, Rafsanjany Kushol, and Yee-Hong Yang. "Blind Image Deconvolution Using Variational Deep Image Prior." IEEE Transactions on Pattern Analysis and Machine Intelligence (2023).
Sabbir Ahmed
Asaduzzaman Herok, and Sabbir Ahmed. "Cotton Leaf Disease Identification Using Transfer Learning." 2nd ICICT4SD (2023), IEEE, Dhaka, Bangladesh
Sabbir Ahmed
Rafid Haque, ABM Ashikur Rahman, and Sabbir Ahmed. "Data-Driven Analysis and Forecasting of COVID-19 Third Wave in SAARC Countries." 2nd ICICT4SD (2023), IEEE, Dhaka, Bangladesh
Dr. Rafsanjany Kushol
Kushol, Rafsanjany, Alan H. Wilman, Sanjay Kalra, and Yee-Hong Yang. "DSMRI: Domain Shift Analyzer for Multi-Center MRI Datasets." Diagnostics 13, no. 18 (2023): 2947.
Dr. Rafsanjany Kushol
Kushol, Rafsanjany, Collin C. Luk, Avyarthana Dey, Michael Benatar, Hannah Briemberg, Annie Dionne, Nicolas Dupré et al. "SF2Former: Amyotrophic lateral sclerosis identification from multi-center MRI data using spatial and frequency fusion transformer." Computerized Medical Imaging and Graphics 108 (2023): 102279.
Dr. Hasan Mahmud
Nowshin Tabassum, Tasfia Tabassum, Fardin Saad, Tahiya Sultana Safa, Hasan Mahmud, Md. Kamrul Hasan, "Exploring the English Accent-independent Features for Speech Emotion Recognition using Filter and Wrapper-based Methods for Feature Selection", Interspeech 2023, 20-24 August, Dublin, Ireland.
Dr. Kamrul Hasan
Nowshin Tabassum, Tasfia Tabassum, Fardin Saad, Tahiya Sultana Safa, Hasan Mahmud, Md. Kamrul Hasan. Exploring the English Accent-independent Features for Speech Emotion Recognition using Filter and Wrapper-based Methods for Feature Selection. Interspeech 2023, Dublin, Ireland.
Tanjila Alam Sathi
Afsana Mimi, Md. Golam Rasul, Tanjila Alam Sathi, Lutfun Nahar Lota,"Personal Thermal Assessment using Feature Reduction and Machine Learning Techniques," at 5th International Conference on Activity and Behavior Computing 2023, Kaiserslautern, Germany.
Md. Nazmul Haque
Maliha Noushin Raida, Zannatun Naim Sristy, Nawshin Ulfat, Sheikh Moonwara Anjum Monisha, Md. Jubair Ibna Mostafa, Md. Nazmul Haque, “A Study on Classifying Stack Overflow Questions based on Difficulty by Utilizing Contextual Features”, Journal of Systems and Software (2023)
Sabbir Ahmed
Sabbir Ahmed, "Classification of Plant Disease from Leaf Images Using Few-Shot Learning." PhD diss., Department of Computer Science and Engineering (CSE), Islamic University of Technology (IUT), Board Bazar, Gazipur, Bangladesh, 2022. [MSc Thesis]
Md. Jubair Ibna Mostafa
Zubair Rahman Tusar, Sadat Bin Sharfuddin, Muhtasim Abid, Md. Nazmul Haque, and Md. Jubair Ibna Mostafa. “Effectiveness of data augmentation and ensembling using transformer-based models for sentiment analysis: Software engineering perspective”. in Proceedings of the 18th International Conference on Software Technologies, (ICSOFT), Rome, Italy, July 10-12, pages 438–447 2023. SciTePress
Syed Rifat Raiyan
Mohsinul Kabir*, Obayed Bin Mahfuz*, Syed Rifat Raiyan*, Hasan Mahmud, and Md Kamrul Hasan. 2023. BanglaBook: A Large-scale Bangla Dataset for Sentiment Analysis from Book Reviews. In Findings of the Association for Computational Linguistics: ACL 2023, pages 1237–1247, Toronto, Canada. Association for Computational Linguistics. DOI: 10.18653/v1/2023.findings-acl.80
Syed Rifat Raiyan
Syed Rifat Raiyan, Md Nafis Faiyaz, Shah Md. Jawad Kabir, Mohsinul Kabir, Hasan Mahmud, and Md Kamrul Hasan. 2023. Math Word Problem Solving by Generating Linguistic Variants of Problem Statements. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 4: Student Research Workshop), pages 362–378, Toronto, Canada. Association for Computational Linguistics. DOI: 10.18653/v1/2023.acl-srw.49
Dr. Hasan Mahmud
Mohsinul Kabir, Obayed Bin Mahfuz, Syed Rifat Raiyan, Hasan Mahmud, and Md Kamrul Hasan. 2023. BanglaBook: A Large-scale Bangla Dataset for Sentiment Analysis from Book Reviews. In Findings of the Association for Computational Linguistics: ACL 2023, pages 1237–1247, Toronto, Canada. Association for Computational Linguistics.
Dr. Hasan Mahmud
Syed Rifat Raiyan, Md Nafis Faiyaz, Shah Md. Jawad Kabir, Mohsinul Kabir, Hasan Mahmud, and Md Kamrul Hasan. 2023. Math Word Problem Solving by Generating Linguistic Variants of Problem Statements. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 4: Student Research Workshop), pages 362–378, Toronto, Canada. Association for Computational Linguistics.
Dr. Hasan Mahmud
Faria Binte Kader, Nafisa Hossain Nujat, Tasmia Binte Sogir, Mohsinul Kabir, Hasan Mahmud, and Md Kamrul Hasan. 2023. “When Words Fail, Emojis Prevail”: A Novel Architecture for Generating Sarcastic Sentences With Emoji Using Valence Reversal and Semantic Incongruity. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 4: Student Research Workshop), pages 334–351, Toronto, Canada. Association for Computational Linguistics.
Md. Jubair Ibna Mostafa
Abdullah Al Jobair, Suzad Mohammad, Zahin Raidah Maisha, Md. Jubair Ibna Mostafa, and Md. Nazmul Haque. “The ugly side of stack overflow: An in-depth exploration of the social dynamics of new users’ engagement and community perception of them” in Communications in Computer and Information Science book series (CCIS, volume 1829), pages 243–265, Cham, 2023. Springer
Dr. Kamrul Hasan
Faria Binte Kader, Nafisa Hossain Nujat, Tasmia Binte Sogir, Mohsinul Kabir, Hasan Mahmud, Md Kamrul Hasan . “When Words Fail, Emojis Prevail”: A Novel Architecture for Generating Sarcastic Sentences With Emoji Using Valence Reversal and Semantic Incongruity. Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 4: Student Research Workshop) Pages 334-351.
Sabbir Ahmed
Md Bakhtiar Hasan, Tasnim Ahmed, Sabbir Ahmed, and Md Hasanul Kabir. "GaitGCN++: Improving GCN-based gait recognition with part-wise attention and DropGraph." Journal of King Saud University-Computer and Information Sciences 35, no. 7 (2023): 101641.
Dr. Md. Azam Hossain
M. M. Rahman, M. S. Islam, M. T. R. Laskar, M. A. Hossain, and A. R. M. Kamal, “Multihop Factual Claim Verification Using Natural Language Prompts”, https://caiac.pubpub.org/pub/ex7vouwq, Canadian Artificial Intelligence Association (CAIAC), Jun. 2023.
Dr. Md. Hasanul Kabir
M.B. Hasan, T. Ahmed, S. Ahmed, and M. H. Kabir, "GaitGCN++: Improving GCN-based gait recognition with part-wise attention and DropGraph," Journal of King Saud University - Computer and Information Sciences, vol. 35, No. 7, pp, 1-19, July 2023. [SCIE]
Dr. Kamrul Hasan
Syed Rifat Raiyan, Md Nafis Faiyaz, Shah Md. Jawad Kabir, Mohsinul Kabir, Hasan Mahmud, Md Kamrul Hasan. Math Word Problem Solving by Generating Linguistic Variants of Problem Statements. Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 4: Student Research Workshop), Pages 362–378
Dr. Md. Hasanul Kabir
A.M. Khan, A.Ashrafee, F.S. Khan, M.B. Hasan and M.H.Kabir, "AttResDU-Net: Medical Image Segmentation Using Attention-Based Residual Double U-Net," in International Joint Conference on Neural Networks (IJCNN), June 2023, pp 1-8.
Dr. Kamrul Hasan
Mohsinul Kabir, Obayed Bin Mahfuz, Syed Rifat Raiyan, Hasan Mahmud, and Md Kamrul Hasan. 2023. BanglaBook: A Large-scale Bangla Dataset for Sentiment Analysis from Book Reviews. In Findings of the Association for Computational Linguistics: ACL 2023, pages 1237–1247, Toronto, Canada. Association for Computational Linguistics.
Dr. Md. Azam Hossain
M. Batin, M. Islam, M. M. Hasan, A. Azad, S. A. Alyami, M. A. Hossain, and S. J. Miklavcic, “Wheat- spikenet: An improved wheat spike segmentation model for accurate estimation from field imaging”, Frontiers in Plant Science, vol. 14, 1226190 (SCIE, Q1)
Dr. Md. Azam Hossain
I. Hussain, R. Jany, R. Boyer, A. Azad, S. A. Alyami, S. J. Park, M. M. Hasan, and M. A. Hossain, “An explainable eeg-based human activity recognition model using machine-learning approach and lime”, Sensors, vol. 23, no. 17, 2023, issn: 1424-8220, (SCIE)
Syed Rifat Raiyan
Syed Rifat Raiyan, Md Nafis Faiyaz, Shah Md. Jawad Kabir. 2023. Variational Mathematical Reasoning: Enhancing Math Word Problem Solvers with Linguistic Variants and Disentangled Attention. Department of Computer Science and Engineering (CSE), Islamic University of Technology, Board Bazar, Gazipur-1704, Dhaka, Bangladesh. URI: 103.82.172.44:8080/xmlui/handle/123456789/2092
Faisal Hussain
A. A. Shuvro, M. S. Khan, M. Rahman, F. Hussain, M. Moniruzzaman and M. S. Hossen, "Transformer Based Traffic Flow Forecasting in SDN-VANET," in IEEE Access, vol. 11, pp. 41816-41826, 2023, doi: 10.1109/ACCESS.2023.3270889.
Ali Abir Shuvro
A. A. Shuvro, M. S. Khan, M. Rahman, F. Hussain, M. Moniruzzaman and M. S. Hossen, "Transformer Based Traffic Flow Forecasting in SDN-VANET," in IEEE Access, vol. 11, pp. 41816-41826, 2023, doi: 10.1109/ACCESS.2023.3270889.
Tanjila Alam Sathi
Hasnain Karim Rabib, Mostafa Galib, Takia Mosharref Nobo, Tanjila Alam Sathi,Mohammed Saidul Islam, Abu Raihan Mostofa Kamal,Md Azam Hossain,"Gender-based Cyberbullying Detection for Under-resourced Bangla Language," 2022, at 12th International Conference on Electrical and Computer Engineering (ICECE), Dhaka, Bangladesh, 2022, pp. 104-107.
Dr. Md. Azam Hossain
M. M. Hasan, M. A. Hossain, N. Alotaibi, F. A. John, and A. AKM, “Binocular rivalry impact on macroblock-loss error concealment for stereoscopic 3d video transmission”, Sensors, 2023, issn: 1424-8220, (SCIE).
Sabbir Ahmed
Tasnim Ahmed, Ahnaf Munir, Sabbir Ahmed, Md. Bakhtiar Hasan, Md. Taslim Reza, Md. Hasanul Kabir, "StructureEnhanced Translation from PET to CT Modality with Paired GANs", 6𝑡ℎ ICMVA (2023), Singapore.
Dr. Md. Hasanul Kabir
S. Ahmed, M.B. Hasan, T. Ahmed, M.R.K. Sony and M. H. Kabir, "Less is More: Lighter and Faster Deep Neural Architecture for Tomato Leaf Disease Classification," IEEE Access, vol. 10, pp. 68868-68884, 2022. [SCIE]
Dr. Md. Hasanul Kabir
A.B.M. Rahman, M.B. Hasan, S. Ahmed, T. Ahmed, M.H. Ashmafee, M.R. Kabir and M. H. Kabir, "Two Decades of Bengali Handwritten Digit Recognition: A Survey," IEEE Access, vol. 10, pp. 92597-92632, 2022. [SCIE]
Dr. Md. Hasanul Kabir
T. Ahmed, A. Munir, S. Ahmed, M.B. Hasan, M.T. Reza and M.H. Kabir, "Structure-Enhanced Translation from PET to CT Modality with Paired GANs," in International Conference on Machine Vision and Applications (ICMVA), March 2023, pp. 142–146. [Best Presentation Award]
Dr. Md. Hasanul Kabir
T.A. Belal, G.M. Shahariar and M.H. Kabir, "Interpretable Multi Labeled Bengali Toxic Comments Classification using Deep Learning," in International Conference on Electrical, Computer and Communication Engineering (ECCE), February 2023, pp. 1–6. [Best Paper Award]
Dr. Md. Hasanul Kabir
S. Ishrak, M.B. Munir and M.H. Kabir, "Dynamic Hand Gesture Recognition using Sequence of Human Joint Relative Angles," in International Conference on Electrical, Computer and Communication Engineering (ECCE), February 2023, pp. 1–6. [Best Paper Award]
Dr. Md. Hasanul Kabir
C. Sinthia and M.H. Kabir, "Detection and Recognition of Bangladeshi Vehicles’ Nameplates Using YOLOV6 and BLPNET," in International Conference on Electrical, Computer and Communication Engineering (ECCE), February 2023, pp. 1–6.
Dr. Md. Azam Hossain
M. Kamal, C. M. Abdullah, F. Shaiara, A. R. M. Kamal, M. M. Hasan, J.-S. Kim, and M. A. Hossain, “Blockchain-based pension system ensuring security, provenance and efficiency”, IEICE TRANSACTIONS on Information and Systems, vol. E106-D, no. 5, 2023, issn: 1745-1361, (SCIE).
Dr. Hasan Mahmud
Mohsinul Kabir, Tasnim Ahmed, Md. Bakhtiar Hasan, Md Tahmid Rahman Laskar, Tarun Kumar Joarder, Hasan Mahmud, Kamrul Hasan, DEPTWEET: A typology for social media texts to detect depression severities, Computers in Human Behavior, Volume 139, 2023, 107503, ISSN 0747-5632, https://doi.org/10.1016/j.chb.2022.107503. (https://www.sciencedirect.com/science/article/pii/S0747563222003235) [Web of Science/SSCI/Scopus, IF: 9.9] [Q1: Human-Computer Interaction in Computer Science, Psychology, Arts and Humanities]
Dr. Kamrul Hasan
Hasan Mahmud, Mashrur M. Morshed and Md. Kamrul Hasan .Quantized depth image and skeleton-based multimodal dynamic hand gesture recognition.Vis Comput (2023). https://doi.org/10.1007/s00371-022-02762-1
Dr. Hasan Mahmud
Hasan Mahmud, Mashrur M. Morshed, Md. Kamrul Hasan, "Quantized depth image and skeleton-based multimodal dynamic hand gesture recognition", The Visual Computer Journal, 4 January 2023, Springer Nature Switzerland, part of Springer Nature, https://doi.org/10.1007/s00371-022-02762-1 [SCIE/Web of Science indexed, IF 3.5] [Q2: Computer Vision and Pattern Recognition]
Md. Nazmul Haque
Abdullah Al Jobair, Suzad Mohammad, Zahin Raidah Maisha, Md. Jubair Ibna Mostafa, and Md. Nazmul Haque,“The Ugly Side of Stack Overflow: An In-depth Exploration of the Social Dynamics of New Users’ Engagement and Community Perception of Them”, International Conference on Evaluation of Novel Approaches to Software Engineering. Cham: Springer Nature Switzerland, 2022.
2022 (70)
Sabbir Ahmed
Refaat Mohammad Alamgir, Ali Abir Shuvro, Mueeze Al Mushabbir, Mohammed Ashfaq Raiyan, Nusrat Jahan Rani, Md Rahman, Md Kabir, and Sabbir Ahmed, "Performance Analysis of YOLO-based Architectures for Vehicle Detection from Traffic Images in Bangladesh", 25𝑡ℎ ICCIT (2022), Cox’s Bazar, Bangladesh
Farzana Tabassum
S. Islam, F. Tabassum, S. Rizwan and T. M. Chowdhury, "Transfer Learning-based Ensemble Approach for Organ Classification: An Empirical Study," 2022 12th International Conference on Electrical and Computer Engineering (ICECE), Dhaka, Bangladesh, 2022, pp. 52-55, doi: 10.1109/ICECE57408.2022.10089089.
Sabbir Ahmed
Md. Hamjajul Ashmafee, Tasnim Ahmed, Sabbir Ahmed, Md. Bakhtiar Hasan, Mst Nura Jahan, A.B.M. Ashikur Rahman, "An Efficient Transfer Learning-based Approach for Apple Leaf Disease Classification", 3𝑟𝑑 ECCE (2023), Chittagong, Bangladesh
Sabbir Ahmed
Ahmed Nusayer Ashik, Md Saimul Haque Shanto, Rizwanul Haque Khan, Md. Hasanul Kabir, and Sabbir Ahmed, "Recognizing Bangladeshi Traffic Signs in the Wild", 25𝑡ℎ ICCIT (2022), Cox’s Bazar, Bangladesh
Sabbir Ahmed
Akib Mohammed Khan, Alif Ashrafee, Reeshoon Sayera, Shahriar Ivan, and Sabbir Ahmed, "Rethinking Cooking State Recognition with Vision Transformers", 25𝑡ℎ ICCIT (2022), Cox’s Bazar, Bangladesh.
Dr. Md. Azam Hossain
C. M. Abdullah, M. Kamal, F. Shaiara, A. R. M. Kamal, and M. A. Hossain, "Bloodcomm: A peerto-peer blockchain-based community for blood donation network", in 25th International Conference on Computer and Information Technology (ICCIT), IEEE, Cox's Bazar, Bangladesh, Dec. 2022
Dr. Md. Azam Hossain
R. Jany, M. H. Ashmafee, I. Hussain, and M. A. Hossain, "Sleepexplain: Explainable non-rapid eye movement and rapid eye movement sleep stage classification from eeg signal", in 25th International Conference on Computer and Information Technology (ICCIT), IEEE, Cox's Bazar, Bangladesh, Dec. 2022
Dr. Md. Azam Hossain
M. M. Rahman, S. Malik, M. S. Islam, M. A. Hossain, and A. R. M. Kamal, "An efficient approach to automatic tag prediction from movie plot synopses using transformer-based language model", in 25th International Conference on Computer and Information Technology (ICCIT), IEEE, Cox's Bazar, Bangladesh, Dec. 2022
Dr. Md. Azam Hossain
M. R. Khan, S. M. N. Rahmatullah, I. M. Fuadul, A. R. M. Kamal, and M. A. Hossain, "Sentiment analysis of covid-19 vaccination in bangla language with code-mixed text from social media", in 12th International Conference on Electrical and Computer Engineering (ICECE), IEEE, Dhaka (BUET), Bangladesh, Dec. 2022
Dr. Md. Azam Hossain
H. K. Rabib, M. Galib, T. M. Nobo, T. A. Sathi, M. S. Islam, A. R. M. Kamal, and M. A. Hossain, "A gender-based cyberbullying detection for under-resourced bangla language", in 12th International Conference on Electrical and Computer Engineering (ICECE), IEEE, Dhaka (BUET), Bangladesh, Dec. 2022
Fardin Saad
An Efficient Approach to Automatic Tag Prediction from Movie Plot Synopses using Transformer based Language Model - To appear at the 25th International Conference on Computer and Information Technology (ICCIT)
Ali Abir Shuvro
R. M. Alamgir et al., "Performance Analysis of YOLO-based Architectures for Vehicle Detection from Traffic Images in Bangladesh," 2022 25th International Conference on Computer and Information Technology (ICCIT), Cox's Bazar, Bangladesh, 2022, pp. 982-987, doi: 10.1109/ICCIT57492.2022.10055758.
Sabbir Ahmed
Md. Samin Morshed, Sabbir Ahmed, Tasnim Ahmed, Muhammad Usama Islam, and A. B. M. Rahman, "Fruit quality assessment with densely connected convolutional neural network", 12𝑡ℎ ICECE (2022), Dhaka, Bangladesh,
Sabbir Ahmed
Minhaz Kamal, Fairuz Shaiara, Chowdhury Mohammad Abdullah, Sabbir Ahmed, Tasnim Ahmed, and Md. Hasanul Kabir, "Huruf: An Application for Arabic Handwritten Character Recognition Using Deep Learning", 25𝑡ℎ ICCIT (2022), Cox’s Bazar, Bangladesh.
Mueeze Al Mushabbir
Performance Analysis of YOLO-based Architectures for Vehicle Detection from Traffic Images in Bangladesh (ICCIT) [DOI: 10.1109/ICCIT57492.2022.10055758]
Dr. Md. Hasanul Kabir
R.M. Alamgir, A.A. Shuvro, M. Al Mushabbir, M.A. Raiyan, N.J. Rani, M.M. Rahman, M.H. Kabir and S. Ahmed, "Performance Analysis of YOLO-based Architectures for Vehicle Detection from Traffic Images in Bangladesh," in International Conference on Computer and Information Technology (ICCIT), December 2022, pp. 982–987.
Dr. Md. Hasanul Kabir
A. Ashik, M.S Shanto, R. Khan, M.H. Kabir and S. Ahmed, "Recognizing Bangladeshi Traffic Signs in the Wild," in International Conference on Computer and Information Technology (ICCIT), December 2022, pp. 1004–1009.
Dr. Md. Hasanul Kabir
M.A. Toma, N.T. Promi, M.A. Pushpo and M.H. Kabir, "Blood Vessel Segmentation in Retinal Images Using Machine Learning Approach," in International Conference on Computer and Information Technology (ICCIT), December 2022, pp. 200–205.
Dr. Md. Hasanul Kabir
F.T. Lisa, M.Z. Hossain, S.N. Mou, S. Ivan and M.H. Kabir, "Land Cover and Land Use Detection using Semi-Supervised Learning," in International Conference on Computer and Information Technology (ICCIT), December 2022, pp. 164–169.
Dr. Md. Hasanul Kabir
M. Kamal, F. Shaiara, C.M. Abdullah, S. Ahmed, T. Ahmed and M.H. Kabir, "Huruf: An Application for Arabic Handwritten Character Recognition Using Deep Learning," in International Conference on Computer and Information Technology (ICCIT), December 2022pp. 1131–1136.
Md. Mezbaur Rahman
Ekram, S. M. S., Rahman, A. A., Altaf, M. S., Islam, M. S., Rahman, M. M., Rahman, M. M., ... & Kamal, A. R. M. (2022, December). BanglaRQA: A Benchmark Dataset for Under-resourced Bangla Language Reading Comprehension-based Question Answering with Diverse Question-Answer Types. In Findings of the Association for Computational Linguistics: EMNLP 2022 (pp. 2518-2532).
Md. Mezbaur Rahman
Islam, M. S., Hussain, I., Rahman, M. M., Park, S. J., & Hossain, M. A. (2022). Explainable Artificial Intelligence Model for Stroke Prediction Using EEG Signal. Sensors, 22(24), 9859.
Dr. Hasan Mahmud
Ratun Rahman, Md Rafid Islam, Akib Ahmed, Dr. Md. Kamrul Hasan, Dr. Hasan Mahmud, "A Study of Permission-based Malware Detection Using Machine Learning", The 15th IEEE International Conference on Security of Information and Networks, SINCONF 2022, Sousse, Tunisia, 11–13 November, 2022.
Dr. Kamrul Hasan
R. Rahman, M. R. Islam, A. Ahmed, M. K. Hasan and H. Mahmud, "A Study of Permission-based Malware Detection Using Machine Learning," 2022 15th International Conference on Security of Information and Networks (SIN), Sousse, Tunisia, 2022, pp. 01-06, doi: 10.1109/SIN56466.2022.9970528.
Tanjila Alam Sathi
MD.Golam Rasul,Wasim Akram,Sayeda Fatema Tuj Zohura,Tanjila Alam Sathi,Lutfun Nahar Lota ,"Future Prediction for Nurse Care Activities using Deep Learning based Multi-Label Classification," at 4th International Conference on Activity and Behavior Computing,London,2022,in book chapter: Human Activity and Behavior Analysis. DOI: 10.1201/9781003371540-26.
Dr. Md. Azam Hossain
S. M. S. Ekram, A. A. Rahman, M. S. Altaf, M. S. Islam, M. M. Rahman, M. M. Rahman, M. A. Hossain, and A. R. M. Kamal, "BanglaRQA: A benchmark dataset for under-resourced Bangla language reading comprehension-based question answering with diverse question-answer types", in Findings of the Association for Computational Linguistics: EMNLP 2022, Abu Dhabi, United Arab Emirates: Association for Computational Linguistics, Dec. 2022, 25182532, (A* Conference).
Dr. Hasan Mahmud
Mohammad Ridwan Kabir, Mohammad Anas Jawad, Mohaimin Ehsan, Hasan Mahmud, Md. Kamrul Hasan, "Renovo: Prototype of a Low-Cost Sensor-Based Therapeutic System for Upper Limb Rehabilitation", 17 October, 2022, https://doi.org/10.48550/arXiv.2109.03631
Dr. Hasan Mahmud
Mohammad Ridwan Kabir, Mohammad Ishrak Abedin, Rizvi Ahmed, Saad Bin Ashraf, Hasan Mahmud, Md. Kamrul Hasan, "Auxilio: A Sensor-Based Wireless Head-Mounted Mouse for People with Upper Limb Disability", 10 October, 2022, https://doi.org/10.48550/arXiv.2210.04483
Fardin Saad
A Case Study on the Independence of Speech Emotion Recognition in Bangla and English Languages using Language-Independent Prosodic Features (Under Review) Link: https://arxiv.org/abs/2111.10776
Dr. Kamrul Hasan
Mohsinul Kabir, Tasnim Ahmed, Md. Bakhtiar Hasan, Md Tahmid Rahman Laskar, Tarun Kumar Joarder, Hasan Mahmud, Kamrul Hasan. DEPTWEET: A typology for social media texts to detect depression severities. Computers in Human Behavior Volume 139, February 2023, 107503
Ridwan Kabir
I. J. Ratul, U.H. Wani, M. M. Nishat, A. Al-Monsur, A. M. Ar-Rafi, F. Faisal, M. R. Kabir, "Survival Prediction of Children Undergoing Hematopoietic Stem Cell Transplantation Using Different Machine Learning Classifiers by Performing Chi-Square Test and Hyperparameter Optimization: A Retrospective Analysis", Computational and Mathematical Methods in Medicine, vol. 2022, Article ID 9391136, 14 pages, 2022. https://doi.org/10.1155/2022/9391136
Dr. Hasan Mahmud
Nazmus Sakib, G. M. Shahariar, Md. Mohsinul Kabir, Md. Kamrul Hasan, Hasan Mahmud. "Assorted, Archetypal and Annotated Two Million (3A2M) Cooking Recipes Dataset based on Active Learning", International Conference on Machine Intelligence and Emerging Technologies (MIET), Noakhali Science and Technology University (NSTU), Sonapur, Noakhali, Bangladesh, 23-25 September 2022.
Md. Bakhtiar Hasan
M. Kabir, T. Ahmed, M. B. Hasan, M. T. R. Laskar, T. K. Joarder, H. Mahmud and K. Hasan, "DEPTWEET: A typology for social media texts to detect depression severities" in Computers in Human Behavior, vol. 139, pp. 107503, 2022, doi: 10.1016/j.chb.2022.107503
Ridwan Kabir
A. B. M. Ashikur Rahman et al., "Two Decades of Bengali Handwritten Digit Recognition: A Survey," in IEEE Access, 2022, doi: 10.1109/ACCESS.2022.3202893.
Sabbir Ahmed
ABM Ashikur Rahman, Md Bakhtiar Hasan, Sabbir Ahmed, Tasnim Ahmed, Md Hamjajul Ashmafee, Mohammad Ridwan Kabir, and Md Hasanul Kabir. "Two Decades of Bengali Handwritten Digit Recognition: A Survey." IEEE Access 10 (2022): 92597-92632.
Md. Bakhtiar Hasan
A. B. M. A. Rahman, M. B. Hasan, S. Ahmed, T. Ahmed, M. H. Ashmafee, M. R. Kabir and M. H. Kabir, "Two Decades of Bengali Handwritten Digit Recognition: A Survey" in IEEE Access, vol. 10, pp. 92597-92632, 2022, doi: 10.1109/ACCESS.2022.3202893.
Dr. Hasan Mahmud
Tasnim Ahmed, Shahriar Ivan, Mohsinul Kabir, Hasan Mahmud, Md. Kamrul Hasan, "Performance analysis of transformer-based architectures and their ensembles to detect trait-based cyberbullying", Social Network Analysis and Mining (SNAM), 12, 99 (2022). https://doi.org/10.1007/s13278-022-00934-4 [Web of Science/ESCI/Scopus] [IF 2.8] [Q1: Communication in Social Science, Human-Computer Interaction, Information Systems]
Dr. Kamrul Hasan
Nazmus Sakib, G. M. Shahariar, Md. Mohsinul Kabir, Md. Kamrul Hasan, Hasan Mahmud. "Assorted, Archetypal and Annotated Two Million (3A2M) Cooking Recipes Dataset based on Active Learning". MIET 2022, Lecture Notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering book series (LNICST,volume 491)
Dr. Kamrul Hasan
Tasnim Ahmed, Md. Mosinul Kabir, Shahriar Ivan, Hasan Mahmud and Md. Kamrul Hasan. "Performance Analysis of Transformer-based Architectures and Their Ensembles to Detect Trait-based Cyberbullying", Journal of Social Network Analysis and Mining, 2022
Ridwan Kabir
S. A. Sabab, M. R. Kabir, S. R. Hussain, H. Mahmud, H. A. Rubaiyeat and M. K. Hasan, "VIS-iTrack: Visual Intention Through Gaze Tracking Using Low-Cost Webcam," in IEEE Access, vol. 10, pp. 70779-70792, 2022, doi: 10.1109/ACCESS.2022.3187969.
Dr. Hasan Mahmud
Shahed Anzarus Sabab, Mohammad Ridwan Kabira, Sayed Rizban Hussaina, Hasan Mahmud, Md. Kamrul Hasan, Husne Ara Rubaiyeatf, "VIS-iTrack: Visual Intention through Gaze Tracking using Low-Cost Webcam", IEEE Access, 4 July 2022, IEEE, vol. 10, pp. 70779-70792, 2022, doi: 10.1109/ACCESS.2022.3187969. [SCIE/SSCI/Web of Science indexed, IF 3.9] [Q1: Computer Science]
Md. Bakhtiar Hasan
S. Ahmed, M. B. Hasan, T. Ahmed, M. R. K. Sony and M. H. Kabir, "Less is More: Lighter and Faster Deep Neural Architecture for Tomato Leaf Disease Classification," in IEEE Access, vol. 10, pp. 68868-68884, 2022, doi: 10.1109/ACCESS.2022.3187203.
Sabbir Ahmed
Sabbir Ahmed, Md Bakhtiar Hasan, Tasnim Ahmed, Md Redwan Karim Sony, and Md Hasanul Kabir. "Less is more: lighter and faster deep neural architecture for tomato leaf disease classification." IEEE Access 10 (2022): 68868-68884.
Md. Bakhtiar Hasan
M. B. Hasan, T. Ahmed, S. Ahmed and M. H. Kabir, "GaitGCN++: Improving GCN-based Gait Recognition with Part-wise Attention and DropGraph" in Journal of King Saud University - Computer and Information Sciences, vol. 35(7), pp. 101641, 2023, doi: 10.1016/j.jksuci.2023.101641
Dr. Kamrul Hasan
Shahed Anzarus Sabab,Mohammad Ridwan Kabir,Sayed Rizban Hussain,Hasan Mahmud,Husne Ara Rubaiyeat,Md. Kamrul Hasan, "VIS-iTrack: Visual Intention through Gaze Tracking using Low-Cost Webcam", IEEE Access, 2022
Dr. Hasan Mahmud
Fardin Saad, Hasan Mahmud, Mohammad Ridwan Kabir, Md. Alamin Shaheen, Paresha Farastu, Md. Kamrul Hasan, "A Case Study on the Independence of Speech Emotion Recognition in Bangla and English Languages using Language-Independent Prosodic Features", 14 May 2022, https://doi.org/10.48550/arXiv.2111.10776
Dr. Md. Hasanul Kabir
S. Farabi, H.H. Himel, F. Gazzali, M. B.Hasan, M.H. Kabir and M.Farazi, "Improving Action Quality Assessment using ResNets and Weighted Aggregation," in 10th Iberian Conference on Pattern Recognition and Image Analysis (IbPRIA), May 2022, pp. 576–587. DOI: 10.1007/978-3-031-04881-4_46
Dr. Md. Azam Hossain
M. A. Hossain, S. Hwang, and J.-S. Kim, “Resource profiling and performance modeling for distributed scientific computing environments”, Applied Sciences, vol. 12, no. 9, 2022, issn: 2076-3417, (SCIE).
Md. Bakhtiar Hasan
Farabi, S., Himel, H., Gazzali, F., Hasan, M.B., Kabir, M.H., Farazi, M. (2022). Improving Action Quality Assessment Using Weighted Aggregation. In: Pinho, A.J., Georgieva, P., Teixeira, L.F., Sánchez, J.A. (eds) Pattern Recognition and Image Analysis. IbPRIA 2022. Lecture Notes in Computer Science, vol 13256. Springer, Cham. https://doi.org/10.1007/978-3-031-04881-4_46
Md. Jubair Ibna Mostafa
Abdullah Al Jobair, Suzad Mohammad, Zahin Raidah Maisha, Md. Jubair Ibna Mostafa, and Md. Nazmul Haque. “An empirical study on neophytes of stack overflow: How welcoming the community is towards them” in Proceedings of the 17th International Conference on Evaluation of Novel Approaches to Software Engineering, (ENASE), Online Streaming, April 25-26, pages 197–208, 2022. SciTePress
Dr. Md. Hasanul Kabir
M. B. Hasan, T. Ahmed, M. H. Kabir, "HEATGait: Hop-Extracted Adjacency Technique in Graph Convolution based Gait Recognition," International Conference on Advances in Computer Technology, Information Science and Communications (CTISC), April 2022, pp. 1-6. doi: 10.1109/CTISC54888.2022.9849799
Md. Bakhtiar Hasan
M. A. Alanezi, M. S. Shahriar, M. B. Hasan, S. Ahmed, Y. A. Sha’aban and H. R. E. H. Bouchekara, "Livestock Management With Unmanned Aerial Vehicles: A Review," in IEEE Access, vol. 10, pp. 45001-45028, 2022, doi: 10.1109/ACCESS.2022.3168295.
Sabbir Ahmed
Mohammed A. Alanezi, Mohammad S. Shahriar, Md Bakhtiar Hasan, Sabbir Ahmed, Yusuf A. Sha’aban, and Houssem REH Bouchekara. "Livestock Management with Unmanned Aerial Vehicles: A Review." IEEE Access (2022).
Dr. Md. Azam Hossain
I. Hussain, M. A. Hossain, R. Jany, M.-A. Bari, M. Uddin, A. R. M. Kamal, Y. Ku, and J.-S. Kim, “Quantitative evaluation of eeg-biomarkers for prediction of sleep stages”, Sensors, vol. 22, no. 8, 2022, issn: 1424-8220, (SCIE).
Dr. Kamrul Hasan
Mashrur M. Morshed, Ahmad Omar Ahsan, Hasan Mahmud, Md. Kamrul Hasan, Learning Audio Representations with MLPs, Proceedings of Machine Learning Research (PMLR): NeurIPS 2021 Competition Track. https://doi.org/10.48550/arXiv.2203.08490
Dr. Rafsanjany Kushol
Kushol, Rafsanjany, Abbas Masoumzadeh, Dong Huo, Sanjay Kalra, and Yee-Hong Yang. "Addformer: Alzheimer’s disease detection from structural mri using fusion transformer." In 2022 IEEE 19th International Symposium On Biomedical Imaging (ISBI), pp. 1-5. IEEE, 2022.
Dr. Hasan Mahmud
Mashrur M. Morshed, Ahmad Omar Ahsan, Hasan Mahmud, Md. Kamrul Hasan, Learning Audio Representations with MLPs, Proceedings of Machine Learning Research (PMLR): NeurIPS 2021 Competition Track, https://doi.org/10.48550/arXiv.2203.08490
Dr. Kamrul Hasan
Shahida Afrin, Hasan Mahmud, Md. Kamrul Hasan, "EMG-based hand gesture dataset to control electronic wheelchair for SCI patients", The International Con- ference on Computing Advancements (ICCA 2022), Association for Computing Machinery (ACM), New York, NY, USA, 10-12 March 2022
Dr. Hasan Mahmud
Shahida Afrin, Hasan Mahmud, Md. Kamrul Hasan, "EMG-based hand gesture dataset to control electronic wheelchair for SCI patients", The International Conference on Computing Advancements (ICCA 2022), Association for Computing Machinery (ACM), New York, NY, USA, 10-12 March 2022.
Dr. Hasan Mahmud
S. M. Rayeed, Gazi Wasif Akram, Sidratul Tamzida Tuba, Golam Sadman Zilani, Hasan Mahmud, and Md. Kamrul Hasan "Bangla sign digits recognition using depth information", Proc. SPIE 12084, Fourteenth International Conference on Machine Vision (ICMV 2021), 120840P (4 March 2022); https://doi.org/10.1117/12.2623400
Md. Nazmul Haque
Al Jobair, A.; Mohammad, S.; Maisha, Z.; Mostafa, M. and Haque, M. (2022). An Empirical Study on Neophytes of Stack Overflow: How Welcoming the Community is towards Them. In Proceedings of the 17th International Conference on Evaluation of Novel Approaches to Software Engineering, ISBN 978-989-758-568-5, ISSN 2184-4895, pages 197-208.
Ridwan Kabir
M. R. Kabir, M. I. Abedin, R. Ahmed, H. Mahmud and M. K. Hasan, "ANTASID: A Novel Temporal Adjustment to Shannon’s Index of Difficulty for Quantifying the Perceived Difficulty of Uncontrolled Pointing Tasks," in IEEE Access, vol. 10, pp. 21774-21786, 2022, doi: 10.1109/ACCESS.2022.3151696.
Dr. Kamrul Hasan
Mohammad Ridwan Kabir, Mohammad Ishrak Abedin, Rizvi Ahmed, Hasan Mahmud, Md. Kamrul Hasan, "ANTASID: A Novel Temporal Adjustment to Shannon’s Index of Difficulty for Quantifying the Perceived Difficulty of Uncontrolled Pointing Tasks", IEEE Access, 15 February 2022, IEEE, 10.1109/ACCESS.2022.3151696
Dr. Hasan Mahmud
Mohammad Ridwan Kabir, Mohammad Ishrak Abedin, Rizvi Ahmed, Hasan Mahmud, Md. Kamrul Hasan, "ANTASID: A Novel Temporal Adjustment to Shannon’s Index of Difficulty for Quantifying the Perceived Difficulty of Uncontrolled Pointing Tasks", IEEE Access, 15 February 2022, IEEE, 10.1109/ACCESS.2022.3151696 [SCIE/SSCI/Web of Science indexed, IF 3.9] [Q1: Computer Science]
Mohammad Ishrak Abedin
ANTASID: A Novel Temporal Adjustment to Shannon’s Index of Difficulty for Quantifying the Perceived Difficulty of Uncontrolled Pointing Tasks
Dr. Kamrul Hasan
Tasnim Niger, Hasanur Rayhan, Kazi Asif Abdullah Noor, Dr. Kamrul Hasan. Framework for Behavioral Disorder Detection Using Machine Learning and Application of Virtual Cognitive Behavioral Therapy. Journal of Minerva Psychiatry.CoRR abs/2204.13900 (2022)
Dr. Hasan Mahmud
Tasnim Ahmed, Md. Mosinul Kabir, Shahriar Ivan, Hasan Mahmud and Md. Kamrul Hasan, "Am I Being Bullied on Social Media? An Ensemble Approach to Categorize Cyberbullying," 2021 IEEE International Conference on Big Data (Big Data), 2021, pp. 2442-2453, doi: 10.1109/BigData52589.2021.9671594.
Md. Bakhtiar Hasan
Rahman R., Bin Azad Z., Bakhtiar Hasan M. (2022) Densely-Populated Traffic Detection Using YOLOv5 and Non-maximum Suppression Ensembling. In: Arefin M.S., Kaiser M.S., Bandyopadhyay A., Ahad M.A.R., Ray K. (eds) Proceedings of the International Conference on Big Data, IoT, and Machine Learning. Lecture Notes on Data Engineering and Communications Technologies, vol 95. Springer, Singapore. https://doi.org/10.1007/978-981-16-6636-0_43
2021 (25)
Dr. Md. Azam Hossain
I. Hussain, M. A. Hossain, and S.-J. Park, "A healthcare digital twin for diagnosis of stroke", in 2021 IEEE International Conference on Biomedical Engineering, Computer and Information Technology for Health (BECITHCON), IEEE, Dhaka, Bangladesh, Dec. 2021, pp. 1821.
Shahriar Ivan
T. Ahmed, M. Kabir, S. Ivan, H. Mahmud and K. Hasan, "Am I Being Bullied on Social Media? An Ensemble Approach to Categorize Cyberbullying," 2021 IEEE International Conference on Big Data (Big Data), 2021, pp. 2442-2453, doi: 10.1109/BigData52589.2021.9671594.
Dr. Kamrul Hasan
Tasnim Ahmed, Md. Mosinul Kabir, Shahriar Ivan, Hasan Mahmud and Md. Kamrul Hasan, "Am I Being Bullied on Social Media? An Ensemble Approach to Categorize Cyberbullying," 2021 IEEE International Conference on Big Data (Big Data), 2021, pp. 2442-2453, doi: 10.1109/BigData52589.2021.9671594
Mueeze Al Mushabbir
End-to-End Natural Language Understanding Pipeline for Bangla Conversational Agents (ICMLA) [DOI: 10.1109/ICMLA52953.2021.00039]
Md. Zahidul Islam
A. S. A. Rabby, M. M. Islam, \textbf{Z. Islam}, N. Hasan and F. Rahman, \textbf{"Towards Building A Robust Large-Scale Bangla Text Recognition Solution Using A Unique Multiple-Domain Character-Based Document Recognition Approach"}, 2021 20th IEEE International Conference on Machine Learning and Applications (ICMLA), Pasadena, CA, USA, Dec. 13-16 2021, pp. 1393-1399
Dr. Kamrul Hasan
MD. Nazmus Sakib, Mehrab Mustafy Rahman, Hasan Mahmud, Md. Kamrul Hasan, "Augmented Reality Based Lifelogging System For Reminiscence", International Conference on Fourth Industrial Revolution and Beyond 2021 - IC4IR 2021, Organized by UGC, Dhaka, 10-11 December, 2021
Dr. Hasan Mahmud
MD. Nazmus Sakib, Mehrab Mustafy Rahman, Hasan Mahmud, Md. Kamrul Hasan, "Augmented Reality Based Lifelogging System For Reminiscence", International Conference on Fourth Industrial Revolution and Beyond 2021 - IC4IR 2021, Organized by UGC, Dhaka, 10-11 December, 2021.
Dr. Kamrul Hasan
S. M. Rayeed, Sidratul Tamzida Tuba, Golam Sadman Zilanni, Hasan Mahmud, Md. Kamrul Hasan, "Bangla Sign Digits Recognition using Depth Information", The 14th International Conference on Machine Vision (ICMV 2021), 8-12 Novemver, 2021, Rome, Italy
Dr. Kamrul Hasan
Hasan Mahmud, Robiul Islam, Md. Kamrul Hasan, "On-air English Capital Alphabet (ECA) recognition using depth information", The Visual Computer Journal, 30 January 2021, Springer-Verlag GmbH Germany, part of Springer Nature, https://doi.org/10.1007/s00371-021-02065-x
Dr. Md. Azam Hossain
M. R. Karim, S. K. Dey, T. Islam, S. Sarker, M. H. Menon, K. Hosain, M. A. Hossain, and S. Decker, "Deephateexplainer: Explainable hate speech detection in under-resourced bengali language", in 2021 IEEE 8th International Conference on Data Science and Advanced Analytics (DSAA), IEEE, Porto, Portugal, Oct. 2021, pp. 110 (A* Conference).
Sabbir Ahmed
Arowa Yasmeen, Fariha Ishrat Rahman, Sabbir Ahmed, Md. Hasanul Kabir, "CSVC-Net: Code-Switched Voice Command Classification using Deep CNN-LSTM Network", Joint 2021 5th International Conference on Imaging, Vision & Pattern Recognition (IVPR) and10th International Conference on Informatics, Electronics & Vision (ICIEV), 2021
Sabbir Ahmed
Ayesha khatun, Sajid shahriar, Hasibul islam, Krishna das, Sabbir Ahmed, Md. Sakibul Islam, "A Systematic Review on the Chronological Development of Bangla Sign Language Recognition Systems", Joint 2021 5th International Conference on Imaging, Vision & Pattern Recognition (IVPR) and10th International Conference on Informatics, Electronics & Vision (ICIEV), 2021
Dr. Md. Hasanul Kabir
A. Yasmeen, F. I. Rahman, S. Ahmed and M. H. Kabir, "CSVC-Net: Code-Switched Voice Command Classification using Deep CNN-LSTM Network," 2021 Joint 10th International Conference on Informatics, Electronics & Vision (ICIEV) and 2021 5th International Conference on Imaging, Vision & Pattern Recognition (icIVPR), 2021, pp. 1-8, doi: 10.1109/ICIEVicIVPR52578.2021.9564183. [Best Presentation Award]
Dr. Md. Hasanul Kabir
S. N. Hossain, M. H. Kabir and A. Pal, "Alignment Free Sequence Similarity Estimation using Local Binary Pattern on DNA Trajectory Images," 2021 Joint 10th International Conference on Informatics, Electronics & Vision (ICIEV) and 2021 5th International Conference on Imaging, Vision & Pattern Recognition (icIVPR), 2021, pp. 1-7, doi: 10.1109/ICIEVicIVPR52578.2021.9564141.
A.B.M. Ashikur Rahman
Uddin, SM Shihab, Md Samin Morshed, Mahruf Islam Prottoy, and ABM Ashikur Rahman. "Age Estimation from Facial Images using Transfer Learning and K-fold Cross-Validation." In 2021 3rd International Conference on Pattern Recognition and Intelligent Systems, pp. 33-36. 2021.
Md. Zahidul Islam
Z. Islam, M. Rukonuzzaman, R. Ahmed, M. H. Kabir and M. Farazi, "Efficient Two-Stream Network for Violence Detection Using Separable Convolutional LSTM", International Joint Conference on Neural Networks (IJCNN), Shenzhen, China, July 18-22, 2021, pp. 1-8
Dr. Md. Hasanul Kabir
Z. Islam, M. Rukonuzzaman, R. Ahmed, M. H. Kabir and M. Farazi, "Efficient Two-Stream Network for Violence Detection Using Separable Convolutional LSTM," 2021 International Joint Conference on Neural Networks (IJCNN), 2021, pp. 1-8, doi: 10.1109/IJCNN52387.2021.9534280.
Dr. Md. Azam Hossain
B. Al-athwari and M. A. Hossain, "Iot architecture: Challenges and open research issues", in Proceedings of 2nd International Conference on Smart Computing and Cyber Security: Strategic Foresight, Security Challenges and Innovation (SMARTCYBER 2021), Springer, Guseong-gun, Republic of Korea, Jun. 2021, pp. 408419. (Scopus Indexed)
Dr. Md. Azam Hossain
M. A. Hossain, I. Hussain, B. Al-Athwari, and S. Dahit, "Network traffic anomalies detection using machine learning algorithm: A performance study", in Proceedings of 2nd International Conference on Smart Computing and Cyber Security: Strategic Foresight, Security Challenges and Innovation (SMARTCYBER 2021), Springer, Guseong-gun, Republic of Korea, Jun. 2021, pp. 274282. (Scopus Indexed)
Dr. Md. Azam Hossain
I. Hussain, M. A. Hossain, and S.-J. Park, "A healthcare digital twin for diagnosis of stroke", in 2021 IEEE International Conference on Biomedical Engineering, Computer and Information Technology for Health (BECITHCON), IEEE, Dhaka, Bangladesh, Dec. 2021, pp. 1821.
Dr. Md Moniruzzaman
P. Black, I. Gondal, A. Bagirov, and M. Moniruzzaman, “Malware Variant Identification Using Incremental Clustering,” Electronics, vol. 10, no. 14, p. 1628, Jul. 2021.
Dr. Md. Hasanul Kabir
A. I. Champa, M. F. Rabbi, S. M. Mahedy Hasan, A. Zaman and M. H. Kabir, "Tree-Based Classifier for Hyperspectral Image Classification via Hybrid Technique of Feature Reduction," 2021 International Conference on Information and Communication Technology for Sustainable Development (ICICT4SD), 2021, pp. 115-119, doi: 10.1109/ICICT4SD50815.2021.9396809.
Dr. Hasan Mahmud
Hasan Mahmud, Robiul Islam, Md. Kamrul Hasan, "On-air English Capital Alphabet (ECA) recognition using depth information", The Visual Computer Journal, 30 January 2021, Springer-Verlag GmbH Germany, part of Springer Nature, https://doi.org/10.1007/s00371-021-02065-x [SCIE/Web of Science indexed, IF 3.5] [Q2: Computer Vision and Pattern Recognition]
Dr. Md. Azam Hossain
Hossain Md Azam and Baseem Al-Atwari, "Blockchain-Based IoT Forensics: Challenges and State-of-the-art Frameworks", Artificial Intelligence and Blockchain for Future Cybersecurity Applications, 361 Springer, 2021.
2020 (26)
Ashraful Alam Khan
Kabir, K. Habibul, Ashraful Alam Khan, Ashir Ahmed, Masahiro Sasabe, and Khondaker Hasibul Kabir. 2020. "AsthaNet: Co-Creating Network Solution for Socio-Economic Development of Disconnected Communities". International Journal of Humanitarian Technology 1 (2): 172-209. Inderscience Publishers. doi:10.1504/ijht.2020.10034657.
Dr. Kamrul Hasan
MF Rabbi, SMM Hasan, AI Champa, M AsifZaman, MK Hasan. Prediction of Liver Disorders using Machine Learning Algorithms: A Comparative Study. 2020 2nd International Conference on Advanced Information and Communication Technology (ICAICT).
Dr. Md. Hasanul Kabir
R. Kushol, M. H. Kabir, M. Abdullah-Al-Wadud, and M. S. Islam, “Retinal blood vessel segmentation from fundus image using an efficient multiscale directional representation technique Bendlets,” Math. Biosci. Eng., vol. 17, no. 6, pp. 7751–7771, 2020. [SCIE]
Dr. Rafsanjany Kushol
Kushol, Rafsanjany, Md Hasanul Kabir, M. Abdullah-Al-Wadud, and Md Saiful Islam. "Retinal blood vessel segmentation from fundus image using an efficient multiscale directional representation technique Bendlets." Mathematical Biosciences and Engineering 17, no. 6 (2020): 7751-7771.
Dr. Md. Hasanul Kabir
Faisal Muhammad Shah, Farzad Ahmed, Sajib Kumar Saha Joy, Sifat Ahmed, Samir Sadek, Rimon Shil, and Md Hasanul Kabir, “Early depression detection from social network using deep learning techniques,” in IEEE Region 10 Symposium (TENSYMP), 2020, pp. 823-826.
Dr. Rafsanjany Kushol
Kushol, Rafsanjany, and Md Sirajus Salekin. "Rbvs-net: A robust convolutional neural network for retinal blood vessel segmentation." In 2020 IEEE International Conference on Image Processing (ICIP), pp. 398-402. IEEE, 2020.
Tanjila Alam Sathi
Mohammad Sabik Irbaz, Abir Azad, Tanjila Alam Sathi, and Lutfun Nahar Lota,"Nurse care activity recognition based on machine learning techniques using accelerometer data," In Adjunct Proceedings of the 2020 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2020 ACM International Symposium on Wearable Computers (UbiComp-ISWC '20). Association for Computing Machinery, New York, NY, USA, 402–407.DOI: 10.1145/3410530.3414339
Dr. Hasan Mahmud
Mohsinul Kabir, Quazi Fahim Faisal Dhruba, Hasan Mahmud, Md Kamrul Hasan, Ahsan Rejwan Zaman, "Gaming Insight: Conversion of Popular Sedentary Games into Motion-Based Form", International Journal of Human–Computer Interaction, Taylor & Francis, Volume 36, Issue 13, Pages 1205-1215, 8 August 2020, doi: 10.1080/10447318.2020.1726597 [SCI/SCIE/SSCI Web of Science, IF 4.920] [Q1: Human Factors and Ergonomics]
Md. Nazmul Haque
Fazle Rabbi, Md. Nazmul Haque, Md. Eusha Kadir, Md. Saeed Siddik and Ahmedul Kabir, "An Ensemble Approach to Detect Code Comment Inconsistencies using Topic Modeling”,The 32nd International Conference on Software Engineering and Knowledge Engineering, SEKE 2020, KSIR Virtual Conference Center, USA, July 9-19, 2020.
Dr. Kamrul Hasan
Kabir, M., Dhruba, Q.F., Mahmud, H., Hasan, M.K., & Zaman, A.R. (2020). Gaming Insight: Conversion of Popular Sedentary Games into Motion-Based Form. International Journal of Human–Computer Interaction, 36, 1205 - 1215.
Md. Nazmul Haque
Md Nazmul Haque, Sadia Sharmin, Amin Ahsan Ali, Abu Ashfaqur Sajib, Mohammad Shoyaib. "Use of relevancy and complementary information for discriminatory gene selection from high-dimensional gene expression data". PLOS ONE 16(10): e0230164. https://doi.org/10.1371/journal.pone.0230164
Dr. Hasan Mahmud
Ahmed Al Marouf, Md Kamrul Hasan, Hasan Mahmud, "Comparative analysis of feature selection algorithms for computational personality prediction from social media", IEEE Transactions on Computational Social Systems, Volume 7, Issue 3, Pages 587-599, 19 February, 2019, 10.1109/TCSS.2020.2966910 [SCIE/Web of Science IF 5] [Q1: Human-Computer Interaction]
Tareque Mohmud Chowdhury
Ahmed, T., Rahman, A., Chowdhury, T.M., Kushol, R., & Raihan, M.A. (2020). A Novel Approach to Classify Electrocardiogram Signals Using Deep Neural Networks. 2020 2nd International Conference on Computer and Information Sciences (ICCIS), 1-6.
Sadia Sharmin
Puloma Roy, Sadia Sharmin, Amin Ahsan Ali, Mohammad Shoyaib . Discretization and Feature Selection Based on Bias Corrected Mutual Information Considering High-Order Dependencies. In Pacific-Asia Conference on Knowledge Discovery and Data Mining, 2020
Sadia Sharmin
Md Eusha Kadir, Pritom Saha Akash, Sadia Sharmin, Amin Ahsan Ali, Mohammad Shoyaib . A Proximity Weighted Evidential k Nearest Neighbor Classifier for Imbalanced Data. In Pacific-Asia Conference on Knowledge Discovery and Data Mining, 2020
Sadia Sharmin
Md Nazmul Haque, Sadia Sharmin, Amin Ahsan Ali, Abu Ashfaqur Sajib, Mohammad Shoyaib . Use of relevancy and complementary information for discriminatory gene selection from high-dimensional cancer data. In bioRxiv, 2020
Tasnim Ahmed
A Novel Approach to Classify Electrocardiogram Signals Using Deep Neural Networks - Tasnim Ahmed, Ariq Rahman, Tareque Mohmud Chowdhury, Rafsanjany Kushol, Md. Nishat Raihan - 2020 International Conference on Computer and Information Sciences (ICCIS)
Lutfun Nahar Lota
Rasul, Md Golam, Mashrur Hossain Khan, and Lutfun Nahar Lota. "Nurse care activity recognition based on convolution neural network for accelerometer data." Adjunct Proceedings of the 2020 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2020 ACM International Symposium on Wearable Computers. 2020.
Lutfun Nahar Lota
Irbaz, Mohammad Sabik, et al. "Nurse care activity recognition based on machine learning techniques using accelerometer data." Adjunct Proceedings of the 2020 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2020 ACM International Symposium on Wearable Computers. 2020.
Dr. Md. Azam Hossain
Hossain Md Azam, Baseem Al-Atwari, Jik-Soo Kim, and Soonwook Hwang. " Exploring the Volatility of Large-Scale Shared Distributed Computing Resources." Proceedings of?International Conference on Smart Computing and Cyber Security: Strategic Foresight, Security Challenges and Innovation, Springer Lecture Notes in Network and System, v.149, ISBN 978-981-15-7990-5, Republic of Korea, July 07- 08, 2020. (Scopus Indexed)
2019 (30)
Dr. Hasan Mahmud
Muhammad Shihab Rashid, Zubayet Zaman, Hasan Mahmud, Md. Kamrul Hasan, "Emotion Recognition with Forearm-based Electromyography" November 2019, https://doi.org/10.48550/arXiv.1911.05305
Dr. Kamrul Hasan
Ahmed Al Marouf, Md Kamrul Hasan, Hasan Mahmud, "Comparative analysis of feature selection algorithms for computational personality prediction from social media", IEEE Transactions on Computational Social Systems, Volume 7, Issue 3, Pages 587-599, 19 February, 2019, 10.1109/TCSS.2020.2966910
Md. Nazmul Haque
Md. Nazmul Haque, Mahir Mahbub, Md Hasan Tarek, Lutfun Nahar Lota, and Amin Ahsan Ali, "Nurse care activity recognition: a GRUbased approach with attention mechanism”In Adjunct Proceedings of the 2019 ACM International Joint Conference on Pervasive and Ubiquitous Computing and the 2019 International Symposium on Wearable Computers (UbiComp/ISWC ’19 Adjunct), pp. 719-723. 2019
Dr. Muhammad Mahbub Alam
Aziz, T.I., Protik, S., Hossen, M.S., Choudhury, S., & Alam, M.M. (2019). Degree-based Balanced Clustering for Large-Scale Software Defined Networks. 2019 IEEE Wireless Communications and Networking Conference (WCNC), 1-6.
Dr. Md. Hasanul Kabir
A. S. Rubel, A. Ahsan Chowdhury and M. H. Kabir, "Facial Expression Recognition Using Adaptive Robust Local Complete Pattern," 2019 IEEE International Conference on Image Processing (ICIP), 2019, pp. 41-45, doi: 10.1109/ICIP.2019.8802911.
Dr. Kamrul Hasan
Islam, M.U., Mahmud, H., Ashraf, F., Hossain, I., & Hasan, M. (2017). Yoga posture recognition by detecting human joint points in real time using microsoft kinect. 2017 IEEE Region 10 Humanitarian Technology Conference (R10-HTC), 668-673.
Dr. Md. Sakhawat Hossen
Hassan, M.Y., Hussain, F., Hossen, M.S., & Choudhury, S. (2019). An online resource allocation algorithm to minimize system interference for inband underlay D2D communications. Int. J. Commun. Syst., 32.
Dr. Md. Sakhawat Hossen
Aziz, T.I., Protik, S., Hossen, M.S., Choudhury, S., & Alam, M.M. (2019). Degree-based Balanced Clustering for Large-Scale Software Defined Networks. 2019 IEEE Wireless Communications and Networking Conference (WCNC), 1-6.
Md. Jubair Ibna Mostafa
Ali Zafar Sadiq, Md. Jubair Ibna Mostafa and Kazi Sakib, "On the Evolutionary Relationship between Change Coupling and Fix-Inducing Changes," In Proceedings of the 14th International Conference on Evaluation of Novel Approaches to Software Engineering (ENASE), Heraklion, Crete, Greece, 2019 pages. 494-501. DOI: 10.5220/0007758804940501
Dr. Kamrul Hasan
Rahman, M.M., Hasan, M.K. A framework for predicting personalized product packages. International Journal of Advanced Trends in Computer Science and Engineering, 2019, 8(4), pp. 1069–1075
Md. Nazmul Haque
Md. Nazmul Haque, M Tanjid Hasan Tonmoy, Saif Mahmud, Amin Ahsan Ali, Muhammad Asif Hossain Khan, Mohammad Shoyaib, GRU-based Attention Mechanism for Human Activity Recognition”,ICASERT-2019: 1st International Conference on Advances in Science, Engineering and Robotics Technology.
Dr. Md. Sakhawat Hossen
Munir, A., Laskar, M.T., Hossen, M.S., & Choudhury, S. (2019). A localized fault tolerant load balancing algorithm for RFID systems. Journal of Ambient Intelligence and Humanized Computing, 1-13.
Md. Jubair Ibna Mostafa
Md. Jubair Ibna Mostafa, "An Empirical Study on Clone Evolution by Analyzing Clone Lifetime," In Proceedings of the IEEE 13th International Workshop on Software Clones (IWSC) co-located with Software Analysis, Evolution and Reengineering (SANER), Hangzhou, China, 2019, pages. 20-26. DOI: 10.1109/IWSC.2019.8665850
Shohel Ahmed
Shohel ahmed, Shake Md. Riazul Islam, Kwak Kyung Sup - “METHOD AND SYSTEM FOR FINGERPRINT-BASED PAYMENT” Application No.(Date) 1020170141375 (2017.10.27),Publication : KR101951125B1, Publication Date:2019-02-21
Md. Jubair Ibna Mostafa
Ali Zafar Sadiq, Ahmedul Kabir, Pritom Saha Akash and Md. Jubair Ibna Mostafa, "Analyzing Corrective Maintenance using Change Coupled Clusters at Fix-inducing Changes," In Proceedings of the International Conference on Electrical, Computer and Communication Engineering (ECCE), Cox’sBazar, Bangladesh, 2019, pages. 1-6. DOI: 10.1109/ECACE.2019.8679503
Dr. Kamrul Hasan
Sobhan, M., Chowdhury, M.Z., Ahsan, I., Mahmu, H., & Hasan, M. (2019). A Communication Aid System for Deaf and Mute using Vibrotactile and Visual Feedback. 2019 International Seminar on Application for Technology of Information and Communication (iSemantic), 184-190.
Abu Raihan Mostofa Kamal
M. R. Islam, S. J. Miah, A. R. M. Kamal, and O. Burmeister, “A design construct of developing approaches to measure mental health conditions,” Australasian Journal of Information Systems, vol. 23, 2019.
Dr. Md. Hasanul Kabir
A. A. Rahman, M. R. Karim, R. Kushol, and M. H. Kabir, “Performance Comparison of Feature Descriptors in Offline Signature Verification,” Journal of Engineering and Technology, vol. 14, no. 1, 2018.
Sadia Sharmin
Md Eusha Kadir, Pritom Saha Akash, Sadia Sharmin, Amin Ahsan Ali, Mohammad Shoyaib . Can a simple approach identify complex nurse care activity?. In Adjunct Proceedings of the 2019 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2019 ACM International Symposium on Wearable Computers, 2019
Sadia Sharmin
Sadia Sharmin, Amin Ahsan Ali, Muhammad Asif Hossain Khan, MohammadShoyaib and Oksam Chae . Simultaneous feature selection and discretization based on mutual information. In Pattern Recognition, Elsevier, 2019
Tasnim Ahmed
A Complete Bangla Optical Character Recognition System: An Effective Approach - Tasnim Ahmed, Md. Nishat Raihan, Rafsanjany Kushol, Md Sirajus Salekin - 2019 22nd International Conference on Computer and Information Technology (ICCIT)
Lutfun Nahar Lota
Haque, Md Nazmul, Mahir Mahbub, Md Hasan Tarek, Lutfun Nahar Lota, and Amin Ahsan Ali. "Nurse Care Activity Recognition: A GRU-based approach with attention mechanism." In Adjunct Proceedings of the 2019 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2019 ACM International Symposium on Wearable Computers, pp. 719-723. 2019.
A.B.M. Ashikur Rahman
Kushol, R., Raihan, M., Salekin, M. S., & Rahman, A. B. M. (2019). Contrast Enhancement of Medical X-Ray Image Using Morphological Operators with Optimal Structuring Element. arXiv preprint arXiv:1905.08545.
Faisal Hussain
M. Y. Hassan, F. Hussain, and S. Choudhury "Connectivity Preserving Obstacle Avoidance Localized Motion Planning Algorithms for Mobile Wireless Sensor Networks", Peer-to-Peer Networking and Applications, 2019, 12(3), pp. 647–659. DOI: 10.1007/s12083-018-0656-y
Faisal Hussain
M. Y. Hassan, F. Hussain, M. S. Hossen, S. Choudhury, "An online resource allocation algorithm to minimize system interference for inband underlay D2D communications", International Journal of Communication Systems, 2019, 32(13), e4011. DOI: 10.1002/dac.4011
2018 (21)
Redwan Karim Sony
Rahman, A. B. M. A., Karim, M. R., Kushol, R., Kabir M. H. (2018). Performance Comparison of Feature Descriptors in Offline Signature Verification. IUT Journal of Engineering and Technology, 14(1). http://jet.iutoic-dhaka.edu/assets/publishedPaper/14_1_1.pdf
Dr. Hasan Mahmud
Ahmed Al Marouf, Md. Kamrul Hasan, and Hasan Mahmud, "Fingertip Detection and Finger Identification Approach for Hand Gesture Recognition using Microsoft Kinect", IUT Journal of Engineering and Technology (JET), Volume 14, Issue 1, December, 2018. https: //old.jet.iutoic-dhaka.edu/assets/publishedPaper/14_1_5.pdf
Dr. Hasan Mahmud
Hasan Mahmud, Md. Kamrul Hasan, Abdullah-Al-Tariq, Md. Hasanul Kabir, and M. A. Mottalib, “Recognition of Symbolic Gestures Using Depth Information”, Advances in Human-Computer Interaction, vol. 2018, Article ID 1069823, 13 pages, 2018. https://doi.org/10.1155/2018/1069823. [ESCI/Web of Science, Scopus, IF 2.9] [Q2: Human-Computer Interaction]
Dr. Md. Hasanul Kabir
Hasan Mahmud, Md. Kamrul Hasan, Abdullah-Al-Tariq, M. H. Kabir, and M. A. Mottalib, "Recognition of Symbolic Gestures Using Depth Information", Advances in Human-Computer Interaction, vol. 2018, 2018. (ESCI)
Dr. Kamrul Hasan
Hasan Mahmud, Md. Kamrul Hasan, Abdullah-Al-Tariq, Md. Hasanul Kabir, and M. A. Mottalib, Recognition of Symbolic Gestures Using Depth Information, Advances in Human-Computer Interaction, vol. 2018, Article ID 1069823, 13 pages, 2018. https://doi.org/10.1155/2018/1069823.
Dr. Kamrul Hasan
Md. Abed Rahman, A. M. Esfar E Alam, Md. Kamrul Hasan and Hasan Mahmud, "Towards A Complete Smartphone Based Lifelogging System for Reminiscence", IUT Journal of Engineering and Technology (JET), Volume 14, Number 1, December 2018.
Dr. Hasan Mahmud
Md. Abed Rahman, A. M. Esfar E Alam, Md. Kamrul Hasan and Hasan Mahmud, "Towards A Complete Smartphone Based Lifelogging System for Reminiscence", IUT Journal of Engineering and Technology (JET), Volume 12, Issue 2, 2018.
Abu Raihan Mostofa Kamal
M. R. Islam, A. R. M. Kamal, N. Sultana, R. Islam, M. A. Moni, et al., “De- tecting depression using k-nearest neighbors (knn) classification technique,” in 2018 International Conference on Computer, Communication, Chemical, Material and Electronic Engineering (IC4ME2), pp. 1–4, IEEE, 2018.
Ahnaf Munir
Ahnaf Munir, Md. Tahmid Rahman Laskar, Md. Sakhawat Hossen Salimur Choudhury., ”A localized fault tolerant load balancing algorithm for RFID systems”, Journal of Ambient Intelligence and Humanized Computing (2018) doi: 10.1007/s12652-018-1114-7
Md. Nazmul Haque
Sayeda Shamma Alia, Md. Nazmul Haque, Sadia Sharmin, Shah Mostafa Khaled, Mohammad Shoyaib, "Bug Severity Classification Based on Class-Membership Information”,2018 Joint 7th International Conference on Informatics, Electronics and Vision (ICIEV) and 2018 2nd International Conference on Imaging, Vision and Pattern Recognition (icIVPR)
Dr. Muhammad Mahbub Alam
Hossen, M.S., Hassan, M.Y., Hussain, F., Choudhury, S., & Alam, M.M. (2018). Relax online resource allocation algorithms for D2D communication. Int. J. Commun. Syst., 31.
Dr. Md. Hasanul Kabir
F. Ahmed and M. H. Kabir, “Facial expression recognition under difficult conditions: A comprehensive study on edge directional texture patterns,” Int. J. Appl. Math. Comput. Sci., vol. 28, no. 2, pp. 399–409, 2018. (SCIE)
Dr. Md. Sakhawat Hossen
Hossen, M.S., Hassan, M.Y., Hussain, F., Choudhury, S., & Alam, M.M. (2018). Relax online resource allocation algorithms for D2D communication. Int. J. Commun. Syst., 31.
Dr. Md. Sakhawat Hossen
Hussain, F., Hassan, M.Y., Hossen, M.S., & Choudhury, S. (2018). System Capacity Maximization With Efficient Resource Allocation Algorithms in D2D Communication. IEEE Access, 6, 32409-32424.
Abu Raihan Mostofa Kamal
A. R. Chowdhury, J. Mahmud, A. R. M. Kamal, and M. A. Hamid, “Maes: modified advanced encryption standard for resource constraint environ- ments,” in 2018 IEEE Sensors Applications Symposium (SAS), pp. 1–6, IEEE, 2018.
Abu Raihan Mostofa Kamal
M. R. Islam, M. A. Kabir, A. Ahmed, A. R. M. Kamal, H. Wang, and A. Ulhaq, “Depression detection from social network data using machine learning techniques,” Health information science and systems, vol. 6, no. 1, p. 8, 2018.
Abu Raihan Mostofa Kamal
M. A. Hamid, M. Abdullah-Al-Wadud, M. M. Hassan, A. Almogren, A. Alamri, A. R. M. Kamal, and M. Mamun-Or-Rashid, “A key distribu- tion scheme for secure communication in acoustic sensor networks,” Future Generation Computer Systems, vol. 86, pp. 1209–1217, 2018.
Sadia Sharmin
Sayeda Shamma Alia, Md Nazmul Haque, Sadia Sharmin, Shah Mostafa Khaled, Mohammad Shoyaib . Bug Severity Classification Based on Class-Membership Information. In 2018 Joint 7th International Conference on Informatics, Electronics & Vision (ICIEV) and 2018 2nd International Conference on Imaging, Vision & Pattern Recognition (icIVPR), 2018
A.B.M. Ashikur Rahman
Rahman, A. A., Karim, M. R., Kushol, R., & Kabir, M. H. (2018). Performance Comparison of Feature Descriptors in Offline Signature Verification. IUT Journal of Engineering and Technology (JET), 2018
Faisal Hussain
M. S. Hossen, M. Y. Hassan, F. Hussain, S. Choudhury and M M Alam, "Relax Online Resource Allocation Algorithms for D2D Communication", International Journal of Communication Systems, 2018; 31:e3555. DOI: 10.1002/dac.3555
Faisal Hussain
F. Hussain, M. Y. Hassan, M. S. Hossen and S. Choudhury, "System Capacity Maximization With Efficient Resource Allocation Algorithms in D2D Communication," IEEE Access, vol. 6, pp. 32409-32424, 2018. DOI: 10.1109/ACCESS.2018.2839190
2017 (23)
Ashraful Alam Khan
Kabir, K. Habibul, Ashraful Alam Khan, Ashir Ahmed, Masahiro Sasabe, and K. Hasibul Kabir. 2017. "Ferry Assisted Delay Tolerant Networking Approach For Carrying Healthcare Digital Data In Disconnected Communities". In International Conference on Healthcare, SDGs and Social Business (SocialTech). Tokyo: Social Business Academia Network.
Dr. Kamrul Hasan
Ahmed Al Marouf, Md. Kamrul Hasan and Hasan Mahmud. Fingertip Detection and Finger Identification Approach for Hand Gesture Recognition using Microsoft Kinect. IUT Journal of Engineering and Technology (JET), Volume 14, Number 1, December 2018.
Dr. Hasan Mahmud
S. M. Shahnewaz, Husne Ara Rubaiyeat, Hasan Mahmud, Md. Kamrul Hasan, "A Scenario Based API Recommendation System Using Syntax and Semantics of Client Source Code", IUT Journal of Engineering and Technology (JET), Volume 2, Issue 1, September 2017.
Dr. Md. Sakhawat Hossen
Y. Hassan, F. Hussain, S. Hossen, S. Choudhury and M. M. Alam, "Interference Minimization in D2D Communication Underlaying Cellular Networks," in IEEE Access, vol. 5, pp. 22471-22484, 2017, doi: 10.1109/ACCESS.2017.2763424.
Dr. Kamrul Hasan
S. M. Shahnewaz, Husne Ara Rubaiyeat, Hasan Mahmud, Md. Kamrul Hasan, "A Scenario Based API Recommendation System Using Syntax and Semantics of Client Source Code", IUT Journal of Engineering and Technology (JET), Volume 13, Number 1, December 2016.
Redwan Karim Sony
Mottalib, M. A., Arnob, R. I., Sony, M. R. K., & Akter, L. (2017). Advanced Agglomerative Clustering Technique for Phylogenetic Classification Using Manhattan Distance. In Proceedings of the International Conference on Bioinformatics & Computational Biology (BIOCOMP) (pp. 9-13). The Steering Committee of The World Congress in Computer Science, Computer Engineering and Applied Computing (WorldComp).
Abu Raihan Mostofa Kamal
A. Al-Tariq, A. R. M. Kamal, M. A. Hamid, M. Abdullah-Al-Wadud, M. M. Hassan, and S. M. M. Rahman, “A scalable framework for protecting user identity and access pattern in untrusted web server using forward secrecy, public key encryption and bloom filter,” Concurrency and Computation: Practice and Experience, vol. 29, no. 23, p. e3863, 2017.
Dr. Muhammad Mahbub Alam
Hassan, M.Y., Hussain, F., Hossen, M.S., Choudhury, S., & Alam, M.M. (2017). A near optimal interference minimization resource allocation algorithm for D2D communication. 2017 IEEE International Conference on Communications (ICC), 1-6.
Dr. Md. Hasanul Kabir
R. Kushol, M. H. Kabir, M. S. Salekin, and A. B. M. A. Rahman, “Contrast enhancement by top-hat and bottom-hat transform with optimal structuring element: Application to retinal vessel segmentation,” in International Conference on Image Analysis and Recognition (ICIAR), 2017, pp. 533–540.
Dr. Md. Sakhawat Hossen
Hussain, F., Hassan, M.Y., Hossen, M.S., & Choudhury, S. (2017). An optimal resource allocation algorithm for D2D communication underlaying cellular networks. 2017 14th IEEE Annual Consumer Communications & Networking Conference (CCNC), 867-872.
Dr. Md. Sakhawat Hossen
Hassan, M.Y., Hussain, F., Hossen, M.S., Choudhury, S., & Alam, M.M. (2017). A near optimal interference minimization resource allocation algorithm for D2D communication. 2017 IEEE International Conference on Communications (ICC), 1-6.
Dr. Rafsanjany Kushol
Kushol, Rafsanjany, Md Hasanul Kabir, Md Sirajus Salekin, and ABM Ashikur Rahman. "Contrast enhancement by top-hat and bottom-hat transform with optimal structuring element: Application to retinal vessel segmentation." In Image Analysis and Recognition: 14th International Conference, ICIAR 2017, Montreal, QC, Canada, July 5–7, 2017, Proceedings 14, pp. 533-540. Springer International Publishing, 2017.
Dr. Md. Hasanul Kabir
M. H. Kabir, M. S. Salekin, M. Z. Uddin, and M. Abdullah-Al-Wadud, “Facial expression recognition from depth video with patterns of oriented motion flow,” IEEE Access, vol. 5, pp. 8880–8889, 2017. (SCIE)
Dr. Muhammad Mahbub Alam
Hassan, Y., Hussain, F., Hossen, S., Choudhury, S., & Alam, M.M. (2017). Interference Minimization in D2D Communication Underlaying Cellular Networks. IEEE Access, 5, 22471-22484.
Abu Raihan Mostofa Kamal
A. R. M. Kamal and M. A. Hamid, “Supervisory routing control for dynamic load balancing in low data rate wireless sensor networks,” Wireless Networks, vol. 23, no. 4, pp. 1085–1099, 2017.
Sadia Sharmin
Sadia Sharmin, Amin Ahsan Ali, Muhammad Asif Hossain Khan, Mohammad Shoyaib . Feature selection and discretization based on mutual information. In 2017 IEEE International Conference on Imaging, Vision & Pattern Recognition (icIVPR), 2017
Sadia Sharmin
Sadia Sharmin, Farzana Aktar, Amin Ahsan Ali, Muhammad Asif Hossain Khan, Mohammad Shoyaib . Bfsp: A feature selection method for bug severity classification. In 2017 IEEE Region 10 Humanitarian Technology Conference (R10-HTC), 2017
Lutfun Nahar Lota
Lota, L.N. and Hossain, B.M., 2017. A systematic literature review on sms spam detection techniques. International Journal of Information Technology and Computer Science, 9(7), pp.42-50.
A.B.M. Ashikur Rahman
Kushol, R., Kabir, M. H., Salekin, M. S., & Rahman, A. A. (2017, July). Contrast enhancement by top-hat and bottom-hat transform with optimal structuring element: application to retinal vessel segmentation. In International Conference Image Analysis and Recognition (pp. 533-540). Springer, Cham.
Faisal Hussain
F. Hussain, M. Y. Hassan, M. S. Hossen, and S. Choudhury, "An Optimal Resource Allocation Algorithm for D2D Communication Underlaying Cellular Networks" in 14th Annual IEEE Consumer Communications & Networking Conference (CCNC 2017), Las Vegas, USA, Jan. 2017. DOI: 10.1109/CCNC.2017.7983247"
Faisal Hussain
M. Y. Hassan, F. Hussain, M. S. Hossen, S. Choudhury and Muhammad Mahbub Alam, "A Near Optimal Interference Minimization Resource Allocation Algorithm for D2D Communication" in IEEE International Conference on Communications 2017 (ICC 2017), Paris, France, May, 2017. pp. 1-6. DOI: 10.1109/ICC.2017.7997452"
Faisal Hussain
M. Y. Hassan, F. Hussain, M. S. Hossen, S. Choudhury and M M Alam, "nterference Minimization in D2D Communication Underlaying Cellular Networks" IEEE Access, vol. 5, pp.22471-22484, 2017. DOI: 10.1109/ACCESS.2017.2763424
2016 (31)
Ashraful Alam Khan
Kushol, Rafsanjany, Md Sirajus Salekin, Md. Hasanul Kabir, and Ashraful Alam Khan. 2016. "Copy-Move Forgery Detection Using Color Space and Moment Invariants-Based Features". In International Conference on Digital Image Computing: Techniques And Applications (DICTA), 1-6. Gold Coast: IEEE.
Md. Hamjajul Ashmafee
S. A. Sabab and M. H. Ashmafee, "Blind Reader: An intelligent assistant for blind," 2016 19th International Conference on Computer and Information Technology (ICCIT), Dhaka, 2016, pp. 229-234, doi: 10.1109/ICCITECHN.2016.7860200.
Dr. Md. Hasanul Kabir
A. B. M. A. Rahman, G. Mostaeen, and M. H. Kabir, “A statistical approach for offline signature verification using local gradient features,” in 2nd International Conference on Electrical, Computer & Telecommunication Engineering (ICECTE), 2016, pp.1-4.
Dr. Rafsanjany Kushol
Kushol, Rafsanjany, Md Sirajus Salekin, Md Hasanul Kabir, and Ashraful Alam Khan. "Copy-move forgery detection using color space and moment invariants-based features." In 2016 International Conference on Digital Image Computing: Techniques and Applications (DICTA), pp. 1-6. IEEE, 2016.
Dr. Md. Hasanul Kabir
N. Sakib, Z. Ahmed, A. Farayez, and M. H. Kabir, “An approach to build simplified semi-autonomous Mars Rover,” in IEEE Region 10 Conference (TENCON), 2016, pp. 3502 - 3505.
Dr. Kamrul Hasan
Md Mamunur Rashid, Kazi Wasif Ahmed, Hasan Mahmud, Md. Kamrul Hasan and Husne Ara Rubaiyeat. Cohesion Based Personalized Community Recommendation System. International Journal of Advanced Computer Science and Applications (IJACSA), 7(8), 2016. http://dx.doi.org/10.14569/IJACSA.2016.070843
Dr. Hasan Mahmud
Md Mamunur Rashid, Kazi Wasif Ahmed, Hasan Mahmud, Md. Kamrul Hasan and Husne Ara Rubaiyeat, “Cohesion Based Personalized Community Recommendation System”, International Journal of Advanced Computer Science and Applications (IJACSA), 7(8), 2016. http://dx.doi.org/10.14569/IJACSA.2016.070843 [Web of Science, Scopus] [Q3: Computer Science]
Ahnaf Munir
Ahnaf Munir, Shihabuzzaman, Md. Sakhawat Hossen, Salimur Choudhury, Muhammad Mahbub Alam., and S. Choudhury “Localized motion planning algorithm for mobile wireless sensor networks”, International Journal of Unconventional Computing (2016), Vol. 12, pp. 363-391.
Dr. Md. Sakhawat Hossen
Munir, A., Uzzaman, S., Hossen, M.S., Choudhury, S., & Alam, M.M. (2016). Localized Motion Planning Algorithm for Mobile Wireless Sensor Networks. Int. J. Unconv. Comput., 12, 363-391.
Dr. Md. Sakhawat Hossen
Munir, A., Hossen, M.S., & Choudhury, S. (2016). Localized Load Balancing in RFID Systems. TPNC.
Dr. Md. Hasanul Kabir
R. Kushol, M. S. Salekin, M. H. Kabir, and A. A. Khan, “Copy-move forgery detection using color space and moment invariants-based features,” in International Conference on Digital Image Computing: Techniques and Applications (DICTA), 2016, pp. 1-6.
Ahnaf Munir
Ahnaf Munir, Md. Sakhawat Hossen and Salimur Choudhury, ”Localized Load Balancing in RFID Systems”, in 5th International Conference on the Theory and Practice of Natural Computing (TPNC) 2016, Sendai, Japan. doi: 10.1007/978-3-319-49001-4 3
Dr. Md. Hasanul Kabir
S. A. S. Sabab, S. R. H. Digonto, H. M. Mahmud, M. H. Kabir, and M. K. H. Hasan, “EYE POINTER: A Real Time Cost Effective Computer Controlling System Using Eye and Head Movement,” in International Conference on Advances in Computer-Human Interactions (ACHI), 2016, pp. 153–159.
Ashraful Alam Khan
Khan, Ashraful Alam, Mahmudun Nabi, Abdullah-Al-Tariq, and Muhammad Mahbub Alam. 2016. “RIFE-MAC: Fair and Efficient Medium Access Control for IEEE 802.11 Based Wireless Mesh Networks”. IUT Journal of Engineering and Technology (JET) 13 (1): 35–45.
Sadia Sharmin
Md Habibur Rahman, Sadia Sharmin, Sheikh Muhammad Sarwar, Mohammad Shoyaib . Software defect prediction using feature space transformation. In Proceedings of the International Conference on Internet of things and Cloud Computing, 2016
A.B.M. Ashikur Rahman
Rahman, A. A., Mostaeen, G., & Kabir, M. H. (2016, December). A statistical approach for offline signature verification using local gradient features. In 2016 2nd International Conference on Electrical, Computer & Telecommunication Engineering (ICECTE) (pp. 1-4). IEEE.
Dr. Md. Azam Hossain
M. A. Hossain, C. N. Nguyen, J.-S. Kim, and S. Hwang, “Exploiting resource profiling mechanism for large-scale scientific computing on grids”, Cluster Computing, vol. 19, pp. 1527–1539, 2016, issn: 1386- 7857, (SCIE).
2015 (21)
Dr. Md Moniruzzaman
M. Moniruzzaman, S. Jeeshan Kabeer, and M. Mahbub Alam, “An enhanced local texture pattern for effective face feature description,” Journal of Engineering and Technology, vol. 12, no. 2, pp. 29–38, 2015
Dr. Hasan Mahmud
Aboubakar Mountapmbeme, Hasan Mahmud and Md. Kamrul Hasan, "Hand Gesture Recognition using Depth Information and DTW", IUT Journal of Engineering and Technology (JET), vol. 12, no. 2, pp. 1-8, December 2015.
Dr. Md. Hasanul Kabir
M. S. Salekin, R. Kushol, and M. H. Kabir, “An Efficient Circular Block Approach for Copy-Move Forgery Detection,” Journal of Engineering and Technology, vol. 12, no. 2, pp. 9–20, 2015.
Shohel Ahmed
BARI, A.S.M. Hossain, Shohel AHMED,AHSAN, Shegufta Bakht, Sadre Ala PARVEZ,AZIZ, Syeda Persia, Md. Tawhidul Islam CHOWDHURY- "ELECTRONIC DEVICE AND METHOD FOR PROVIDING INFORMATION THEREOF” Publication number: 20150220247, Publication Date: Aug 06, 2015
Dr. Md. Hasanul Kabir
M. H. Kabir, F. Ahmed, and Abdullah-Al-Tariq, “An efficient method for extracting key-frames from 3D human joint locations for action recognition,” in International Conference Image Analysis and Recognition (ICIAR), 2015, pp. 277–284.
Ashraful Alam Khan
Khan, Ashraful Alam, K. Habibul Kabir, and Muhammad Mahbub Alam. 2015. “Connecting the Disconnected: A Combination of DTN, CDN and TCP/IP Approach”. IUT Journal of Engineering and Technology (JET) 12(2): 39–49.
Dr. Kamrul Hasan
Rahman, Z., & Hasan, M.K. (2015). Better user recommendations using enhancing software development process repository. 2015 18th International Conference on Computer and Information Technology (ICCIT), 70-75.
Dr. Kamrul Hasan
Md. Abid Hasan, Md. Kamrul Hasan, M. Abdul Mottalib.Linear regression-based feature selection for microarray data classification. International Journal of Data Mining and Bioinformatics (IJDMB), Vol. 11, No. 2, 2015
Sadia Sharmin
Sadia Sharmin, Md Rifat Arefin, M Abdullah-Al Wadud, Naushin Nower, Mohammad Shoyaib . SAL: An effective method for software defect prediction. In 2015 18th International Conference on Computer and Information Technology (ICCIT), , 2015
Dr. Md. Azam Hossain
Hossain Md Azam, Hieu Trong Vu, Jik-Soo Kim, Myungho Lee, and Soonwook Hwang. "Scout: a monitor and profiler of grid resources for large-scale scientific computing." In Cloud and Autonomic Computing (ICCAC), 2015 International Conference on, pp. 260-267. IEEE, 2015 (Scopus Indexed)
2014 (12)
Dr. Kamrul Hasan
Md. Nafiz Hamid, Md. Abu Naser, Md. Kamrul Hasan, Hasan Mahmud, "A cohesion-based friend-recommendation system", Social Network Analysis and Mining (SNAM), vol. 4, no. 1, pp. 1 27 February 2014, Springer-Verlag GmbH Austria, part of Springer Nature, https://doi.org/10.1007/s13278-014-0176-6
Dr. Kamrul Hasan
A.F.M. Nazmul Haque Nahin, Jawad Mohammad Alam, Hasan Mahmud, Md. Kamrul Hasan, "Identifying emotion by keystroke dynamics and", Journal of Behaviour and Information Technology (BIT), vol. 33, no. 9, p. 987-996, 3 July 2014. https://doi.org/10.1080/0144929X.2014.907343
Dr. Hasan Mahmud
Mefta Sadat, Rasam Bin Hossain, Hasan Mahmud, "Recognizing Human Affection: Smartphone Perspective," Global Journal of Computer Science and Technology (GJCST), vol. 14, no. 6, pp. 9-15, 2014. https://computerresearch.org/index.php/computer/article/view/140
Dr. Hasan Mahmud
A.F.M. Nazmul Haque Nahin, Jawad Mohammad Alam, Hasan Mahmud, Md. Kamrul Hasan, "Identifying emotion by keystroke dynamics and", Journal of Behaviour and Information Technology (BIT), vol. 33, no. 9, p. 987-996, 3 July 2014. https://doi.org/10.1080/0144929X.2014.907343 [SCI/SSCI Web of Science, IF 3.7] [Q1: Human-Computer Interaction in Computer Science, Arts and Humanities, Psychology, Social Sciences]
Dr. Muhammad Mahbub Alam
Akand, M.M., Nayeem, M.T., Sumon, M.R., & Alam, M.M. (2014). A Probabilistic Delay Model for Bidirectional VANETs in City Environments. ArXiv, abs/1411.2931.
Dr. Md. Hasanul Kabir
M. R. I. Hossain, I. Ahmed, and M. H. Kabir, “Automatic lung tumor detection based on GLCM features,” in Asian Conference on Computer Vision (ACCV) Workshop, 2015, pp. 109–121.
Abu Raihan Mostofa Kamal
A. R. M. Kamal, C. J. Bleakley, and S. Dobson, “Failure detection in wireless sensor networks: A sequence-based dynamic approach,” ACM Transactions on Sensor Networks (TOSN), vol. 10, no. 2, pp. 1–29, 2014.
Dr. Md. Hasanul Kabir
F. Bashar, A. Khan, F. Ahmed, and M. H. Kabir, “Robust facial expression recognition based on median ternary pattern (MTP),” in 2013 International Conference on Electrical Information and Communication Technology (EICT), 2014, pp. 1–5.
Dr. Hasan Mahmud
Md. Nafiz Hamid, Md. Abu Naser, Md. Kamrul Hasan, Hasan Mahmud, "A cohesion-based friend-recommendation system", Social Network Analysis and Mining (SNAM), vol. 4, no. 1, pp. 1 27 February 2014, Springer-Verlag GmbH Austria, part of Springer Nature, https://doi.org/10.1007/s13278-014-0176-6 [ESCI/Web of Science, Scopus] [IF 2.8] [Q1: Communication in Social Science, Human-Computer Interaction, Information Systems]
Dr. Md. Hasanul Kabir
F. Bashar, A. Khan, F. Ahmed, and M. H. Kabir, “Face recognition using similarity pattern of image directional edge response,” Adv. Electr. Comput. Eng., vol. 14, no. 1, pp. 69–76, 2014. (SCIE)
Dr. Md. Hasanul Kabir
F. Ahmed, M. H. Kabir, S. Bhuyan, H. Bari, and E. Hossain, “Automated Weed Classification with Local Pattern-Based Texture Descriptors,” Int. Arab J. Inf. Technol., vol. 11, no. 1, pp. 87–94, 2014. (SCIE)
2013 (6)
Abu Raihan Mostofa Kamal
A. R. M. Kamal and M. A. Hamid, “Reliable data approximation in wireless sensor network,” Ad hoc networks, vol. 11, no. 8, pp. 2470–2483, 2013.
Dr. Hasan Mahmud
Md. Nafiz Hamid, Md. Abu Naser, Md. Kamrul Hasan, Hasan Mahmud. A Cohesion Based Frind Recommendation System. In the Proceedings of 2nd Workshop on Information and Communication Technology,4th October 2013, pp. 1-8, organized by IUT Computer Society, IUT.
Dr. Md. Hasanul Kabir
A. Khan, F. Bashar, F. Ahmed, and M. H. Kabir, “Median ternary pattern (MTP) for face recognition,” in International Conference on Informatics, Electronics and Vision (ICIEV), 2013, pp. 1–5.
Dr. Hasan Mahmud
Fayaz Shahdib, Md. Wali Ullah Bhuiyan, Md. Kamrul Hasan, Hasan Mahmud, "Obstacle Detection and Object Size Measurement for Autonomous Mobile Robot using Sensor", International Journal of Computer Applications, vol. 66, no. 9, p. 0975-8887, 2013.
Abu Raihan Mostofa Kamal
A. R. M. Kamal, C. Bleakley, and S. Dobson, “Packet-level attestation (pla) a framework for in-network sensor data reliability,” ACM Transactions on Sensor Networks (TOSN), vol. 9, no. 2, pp. 1–28, 2013.
2012 (16)
Abu Raihan Mostofa Kamal
Abu Raihan M. Kamal, Chris J. Bleakley, Simon Dobson: Congestion mitigation using in-network sensor datasummarization. The 9th ACM International Symposium on Per- formance Evaluation of Wireless Ad Hoc, Sensor, and Ubiquitous Networks. PE-WASUN 2012:p-93-100. Paphos,Cyprus. October 24-25, 2012.
Dr. Hasan Mahmud
Moumie Soulemane, Mohammad Rafiuzzaman, Hasan Mahmud, "Crawling the Hidden Web: An Approach to," International Journal of Computer Applications, vol. 55, no. 1, pp. 7-15, October 2012.
Dr. Hasan Mahmud
Fayaz Shahdib, Md. Wali Ullah Bhuiyan, Md. Kamrul Hasan, Hasan Mahmud. Obstacle Detection and Object Size Measurement for Autonomous Mobile Robot Using Sensor Fusion. In the Proceedings of 1st Workshop on Information and Communication Technology, 21-22 June 2012, pp. 9-16, organized by IUT Computer Society, IUT.
Dr. Hasan Mahmud
S.M. Shahnewaz, Md. Kamrul Hasan, Hasan Mahmud. A Scenario Based API Recommendation System Using Syntax and Semantics of Client Source Code. In the Proceedings of 1st Workshop on Information and Communication Technology, 21-22 June 2012, pp. 17-30, organized by IUT Computer Society, IUT.
Dr. Muhammad Mahbub Alam
Rahman, M.A., Islam, M.N., & Alam, M. (2012). Numerical Solutions of Volterra Integral Equations Using Laguerre Polynomials. Journal of Scientific Research, 4, 357.
Dr. Md. Hasanul Kabir
F. Ahmed and M. H. Kabir, “Facial feature representation with directional ternary pattern (DTP): Application to gender classification,” in IEEE 13th International Conference on Information Reuse & Integration (IRI), 2012, pp. 159–164.
Dr. Md. Hasanul Kabir
F. Ahmed and M. H. Kabir, “Directional ternary pattern ( DTP) for facial expression recognition,” in IEEE International Conference on Consumer Electronics (ICCE), 2012, pp. 265–266.
Dr. Md. Hasanul Kabir
S. J. Kabeer, M. M. Tanvee, A. Rahman, M. A. Mottalib, and M. H. Kabir, “BFSSGA: Enhancing the performance of genetic algorithm using boosted filtering approach,” Int. J. Comput. Appl., vol. 51, no. 19, pp. 29–34, 2012.
Dr. Hasan Mahmud
Md. Sami Uddin, Jahidul Islam Khan, Hasan Mahmud, "Designing and Implementing Tele-rehabilitation on Hand Skill Development for the Disabled People in Bangladesh," International Journal of Software Engineering (IJSE), vol. 5, no. 2, pp. 37-49, 2012
Dr. Md. Hasanul Kabir
M. H. Kabir and F. Ahmed, “Face recognition with directional ternary pattern (DTP),” in International Conference on Graphic and Image Processing (ICGIP), 2012, pp. 7E1-7E5.
Dr. Md. Hasanul Kabir
M. H. Kabir, T. Jabid, and O. Chae, “Local Directional Pattern Variance (LDPv): A Robust Feature Descriptor for Facial Expression Recognition,” Int. Arab J. Inf. Technol., vol. 9, no. 4, pp. 382–391, 2012. (SCIE)
Dr. Md. Azam Hossain
M. R. Karim, M. A. Hossain, M. M. Rashid, B.-S. Jeong, and H.-J. Choi1, “A mapreduce framework for mining maximal contiguous frequent patterns in large dna sequence datasets”, IETE Technical Review, vol. 29, no. 2, pp. 162–168, 2012, issn: 0974-5971, (SCIE).
2011 (14)
Dr. Hasan Mahmud
S.M. Shahnewaz, Md. Asikur Rahman, Hasan Mahmud, "A Self Acting Initial Seed Selection Algorithm for K-means Clustering Based on Convex-Hull". In: Abd Manaf A., Zeki A., Zamani M., Chuprat S., El-Qawasmeh E. (eds) Informatics Engineering and Information Science. ICIEIS 2011. Communications in Computer and Information Science, vol 252. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-642-25453-6_54
Dr. Md. Hasanul Kabir
Y. G. Lee, Y. K. Yoon, O. Chae, and M. H. Kabir, “Method And Apparatus For Motion Compensation,” US Patent 8036525, Oct-2011.
Dr. Hasan Mahmud
Hasan Mahmud, Moumie Soulemane and Mohammad Rafiuzzaman, "A framework for dynamic indexing from hidden web", International Journal of Computer Science Issues, vol. 8, no. 5, pp. 249-258, 2011.
Dr. Muhammad Mahbub Alam
Islam, M.S., Alam, M.M., Hong, C., & Lee, S. (2011). eMCCA: An enhanced mesh coordinated channel access mechanism for IEEE 802.11s wireless mesh networks. Journal of Communications and Networks, 13, 639-654.
Dr. Muhammad Mahbub Alam
Hamid, M.A., Abdullah-Al-Wadud, M., & Alam, M.M. (2011). A reliable structural health monitoring protocol using wireless sensor networks. 14th International Conference on Computer and Information Technology (ICCIT 2011), 601-606.
Dr. Muhammad Mahbub Alam
Rahman, M.O., Alam, M.M., Monowar, M., Hong, C., & Lee, S. (2011). nW-MAC: multiple wake-up provisioning in asynchronously scheduled duty cycle MAC protocol for wireless sensor networks. annals of telecommunications - annales des télécommunications, 66, 567-582.
Dr. Muhammad Mahbub Alam
Alam, M.M., Islam, M.S., Hamid, M.A., Hong, C., & Lee, S. (2011). Congestion-aware fair rate control in wireless mesh networks. annals of telecommunications - annales des télécommunications, 66, 275-291.
Dr. Md. Hasanul Kabir
M. Murshed, M. H. Kabir, and O. Chae, “Moving object tracking–an edge segment based approach,” International Journal of Innovative Computing, Information and Control, vol. 7, no. 7, pp. 3963–3979, 2011. (ESCI)
Dr. Md. Sakhawat Hossen
Faisal, A., Emam, H., A.S.M., H., & Hossen, S. (2011). Compound Local Binary Pattern (CLBP) for Rotation Invariant Texture Classification. International Journal of Computer Applications, 33, 5-10.
Dr. Md. Hasanul Kabir
T. Jabid, M. H. Kabir, and O. Chae, “Local Directional Pattern (LDP) for Face Recognition,” International Journal of Innovative Computing, Information and Control, vol. 8, no. 4, pp. 2423–2437, 2011. (ESCI)
Dr. Md. Azam Hossain
Md. Rezaul Karim, Md. Mamunur Rashid, Hossain Md. Azam and Byeong-Soo Jeong, "A Parallel and Distributed Programming Model for Mining Correlated, Associated, Associated-Correlated and Independent Patterns from Large Transactional Databases Using MapReduce on Hadoop¡±, Proc.The 6th International Conference on Ubiquitous Information Technologies and Applications , Seoul, South Korea, Dec, 15-17, 2011
2010 (23)
Abu Raihan Mostofa Kamal
Abu Raihan M. Kamal, Mohammad Abdur Razzaque, Paddy Nixon: 2PDA: two-phase data approximation in wireless sensor network. The 8th ACM International Symposium on Performance Evaluati n of Wireless Ad Hoc, Sensor, and Ubiquitous Networks. PE- WASUN 2010:p-1-8. Bodrum, Turkey. October 17-21, 2010.
Dr. Hasan Mahmud
Hasan Mahmud, S. M. Didar-Al-Alam, Md. Sarwar Morshed, Md. Obaidul Haque and Md. Kamrul Hasan, "Designing access control model and enforcing security policies using PERMIS for a smart item e-health scenario," International Journal of Engineering Science and Technology, vol. 2, no. 8, pp. 3777-3787, 2010.
Dr. Hasan Mahmud
Md. Sarwar Morshed, Hasan Mahmud and S. M. Didar-Al-Alam, "Evaluation of nonlinearity effects on performance of DVB-H transmission link," International Journal of Engineering Science and Technology, vol. 2, no. 8, pp. 3854-3864 , 2010.
Dr. Md. Sakhawat Hossen
Hossen, M.S., Kabir, A., Khan, R.H., & Azfar, A. (2010). Interconnection between 802.15.4 Devices and IPv6: Implications and Existing Approaches. ArXiv, abs/1002.1146.
Dr. Md. Hasanul Kabir
T. Jabid, M. H. Kabir, and O. Chae, “Robust facial expression recognition based on local directional pattern,” ETRI J., vol. 32, no. 5, pp. 784–794, 2010. (SCI)
Dr. Muhammad Mahbub Alam
Monowar, M., Alam, M.M., Rahman, M.O., Hong, C., & Lee, S. (2010). A load-aware energy-efficient and throughput-maximized asynchronous duty cycle MAC for wireless sensor networks. annals of telecommunications - annales des télécommunications, 65, 777-794.
Dr. Muhammad Mahbub Alam
Islam, S., Alam, M.M., & Hong, C. (2010). An efficient multi-channel communications scheme for wireless sensor network.
Dr. Muhammad Mahbub Alam
Islam, M.S., Alam, M.M., Hong, C., & Lee, S. (2010). Load-Adaptive Practical Multi-Channel Communications in Wireless Sensor Networks. Sensors (Basel, Switzerland), 10, 8761 - 8781.
Dr. Muhammad Mahbub Alam
Monowar, M., Alam, M.M., Rahman, M.O., & Hong, C. (2010). LER-MAC: A Load-independent Energy-efficient and Rate-control Integrated Asynchronous Duty Cycle MAC for Wireless Sensor Networks. 2010 IEEE International Symposium on "A World of Wireless, Mobile and Multimedia Networks" (WoWMoM), 1-9.
Dr. Muhammad Mahbub Alam
Alam, M.M., Hamid, M.A., Razzaque, M.A., & Hong, C. (2010). Fair Scheduling and Throughput Maximization for IEEE 802.16 Mesh Mode Broadband Wireless Access Networks. IEICE Trans. Commun., 93-B, 1459-1474.
Dr. Muhammad Mahbub Alam
Islam, M.S., Alam, M.M., Hamid, M.A., Hong, C., & Lee, S. (2010). EFT: a high throughput routing metric for IEEE 802.11s wireless mesh networks. annals of telecommunications - annales des télécommunications, 65, 247-262.
Dr. Muhammad Mahbub Alam
Hamid, M.A., Alam, M.M., Islam, M.S., & Hong, C. (2010). Enforcing Fairness for Data Collection in Wireless Sensor Networks. 2010 8th Annual Communication Networks and Services Research Conference, 192-198.
Dr. Muhammad Mahbub Alam
Islam, M.S., Alam, M.M., Hong, C., & Sung, J. (2010). Enhanced Channel Access Mechanism for IEEE 802.11s Mesh Deterministic Access. 2010 IEEE Wireless Communication and Networking Conference, 1-6.
Dr. Muhammad Mahbub Alam
Islam, M.S., Alam, M.M., Hamid, M.A., & Hong, C. (2010). High throughput path selection for IEEE 802.11s based wireless mesh networks. ICUIMC '10.
Dr. Md. Hasanul Kabir
T. Jabid, M. H. Kabir, and O. Chae, “Facial expression recognition using Local Directional Pattern (LDP),” in IEEE International Conference on Image Processing (ICIP), 2010, pp. 1605–1608.
Dr. Md. Hasanul Kabir
T. Jabid, M. H. Kabir, and O. Chae, “Local directional pattern (LDP) – A robust image descriptor for object recognition,” in IEEE International Conference on Advanced Video and Signal Based Surveillance (AVSS), 2010, pp. 482–487.
Dr. Md. Hasanul Kabir
M. H. Kabir, T. Jabid, and O. Chae, “A local directional pattern variance (LDPv) based face descriptor for human facial expression recognition,” in IEEE International Conference on Advanced Video and Signal Based Surveillance (AVSS), 2010, pp. 526–532.
Dr. Md. Hasanul Kabir
T. Jabid, M. H. Kabir, and O. Chae, “Gender classification using local directional pattern (LDP),” in 20th International Conference on Pattern Recognition (ICPR), 2010, pp. 2162–2165.
Dr. Md. Hasanul Kabir
T. Jabid, M. H. Kabir, and O. Chae, “Local Directional Pattern (LDP) for face recognition,” in International Conference on Consumer Electronics (ICCE), 2010, pp. 329–330.
Dr. Md. Hasanul Kabir
M. H. Kabir, A. Al-Wadud, and O. Chae, “Brightness Preserving Image Contrast Enhancement Using Weighted Mixture of Global and Local Transformation Functions,” Int. Arab J. Inf. Technol., vol. 7, no. 4, pp. 403–410, 2010. (SCIE)
Dr. Hasan Mahmud
S. M. Didar-Al-Alam, Hasan Mahmud and Md. Abdul Mottalib, "Modifications in Proximity Based Access Control for Multiple User Support," International Journal of Engineering Science and Technology, vol. 2, no. 8, pp. 3603-3613, 2010.
Dr. Md. Hasanul Kabir
Y.-G. Lee, Y.-K. Yoon, O.-S. Chae, and M. H. Kabir, “Method and apparatus for motion compensation,” EP Patent 20100156903, 2010.
Dr. Kamrul Hasan
Md Kamrul Hasan, Mohammad Kaykobad, Young-Koo Lee, Sungyoung Lee. A comprehensive Analysis of Degree Based Condition for Hamiltonian Cycles, Theoretical Computer Science 411(1):285-287 DOI: 10.1016/j.tcs.2009.09.018
2009 (4)
Dr. Kamrul Hasan
Md Kamrul Hasan, Anh Pham Ngoc, Young-Koo Lee, Sungyoung Lee. Preference Learning on an OSGi Based Home Gateway. IEEE Transactions on Consumer Electronics 55(3):1322 - 1329 DOI: 10.1109/TCE.2009.5277995
Dr. Kamrul Hasan
Md Kamrul Hasan, Lenin Mehedy, Salim Zabir,Sungyoung Lee, Young-Koo Lee. A Middleware Based Network Hot Swapping Solution for SCA Compliant Radio. IEEE Transactions on Consumer Electronics 55(3):1315 - 1321, DOI: 10.1109/TCE.2009.5277994
Abu Raihan Mostofa Kamal
Abu Raihan Mostofa Kamal, M. Aminul Islam, Md. Khaled-Ur-Rahman and Md. Zubairul Islam.Performance Enhancement in Media Access Control (MAC) layer protocol on Wireless Sensor Network. IUT Journal of Engineering and Technology, 2009, Vol. 7, No. 2, Pages 23-36.
Dr. Muhammad Mahbub Alam
Hamid, M.A., Alam, M.M., Islam, M.S., Hong, C., & Lee, S. (2010). Fair data collection in wireless sensor networks: analysis and protocol. annals of telecommunications - annales des télécommunications, 65, 433-446.
2008 (5)
Abu Raihan Mostofa Kamal
Rasib Hassan Khan , K. M. Imtiaz-ud-Din , Abdullah Ali Faruq , Abu Raihan Mostofa Kamal, M. Abdul Mottalib. Security Adaptive Protocol Suite: Ranked Neighbor Dis- covery (RND) and Security Adaptive AODV(SA-AODV). 5th International Conference on Electrical and Computer Engineering (ICECE 2008), BUET, Bangladesh. December 22-24, 2008.
Abu Raihan Mostofa Kamal
A.K.M. Rasheduzzaman, M. Asikur Rahman, Daud M Jamilur Rahman and Abu Raihan Mostofa Kamal. Density-based Clustering Technique for efficient Data Mining. 11th International Conference on Computer and Information Technology (ICCIT 2008). KUET, Bangladesh. December 25-27, 2008.
Abu Raihan Mostofa Kamal
Md.Shariful Islam, Abu Raihan Mostofa Kamal, Mahfuz Hasan and Dr.Hafiz Md. Hasan Babu, An approach towards efficient Key Management in Mobile Ad Hoc Network, Dhaka University Journal of Science (ISSN 1022-2502), July 2008. Vol.56, No. 2, Pages 129-132 .
Dr. Md. Sakhawat Hossen
R. H. Khan, A. Ahsan, M. Haque, A. F. M. S. Kabir and S. Hossen, "MC-CDMA: An Alternative Multiple Access Technique in 3G Wireless Architecture," 2008 International Conference on Complex, Intelligent and Software Intensive Systems, Barcelona, Spain, 2008, pp. 573-578, doi: 10.1109/CISIS.2008.88.
Abu Raihan Mostofa Kamal
Abu Raihan Mostofa Kamal, Lutful Karim, Hafiz Md. Hasan Babu and Md. Shariful Islam, An Adaptive Secure Routing in Mobile Ad Hoc Networks, Dhaka University Journal of Science (ISSN 1022-2502), January 2008. Vol.56, No. 1, Pages 9-15 .
2007 (2)
Dr. Kamrul Hasan
Lenin Mehedy, Md Kamrul Hasan, Mohammad Kaykobad. An improved degree based condition for Hamiltonian cycles. Information Processing Letters 102(2):108-112 DOI: 10.1016/j.ipl.2006.11.013
Dr. Md. Hasanul Kabir
M. A.-A. Wadud, M. H. Kabir, M. A. A. Dewan and O. Chae, “A Dynamic Histogram Equalization for Image Contrast Enhancement”, IEEE Transactions on Consumer Electronics, Vol. 53, No. 2, pp. 593–600, 2007. [SCI]
2006 (1)
Abu Raihan Mostofa Kamal
Abu Raihan Mostofa Kamal, Lutful Karim, Hafiz Md. Hasan Babu and Md. Shariful Islam. Enhanced Security of AODV Protocol in Mobile Ad Hoc Networks. First Inter- national Conference on Next-Generation Wireless Systems 2006 (ICNEWS2006). IEEE Communication Society. Dhaka, Bangladesh. January 2-4, 2006.
2005 (1)
Abu Raihan Mostofa Kamal
Md. Sarwar Morshed, Abu Raihan Mostofa Kamal, Abu Saleh Muhammad Barkat Ullah. Susceptible SQL Detector (SSD) – a Parser-based Security Solution to Prevent SQL-Injection Attack. The 8th International Conference on Computer and Information Technology (ICCIT 2006). Dhaka, Bangladesh. December 28-30, 2005.
Undated
Shohel Ahmed
Ahmed Shohel, Sungjoon Park, Jason J. Jung, Sanggil Kang, “A Personalized URL Re-ranking Method using Psychological User Browsing Characteristics”- Journal of Universal Computer Science, vol. 15, no. 4 (2009), 926-940.
Shohel Ahmed
Nuraini Jamil, Ahmed Shohel, Kangseok Kim, and Sanggil Kang, “Adaptive Scene Classification based on Semantic Concepts and Edge Detection”- Journal of Intelligence and Information Systems, vol.15, no. 2 (2009), pp.1-13.
Shohel Ahmed
Ahmed Shohel, Pyungkwan Ko, Ju-wan Kim, Young-Kuk Kim, Sanggil Kang, “An Enhanced Recommendation Technique for Personalized E-Commerce Portal” in Second International Symposium on Intelligent Information Technology Application (IITA 2008), pp . 196-200.
Tajkia Rahman Toma
Mohayeminul Islam, Tajkia Rahman Toma, Md. Selim, Alim Ul Gias and Shah Mostafa Khaled. "Design Migration from Procedural to Object Oriented Paradigm by Clustering Data Call Graph". International Journal of Information Engineering and Electronic Business (IJIEEB). 13 pages, 2016.
Tajkia Rahman Toma
Tajkia R. Toma, Mohayeminul Islam, Mohammad Shoyaib and Md. Shariful Islam. "A Dependency Graph Generation Process for Client-side Web Applications". International Journal of Information Engineering and Electronic Business (IJIEEB). 13 pages, 2015.
Tajkia Rahman Toma
Tajkia Rahman Toma and Md. Shariful Islam. "An Efficient Mechanism of Generating Call Graph for JavaScript using Dynamic Analysis in Web Application". International Conference on Informatics, Electronics & Vision (ICIEV). 6 pages, 2014.
Tajkia Rahman Toma
Md. Selim, Md. Saeed Siddik, Tajkia Rahman, Alim Ul Gias and Shah Mostafa Khaled. "Approximating Object based Architecture for Legacy Software Written in Procedural Languages using Variable Neighborhood Search". International Conference on Software, Knowledge, Intelligent Management and Applications (SKIMA). 8 pages, 2014.
Dr. Md Moniruzzaman
M. Moniruzzaman, A. Bagirov, and I. Gondal, “Partial undersampling of imbalanced data for cyber threats detection,” in Proceedings of the Australasian Computer Science Week Multiconference, ACSW ’20, (New York, NY, USA), Association for Computing Machinery, 2020
Dr. Md Moniruzzaman
M. Moniruzzaman, A. Bagirov, I. Gondal, and S. Brown, “A server side solution for detecting webinject: A machine learning approach,” in Trends and Applications in Knowledge Discovery and Data Mining (M. Ganji, L. Rashidi, B. C. M. Fung, and C. Wang, eds.), (Cham), pp. 162–167, Springer International Publishing, 2018
Md. Hamjajul Ashmafee
M. H. Ashmafee, T. Ahmed, S. Ahmed, B. Hasan, N. Jahan, and A. Rahman, “An Efficient Transfer Learning-based Approach for Apple Leaf Disease Classification,” 3rd International Conference on Electrical, Computer and Communication Engineering (ECCE 2023), Dhaka, 2023.
Md. Hamjajul Ashmafee
R. Rahman, A. A. Farhad, R. Hasan, M. T. Lashkar, M. H. Ashmafee, and A. R. M. Kamal, “ChartSumm: A Large Benchmark for Automatic Chart Summarization,” 36th Canadian Conference on Artificial Intelligence (CANAI 2023), 2023.
Md. Hamjajul Ashmafee
M. K. A. H. Sumon, M. H. Ashmafee, M. R. Islam, and A. R. Mostofa Kamal “Explainable NLQ-based Visual Interactive System: Challenges and Objectives,” 2nd International Conference on Computing Advancement (ICCA), 2022
Md. Hamjajul Ashmafee
R. Jany, M. H. Ashmafee, I. Hussain, and M. A. Hossain, “SleepExplain: Explainable Non-Rapid Eye Movement and Rapid Eye Movement Sleep Stage Classification from EEG Signal,” presented at the 25th International Conference on Computer and Information Technology (ICCIT), Cox’s Bazar, 2022
Md. Hamjajul Ashmafee
M. R. Islam, J. Zhang, M. H. Ashmafee, I. Razzak, J. Zhou, X. Wang, and G. Xu, “ExVis: Explainable Visual Decision Support System for Risk Management,” BESC 2021: The 8th International Conference on Behavioural and Social Computing, 2021
Md. Hamjajul Ashmafee
ABM Rahman, M Hasan, S Ahmed, M. H. Ashmafee, MR Kabir, H Kabir, “Two Decades of Bengali Handwritten Digit Recognition: A Survey,” IEEE A
"""  

# Initialize a list to hold the data  
data = []  

# Regex to match authors and titles  
pattern = r'(?P<authors>.+?)\. \d{4}\. (?P<title>.+?)(?:\.|$)'  

# Extract authors and titles  
matches = re.finditer(pattern, text, re.DOTALL)  
for match in matches:  
    authors = match.group("authors").strip()  
    title = match.group("title").strip()  
    # Format authors with quotes  
    authors_quoted = f'"{authors}"'  
    data.append([authors_quoted, title])  

# Write to CSV  
with open('iut_authors.csv', mode='w', newline='', encoding='utf-8') as file:  
    writer = csv.writer(file)  
    writer.writerow(['Authors', 'Title'])  # Write header  
    writer.writerows(data)  # Write data rows  

print("CSV file created successfully.")