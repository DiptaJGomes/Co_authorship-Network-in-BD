import re
import pandas as pd
import matplotlib.pyplot as plt

# Sample text as input
text = """1. Bangladesh University of Engineering and Technology
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#380 in Asia
#1227 in the World
Bangladesh University of Engineering and Technology logo
Founded 1962
Statistics 
Rankings 
2. University of Dhaka
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#529 in Asia
#1526 in the World
University of Dhaka logo
Acceptance Rate 11% 
Enrollment 37,018 
Founded 1921
Statistics 
Rankings 
3. Khulna University of Engineering and Technology
Bangladesh Flag Bangladesh | Khulna
For Computer Science

#660 in Asia
#1789 in the World
Khulna University of Engineering and Technology logo
Acceptance Rate 10% 
Founded 2003
Statistics 
Rankings 
4. Rajshahi University of Engineering and Technology
Bangladesh Flag Bangladesh | Rajshahi
For Computer Science

#849 in Asia
#2135 in the World
Rajshahi University of Engineering and Technology logo
Acceptance Rate 10% 
Founded 2003
Statistics 
Rankings 
5. North South University
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#862 in Asia
#2151 in the World
North South University logo
Acceptance Rate 25% 
Founded 1992
Statistics 
Rankings 
6. Daffodil International University
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#878 in Asia
#2182 in the World
Daffodil International University logo
Acceptance Rate 30% 
Founded 2002
Statistics 
Rankings 
7. Chittagong University of Engineering and Technology
Bangladesh Flag Bangladesh | Chittagong
For Computer Science

#889 in Asia
#2195 in the World
Chittagong University of Engineering and Technology logo
Acceptance Rate 9% 
Enrollment 4,500 
Founded 2003
Statistics 
Rankings 
8. Jahangirnagar University
Bangladesh Flag Bangladesh | Savar
For Computer Science

#955 in Asia
#2336 in the World
Jahangirnagar University logo
Acceptance Rate 16% 
Founded 1970
Statistics 
Rankings 
9. Rajshahi University
Bangladesh Flag Bangladesh | Rajshahi
For Computer Science

#1049 in Asia
#2532 in the World
Rajshahi University logo
Acceptance Rate 30% 
Enrollment 2,200 
Founded 1953
Statistics 
Rankings 
10. BRAC University
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#1051 in Asia
#2535 in the World
BRAC University logo
Acceptance Rate 45% 
Founded 2001
Statistics 
Rankings 
11. Khulna University
Bangladesh Flag Bangladesh | Khulna
For Computer Science

#1137 in Asia
#2730 in the World
Khulna University logo
Acceptance Rate 15% 
Founded 1990
Statistics 
Rankings 
12. Shahjalal University of Science and Technology
Bangladesh Flag Bangladesh | Sylhet
For Computer Science

#1165 in Asia
#2796 in the World
Shahjalal University of Science and Technology logo
Acceptance Rate 12% 
Enrollment 7,662 
Founded 1986
Statistics 
Rankings 
13. University of Chittagong
Bangladesh Flag Bangladesh | Chittagong
For Computer Science

#1183 in Asia
#2832 in the World
University of Chittagong logo
Founded 1966
Statistics 
Rankings 
14. American International University - Bangladesh
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#1189 in Asia
#2843 in the World
American International University - Bangladesh logo
Acceptance Rate 60% 
Enrollment 9,607 
Founded 1995
Statistics 
Rankings 
15. Islamic University
Bangladesh Flag Bangladesh | Kushtia
For Computer Science

#1275 in Asia
#2997 in the World
Islamic University logo
Founded 1979
Statistics 
Rankings 
16. United International University
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#1278 in Asia
#3004 in the World
United International University logo
Acceptance Rate 25% 
Founded 2003
Statistics 
Rankings 
17. Mawlana Bhashani Science and Technology University
Bangladesh Flag Bangladesh | Tangail
For Computer Science

#1375 in Asia
#3192 in the World
Mawlana Bhashani Science and Technology University logo
Acceptance Rate 16% 
Founded 2001
Statistics 
Rankings 
18. Islamic University of Technology
Bangladesh Flag Bangladesh | Gazipur
For Computer Science

#1377 in Asia
#3197 in the World
Islamic University of Technology logo
Acceptance Rate 11% 
Enrollment 2,400 
Founded 1978
Statistics 
Rankings 
19. East West University - Dhaka
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#1402 in Asia
#3249 in the World
East West University - Dhaka logo
Acceptance Rate 50% 
Founded 1996
Statistics 
Rankings 
20. Ahsanullah University of Science and Technology
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#1406 in Asia
#3258 in the World
Ahsanullah University of Science and Technology logo
Acceptance Rate 86% 
Founded 1995
Statistics 
Rankings 
21. International Islamic University, Chittagong
Bangladesh Flag Bangladesh | Chittagong
For Computer Science

#1413 in Asia
#3271 in the World
International Islamic University, Chittagong logo
Acceptance Rate 33% 
Founded 1995
Statistics 
Rankings 
22. Independent University, Bangladesh
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#1517 in Asia
#3511 in the World
Independent University, Bangladesh logo
Acceptance Rate 20% 
Enrollment 7,048 
Founded 1993
Statistics 
Rankings 
23. Bangladesh Agricultural University
Bangladesh Flag Bangladesh | Mymensingh
For Computer Science

#1572 in Asia
#3629 in the World
Bangladesh Agricultural University logo
Acceptance Rate 11% 
Enrollment 6,075 
Founded 1961
Statistics 
Rankings 
24. Bangabandhu Sheikh Mujib Medical University
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#1573 in Asia
#3630 in the World
Bangabandhu Sheikh Mujib Medical University logo
Acceptance Rate 11% 
Founded 1998
Statistics 
Rankings 
25. Green University of Bangladesh
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#1686 in Asia
#3903 in the World
Green University of Bangladesh logo
Acceptance Rate 70% 
Founded 2003
Statistics 
Rankings 
26. Noakhali Science and Technology University
Bangladesh Flag Bangladesh | Noakhali
For Computer Science

#1840 in Asia
#4267 in the World
Noakhali Science and Technology University logo
Acceptance Rate 10% 
Founded 2006
Statistics 
Rankings 
27. Bangladesh University of Professionals
Bangladesh Flag Bangladesh | Mirpur
For Computer Science

#1899 in Asia
#4417 in the World
Bangladesh University of Professionals logo
Acceptance Rate 75% 
Founded 2008
Statistics 
Rankings 
28. Hajee Mohammad Danesh Science and Technology University
Bangladesh Flag Bangladesh | Dinajpur
For Computer Science

#1964 in Asia
#4579 in the World
Hajee Mohammad Danesh Science and Technology University logo
Founded 1999
Statistics 
Rankings 
29. University of Science and Technology Chittagong
Bangladesh Flag Bangladesh | Chittagong
For Computer Science

#1974 in Asia
#4603 in the World
University of Science and Technology Chittagong logo
Acceptance Rate 63% 
Enrollment 5,682 
Founded 1992
Statistics 
Rankings 
30. Patuakhali Science and Technology University
Bangladesh Flag Bangladesh | Patuakhali
For Computer Science

#1997 in Asia
#4652 in the World
Patuakhali Science and Technology University logo
Acceptance Rate 9% 
Founded 2001
Statistics 
Rankings 
31. Pabna Science and Technology University
Bangladesh Flag Bangladesh | Pabna
For Computer Science

#2008 in Asia
#4673 in the World
Pabna Science and Technology University logo
Enrollment 4,500 
Founded 2001
Statistics 
Rankings 
32. Begum Rokeya University
Bangladesh Flag Bangladesh | Rangpur
For Computer Science

#2019 in Asia
#4697 in the World
Begum Rokeya University logo
Founded 2008
Statistics 
Rankings 
33. Comilla University
Bangladesh Flag Bangladesh | Comilla
For Computer Science

#2038 in Asia
#4749 in the World
Comilla University logo
Founded 2006
Statistics 
Rankings 
34. Jagannath University - Dhaka
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#2044 in Asia
#4760 in the World
Jagannath University - Dhaka logo
Acceptance Rate 15% 
Enrollment 33,000 
Founded 2005
Statistics 
Rankings 
35. Premier University
Bangladesh Flag Bangladesh | Chittagong
For Computer Science

#2088 in Asia
#4866 in the World
Premier University logo
Founded 2001
Statistics 
Rankings 
36. Bangabandhu Sheikh Mujibur Rahman Science and Technology University
Bangladesh Flag Bangladesh | Gopalganj
For Computer Science

#2102 in Asia
#4906 in the World
Bangabandhu Sheikh Mujibur Rahman Science and Technology University logo
Acceptance Rate 20% 
Founded 2001
Statistics 
Rankings 
37. Bangabandhu Sheikh Mujibur Rahman Agricultural University
Bangladesh Flag Bangladesh | Gazipur
For Computer Science

#2108 in Asia
#4919 in the World
Bangabandhu Sheikh Mujibur Rahman Agricultural University logo
Acceptance Rate 15% 
Founded 1998
Statistics 
Rankings 
38. Southern University Bangladesh
Bangladesh Flag Bangladesh | Chittagong
For Computer Science

#2139 in Asia
#4999 in the World
Southern University Bangladesh logo
Acceptance Rate 53% 
Founded 2002
Statistics 
Rankings 
39. Bangladesh University of Textiles
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#2167 in Asia
#5079 in the World
Bangladesh University of Textiles logo
Founded 2010
Statistics 
Rankings 
40. Dhaka International University
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#2226 in Asia
#5259 in the World
Dhaka International University logo
Acceptance Rate 42% 
Founded 1995
Statistics 
Rankings 
41. World University of Bangladesh
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#2233 in Asia
#5277 in the World
World University of Bangladesh logo
Enrollment 6,673 
Founded 2003
Statistics 
Rankings 
42. Sylhet Agricultural University
Bangladesh Flag Bangladesh | Sylhet
For Computer Science

#2252 in Asia
#5322 in the World
Sylhet Agricultural University logo
Acceptance Rate 84% 
Enrollment 4,000 
Founded 2006
Statistics 
Rankings 
43. Bangladesh University
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#2260 in Asia
#5345 in the World
Bangladesh University logo
Acceptance Rate 25% 
Enrollment 6,500 
Founded 2001
Statistics 
Rankings 
44. Jatiya Kabi Kazi Nazrul Islam University
Bangladesh Flag Bangladesh | Mymensingh
For Computer Science

#2305 in Asia
#5459 in the World
Jatiya Kabi Kazi Nazrul Islam University logo
Acceptance Rate 11% 
Founded 2006
Statistics 
Rankings 
45. Northern University of Bangladesh
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#2311 in Asia
#5476 in the World
Northern University of Bangladesh logo
Acceptance Rate 86% 
Founded 2002
Statistics 
Rankings 
46. Stamford University Bangladesh
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#2328 in Asia
#5525 in the World
Stamford University Bangladesh logo
Acceptance Rate 85% 
Founded 2002
Statistics 
Rankings 
47. Uttara University
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#2334 in Asia
#5540 in the World
Uttara University logo
Acceptance Rate 85% 
Founded 2003
Statistics 
Rankings 
48. University of Information Technology and Sciences
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#2372 in Asia
#5650 in the World
University of Information Technology and Sciences logo
Acceptance Rate 51% 
Founded 2003
Statistics 
Rankings 
49. Chittagong Medical University
Bangladesh Flag Bangladesh | Chittagong
For Computer Science

#2386 in Asia
#5687 in the World
Founded 2016
Statistics 
Rankings 
50. Sher-e-Bangla Agricultural University
Bangladesh Flag Bangladesh | Dhaka
For Computer Science

#2400 in Asia
#5738 in the World
Sher-e-Bangla Agricultural University logo
Enrollment 3,428 
Founded 2001"""

# List of sample research websites for illustration; replace these with actual URLs if available.
research_websites = [
    "https://www.buet.ac.bd", "https://www.du.ac.bd", "https://www.kuet.ac.bd",
    "https://www.ruet.ac.bd", "https://www.northsouth.edu", "https://www.daffodilvarsity.edu.bd",
    "https://www.cuet.ac.bd", "https://www.juniv.edu", "https://www.ru.ac.bd",
    "https://www.bracu.ac.bd", "https://ku.ac.bd", "https://www.sust.edu",
    "https://www.cu.ac.bd", "https://www.aiub.edu", "https://www.iu.ac.bd",
    "https://www.uiu.ac.bd", "https://www.mbstu.ac.bd", "https://www.iutoic-dhaka.edu",
    "https://www.ewubd.edu", "https://www.aust.edu", "https://www.iiuc.ac.bd",
    "https://www.iub.edu.bd", "https://www.bau.edu.bd", "https://www.bsmmu.edu.bd",
    "https://www.green.edu.bd", "https://www.nstu.edu.bd", "https://www.bup.edu.bd",
    "https://www.hstu.ac.bd", "https://www.ustc.ac.bd", "https://www.pstu.ac.bd",
    "https://www.pust.ac.bd", "https://www.brur.ac.bd", "https://www.cou.ac.bd",
    "https://www.jnu.ac.bd", "https://www.puc.ac.bd", "https://www.bsmrstu.edu.bd",
    "https://www.bsmrau.edu.bd", "https://www.southern.edu.bd", "https://www.butex.edu.bd",
    "https://www.diu.edu.bd", "https://www.wub.edu.bd", "https://www.sau.ac.bd",
    "https://www.bu.edu.bd", "https://www.jkkniu.edu.bd", "https://www.nub.ac.bd",
    "https://www.stamforduniversity.edu.bd", "https://www.uttarauniversity.edu.bd",
    "https://www.uits.edu.bd", "https://www.cmu.edu.bd", "https://www.sau.edu.bd"
]

# Regular expression to match each university entry
pattern = re.compile(r"(\d+)\.\s*([^\n]+)\nBangladesh Flag Bangladesh \|")

# Extracted data list
data = []

# Find all matches in the text and associate with research websites
for i, match in enumerate(pattern.finditer(text)):
    university_name = match.group(2)
    website = research_websites[i] if i < len(research_websites) else "N/A"
    
    # Append as a tuple
    data.append((university_name, website))

# Create DataFrame
df = pd.DataFrame(data, columns=["University Name", "Research Website"])

# Display the table
print(df)

# Plot setup
fig, ax = plt.subplots(figsize=(8, 4))
ax.axis("off")  # Hide the axes

# Create the table
table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc="center",
    loc="center"
)

# Table styling
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Header styling
for j in range(len(df.columns)):
    table[0, j].set_fontsize(12)
    table[0, j].set_text_props(weight="bold", color="white")
    table[0, j].set_facecolor("#4C72B0")  # Set header color

# Body styling
for i in range(1, len(df) + 1):
    for j in range(len(df.columns)):
        table[i, j].set_facecolor("#F2F2F2" if i % 2 == 0 else "#E6E6E6")  # Alternating row colors

plt.show()

# Regular expression to match each university entry
pattern = re.compile(r"(\d+)\.\s*([^\n]+)\nBangladesh Flag Bangladesh \|")

# Extracted data list
data = []

# Find all matches in the text and associate with research websites
for i, match in enumerate(pattern.finditer(text)):
    university_name = match.group(2)
    website = research_websites[i] if i < len(research_websites) else "N/A"
    
    # Append as a tuple
    data.append((university_name, website))

# Create DataFrame
df = pd.DataFrame(data, columns=["University Name", "Research Website"])

# Save the DataFrame to a CSV file
df.to_csv("universities_with_websites.csv", index=False)

# Display message
print("CSV file has been saved successfully.")