import re
import csv

# Input text
text = """
Abu Sayed Md Mostafizur Rahaman, Saiyeda Marzia, Tafsir Haque Arnob, Md Zahidur Rahman, Jesmin Akhter, Forensic Artifact Discovery and Suspect Profiling through Google Assistant, Mobile and Forensics, 5, 1, USA, 2023. doi: https://doi.org/10.12928/mf.v5i1.8046
Deepon Deb Nath, Shivazi Biswas, Jesmin Akhter, Abu Sayed Md Mostafizur Rahaman, A Hybrid Approach for Android Malicious Software Classification, Computing Open, 1, pp.233, 2023. doi: https://doi.org/10.1142/S2972370123300029
Musaddik Habib Shirsho, Md Masud Rana, Jesmin Akhter, Abu Sayed Md Mostafizur Rahaman, Enhancing Image Manipulation Detection through Ensemble ELA and Transfer Learning Techniques, International Journal of Computing and Digital Systems, 16, 1, pp.1-11, University of Bahrain, 2024. doi: http://dx.doi.org/10.12785/ijcds/XXXXXX
Abu Sayed Md. Mostafizur Rahaman Khaled Redwan, Jesmin Akhter, Forensic Tools for Windows Forensic Analysis: A Comprehensive Review, International Journal of Research Publication and Reviews, 5, 5, pp.5483-5490, 2024.
Tasfia Zaima, Tabassum Ibnat Ena, Tamim Ikbal, Abu Sayed Md Mostafizur Rahaman, Demystifying IoT Network Intrusion Detection: Assessing ML Algorithms with the Aid of Explainable AI, International Journal of Computing and Digital Systems, 16, 1, pp.1-13, University of Bahrain, 2024. doi: http://dx.doi.org/10.12785/ijcds/XXXXXX
MM Hasan, MM Rana, ASMM Rahaman, Insights into Manipulation: Unveiling Tampered Images Using Modified ELA, Deep Learning, and Explainable AI, Journal of Computer and Communications, 12, 6, pp.135-151, Scientific Research Publishing, 2024. doi: 10.4236/jcc.2024.126009
Bezier Curve as an Efficient Off-Line Path Planner,
Md. Abdur Rahman, Abu Sayed Md. Mostafizur Rahaman, Abeda Sultana, Jesmin Akhter, "Journal of Mathematics and Mathematical Sciences", v-19, p. 63-72, 2004.

Justification of High Spectral Efficiency of VPSK Digital Modulation,
Md. Abdur Rahman, Abu Sayed Md. Mostafizur Rahaman, Abeda Sultana, Jesmin Akhter, "Journal of Mathematics and Mathematical Sciences", v-19, p. 35-42, 2004.

Reliable Modulation method in PLC Communication for Home Network,
Abu Sayed Md. Mostafizur Rahaman, Akram Hossain, Jahangirnagar University Journal of Science, v-28, December, 2005.

Performance Evaluation of Two-hop Wireless Link under Rayleigh and Nakagami-m Fading Channel for 8-PSK and 16-QAM,
Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam, M.R. Amin", IACSIT International Journal of Engineering and Technology, Vol. 3, No.5, October 2011

Application of Zero-Forcing Adaptive Equalization in Compensation of Fading Effect of Two-hop Wireless Link,
Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam, M.R. Amin,IACSIT International Journal of Engineering and Technology, pp. 628-633, Vol. 3, No. 6, Singapore, 2011.

Array Antenna System of Frequency Independent Antennas Based on RWG Elements,
Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam, M.R. Amin, JOURNAL OF ELECTRONICS AND COMPUTER SCIENCE RESEARCH, VOL. 2 NO. 1, 20 APRIL 2013

Impact of Geometry and Feed Point on Radiation Pattern of a Patch Antenna and Its Linear Array as a Substitute of Multi-hop Link,
Abu Sayed Md. Mostafizur Rahaman, Jesmin Akhter, Md. Imdadul Islam, M.R. Amin, Jahangirnagar University Journal of Electronics and Computer Science and Engineering, Vol. 15, pp. 7-15, June 2014, Bangladesh

Selection of the best two-hop AF wireless link under multiple antenna schemes over fading channel,
Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam, M.R. Amin, Journal of Information Processing System (JIPS), Volume: 11, No: 1, Page: 57 ~ 75, 2015, Republic of Korea.

Traffic Modeling of Finite Queue and General Service Time Distribution,
Md. Imdadul Islam, Md. Zahirul Islam, Abu Sayed Md. Mostafizur Rahaman, Israt jahan."Jahangirnagar University Journal of Science", V-38, No. 2, pp-23-34, 2015

Adaptive Beamforming and Cancellation of Jammer using Linear Array Antenna System,
 Israt Jahan, Md. Imdadul Islam and Abu Sayed Md. Mostafizur Rahaman,"International Journal of Engineering Sciences & Research Technology", V-4, Issue 4, 648-657, April 2015

Scientific Journal Impact Factor: 3.449

(ISRA), Impact Factor: 2.114

Pattern Recognition Using the Concept of Disjoint Matrix of MIMO System,
Md. Imdadul Islam, Rahmina Rubaiat,  Md. Mezbahul Islam and Abu Sayed Md. Mostafizur Rahaman, "International Arab Journal of Information Technology (IAJIT)", vol. 14, no. 4, July 2017

Impact Factor for IAJIT: 0.519

IAJIT is indexed by: ELSEVIER and Thomson Reuters

The MIMO Performance of LTE Network under Rayleigh Fading Environment ,
Jesmin Akhter, Md. Imdadul Islam, ASM M Rahaman, M R Amin, "International Journal of Computer Science and Information Security", Vol. 14 No. 8, pp. 88-94, AUGUST 2016 

Thomson Reuters

Resource Management of Mobile Communication System,
Dewan Md. Mostafezur Rahman, Md. Imdadul Islam, Abu Sayed Md. Mostafizur Rahaman, Mohammad Shorif Uddin, Md. Akram Hossain, "International Journal of Advanced Engineering Research and Science (IJAERS)", Vol-3,Issue-8,August 2016,  Thomson Reuters ResearcherID: P-3738-2015

 ISRA JIF-1.317| PIF-2.465|IBI-3.2|SJIF-4.072

Traffic Modeling of Mobile Cellular Network Using Combination of Limited and Unlimited User Groups ,
Dewan Md. Mostafezur Rahman, Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam,  Mohammad Shorif Uddin and Md. Akram Hossain, "International Journal of Computer Science and Information Security", issue  (Vol. 14 No. 10), October 2016, IJCSIS ISSN 1947-5500, Pittsburgh, PA, USA

Thomson Reuters

Performance Evaluation of Femtocell Based LTE Network under the Concept of Cross-layer Optimization,
Jesmin Akhter, Md. Imdadul Islam, ASM M Rahaman and M R Amin, ‘Performance Evaluation of Femtocell Based LTE Network under the Concept of Cross-layer Optimization,’ International Journal of Computer Science and Information Security,  (pp. 52-60), vol. 14, no. 7, July 2016

Impact of ınterferences on channel capacity of TLE mobile communication system,
Dewan Md. M Rahman, Abu Sayed Md Mostafizur Rahaman, Md. Imdadul Islam, Mohammad Shorif Uddin and Md. Akram Hossain,” Impact of ınterferences on channel capacity of TLE mobile communication system” Turkish Journal of Electrical Engineering & Computer Sciences. (Accepted)

Comparison of SNR and SIR Based Fading Models in Determination of Normalized Channel Capacity of Cooperative Cognitive Radio Network,
Md Abul Kalam Azad, Abu Sayed Md Mostafizur Rahaman, Md. Imdadul Islam, Jugal K. Das, “Comparison of SNR and SIR Based Fading Models in Determination of Normalized Channel Capacity of Cooperative Cognitive Radio Network”, International Journal of Computer Science and Information Security, Vol. 15 No. 3, pp. 56-61, MAR 2017

Human Face Recognition Using Eigen Decomposition on ROI,
Tania Khatun, Abul Kalam Azad, ASM M Rahaman, Md. Rafsan Jani and Md. Imdadul Islam, ‘Human Face Recognition Using Eigen Decomposition on ROI,’ International Journal of Computer Science and Information Security, Vol. 14 No. 12, pp. 1071-1079, DEC 2016

Performance Analysis of CSMA/CA Network using Modified State Transition Chain,
Dulal Chakraborty, Abul Kalam Azad, Md. Imdadul Islam and Abu Sayed Md. Mostafizur Rahaman, ‘Performance Analysis of CSMA/CA Network using Modified State Transition Chain,’International Journal of Computer Science and Information Security, Vol. 14 No. 12, pp. 1064-1070, DEC 2016

Determination of Array Gain of Single Hop to Achieve the Performance of a 2-Hop Wireless Link,
Abu Sayed Md. Mostafizur Rahaman, Jesmin Akhter, Md. Rafsan Jani, Md. Imdadul Islam, Vol.06 No.07(2018), Article ID:86393,15 pages 

Selection of Antenna Elements of AAS Based on Simulation of RWG Edge Elements,
Abu Sayed Md. Mostafizur Rahaman, Md. Imdadul Islam, ‘Selection of Antenna Elements of AAS Based on Simulation of RWG Edge Elements,’ Jahangirnagar University Journal of Science, vol. 40, no.2, pp.15-29, 2018
"""

# Regular expression to extract author names and titles
pattern = r"^([\w\s,\.]+?),\s([\w\s\-:()]+?),\s(?:Mobile|International|Journal|IACSIT|Jahangirnagar|Proceedings|Computing|Heliyon)", re.MULTILINE

# Find all matches
matches = re.findall(pattern, text)

# Save the results to a CSV file
csv_file = "authors_titles_ju_8.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Authors", "Title"])  # Write the header
    writer.writerows(matches)  # Write the extracted data

print(f"Data extracted and saved to {csv_file}")
