import re
import csv

# Input text containing research titles and authors
input_text = """
Sarwar, H., Hossain, S., Rahman, M., Ahmed, S., Akter, N., & Rahman, C. M. (2013). Selection of an optimal set of features for bengali character recognition. In Technical Challenges and Design Issues in Bangla Language Processing (pp. 96–116). IGI Global. https://doi.org/10.4018/978-1-4666-3970-6.ch005

Rahman, C. M., & Numao, M. (1996). Top-down induction of recursive programs from small number of sparse examples. In L. De Raedt (Ed.), Advances in Inductive Logic Programming: Vol. 32 of Fron. IOS Press.

Nasreen, Hossain, S., Sarwar, H., & Rahman, C. M. (2010). Development of a recognizer for Bangla text: Present status and future challenges. In M. Mori & J. Trdine (Eds.), Character Recognition (pp. 83–112). InTechOpen. https://doi.org/10.5772/9780

Farid, D. M., Rahman, M. Z., & Rahman, C. M. (2012). Mining complex network data for adaptive intrusion detection. In A. Karahoca (Ed.), Data Mining. InTech.

Hassan, M. A., Khan, R. R., Kabir, M. F., & Rahman, C. M. (2009). Finding the appropriate meaning of polysemous words using context dependency. In P. Garg & J. Ranjan (Eds.), Advances in Computer Science and Engineering (pp. 251–260). Macmillan.

Paul, S. K., Bouakaz, S., Rahman, C. M., & Uddin, M. S. (2021). Component-based face recognition using statistical pattern matching analysis. Pattern Analysis and Applications, 24(1), 299–319. https://doi.org/10.1007/s10044-020-00895-4

Mahdy, M. R. C., Rivy, H. M., Jony, Z. R., Alam, N. B., Masud, N., Quaderi, G. D. A., Moosa, I. M., Rahman, C. M., & Sohel Rahman, M. (2020). Dielectric or plasmonic Mie object at air-liquid interface: The transferred and the traveling momenta of photon. Chinese Physics B, 29(1). https://doi.org/10.1088/1674-1056/ab5efa

Farid, D. M., Zhang, L., Rahman, C. M., Hossain, M. A., & Strachan, R. (2014). Hybrid decision tree and naïve Bayes classifiers for multi-class classification tasks. Expert Systems with Applications, 41(4 PART 2), 1937–1946. https://doi.org/10.1016/j.eswa.2013.08.089

Farid, D. M., Zhang, L., Hossain, A., Rahman, C. M., Strachan, R., Sexton, G., & Dahal, K. (2013). An adaptive ensemble classifier for mining concept drifting data streams. Expert Systems with Applications, 40(15), 5895–5906. https://doi.org/10.1016/j.eswa.2013.05.001

Farid, D. M., & Rahman, C. M. (2013). Mining complex data streams: Discretization, attribute selection and classification. Journal of Advances in Information Technology, 4(3), 129–135. https://doi.org/10.4304/jait.4.3.129-135

Biswas, A., Farid, D. M., & Rahman, C. M. (2012). A new decision tree learning approach for novel class detection in concept drifting data stream classification. Journal of Computer Science and Engineering, 14(1).

Huda, M. N., Hasan, M. M., Hassan, F., Kotwal, M. R. A., Muhammad, G., & Rahman, C. M. (2011). Articulatory feature extraction for speech recognition using neural network. International Review on Computers and Software, 6(1), 25–31.

Afza, A. J. M. A., Farid, D. M., & Rahman, C. M. (2011). A hybrid classifier using boosting, clustering, and naïve bayesian classifier. World of Computer Science and Information Technology Journal (WCSIT), 1(3), 105–109.

Farid, D. M., Harbi, N., Bahri, E., Rahman, M. Z., & Rahman, C. M. (2010). Attacks classification in adaptive intrusion detection using decision tree. World Academy of Science, Engineering and Technology, 63, 86–90. 

Farid, D. M., Harbi, N., Ahmmed, S., Rahman, M. Z., & Rahman, C. M. (2010). Mining network data for intrusion detection through Naïve Bayesian with clustering. World Academy of Science, Engineering and Technology, 66, 341–345. 

Osman Gani, M. D., Sarwar, H., & Rahman, C. M. (2009). Prediction of state of wireless network using Markov and hidden Markov model. Journal of Networks, 4(10), 976–984. https://doi.org/10.4304/jnw.4.10.976-984

Islam, M. M., Khondoker, M. R. H., & Rahman, C. M. (2001). Application of artificial intelligence techniques in automatic hull form generation. Ocean Engineering, 28(12), 1531–1544. https://doi.org/10.1016/S0029-8018(01)00020-8

Rahman, C. M., & Masud, M. M. (2001). Extending the knowledge intensive Genetic Algorithm based supervised concept learner to adopt continuous attributes. Journal of Electrical Engineering, EE29 (1).

Rahman, C. M., & Numao, M. (2001). Automated bias shift in a constrained space for logic program synthesis. Transaction of the Japanese Society for Artificial Intelligence, 16(6), 548–556. https://doi.org/10.1527/tjsai.16.548

Wasif, A., & Rahman, C. M. (2000). Application of dynamic programming principle in decision tree construction. Computer Science and Informatics Journal, 30(2).

Rahman, C. M., Kavi, A. Al, & Alam, A. M. S. (2000). Logic program synthesis from input/output examples using Genetic Inductive logic Programmimg. Journal of Electrical Engineering, EE28 (2).

Rahman, C. M., & Morshed, M. (2000). Decision tree based learning of handwritten Bangla characters. Journal of Electrical Engineering, EE28 (2).

Rahman, C. M., & Kabir, H. (2000). A new design methodology for getting normalized relations in relational databases. Bangladesh Journal of Computer and Information Technology, 7.

Rahman, C. M., & Rasul, G. (1999). Genetic algorithm based model for Bengali character recognition. Computer Science and Informatics Journal, 29(2).

Rahman, C. M., & Wasif, A. (1999). Construction of classification trees by the criterion of attribute dependency. Journal of Electrical Engineering, EE27 (2).

Rahman, C. M., & Masraq, R. (1999). Combination of cell multiplexing algorithms in ATM networks: An approach with Genetic Algorithm. Journal of Electrical Engineers, EE27 (2).

Rahman, C. M., & Kaykobad, M. (1999). Performance analysis of Hashing techniques. BUET Studies, 2(2).

C. M. Rahman, M. E. Sobhani, A. T. Rodela and S. Shatabda, "An Enhanced Text Compression Approach Using Transformer-based  

       Language Models," 2024  IEEE Region 10 Symposium (TENSYMP), Delhi, India, 2024.

       Niful Islam, Debopom Sutradhar, Swakkhar Shatabda & Chowdhury Mofizur Rahman (2023). Cotton Percentage Prediction  

       from Fabric Images Using Transfer Learning. In 26th International Conference on Computer and Information Technology

       (ICCIT), 2023. Appears in IEEE Xplore. DOI: 10.1109/ICCIT60459.2023

Siddiqi, F. A., & Rahman, C. M. (2020). Evolutionary multi-objective whale optimization algorithm. In A. Abraham, A. K. Cherukuri, P. Melin, & N. Gandhi (Eds.), International Conference on Intelligent Systems Design and Applications (Vol. 941, pp. 431–446). Springer. https://doi.org/10.1007/978-3-030-16660-1_43

Islam, F., Hoq, M. N., & Rahman, C. M. (2019). Application of transfer learning to detect potato disease from leaf image. IEEE International Conference on Robotics, Automation, Artificial-Intelligence and Internet-of-Things (RAAICON), 127–130. https://doi.org/10.1109/RAAICON48939.2019.53

Saha, D., Haque, M., Sarkar, A., Alam, F., Farid, D. M., Rahman, C. M., & Shatabda, S. (2018). Novel class detection in concept drifting data streams using decision tree leaves. IEEE International WIE Conference on Electrical and Computer Engineering (WIECON-ECE), 87–90. https://doi.org/10.1109/WIECON-ECE.2018.8782911

Rahman, C. M., Afroze, L., Refath, N. S., & Shawon, N. (2018). Iterative Feature Selection Using Information Gain Naïve Bayes for Document Classification. 21st International Conference of Computer and Information Technology (ICCIT). https://doi.org/10.1109/ICCITECHN.2018.8631971

Niloy, A. R., Taniza, F. A., Ali, M., Mashud, M. A. A., Shatabda, S., & Rahman, C. M. (2017). Guiding artificial neural networks using discriminatory information in hidden layers. IEEE International WIE Conference on Electrical and Computer Engineering (WIECON-ECE), 6–9. https://doi.org/10.1109/WIECON-ECE.2017.8468907

Rayhan, F., Ahmed, S., Mahbub, A., Jani, M. R., Shatabda, S., Farid, D. M., & Rahman, C. M. (2017). MEBoost: Mixing estimators with boosting for imbalanced data classification. 11th International Conference on Software, Knowledge, Information Management and Applications (SKIMA). https://doi.org/10.1109/SKIMA.2017.8294128

Islam, M. J., Khan, R. R., Kabir, M. F., & Rahman, C. M. (2013). A heuristic approach to resolve ambiguity of homonymous and polysemous words using context dependency. 7th International Conference on Software, Knowledge, Information Management, and Applications (SKIMA).

Naurin, N., Sabbir, R., Sahabuddin, M., & Rahman, C. M. (2013, December 18). Boosting up the performance of Naïve Bayesian classifier: Using the relevant discriminating attributes. 7th International Conference on Software, Knowledge, Information Management and Applications (SKIMA).

Farid, D. M., Siddiqui, S. A., & Rahman, C. M. (2013, December 18). Scaling up the classification accuracy of decision tree classifier for multi-class classification tasks. 7th International Conference on Software, Knowledge, Information Management and Applications (SKIMA).

Farid, D. M., Maruf, G. M., & Rahman, C. M. (2013). A new approach of Boosting using decision tree classifier for classifying noisy data. International Conference on Informatics, Electronics and Vision (ICIEV), 1–4. https://doi.org/10.1109/ICIEV.2013.6572718

Farid, D. M., & Rahman, C. M. (2012). Novel class detection in concept-drifting data stream mining employing decision tree. 7th International Conference on Electrical and Computer Engineering, 630–633. https://doi.org/10.1109/ICECE.2012.6471629

Kotwal, M. R. A., Hassan, F., Banik, M., Huda, M. N., & Rahman, C. M. (2011, February). Effects of acceleration co-efficient (ΔΔ) on neural network based Bangla speech recognition. 2nd International Conference on Computer Processing of Bangla (ICCPB).

Mridha, M. F., Hossain, M. Z., Banik, M., Huda, M. N., Rahman, C. M., & Das, J. K. (2010). Development of grammatical attributes for Bangla root and primary suffix for universal networking language. In O. Tonmukayakul, M. Songkroh, & P. Sureephong (Eds.), 4th International Conference on Software, Knowledge, Information Management and Applications: Towards Happiness and Sustainable Development, SKIMA 2010 (pp. 61–65). SKIMA.

Huda, M. N., Muhammad, G., Hasan, M. M., Kotwal, M. R. A., Hassan, F., Islam, G. M. M., Hossain, M. S., & Rahman, C. M. (2010). Which one is dominant for neural network based speech recognition - Δ or ΔΔ articulatory parameters? International Conference on Intelligent Computing and Cognitive Informatics (ICICCI), 66–70. https://doi.org/10.1109/ICICCI.2010.38

Mridha, M. F., Banik, M., Nawab Yousuf Ali, M., Huda, M. N., Rahman, C. M., & Das, J. K. (2010). Formation of Bangla word dictionary compatible with UNL structure. In O. Tonmukayakul, M. Songkroh, & P. Sureephong (Eds.), 4th International Conference on Software, Knowledge, Information Management and Applications: Towards Happiness and Sustainable Development, SKIMA 2010 (pp. 49–54). SKIMA.

Mridha, M. F., Nawab Yousuf Ali, M., Banik, M., Huda, M. N., Rahman, C. M., & Das, J. K. (2010). Conversion of Bangla sentence to universal networking language (T. O., S. M., & S. P. (eds.); pp. 55–60). SKIMA. https://www.scopus.com/inward/record.uri?eid=2-s2.0-84904994615&partnerID=40&md5=d763399611a7195aeee0ece15e6bcfbc

Kotwal, M. R. A., Hossain, M. S., Hassan, F., Muhammad, G., Huda, M. N., & Rahman, C. M. (2010). Bangla phoneme recognition using hybrid features. International Conference on Electrical & Computer Engineering (ICECE ), 718–721. https://doi.org/10.1109/ICELCE.2010.5700793

Mridha, M. F., Huda, M. N., Rahman, C. M., & Das, J. K. (2010). Development of morphological rules for Bangla root, verbal suffix and primary suffix for universal networking language. International Conference on Electrical & Computer Engineering (ICECE 2010), 570–573. https://doi.org/10.1109/ICELCE.2010.5700756

Hossain, M. S., Kotwal, M. R. A., Hassan, F., Hasan, M. M., Banik, M., Huda, M. N., & Rahman, C. M. (2010, August 10). Preparation of Bangla speech corpus for phoneme recognition. International Conference on Software, Knowledge, Information Management and Applications (SKIMA).

Farid, D. M., Harbi, N., Bahri, E., Rahman, M. Z., & Rahman, C. M. (2010, March 29). Attacks classification in adaptive intrusion detection using decision tree. International Conference on Computer Science (ICCS 2010).

Farid, D. M., Harbi, N., Ahmmed, S., Rahman, M. Z., & Rahman, C. M. (2010). Mining network data for intrusion detection through naïve bayesian with clustering. Proceedings of the International Conference on Computer, Electrical, System Science, and Engineering (ICCESSE 2010, 836–840.

Faisal Kabir, M., Chowdury, H. A. M., Dahal, K., Hossain, A., & Rahman, C. M. (2010). Disjunctive naïve bayesian classifier to enhance accuracy for dynamic prediction. In O. Tonmukayakul, M. Songkroh, & P. Sureephong (Eds.), 4th International Conference on Software, Knowledge, Information Management and Applications: Towards Happiness and Sustainable Development, SKIMA 2010 (pp. 265–269). SKIMA.

Huda, M. N., Hassan, F., Kotwal, M. R. A., Hasan, M. M., Hossain, M. S., & Rahman, C. M. (2010). Inhibition/enhancement of articulatory features - Which one is dominant for speech recognition? First International Conference on Integrated Intelligent Computing (ICIIC), 184–188. https://doi.org/10.1109/ICIIC.2010.21

Md. Farid, D., Darmont, J., Harbi, N., & Rahman, C. M. (2010). A new supervised learning algorithm using naïve Bayesian classifier. International Conference IADIS Information Systems 2010, 78–84.

Banik, M., Saha, A. K., Kotwal, M. R. A., Huda, M. N., & Rahman, C. M. (2010). Distinctive phonetic feature extraction for Japanese language. In O. Tonmukayakul, M. Songkroh, & P. Sureephong (Eds.), 4th International Conference on Software, Knowledge, Information Management and Applications: Towards Happiness and Sustainable Development, SKIMA 2010 (pp. 66–69). SKIMA.

Shahadat Hossain, M., Kotwal, M. R. A., Banik, M., Hassan, F., Hasan, M. M., Huda, M. N., & Rahman, C. M. (2010). Preparation of Bangla speech corpus for phoneme recognition. In O. Tonmukayakul, M. Songkroh, & P. Sureephong (Eds.), International Conference on Software, Knowledge, Information Management and Applications (SKIMA) (pp. 44–48). SKIMA.

 Hossain, S., Akter, N., Faqruddin Ali Azam, S. M., Sarwar, H., & Rahman, C. M. (2010). Comparative analysis on feature vectors for printed Bangla OCR. In O. Tonmukayakul, M. Songkroh, & P. Sureephong (Eds.), 4th International Conference on Software, Knowledge, Information Management and Applications: Towards Happiness and Sustainable Development, SKIMA 2010 (pp. 114–119). SKIMA.

Mridha, M. F., Rahman, M. S., Huda, M. N., & Rahman, C. M. (2010). Structure of dictionary entries of Bangla morphemes for morphological rule generation for universal networking language. 2010 International Conference on Computer Information Systems and Industrial Management Applications (CISIM), 454–459. https://doi.org/10.1109/CISIM.2010.5643498

Mridha, M. F., Huda, M. N., Rahman, C. M., & Das, J. K. (2010). Development of morphological rules for Bangia root, verbal suffix and primary suffix for universal networking language. 570–573. https://doi.org/10.1109/ICELCE.2010.5700756

Bhadra, K. C., & Rahman, C. M. (2009). Bangla keyboard layout design using frequency and association among bangia characters. Proceedings of 2009 12th International Conference on Computer and Information Technology (ICCIT), 394–399. https://doi.org/10.1109/ICCIT.2009.5407270

Das, R. N., Farid, D. M., & Rahman, C. M. (2009, October 21). A new decision tree building algorithm using bayesian classifier. Proceedings of the 3rd International Conference on Software, Knowledge and Information Management and Applications.

Zia, M. Z. K., Rahman, D. M. F., & Rahman, C. M. (2008). Two-level dictionary-based text compression scheme. International Conference on Computer and Information Technology (ICCIT), 13–18. https://doi.org/10.1109/ICCITECHN.2008.4803026

Gani, M. O., Mehedi, I. J., Seraj, M., Sarwar, H., & Rahman, C. M. (2008). Prediction of the density of active wireless device using markov model. International Conference on Computer and Information Technology (ICCIT), 691–695. https://doi.org/10.1109/ICCITECHN.2008.4803085

Kabir, M. F., Aziz, S., Ahmmed, S., & Rahman, C. M. (2007). Information theoretic SOP expression minimization technique. 10th International Conference on Computer and Information Technology (ICCIT). https://doi.org/10.1109/ICCITECHN.2007.4579404

Mahmud, J., & Rahman, C. M. (2005). On analysis of multi-dimensional features for signature verification. International Conference on Computational Intelligence for Modelling, Control and Automation and International Conference on Intelligent Agents, Web Technologies and Internet Commerce (CIMCA-IAWTIC’06), 2, 735–740. https://doi.org/10.1109/CIMCA.2005.1631556

Ahmed, S., Ahmed, S., & Rahman, C. M. (2005, December 27). Discretization of continuous attributes in Genetic Algorithm based Concept Learner. Proceeding of the 8th International Conference on Computer and Information Technology.

Mahmud, J., & Rahman, C. M. (2005). On the power of feature analyzer for signature verification. Digital Image Computing: Techniques and Applications (DICTA’05), 2005, 217–222. https://doi.org/10.1109/DICTA.2005.1578130

Ahmed, R., & Rahman, C. M. (2004, December 26). Induction of better decision trees using population oriented multi-objective simulated annealing. Proceeding of the 7th International Conference on Computer and Information Technology.

Ali, M. A., Masud, M. M., & Rahman, C. M. (2004, December 26). Implementation of ID3 algorithm by coverage vector. Proceeding of the 7th International Conference on Computer and Information Technology.

Masud, M. M., Ahmmed, S., & Rahman, C. M. (2004, December 26). A new correlation based neural network pruning. Proceeding of the 7th International Conference on Computer and Information Technology.

Huda, M. S., Mia, M. S., Alam, K. M. R., & Rahman, C. M. (2004, December 28). A weighted distance metric based Bayesian classifier. Proceeding of the 3rd International Conference on Electrical and Computer Engineering.

Huda, M. S., Alam, K. M. R., Mutsuddi, K., Rahman, M. K. S., & Rahman, C. M. (2004). A dynamic k-nearest neighbour algorithm for pattern analysis problem. Proceeding of the 3rd International Conference on Electrical and Computer Engineering.

Rahman, a K. M. A., & Rahman, C. M. (2003). A new approach for compressing color images using neural network. In M. Mohammadian (Ed.), Proceedings of International Conference on computational Intelligence for Modelling, Control and Automation - CIMCA’2003 (pp. 12–14).

Sohel, F. A., & Rahman, C. M. (2003). Association rule mining in dynamic database using the concept of border sets. Proceeding of the 3rd International Conference on Electrical, Electronics and Computer Engineering.

Sohel, F. A., Rahman, C. M., & Karmakar, G. C. (2003, December 22). Automatic video object segmentation from VOP. Proceeding of the 3rd International Conference on Electrical, Electronics and Computer Engineering.

Hasan, M. M., & Rahman, C. M. (2003, December 19). Text categorization using association rule based decision tree. Proceeding of the 6th International Conference on Computer and Information Technology.

Saber, A. Y., & Rahman, C. M. (2003, December 19). Cluster and compression for image. 6th International Conference on Computer and Information Technology.

Masud, M. M., & Rahman, C. M. (2003, December 19). Application of minimum description length principle to genetic algorithm based concept learner. Proceeding of the 6th International Conference on Computer and Information Technology.

Huda, M. S., & Rahman, C. M. (2003, December 19). A new algorithm for Naïve Bayesian classifier. Proceeding of the 6th International Conference on Computer and Information Technology.

Mahmud, J. U., & Rahman, C. M. (2003, December 19). Hand written Bangla digit recognition by improved feature analysis and MLP network. Proceeding of the 6th International Conference on Computer and Information Technology.

Rahman, C. M., Sohel, F. A., Naushad, P., & Kamruzzaman, S. M. (2003, May 26). Text classification using the concept of association rule of data mining. Proceeding of the International Conference on Information Technology.

Mahmud, J. U., Raihan, M. F., & Rahman, C. M. (2003). A complete OCR system for continuous Bengali characters. TENCON 2003. Conference on Convergent Technologies for Asia-Pacific Region, 4, 1372–1376. https://www.scopus.com/inward/record.uri?eid=2-s2.0-2342462805&partnerID=40&md5=3b05b51b3bfe7c3c35239efa3cfc9e8d

Sadi, M. S., Rahman, C. M., & Babu, H. M. H. (2002, December 26). An efficient and coherent method using data mining to cluster web documents. Proceeding of the 2nd International Conference on Electrical and Computer Engineering.

Alam, K. M. R., Sadi, M. S., & Rahman, C. M. (2002, October 23). A comparison between Deadlock and Deadlock free concurrency control protocols and a decision which protocol is suitable where. Proceeding of the 2nd International Conference on Electrical Engineering, Jointly Organized by Electrical Engineering Division, IEB and IEEE, Bangladesh Section.

Chowdhury, A. A., Ahmed, E., Ahmed, S., Hossain, S., & Rahman, C. M. (2002, October 23). Optical Character Recognition of Bangla characters using neural network: A better approach. Proceeding of the 2nd International Conference on Electrical Engineering, Jointly Organized by Electrical Engineering Division, IEB and IEEE, Bangladesh Section.

Sadi, M. S., Alam, K. M. R., Huda, M. S., Rahman, C. M., & Babu, H. M. H. (2002, October 23). A comparative analysis on adoption a typical approach to the emerging problems of software industries in Bangladesh. Proceeding of the 2nd International Conference on Electrical Engineering, Jointly Organized by Electrical Engineering Division, IEB and IEEE, Bangladesh Section.

Huda, M. S., & Rahman, C. M. (2002, October 23). Improving the performance of naive bayesian classification using lazy learning and attribute dependence method. Proceeding of the 2nd International Conference on Electrical Engineering, Jointly Organized by Electrical Engineering Division, IEB and IEEE, Bangladesh Section.

Rahman, C. M., & Saber, A. Y. (2002, December 27). Image compression using dynamic clustering algorithm and neural network. Proceeding of the 5th International Conference on Computer and Information Technology.

Saber, A. Y., Chowdhury, M. A. M., & Rahman, C. M. (2002, December 27). Designing 11 segment display for Bangla digits. Proceeding of the 5th International Conference on Computer and Information Technology.

Ahmed, S., Sharmin, M., & Rahman, C. M. (2002, December 27). A generic thinning algorithm with better performance. Proceeding of the 5th International Conference on Computer and Information Technology.

Wasif, A., & Rahman, C. M. (2001, December 28). Performance improvement of decision trees by application of multiple split criteria. Proceeding of the 4th International Conference on Computer and Information Technology.

Rahman, C. M., & Masud, M. M. (2001, December 28). Extending the knowledge intensive genetic algorithm based supervised concept learner. Proceeding of the 4th International Conference on Computer and Information Technology.

Safi, S. A., Haider, M. R., Farid, E. H., Pradhan, M. H., Bari, R., & Rahman, C. M. (2001, December 28). Algorithm for optimization and dimensioning of telephone system in a new urban area. Proceeding of the 4th International Conference on Computer and Information Technology.

Islam, M. M., Rahman, C. M., & Khondoker, M. R. H. (2001, January 25). Generation of vessels’ faired hull form using neural networks and genetic algorithms. Proceeding of the 3rd International Conference on Computer and Information Technology.

Hossain, M. A., Rashid, M. M., & Rahman, C. M. (2001, January 25). A new genetic algorithm based text classifier. Proceeding of the 3rd International Conference on Computer and Information Technology.

Parveen, P., & Rahman, C. M. (2001, January 25). Interactive hierarchical document organization. Proceeding of the 3rd International Conference on Computer and Information Technology.

Rahman, A. K. M. A., & Rahman, C. M. (2001, January 25). Image compression using a counter propagation network. Proceeding of the 3rd International Conference on Computer and Information Technology.

Rahman, C. M., Akther, A., & Wasif, A. (2001, January 25). Handwritten Bangla digit recognition using a neural network. Proceeding of the 3rd International Conference on Computer and Information Technology.

Reaz, M., Khondoker, H., Rahman, C. M., & Islam, M. M. (2001). Effectiveness of neural network and genetic algorithm in hull form design. 2, 653–659. 

Rahman, C. M., & Morshed, M. M. (1999, December 3). Decision tree based learning of handwritten Bangla characters. Proceeding of the 2nd International Conference on Computer and Information Technology.

Kavi, A. Al, Alam, A. M. S., & Rahman, C. M. (1999, December 3). Logic program synthesis from input/output examples using genetic inductive logic programming. Proceeding of the 2nd International Conference on Computer and Information Technology.

Wasif, A., & Rahman, C. M. (1999, December 3). Application of dynamic programming principle in decision tree construction. Proceeding of the 2nd International Conference on Computer and Information Technology.

Rahman, C. M., & Chowdhury, R. A. (1999, December 3). Multi way splits on continuous attributes for decision trees. Proceeding of the 2nd International Conference on Computer and Information Technology.

Rahman, F., & Rahman, C. M. (1998, December 18). A hybrid algorithm for concept learning. Proceeding of the 1st International Conference on Computer and Information Technology.

Masraq, R., & Rahman, C. M. (1998, December 18). Combination of cell multiplexing algorithms in ATM networks: A genetic programming approach. Proceedings of the 1st International Conference on Computer and Information Technology.

Wasif, A., Palit, R., Rashid, M. M., & Rahman, C. M. (1998, December 18). Increasing the performance of classification trees by using a mixed criterion of attribute dependency and gain ratio. Proceedings of the 1st International Conference on Computer and Information Technology.

Wasif, A., Palit, R., Rashid, M. M., & Rahman, C. M. (1998, December 18). Construction of decision trees by using the criterion of class- dependency. Proceedings of the 1st International Conference on Computer and Information Technology.

Kabir, M. H., & Rahman, C. M. (1998, December 18). A new design methodology for getting normalized relations in relational databases. Proceedings of the 1st International Conference on Computer and Information Technology.

Sharmin, E., Akther, A., & Rahman, C. M. (1998, December 18). Text categorization using genetic algorithm. Proceedings of the 1st International Conference on Computer and Information Technology.

Rasul, G., & Rahman, C. M. (1998, December 18). Genetic algorithm based model for Bengali character recognition. Proceeding of the 1st International Conference on Computer and Information Technology.

Kadir, M. I., & Rahman, C. M. (1997, December 9). Strategies of AI discovery systems: A brief review. Proceeding of the 1st National Conference on Computer and Information Systems.

Kabir, M. H., & Rahman, C. M. (1997, December 9). Database normalization using machine learning techniques. Proceeding of the 1st National Conference on Computer and Information Systems.

Islam, M. M., & Rahman, C. M. (1997, December 9). A hybrid learning technique for concept acquisition. Proceeding of the 1st National Conference on Computer and Information Systems.

Rasul, G., & Rahman, C. M. (1997, December 9). Genetic algorithm approach to supervised learning and recognition of Bengali numerals. Proceeding of the 1st National Conference on Computer and Information Systems.

Mostafa, G., & Rahman, C. M. (1997, December 9). Development of a 16 bit microprocessor trainer for the educational institutions of Bangladesh. Proceeding of the 1st National Conference on Computer and Information Systems.

Rahman, C. M., & Numao, M. (1996). Learning simple recursive concepts by discovering missing examples. In N. Foo & R. Goebel (Eds.), PRICAI’96: Topics in Artificial Intelligence (pp. 360–371). Springer. https://doi.org/10.1007/3-540-61532-6_31

Rahman, C. M., & Numao, M. (1996). Learning simple recursive programs by discovering missing examples. Proceeding of the 4th Pacific Rim International Conference on Artificial Intelligence.

Rahman, C. M., & Numao, M. (1995). Look-ahead in ILP by taming the hypothesis search space. Proceeding of the 8th Australian Joint Conference on Artificial Intelligence, Awarded the IEEE’95 Best Student Paper.

Rahman, C. M., & Numao, M. (1995, September). Top-down induction of recursive programs from small number of sparse examples. Proceedings of the 5th International Workshop on Inductive Logic Programming.

Rahman, C. M., & Numao, M. (1995, September). Logic program synthesis as a controlled search through appropriate hypothesis sub-space. In Proceedings of the 5th International Workshop on Inductive Logic Programming.

Rahman, C. M., & Numao, M. (1994). Constructive induction for recursive programs. In S. Arikawa & K. P. Jantke (Eds.), International Workshop on Algorithmic Learning Theory (Vol. 872, pp. 161–175). Springer. https://doi.org/10.1007/3-540-58520-6_62
"""

# Regular expression to match the author list and title
pattern = r'([A-Za-z\s,\.&]+)\s+\(\d{4}\)\.\s+(.+?)\.\s+In'

# Extracting data
extracted_data = re.findall(pattern, input_text)

# Define the CSV file name
csv_file = 'research_titles_and_authors.csv'

# Writing to CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Authors', 'Title'])
    # Write the extracted data
    for authors, title in extracted_data:
        writer.writerow([authors.strip(), title.strip()])

print(f'Data has been written to {csv_file}')