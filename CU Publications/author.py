import csv
import re

# Text content
text = """
An Efficient and Scalable Algorithm for Segmented Alignment of Ontologies of Arbitrary Size
M.H. Seddiqui, M. Aono
Elsevier, Web Semantics: Science, Services and Agents on the World Wide Web (2009), Volume 7, Issue 4, Pages 344-356, December - 2009
[Most Cited Article Award]
Object Recognition without markers for Augmented Reality Applications using Scale Invariant Feature Transform
Anjan Kumar Paul, Mohammad Khairul Islam, Young-Bum Kim, Bai-Tao Zhou, Joong-Hwan Baek
International Conference on Information and Communication Technologies (ICICT), Ulaanbaatar, Mongolia, 126-133, August - 2009
Ontology Driven IPC Based Classification of a Research Abstract
M.H. Seddiqui, M. Aono
Proceedings of IAENG International Conference on Data Mining and Applications (ICDMA09) of IMECS, Kowloon, Hong Kong, 692–697, March - 2009
[“Certificate of Merit” Award]
Object Recognition for Markerless Augmented Reality Embodiment
Anjan Kumar Paul, Hyung-Jin Lee, Young-Bum Kim, Mohammad Khairul Islam, Joong-Hwan Baek
The Journal of Korea Institute of Navigation, vol. 13, no. 1, 126-133, January - 2009
Anchor-flood: results for OAEI 2009
MH Seddiqui, M Aono
Proceedings of the ISWC 2009 Workshop on ontology matching, 127-134, 2009, 2009
Development of an effective travel time prediction method using modified moving average approach
NK Chowdhury, RPD Nath, H Lee, J Chang
International Conference on Knowledge-Based and Intelligent Information and …, 2009, 2009
Knowledge-Based and Intelligent Information and Engineering Systems: 13th International Conference, KES 2009, Santiago, Chile, September 28-30, 2009, Proceedings
JD Velásquez, SA Ríos
Springer, 2009, 2009
Development of an Effective Travel Time Prediction Method using Modified Moving Average Approach.
Chowdhury, N.K., Nath, R.P.D., Lee, H., and Chang, J.
Lecture Notes in Computer Science(), vol 5711. Springer, Berlin, Heidelberg., 13th International Conference on Knowledge-Based and Intelligent Information and Engineering Systems., 130-138, 2009
Face Detection and Recognition for Video Retrieval
Mohammad Khairul Islam, Hyung-Jin Lee, Anjan Kumar Paul, Joong-Hwan Baek
The Journal of Korea Institute of Navigation, vol. 12, no 6, 691-698, December - 2008
Person Detection and Segmentation Based on Face Localization and Region Growing for Video Indexing
Mohammad Khairul Islam, Hyung-Jin Lee, Anjan Kumar Paul, Joong-Hwan Baek
International Conference on Internet Information Retrieval, Korea Aerospace University, South Korea, 98-103, December - 2008
Privacy preserving support vector machines in wireless sensor networks
Dong Seong Kim, Muhammad Anwarul Azim, Jong Sou Park
IEEE, Third International Conference on Availability, Reliability and Security, 1260-1265, March - 2008
Alignment results of anchor-flood algorithm for oaei-2008
MH Seddiqui, M Aono
Proceedings of the 3rd International Conference on Ontology Matching-Volume 431, 120-127, 2008
Performance Comparison of Fuzzy Queries on Fuzzy Database and Classical Database
A.H.M. Sajedul Hoque, Md. Sadek Ali, Md. Aktaruzzaman Sujit Kumer Mondol, and Babul Islam
International Conference on Electrical and Computer Engineering, IEEE, 654-658, 2008
This Paper shows the comparison of Fuzzy queries on Fuzzy Database and Classical Database
Travel Time Prediction Algorithm Based on Time-varying Average Segment Velocity using Naive Bayesian Classification
Um, J., Chowdhury, N.K., Lee, H., Chang, J., and Kim, Y.
Journal of Korea Spatial System Society (KSISS), Volume 10 Issue 3 Pages.31-43, 2008
Travel Time Prediction Algorithm using Rule-based Classification on Road Networks
Lee, H., Chowdhury, N.K., Chang, J.
Journal of the Korean Contents Association, Vol. 8 No. 10 pp-76-87, 2008
A New Travel Time Pre-diction Method for Intelligent Transportation System.
Lee, H., Chowdhury, N.K., and Chang, J.
Lecture Notes in Computer Science(), vol 5177. Springer, Berlin, Heidelberg., 12th International Conference on Knowledge-Based and Intelligent Information and Engineering Systems., 2008
Short-Term Travel Time Prediction Algorithm Based on Naive Bayesian Classification.
Chowdhury, N.K., and Chang, J.
Korean Database Conference (KDBC), 53-60, 2008
SVM-based Person Identification Using Illumination-compensated Features For Video Indexing
Mohammad Khairul Islam, Anjan Kumar Paul, Joong-Hwan Baek
International Conference on Internet Information Retrieval, Korea Aerospace University, South Korea, 53-59, December - 2007
Content-based Music Retrieval Using Beat Information
Mohammad Khairul Islam, Hyung-Jin Lee, Anjan Kumar Paul, Joong-Hwan Baek
International Conference on Fuzzy Systems and knowledge Discovery (FSKD), Haikou, China, 317-321, August - 2007
Music Identification Using Its Pattern
Mohammad Khairul Islam, Jae-Ung Yun, Anjan Kumar Paul, Joong-Hwan Baek
The Institute of Electronics Engineers of Korea (IEEK) Summer Conference, Pusan, South Korea, 419-420, July - 2007
Content-based Digital Video Retrieval using Facial Information
Mohammad Khairul Islam, Hyung-Jin Lee, Anjan Kumar Paul, Joong-Hwan Baek
The Korea Institute of Signal Processing and Systems (KISPS) Summer Conference, Ulsan University, South Korea, 18-21, June - 2007
New Range and k-NN Query Processing Algorithms using Materialization Technique in Spatial Network.
Um, J., Chowdhury, N.K., and Chang, J.
IEEE, International Symposium on Information Technology Convergence (ISITC), 76-80, 2007
Resolving geo‐spatial semantic conflicts–an interoperability issue
MS Hossain, R Mustafa
Humanomics, 2007, 2007
Range and k-Nearest Neighbour Query Processing Algorithms using Materialization Techniques in Spatial Network Databases
Kim, Y., Chowdhury, N.K., Lee, H., and Chang, J.
Journal of Korea Spatial Information System Society (KSISS), Volume 9 Issue 2 Pages.67-79, 2007
An Effective Video BGM Retrieval System Based On Beat Analysis
Mohammad Khairul Islam, Jae-Ung Yun, Hyung-Jin Lee, Anjan Kumar Paul, Joong-Hwan Baek
International Conference on Information Retrieval, Hankuk Aviation University, South Korea, 77-82, December - 2006
Actor Based Video Indexing and Retrieval Using Visual Information
Mohammad Khairul Islam, Soon-Tak Lee, Joong-Hwan Baek
International Conference on Natural Computation, LNCS, Xi’an, China, 492-501, September - 2006
Face Detection and Matching for Video Indexing
Mohammad Khairul Islam, Soon-Tak Lee, Jae-Ung Yun, Joong-Hwan Baek
The Korea Institute of Signal Processing and Systems (KISPS) Summer Conference, Suncheon National University, South Korea, 45-48, June - 2006
ApproximatTravel Time Measure From Moving Object Trajectory In Road Network
Chowdhury, N.K., Faruqui, R.U., and Hossen, M.K.
Computer Science and Engineering Research Journal, Vol. 04, ISSN: 1990- 4010, 2006
Bangla Compound Character Issue in TTS
Md. Hanif Seddiqui, Mohammad Shahjahan Feroz Farazi, Mohammad Khairul Islam, Muhammad Anwarul Azim
Asian Journal of Information technology 3 (2), 102-106, February - 2004
A New Numbering System and its Relations with Decimal, Binary, Hexadecimal and Octal Numbering System
Mohammad Shahjahan Feroz Farazi, Mohammad Hanif Siddiqui, Muhammad Anwarul Azim, Mohammad Khairul Islam, Mohammad Jalal Ahammad
Asian Journal of Information technology 3 (2), 96-100, 2004
K-Index-Sort: Sorting Unique Integer in Linear Time
A.H.M. Kamal, Zia Uddin Ahmed Khan, Mohammad Khairul Islam, Muhammad Anwarul Azim
Asian Journal of Information technology, 23-26, 2004
Insertion Sort: That apply Binary Search and Keep Track
A. H. M. Kamal, Enamul Azim, Mohammad Khairul Islam
International Conference on Computer and Information Technology (ICCIT), Jahangirnagar University, Dhaka, Bangladesh, 68-70, December - 2003
Construction of Deterministic Finite Automata (DFA) from Regular Expression
A. H. M. Kamal, Mohammad Khairul Islam
International Conference on Computer, Communication and Control Technologies (CCCT 2003), USA, 85-87, July - 2003
Parts of speech tagging using morphological analysis in bangla
MH Seddiqui, A Rana, A Al Mahmud, T Sayeed
Proceeding of the 6th International Conference on Computer and Information Technology (ICCIT), 2003, 2003
A new approach of Bangla machine translation considering Allomorph
MH Siddique, AKMS Rana, A Al Mamun
6th International Conference on Computer and Information Technology (ICCIT), 308-312, 2003, 2003
Morphological Analysis of Bangla Words
MH Seddiqui, AKMS Rana, A Al Mahmud, T Sayeed
6th International Conference on Computer and Information Technology (ICCIT), 2003, 2003
Algorithmic approach to synthesize voice from Bengali text
Md Hanif Seddiqui, Muhammad Anwarul Azim, Md Shahidur Rahman, M Zafar Iqbal
International Conference on Computer Sciences and Information Technology, 233-236, December - 2002
An Optimal Bangla Keyboard Layout
MH Seddiqui, MM Hassan, MS Hossain, MN Islam
Proceedings of International Conference on Computer and Information Technology (ICCIT), 2002, 2002
Algorithmic approach to synthesize voice from bangla text
MH Seddiqui, MA Azim, MS Rahman, MZ Iqbal
Proceedings of the 5th International Conference on Computer and Information Technology (ICCIT), 233-236, 2002, 2002
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
