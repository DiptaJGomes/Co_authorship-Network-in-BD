import csv
import re

# Provided text
text = """
[1] Logic scheme Optimizsation of Mealy Automata on  PLA. “Automatics  and Computer Science”- . Riga, 1991,  p.90-94 (Russ).

[2] Logic scheme Optimization of Mealy Automata on PLA.” Cybernetics and System analysis”.  – Kiev, 1991, No. 5, P. 180-184 (Russ.)

[3] Optimization of logic condition forming scheme in matrix realization of automata. ”Microprocessor Systems and their uses”- Kiev, 1990, P. 29-34 (Russ.).

[4] PR-Automata: Functions, Optimization, Selection of Synthesizing Method. "A Methodical mini guide.” – Kiev. IC, 1991, 26P (Russ).

[5] Systematic Instructions for Solving Problems on the course: “Applied Theory of Digital Automata”. – Donetsk. DPI, 1999, 25P (Russ).

[6] Computer Aided Design for Control unit based on matrix LSI “CI-90.” All-Union Scientific Technical Seminar on “CAD in Radio Electronics.”-Tver , 1991. P. 7-8(Russ.).

[7] Development and investigation of the multilevel realization of microprogarmmed automata on programmable large scale integration scheme with matrix structure, Ph.D. thesis resume, Kiev, 1993.141P (Russ.).

[8] Minimization of Microprogram automaton ( Sequential Machine) using programmable logic arrays (PLA). “Jahangirnagar University Journal of Science”. – Dhaka, Vol. 19, 1995, P. 65-70.

[9] Software Panorama: A case study for Bangladesh. “National Conference on Computer and  Information Systems. –Dhaka, 1997, P.16-21.

[10] Minimization of Hardware cost for the synthesis of Mealy Automata using programmable logic arrays. “Bangladesh Journal of Computer and Information Technology”. – Dhaka, Vol. 7, No.1, 2000, P.34-38.

[11] Design and Software Implementation of Traffic Signaling. “Jahangirnagar University Journal of Science”. – Dhaka, Vol. 24, 2001, P.77-84.

[12] Optimization of Microprogrammed Automata Scheme for the input Variables Replacement Method.-ICCIT, Dhaka, Vol. 1,2003,P.104-108.

[13] Structures of Multilevel Scheme of Mealy Automata on PLA.-ICCIT,Dhaka,Vol.1,2003,P.192-196.

[14] Implementation of Virtual Ethernet LAN -ICCIT, Dhaka, Vol.1, 2003 P.431-435,

[15] Anthropocentric and tecnocentric systems for intellectual  controlling –Bulletin Donetsk  University, Ukraine, Series A, No.1, page 434-438, 2005.

[16] Proposed framework for information security management with its significant for an organization, Journal of electronics and computer science, J.U., vol. 6, 2005.

[17] A Newly Designed Markovian Chain for    Packet Data Traffic,’ Jahangirnagar University Journal of Science, vol.29, pp.63-68,  Dec’2006

[18] A Mathematical Model of Traffic Performance  of Mobile Cellular Network,' Journal of  Electronics and Computer Science, vol.8,   pp.1-9, June 2007.

[19] Modeling of Mixed  Traffic for Mobile Cellular Network,’ Journal of Telecommunications and Information Technology, vol. 1/2007, pp. 83-89, Szachowa st, 04-894, Warsaw, Poland.

[20] Modeling of Voice Data  Integrated Traffic in 3G Mobile Cellular Network,’ Journal of  Telecommunications   and Information Technology, vol. 2/2007, pp. 103-108, Szachowa st, 04-894, Warsaw, Poland.

[21] Performance Evaluation of Wireless ATM Network Based on Two States Absorbing Markovian Chain,’ Jahangirnagar University Journal of Science, vol.30, No.2, 215-228, Dec’2007.

[22] Performance Evaluation of    Underlay Overlay Cellular System Based on Equivalent Random Theory Traffic  Model,’ , Journal of Science, University of Dhaka.

[23] M.N.Y. Ali, J.K. Das,  S.M. Abdullah  Al  Mamun, M.E.H. Choudhury, “Specific  Features of a Converter of Web Documents from Bengali to Universal Networking   Language”, International Conference on Computer and Communication Engineering 2008 (ICCCE’08), Kuala Lumpur, Malaysia.pp. 726-731 

[24] M.N.Y. Ali, J.K. Das, S.M. Abdullah Al Mamun, A. M. Nurannabi,”Morpholoical     Analysis of Bangla worfs for Universal Networking Language”, International Conference on Digital Information Management, icdim, 2008, London, England, pp. 532-537

[25] M.N.Y. Ali, M. Ameer Ali,  A. M. Nurannabi, J.K. Das, “Algorithm for Conversion of Bangla Sentence to Universal Networking Language, ”International Conference on Asian Language Processing 2010  (IALP’10), Haribin, China,  December 28-30,2010 

[26] M.N.Y. Ali, M. Z. H. Sarker, G.A. Farook, J.K. Das, “Rules for Morphological Analysis of Bangla Verbs for Universal Networking Language, ”International Conference on Asian Language Processing 2010  (IALP’10), Haribin, China,  December 28-30,2010 

[27] M.N.Y. Ali, S. Al Noor, M. Z. Hossain, J.K. Das, “Development of Analysis Rules for Bangla Root and Primary Suffix for Universal Networking Language, ”International Conference on Asian Language Processing 2010  (IALP’10), Haribin, China,  December 28-30, 2010 

[28] M. Z. Hossain, M.N.Y. Ali, S. M. Allayear, J.K. Das, “Development of Templates for Dictionary Entries of Bangla Roots and Primary Suffixes for Universal Networking Language, ”International Conference on Asian Language Processing 2010  (IALP’10), Haribin, China,  December 28-30, 2010 

[29] M.N.Y. Ali, A. M. Nurannabi, M. Ameer Ali, J.K. Das, “Conversion of Bangal Sentence for Universal Networking Language, ”International Conference on Computer and Information Technology,  December 23-35, 2010 

[30] M. N. Y. Ali, Md. Z. H. Sarker, J. K. Das, “Analysis and Generation of Bengali Case Structure Constrcts for Universal Networking Language’’, IJCA International Journal of Computer Applications, March, 2011.

[31] M. N. Y. Ali, Md. Z. H. Sarker G. F. Ahmed, J. K. Das, “Conversion of Bangla Sentence into Universal Networking Language Expression’’, IJCSI International Journal of Computer Science Issues, Vol. 8, Issue 2, March 2011.

[32] Aloke Kumar Saha, Jugal Krishna Das, “Identification of Extreme Guilt and Grave Fault in Bengali Language using Machine Learning”, International Journal of Recent Technology and Engineering (IJRTE), (SCOPUS Indexed International Journal), Vol. 8, No. 6, ISSN: 2277-3878, pp. 1359-1365, March 2020. 

[33] Aloke Kumar Saha, M.F. Mridha, Jahir Ibna Rafiq, Jugal K Das, “Information Extraction from Natural Language Using Universal Networking Language”, International Conference on Computer, Communications and Computational Studies (IC4S), Thailand, October 2018. 

[34] Aloke Kumar Saha, M. F. Mridha, Jahir Ibna Rafiq and Jugal Krishna Das, “Data Extraction from Natural Language Using Universal Networking Language”, International Conference on Current Trends in Computer, Electrical, Electronics and Communication (ICCTCEEC), Karnataka, India, September 2017. (IEEE Xplore )

[35] Aloke Kumar Saha, M. F. Mridha, Jugal Krishna Das,“ Creating a  Bangla Enconversion  Module for Generating UNL Expression from Bangla  Bagdhara (Phrase and Idoms)”, 1292-JEAS, Journal Teknologi, April 2017.

[36] M. F. Mridha, Aloke Kumar Saha, Md. Akhtaruzzaman Adnan, Molla Rashied Hussein and Jugal Krishna Das,”Design And Implementation Of An Efficient Enconverter For Bangla Language” ARPN Journal of Engineering and Applied Sciences, Vol. 10, No. 15, ISSN 1819-6608, pp. 6543-6548, August 2015.

[37] Aloke Kumar Saha, Md. Firoz Mridha, Molla Rashied Hussein and Jugal Krishna Das, “Design and Implementation of an efficient DeConverter for generating Bangla sentences from UNL Expression”, 4th International Conference on Informatics, Electronics & Vision (ICIEV), June 2015.

[38] Muhammad F. Mridha, Aloke Kumar Saha and Jugal Krishna Das, “New Approach of Solving Semantic Ambiguity Problem of Bangla Root Words Using Universal Networking Language (UNL)”, 3rd International Conference on Informatics, Electronics & Vision (ICIEV), May 2014.

[39] Aloke Kumar Saha, Muhammad F. Mridha and Jugal Krishna Das, “Analysis of Bangla Root words for Universal Networking Language (UNL)”, International Journal of Computer Applications (0975 – 8887) Vol. 89, March 2014.

[40] Muhammad F. Mridha, Aloke Kumar Saha and Jugal Krishna Das, “Solving Semantic Problem of Phrases in NLP Using Universal Networking Language (UNL)”, International Journal of Advanced Computer Science and Applications (IJACSA), Special Issue on Natural Language Processing (NLP), 2014. 

[41] Aloke Kumar Saha, Muhammad F. Mridha, Shammi Akhtar and Jugal Krishna Das, “Attribute Analysis for Bangla Words for Universal Networking Language (UNL)”, International Journal of Advanced Computer Science and Applications (IJACSA), Vol. 4, No.1, 2013.

[42] Aloke Kumar Saha, Muhammad F. Mridha and Jugal Krishna Das, “Semantic Analysis of Bangla Language for Developing A UNL Deconverter”, International Journal of Advanced Research in Computer Science and Software Engineering (IJARCSSE), ISSN: 2277 128X, Vol. 2, No. 12, December 2012.

[43] Aloke Kumar Saha, Muhammad F. Mridha, Kamal Kanti Biswas, and Jugal Krishna Das, “A New Approach of Developing a Deconverting rules for Bangla Language”, International Journal of Computer Engineering Science (IJCES), ISSN: 2250:3439, Vol. 2, No. 12, December 2012.

[44] Aloke Kumar Saha, Muhammad F. Mridha, Manoj Banik, and Jugal Krishna Das, “Specification of UNL Deconverter for Bangla Language”, International Journal of Scientific & Engineering Research (IJSER), ISSN: 2229-5518, Vol. 3, No. 9, September 2012.

[45] M. F. Mridha, Molla Rashied Hussein, Md. Musfiqur Rahaman, Jugal Krishna Das “A Proficient Autonomous Bangla Semantic Parser for Natural Language Processing”, ARPN Journal of Engineering and Applied Sciences, VOL. 10, NO. 15, AUGUST 2015,ISSN 1819-6608, pp 6398-6403. (SCOPUS)

[46] Muhammad Firoz Mridha, Manoj Banik, Md. Nawab Yousuf Ali, Mohammad Nurul Huda, Chowdhury Mofizur Rahman, Jugal Krishna Das, “Formation of Bangla Word Dictionary Compatible with UNL Structure,” SKIMA’10, Paro, Bhutan, August, 2010.

[47] Muhammad Firoz Mridha, Md. Zakir Hossain, Manoj Banik, Mohammad Nurul Huda, Chowdhury Mofizur Rahman, Jugal Krishna Das, “ Development of Grammatical Attributes for Bangla Root and Primary Suffix for Universal Networking Language,” SKIMA’10, Paro, Bhutan, August, 2010.

[48] Muhammad Firoz Mridha, Mohammad Nurul Huda, Chowdhury Mofizur Rahman, Jugal Krishna Das, “Development of Morphological Rules for Bangla Root and Verbal Suffix for Universal Networking Language”. 6th International Conference on Electrical and Computer Engineering,ICECE 2010, 18-20 December 2010, Dhaka, Bangladesh. (IEEE Xplore )

"""

# Regex pattern to extract authors and titles
pattern = r"\[\d+\]\s*(.*?),\s*“(.*?)”"

# Extract matches
matches = re.findall(pattern, text)

# Save to CSV
with open('authors_titles_ju.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Authors'])  # Write header
    for title, authors in matches:
        writer.writerow([title.strip(), authors.strip()])

print("research_data_ju.csv")