import csv
import re

# Input text
text = """
Sarwar Jahan, Md Al-Imran, Md. Imdadul Islam, M. R. Amin, Comparison of Data Rate and Energy Per Node of Wireless Sensor Network Under Small Scale Fading, International Journal of Computer Networks and Applications (IJCNA), 11, 2, pp.111-126, May 2024. doi: 10.22247/ijcna/2024/224439
Q3 Journal

Shifat Jahan Setu, Fahima Tabassum, Sarwar Jahan and Md. Imdadul Islam, Detection of Diabetes using Combined ML Algorithm, I.J. Intelligent Systems and Applications, 16, 1, pp.11-23, Feb 2024. doi: 10.5815/ijisa.2024.01.02
Scopus indexed

Humayra Ferdous, Sarwar Jahan, Fahima Tabassum and Md. Imdadul Islam, The Performance Analysis of Digital Filters and ANN in De-noising of Speech and Biomedical Signal, International Journal of Image, Graphics and Signal Processing (IJIGSP), 15, 1, pp.63-78, Feb'2023. doi: 10.5815/ijigsp.2023.01.06
(Scopus indexed)

Sharad Hasan , Sarwar Jahan and Md. Imdadul Islam, Disease detection of apple leaf with combination of color segmentation and modified DWT, Journal of King Saud University Computer and Information Sciences, July 2022. doi: doi.org/10.1016/j.jksuci.2022.07.004Get rights and content
Disease detection of apple leaf with combination of color segmentation and modified DWT

Md. Habibur Rahman, Jesmin Akhter, Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam, Data Classification Using Combination of Five Machine Learning Techniques, Journal of Computer and Communications, 9, 12, pp.48-62, Dec' 2021. doi: 10.4236/jcc.2021.912004
Published in Dec' 2021

Meherunnesa Tania, Diba Afroze, Jesmin Akhter, Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam, 'Image Recognition Using Machine Learning with the Aid of MLR', International Journal of Image, Graphics and Signal Processing (IJIGSP), vol. 13, Issue 6, pp.12-22, Dec' 2021. doi: 10.5815/ijigsp.2021.06.02
Published in Dec' 2021

Tandra Rani Das, Sharad Hasan, Md. Rafsan Jani, Fahima Tabassu and Md. Imdadul Islam, Bangla Handwritten Character Recognition Using Extended Convolutional Neural Network, Journal of Computer and Communications, 9, 3, pp.158-171, March 2021. doi: 10.4236/jcc.2021.93012
Published in March 2021

Md Abul Kalam Azad, Anup Majumder, Jugal Krishna Das, Md Imdadul Islam, Improving signal detection accuracy at FC of a CRN using machine learning and fuzzy rules, Indonesian Journal of Electrical Engineering and Computer Science, 21, 2, pp.1140-1150, Feb' 2021. doi: DOI: 10.11591/ijeecs.v21.i2
scopus indexed journal

Sarwar Jahan1, Md. Imdadul Islam, M. R. Amin, Performance Evaluation of Multi-Hop Wireless Network with Point-to-Point Traffic Model and Fuzzy System, Jordan Journal of Electrical Engineering, vol. 6, no. 4, pp.316-333, 2020. doi: DOI: 10.5455/jjee.204-1592119349
peer reviewed journal

Bishal Gautam, Md. Rafsan Jani, Bulbul Ahammad, Rahmina Rubaiat, Md. Imdadul Islam, Convex-hull of Users under Adaptive Beam in WAN to Minimize Interference, International Journal of Computer Sciences and Engineering, 8, 10, pp.52-59, October 2020.
Peer-Reviewed and UGC Approved

Samsunnahar Khandakar, Md. Imdadul Islam, Fahima Tabassum, Risala T. Khan, Recognition of Bangla Handwritten Number Using Combination of PCA and FIS with the Aid of DWT, Journal of Computer and Communications, 8, 9, pp.109-125, September 2020. doi: DOI: 10.4236/jcc.2020.89010
Published in September 2020

Md Abul Kalam Azad, Anup Majumder, Muhammad R. A. Khandaker, Jugal K. Das, Md. Imdadul Islam, Primary User Aided Cognitive Radio Network With Optimum Location Of Relay, International Journal of Scientific & Technology Research, Volume 9, Issue 09, pp.217-221, September 2020.
Scopus Indexed

Sarwar Jahan, Md. Imdadul Islam, M. R. Amin, Optimization of Dual-Hop Wireless Link Under Energy Harvesting Scheme, International Journal of Scientific & Technology Research, Volume 9, Issue 09, pp.147-153, September 2020.
Scopus Indexed

Bir Bahadur Khatri, Bulbul Ahammad, Md. Mezbahul Islam, Rahmina Rubaiat and Md. Imdadul Islam, Performance Evaluation of LTE Network using Maximum Flow Algorithm, International Journal of Computer Science and Information Technology, 12, 4, pp.67-79, 2020.
Performance Evaluation of LTE Network using Maximum Flow Algorithm

Bulbul Ahammad, Risala T. Khan and Md. Imdadul Islam, WLAN-LTE Integrated Traffic Model under Unlicensed Spectrum, International Journal of Computer Science and Information Security (IJCSIS), 17, 3, pp.85-100, 2019.
Published in March 2019.

Md. Mafiul Hasan Matin, Tanzim Kabir, Amina Khatun, Md. Imdadul Islam, Data Prediction Model Using Combination of Clustering and Fuzzy Technique, Journal of Computer and Communications, 8, 7, pp.79-89, 2020. doi: 10.4236/jcc.2020.87007
Published in July 2020

Adila Nuzhat, Fahima Tabassum, Md. Imdadul Islam, Object Detection using Convolutional Neural Network and Extended SURF with FIS, International Journal of Engineering and Advanced Technology (IJEAT), 9, 5, pp.918-925, 2020. doi: 10.35940/ijeat.E9915.069520
 ISSN: 2249 – 8958, pp.918-925, Volume-9 Issue-5, June 2020

https://www.ijeat.org/download/volume-9-issue-5/

The Tradeoff between Mean Delay and Energy Saving Factor under DRX Scheme,
Mohammad Asif Hossain, Md. Imdadul Islam, Fahima Tabassum and M. R. Amin, ‘The Tradeoff between Mean Delay and Energy Saving Factor under DRX Scheme,’ International Journal of Computer Applications (0975 – 8887), Volume 177, No. 43, pp.40-47, March 2020

DOI: 10.5120/ijca2020919946

Human Face Recognition with Combination of DWT and Machine Learning,
FahimaTabassum, Md.Imdadul Islam, RisalaTasin Khan and M. R. Amin, ‘Human Face Recognition with Combination of DWT and Machine Learning,’  Journal of King Saud University - Computer and Information Sciences (Elsevier), Feb 2020

Traffic Modelling of Low Dense Femtocellular Network for Long Term Evolution,
Jesmin Akhter, Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam, M. R. Amin, ‘Traffic Modelling of Low Dense Femtocellular Network for Long Term Evolution,’ Journal of Computer and Communications, pp.88-101, Vol.7, No.12, December 2019

International Journal of Innovative Technology and Exploring Engineering (IJITEE),
Samsunnahar Khandakar, Jahirul Islam Babar, Anup Majumder, Md. Imdadul Islam 'Complexity Analysis and Accuracy of Image Recovery Based on Signal Transformation Algorithms,'International Journal of Innovative Technology and Exploring Engineering (IJITEE), ISSN: 2278-3075, Volume-9 Issue-1, pp.1607-1612, November 2019

 

Human Face Detection Based on Combination of Linear Regression, PCA and Fuzzy C-Means Clustering,
Momotaz Begum Panna and Md. Imdadul Islam, ‘Human Face Detection Based on Combination of Linear Regression, PCA and Fuzzy C-Means Clustering,’ IJCSIS , Vol. 17 No. 7, pp. 57-62, JULY 2019

Performance Analysis of Multi-Hop Wireless Link under Maximum Flow Algorithm,
Sarwar Jahan, Md. Imdadul Islam and M. Ruhul Amin, ‘Performance Analysis of Multi-Hop Wireless Link under Maximum Flow Algorithm,’ Journal of Computer and Communications Vol.7 No.8, pp.8-16, August 2019

Electrical Load Forecasting Using Fuzzy System,
Mahir Faysal, Md. Jahirul Islam1, Md. Mohiuddin Murad, Md. Imdadul Islam, M. Ruhul Amin, ‘Electrical Load Forecasting Using Fuzzy System,’ Journal of Computer and Communications, pp. 27-37, vol. 7, no.9, Sept’ 2019

Combination of SVM, LDA, PCA and linear regression under fuzzy system in human face recognition,
Bulbul Ahammad, Liton Jude Rozario, Anup Majumder, Md. Imdadul Islam, ‘Combination of SVM, LDA, PCA and linear regression under fuzzy system in human face recognition,’  International Journal of Engineering &Technology, 7 (4) (2018) pp. 6970-6976

 

Optimum Positioning and planning of cell patterns in an irregular area for cellular network,
Imdadul Islam, L. J. Rozario and M. Hussain,  Journal of Electronics and Computer Science, Vol.1, pp.6-9,  June 1998, ISSN 1680-6743

Central Dynamic Channel allocation Strategy for GSM Network,
Md. Imdadul Islam, Q. Maula and M. Murshed, Jahangirnagar University Journal of Science, Vol.-22 & 23, ISSN-1022 8594, PP.103-111, Dec, 2000

Electrical Load Forecasting by Moving Average Method,
Q. Maula, Imdadul Islam and I. Shariar,  Journal of Electronics and Computer Science, Vol.2, pp. 19-23,  June 2001, ISSN 1680-6743

A theoretical approach to detect MHz range radio signal for Wireless Local Loop,
Imdadul Islam, Q. Maula and L. J. Rozario,  Jahangirnagar University Journal of Science, Vol.-25, pp.105-110, June-2002,   ISSN-1022 8594

BASIC Stamp II- A bais for Control Application,
M. H. Ali and Imdadul Islam, Journal of Electronics and Computer Science, Vol. 3 Feb’ 2002, pp. 13-18, ISSN 1680-6743

Traffic Analysis of an Overloaded Cell of Wireless Local Loop in DCA (Dynamic Channel Allocation) Environment,
Imdadul Islam, I. Jahan and L. J. Rozario,  Journal of Electronics and Computer Science, Vol. 3 Feb’ 2002, pp. 7-11,  ISSN 1680-6743

Analysis of Overflow Traffic Profile in Alternate Routing Network Based on ERT Method,
Imdadul Islam, Q. Maula and L. J. Rozario, Journal of Electronics and Computer Science, ISSN 1680-6743, Vol. 3,  pp. 31-34, June’ 2003

Impact of Channel Reservation on Call Blocking & Forced Termination in Mobile Cellular Network,
Imdadul Islam , F. H. Bhuiyan and A. Kabir, Jahangirnagar University Journal of Science, Vol.-26,  2003, pp. 123-132, ISSN-1022 8594

Modeling of Limited and Unlimited Queuing Traffic for ATM Network’ System,
Imdadul Islam and M. H. Chowdhury, Journal of Electronics and Computer Science, Vol.5 June 2004, pp. 1-6,  ISSN 1680-6743

Impact of Geometry and Weighting Factors in Radiation Pattern and Signal Response of Array Antennal System,
Imdadul Islam, B. Alam and N. Sultana, Journal of Electronics and Computer Science, Vol.5 June 2004, pp. 15-23, ISSN 1680-6743

An Analytical Modeling of Low Dense Network Traffic for LEO Mobile Satellite Systems Based on Mobility Model,
Imdadul Islam and S. Hossain , Journal of Electronics and Computer Science, pp. 31-44, Vol. 5 June’ 2004, ISSN 1680-6743

WLL Network in Dynamic Channel Allocation Environment,
Imdadul Islam and S. Hossain, Indian Journal of Telecommunications, vol.54, Issue 3, pp.28-40, May-June 2004

An Analytical Model of Performance Measurement of SDMA Traffic with Provision of Tertiary Beam for PCT-II Case,
Imdadul Islam and S. Hossain,  WSEAS TRANSACTIONS ON COMMUNICATIONS, ISSN: 1109-2742 (International Index of Published Series in Paris and in the Library's Index of Athens), pp. 411-418, April’ 2004

Capacity increment of a single mode fibre using WDM with bit skew compensation technique,
Imdadul Islam, S. Karim and S. Hossain, Jahangirnagar university Journal of Science, vol. 28, pp. 185-193, 2005

Impact of Length of Foreign Agent Chain on Protocol Cost of Mobile IP Network,
Imdadul Islam and S. Hossain, Journal of Electronics and Computer Science,’  ISSN 1680-6743, Vol. 6, pp.27-33,  June’ 2005

An Analytical Model of Performance Analysis of SDMA System of Low Dense Traffic Network,
Imdadul Islam and S. Hossain,  Journal of Science, J.U. vol.27., Dec’2005, pp.133-143

Comparison of Traffic Performance of QPSK and 16-QAM Modulation Techniques for OFDM System,
Imdadul Islam and S. Hossain, Journal of Telecommunications and Information Technology” (JTIT), pp.147-152, Szachowa St. 1, 04-894 Warsaw, Poland, 2005

A Newly Developed Random Walk Model for PCS Network’ Journal of Telecommunications and Information Technology,
Imdadul Islam and S. Hossain, (JTIT), pp.153-156, Szachowa St. 1, 04-894 Warsaw, Poland, 2005

Impact of Partial Response Coding for Reduction of Inter Channel Interference in OFDM system,
M. R. Rahman, S. A. Mamun, M. Kabir and Imdadul Islam,  Asian Journal of Information Technology, ISSN: 1683-3915, vol.4, no.12, Dec’2005, pp.1137-1140

A newly designed Markovian chain for packet data traffic,
Imdadul Islam, S. Hossain and J.K. Das, Jahangirnagar university Journal of Science, vol. 29, pp. 63-68, 2006

Digital Signal Processing of Electrical Signal from the Brain and the Heart,
Imdadul Islam, M. Zulhasnine, J. K. Das and S. Karim, Journal of Electronics and Computer Science,  ISSN 1680-6743, Vol. 7, pp.1-6,  June’ 2006

Performance Evaluation of Wireless ATM Network Based on Two States Absorbing Markovian Chain,
Md. Imdadul Islam and J. K. Das,  Jahangirnagar University Journal of Science, vol.30, No.2, 215-228, Dec’2007

Radiation Pattern and Beam width Control of Linear and Rectangular Array Antenna System,
Nowf Al Haque, M. Ariful Alam, Md. Imdadul Islam and M.R. Amin, East West Journal, Vol. 1, pp. 119-128, 2007

Reception of TV signal at 200MHz using cross dipole antenna,
Imdadul Islam, S. Karim and A. Matin, Jahangirnagar University Journal of Science, vol.30, pp. 141-146, June 2007

A Mathemetical Model of Traffic Performance of Mobile Cellular Network,
Imdadul Islam and J. K. Das,  Journal of Electronics and Computer Science, Vol. 8, pp. 1-9, June’ 2007

Modeling of voice data integrated traffic in 3G mobile cellular network,
Imdadul Islam, J. K. Das and S. Hossain ,  Journal of  Telecommunications and Information Technology, National Institute of Telecommunications Szachowa st  104-894 Warsaw, vol. 2/2007, Poland, June’2007

Modeling of mixed traffic for mobile cellular network,
Imdadul Islam, J. K. Das and S. Hossain, Journal of Telecommunications and Information Technology, National Institute of Telecommunications Szachowa st  104-894 Warsaw, pp.83-89, vol.1/2007, Poland, June 2007

Development of deterministic service time traffic model for packet communications,
S. Karim, Imdadul Islam, A. Rab, M. R. Hasan and M. R. Amin, Information Technology Journal 6(1), Asian Network for Scientific Information, 160-165, 2007

Performance evaluation of rake receiver of DS-CDMA under AWGN environments,
Md. Imdadul Islam, M. ZulHasnine and M.R. Amin, Journal of Discrete Mathematical Sciences & Cryptography , Taru  Publications, G-159, Pushkar Enclave, Pashchim Vihar, New Delhi - 110063 (India), pp. 276-279, vol.11, no.3, 2008

Optimum Location of a Switching Station of an Urban Network,
Md. Imdadul Islam, S. Jahan and M.R. Amin, IETECH Journal of Communication Techniques, vo.2, no.1, pp.28-34, 2008

Dynamic Channel Allocation in Mobile Cellular Networks’ Network,
Shahrina Mou, Md. Imdadul Islam and M.R. Amin, Journal of Discrete Mathematical Sciences & Cryptography , vol.11, no.6, pp.705-714, 2008, Pashchim Vihar, New Delhi – 110063

Performance estimation of call admission schemes based voice/data integrated wireless network with customer retrials,
L. J. Rozario and Md. Imdadul Islam,  Journal of Discrete Mathematical Sciences & Cryptography, pp. 253-294, Taru  Publications, G-159, Pushkar Enclave, Pashchim Vihar, New Delhi - 110063 (INDIA), 2009

Evaluation of Delay of Voice End User in Cellular Mobile Networks with 2D Traffic System,
M.R. Amin and Md. Imdadul Islam, Research Journal of Information Technology, vol. 1, no. 2, pp. 57-69, 2009

Throughput optimization for interfering channels in wireless link,
S.M. Mamun, Md. Fahimul Islam and Md. Imdadul Islam,  Dhaka Univ. J. Sci. 57(1), pp.71-73, Jan, 2009

Two Dimensional Continuous Time Markov Chain for Packet Traffic: A Newly Proposed Approach,
Md. Imdadul Islam, J. K. Das and Habibur Rahman, Dhaka University Journal of Science, 2009

Call Admission Scheme of Mixed Traffic for Mobile Cellular Network,
Md. Imdadul Islam, J. K. Das, and M. R. Amin,  Journal of Discrete Mathematical Sciences & Cryptography, Taru  Publications, G-159, Pushkar Enclave, Pashchim Vihar, New Delhi - 110063 (INDIA), 2009

Performance Comparison of Two and Three Beam SDMA Traffic in Mobile Cellular Network,
Md. Imdadul Islam and  J.K. Das,  Journal of Discrete Mathematical Sciences & Cryptography, Taru  Publications, G-159, Pushkar Enclave, Pashchim Vihar, New Delhi - 110063 (India), Vol.12, No.1, pp.51-61, Feb’ 2009

Performance Evaluation of Underlay Overlay Cellular System Based on Equivalent Random Theory Traffic Model,
Md. Imdadul Islam, J. K. Das and Habibur Rahman,  Dhaka University Journal of Science, 57(1), pp.39-42, January, 2009

Determination of save operating border of asynchronous data traffic based on MMPP,
Md. Imdadul Islam and M. R. Amin, Journal of Convergence Information Technology, vol.4, no.4, Dec 2009

The impact of Geometry on parameters of a slot antenna,
K.M. Akkas Ali and Md. Imdadul Islam, Jahangirnagar University Journal of Science, v0l.33, no.1, pp.145-164, Dec 2010

Demystifying the digital adaptive filters conducts in acoustic echo cancellation,
Md. Anamul Haque, A.K.M Kamrul Islam and Md. Imdadul Islam,  Journal of Multimedia, vol.5, no.6, pp.568-579, Academy Publisher, Dec’2010

Call Admission Control Strategy for System Throughput Maximization Using DOVE,
Tanzilah Noor Shabnam, Md. Imdadul Islam and M. R. Amin, J. Convergence Information Technology (JCIT) (Korea), vol. 5, no. 8, pp. 137-145,  Oct’2010. 

Cost Optimization of Underlay Overlay Cellular Network for Handoff Traffic,
Sarwar Jahan, Md. Imdadul Islam, and M. R. Amin,  J. Telecommunications (UK), Accepted, 2010

Fingerprint Detection Using Canny Filter and DWT, a New Approach,
Md. Imdadul Islam, Nasima Begum, Mahbubul Alam and M.R. Amin, Journal of Information Processing Systems, vo.6, no.4, pp.511-520, Dec’2010, 

Performance Evaluation of the WiMAX Network Based on Combining the 2D Markov Chain and MMPP Traffic Model,
Tonmoy Saha, Md. Abu Shufean, Mahbubul Alam and Md. Imdadul Islam, Journal of Information Processing Systems, Vol.7, No.4, pp. 653-678, December 2011

Performance Evaluation of Finite Queue Switching Under Two-Dimensional M/G/1(m) Traffic,
Md. Syeful Islam, Md. Rezaur Rahman, Anupam Roy, Md. Imdadul Islam and M. R. Amin, Journal of Information Processing Systems, Vol.7, No.4, pp.679-690, December 2011 

Application of Zero Forcing Adaptive Equalization in Compensation of Fading Affect of Two-hop Wireless Link,
1Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam and M. R.  Amin,  IACSIT International Journal of Engineering and Technology, vol. 3, no. 6, pp. 628-633, Dec' 2011

MMPP+M/D/1 Traffic Model in Video-Data Integrated Service under ATM System,
Anupam Roy, Md. Imdadul Islam and M.R. Amin, International Journal of Engineering and Technology, Vol. 3, No. 6, pp. 615-620, December 2011

Performance Comparison of Uplink Cellular Network under Rayleigh and Nakagami-m Fading Environments,
M. Nazimuzzaman, Himadri S. Saha, Md. Imdadul Islam, M.R. Amin, International Journal of Soft Computing and Engineering (IJSCE), vol.1, Issue-5, pp. 276-280, Nov’ 2011

Performance Evaluation of Full Rate Space-Time Block Code for Multiple Input Single Output (MISO) Wireless Communication System,
Fahima Tabassum, Mahbubul Alam, Md. Imdadul Islam and M.R. Amin,  WSEAS Transcations on Communications, Issue 8, vol.10, pp. 233-242, August 2011, 

Performance Evaluation of Two-hop Wireless Link under Rayleigh and Nakagami-m Fading Channel for 8-PSK and 16-QAM,
Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam and M. R.  Amin, IACSIT International Journal of Engineering and Technology, Vol. 3, No. 5, pp.454-459, October 2011

‘Performance Comparison of STFT, WT, LMS and RLS Adaptive Algorithms in Denoising of Speech Signal,
Mahbubul Alam, Md. Imdadul Islam, and M. R. Amin, IACSIT International Journal of Engineering and Technology, Vol.3, No.3,pp.235-238,  June 2011

Fingerprint detection based on DWT: a new approach,
N. Begum, Md. Imdadul Islam,  Journal of Discrete Mathematical Sciences & Cryptography, India, pp.77-87, Feb 2011

Cost Optimization of Alternate Routing Network of M/G/1(M) Traffic,
Md. Imdadul Islam, M. F. K. Patwary and M.R. Amin,  The Mediterranean Journal of Electronics and Communications, vol.6, no.1, pp.190-195, 2011

Comparison of LMS and FDAF Algorithms in Equalization of Fading Channel,
Md. Imdadul Islam, Md. Ariful Islam, Nur Mohammad, Mahbubul Alam, and M.R. Amin, IACSIT International Journal of Engineering and Technology, Vol.3, No.1, pp.16-21, February 2011, ISSN: 1793-8236,  http://www.ijetch.org/abstract/193-T304.htm

Recovery of Noisy ECG Signal by ANFIS and DWT,
Md. Imdadul Islam, Nasima Begum, Mahbubul Alam and M. R. Amin, JOURNAL OF ELECTRONICS AND COMPUTER SCIENCE RESEARCH VOL. 1 NO. 3,pp12-119, DECEMBER 2012 (ISSN: 2306-5605)

Cost Analysis of VoIP Traffic under IEEE 802.16e/m,
Jesmin Akhter, Md. Imdadul Islam, and M. R. Amin, JOURNAL OF ELECTRONICS AND COMPUTER SCIENCE RESEARCH VOL. 1 NO. 3, pp7-11, DECEMBER 2012 (ISSN: 2306-5605)

Enhancement of Performance of Cognitive Radio Network with Incorporation of MRC Scheme at Secondary Receiver,
Risala T. Khan, Tanzilah Noor Shabnam, Md. Imdadul Islam, and M. R. Amin, IACSIT International Journal of Engineering and Technology, Vol. 4, No. 4, pp.495-499, August 2012

A New Approach to Fingerprint Detection Using a Combination of Minutiae Points and Invariant Moments Parameters,
Sarnali Basak, Md. Imdadul Islam and M. R. Amin,  Journal of Information Processing Systems, Vol.8, No.3, pp.421-436, September 2012

Determination of Medium Access Probability of Cognitive Radio under Different Fading,
Rezwan Ahmad, Md. Imdadul Islam, M. R. Amin,   International Journal of Soft Computing and Engineering (IJSCE), ISSN: 2231-2307, Volume-2, Issue-3, pp.459-463,  July 2012

Fingerprint Detection Applying Discrete Wavelet Transform on ROI,
Mahbubul Alam, Sarnali Basak and Md. Imdadul Islam,  International Journal of Scientific & Engineering Research, pp.1-5, Volume 3, Issue 6, June-2012 1, ISSN 2229-5518

Performance Evaluation of Dissimilar Bandwidth Traffic of Mobile Cellular Network Based on Guard Channel Strategy ,
Fahima Tabassum, Normin Abedin and Md. Imdadul Islam, Journal of Electronics and Computer Science, Vol.13, pp.21-25, June 2012

Derivation of BER of MPSK: A New Approach,
M. A. Khandaker, S. M. raihan Azim and Md. Imdadul Islam,  Journal of Electronics and Computer Science, Vol.13, pp.2-4, June 2012

Evaluation of Three Layered Cell Mobile Cellular Network Using QERT Traffic Model,
Risala Tasin Khan and Md. Imdadul Islam, Journal of Electronics and Computer Science, Vol.11, pp.1-5, June 2012

Cost Evaluation of Traffic of Alternate Routing Network: an Extension towards Multi Exchange Network,
Md. Abu Shameem, Md. Imdadul Islam and M. R. Amin Member, IEEE, Journal of Electronics and Computer Science, vol.13, pp.11-19, June 2012

Detection of Virtual Core Point of A Fingerprint: A New Approach,
Sarnali Basak, Md. Imdadul Islam, M. R. Amin , International Journal of Soft Computing and Engineering (IJSCE), Volume-2, Issue-2, pp.236-239, May 2012, 

Cost Based Performance Evaluation of H2/D/1 and E2/D/1 Traffic Model,
Jesmin Akhter, Md. Imdadul Islam, Himadri Saha, M. R. Amin, International Journal of Engineering and Innovative Technology (IJEIT), Volume 1, Issue 4, pp.163-170, April 2012, 

Performance Evaluation of Two-Hop Wireless Link under Rayleigh and Nakagami-m Fading,
Himadri S. Saha, Md. Imdadul Islam, M.R. Amin, International Journal of Engineering and Technology Volume 2 No. 1, pp.22-27, January, 2012, 

Performance Evaluation of Two-Hop Wireless Link under Nakagami-m Fading,
Afsana Nadia Nova, A. R. Chowdhuray, Md. Imdadul Islam and M. Amin,  International Journal of Advanced Computer Science and Applications (IJACSA), vol.4, no.7, pp.142-146, 2013

Spectrum Sensing and Data Transmission in a Cognitive Relay Network Including Spatial False Alarm,
Tishita, Sumiya Akhter, Md. Imdadul Islam, M. Amin,  Journal of Information Processing Systems (JIPS), Korea, Accepted, July 2013

Array Antenna System of Frequency Independent Antennas Based on RWG Elements,
Abu Sayed Md. Mostafizur Rahaman, Jesmin Akhter and Md. Imdadul Islam, Journal of Electronics and Computer Science Research, vol.2 no.1, pp.7-14, April, 2013

Performance Evaluation of Voice-Data Integrated Traffic in IEEE 802.11 and IEEE 802.16e WLAN,
Anupam Roy, Md. Imdadul Islam, And M. R. Amin,   WSEAS TRANSACTIONS on COMMUNICATIONS, Issue 7, Volume 12, pp.352-365, July 2013

Performance Evaluation of Cognitive Radio Network under Limited User Traffic,
Md. Budrul Hasan Bhuiyan, Md. Fazlay Rabbi, Risala Tasin Khan, Jesmin Akhter and Md. Imdadul Islam,  JAHANGIRNAGAR UNIVERSITY JOURNAL OF ELECTRONICS AND COMPUTER SCIENCE ,Volume 15, pp.23-28, June 2014

Recovery of Grayscale Image from Its Halftoned Version Using Smooth Window Function,
Hafsa Moontari Ali, Roksana Khanom, Sarnali Basak and Md. Imdadul Islam,  JAHANGIRNAGAR UNIVERSITY JOURNAL OF ELECTRONICS AND COMPUTER SCIENCE ,Volume 15, pp.15-22, June 2014

Impact of Geometry and Feed Point on Radiation Pattern of a Patch Antenna and Its Linear Array as a Substitute of Multi-hop Link,
Abu Sayed Md. Mostafizur Rahaman, Jesmin Akhter, Md.Imdadul Islam and M.R Amin,  JAHANGIRNAGAR UNIVERSITY JOURNAL OF ELECTRONICS AND COMPUTER SCIENCE ,Volume 15, pp.7-14,  June 2014

Cross-Layer Analytical Model for Cognitive Radio Network under Engset and M/G/1/m Traffic,
Sajib Kumar Kuri, Risala Tasin Khan and Md. Imdadul Islam,  Volume 15, pp.1-5, June 2014

Performance Evaluation of VoIP Service of Cognitive Radio System Based on DTMC,
Ummy Habiba, Md. Imdadul Islam M. R. Amin,  Journal of Information Processing Systems (Korea), J Inf Process Syst, Vol.10, No.1, pp.119~131, March 2014

Spectrum Sensing and Data Transmission in a Cognitive Relay Network Considering Spatial False Alarms,
Tasnina A. Tishita, Sumiya Akhter, Md. Imdadul Islam and M. R. Amin,  J Inf Process Syst, Vol.10, No.3, pp.1-12, June 2014

Image Based Measurement of Length and Distance of an Inaccessible Object,
Md. Imdadul Islam, Mahbubul Alam, Sarnali Basak, Md. Al-Amin Khandaker, S M Raihan Azim5, International Journal of Advanced Computer Research (ISSN (print): 2249-7277 ISSN (online): 2277-7970) pp.123-128, Volume-3 Number-3 Issue-12 September-2013

Traffic Analysis of a Cognitive Radio Network Based on the Concept of Medium Access Probability,
Risala T. Khan, Md. Imdadul Islam and M. R. Amin , (JIPS)Journal of Information Processing Systems (Korea), vol. 10, no.4, pp. 602 ~ 617, DEC’2014

Performance Evaluation of the WiMAX Network under a Complete Partitioned User Group with a Traffic Shaping Algorithm,
Jesmin Akhter, Md. Imdadul Islam and M. R. Amin, (JIPS) Journal of Information Processing Systems (Korea), vol. 10, no.4, pp. 568 ~ 580, DEC’2014

Preliminary Identification of Fingerprint based on Shape Features,
Hafsa Moontari Ali and Md. Imdadul Islam, ‘Preliminary Identification of Fingerprint based on Shape Features,’ International Journal of Computer Applications (0975 – 8887),Volume 120 – No.15, pp.11-16, June 2015

Selection of the Best Two-Hop AF Wireless Link under Multiple Antenna Schemes over a Fading Channe,
Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam and M.R. Amin,  Journal of Information Processing Systems, vol. 11, no. 1, pp. 57~75, 2015.

Adaptive Beamforming and Cancellation of Jammer Using Linear Array Antenna System,
Israt Jahan, Md. Imdadul Islam And A.S.M. Mostafizur Rahaman, International Journal of Engineering Sciences & Research Technology, pp.648-657, vol.4, issue-6, April, 2015

Performance Evaluation of Voice Traffic of IEEE 802.16e under Femto Cellular Network,
Jesmin Akhter, Md. Imdadul Islam, M.R. Amin, International Journal of Computer Applications (0975 – 8887), Volume 124, No.5, pp.37-41, August 2015

Medium Access Probability of Cognitive Radio Network at 1900 MHz and 2100 MHz,
Risala Tasin Khan, Md. Imdadul Islam, M.R. Amin,  International Journal of Computer Applications (0975 – 8887),Volume 124, No.5, pp. 42-45, August 2015,

Performance Evaluation of Cognitive Radio Network Based on 2-D Markov Chain,
Md. Imdadul Islam, Md. Fazlay Rabbi, Risala Tasin Khan, and Jesmin Akhter, ‘Performance Evaluation of Cognitive Radio Network Based on 2-D Markov Chain,’ Journal of Telecommunications and Information Technology (JTIT), pp.39-44, vol.3, Sept' 2015

Identification of Fingerprint using Discrete Wavelet Packet Transform,
Fahima Tabassum, Md. Imdadul Islam and M.R. Amin, ‘Identification of Fingerprint using Discrete Wavelet Packet Transform,’ International Journal of Computer Applications (0975 – 8887), Volume 128 – No.7, pp.38-44, October 2015

 

Performance Evaluation of Two-Hop Wireless Network under Asymmetric Fading Environment,
Sarwar Jahan, Md Imdadul Islam, Mohamed Ruhul Amin, ‘Performance Evaluation of Two-Hop Wireless Network under Asymmetric Fading Environment,’ Journal of Computer and Communications, 2015, 3, 21-27

Analysis of Sleep Window of IEEE802.16m Network Based on State Transition Chain,
Mohammad Asif Hossain, Mohammad Imdadul Islam, Mohamed Ruhul Amin, ‘Analysis of Sleep Window of IEEE802.16m Network Based on State Transition Chain,’ Journal of Computer and Communications, 2015, 3, 77-83

Traffic Modeling of Finite Queue and General Service Time Distribution,
Md. Imdadul Islam, Md. Zahirul Islam, A.S.M. Mostafizur Rahaman and Israt Jahan, ‘Traffic Modeling of Finite Queue and General Service Time Distribution,’ Jahangirnagar University Journal of Science, vo.38, no.2, pp. 23-34, Dec’2015

Recovery of Image through Alamouti Channel with Incorporation of RSA Algorithm,
Aninda Majumder, Mohammad Raihan Ruhin, Tahsina Hashem, Md. Imdadul Islam, ‘Recovery of Image through Alamouti Channel with Incorporation of RSA Algorithm,’ Journal of Computer and Communications, 2016, 4, pp.1-10.

Load Sensitive Power Saving Technique for 4G Mobile Network under Limited User Traffic,
Mohammad Asif Hossain, Mohammad Imdadul Islam, Mohamed Ruhul Amin, ‘Load Sensitive Power Saving Technique for 4G Mobile Network under Limited User Traffic,’ Communications and Network, 8, pp.79-87, May 2016

Optimum Access Analysis of Collaborative Spectrum Sensing in Cognitive Radio Network using MRC,
Risala Tasin Khan, Md. Imdadul Islam, Shakila Zaman  and M.R. Amin, ‘ Optimum Access Analysis of Collaborative Spectrum Sensing in Cognitive Radio Network using MRC,’  (IJACSA) International Journal of Advanced Computer Science and Applications, pp. 367-373, Vol. 7, No. 7, 2016

Resource Management of Mobile Communication System,
Dewan Md. Mostafezur Rahman, Md. Imdadul Islam, Abu Sayed Md. Mostafizur Rahaman, Mohammad Shorif Uddin, Md. Akram Hossain,  ‘Resource Management of Mobile Communication System,’ International Journal of Advanced Engineering Research and Science (IJAERS), Vol-3, Issue-8, pp.72-76, Aug- 2016

The MIMO Performance of LTE Network under Rayleigh Fading Environment,
Jesmin Akhter, Md. Imdadul Islam, ASM M Rahaman and M R Amin, ‘The MIMO Performance of LTE Network under Rayleigh Fading Environment,’ International Journal of Computer Science and Information Security,  (pp. 88-94), vol. 14, no. 8 AUG 2016

Performance Evaluation of Femtocell Based LTE Network under the Concept of Cross-layer Optimization,
Jesmin Akhter, Md. Imdadul Islam, ASM M Rahaman and M R Amin, ‘Performance Evaluation of Femtocell Based LTE Network under the Concept of Cross-layer Optimization,’ International Journal of Computer Science and Information Security,  (pp. 52-60), vol. 14, no. 7, July 2016

Traffic Modeling of Mobile Cellular Network Using Combination of Limited and Unlimited User Groups,
Dewan Md. Mostafezur Rahman, Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam, Mohammad Shorif Uddin and Md. Akram Hossain, ‘Traffic Modeling of Mobile Cellular Network Using Combination of Limited and Unlimited User Groups,’ International Journal of Computer Science and Information Security,  vol. 14, no. 10,  pp. 40-46, OCT 2016

Comparison of FIR and IIR Filter Bank in Reconstruction of Speech Signal,
Fahima Tabassum, Md. Imdadul Islam and M. R. Amin, ‘Comparison of FIR and IIR Filter Bank in Reconstruction of Speech Signal,’  International Journal of Computer Science and Information Security,  vol. 14, no. 9, pp. 864-872, SEP 2016

Performance Analysis of CSMA/CA Network using Modified State Transition Chain,
Dulal Chakraborty, Abul Kalam Azad, Md. Imdadul Islam and Abu Sayed Md. Mostafizur Rahaman, ‘Performance Analysis of CSMA/CA Network using Modified State Transition Chain,’ International Journal of Computer Science and Information Security, Vol. 14 No. 12, pp. 1064-1070, DEC 2016 (Thomson Enlisted)

Human Face Recognition Using Eigen Decomposition on ROI,
Tania Khatun, Abul Kalam Azad, ASM M Rahaman, Md. Rafsan Jani and Md. Imdadul Islam, ‘Human Face Recognition Using Eigen Decomposition on ROI,’ International Journal of Computer Science and Information Security, Vol. 14 No. 12, pp. 1071-1079, DEC 2016

Comparison of CSI and Fixed Gain Relay of Two-hop Wireless Link under Small-Scale Fading,
Sarwar Jahan, Md. Imdadul Islam and M. R. Amin, ‘Comparison of CSI and Fixed Gain Relay of Two-hop Wireless Link under Small-Scale Fading,’ International Journal of Computer Science and Information Security,  vol. 15 no. 6, pp.6-10,  JUN 2017

Pattern Recognition Using the Concept of Disjoint Matrix of MIMO System,
Mezbahul Islam , Rahmina Rubaiat , Imdadul Islam , Mostafizur Rahaman , and Mohamed Ruhul Amin, ‘Pattern Recognition Using the Concept of Disjoint Matrix of MIMO System,’ The International Arab Journal of Information Technology, Vol. 14, No. 4, pp.495-501, July 2017

Human Face Detection Using Combination of LDA and DWT,
M. Amin, S. S. Khan and Md. Imdadul Islam, ‘Human Face Detection Using Combination of LDA and DWT,’ International Journal of Computer Science and Information Security, vol. 15 no. 7, pp. 87-94, Jul 2017

Comparison of filter banks of DWT in recovery of image using one dimensional signal vector,
Fahima Tabassum, Md. Imdadul Islam, M.R. Amin, ‘Comparison of filter banks of DWT in recovery of image using one dimensional signal vector,’ In Press, Corrected Proof,  Journal of King Saud University - Computer and Information Sciences, Available online 6 March 2019

Energy Detection in Cognitive Radio Network under Rayleigh and Nakagami-m Fading Channels,
Shirin Akhter, Md. Imdadul Islam, M. R. Amin, ‘Energy Detection in Cognitive Radio Network under Rayleigh and Nakagami-m Fading Channels’ International Journal of Computer Science and Information Security, vol. 17, no. 2, pp. 132-136, FEB 2019

Cooperative Relayed Network under Rayleigh and Nakagami-m Fading Channel, Channels International Journal of Computer Science and Information Security,
Sarwar Jahan, Md. Imdadul Islam, M. R. Amin, ‘Cooperative Relayed Network under Rayleigh and Nakagami-m Fading Channel,’ Channels’ International Journal of Computer Science and Information Security, vol. 17, no. 1, pp. 101-108, JAN 2019

Md. Rafsan jani and Md. Imdadul Islam, De-noising and Feature Extraction of ECG and EEG Signal Using Adaptive Algorithm and Wavelet Transform',
 Jahangirnagar University Journal of Science, vo.41, no.1, pp. 43-56, June’2018

Md Abul Kalam Azad, Sanjit Kumar Saha, Md. Imdadul Islam, Jugal Krishna Das, 'Detection of Primary User at Fusion Center of a CRN Using Fuzzy-Logic Rules',
‘Detection of Primary User at Fusion Center of a CRN Using Fuzzy-Logic Rules,’ International Journal of Computer Science and Information Security, vol. 16 no. 8 AUG 2018,  pp. 84-92
 

Abul Kalam Azad, Jugal K. Das, Imdadul Islam, 'Signal Detection of Co-Operative Cognitive Radio Network under Neural Network',
‘Signal Detection of Co-Operative Cognitive Radio Network under Neural Network,’ Journal of Computer and Communications, vol.6, no.9, pp. 60-72, September 2018

 

Md. Imran Hosen, Tahsina Tabassum, Jesmin Akhter and Md. Imdadul Islam, Detection of Fruits Defects Using Colour Segmentation Technique, International Journal of Computer Science and Information Security, Vol. 16 No. 6, pp. 215-223 JUNE 2018,
Detection of Fruits Defects Using Colour Segmentation Technique

Abu Sayed Md. Mostafizur Rahaman, Jesmin Akhter, Md. Rafsan Jani and Md. Imdadul Islam Determination of Array Gain of Single Hop to Achieve the Performance of a 2-Hop Wireless Link, Journal of Computer and Communications, Volume 6, Number 7, pp.84.98, July 2018,
Determination of Array Gain of Single Hop to Achieve the Performance of a 2-Hop Wireless Link

Human Face Detection Based on Combination of Logistic Regression, Distance of Facial Components and Principal Component Analysis,
Anup Majumder,  Md. Mezbahul Islam, Rahmina Rubaiat, Md. Imdadul Islam , ‘Human Face Detection Based on Combination of Logistic Regression, Distance of Facial Components and Principal Component Analysis,’ International Journal of Computer Science and Information Security, Vol. 16 No. 2 FEB’ 2018, pp.34-41

 

Recovery of RGB Image from Its Halftoned Version based on DWT,
Tasnim Ahmed, Md. Imdadul Islam and Md. Habibur Rahman,  International Journal of Computer Science and Information Security, vol. 16 no. 4,   pp. 145-150, APR 2018

Selection of Antenna Elements of AAS Based on Simulation of RWG Edge Elements,
Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam, ‘Selection of Antenna Elements of AAS Based on Simulation of RWG Edge Elements,’ Jahangirnagar University Journal of Science, vol. 40, no.2, pp.15-29, 2018

Human Face Detection Based on Combination of Logistic Regression, Distance of Facial Components and Principal Component Analysis,
Anup Majumder,  Md. Mezbahul Islam,  Rahmina Rubaiat and  Md. Imdadul Islam, International Journal of Computer Science and Information Security, vol. 16,  no. 2,  pp. 34-41, FEB 2018

CONFERENCE PAPER
T. Afrose, M. Hossen and Md. Imdadul Islam, ‘Heart Diseases Prediction Using Multiple Machine Learning Techniques, 2022 4th International Conference on Sustainable Technologies for Industry 4.0 (STI), pp.1-5, Dhaka, Bangladesh, December 2022.
Heart Diseases Prediction Using Multiple Machine Learning Techniques

M. Khatun, M. I. Islam, P. Chakraborty, T. Ahmed, A. Sarker and M. Shamim-Ul-Islam, Secrecy Capacity via Cooperative Transmitting under Rayleigh and Nakagami-m Fading Channel, 2020 IEEE Region 10 Symposium (TENSYMP), pp.82-85, Dhaka, Bangladesh, June 2020. doi: 10.1109/TENSYMP50017.2020.9230615
IEEE Region 10 

Impact of SUs under FC in Co-operative Cognitive Radio Network in PUEA Environment,
Fahmida Hossain, AnzumanYeasmin Snigdha and Md. Imdadul Islam, ‘Impact of SUs under FC in Co-operative Cognitive Radio Network in PUEA Environment,’ 2019 1st International Conference on Advances in Science, Engineering and Robotics Technology (ICASERT), 3-5 May 2019,  Dhaka, Bangladesh

Comparison of Performance of Cognitive Radio Network under Single and Multi-User Scenario,
Md Abul Kalam Azad,  Md. Imdadul Islam,  Muhammad R. A. Khandaker and  Jugal K. Das, ‘Comparison of Performance of Cognitive Radio Network under Single and Multi-User Scenario,’  2019 1st International Conference on Advances in Science, Engineering and Robotics Technology (ICASERT), 3-5 May 2019,  Dhaka, Bangladesh

Optimum cell-Site Positioning Model for Cellular Network by Grid line Shifting Method,
Md. Imdadul Islam and S. Hossain,  IEEE Region 10 Conference' TENCON', vol.1, pp.1-3, 1999

Optimum Cell-site Positioning Model for Cellular Network by Linear Regression of Coverage Border,
Md. Imdadul Islam and S. Hossain,  TENCON'2000, Kuala Lumpur, pp. 191-194,  25-27 Sept'2000. 0-7803-6355-8/00/$10.00(C) 2000 IEEE

Analysis of Two Dimensional Limited Source and Mixed Traffic Model for a BTS of a Small Mobile Cellular Network,
Imdadul Islam, Q. Maula and L. J. Rozario, International Conference on Computer and Information Technology 2001, ICCIT2001, University of Dhaka, Dhaka, In Cooperation with IEEE in Bangladesh. pp. 190-196, Dec’2001, http://iccit2001.starbd.net, ISBN 984-32-015-2

Overflow traffic of limited trunk and limited source network for alternate routing,
Md. Imdadul Islam, S. Hossain and L. J. Rozario, 5th ICCIT, EastWest University, pp. 288-292, Dec’ 2002

Structures of Multilevel Scheme of Mealy Automata on PLA,
J. K. Das and Md. Imdadul Islam, International Conference on Computer and Information Technology 2003,  ICCIT2003, pp. 192-196, Jahangirnagar University, Dhaka, In Cooperation with IEEE in Bangladesh

A Proposed 2-D Queuing Model of PCT-I traffic,
S. Hossain and Md. Imdadul Islam,  International Conference on Computer and Information Technology 2003, ICCIT2003, pp. 114-118,  Jahangirnagar University, Dhaka, In Cooperation with IEEE in Bangladesh

Analytical Model of traffic performance of mobile Cellular Network in Underlay Over lay Cell System,
Md. Imdadul Islam and S. Hossain,  International Conference on Computer and Information Technology 2003, ICCIT2003, pp. 230-234, Jahangirnagar University, Dhaka, In Cooperation with IEEE in Bangladesh

Simulation and Analysis of 2-D PCT-II Traffic Model for Mobile Cellular Network,
Md. Imdadul Islam and S. Hossain,  6th International Conference on Computer and Information Technology 2003, ICCIT2003, pp. 676-679, Jahangirnagar University, Dhaka, In Cooperation with IEEE in Bangladesh

Analysis of Radiation Pattern of Two Dimensional Array Antenna System,
Imdadul Islam, B. Alam and N. Sultana,  7th ICCIT, 2004, BRAC University, pp. 744-747, Dec’2004

A theoretical analysis of SDMA traffic of limited user network for DL case,
Shahid Hossain and Imdadul Islam,  7th ICCIT, 2004, BRAC University, pp. 728-732, Dec’2004

Modeling of M/M/n/K traffic for LEO mobile satellite systems,
M. F. Azam and Imdadul Islam,  7th ICCIT, 2004, BRAC University, pp.2652-267,  Dec’2004

Enhancement of throughput of wireless channel based on newly designed constellation of QAM under AWGN environment,
Imdadul Islam, F. H. Bhuiyan and N. I. Patwary,  7th ICCIT, 2004, BRAC University, pp.247-250, Dec’2004

Implementation of FIR Filter Based on Newly Designed Window Function,
Imdadul Islam, B. Alam and N. Sultana, International Conference on Computer and Information Technology 2004, ICCIT2004, BRAC University, Dhaka, pp.768-771,  In Cooperation with IEEE in Bangladesh, Dec’2004

Reverse Link Capacity of a CDMA Cellular System Based on General Path Loss Model,
Imdadul Islam, M. R. Hasan and M. R. Amin,  ICECE-2004, pp. 359-261, under IEEE, BUET, Dhaka

A Proposed Random Walk Model for Mobile Cellular Network,
Imdadul Islam and S. Hossain, ICECE-2004, under IEEE, BUET, pp. 386-389, Dhaka 2004

Theoretical Modeling of Traffic of Multilayer Cell of 3G Mobile Cellular Network,
Imdadul Islam and S. Hossain,  IEEE TENCON 2004, Chiang Mal, Thailand

Channel Allocation of Mobile Cellular Network Based on Graph Theory,
Imdadul Islam and S. Hossain, IEEE TENCON 2004, Chiang Mal, Thailand

A Proposal in Improvement of Connection Reestablishment of Ad-Hoc Mobile Cellular Network,
Imdadul Islam and S. Hossain,  Global Mobile Congress, GMC'2004, Shanghai, China

Analysis of SDMA PCT-II Traffic for Duplicated First Case A Theoretical Study,
S. Hossain and Imdadul Islam,  2005 International Conference on Wireless Communications, Networking and Mobile Computing, Wuhan, China, pp.423-426, Sept. 23-26, 2005

Performance Analysis of Wireless Mobile IP Network Based on RSVP,
Imdadul Islam, F. H. Bhuiyan and N. I. Patwary,  pp.791-795, ICCIT’2005, IUT, Dhaka

Performance analysis of multiple antennas BS and single antenna MS link of mobile cellular network,
M. S. Karim, Imdadul Islam and S. Hossain,  The Third International Conference on Wireless and Optical Communications Networks WOCN, Bangalore, India, 1-4244-0340-5/06/$20.00@2006 IEEE,  April, 2006

Modeling of random access channel for limited user network,
M. S. Karim, Imdadul Islam and S. Hossain,  The Third International Conference on Wireless and Optical Communications Networks WOCN, Bangalore, India, 1-4244-0340-5/06/$20.00@2006 IEEE,  April, 2006

Call admission scheme of voice data integrated traffic of mobile cellular network under DCA environment,
M. S. Karim, Imdadul Islam and S. Hossain,  The Third International Conference on Wireless and Optical Communications Networks WOCN, Bangalore, India, 1-4244-0340-5/06/$20.00@2006 IEEE,  April, 2006

Performance Analysis of Rake Receiver under AWGN Environments,
Imdadul Islam, S. Hossain and M. Zulhasnine,  Proceedings of the Int. Conf. on Computer and Communication Engineering, ICCCE’06, Vol. II, 9-11, pp.796-800, May 2006, Kuala Lumpur, Malaysia

A Simplified Traffic Model of Mobile Cellular Network with Customer Retrial,
Imdadul Islam and S. Hossain,  Proceedings of the Int. Conf. on Computer and Communication Engineering, ICCCE’06 Vol. II, 9-11, pp. 740-744,  May 2006, Kuala Lumpur, Malaysia

Wideband Beam forming of Array Antenna at Desired Directions Based on Direct Mathematical Model,
M. S. Karim, Imdadul Islam and S. Hossain,  Proceedings of the Int. Conf. on Computer and Communication Engineering, ICCCE’06 Vol. II, pp.710-714,  9-11 May 2006, Kuala Lumpur, Malaysia

Performance Analysis of Wireless Mobile TCP Network,
Imdadul Islam and S. Hossain,  The 8th International Conference on Advanced Communication Technology 2006, February 20 ~ 22, 2006, Phoenix Park, Republic of Korea,

A New Call Admission Control in 3G Mobile Cellular Network,
Imdadul Islam and S. Hossain,  The 8th International Conference on Advanced Communication Technology 2006, February 20~22, 2006, Phoenix Park, Republic of Korea,

Extraction of Biomedical Signals in Noisy Environment,
Imdadul Islam, M. Zulhasnine, J. K. Das and S. Karim,  9th International Conference on Computer and Information Technology (ICCIT-2006), IUB, Dhaka 2006

Throughput Optimization of Multi-user Wireless link,
M. F. Islam, Imdadul Islam and M. R. Amin,  9th International Conference on Computer and Information Technology (ICCIT-2006), pp.460-463, IUB, Dhaka 2006

Adaptive beamforming of linear Array antenna system with provision of side lobe cancellation,
M.R.A. Khandaker, Imdadul Islam and M. R. Amin, 10th ICCIT, UIU, pp.1-4, 2007

Optimization of k-fold multicast wireless network using M/M/n/n+q traffic model,
Asfara R. Towfiq, N.A. Siddiky, Md. Imdadul Islam and M. R. Amin, 5th ICECE, pp.493-496, BUET, Dhaka 2008

Performance evaluationof DOVE of a voice/data integrated wireless mobile network,
H.M. Rahat, Runa Lila, Sabiha Rahman Juthy, Md. Imdadul Islam and M. R. Amin, 11th ICCIT, pp.85-88, KUET, 2008

Evaluation of Traffic Parameters of Multidimensional Traffic of a Combined Link Using a Tabular Method,
Md. Imdadul Islam,  Md. Shahriar Karim, J. K. Das and M. R. Amin, pp.161-165,  ICCIT 2008, KUET, Bangladesh

Capacity enhancement of limited user traffic of mobile cellular networks using DOVE Technique,
Md. Omar Faruq, Md. Arifur Rahman, Md. Imdadul Islam and M. R. Amin,  12th ICCIT, pp. 56-60, Dec’2009

A modified MAP in performance evaluation of asynchronous packet traffic,
Anupam Roy, Md. Jweel Hossain and Md. Imdadul Islam,  12th ICCIT, pp. 70-73, Dec’2009

Evaluation of performances of digital adaptive filter in acoustic echo cancellation,
Md. Anamul Haque, A.K.M. Kamrul Islam and Md. Imdadul Islam,  12th ICCIT, pp. 215-219, Dec’2009

Adaptive array antenna system in cancellation of jammer and noise of wireless link,
Md. Imdadul Islam, Md. Golam Gaus, Avijeet Das, Mushlah Uddin Sarker and M. R. Amin,  12th ICCIT, pp. 321-326, Dec’2009

Performance evaluation of MIMO system incorporating water filling model and minimum eigenvalue constraints,
Nur Afroza Khurshid, Md. Imdadul Islam and M. R. Amin, 12th ICCIT, pp. 675-678, Dec’2009

‘Performance evaluation of a mobile cellular network with two hop Ad-Hoc relaying,
Nusrat Sultana, M.A. Jobayer Bin Bakkre, Md. Imdadul Islam and M. R. Amin, 12th ICCIT, pp. 685-690, Dec’2009

Performance evaluation of time dependent micro macro cellular network using MMPP traffic,
Mushlah Uddin Sarker, Md. Imdadul Islam and M. R. Amin, 12th ICCIT, pp. 460-464, Dec’2009

Performance Evaluation of Multidimensional Traffic in Micro-Macro Cellular System,
Sarwar Jahan, Md. Imdadul Islam, and M. R. Amin,  Proceedings of 13th International Conference on Computer and Information Technology (ICCIT 2010), 23-25 December, 2010, Dhaka, Bangladesh

Fingerprint Detection Using Canny Filter and DWT, a New Approach,
Md. Imdadul Islam, Nasima Begum, Mahbubul Alam and M.R. Amin,  Proceedings of 13th International Conference on Computer and Information Technology (ICCIT 2010), 23-25 December, 2010, Dhaka, Bangladesh

Performance comparison of Bow-Tie and Slot Antenna Based on RWG Edge Elements,
Md. Asif Hossain, Mushlah Uddin Sarkar, Md. Imdadul Islam and M.R. Amin,  2nd International Conference on Computer Research and Development, Malaysia 2010

The Impact of Frequency on Radiation Pattern of Bowtie and Spiral Antenna Based on RWG Elements,
Mushlah Uddin Sarkar, Md. Asif Hossain, Md. Imdadul Islam  and M.R. Amin,  2010 2nd International Conference on Electronic Computer Technology (ICECT 2010), Malaysia 2010

Cost Based Performance Evaluation of M/G/1/K Traffic Model,
Jesmin Akhter1 and Md. Imdadul Islam,  Accepted for Proceedings of 14th International Conference on Computer and Information Technology (ICCIT 2011), pp.303.308,  December, 2011, Dhaka, Bangladesh

Reduction of ICI in OFDM Using Window Functions,
Md. Al- Mahadi Hasan, Shoumik Das, Md. Imdadul Islam and M. R. Amin,  2012 7th International Conference on Electrical and Computer Engineering, pp.303-306, 20-22 December,  2012, Dhaka, Bangladesh, 978-1-4673-1436-7/12/$31.00 ©2012 IEEE

Determination of Energy Efficiency of a Multi-user Wireless Network Based on Limited User Traffic Model,
Md. Nurul Islam, Shamim, Ahmed, Ummy Habiba, Md.Imdadul Islam and M. R. Amin, 8th International Conference on Electrical and Computer Engineering, pp.406 – 408, 2014, 20-22 Dec’ 2014, Dhaka, Bangladesh

Performance Analysis of MIMO Link under Fading Channels,
Tahsina Hashem and Md. Imdadul Islam, 17th International Conference on Computer and Information Technology (ICCIT), pp. 498-503, Dec’ 2014, Dhaka, Bangladesh

A Simplified Image Compression Technique Based on Haar Wavelet Transform,
Fahima Tabassum, Md. Imdadul Islam, 2nd International Conference on Electrical Engineering and Information Communication Technology (ICEEICT 2015) under IEEE Bangladesh section, May 21-23, Jahangirnagar University, Dhaka, Bangladesh

Comparison of Cyclostationary and Energy Detection in Cognitive Radio Network,
Risala. T. Khan, Shakila zaman, Md.Imdadul Islam, and M. R. Amin, ‘Comparison of Cyclostationary and Energy Detection in Cognitive Radio Network’,2016 International Workshop on Computational Intelligence (IWCI) 12-13 December 2016, pp.165-168, Dhaka, Bangladesh

Traffic Modelling of WiMAX under BMAP with Length of Packet of General Distribution,
Jesmin Akhter,  Md.Imdadul Islam, and M. R. Amin, ‘Traffic Modelling of WiMAX under BMAP with Length of Packet of General Distribution’ 9th International Conference on Electrical and Computer Engineering 20-22 December, 2016, pp.78-81,Dhaka, Bangladesh

Traffic Modelling of Low Dense Femtocellular Network,
Jesmin Akhter, Md. Imdadul Islam, and M. R. Amin,’ Traffic Modelling of Low Dense Femtocellular Network’ 9th International Conference on Electrical and Computer Engineering 20-22 December, 2016, pp.74-77, Dhaka, Bangladesh

Digital Watermarking Using Discrete Wavelet Transform and Eigen Decomposition,
Swarna Das,  Mohtasim Bellah,  Md. Imdadul Islam, ‘Digital Watermarking Using Discrete Wavelet Transform and Eigen Decomposition,’ 2019 International Conference on Electrical, Computer and Communication Engineering (ECCE), 7-9 Feb. 2019, Cox'sBazar, Bangladesh


"""

# Regular expression to match author list and title
pattern = r"^(.+?), (.+?), .+?\. doi:"  # Captures authors and title

# Extract matches
matches = re.findall(pattern, text, re.MULTILINE)

# Save data to a CSV file
with open('author_title_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Authors', 'Title'])  # Write the header
    for authors, title in matches:
        writer.writerow([authors.strip(), title.strip()])

print("Data saved to author_title_list.csv")
