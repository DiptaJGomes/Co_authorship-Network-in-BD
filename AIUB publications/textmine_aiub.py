import csv
import re

# Input text data
text = """
tarikul islam, md. fayz-al-asad, m. a. khatun, n. parveen, hijaz ahmed and sameh askarh" natural convection heat transport performance of nanofluids under the influence of inclined magnetic field"
Results in Physics, 2024
[Ref No.: 6869]

md. manzurul hasan, debajyoti mondal, and md. saidur rahman "linear-time rectilinear drawings of subdivisions of triconnected cubic planar graphs with orthogonally convex faces"
Thai Journal of Mathematics -TJM, 2024
[Ref No.: 6872]

md. khairul alam mazumder,m. f. mridha, sultan alfarhood, mejdl safran, md. abdullah-al-jubair, dunren che "a robust and light-weight transfer learning-based architecture for accurate detection of leaf diseases across multiple plants using less amount of image"
Frontiers in Plant Science, 2024
[Ref No.: 6893]

zerin hasan sahosh, azraf faheem, marzana bintay tuba, md. istiaq ahmed, syeda anika tasnim" a comparative review on ddos attack detection using machine learning techniques"
Malaysian Journal of Science and Advanced Technology, 2024
Keywords: Networking,Artificial Intelligence [Ref No.: 6902]

sristy shidul nath,razuan karim, sristy shidul nath and mahdi h. mirazand mahdi h. miraz "deep learning based cyberbullying detection in bangla language"
Annals of Emerging Technologies in Computing (AETiC), 2024
Keywords: Deep Learning [Ref No.: 6903]

nusrat jahan anannya and md mehedi hasan" a fast-moving user-group detection algorithm for handover mitigation in ultra-dense cellular network"
., 2024
[Ref No.: 6831]

md. helal miah, mayeen uddin khandaker, mohammad aminul islam, mohammad nur-e-alam, hamid osman and md. habib ullah "perovskite materials in x-ray detection and imaging: recent progress, challenges, and future prospects"
RSC Advances, 2024
Keywords: Renewable Energy, Semiconductor Technologies,Energy Storage Materials [Ref No.: 6852]

md. roni islam, m. k. r. khan, md. sarowar hossain, m. m. rahman, m. mahbubul haque, m. aliuzzaman, m. k. alame and m. s. i. sarker "structural, thermodynamic, and magnetic properties of srfe12o19 hexaferrite modified by co-substitution of cu and gd"
RSC Advances, 2024
Keywords: Electrochemistry [Ref No.: 6865]

ashraful goni, md. umor faruk jahangir, rajarshi roy chowdhury "a study on cyber security: analyzing current threats, navigating complexities, and implementing prevention strategies"
International Journal of Research and Scientific Innovation, 2024
[Ref No.: 6744]

mohammad mahmudul hasan, marcelo corrales, george kousiouris, dimosthenis anagnostopoulos" cidata: an ontology-based framework for international data transfers and gdpr compliance"
International Journal of Metadata, Semantics and Ontologies, 2024
[Ref No.: 6768]

md. khairul alam mazumder, m. f. mridha, sultan alfarhood, mejdl safran, md. abdullah-al-jubair, dunren che "a robust and light-weight transfer learning-based architecture for accurate detection of leaf diseases across multiple plants using less amount of images"
Frontiers in Plant Science, 2024
Keywords: Deep Learning,Artificial Intelligence,Computer Vision,Image Processing [Ref No.: 6787]

bithi paul" biosynthesis of silver nanoparticles by banana pulp extract: characterizations, antibacterial activity, and bioelectricity generation"
Heliyon, 2024
[Ref No.: 6814]

w. a. khan, m.j. uddin "nano-bioconvective anisotropic slip flow in anisotropic porous medium with coriolis force effects"
Heat Transfer, 2024
Keywords: Nanotechnology [Ref No.: 6662]

jahidul islam, mahmud shareef, rubel anwar, sajeda akter, md. habib ullah, hamid osman, ismail m.m. rahman, mayeen uddin khandaker, faisal islam chowdhury "a brief insight on electrochemical energy storage toward the production of value-added chemicals and electricity generation"
Journal of Energy Storage, 2024
[Ref No.: 6704]

md. faruk abdullah al sohan" unmasking deception: a comprehensive survey on fake news detection strategies and technologies"
International Journal of Advanced Networking and Applications (IJANA), 2024
[Ref No.: 6726]

rifat al mamun rudro, md. faruk abdullah al sohan, afroza nahar "enhancing academic integrity for bangladesh's educational landscape"
Bangladesh Journal of Bioethics, 2024
[Ref No.: 6727]

rifath mahmud" emotion detection using machine learning: an analytical review"
Malaysian Journal of Science and Advanced Technology, 2024
Keywords: Computer Vision,Image Processing [Ref No.: 6740]

md. nur alam, mujahid iqbal, mohammad hassan, md. fayz-al-asad, muhammad sajjad hossain, cemil tunç" bifurcation, phase plane analysis and exact soliton solutions in the nonlinear schrodinger equation with atangana’s conformable derivative"
Chaos, Solitons and Fractals, 2024
[Ref No.: 6912]

dipta gomes "classification of food objects using deep convolutional neural network using transfer learning"
International Journal of Education and Management Engineering (IJEME), 2024
Keywords: Deep Learning,Artificial Intelligence,Neural Networks,Computer Vision [Ref No.: 6918]

md. tanvir hasan and mufti mahmud md. shamsul arefin,mohammed mostafizur rahman "a topical review on enabling technologies for the internet of medical things: sensors, devices, platforms, and applications"
Micromachines, 2024
Keywords: IoT [Ref No.: 6923]

md. arifuzzaman, tusar saha, jiban podder, fahad al-bin, hari narayan das "effect of silver doping on the band gap tuning of tungsten oxide thin films for optoelectronic applications"
Heliyon, 2024
Keywords: Semiconductor Technologies [Ref No.: 6932]

most. nadia tamanna "numerical investigation of heat transfer enhancement on tangent hyperbolic fluid over a stretching sheet with an inclined magnetic field filled with hybrid nanofluids"
Springer Link, 2024
[Ref No.: 6936]

s. s. billah, m. s. hossain, md. fayz-al-asad, m. s. i. mallik, s. c. paul, m. j. h. munshi and m. m. a. sarker "free convection at different locations of adiabatic elliptic blockage in a square enclosure"
Mathematical Modelling and Numerical Simulation with Applications, 2024
[Ref No.: 6920]

zasmin haque" marburg virus and risk factor among infected population: a modeling study"
Malaysian Journal of Mathematical Sciences, 2024
[Ref No.: 6966]

bithi paul "biosynthesis and characterizations of silver nanoparticles by using green banana peel extract: evaluation of their antibacterial and electrical performances"
Heliyon, 2024
[Ref No.: 6968]

rakin s. aftab, md. kais k. emon, sanjana f. anny, durjoy sarker, md. mazid-ul-haque" security analysis in online transaction systems: a proposed framework"
I.J. Information Engineering and Electronic Business, 2024
[Ref No.: 6969]

md. fayz-al-asad, f. mebarek-oudina, h. vaidya, md. shamim hasan, md. manirul alam sarker and a. i. ismail "finite element analysis for magneto-convection heat transfer performance in vertical wavy surface enclosure: fin size impact"
Frontiers in Heat and Mass Transfer, 2024
Keywords: Fin surface; finite element method; combined convection; MHD; wavy enclosure [Ref No.: 6979]

h ara1, s a tarek2, m k biswas3, s m s al-din4, e hoque1, k m e hasan1, a k m m hossain1, s b faruque1, y haque1 and s m sharafuddin1 "investigating the z-scan technique for quantifying circulating cell-free dna (ccfdna) extracted from blood plasma as a potential biomarker for various cancers"
Biomedical Physics & Engineering Express, 2024
Keywords: Circulating Cell-Free DNA, Nonlinear Optical Response, CW Z-scan [Ref No.: 6980]

dr. muhammad firoz mridha" leveraging deep neural networks to uncover unprecedented levels of precision in the diagnosis of hair and scalp disorders"
Skin Research and Technology, 2024
[Ref No.: 6983]

md rifat hossan, foyasl ahamed nirob, arafat islam, tanjim mahmud rakin, md al-amin" a comprehensive analysis of blockchain technology and consensus protocols across multilayered framework"
IEEE Access, 2024
[Ref No.: 6984]

zahan, n., fahim, s. a., shuvo, md. s. h., sarker, m., masum, s. md., & molla, md. a. i. "fabrication and characterization of c–doped tio2 nanoparticles for the photodegradation of organic dyes"
Inorganic and Nano-Metal Chemistry, 2024
[Ref No.: 6986]

putul, r. a., fahim, s. a., masum, s. md., & molla, md. a. i. "fabrication and characterisation of b-zno nanoparticles for photodegradation of ciprofloxacin antibiotic and textile dyes"
International Journal of Environmental Analytical Chemistry, 2024
[Ref No.: 6987]

dr. muhammad firoz mridha" cauli-det: enhancing cauliflower disease detection with modified yolov8"
Frontiers in Plant Science, 2024
[Ref No.: 6988]

saikat baul, md. ratan rana, farzana bente alam. "a real-time light-weight computer vision application for driver’s drowsiness detection"
International Journal of Engineering and Manufacturing (IJEM), 2024
Keywords: Drowsiness detection, computer vision, Dlib, OpenCV, ear, mar, head tilt angle. [Ref No.: 6989]

saydul akbar murad, zafril rizal m. azmi, abu jafar md. muzahid, md. murad hossain sarker, m. saef ullah miah, md. khairul bashar bhuiyan, nick rahimi, anupam kumar bairagi "priority based job scheduling technique that utilizes gaps to increase the efficiency of job distribution in cloud computing"
Sustainable Computing: Informatics and Systems, 2024
Keywords: Cloud computing; Job scheduling; Backfilling; Resource management; Gap searching; SJF; LJF; FCFS [Ref No.: 7002]

md saef ullah miah, md mohsin kabir, talha bin sarwar, mejdl safran, sultan alfarhood & m. f. mridha "a multimodal approach to cross‑lingual sentiment analysis with ensemble of transformer and llm"
Scientific Reports, 2024
[Ref No.: 7003]

hafijur rahman, md. soriful islam, abul khair, md. shohag hossain reyad "a study on the numerical accuracy and efficiency of the bisection method in finding nth roots of positive real numbers"
Int. J. Sci. Res. in Multidisciplinary Studies, 2024
Keywords: Algebraic and transcendental equations, nth root, Bisection method, Root mean square error, Numerical computation of zeros, Efficiency, Accuracy, Rate of convergence [Ref No.: 7004]

dr. muhammad firoz mridha" explainable federated learning for privacy-preserving bangla sign language detection"
Engineering Applications of Artificial Intelligence, 2024
[Ref No.: 7009]

dr. muhammad firoz mridha" indicdialogue: a dataset of subtitles in 10 indic languages for indic language modeling"
Data in Brief, 2024
[Ref No.: 7010]

dr. muhammad firoz mridha" explainable ai approaches in deep learning: advancements, applications and challenges"
Computers and Electrical Engineering, 2024
[Ref No.: 7011]

dr. muhammad firoz mridha" a machine learning approach for vocal fold segmentation and disorder classification based on ensemble method"
Scientific Reports, 2024
[Ref No.: 7012]

shahnaj parvin, abdur rahman "a real-time human bone fracture detection and classification from multi-modal images using deep learning technique"
Applied Intelligence, 2024
Keywords: Bone Fracture, Deep-learning [Ref No.: 7014]

bég, osman anwar, debasis kumar, mohammed jashim uddin, md abdul alim, and tasveer a. bég "simulation of magneto-nano-bioconvective coating flow with blowing and multiple slip effects"
Journal of Nanomaterials, Nanoengineering and Nanosystems, 2024
Keywords: Stefan blowing; Bio-nanofluid; Slips Effects; Wedge Flow; NDSolve; Materials processing. [Ref No.: 7017]

dr. mohammed jashim uddin" computation of rheological nanofluid coating boundary layer transport with convective wall heating."
Journal of Nanomaterials, Nanoengineering and Nanosystems, 2024
Keywords: Lie symmetry group transformation; Power law nanofluid; Porous media; Convective wall boundary conditions; thermal enhancement, nano-coating manufacture, MAPLE 18. [Ref No.: 7018]

ashadu jaman shawon 1, *, mohi uddin anondo 2 , anika tabassum 3 syed nafiul shefat 4" the 2023 outbreak of dengue in bangladesh and the non-identify criteria."
IOSR Journal Of Pharmacy And Biological Sciences, 2024
Keywords: Dengue, Dengue virus, Aedes mosquito, 2023 Outbreak, Dengue cases, Bangladesh, Death, Dengue Tests [Ref No.: 7022]

md. fayz-al- asad" influence of baffle size and position on natural convective heat transport in a skewed cavity by finite element method"
Modern Physics Letters B, 2024
[Ref No.: 7027]

pulok sarker, adnan sayed, abu bakar siddique, avijit saha apu, syeda anika tasnim, rifath mahmud "a comparative review on stock market prediction using artificial intelligence"
Malaysian Journal of Science and Advanced Technology (MJSAT), 2024
[Ref No.: 7028]

syeda anika tasnim " a comparativereview on stock market prediction using artificial intelligence"
Malaysian Journal of Science and Advanced Technology, 2024
[Ref No.: 7029]

s m abdullah shafi, myesha samia, sultanul arifeen hamim" emotion classification in bangla text data using gaussian naive bayes classifier: a computational linguistic study"
Malaysian Journal of Science and Advanced Technology, 2024
[Ref No.: 7030]

md. sydur rahman, aditya kumar saha, uma chakraborty, humaira tabassum sujana , s. m. abdullah shafi "evaluating the impact of test-driven development on software quality enhancement"
International Journal of Mathematical Sciences and Computing (IJMSC), 2024
[Ref No.: 7031]

md. fayz-al- asad" low cost artificial intelligence internet of things based water quality monitoring for rural areas"
Internet of Things, 2024
[Ref No.: 7033]

md. fayz-al- asad "computational modelling and simulations to study the thermal enhancement in nanofluid flow in undulating wavy cavity of a cylinder: finite element analysis"
Journal of Computational Design and Engineering, 2024
[Ref No.: 7043]

md. sarowar hossain, g. singh, e. haque, m. nishat, e. tarif, p. k. mukhopadhyay "electrostatic micro‑actuation system to evaluate the elastic moduli of metals with the application of dc voltage"
Experimental Techniques, 2024
Keywords: Lattice strain, Electrostatic force, Static defection, Micro-actuation, Tensile stress [Ref No.: 7047]

m.d. hossain, m.a. hossain, md. sarowar hossain, m. n. i. khan d, s. s. sikder "sintering temperature dependent characterization of ni nano ferrite with the optimization of frequency dependent properties"
Surface and Interface, 2024
Keywords: Ni ferrite, Sintering temperature, XRD, FESEM, Permeability [Ref No.: 7048]

tanmoy kumar ghosh, m. k. r. khan, m. m. rahman, md. sarowar hossain, suravi islam, nazia khatun and m. s. i. sarker "enhanced electrical, optical and magnetic properties of bifeo3 perovskite nanoparticles co-doped with y and cu"
AIP Advances, 2024
Keywords: Magnetic properties, Doping, Ferromagnetism, Magnetic materials, Phase transitions, X-ray diffraction, Dielectric properties, Raman spectroscopy, Perovskites, Nanoparticle [Ref No.: 7049]

md. rafiqul islam , md. shahidul islam and saikat majumder "breast cancer prediction: a fusion of genetic algorithm, chemical reaction optimization, and machine learning techniques"
Applied Computational Intelligence and Soft Computing, 2024
[Ref No.: 7053]

dr. md iftekharul mobin" social media as a mirror: reflecting mental health through computational linguistics"
IEEE Access, 2024
[Ref No.: 7054]

prof. dr. md. rafiqul islam "prediction of essential proteins using genetic algorithm as a feature selection technique"
IEEE Acess, 2024
[Ref No.: 7062]

rifat al mamun rudro, kamruddin nur, md. faruk abdullah al sohan, m. f. mridha, sultan alfarhood and mejdl safran "spf-net: solar panel fault detection using u-net based deep learning image classification"
Energy Reports, 2024
[Ref No.: 7067]

dr. muhammad firoz mridha" safeguardnet: enhancing corporate safety via tailored deep transfer learning for threat recognition"
IEEE Access, 2024
[Ref No.: 7070]

dr. muhammad firoz mridha" explainable deep learning for diabetes diagnosis with deepnetx2"
Biomedical Signal Processing and Control, 2024
[Ref No.: 7071]

md. reazul islam "machine learning-driven iot device for women’s safety: a real-time sexual harassment prevention system"
Multimedia Tools and Applications, 2024
Keywords: IoT, ML,AI [Ref No.: 7072]

mayesha sharmim tisha, md. kamrujjaman , ishrat zahan "dynamics of reaction–diffusion–advection system and its impact on river ecology in the presence of spatial heterogeneity"
Partial Differential Equations in Applied Mathematics, 2024
Keywords: Competition, Couple of species, Simulation, RDA, Advection [Ref No.: 7075]

mayesha sharmim tisha" wiener and lévy processes to prevent disease outbreaks: predictable vs stochastic analysis"
Partial Differential Equations in Applied Mathematics, 2024
[Ref No.: 7076]

bithi paul "crystallographic structure, antibacterial effect, and catalytic activities of fig extract mediated silver nanoparticles"
Heliyon, 2024
[Ref No.: 6998]

shuvo biswas, rafid mostafiz, bikash kumar paul, khandaker mohammad mohi uddin, md. abdul hadi, fahmida khanom "dfu_xai: a deep learning-based approach to diabetic foot ulcer detection using feature explainability"
Biomedical Materials & Devices, 2024
Keywords: Diabetic foot ulcers · Deep learning · Explainable AI · Convolutional neural networks [Ref No.: 6999]

md. mortuza ahmmed, shalini puri "current trends and future trajectories: polymer-modified concrete in the context of bangladesh"
Journal of Polymer and Composites, 2024
Keywords: PMC, construction, development, sustainability, Bangladesh. [Ref No.: 7090]

kh. abdul maleque "combined fluid and ferrofluid buoyancy force, heat absorption and non linear ferro-viscosity effects on ferro- hydrodynamics fluid flow in orthogonal porous surface"
Latin American Applied Research, 2024
Keywords: Curvilinear surfaces,, Incompressible Ferro Fluid,, Mixed Convection,, Ferrofluid Buoyancy Force, Non-linear ferro-viscosity,, Heat absorption/Generation. [Ref No.: 7091]

rifat al mamun rudro , kamruddin nur , md. faruk abdullah al sohan, m.f. mridha, sultan alfarhood, mejdl safran, karthick kanagarathinam "spf-net: solar panel fault detection using u-net based deep learning image classification"
Energy Reports, 2024
[Ref No.: 7092]
abhijit bhowmik, noorhozaimi mohd. nur, m. saef ullah miah, debajyoti karmekar "aspect-based sentiment analysis model for evaluating teachers' performance from students' feedback"
AIUB Journal of Science and Engineering (AJSE), 2023
[Ref No.: 7000]

mohammad sojon beg, muhammad yusri ismail, md. saef ullah miah "evaluating the performance of a visual support system for driving assistance using a deep learning algorithm"
Journal of Advanced Research in Applied Sciences and Engineering Technology, 2023
Keywords: Image Processing, Collision Avoidance, Deep Learning, Yolo V8, Object Detection [Ref No.: 7001]

md. reazul islam, md. mohsin kabir, muhammadfiroz mridha, sultan alfarhood, mejdl safran, dunrenche "deep learning-based iot system for remote monitoring and early detection of health issues in real-time"
MDPI, 2023
Keywords: IoT, ML, DL [Ref No.: 6994]

b. rajini kanth, md. sarowar hossain, p. k. mukhopadhyay "structure, microstructure and magneto-elastic property study on co40ni29al31 ferromagnetic shapememory alloy ribbon"
Materials Today:Proceedings, 2023
[Ref No.: 7050]

kazi sadia, ariyan jahangir "blockchain based agriculture using the application of uav and deep learning technique: alexnet cnn"
Malaysian Journal of Science and Advanced Technology, 2023
Keywords: AlexNet, Blockchain, Supply Chain, Sustainable Development Goals , Unmanned Air Vehicle [Ref No.: 6991]

khondokar oliullah, mahedi hasan rasel, md. manzurul islam, md. reazul islam, md. anwar hussen wadud & md. whaiduzzaman "a stacked ensemble machine learning approach for the prediction of diabetes"
Journal of Diabetes & Metabolic Disorders, 2023
Keywords: ML [Ref No.: 6992]

dr. mahfuza khatun" unraveling the burden of t2d among the adolescents in bangladesh: a statistical exploration of prevalence and influencing factors"
AIUB Journal of Science and Technology, 2023
[Ref No.: 6891]

tusar saha" structure based photocatalytic efficiency and optical properties of zno nanoparticles modified by annealing including williamson-hall microstructural investigation"
Materials Science and Engineering: B, 2023
[Ref No.: 6397]

razuan karim, mukter zaman, wong hin yong "a non-invasive methods for neonatal jaundice detection and monitoring to assess bilirubin level: a review"
International journal of Annals of Emerging Technologies in Computing (AETiC), 2023
[Ref No.: 6401]

md. faruk abdullah al sohan "utilization of machine learning strategies in the investigation of suspected credit card fraud"
Int. J. Advanced Networking and Applications, 2023
[Ref No.: 6389]

m ferdows, e e tzirtzilakis "hyperthermia temperature reduction in biomagnetic flow: thermal transfer in fe3o4–blood particle suspension with uniform and non-uniform effects"
Physics of Fluid, 2023
[Ref No.: 6390]

md. nazmul hossain" a comprehensive analysis of machine learning approaches for fake news detection and its effects"
Turkish Journal of Computer and Mathematics Education (TURCOMAT), 2023
[Ref No.: 6348]

md. al-amin" towards a novel identity check using latest w3c standards & hybrid blockchain for paperless verification"
International Journal of Information Engineering and Electronic Business(IJIEEB), 2023
[Ref No.: 6345]

d. mistry, m. f. mridha, m. safran, s. alfarhood, a. k. saha and d. che" privacy-preserving on-screen activity tracking and classification in e-learning using federated learning"
IEEE Access, 2023
[Ref No.: 6276]

a. j. keya, m. m. kabir, n. j. shammey, m. f. mridha, m. r. islam and y. watanobe" g-bert: an efficient method for identifying hate speech in bengali texts on social media"
IEEE Access, 2023
[Ref No.: 6277]

khan md hasib , nurul akter towhid , kazi omar faruk , jubayer al mahmud, m. f. mridha" strategies for enhancing the performance of news article classification in bangla: handling imbalance and interpretation"
Engineering Applications of Artificial Intelligence, 2023
[Ref No.: 6278]

m. s. h. shovon, s. j. mozumder, o. k. pal, m. f. mridha, n. asai and j. shin" plantdet: a robust multi-model ensemble method based on deep learning for plant disease detection"
IEEE Access, 2023
[Ref No.: 6279]

k. mridha, m. m. uddin, j. shin, s. khadka and m. f. mridha" an interpretable skin cancer classification using optimized convolutional neural network for a smart healthcare system"
IEEE Access, 2023
[Ref No.: 6280]

mohammad, zabir, arif reza anwary, muhammad firoz mridha, md sakib hossain shovon, and michael vassallo" an enhanced ensemble deep neural network approach for elderly fall detection system based on wearable sensors"
Sensors, 2023
[Ref No.: 6281]

k. mridha, s. ghimire, j. shin, a. aran, m. m. uddin and m. f. mridha" automated stroke prediction using machine learning: an explainable and exploratory study with a web application for early intervention"
IEEE access, 2023
[Ref No.: 6282]

8. hosen, sabbir, jannatul ferdous eva, ayman hasib, aloke kumar saha, m. f. mridha, and anwar hussen wadud" hqa-data: a historical question answer generation dataset from previous multi perspective conversation"
Data in Brief, 2023
[Ref No.: 6283]

islam, md. reazul, md. mohsin kabir, muhammad firoz mridha, sultan alfarhood, mejdl safran, and dunren che." deep learning-based iot system for remote monitoring and early detection of health issues in real-time"
Sensors, 2023
[Ref No.: 6284]

dr. md. abdullah - al - jubair" convowaste: an automatic waste segregation machine using deep learning"
IEEE Xplore, 2023
[Ref No.: 6270]

dr. md. abdullah - al - jubair" prediction of cryptocurrency price using machine learning techniques and public sentiment analysis"
IEEE Xplore, 2023
[Ref No.: 6271]

md. abu jubaer, md. nabobi hasan, mufrad mustavi, md. tanvir shahriar, tanvir ahmed "potato leaf disease detection using image processing"
International Journal of Education and Management Engineering(IJEME), 2023
[Ref No.: 6272]

pradipta chakraborty, santanu dey, shovan kumar kundu & soumen basu "influence of sm and fe co-doping on structural and electrical features of yttrium chromite nanoparticles"
Brazilian Journal of Physics, 2023
Keywords: Nanotechnology,Energy Storage Materials [Ref No.: 6290]

md. tanjimul islam , shahid uddin fahim , fatema jahan , humayra ferdous , md. ehasanul haque "a study on the effectiveness of online classes in bangladesh during the covid-19 pandemic"
AIUB Journal of Business and Economics (AJBE), 2023
Keywords: Population Dynamics [Ref No.: 6288]

shethil ahammed, ayesha amin, m. junayed ibne mohiuddin udoy, abdullah al maruf, kazi sadia, md. abdullah-al-jubair, mohammad shidujaman" an approach to user-friendly gui model using hci principles on university websites"
IEEE Xplore, 2023
[Ref No.: 6297]

yahaya saadu itas, kamaluddeen abubakar isah, awwal hussain nuhu, razif razali, salisu tata, naseer k. a, abubakr m. idris, md. habib ullah, mayeen uddin khandaker "the potentials of boron-doped (nitrogen deficient) and nitrogen-doped (boron deficient) bnnt photocatalysts for decontamination of pollutants from water bodies"
RSC Advances, 2023
[Ref No.: 6299]

shrabonti mitra, md. abdul malek, tanzin sultana, abhijit pathak, md. jainal abedin, khadizatul kobra, md. habib ullah, mayeen uddin khandaker "blended learning pedagogy and its implementation in the tertiary education: bangladesh perspectives"
Journal of Autonomous Intelligence, 2023
[Ref No.: 6300]

sabbir hossain, rahman sharar, md. ibrahim bahadur, abu sufian, rashidul hasan nabil "medibert: a medical chatbot built using keybert, biobert and gpt-2"
International Journal of Intelligent Systems and Applications(IJISA), 2023
Keywords: Artificial Intelligence [Ref No.: 6301]

md. sohidul islam, md. sajjad, mohammad mahmudul hasan, mohammad sakib islam mazumder "phishing attack detecting system using dns and ip filtering"
Asian Journal of Computer Science and Technology, 2023
[Ref No.: 6303]

foysal ahamed ni̇rob, mohammad mahmudul hasan "predicting stock price from historical data using lstm technique"
Journal of Artificial Intelligence and Data Science, 2023
[Ref No.: 6304]

fariya sultana prity, mohammad mahmudul hasan "mapping gaps between academic resources and industrial works in software testing"
Journal of Advancement in Software Engineering and Testing, 2023
[Ref No.: 6305]

26) abhijit bhowmik, noorhuzaimi mohd noor, m. saef ullah miah, md. mazid-ul-haque, debajyoti karmaker" a comprehensive dataset for aspect-based sentiment analysis in evaluating teacher performance"
AIUB Journal of Science and Engineering, 2023
[Ref No.: 6311]

abhijit bhowmik, noorhuzaimi mohd noor, m. saef ullah miah, md. mazid-ul-haque, and debajyoti karmaker "a comprehensive dataset for aspect-based sentiment analysis in evaluating teacher performance"
AIUB Journal of Science and Engineering (AJSE), 2023
Keywords: Artificial Intelligence [Ref No.: 6313]

dr. md. mozahar ali "dft approach into the physical properties of mte3 (m= hf, zr) superconductors: a comprehensive study"
AIP Advances, 2023
[Ref No.: 6462]

dr. md. saef ullah miah" an automated materials and processes identification tool for material informatics using deep learning approach"
Heliyon, 2023
[Ref No.: 6496]

dr. md. saef ullah miah" a comprehensive dataset for aspect-based sentiment analysis in evaluating teacher performance"
AIUB Journal of Science and Engineering (AJSE), 2023
[Ref No.: 6498]

md. manzurul hasan, debajyoti mondal, and md. saidur rahman "relating planar graph drawings to planar satisfiability problems"
Information Processing Letters (IPL), Elsevier, 2023
[Ref No.: 6499]

hiroaki fukuoka, mahjabin taskin, kungen teii, and yoshimine kato" measurement of oxygen concentration in atmospheric air using ultrasound time of flight with humidity compensation"
Review of Scientific Instruments, 2023
[Ref No.: 6514]

mohammad ferdows; abid hossain; m.j uddin; fahiza tabassum mim; shuyu sun "lie group analysis of magnetohydrodynamic flow with nonlinear hydrodynamic, linear thermal and mass slips"
Journal of Nonlinear Mathematical Physics, 2023
Keywords: Nanotechnology [Ref No.: 6556]

r: shahriar fahim, sm katibur rahman, sharfuddin mahmood" blockchain: a comparative study of consensus algorithms pow, pos, poa, pov"
International Journal of Mathematical Sciences and Computing, 2023
[Ref No.: 6552]

kanija muntarina, rafid mustafa, fahmida khanom, sumaita binte shorif, mohammad shorif uddin "multiresedge: a deep learning-based edge detection approach"
Intelligent Systems with Applications, 2023
Keywords: Deep Learning,Computer Vision,Image Processing [Ref No.: 6553]

md shakhawat hossain ,md. mahmudur rahman, m. mahbubul syeed , mohammad faisal uddin, mahady hasan , md. aulad hossain , amel ksibi , mona m. jamjoom , zahid ullah , and md abdus samad" deeppoly: deep learning based polyps segmentation and classification for autonomous colonoscopy examination"
IEEE Access, 2023
Keywords: Computer Vision,Image Processing,Medical Imaging [Ref No.: 6560]

dr. rehena parveen, s. m. nasim azad, sharmin islam, samira salam" the relationship between addictive use of social media and students' study efficiency : a cross sectional study on bsmrstu students."
Global Scientific Journal, 2023
[Ref No.: 6566]

samira salam , md. abul kalam azad, rehena parveen" rural-urban migration and social mobility in bangladesh: an empirical study using stochastic process"
Journal of Advance Multidisciplinary Research, 2023
[Ref No.: 6567]

anika saba ibte sum "a comprehensive analysis of machine learning approaches for fake news detection and its effects"
Turkish Journal of Computer and Mathematics Education (TURCOMAT), 2023
[Ref No.: 6568]

md. faruk abdullah al sohan" unleashing the potential of c++: using optimization techniques on procedeural-oriented programming for enhanced efficiency"
International Journal of Engineering Research in Computer Science and Engineering (IJERCSE), 2023
[Ref No.: 6725]

dr. akinul islam jony" navigating the cyber threat landscape: a comprehensive analysis of attacks and security in the digital age"
Journal of Information Technology and Cyber Security, 2023
[Ref No.: 6734]

dr. akinul islam jony" advancement in bangla sentiment analysis: a comparative study of transformer-based and transfer learning models for e-commerce sentiment classification"
Journal of Information Systems Engineering and Business Intelligence, 2023
[Ref No.: 6735]

kh. abdul maleque "the thermal absorption/generation on ferro-fluid combined convective flow over curvilinear porous surfaces"
AIUB journal of Science and Technology (AJSE), 2023
[Ref No.: 6737]

mst. ummay sumaya" effect of stabilizer content in different solvents on the synthesis of zno nanoparticles using the chemical precipitation method."
Journal of Heliyon, 2023
[Ref No.: 6718]

dr. samia mahjabin" boosting perovskite solar cell stability through a sputtered mo-doped tungsten oxide (wox) electron transport layer"
Energy Fuels, 2023
[Ref No.: 6720]

m.t. aziz, s.m.h. mahmud, m.f. elahe, h. jahan, m.h. rahman, d. nandi, l.k. smirani, k. ahmed, f.m. bui, m.a moni "a novel hybrid approach for classifying osteosarcoma using deep feature extraction and multilayer perceptron"
Diagnostics / MDPI, 2023
[Ref No.: 6663]

utshab das, hasan sanjary islam, kakon paul avi, ajmayeen adil, dip nandi "comparative analysis of data mining techniques for predicting the yield of agricultural crops"
International Journal of Information Technology and Computer Science(IJITCS), 2023
[Ref No.: 6664]

s m hasan mahmud, md mamun ali, mohammad fahim shahriar, fahad ahmed al-zahrani, kawsar ahmed, dip nandi, francis m bui "detection of different stages of alzheimer’s disease using cnn classifier"
Computers, Materials & Continua, 2023
[Ref No.: 6665]

snigdho dip howlader, tushar biswas, aishwarjyo roy, golam mortuja, dip nandi" a comparative analysis of algorithms for heart disease prediction using data mining"
International Journal of Information Technology and Computer Science (IJITCS), 2023
[Ref No.: 6666]

sadi mohammad, ibrahim adnan chowdhury, niloy roy, md. nazim hasan, dip nandi "investigation of student dropout problem by using data mining technique"
International Journal of Education and Management Engineering (IJEME), 2023
[Ref No.: 6667]

ahmed sikder, william ghann, md rafsun jani, md tohidul islam, saquib ahmed, mohammed m. rahman, md abdul majed patwary, mohsin kazi, jahidul islam, faisal i. chowdhury, mohammad a. yousuf, mohammad mahbub rabbani, mohammad hossain shariare, and jamal uddin "characterization and comparison of dsscs fabricated with black natural dyes extracted from jamun, black plum, and blackberry"
Energies, 2023
Keywords: Renewable Energy, Nanotechnologies,Electrochemistry,Nano Chemistry [Ref No.: 6668]

md. faruk abdullah al sohan "enhancing ddos attack detection using machine learning: a framework with feature selection and comparative analysis of algorithms"
Turkish Journal of Computer and Mathematics Education, 2023
[Ref No.: 6670]

sagar dutta , md. shahjahan ali , angkita mistry tama , md. masud parvez , m.a. hakim , md. sarowar hossain, humayra ferdous "enhancement of dielectric properties and conduction mechanism in bati0.85sn0.15o3 for energy storage application"
Journal of Energy Storage, 2023
[Ref No.: 6671]

yahaya saadu itas, abdussalam balarabe suleiman, chifu e. ndikilar, abdullahi lawal, razif razali, md. habib ullah, hamid osman, and mayeen uddin khandaker "dft studies of the photocatalytic properties of mos2-doped boron nitride nanotubes for hydrogen production"
ACS Omega, 2023
[Ref No.: 6644]

ayesha u, mamun asma, islam mn, hossain mr, tasmia sa and hossain mg. 2023. "early initiation of breastfeeding and its determinants of mothers in rajshahi district, bangladesh: a cross-sectional study"
Human Biology Review, 2023
Keywords: Industrial Applicants [Ref No.: 6646]

keya, ashfia jannat, arpona, sayefa arafah, kabir, muhammad mohsin, and mridha "recurrent albert for recommendation: a hybrid architecture for accurate and lightweight restaurant recommendations"
Cognitive Computation and Systems, 2023
[Ref No.: 6680]

j. r. jim, m. t. hosain, m. f. mridha, m. m. kabir and j. shin "toward trustworthy metaverse: advancements and challenges"
IEEE Access, 2023
[Ref No.: 6681]

m. s. h. shovon, m. f. mridha, k. m. hasib, s. alfarhood, m. safran and d. che "addressing uncertainty in imbalanced histopathology image classification of her2 breast cancer: an interpretable ensemble approach with threshold filtered single instance evaluation (sie)"
IEEE Access, 2023
[Ref No.: 6682]

jahin, md abrar, shovon, md sakib hossain, islam, md. saiful, shin, jungpil, mridha, m. f. and okuyama" qamplifynet: pushing the boundaries of supply chain backorder prediction using interpretable hybrid quantum-classical neural network."
Scientific Reports, 2023
[Ref No.: 6683]

sagar dutta and md. shahjahan ali and angkita mistry tama and md. masud parvez and humayra ferdous and m.a. hakim and md. sarowar hossain "enhancement of dielectric properties and conduction mechanism in bati0.85sn0.15o3 for energy storage application"
Journal of Energy Storage, 2023
[Ref No.: 6684]

sagar dutta, md. shahjahan ali, angkita mistry tama, md. masud parvez, humayra ferdous, m.a. hakim, md. sarowar hossain "enhancement of dielectric properties and conduction mechanism in bati0.85sn0.15o3 for energy storage application"
Journal of Energy Storage, 2023
Keywords: Industrial Applicants, Semiconductor Technologies, Sensor Technology [Ref No.: 6686]

mohammad rabiul islam "cnn based covid-19 detection from image processing"
Journal of ICT Research and Applications, 2023
Keywords: Image Processing [Ref No.: 6660]

s. parvin, n.c. roy, l.k. saha "natural convective non-newtonian nanofluid flow in a wavy-shaped enclosure with a heated elliptic obstacle"
Heliyon, 2023
[Ref No.: 6579]

prof. dr. md. rafiqul islam" a hybrid metaheuristic method for solving resource constrained project scheduling problem"
Evolutionary Intelligence, 2023
[Ref No.: 6592]

prof. dr. md. rafiqul islam" solving maximum clique problem using chemical reaction optimization, ,"
OPSEARCH,, 2023
[Ref No.: 6596]

prof. dr. md. rafiqul islam" user authentication and access control to blockchain based forensic log data,"
EURASIP Journal on Information Security, 2023
[Ref No.: 6597]

prof. dr. md. rafiqul islam" chemical reaction optimization for minimum weight dominating set,"
Applied Computational Intelligence and Soft Computing, 2023
[Ref No.: 6598]

prof. dr. md. rafiqul islam" edge intelligence for network intrusion prevention in iot ecosystem,"
Computers and Electrical Engineering, 2023
[Ref No.: 6599]

prof. dr. md. rafiqul islam" a solution method to maximal covering location problem based on chemical reaction optimization(cro) algorithm,"
Soft Computing,, 2023
[Ref No.: 6600]

prof. dr. md. rafiqul islam" identification of essential protein using chemical reaction optimization and machine learning technique,"
IEEE/ACM Transactions on Computational Biology and Bioinformatics, 2023
[Ref No.: 6601]

md. md. ariful islam, md antonin islam, md. amzad hossain jacky, md.al- amin, m. saef ullah miah, muhidul islam khan, md. iqbal hossain" distributed ledger technology based integrated healthcare solution for bangladesh"
IEEE Access, 2023
[Ref No.: 6627]

mustak un nobi, md., md. rifat, m. f. mridha, sultan alfarhood, mejdl safran, and dunren che "gld-det: guava leaf disease detection in real-time using lightweight deep learning approach based on mobilenet"
Agronomy, 2023
[Ref No.: 6632]

shakila rahman, jahid hasan rony, jia uddin, md abdus samad "real-time obstacle detection with yolov8 in a wsn using uav aerial photography"
MDPI Journal of Imaging, 2023
[Ref No.: 6633]

m. atikur rahman, zahid hasan, jahidul islam, d. k. das, faisal i. chowdhury, mayeen uddin khandaker, hossain m. zabed, d. a. bradley, hamid osman, and md. habib ullah "tailoring the properties of bulk batio3 based perovskites by heteroatom-doping towards multifunctional applications: a review"
ECS Journal of Solid State Science and Technology, 2023
[Ref No.: 6648]

nafiz fahad, kah ong michael goh, md. ismail hossen, connie tee, md. asraf ali "building a fortress against fake news harnessing the power of subfields in artificial intelligence"
Journal of Telecommunications and the Digital Economy, 2023
Keywords: Deep Learning [Ref No.: 6653]

3 "dsc index: measuring the digital supply chain practice among the higher education institutions community in least developed countries"
AIUB Journal of Science and Engineering (AJSE), 2023
[Ref No.: 6785]

shams forruque ahmed, md sakib bin alam, mahfara hoque, aiman lameesa, shaila afrin, tasfia farah, maliha kabir, gm shafiullah, sm muyeen "industrial internet of things enabled technologies, challenges, and future directions"
Computers and Electrical Engineering, 2023
Keywords: Internet of Things [Ref No.: 6786]

md. abu jafor, md. anwar hussen wadud, kamruddin nur and mohammad motiur rahman "employee promotion prediction using improved adaboost machine learning approach"
AIUB Journal of Science and Engineering (AJSE), 2023
Keywords: Artificial Intelligence [Ref No.: 6739]

faruk abdullah al sohan, syma kamal chaity, rubina islam reya "enhancing ddos attack detection using machine learning: a framework with feature selection and comparative analysis of algorithms"
Turkish Journal of Computer and Mathematics Education (TURCOMAT), 2023
Keywords: Machine to Machine Data Analytics [Ref No.: 6799]

rifat al mamun rudro" utilization of machine learning strategies in the investigation of suspected credit card fraud"
The International Journal of Advanced Networking and Applications, 2023
[Ref No.: 6800]

akinul islam jony" navigating the cyber threat landscape: a comprehensive analysis of attacks and security in the digital age"
Journal of Information Technology, 2023
[Ref No.: 6801]

md. asraf ali , md. kishor morol , muhammad f mridha, nafiz fahad , md sadi al huda, nasim ahmed "exploring a novel machine learning approach for evaluating parkinson's disease, duration, and vitamin d level"
International Journal of Advanced Computer Science and Applications, 2023
Keywords: Artificial Intelligence [Ref No.: 6769]

abhijit bhowmik, noorhozaimi mohd. nur, m. saef ullah miah, debajyoti karmekar "aspect-based sentiment analysis model for evaluating teachers' performance from students' feedback"
AIUB Journal of Science and Engineering (AJSE), 2023
[Ref No.: 6770]

md reazul islam, khondokar oliullah, md mohsin kabir, munzirul alom, m.f. mridha "machine learning enabled iot system for soil nutrients monitoring and crop recommendation"
Journal of Agriculture and Food Research, 2023
Keywords: Machine to Machine Data Analytics [Ref No.: 6771]

mustak un nobi m, rifat m, mridha mf, alfarhood s, safran m, che d. "gld-det: guava leaf disease detection in real-time using lightweight deep learning approach based on mobilenet"
MDPI, 2023
Keywords: Deep Learning,Computer Vision [Ref No.: 6764]

md. mortuza ahmmed" unraveling the burden of t2d among the adolescents in bangladesh: a statistical exploration of prevalence and influencing factors"
AJSE, 2023
[Ref No.: 6766]

sm hasan mahmud, md mamun ali, mohammad fahim shahriar, fahad ahmed al-zahrani, kawsar ahmed, dip nandi, francis m bui "detection of different stages of alzheimer’s disease using cnn classifier"
Computers, Materials & Continua, 2023
Keywords: Deep Learning,Machine to Machine Data Analytics,Image Processing [Ref No.: 6767]

tofayet sultan, nusrat jahan, ritu basak, mohammed shaheen alam jony, rashidul hasan nabil" machine learning in cyberbullying detection from social-media image or screenshot with optical character recognition"
International Journal of Intelligent Systems and Applications, 2023
[Ref No.: 6774]

md ohiduzzaman, mni khan, ka khan, bithi paul "green synthesis of silver nanoparticles by using allium sativum extract and evaluation of their electrical activities in bio-electrochemical cell"
IOP-science, 2023
[Ref No.: 6775]

sayma alam suha, muhammad nazrul islam "exploring the dominant features and data-driven detection of polycystic ovary syndrome through modified stacking ensemble machine learning technique"
Heliyon, 2023
[Ref No.: 6780]

sayma alam suha, muhammad nazrul islam "a systematic review and future research agenda on detection of polycystic ovary syndrome (pcos) with computer-aided techniques"
Heliyon, 2023
[Ref No.: 6781]

sayma alam suha and tahsina farah sanam "exploring dominant factors for ensuring the sustainability of utilizing artificial intelligence in healthcare decision making: an emerging country context"
International Journal of Information Management Data Insights, 2023
[Ref No.: 6783]

rajarshi roy chowdhury, azam che idris, pg emeroylariffion abas "identifying sh-iot devices from network traffic characteristics using random forest classifier"
Wireless Networks, 2023
[Ref No.: 6745]

rajarshi roy chowdhury, azam che idris and pg emeroylariffion abas" a deep learning approach for classifying network connected iot devices using communication traffic characteristics"
Journal of Network and Systems Management, 2023
[Ref No.: 6746]

rajarshi roy chowdhury, azam che idris, pg emeroylariffion abas "device identification using optimized digital footprints"
IAES International Journal of Artificial Intelligence, 2023
[Ref No.: 6747]

rajarshi roy chowdhury, debashish roy, md mamunur rashid, md sumon reza "social, economic, and environmental impacts of the one belt one road initiatives"
American International Journal of Multidisciplinary Scientific Research, 2023
[Ref No.: 6748]

b. gul, md. fayz-al-asad, m.s. khan, m. rahaman, g. periyasami, h. ahmad" insight into the optoelectronic nature and mechanical stability of binary chalcogenides: a first‐principles study"
ChemElectroChem, 2023
[Ref No.: 6867]

tarikul islam, md. nur alam, shafiullah niazai, ilyas khan, md. fayz-al-asad & sultan alqahtani" heat generation/absorption effect on natural convective heat transfer in a wavy triangular cavity filled with nanofuid"
Scientific Reports, 2023
[Ref No.: 6868]

h. goni, f. khanom, t. s. khaleque* "convection in the earth-like mantle with the influence of strong viscosity variation"
Journal of Applied Mathematics and Computation, 2023
[Ref No.: 6835]

s m hasibul hoque ,giovanni pirrone, fabio matrone, alessandra donofrio , giuseppe fanetti, angela caroli, rahnuma shahrin rista, roberto bortolus, michele avanzo, annalisa drigo andpaola chiovati "clinical use of a commercial artificial intelligence-based software for autocontouring in radiation therapy: geometric performance and dosimetric impact"
Cancers, 2023
[Ref No.: 6836]

syma kamal chaity" enhancing ddos attack detection using machine learning: a framework with feature selection and comparative analysis of algorithms"
Turkish Journal of Computer and Mathematics Education, 2023
[Ref No.: 6895]

syma kamal chaity" iot based single identification database model for under development countries"
Turkish Journal of Computer and Mathematics Education (TURCOMAT), 2023
[Ref No.: 6896]

md reazul islam, khondokar oliullah, md mohsin kabir, munzirul alom, mf mridha" machine learning enabled iot system for soil nutrients monitoring and crop recommendation"
Journal of Agriculture and Food Research, 2023
[Ref No.: 6897]

ashfia jannat keya, hasibul hossain shajeeb, md saifur rahman, mf mridha" fakestack: hierarchical tri-bert-cnn-lstm stacked model for effective fake news detection"
Plos One, 2023
[Ref No.: 6898]

abdul ahad, jiban podder, tusar saha, hn das" effect of chromium doping on the band gap tuning of titanium dioxide thin films for solar cell applications"
Heliyon, 2023
[Ref No.: 6900]

md mortuza ahmmed, m mostafizur rahman, mahfuz khatun "unraveling the burden of t2d among the adolescents in bangladesh: a statistical exploration of prevalence and influencing factors"
AIUB Journal of Science and Engineering (AJSE), 2023
[Ref No.: 6884]

m.s. sikder, m.d. hossain, i. sardar, md. sarowar hossain, m.n.i. khan, m.r. rahman "improved magnetic and dielectric quality factors with low losses in rare earth (eu) substituted co-ni-zn ferrites for high frequency devices"
Results in Physics, 2023
[Ref No.: 6159]

s. a. tarek,1a) s. b. faruque,1 s. m. sharafuddin,1 k. m. e. hasan,1 a. k. m. m. hossain,1 h. ara,1 m. k. biswas,2 y. haque1 "linear and thermo-optically generated nonlinear optical response of bovine serum albumin and its constituent amino acids in continuous wave z-scan"
AIP Advances, 2023
[Ref No.: 6161]

saiful islam, mahbuba khanom, md. al-amin, s. mosaddeq ahmed, farzana khalil, mohammad mahbub rabbani, mohammad tariqul islam & md. a. r. jamil "porous hybrid electrode materials for high energy density li-ion and li-s batteries"
Springer, Cham, 2023
[Ref No.: 6170]

k. . biswas, n. k. paul, d. saha, t. ahmed, and r. mahmud "detection of traffic rule violations using machine learning: an analytical review"
Malaysian Journal of Science and Advanced Technology, 2023
Keywords: Artificial Intelligence [Ref No.: 6171]

tofayet sultan, nusrat jahan, ritu basak, mohammed shaheen alam jony, rashidul hasan nabil" machine learning in cyberbullying detection from social-media image or screenshot with optical character recognition"
International Journal of Intelligent Systems and Applications (IJISA), 2023
[Ref No.: 6173]

dr. kamruddin md. nur "computer vision-based iot architecture for post covid-19 preventive measures"
Journal of Advances in Information Technology (JAIT), 2023
[Ref No.: 6118]

pritam khan boni, md. rafiqul islam "chemical reaction optimization for minimum weight dominating set"
Applied Computational Intelligence and Soft Computing, 2023
[Ref No.: 6058]

md.ismail hossen, nafiz fahad, md. ridoy sarkar, mohammad ruhani rabbi "artificial intelligencein agriculture: a systematicliterature review"
Turkish Journal of Computer and Mathematics Education, 2023
[Ref No.: 6060]

m. f. mridha, zabir mohammad, muhammad mohsin kabir, aklima akter lima, sujoy chandra das, md. rashedul islam, and yutaka watanobe" an unsupervised writer identification based on generating clusterable embeddings"
Computer Systems Science and Engineering, 2023
[Ref No.: 6120]

2. ahsanul akib, kamruddin nur, suman saha, jannatul ferdous srabonee , and m. f. mridha" computer vision-based iot architecture for post covid-19 preventive measures"
Journal of Advances in Information Technology, 2023
[Ref No.: 6121]

anima baroi, md. abu bakar siddique, md. ahedul akbor, farah noshin chowdhury, md. a. r. jamil, md. khabir uddin & md. mostafizur rahman "exposure and health risks of metals in imported and local brands’ lipsticks and eye pencils from bangladesh"
Environmental Science and Pollution Research, 2023
Keywords: Public health Awareness [Ref No.: 6178]

tahseen asma meem, shaira tashnub torsa, mehedi hasan, mahfujur rahman "a comparative study of fixing one barrier varying another barrier for a resonant tunneling diode"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2023
[Ref No.: 6184]

shahriar atik fahim "b–sn/tio2 nanoparticles for photodegradation of metronidazole antibiotics under different lights"
Materials Chemistry and Physics, Elsevier, 2023
[Ref No.: 6187]

hafijur rahman, gour chandra paul "tripartite sub-image histogram equalization for slightly low contrast gray-tone image enhancement"
Pattern Recognition, 2023
Keywords: Image Processing [Ref No.: 6190]

b. himabindu, n.s.m.p. latha devi, g. sandhya, t. naveen reddy, tusar saha, b. rajini kanth, md. sarowar hossain "structure based photocatalytic efficiency and optical properties of zno nanoparticles modified by annealing including williamson-hall microstructural investigation"
Material Science and Engineering B, 2023
Keywords: Nanotechnologies,Electrochemistry [Ref No.: 6210]

bijoya bose, nishat tasnim khan, sumaiya ashreen, faisal ahmed, md. mazid-ul-haque, abhijit bhowmik "hybrid scrum-xp: a proposed model based on effectiveness of agile model on varieties of software companies in bangladesh"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2023
Keywords: Model-driven software engineering,Software Architectures [Ref No.: 6195]

tonima mustafa1* , trishna roy1 , mst hasina begum1 , md masud rana1 , shanzida islam2 , farzana khalil3 and md. amjad hossain4 "proximate composition and mineral content of three wild and cultured fish species of bangladesh"
Jagannath University Journal of Life and Earth Sciences, 2023
[Ref No.: 6217]

kaushik biswas, niloy kanti paul, dipanwita saha, tanvir ahmed, and rifath mahmud "detection of traffic rule violations using machine learning: an analytical review"
Malaysian Journal of Science and Advanced Technology, 2023
Keywords: Artificial Intelligence,Computer Vision,Image Processing [Ref No.: 6218]

dr. md. saef ullah miah" 4d: a real-time driver drowsiness detector using deep learning"
Electronics, 2023
[Ref No.: 6243]

dr. md. saef ullah miah" distributed ledger technology based integrated healthcare solution for bangladesh"
IEEE Access, 2023
[Ref No.: 6244]

dr. md. saef ullah miah" yus - a deep learning algorithm for collision avoidance through object and vehicle detection"
Journal of Advanced Research in Applied Sciences and Engineering Technology, 2023
[Ref No.: 6245]

anik sen , rasel ahmed , samiha hossain , sazzad hossain tasnim , tanvir ahmed "find out the innovative techniques of data sharing using cryptography by systematic literature review"
Turkish Journal of Computer and Mathematics Education (TURCOMAT), 2023
[Ref No.: 6250]

1-15 "bio-nanoconvective micropolar fluid flow in a darcy porous medium past a cone with second-order slips and stefan blowing: fem solution"
Iranian Journal of Science and Technology, Transactions of Mechanical Engineering, 2023
[Ref No.: 6251]

24) bijoya bose khan, sumaiya, faisal, md. mazid-ul-haque, abhijit bhowmik "hybrid scrum-xp: a proposed model based on effectiveness of agile model on varieties of software companies in bangladesh"
AIUB Journal of Science and Engineering, 2023
Keywords: Software processes and methodologies [Ref No.: 6253]

md. manzurul hasan, shaheena sultana, and md. saidur rahman "sliding column model for t-unit bar visibility representations of graphs"
Discrete Mathematics, Algorithms and Applications, © World Scientific , Singapore., 2023
[Ref No.: 5688]

md rahat ibne sattar, md thowhid bin hossain efty, taiyaba shadaka rafa, tusar das, md sharif samad, abhijit pathak, mayeen uddin khandaker, md. habib ullah "an advanced and secure framework for conducting online examination using blockchain method"
Cyber Security and Applications, 2023
[Ref No.: 5755]

dr. afroza nahar" second law analysis for free convection in an l-shaped cavity filled with nanofluid"
AIUB Journal of Science and Engineering, 2023
[Ref No.: 5902]
m. f. mridha, md. al imran, md. anwar hussen wadud and md. abdul hamid" an improved user anonymous secure authentication protocol for healthcare system using wireless medical sensor network"
International Journal of Computing and Digital Systems, 2022
[Ref No.: 5548]

) shahadat hossain, md. manzurul hasan, md. mahmudur rahman and mimun barid "factors behind the world crime index: some parametric observations using dbscan and linear regression"
Springer Nature Switzerland AG, 2022
[Ref No.: 5578]

mahmudur rahman, shahadat hossain, mimun barid and md. manzurul hasan "inductions of usernames' strengths in reducing invasions on social networking sites (snss)"
Springer Nature Switzerland AG 2022, 2022
[Ref No.: 5579]

afroza nahar, hasanuzzaman, m., rahim, n. a., & parvin, s" thermo-fluid physiognomies of a photovoltaic thermal collector: a comparative study with different flow channel materials"
Journal of Solar Energy Engineering, 2022
[Ref No.: 5506]

salma parvin, abrar islam and afroza nahar." performance analysis of a direct absorption solar collector using different nanofluids: effect of physical parameters"
GANIT: Journal of Bangladesh Mathematical Society, 2022
[Ref No.: 5504]

nyme ahmed, md rifat-ibn-alam, golam ahsan akib, syed nafiul shefat, dip nandi "an extensive analysis on computing students' academic performance in online environment using decision tree"
Turkish Journal of Computer and Mathematics Education (TURCOMAT), 2022
[Ref No.: 5439]

mohammed kaosar mohammad nuruzzaman bhuiyan, md. m billah, dipanita saha, md. mahbubur rahman "iot based health monitoring system and its challenges and opportunities"
SpringerLink, 2022
[Ref No.: 5501]

md. masum billah" concept network using network text analysis"
Easychair, 2022
[Ref No.: 5502]

md ismail hossen, j. hossen, md nazmul hossain "an approach to recognize handwritten digits using machine learning classifiers"
Lecture Notes in Electrical Engineering, 2022
[Ref No.: 5341]

sultan abu saleh mahmud1 , tasnuva ferdous2 , md morshedul alam3 , md. shohag hossain2 , habibul bari shozib1 , farzana khalil4 , faija akter5 , mohammad nazir hossain3 * "para-phenylenediamine (ppd) in commercially available henna preparations in bangladesh"
Bioresearch Communications, 2022
[Ref No.: 5353]

nurul absar, nazim uddin, mayeen uddin khandaker, md. habib ullah "the efficacy of deep learning based lstm model in forecasting the outbreak of contagious diseases"
Infectious Disease Modelling, 2022
[Ref No.: 5365]

md. mehedi hassan onik" a systematic literature review of blockchain technology adoption in bangladesh"
Annals of Emerging Technologies in Computing (AETiC), 2022
Keywords: Blockchain, Sustainable production and Consumption [Ref No.: 5375]

jahidul islam, mahmud shareef, hossain m zabed, xianghui qi, faisal islam chowdhury, jagotamoy das, jamal uddin, yusuf valentino kaneti, mayeen uddin khandaker, abubakr m idris, md. habib ullah, mostafa kamal masud "electrochemical nitrogen fixation in metal-n2 batteries: a paradigm for simultaneous nh3 synthesis and energy generation"
Energy Storage Materials, 2022
[Ref No.: 5905]

md. al-amin, khondoker shahrina, rubyet hossain, debashish sarker, sumya sultana meem "decentralized payment aggregator: hyperledger fabric"
International Journal of Advanced Computer Science and Applications (IJACSA), 2022
Keywords: Blockchain,Distributed and parallel systems [Ref No.: 5907]

dr. md. rabiul auwul "a review of security and privacy concerns in the internet of things (iot)"
Journal of Sensors, 2022
[Ref No.: 5891]

md. mortuza ahmmed "a cluster based feasible time interval for tracking lost or stolen vehicle"
AIUB Journal of Science and Engineering (AJSE), 2022
[Ref No.: 5893]

md. mortuza ahmmed "the mathematical and machine learning models to forecast the covid-19 outbreaks in bangladesh"
Journal of Interdisciplinary Mathematics, 2022
[Ref No.: 5894]

md. mortuza ahmmed "public healthcare facilities and its utilization: bangladesh perspective"
International Journal of Clinical Images and Medical Reviews, 2022
[Ref No.: 5895]

tania rahman, shanto kumar saha, md. sajjadur rahman sohel, md. tamim maula, abhijit bhowmik, rashidul hasan nabil "risk identification and analysis in software development in bangladesh it industry: a hybrid model"
AIUB Journal of Science and Engineering (AJSE), 2022
[Ref No.: 5896]

hasan, md. nabobi, mufrad mustavi, md. abu jubaer, md. tanvir shahriar, and tanvir ahmed. "plant leaf disease detection using image processing: a comprehensive review"
Malaysian Journal of Science and Advanced Technology, 2022
Keywords: Artificial Intelligence,Image Processing [Ref No.: 5898]

tanvir ahmed, rashidul hasan nabil, and md. siyamul islam "detection of paddy blast: an image processing approach with threshold based otsu"
Malaysian Journal of Science and Advanced Technology, 2022
Keywords: Image Processing [Ref No.: 5899]

tanvir ahmed, rashidul hasan nabil, and md. siyamul islam "detection of paddy blast: an image processing approach with threshold based otsu"
Malaysian Journal of Science and Advanced Technology, 2022
[Ref No.: 5900]

m.k. islam, afroza nahar, m. hasanuzzaman, n.a. rahim" experimental performance investigation of a nanofluid based parabolic trough concentrator in malaysia"
AIUB Journal of Science and Engineering, 2022
[Ref No.: 5901]

rifat ibn alam; md. golam ahsan akib; nyme ahmed; syed nafiul shefat; dip nandi" a comparative analysis among online and on-campus students using decision tree"
I. J. Mathematical Sciences and Computing, 2022
[Ref No.: 5870]

jubayer ahamed, maisha maliha, zeba labiba, md. ariful islam, dr. dip nandi "a review report on the fingerprint-based biometric system in atm banking"
Association for Computing Machinery Digital Library(ACM_DL), 2022
Keywords: Software Architectures,Software Engineering Education and Training [Ref No.: 5872]

anjir ahmed chowdhury; md abir hossen; md ali azam; md hafizur rahman "deepqgho: quantized greedy hyperparameter optimization in deep neural networks for on-the-fly learning"
IEEE Access, 2022
Keywords: Deep Learning,Algorithms [Ref No.: 5873]

mohammad fahim khan, mohammad mahmudul hasan, sheikh aysha khatun "advancement of agri-trading systems towards improving farmers' economic situations in bangladesh"
International Journal of Environmental Sustainability and Green Technologies (IJESGT), 2022
[Ref No.: 5874]

rasel iqbal emon, md. mehedi hassan onik, abdullah al hussain1 , toufiq ahmed tanna1 , md. akhtaruzzaman emon, muhammad al amin rifat and mahdi h. miraz "privacy-preserved secure medical data sharing using hierarchical blockchain in edge computing"
Annals of Emerging Technologies in Computing (AETiC), 2022
Keywords: Blockchain [Ref No.: 5879]

• nusrat jahan, m. n. i. khan, m. r. hasan, m. s. bashar, a. islam, m. k. alam, m. a. hakim and j. i. khandaker" correlation among the structural, electric and magnetic properties of al3+ substituted ni–zn–co ferrites"
RSC Advanced, 2022
[Ref No.: 5848]

nyme ahmed, rifat-ibn-alam, md. golam ahsan akib, syed nafiul shefat, dr. dip nandi "an extensive analysis on computing students' academic performance in online environment using decision tree"
Turkish Journal of Computer and Mathematics Education (TURCOMAT), 2022
Keywords: Big Data [Ref No.: 5836]

rifat-ibn-alam, md. golam ahsan akib, nyme ahmed, syed nafiul shefat, dip nandi "a comparative analysis among online and oncampus students using decision tree"
Internatioal Journel of Mathematical Sciences and Computing, 2022, 2022
Keywords: Big Data [Ref No.: 5837]

syed nafiul shefat, md. golam ahsan akib, nyme ahmed, rifat-ibn-alam, dr. dip nandi "investigation of computing students’ performances in a fully online environment during covid-19 pandemic"
Malaysian Journal of Science and Advanced Technology (MJSAT), 2022
Keywords: Big Data [Ref No.: 5838]

nyme ahmed, syed nafiul shefat, taimur ahad "keep me in distance: an internet of things based social distance monitoring system in covid19"
International Journal of Advanced Networking and Applications, 2022
[Ref No.: 5839]

nyme ahmed, rifat-ibn-alam, syed nafiul shefat "performance evaluation of data mining classification algorithms for predicting breast cancer"
Malaysian Journal of Science and Advanced Technology (MJSAT), 2022
Keywords: Big Data [Ref No.: 5840]

md. mortuza ahmmed "covid-19 and sustainable development goals: bangladesh perspective"
International Journal of Advanced Operations Management, 2022
[Ref No.: 5756]

sajid bin-faisal, dip nandi, mashiour rahman "dual layer encryption for iot based vehicle systems over 5g communication"
https://www.mecs-press.org/ijitcs/, 2022
Keywords: Internet of Things,Digital Transformation,Security in Smart Environments [Ref No.: 5752]

rashidul hasan nabil, aneem-al-ahsan rupai, mimun barid, adnan sami and md. nazmul hossain "an intelligent examination monitoring tool for online student evaluation"
Malaysian Journal of Science and Advanced Technology, 2022
[Ref No.: 5753]

nyme ahmed, rifat-ibn-alam, md. golam ahsan akib, syed nafiul shefat, dip nandi "an extensive analysis on computing students' academic performance in online environment using decision tree"
Turkish Journal of Computer and Mathematics Education (TURCOMAT), 2022
Keywords: Data Mining and Business Intelligence [Ref No.: 5775]

rifat-ibn-alam, md golam ahsan akib, nyme ahmed, syed nafiul shefat, dip nandi "a comparative analysis among online and on-campus students using decision tree"
International Journal of Mathematical Sciences and Computing (IJMSC), 2022
Keywords: Data Mining and Business Intelligence [Ref No.: 5776]

syed nafiul shefat, md golam ahsan akib, nyme ahmed, rifat-ibn-alam, dip nandi "investigation of computing students’ performances in a fully online environment during covid-19 pandemic"
Malaysian Journal of Science and Advanced Technology, 2022
Keywords: Data Mining and Business Intelligence [Ref No.: 5777]

nyme ahmed, methila farzana woishe, nila sultana, tamanna zaman bristy "table token generator and indicator in restaurant using micro-controller"
European Journal of Engineering and Technology Research, 2022
Keywords: Internet of Things [Ref No.: 5778]

nyme ahmed, rifat-ibn-alam, syed nafiul shefat "performance evaluation of data mining classification algorithms for predicting breast cancer"
Malaysian Journal of Science and Advanced Technology, 2022
Keywords: Data Mining and Business Intelligence [Ref No.: 5780]

18) tania rahman, shanto kumar saha, md. sajjadur rahman sohel, md. tamim maula, abhijit bhowmik "risk identification and analysis in software development in bangladesh it industry: a hybrid model"
AIUB Journal of Science and Engineering, 2022
Keywords: Model-driven software engineering [Ref No.: 5781]

syma kamal chaity" iot based parallel server architecture in low power environment"
Int. J. Advanced Networking and Applications, 2022
[Ref No.: 5791]

md. manzurul hasan, debajyoti mondal, and md. saidur rahman, positive planar "positive planar satisfiability problems under 3-connectivity constraints"
Theoretical Computer Science, Science Direct, Elsevier, 2022
[Ref No.: 5685]

shahadat hossain, md. manzurul hasan, and mimun barid. "a heuristic approach for analyzing some reading behaviors of online news viewers using rf and knn"
Proceedings of TEHI 2022, Springer, Singapore., 2022
[Ref No.: 5686]

saiful islam, seunggyeong lee, seulgi lee, muhammad hilmy alfaruqi, balaji sambandam, vinod mathew, jang-yeon hwang, jaekook kim "triggering the theoretical capacity of na1.1v3o7.9 nanorod cathode by polypyrrole coating for high-energy zinc-ion batteries"
Chemical Engineering Journal, 2022
Keywords: Energy Storage Materials [Ref No.: 5690]

monowar, muhammad m., md. a. hamid, faris a. kateb, abu q. ohi, and m. f. mridha "self-supervised clustering for leaf disease identification"
Agriculture, 2022
[Ref No.: 5691]

dr. muhammad firoz mridha "a comprehensive survey on the detection, classification, and challenges of neurological disorders"
Biology, 2022
Keywords: Bioinformatics [Ref No.: 5692]

monowar, muhammad m., md. a. hamid, abu q. ohi, madini o. alassafi, and m. f. mridha "autoret: a self-supervised spatial recurrent network for content-based image retrieval"
Sensors, 2022
[Ref No.: 5693]

m. a. h. wadud, m. f. . mridha, and m. m. . rahman "word embedding methods for word representation in deep learning for natural language processing"
Iraqi Journal of Science, 2022
[Ref No.: 5694]

md. mohsin kabir, adit ishraq, kamruddin nur, and m. f. mridha "content-based image retrieval using autoembedder"
Journal of Advances in Information Technology, 2022
[Ref No.: 5695]

dr. md. mozahar ali" influence of heavy hf doping in ceo2: prediction on various physical properties"
Results in Physics, 2022
[Ref No.: 5666]

bithi paul "green synthesis and characterization of silver nanoparticles by using bryophyllum pinnatum and the evaluation of its power generation activities on bio-electrochemical cell"
Materials Chemistry and Physics, 2022
[Ref No.: 5644]

abhijit bhowmik "a machine learning approach for bengali handwritten vowel character recognition"
IAES International Journal of Artificial Intelligence (IJ-AI), 2022
[Ref No.: 5707]

shafin talukder, sk. tasnim bari ira, aseya khanom, prantika biswas sneha and wardah saleh" vehicle collision detection & prevention using vanet based iot with v2v"
International Journal of Wireless and Mobile Networks (IJWMN), 2022
[Ref No.: 5711]

wardah saleh and shahrin chowdhury" ran slicing: towards multi-tenancy in 5g radio access networks"
International Journal of Wireless and Mobile Networks (IJWMN), 2022
[Ref No.: 5712]

bithi paul" nano-bio effects: interaction of zno and dna-bases"
Nano-Structures & Nano-Objects, 2022
[Ref No.: 5723]

m. a. hussen wadud, m. f. mridha, jungpil shin, kamruddin nur, and aloke kumar saha "deep-bert: transfer learning based deep learning model for classifying multilingual offensive texts on social media"
Computer Systems Science and Engineering (CSSE), 2022
Keywords: Deep Learning [Ref No.: 5735]

md. mohsin kabir, adit ishraq, kamruddin nur, and m. f. mridha "content-based image retrieval using autoembedder"
Journal of Advances in Information Technology (JAIT), 2022
Keywords: Deep Learning [Ref No.: 5736]

md masuduzzaman , anik islam , kazi sadia , soo young shin "uav-based mec-assisted automated traffic management scheme using blockchain"
Future Generation Computer Systems, 2022
Keywords: Blockchain [Ref No.: 5737]

md. mortuza ahmmed "the obstacles to combat against covid-19 pandemic and the remedies: bangladesh scenario"
Journal of Public Health Research, 2022
[Ref No.: 5597]

md iftekharul alam efat, md shazzad hossain shihab, shuvra aditya, jahangir hossain setu, km imtiaz-ud-din" identifying optimized speaker identification model using hybrid gru-cnn feature extraction technique"
Int. J. of Computational Vision and Robotics (IJCVR), 2022
[Ref No.: 5610]

md. navid bin anwar, afroza nahar, nashid kamal md., mehedi hasan shuvo" a waiting time based bully algorithm for leader node selection in distributed system"
Malaysian Journal of Science, 2022
[Ref No.: 5647]

methila farzana woishe" optimizing iot based parallel server in a low power operational environment"
International Journal of Advanced Networking and Applications, 2022
[Ref No.: 5656]

nyme ahmed, methila farzana woishe, nila sultana, tamanna zaman bristy" table token generator and indicator in restaurant using micro-controller"
European Journal of Engineering and Technology Research7, 2022
[Ref No.: 5657]

md ismail hossain sadhin, methila farzana woishe, nila sultana, tamanna zaman bristy" identifying lung cancer using ct scan images based on artificial intelligence"
Malaysian Journal of Science and Advanced Technology (MJSAT), 2022
[Ref No.: 5658]

nila sultana, methila farzana woishe, tamanna zaman bristy, dr. md taimur ahad" an efficient iot enabled smart ambulance routing appling loadng routing protocol: aiming to achieve sustainable development goals"
Turkish Journal of Computer and Mathematics Education (TURCOMAT), 2022
[Ref No.: 5659]

vivek kumar singh, prashasti singh, ashraf uddin, parveen arora, sujit bhattacharya "exploring the relationship between journals indexed from a country and its research output: an empirical investigation"
Scientometrics, 2022
[Ref No.: 6075]

nyme ahmed, dip nandi, a. g. m zaman "analyzing student evaluations of teaching in a completely online environment"
International Journal of Modern Education and Computer Science (IJMECS), 2022
Keywords: Data Mining and Business Intelligence [Ref No.: 6076]

m.j uddin, na amirsom, oa beg, a.i.m ismail "computation of bio-nano-convection power law slip flow from a needle with blowing effects in a porous medium"
Waves in Random and Complex Media, 2022
Keywords: Nanotechnology [Ref No.: 6081]

o. a bég,tasveer bég,w. a. khan,m. j. uddin "multiple slip effects on nanofluid dissipative flow in a converging/diverging channel: a numerical study"
Heat Transfer—Asian Research., 2022
Keywords: Nanotechnology [Ref No.: 6086]

m. f. mridha, md. kishor morol, md. asraf ali, md sakib hossain shovon "convoher2: a deep neural network for multi-stage classification of her2 breast cancer"
AIUB Journal of Science and Engineering, 2022
[Ref No.: 6094]

tasriva sikandar, sam matiur rahman, dilshad islam, md asraf ali, md. abdullah al mamun, mohammad fazle rabbi, kamarul h. ghazali, omar altwijri, mohammed almijalli, nizam uddin ahamed "walking speed classification from marker-free video images in two-dimension using optimum data and a deep learning method"
Bioengineering, 2022
[Ref No.: 6095]

dr. akinul islam jony" a comparison of opinion mining algorithms by using product review data"
International Journal of Information Engineering and Electronic Business, 2022
[Ref No.: 6099]

dr. akinul islam jony" strategies for enhancing the multi-stage classification performances of her2 breast cancer from hematoxylin and eosin images"
Diagnostics, 2022
[Ref No.: 6100]

dr. kamruddin md. nur "deep-bert: transfer learning for classifying multilingual offensive texts on social media"
Computer Systems Science and Engineering (CSSE), 2022
[Ref No.: 6101]

m.d. hossain, m.n.i. khan, md sarowar hossain, s. j. ahned, m. k. alam, s. i. liba, m. a. hakim, a. t. m. k. jamil "structure-based magnetic, electrical and transport properties of ni–zn–co ferrite by v5+ substitution"
Current Applied Physics, 2022
[Ref No.: 6048]

prof. dr. dip nandi" investigation of machine learning algorithms for network intrusion detection"
I.J. Information Engineering and Electronic Busines, 2022
[Ref No.: 6023]

prof. dr. dip nandi" comparative analysis of data mining techniques to predict cardiovascular disease"
International Journal of Information Technology and Computer Science(IJITCS), 2022
[Ref No.: 6024]

prof. dr. dip nandi" a comprehensive study to investigate student performance in online education during covid-19"
International Journal of Modern Education and Computer Science (IJMECS), 2022
[Ref No.: 6025]

shakila rahman" oadc: an obstacle-avoidance data collection scheme using multiple unmanned aerial vehicles"
MDPI Applied Sciences, 2022
[Ref No.: 6014]

shakila rahman" energy-efficient charging of sensors for uav-aided wireless sensor network"
International Journal of Internet, Broadcasting and Communication, 2022
[Ref No.: 6018]

mohammad alahmad1,*, imad alshaikhli2 , abdulrahman alkandari3, abdullah alshehab4, mohamamd rabiul islam5, meshal alnasheet6 "influence of hedera hash graph over blockchain"
Journal of Engineering Science and Technology, 2022
Keywords: Blockchain,Algorithms [Ref No.: 5998]

nyme ahmed, dip nandi, a. g. m. zaman" analyzing student evaluations of teaching in a completely online environment"
International Journal of Modern Education and Computer Science (IJMECS), 2022
Keywords: Algorithms,Data Mining and Business Intelligence [Ref No.: 5996]

md. tanvir mahtab, a. g. m. zaman, montasir rahman mahin, mohammad nazim mia, md. tanjirul islam "stock price prediction: an incremental learning approach model of multiple linear regression"
AIUB Journal of Science and Engineering, 2022
Keywords: Machine to Machine Data Analytics [Ref No.: 6008]

md al-amin, saiful islam, sayed ul alam shibly, samia iffat "comparative review on the aqueous zinc-ion batteries (azibs) and flexible zinc-ion batteries (fzibs)"
Nanomaterials, 2022
Keywords: Nanotechnologies [Ref No.: 5990]

md. sohidul islam" outage capacity analysis for next generation wireless communication using non-orthogonal multiple access"
International Journal of Information and Communication Engineering, 2022
Keywords: Wireless/ Mobile Communication [Ref No.: 5985]

jannatul ferdosy, md. mortuza ahmmed, md. ashraful babu, m. mostafizur rahman" determinants of knowledge and precautionary practices about nosocomial infection among fourth graded hospital workers in bangladesh: a mathematical and statistical approach"
Journal of Interdisciplinary Mathematics, 2022
[Ref No.: 5986]

md. ashraful babu, md. mortuza ahmmed, md. abu helal, m. a. hoque "the fbprophet forecasting model to evaluate the spread of covid-19 pandemic: a machine learning approach"
Journal of Interdisciplinary Mathematics, 2022
[Ref No.: 5987]

md. hridoy bhuyan, mohammad mahmudul hasan, fowjia tajnin muna "digital bangladesh: an electronic automated system for bangladesh police administration"
Asian Journal of Computer Science and Technology, 2022
[Ref No.: 5988]

partha sutradhar, victor stany rozario "in - depth case study on artificial neural network weights optimization using meta - heuristic and heuristic algorithmic approach"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2022
Keywords: Deep Learning,Machine to Machine Data Analytics,Neural Networks [Ref No.: 5978]

dr. md. abdullah - al - jubair "ar lab/practical simulation book for physics chemistry & computer science"
ACM Digital Library, 2022
[Ref No.: 5922]

oishi khanam" future possible age of the universe with density variation"
I. J. Mathematical Sciences and Computing, 2022
[Ref No.: 6248]

dr. md. saef ullah miah" sentence boundary extraction from scientific literature of electric double layer capacitor domain: tools and techniques"
MDPI Applied Sciences, 2022
[Ref No.: 6236]

dr. md. saef ullah miah" predicting young imposter syndrome using ensemble learning"
Complexity, 2022
[Ref No.: 6237]

dr. md. saef ullah miah" application of machine learning algorithms to predict the thyroid disease risk: an experimental comparative study"
PeerJ Computer Science, 2022
[Ref No.: 6238]

dr. md. saef ullah miah" a machine learning approach for bengali handwritten vowel character recognition"
IAES International Journal of Artificial Intelligence (IJ-AI), 2022
[Ref No.: 6239]

dr. md. saef ullah miah" evaluating keyphrase extraction algorithms for finding similar news articles using lexical similarity calculation and semantic relatedness measurement by word embedding"
PeerJ Computer Science, 2022
[Ref No.: 6240]

dr. md. saef ullah miah" restinet: on improving the performance of tiny-yolo-based cnn architecture for applications in human detection"
MDPI Applied Sciences, 2022
[Ref No.: 6241]

dr. md. saef ullah miah" restinet: an efficient deep learning approach to improve human detection accuracy"
MethodsX, 2022
[Ref No.: 6242]

gour chandra paul, mrinal chandra barman, hafijur rahman "an effective method in investigating structures of polytropic protoplanets formed via gravitational instability"
Heliyon, 2022
[Ref No.: 6191]

hafijur rahman, k.c. roy, s.k. das, s.a. hossain "a study on the numerical accuracy and efficiency of the bisection method in finding square roots of positive real numbers"
Int. J. of Sci. Research in Computer Science and Engineering, 2022
[Ref No.: 6192]

hafijur rahman, a. khair, n. sultana "a competitive study on the euler and different order runge-kutta methods with accuracy and stability"
Int. J. of Sci. Research in Mathematical and Statistical Sciences, 2022
[Ref No.: 6193]

shahriar atik fahim "natural sunlight driven photocatalytic removal of toxic textile dyes in water using b-doped zno/tio2 nanocomposites"
Catalysts, 2022
[Ref No.: 6186]

mahfujur rahman, mehedi hasan, md masum billah, rukaiya jahan sajuti "political fake news detection from different news source on social media using machine learning techniques"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2022
[Ref No.: 6181]

mahfujur rahman, mehedi hasan, md masum billah, rukaiya jahan sajuti "grading system prediction of educational performance analysis using data mining approach"
The Malaysian Journal of Science and Advanced Technology, 2022
[Ref No.: 6182]

mr. mehedi hasan, m. tanseer ali, md. kamrul hasan, shaira tashnub torsa, mahfujur rahman "comparative study of single and double barrier gaas/al0.3ga0.7as based resonant tunneling diodes considering negf"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2022
[Ref No.: 6183]

mridha, m. f.,prodeep, akibur rahman,hoque, a. s. m. morshedul,islam, md. rashedul,lima, aklima akter,kabir, muhammad mohsin,hamid, md. abdul,watanobe, yutaka" a comprehensive survey on the progress, process, and challenges of lung cancer detection and classification"
Journal of Healthcare Engineering, 2022
[Ref No.: 6122]

wadud, md. anwar hussen, mohammed alatiyyah, and m. f. mridha" non-autoregressive end-to-end neural modeling for automatic pronunciation error detection"
Applied Sciences, 2022
[Ref No.: 6123]

mohammad, zabir, muhammad mohsin kabir, muhammad mostafa monowar, md abdul hamid, and muhammad firoz mridha "self-writer: clusterable embedding based self-supervised writer recognition from unlabeled data"
Mathematics, 2022
[Ref No.: 6124]

k. m. hasib, a. tanzim, j. shin, k. o. faruk, j. a. mahmud and m. f. mridha "bmnet-5: a novel approach of neural network to classify the genre of bengali music based on audio features"
Open Access, 2022
[Ref No.: 6125]

dr. muhammad firoz mridha "3d gesture recognition and adaptation for human–robot interaction"
IEEE Access, 2022
[Ref No.: 6126]

shovon, md sakib hossain, md jahidul islam, mohammed nawshar ali khan nabil, md mohimen molla, akinul islam jony, and m. f. mridha. "strategies for enhancing the multi-stage classification performances of her2 breast cancer from hematoxylin and eosin images"
Diagnostics, 2022
[Ref No.: 6127]

keya, ashfia jannat, md. anwar hussen wadud, m. f. mridha, mohammed alatiyyah, and md. abdul hamid "augfake-bert: handling imbalance through augmentation of fake news using bert to enhance the performance of fake news classification"
Applied Sciences, 2022
[Ref No.: 6128]

m. anwar hussen wadud, m. f. mridha, j. shin, k. nur and a. kumar saha "deep-bert: transfer learning for classifying multilingual offensive texts on social media"
Computer Systems Science and Engineering, 2022
[Ref No.: 6129]

md. anwar hussen wadud, muhammad mohsin kabir, m.f. mridha, m. ameer ali, md. abdul hamid, muhammad mostafa monowar "how can we manage offensive text in social media - a text classification approach using lstm-boost"
International Journal of Information Management Data Insights, 2022
[Ref No.: 6130]

md. nazmul hossain "an approach to recognize vehicles context flow for smartphone-based outdoor parking using supervised machine learning classifiers"
AIUB Journal of Science and Engineering (AJSE), 2022
[Ref No.: 6111]

md. nazmul hossain "an intelligent examination monitoring tool for online student evaluation"
Malaysian Journal of Science and Advanced Technology (MJSAT), 2022
[Ref No.: 6112]

g.c. biswas, s. choudhury, m.m. rabbani, j. das "a review on potential electrochemical point-of-care tests targeting pandemic infectious disease detection: covid-19 as a reference"
Chemosensors, 2022
Keywords: Nanotechnologies,Nano Chemistry,Analytical Chemistry [Ref No.: 6115]

s. faraezi, m.s khan, f.z. monira, a.a. mamun, t. akter, m.a. mamun, m.m. rabbani, j. uddin, and a.j.s. ahammad, "sensitivity control of hydroquinone and catechol at poly(brilliant cresyl blue)-modified gce by varying activation conditions of the gce: an experimental and computational study"
ChemEngineering, 2022
Keywords: Analytical Chemistry [Ref No.: 6116]

n. sultana, s.d. shawon, s.m.a. nayem, m.m. hasan, t. islam, s.s. shah, m.m. rabbani, m.a. aziz, a.j.s. ahammad "cobalt oxide nanorod-modified gce as sensitive electrodes for simultaneous detection of hydroquinone and catechol"
Processes, 2022
Keywords: Nanotechnologies,Nano Chemistry,Analytical Chemistry [Ref No.: 6117]

md. dulal hossain, a. t. m. kaosar jamil, md. sarowar hossain, syed jamal ahmed, harinarayan das, rimi rashid, m. a. hakim, m n i khan "investigation on structure, thermodynamic and multifunctional properties of ni-zn-co ferrite for gd3+ substitution"
RSC Advances, 2022
[Ref No.: 6045]

a. kaiyum, m.a. hossain, md. sarowar hossain, r. rashid, a. kumar, m.a. hakim, m.n.i. khan "influence of eu3+ substitution on structural, magnetic and dielectric properties of bi0.9la0.1feo3"
Journal of Magnetism and Magnetic Materials, 2022
[Ref No.: 6046]

md. iftekharul alam efat, md. shazzad hossain, shuvra aditya, jahanggir hossain setu and k.m. imtiaz-ud-din" identifying optimised speaker identification model using hybrid gru-cnn feature extraction technique"
International Journal of Computational Vision and Robotics, 2022
[Ref No.: 6119]

fahima khanam, farha akhter munmun, nadia afrin ritu, aloke kumar saha, and m. f. mridha "text to speech synthesis: a systematic review, deep learning based architecture and future research direction"
Journal of Advances in Information Technology, 2022
[Ref No.: 6132]

mustafizur rahman, shusmita islam, rubiyet fardous, lamisa yesmin, dip nandi" applying scrum development on safety critical systems"
International Journal of Information Technology and Computer Science(IJITCS), 2022
[Ref No.: 6145]

sumaiya sultana, sumaiya rahman eva, nayeem hasan moon, akinul islam jony, dip nandi" a comparison of opinion mining algorithms by using product review data"
I.J. Information Engineering and Electronic Business, 2022
[Ref No.: 6146]

rifat-ibn alam, md. golam ahsan akib, nyme ahmed, syed nafiul shefat, dip nandi" a comparative analysis among online and on-campus students using decision tree"
International Journal of Mathematical Sciences and Computing(IJMSC), 2022
[Ref No.: 6147]

sajid bin-faisal, dip nandi, mashiour rahman" dual layer encryption for iot based vehicle systems over 5g communication"
I.J. Information Technology and Computer Science, 2022
[Ref No.: 6148]

syed nafiul shefat, md golam ahsan akib, nyme ahmed, dip nandi" investigation of computing students’ performances in a fully online environment during covid-19 pandemic"
Malaysian Journal of Science and Advanced Technology, 2022
[Ref No.: 6149]

md motaleb hassan, mishu majumder, mosumi mitra, khadiza akter mitu, md. sazzad hossain "application of semi-distributed hydrological model in northern region of bngladesh"
International journal of Geology, Agriculture and environmental sciences, 2022
[Ref No.: 6152]

kawser irom rushee" a comparison of missing value imputation techniques on coupon acceptance prediction."
International Journal of Information Technology and Computer Science, 2022
[Ref No.: 6174]

tamanna zaman bristy "identifying lung cancer using ct scan images based on artificial intelligence"
International Journal of Computer and Information System, 2022
Keywords: Machine to Machine Data Analytics [Ref No.: 6853]

tamanna zaman bristy "optimizing iot based parallel server in a low power operational environment"
International Journal of Advanced Networking and Applications, 2022
[Ref No.: 6854]

tamanna zaman bristy" an efficient iot enabled smart ambulance routing appling loadng routing protocol: aiming to achieves sustainable development goals"
Turkish Journal of Computer and Mathematics Education (TURCOMAT), 2022
[Ref No.: 6855]

tamanna zaman bristy "table token generator and indicator in restaurant using micro-controller"
European Journal of Engineering and Technology Research, 2022
[Ref No.: 6856]

tamanna zaman bristy "a secured model of iot-based smart gas detecting and automatic alarm system"
International Journal of Computer and Information System (IJCIS), 2022
[Ref No.: 6857]

sandhya aneja; nagender aneja; bharat bhargava; rajarshi roy chowdhury "device fingerprinting using deep convolutional neural networks"
International Journal of Communication Networks and Distributed Systems, 2022
[Ref No.: 6753]

rajarshi roy chowdhury, azam che idris and pg emeroylariffion abas "internet of things device classification using transport and network layers communication traffic traces"
International Journal of Computing and Digital Systems, 2022
[Ref No.: 6754]

rajarshi roy chowdhury, pg emeroylariffion abas "a survey on device fingerprinting approach for resource-constraint iot devices: comparative study and research challenges"
Internet of Things, 2022
[Ref No.: 6755]

rajarshi roy chowdhury, azam che idris, pg emeroylariffion abas "packet-level and ieee 802.11 mac frame-level analysis for iot device identification"
Turkish Journal of Electrical Engineering and Computer Sciences, 2022
[Ref No.: 6750]

sayma alam suha and m. akhtaruzzaman and tahsina farah sanam "a fuzzy model for predicting burn patients’ intravenous fluid resuscitation rate"
Healthcare Analytics, 2022
[Ref No.: 6782]

nuzhat tabassum, sujeendran menon, agnieszka jastrzębska "time-series classification with safe: simple and fast segmented word embedding-based neural time series classifier"
Information Processing & Management, 2022
Keywords: Neural Networks [Ref No.: 6776]

sayma alam suha & muhammad nazrul islam "an extended machine learning technique for polycystic ovary syndrome detection using ovary ultrasound image"
Scientific Reports, 2022
[Ref No.: 6777]

sayma alam suha and tahsina farah sanam "a deep convolutional neural network-based approach for detecting burn severity from skin burn images"
Machine Learning with Applications, 2022
[Ref No.: 6778]

md. mahbubur rahman and dipanjali kundu and sayma alam suha and umme raihan siddiqi and samrat kumar dey" hospital patients’ length of stay prediction: a federated learning approach"
Journal of King Saud University-Computer and Information Sciences, 2022
[Ref No.: 6779]

saikat baul, md. ratan rana "analyzing database security and a study of ownership protection using watermarking algorithm"
Scientific Research in Computer Science, Engineering and Information Technology, 2022
Keywords: Other [Ref No.: 6772]

saikat baul, md. ratan rana, sakimul karim adan, nazia tafannum, farzana alam "analyzing different software project management tools and proposing a new project management tool using process re-engineering on open-source and saas platforms for a developing country like bangladesh"
International Journal of Advances in Electronics and Computer Science, 2022
Keywords: Software Architectures,Other [Ref No.: 6773]

md sohan, faruk abdullah al, samiur rahman khan, nusrat jahan anannya, md taimur ahad" towards a secured smart iot using light weight blockchain: an aim to secure pharmacy products"
N/A, 2022
[Ref No.: 6830]

dr. jahida binte islam "dual z-scheme heterojunction g-c3n4/ag3po4/agbr photocatalyst with enhanced visible-light photocatalytic activity"
Ceramics International, 2022
[Ref No.: 6615]

jahida binte islam, md rakibul islam, mai furukawa, ikki tateishi, hideyuki katsumata, satoshi kaneco "ag-modified g-c3n4 with enhanced activity for the photocatalytic reduction of hexavalent chromium in the presence of edta under ultraviolet irradiation"
Environmental Technology, 2022
[Ref No.: 6616]

prof. dr. md. rafiqul islam" an efficient roi detection algorithm for bangla text extraction and recognition from natural scene images,"
Journal of King Saud University- Computer Science and Information Sciences, 2022
[Ref No.: 6593]

prof. dr. md. rafiqul islam" protein complex prediction in large protein-protein interaction network,"
Informatics in Medicine Unlocked, 2022
[Ref No.: 6594]

prof. dr. md. rafiqul islam" cluster- based authentication process in a smart city"
Security and Communication Network, 2022
[Ref No.: 6595]

ayesha siddiqua "numerical simulation for nanofluid flow in a wall driven cavity with solid hindrance: impact of thermal conductivity ratio and heat generation"
Journal of Nanofluids, 2022
[Ref No.: 6607]

prof. dr. md. rafiqul islam" a hybrid framework based on genetic algorithm and simulated annealing for rna structure prediction with pseudoknots"
Journal of King Saud University- Computer Science and Information Sciences, 2022
[Ref No.: 6587]

md. siddikur rahman , nujhat tabassum safa , sahara sultana , samira salam , ajlina karamehic-muratovic , hans j. overgaard "role of artificial intelligence-internet of things (ai-iot) based emerging technologies in the public health response to infectious diseases in bangladesh"
Parasite Epidemiology and Control, 2022
[Ref No.: 6565]

syma kamal chaity" iot based medical information management system"
International Journal of Scientific & Engineering Research, 2022
[Ref No.: 6626]

nyme ahmed, dip nandi, a.g.m zaman "analyzing student evaluations of teaching in a completely online environment"
I.J. Modern Education and Computer Science, 2022
Keywords: Data Mining and Business Intelligence [Ref No.: 6647]

farhana afroz, bm sajjad hossain, mohammad abu taher, & jubayer ahamed "establishing democracy in bangladesh: evaluating the role of media"
AIUB Journal of Business and Economics (AJBE), 2022
[Ref No.: 6674]

dr. samia mahjabin" investigation of morphological, optical, and dielectric properties of rf sputtered wox thin films for optoelectronic applications"
Nanomaterials, 2022
[Ref No.: 6722]

sharmin jahan, subrata banik, nure alam chowdhury, abdul mannan and a a mamun "electrostatic shock structures in a magnetized plasma having non-thermal particles"
gases, 2022
Keywords: Natural Sciences [Ref No.: 6729]

dr. samia mahjabin" sputtered wox thin film as the electron transport layer for efficient perovskite solar cells"
Applied Physics A, 2022
[Ref No.: 6733]

saikat baul,md. ratan rana,sakimul karim adan,nazia tafannum, farzana alam "analyzing different software project management tools and proposing a new project management tool using process re-engineering on open-source and saas platforms for a developing country"
Support Open Access INTERNATIONAL JOURNAL OF ADVANCES IN ELECTRONICS AND COMPUTER SCIENCE ( IJAECS ), 2022
Keywords: Software engineering for Contemporary Software Systems [Ref No.: 6554]

sheekar banerjee, aminun nahar jhumur "a novel approach of marine ecosystem monitoring system with multi-sensory submarine on robotic platform for visualizing the climate change effect over oceanic environment"
Trends in Sciences, 2022
Keywords: Digital Transformation,Wireless/ Mobile Communication,Artificial Intelligence [Ref No.: 6559]

mrinmoy karmokar, heerok mutsuddy, shahadat hossain, and md. manzurul hasan "an implementation of basic ant-colony optimization based routing in6 of 11 wireless sensor networks"
Springer, In Proceedings of the ICO 2022 (Intelligent Computing & Optimization), 2022
[Ref No.: 6544]

shapla akter, md. jamil hossain, shahadat hossain, joyanta ghosh, md. omar faruq dehan, and md. manzurul hasan, "is rdbms or nosql better suited for mis?: a comparative analysis"
Springer, In Proceedings of the ICO 2022 (Intelligent Computing & Optimization), 2022
[Ref No.: 6545]

nahid hasan, tanzila hasan, shahadat hossain & md. manzurul hasan "false smut disease detection in paddy using convolutional neural network"
Springer, in Proceedings of the MIET 2022, 2022
[Ref No.: 6546]

sumi akter" analysis of the influence of trivalent cr3+ doping on the structural and electromagnetic properties of cu0.5mg0.5crxfe2−xo4 nanoferrites"
AIP Advances, 2022
[Ref No.: 6547]

rashidul hasan nabil ,aaa rupai, mimun barid, adnan sami, md. nazmul hossain "an intelligent examination monitoring tool for online student evaluation"
Malaysian Journal of Science and Advanced Technology, 2022
[Ref No.: 6548]

shahadat hossain, md. manzurul hasan, and tanzila mehenaz" ramifications of corruption perception index: an exploratory data analyses using dbscan"
In Proceedings of the ICCA 2022, ACM Digital Library, 2022
[Ref No.: 6539]

shanjidah akhter, samir asif, mehedi hasan sazzad, and md. manzurul hasan. "performance analysis of parallel overlapping community detection algorithms in large-scale social networks"
In Proceedings of the ICCA 2022, ACM Digital Library, 2022
[Ref No.: 6540]

shahadat hossain, tanzila mehenaz, fahim shahriar, md. al-mamun riyadh and md. manzurul hasan," training tracker: a training management system"
Springer, Cham, In Proceedings of the ICO 2022 (Intelligent Computing & Optimization),, 2022
[Ref No.: 6541]

nusrat songita khan, fahad molla, rubayat shusmita khan, enamul haque shamim, shahadat hossain, and md. manzurul hasan "exploration of online fake news through machine learning and sentiment analyses"
Springer, In Proceedings of the ICO 2022 (Intelligent Computing & Optimization), 2022
[Ref No.: 6542]

rifat-ibn-alam, nyme ahmed, syed nafiul shefat, taimur ahad "keep me in distance: an internet of things based social distance monitoring system in covid19"
International Journal of Advanced Networking and Applications (IJANA), 2022
Keywords: Data Mining and Business Intelligence [Ref No.: 6513]

md. kishor morol, shuvra smaran das, sharfuddin mahmood "data security and privacy in cloud computing platforms: a comprehensive review"
International Journal of Current Science Research and Review, 2022
[Ref No.: 6505]

mahfujur rahman, mehedi hasan, md masum billah, rukaiya jahan sajuti "political fake news detection from different news source on social media using machine learning techniques"
AIUB Journal of Science and Engineering (AJSE), 2022
[Ref No.: 6501]

rukaiya jahan sajuti mahfujur rahman, mehedi hasan, md masum billah "grading system prediction of educational performance analysis using data mining approach"
Malaysian Journal of Science and Advance Technology, 2022
[Ref No.: 6502]

bristy talukder md masum billah, din mohammad dohan, afsara tasnim, shaily sarker "analyzing the effect of covid-19 on mental health based on bangladeshi university students"
ICCA '22: Proceedings of the 2nd International Conference on Computing Advancements, 2022
[Ref No.: 6503]

md. abdullah al nahid1 , michinori karikomi1 , eri nasuno1 , norihiro kato1 , takaaki sato2 , and ken-ichi iimura1 "phase transfer of amiet-functionalized gold nanoparticles from aqueous to organic solvents"
Journal of Oleo Science, 2022
[Ref No.: 6489]

md. fayz-al- asad" reliable analysis for the drinfel’d-sokolov-wilison equation in mathematical physics"
Palestine Journal of Mathematics, 2022
[Ref No.: 6441]

md. fayz-al- asad" numerical study of the effect of a heated cylinder on natural convection in a square cavity in the presence of a magnetic field"
Mathematical and Computational Applications, 2022
[Ref No.: 6442]

md. fayz-al- asad" impact of non-uniform periodic magnetic field on unsteady natural convection flow of nanofluids in square enclosure,"
Fractal and Fractional, 2022
[Ref No.: 6443]

md. fayz-al- asad" hydrothermal and entropy investigation of nanofluid natural convection in a lid-driven cavity concentric with an elliptical cavity with a wavy boundary heated from below"
Nanomaterials, 2022
[Ref No.: 6444]

md. fayz-al- asad" analytic simulation of mhd boundary layer flow of a chemically reacting upper-convected maxwell fluid past a vertical surface subjected to double stratifications with variable properties"
European Physical Journal Plus, 2022
[Ref No.: 6445]

shahnaj parvin, md. ezharul islam, and liton jude rozario "nighttime vehicle detection methods based on headlight feature: a review"
IAENG International Journal of Computer Science, 2022
[Ref No.: 6418]

mohammad mahmudul hasan, fowjia tajnin muna "technology trends and cyber security in bangladesh: myths and reality"
International Journal of Technology Diffusion (IJTD), 2022
[Ref No.: 6302]

md. faruk abdullah al sohan, samiur rahman khan, nusra jahan anannya "towards a secured smart iot using light weight blockchain: an aim to secure pharmacy products"
arxiv logo > cs > arXiv:2206.06925 Search..., 2022
[Ref No.: 6298]

mubashir qayyum, farnaz ismail, syed inayat ali shah, muhammad sohail, kanayo kenneth asogwa, fatema tuz zohra "analysis of fractional thin film flow of third grade fluid in lifting and drainage via homotopy perturbation procedure"
Advances in Mathematical Physics, 2022
Keywords: Nanotechnology [Ref No.: 6275]

md. masum billah "design and implementation of a feasible model for the iot based ubiquitous healthcare monitoring system for rural and urban areas"
IEEE Access, 2022
[Ref No.: 6391]

tusar saha" thermodynamic and dynamic stability in a new potential cs2agascl6 perovskite: insight from dft study"
Physical Chemistry Chemical Physics, 2022
[Ref No.: 6392]

tusar saha" effect of tungsten doping on the microstructure, optical and photocatalytic activity of titanium dioxide thin films deposited by spray pyrolysis"
Optical Materials, 2022
[Ref No.: 6393]

md ashraful babu, md mortuza ahmmed, mir kaosar ahamed, m mostafizur rahman "a cluster based feasible time interval for tracking lost or stolen vehicle"
AIUB Journal of Science and Engineering (AJSE), 2022
Keywords: Security in Smart Environments,Intelligent Transportation [Ref No.: 6924]

jannatul ferdosy, md mortuza ahmmed, md ashraful babu, m mostafizur rahman "determinants of knowledge and precautionary practices about nosocomial infection among fourth graded hospital workers in bangladesh: a mathematical and statistical approach"
Journal of Interdisciplinary Mathematics, 2022
Keywords: Deep Learning [Ref No.: 6925]

md ashraful babu, md mortuza ahmmed, amena ferdousi, m mostafizur rahman, md saiduzzaman, vaibhav bhatnagar, linesh raja, ramesh chandra poonia "the mathematical and machine learning models to forecast the covid-19 outbreaks in bangladesh"
Journal of Interdisciplinary Mathematics, 2022
Keywords: Machine to Machine Data Analytics [Ref No.: 6927]
tusar saha" electronic structure transition of cubic cssncl3 under pressure: effect of rpbe and pbesol functionals and gw method"
Heliyon, 2021
[Ref No.: 6394]

tusar saha" semiconductor to metallic transition under induced pressure in cs 2 agbibr 6 double halide perovskite: a theoretical dft study for photovoltaic and optoelectronic applications"
RSC advances, 2021
[Ref No.: 6395]

tusar saha" pressure induced semiconductor to metal phase transition in cubic cssnbr3 perovskite"
AIP Advances, 2021
[Ref No.: 6396]

subrata das, sagar dutta, angkita mistry tama, ma basith "nanostructured lafeo3-mos2 for efficient photodegradation and photocatalytic hydrogen evolution"
Materials Science and Engineering: B, 2021
Keywords: Nanotechnology and Fabrication [Ref No.: 6287]

mmspt muhammad sohail, hussam alrabaiah, umair ali, fatema tuz zohra "numerical exploration of thermal and mass transportation by utilising non-fourier double diffusion theories for casson model under hall and ion slip effects"
Pramana-Journal of Physics, 2021
Keywords: Nanotechnology [Ref No.: 6274]

md. fayz-al- asad" impact of undulation on magneto-free convective heat transport in an enclosure having vertical wavy sides"
International Communications in Heat and Mass Transfer, 2021
[Ref No.: 6415]

md. fayz-al- asad" impact of a closed space rectangular heat source on natural convective flow through triangular cavity"
Results in Physics, 2021
[Ref No.: 6416]

shahnaj parvin, liton jude rozario, md. ezharul islam "vehicle number plate detection and recognition techniques: a review"
Advances in Science, Technology and Engineering Systems Journal (ASTESJ), 2021
[Ref No.: 6419]

shahnaj parvin, liton jude rozario, md. ezharul islam "vision-based on-road nighttime vehicle detection and tracking using taillight and headlight features"
Journal of Computer and Communications (JCC), 2021
[Ref No.: 6420]

md. fayz-al- asad" influence of fin length on magneto-combined convection heat transfer performance in a lid-driven wavy cavity"
Fractal and Fractional, 2021
[Ref No.: 6427]

md. fayz-al- asad" heat transport exploration of free convection flow inside enclosure having vertical wavy walls"
Journal of Applied and Computational Mechanics, 2021
[Ref No.: 6428]

md. fayz-al- asad" impact of electronic states of conical shape of indium arsenide/gallium arsenide semiconductor quantum dots"
AAM: An International Journal, 2021
[Ref No.: 6429]

md. fayz-al- asad" an analytical approach to study the blood flow over a non-linear tapering stenosed artery in flow of carreau fluid model"
Complexity, 2021
[Ref No.: 6430]

md. fayz-al- asad" new solution configurations for two different models related to the nonlinear schrodinger equation through a graded-index waveguide"
AIP Advances, 2021
[Ref No.: 6431]

md. fayz-al- asad" stable and functional solutions of the klein-fock-gordon equation with nonlinear physical phenomena"
Physica Scripta, 2021
[Ref No.: 6432]

md. fayz-al- asad" an analytical technique for solving new computational solutions of the modified zakharov-kuznetsov equation arising in electrical engineering"
Journal of Applied and Computational Mechanics, 2021
[Ref No.: 6433]

md. fayz-al- asad" the numerical investigation of the heat transport in the nanofluids under the impacts of magnetic field: application in industrial zone"
Mathematical Problem in Engineering, 2021
[Ref No.: 6434]

md. fayz-al- asad" applied mathematical modelling and heat transport investigation in hybrid nanofluids under the impact of thermal radiation: numerical analysis"
Mathematical Problem in Engineering, 2021
[Ref No.: 6435]

md. fayz-al- asad" mhd boundary layer flow over a stretching sheet: a new stochastic method"
Mathematical Problem in Engineering, 2021
[Ref No.: 6436]

md. fayz-al- asad" transient flow of jeffrey fluid over a permeable wall"
Mathematical Problem in Engineering, 2021
[Ref No.: 6437]

md. fayz-al- asad" an efficient mathematical approach for the fraction order differentiation based on future applications of chaotic parameter"
Mathematical Problem in Engineering, 2021
[Ref No.: 6438]

md. fayz-al- asad" a study of new class of star-like functions associated by symmetric (p,q) – calculus"
Journal of Mathematics, 2021
[Ref No.: 6439]

md. fayz-al- asad" variationally improve bezier surfaces with shifted knots"
Advances in Mathematical Physics, 2021
[Ref No.: 6440]

dr. mahfuza khatun" smart monitoring for anxiety, depression and cardiovascular effect in post covid-19 survivors"
22nd International Mathematics Conference, 2021
[Ref No.: 6497]

rahul biswas, shaikat das joy "the assisting pair – a new approach for assist the blind people"
International Research Journal of Modernization in Engineering Technology and Science., 2021
[Ref No.: 6506]

fardin ahmed niloy, md. nozib ud dowla, md. samiul alam, jobair hossain, fahim muntasir, shahadat hossain and md. manzurul hasan "landchain: a blockchain-based lightweight land administration system for bangladesh"
Springer, in Proceedings of the IC4IR 2021, 2021
[Ref No.: 6537]

shaikat das joy, rahul biswas "the assisting pair – a new approach for assist the blind people"
International Research Journal of Modernization in Engineering Technology and Science, 2021
Keywords: Deep Learning [Ref No.: 6738]

sharmin jahan, mohammad nurul haque, nure alam chowdhury, abdul mannan and abdullah al mamun "ion-acoustic rogue waves in double pair plasma having non-extensive particles"
universe, 2021
Keywords: Natural Sciences [Ref No.: 6730]

sharmin jahan, rubaiya khondoker shikha, abdul mannan and a a mamun "modulational instability of ion-acoustic waves in pair-ion plasma"
plasma, 2021
Keywords: Natural Sciences [Ref No.: 6731]

sharmin jahan, booshrat e. sharmin, nure alam chowdhury , abdul mannan, tanu shree roy and a a mamun "electrostatic ion-acoustic shock waves in a magnetized degenerate quantum plasma"
plasma, 2021
Keywords: Natural Sciences [Ref No.: 6728]

dr. samia mahjabin" effects of oxygen concentration variation on the structural and optical properties of reactive sputtered wox thin film"
Solar Energy, 2021
[Ref No.: 6721]

prof. dr. md. rafiqul islam" dna motif discovery using chemical reaction optimization,"
Evolutionary Intelligence, 2021
[Ref No.: 6588]

prof. dr. md. rafiqul islam" mobile robot path planning with obstacle avoidance using chemical reaction optimization"
Soft Computing,, 2021
[Ref No.: 6590]

prof. dr. md. rafiqul islam" , convolutional neural network based on hog feature for bird species detection and classification"
ASTES Journal, 2021
[Ref No.: 6591]

s. parvin, n.c. roy, l.k. saha, s. siddiqa "heat transfer characteristics of nanofluids from a sinusoidal corrugated cylinder placed in a square cavity"
Proc. Inst. Mech. Eng. C: J. Mech. Eng. Sci., 2021
[Ref No.: 6580]

n.c. roy, s. masud, s. parvin, s. roy, r.p. sharma "impact of variable thermo-physical properties on the combustion of a gas mixture past an axisymmetric body with thermal radiation"
Cleaner Engineering and Technology, 2021
[Ref No.: 6581]

s. parvin, n.c.roy, l. k. saha "magnetohydrodynamic natural convection of a hybrid nanofluid from a sinusoidal wavy cylinder placed in a curve-shaped cavity"
AIP Advances, 2021
[Ref No.: 6582]

s. parvin, n.c. roy, r.s.r. gorla "thermal ignition of a combustible over an inclined hot plate"
SN Applied Sciences volume, 2021
[Ref No.: 6583]

jahida binte islam, md. rakibul islam, mai furukawa, ikki tateishi, hideyuki kastumata, satoshi kaneco "performance of edta modified magnetic znfe2o4 during photocatalytic reduction of cr(vi) in aqueous solution under uv irradiation."
Journal of Environmental Science and Health, Part A, 2021
[Ref No.: 6613]

rajarshi roy chowdhury, sandhya aneja, nagender aneja, pg emeroylariffion abas "packet-level and ieee 802.11 mac frame-level network traffic traces data of the d-link iot devices"
Data in Brief, 2021
[Ref No.: 6756]

a. f. m. saifuddin saif "robust underwater fish detection using an enhanced convolutional neural network"
International Journal of Image, Graphics and Signal Processing, 2021
Keywords: Deep Learning,Computer Vision,Image Processing [Ref No.: 6832]

pritam khan boni "mobile robot path planning with obstacle avoidance using chemical reaction optimization"
Soft Computing, 2021
Keywords: Algorithms [Ref No.: 6057]

faruk hosain, md sarowar hossain, sony ahmed, abdullah al-ragib, md. najmol hoque, and md. shafiul islam "enhancement of in-vitro anthelmintic activity of zinc oxide nanoparticles reinforced by silver (ag) doping against pheretima posthuman"
Analytical Chemistry Letters, 2021
Keywords: Anthelmintics, Pheretima posthuma, zinc oxide, albendazole, nanoparticles [Ref No.: 6047]

anjir ahmed chowdhury, argho das, suben kumer saha, mahfujur rahman, khandaker tabin hasan "sentiment analysis of covid-19 vaccination from survey responses in bangladesh"
Cognitive Computation, 2021
[Ref No.: 6180]

ummay ayesha, a. s. m. a. mamun, md. abu sayem & md. golam hossain "factors associated with duration of breastfeeding in bangladesh: evidence from bangladesh demographic and health survey 2014"
BMC Public Health, 2021
Keywords: Public health Nutrition ,Public health Awareness [Ref No.: 6166]

oishi khanam "spatio-temporal brusselator model and biological pattern formation"
Annual Research & Review in Biology, 2021
[Ref No.: 6247]

dr. md. saef ullah miah" study of keyword extraction techniques for electric double-layer capacitor domain using text similarity indexes: an experimental analysis"
Complexity, 2021
[Ref No.: 6234]

dr. md. saef ullah miah" recommending research articles: a multi-level chronological learning-based approach using unsupervised keyphrase extraction and lexical similarity calculation"
IEEE Access, 2021
[Ref No.: 6235]

mohammad rabiul islam , prof. dr. imad fakhri al-shaikhli "interactive multimedia english learning integrated with mobile augmented reality"
International Journal of Innovative Research and Publications, 2021
Keywords: Augmented Reality [Ref No.: 5999]

shakila rahman "a deep learning-based dengue mosquito detection method using faster r-cnn and image processing techniques"
Annals of Emerging Technologies in Computing (AETiC), 2021
[Ref No.: 6015]

m d hossain, a t m k jamil, m r hasan, m a ali, i n esha, md sarowar hossain, m a hakim and m n i khan "impact of v substitution on the physical properties of ni–zn–co ferrites: structural, magnetic, dielectric and electrical properties"
Material Research Express, 2021
[Ref No.: 6049]

m.r. hassan, md. sarowar hossain, m.a. hakim, m.a. matin, m.n.i. khan, s.s. sikder "structural effect on magneto-electric properties in (1-x)bife0.9la0.1o3+xni0.6zn0.4fe1.94v0.06o4 composites"
Results in Physics, 2021
[Ref No.: 6033]

md. sarowar hossain, sankar kumar das, md. moniruzzaman, m.a. hakim, m.a. basith "frequency and temperature dependent electric polarization, relaxation, and transport properties of mo and w doped batio3"
Results in Physics, 2021
Keywords: Perovskite, Dielectric properties, Relaxor ferroelectric, Activation energy [Ref No.: 6034]

md. rabiul auwul, chongqi zhang, md. shahjaman" a robust procedure for machine learning algorithms using gene expression data"
Biointerface Research in Applied Chemistry, 2021
[Ref No.: 5660]

dr. md. rabiul auwul" identification of specific gene modules and candidate signatures in necrotizing enterocolitis disease:2 | p a g e network- based gene co-expression approach"
Biointerface Research in Applied Chemistry, 2021
[Ref No.: 5661]

dr. md. rabiul auwul "a network-based systems biology approach for identification of shared gene signatures between male and female in covid-19 datasets"
Informatics in Medicine Unlocked, 2021
[Ref No.: 5662]

dr. md. rabiul auwul "bioinformatics and multi-omics approach to identify comorbidities with application in schizophrenia with psychiatric disorders"
European Journal of Medical and Health Sciences, 2021
[Ref No.: 5663]

dr. md. rabiul auwul" network-based transcriptomic analysis identifies the genetic effect of covid-19 to chronic kidney disease patients: a bioinformatics approach"
Saudi Journal of Biological Sciences, 2021
[Ref No.: 5653]

dr. md. rabiul auwul" bioinformatics and machine learning approaches identified potential drug targets and pathways in covid-19’"
Briefings in Bioinformatics, 2021
[Ref No.: 5654]

dr. md. rabiul auwul" rmisbeta: a robust missing value imputation approach for transcriptomic and metabolomics data analysis’"
Computers in Biology and Medicine, 2021
[Ref No.: 5655]

khandaker tabin hasan, mohammed mostafizur rahman, md mortuza ahmmed, anjir ahmed chowdhury, mohammad khairul islam "4p model for dynamic prediction of covid-19: a statistical and machine learning approach"
Cognitive Computation, 2021
[Ref No.: 5627]

amena ferdosui, m mostafizur rahman, ayesha siddiqua "integrating factor for non-exact reducible to homogeneous ordinary differential equations"
Journal of Applied Mathematics and Statistical Analysis, 2021
[Ref No.: 5628]

md mortuza ahmmed, md ashraful babu, mohammad abdul hoque, m mostafizur rahman "a pls-sem approach to connect fertility, gdp, and childhood mortality with female life expectancy (fle) in bangladesh"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5629]

dr. m. mostafizur rahman "impact of covid-19 on academic and psychological aspects of undergraduate students in bangladesh: a case study"
AIUB Journal of Science and Engineering, 2021
[Ref No.: 5630]

amena ferdousi, m. mostafizur rahman, sajjadul bari "comparative analysis of heavy metals and water attribute constraints of buriganga and turag river of dhaka, bangladesh-reassess"
Research and Reviews: Journal of Environmental Sciences, 2021
[Ref No.: 5631]

ahmed shahriar sakib, md saddam hossain mukta , fariha rowshan huda,tohedul islam , mohammed eunus ali "identifying insomnia from social media posts: psycholinguistic analyses of user tweets"
JMIR, 2021
Keywords: Data Mining and Business Intelligence [Ref No.: 5611]

s. m. hasan mahmud, wenyu chen, yongsheng liu, md. abdul awal, kawsar ahmed , md. habibur rahman and mohammad ali moni "predtis: prediction of drug–target interactions based on multiple feature information using gradient boosting framework with data balancing and feature selection techniques"
briefings in bioinformatics, 2021
[Ref No.: 5617]

s m hasan mahmud, wenyu chen, yongsheng liu, md abdul awal, kawsar ahmed, md habibur rahman, mohammad ali moni "bioinformatics and system biology approach to identify the influences of sars-cov-2 infections to idiopathic pulmonary fibrosis and chronic obstructive pulmonary disease patients""
Briefings in Bioinformatics, 2021
[Ref No.: 5618]

dr. s. m. hasan mahmud" dimensionality reduction based multi-kernel framework for drug-target interaction prediction"
Chemometrics and Intelligent Laboratory System, 2021
[Ref No.: 5619]

m. a. awal, m. masud, m. s. hossain, a. a. -m. bulbul, s. m. h. mahmud and a. k. bairagi" a bayesian optimization-based machine learning framework for covid-19 detection from inpatient’s facility data"
IEEE access, 2021
[Ref No.: 5620]

md habibur rahmanmd habibur rahmanhumayan kabir ranahumayan kabir ranasilong pengshow all 7 authorsmohammad ali monimohammad ali moni" bioinformatics and system biology approaches to identify pathophysiological impact of covid-19 to the progression and severity of neurological diseases"
Computers in Biology and Medicine, 2021
[Ref No.: 5621]

4. amena ferdosui, m. mostafizur rahman and ayesha siddiqua "integrating factor for non-exact reducible to homogeneous ordinary differential equations"
Journal of Applied Mathematics and Statistical Analysis, 2021
[Ref No.: 5583]

md. mortuza ahmmed, m. mostafizur rahman, abhijit bhowmik, ayesha siddiqua "impact of covid-19 on academic and psychological aspects of undergraduate students in bangladesh: a case study"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2021
[Ref No.: 5585]

al sohan, md faruk abdullah; nahar, afroza; bin-faisal, md sajid "leach-s2: a brief approach on a proposal of an energy efficient leach routing"
International Journal of Advanced Networking and Applications, 2021
Keywords: Wireless/ Mobile Communication [Ref No.: 5751]

md sabbir, al bakin tushar , feroz riazul iqbal , sourav gupta ananda, naima hassan "web-based health monitoring system and textual mining"
International Journal of Advanced Trends in Computer Science and Engineering, 2021
Keywords: Data Mining and Business Intelligence [Ref No.: 5714]

farzana khalil, mohammad shoeb, mir mamun, tonima mustafa, nilufar nahar" dichlorodiphenyltrichloroethane (ddt) residues status in fishes and prawns of chittagong chemical complex area, bangladesh"
Bangladesh Journal of Zoology, 2021
[Ref No.: 5679]

abhijit bhowmik "impact of covid-19 on academic and psychological aspects of undergraduate students in bangladesh: a case study"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2021
[Ref No.: 5638]

mimun barid, shahadat hossain, md. mahmudur rahman and md. manzurul hasan. "sentiment analysis applying the big 5 and polarity on the icc's top odi all- rounders based on twitter."
Proceedings of the ICCIT 2021, IEEE Xplore., 2021
[Ref No.: 5687]

rafeed mohammad, md. mir hossain, shahadat hossain, md manzurul hasan, and tanvir hossain. "negative sentence detection through ai bangla voice assistant by dnn using bag-of-words."
Proceedings of BIM 2021, IEEE Computer Society Bangladesh Chapter, CNSER, IC Lab and BdREN., 2021
[Ref No.: 5689]

• nusrat jahan, j. i. khandaker s. i. liba, s. m. hoque, m. n. i. khan" structural analysis through cations distributions of diamagnetic al3+ ions substituted ni-zn-co ferrites"
Journal of Alloys and Compound, 2021
[Ref No.: 5845]

• nusrat jahan, j. i. khandaker, h. das, and m. n. i. khan" structural and magnetic properties analysis of trivalent al3+ ions substituted ni-zn-co nano-spinel ferrites"
Journal of Advances in Natural Sciences: Nanoscience and Nanotechnology, 2021
[Ref No.: 5846]

• nusrat jahan, m. n. i. khan and j. i. khandaker" exploration through structural, electrical, and magnetic properties of al3+ ions doped ni-zn-co nano spinel ferrites"
ACS Omega, 2021
[Ref No.: 5847]

dr. abdus salam" probabilistic rule learning systems: a survey"
ACM Computing Surveys, 2021
[Ref No.: 5885]

dr. abdus salam" a survey on automatically constructed universal knowledge bases"
Journal of Information Science, 2021
[Ref No.: 5886]

wardah saleh" heartbeat sensor system for remote health monitoring"
IJCA (International Journal of Computer Applications), 2021
[Ref No.: 5026]

dr. md. manzurul hasan" an analytical study of influencing factors on consumer behaviors in facebook using ann and rf"
In Proceedings of the International Conference on Intelligent Computing & Optimization (ICO’2020),, 2021
[Ref No.: 5021]

dr. md. manzurul hasan" graceful cascading labelling algorithm: construction of graceful labelling of trees"
In Proceedings of the 2nd ICREST 2021, IEEE Xplore, 2021
[Ref No.: 5022]

dr. s. m. hasan mahmud" weakly supervised image classification and pointwise localization with graph convolutional networks"
Pattern Recognition, 2021
[Ref No.: 5031]

dr. md. manzurul hasan "covid-19: myths and some possible arguments in favors or in contradictions"
International Journal of Medical Science and Health Research, 2021
[Ref No.: 5017]

prof. dr. dip nandi" investigation of facilities for an m-learning environment"
International Journal of Modern Education and Computer Science (IJMECS), 2021
[Ref No.: 5057]

md. siyamul islam" covid-19: myths and some possible arguments in favors or in contradictions"
International Journal of Medical Science and Health Research, 2021
[Ref No.: 5070]

dr. m m manjurul islam" multi-sensor fusion-based time-frequency imaging and transfer learning for spherical tank crack diagnosis under variable pressure conditions"
Measurement, 2021
[Ref No.: 5075]

dr. mohammed jashim uddin" energy conservation of bio-nanofluids past a needle in the presence of stefan blowing: lie symmetry and numerical simulation"
.Case Studies in Thermal Engineering, 2021
[Ref No.: 5073]

mohaimen- bin- noor" investigation of facilities for an m-learning environment"
International Journal of Modern Education & Computer Science, 2021
[Ref No.: 5102]

prof. dr. dip nandi" comparative analysis of three improved deep learning architectures for music genre classification"
International Journal of Information Technology and Computer Science (IJITCS), 2021
[Ref No.: 5103]

prof. dr. dip nandi" investigation of security challenges from the perspective of stakeholders in iot"
AIUB Journal of Science and Engineering [AJSE], 2021
[Ref No.: 5104]

prof. dr. dip nandi" secured question paper management system"
AIUB Journal of Science and Engineering [AJSE], 2021
[Ref No.: 5105]

md. habib ullah, haram moon, chang-sik ha "effect of phs on the structure evolution of platinum nanoclusters and their surface plasmon resonance properties"
Journal of Nanoscience and Nanotechnology, 2021
[Ref No.: 5106]

prof. dr. dip nandi" predicting spread, recovery and death due to covid-19 using a time-series model (prophet)"
AIUB Journal of Science and Engineering [AJSE], 2021
[Ref No.: 5108]

islam raiyan, uddin shihab, sakibjamil mahmud, islam md. shariful, and ahmed tanvir" an overview of image processing techniques for detecting covid-19 and other infectious diseases"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5109]

md. mortuza ahmmed "4p model for dynamic prediction of covid-19: a statistical and machine learning approach"
Cognitive Computation, 2021
[Ref No.: 5097]

md. mortuza ahmmed "direct and indirect effects of covid-19 on maternal and child health in bangladesh"
Journal of Statistics and Management Systems, 2021
[Ref No.: 5098]

2. oa beg, ft zohra, mj uddin, aim ismail, s sathasivam. "energy conservation of nanofluids from a biomagnetic needle in the presence of stefan blowing: lie symmetry and numerical simulation."
Case Studies in Thermal Engineering, 2021
[Ref No.: 5114]

4. m sohail, u ali, ft zohra, w al-kouz, ym chu, p thounthong "utilization of updated version of heat flux model for the radiative flow of a non-newtonian material under joule heating: oham application."
Open Physics, 2021
[Ref No.: 5115]

roushanara begum" numerical computation of natural ventilation system at different floor for a multistory building"
International Journal of Scientific & Engineering Research, 2021
[Ref No.: 5118]

dr. mohammad tariqul islam" preparation of activated carbon/tio2 nanohybrids for photodegradation of reactive red-35 dye using sunlight"
Photochem, 2021
[Ref No.: 5121]

dr. md. mahbub chowdhury mishu" predicting spread, recovery and death due to covid-19 using a time-series model (prophet)"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5123]

singh, v.k., arora, p., uddin, a., bhattacharya, s. "india’s rank and global share in scientific research: how publication counting method and subject selection can vary the outcomes?"
Journal of Scientific and Industrial Research (JSIR), 2021
[Ref No.: 5129]

uddin, a., hasan, md.m., islam, md.s., onik, md.m.h." factors, observed during covid covid-19 to overcome financial crisis: a case of bangladesh"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5130]

m. mahmudul hasan, george kousiouris, dimosthenis anagnostopoulos, teta stamati, peri loucopoulos, mara nikolaidou "cismet: a semantic ontology framework for regulatory-requirements-compliant information systems development and its application in the gdpr case"
International Journal on Semantic Web and Information Systems (IJSWIS), 2021
[Ref No.: 5131]

yeasmin, s., kuri, r., mahamudul hasan rana, a.r.m., ...sala uddin pathan, a.q.m., riaz, h. "multi-category bangla news classification using machine learning classifiers and multi-layer dense neural network"
International Journal of Advanced Computer Science and Applications, 2021
[Ref No.: 5136]

mohammad samawat ullah" evaluation of tsp for emergency routing"
International Journal of Information Technology and Computer Science (IJITCS), 2021
[Ref No.: 5138]

md manzurul hasan, ashraf uddin, md mehedi hassan onik, md siyamul islam "covid-19: myths and some possible arguments in favors or in contradictions"
International Journal of Medical Science and Health Research, 2021
[Ref No.: 5144]

a. onik, m. m. h., islam, m. s., hasan, m. m., & uddin "survival of bangladesh economy during covid-19 recession with the use of technology: an application of keynesian approach"
American International Journal of Supply Chain Management, 2021
[Ref No.: 5145]

dr. afroza nahar" impact of prolonged isolation from the campus on the mental health of the students during covid-19 pandemic."
AJSE, 2021
[Ref No.: 5153]

dr. md. mahbub chowdhury mishu" identification of risk of occurring skin cancer (melanoma) using convolutional neural network (cnn)"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5142]

md. mehedi hassan onik" survival of bangladesh economy during covid-19 recession with the use of technology: an application of keynesian approach"
American International Journal of Supply Chain Management, 2021
[Ref No.: 5170]

md. mehedi hassan onik" factors, observed during covid-19 to overcome financial crisis: a case of bangladesh"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5171]

md. mehedi hassan onik" covid-19: myths and some possible arguments in favors or in contradictions"
International Journal of Medical Science and Health Research, 2021
[Ref No.: 5172]

dr. khandaker tabin hasan" 4p model for dynamic prediction of the covid-19: a statistical and machine learning approach"
Cognitive Computing, Springer Nature, 2021
[Ref No.: 5205]

dr. khandaker tabin hasan" analysis and prediction of covid-19 pandemic in bangladesh by using anfis and lstm network"
Cognitive Computing, Springer Nature, 2021
[Ref No.: 5206]

dr. khandaker tabin hasan" forecasting respiratory tract infection episodes from prescription data for healthcare service planning"
International Journal of Data Science and Analytics, Springer International Publishing, 2021
[Ref No.: 5207]

a.g.m. zaman" evaluation of tsp for emergency routing"
International Journal of Information Technology and Computer Science (IJITCS), 2021
[Ref No.: 5209]

dr. md. razib hayat khan" agile fitness of software companies in bangladesh: a empirical study"
: International Journal of Advanced Computer Science and Application, 2021
[Ref No.: 5212]

dr. md. razib hayat khan" vehicular cloud computing networks: availability modeling and sensitivity analysis"
International Journal of Sensor Networks, 2021
[Ref No.: 5213]

dr. md. manzurul hasan" a secret sim switching technique to adapt the upcoming technology trends"
In Proceedings of the ICICT4SD 2021, IEEE Xplore, 2021
[Ref No.: 5224]

dr. md. manzurul hasan" survival of bangladesh economy during covid-19 recession with the use of technology: an application of keynesian approach"
American International Journal of Supply Chain Management, 2021
[Ref No.: 5225]

dr. md. manzurul hasan" factors, observed during covid-19, to overcome financial crisis: a case of bangladesh"
AIUB Journal of Science and Engineering (AJSE), AJSE, Covid-19 Special Issue, 2021
[Ref No.: 5226]

juena ahmed noshin" trifecta approach to atm transaction security"
International Journal of Computer Applications, 2021
[Ref No.: 5227]

sajib hasan" evaluation of tsp for emergency routing"
International Journal of Information Technology and Computer Science(IJITCS), 2021
[Ref No.: 5229]

dr. mohammad mahbub rabbani" dye-sensitized solar cell with plasmonic gold nanoparticles modified photoanode"
Nano-Structures & Nano-Objects, 2021
[Ref No.: 5238]

shahadat hossain, md. manzurul hasan and tanvir hossain "an empirical study on dimensionality reduction approach for f-commerce dataset by principal component analysis (accepted)"
Taylor & Francis, in Proceedings of BIM 2021, 2021
[Ref No.: 5240]

md. siyamul islam" survival of bangladesh economy during covid-19 recession with the use of technology: an application of keynesian approach"
American International Journal of Supply Chain Management, 2021
[Ref No.: 5241]

md. siyamul islam" factors, observed during covid covid-19 to overcome financial crisis: a case of bangladesh"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5242]

dr. md. sakir hossain" soft frequency reuse with allocation of resource plans based on machine learning in the networks with flying base stations"
IEEE Access, 2021
[Ref No.: 5246]

h ara, s m s al din, s a tarek , m k biswas, s m sharafuddin, s b faruque, y haque "direct albumin quantification by nanodrop and optical properties of blood plasma, iosr journal of biotechnology and biochemistry"
IOSR Journal of Biotechnology and Biochemistry, 2021
Keywords: Biomedical [Ref No.: 5398]

s. a. tarek, s. b. faruque, s. m. sharafuddin, k. m. e. hasan, a. k. m. m. hossain, h. ara, m. k. biswas, and y. haque "closed aperture cw z-scan of l-tryptophan for determination of optical nonlinearity in the thermal regime"
Journal of Optical Society of America B, 2021
[Ref No.: 5399]

md. masum billah" internet of things (iot): a review of its enabling technologies in healthcare applications, standards protocols, security, and market opportunities"
IEEE Internet of Things Journal, 2021
Keywords: Internet of Things [Ref No.: 5371]

md. masum billah" unsupervised method of clustering and labeling of the online product based on reviews"
International Journal of Modeling, Simulation, and Scientific Computing, 2021
[Ref No.: 5372]

md. faruk abdullah al sohan, dr. afroza nahar, samia yasmin "impact of prolonged isolation from the campus on the mental health of the students during covid-19 pandemic"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5373]

md. faruk abdullah al sohan, afroza nahar, md sajid bin-faisal "leach-s2: a brief approach on a proposal of an energy efficient leach routing"
International Journal of Advanced Networking and Applications, 2021
[Ref No.: 5374]

md. mortuza ahmmed, md. ashraful babu, mohammad abdul hoque, m. mostafizur rahman "a pls-sem approach to connect fertility, gdp, and childhood mortality with female life expectancy (fle) in bangladesh"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5362]

s m rahid haque, md. atik foysal, arupkumar das, md. shahidul islam leaon, dr. md. abdullah - al - jubair. "heart disease prediction using data mining classification algorithms"
Journal of Cardiovascular Disease Research, 2021
Keywords: Artificial Intelligence [Ref No.: 5349]

t. b. shams, md. sakir hossain, m. f. mahamud, m. s. tehjib, z. hossain, and m. i. pramanik" eeg-based biometric authentication using machine learning: a comprehensive survey"
ECTI Transactions on Electrical Engineering, Electronics, and Communications, 2021
Keywords: Biomedical [Ref No.: 5351]

ami akter1, anowar hosen2, md. amjad hossain3 farzana khalil4 and tonima mustafa1* "heavy metal concentrations and human health risk assessment of selected wild and cultured fishes of bangladesh"
Bangladesh Journal of Zoology, 2021
[Ref No.: 5352]

md. ismail hossen, michael goh, tee connie, and md. nazmul hossain" an approach to recognize vehicles context flow for smartphone-based outdoor parking using supervised machine learning classifiers"
AIUB Journal of Science and Engineering (AJSE), 2021
Keywords: Smart Cities,Machine to Machine Data Analytics,Artificial Intelligence [Ref No.: 5342]

beg oa, beg tv, mj uddin, khan wa "multiple slip effects on nanofluid dissipative flow in a converging/diverging channel: a numerical study"
HEAT TRANSFER ASIAN RESEARCH, 2021
Keywords: Nanotechnologies [Ref No.: 5337]

partha sutradhar, prosenjit kumer tarefder, imran prodan, md. sheikh saddi, victor stany rozario "multi - modal case study on mri brain tumor detection using support vector machine, random forest, decision tree, k - nearest neighbor, temporal convolution & tr ansfer learning"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2021
Keywords: Deep Learning,Neural Networks,Medical Imaging, Image Processing [Ref No.: 5338]

musaddiq al karim, mst. yeasmin ara, md. mahadi masnad, mostafa rasel, dip nandi "student performance classification and prediction in fully online environment using decision tree"
AIUB Journal of Science and Engineering [AJSE], 2021
Keywords: Data Mining and Business Intelligence [Ref No.: 5339]

md. mortuza ahmmed "impact of covid-19 on academic and psychological aspects of undergraduate students in bangladesh: a case study"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5340]

anjir ahmed chowdhury, dr. khandaker tabin hasan , khadija kubra shahjalal hoque "analysis and prediction of covid-19 pandemic in bangladesh by using anfis and lstm network"
Cognitive Computation, 2021
Keywords: Deep Learning,Artificial Intelligence,Fuzzy Logic [Ref No.: 5259]

dr. khandaker tabin hasan, dr. m. mostafizur rahman, md. mortuza ahmmed, anjir ahmed chowdhury, mohammad khairul islam "4p model for dynamic prediction of covid-19: a statistical and machine learning approach"
Cognitive Computation, 2021
Keywords: Deep Learning,Artificial Intelligence [Ref No.: 5260]

anjir ahmed chowdhury, sabrina kashem chowdhury, md hanif, sadia noor nosheen, md. saniat rahman zishan "design and development of citizen surveillance and social-credit information system for bangladesh"
AIUB Journal of Science and Engineering, 2021
Keywords: Deep Learning,Artificial Intelligence,Computer Vision [Ref No.: 5262]

saiful islam, muhammad hilmy alfaruqi, dimas yunianto putro, sohyun park, seokhun kim, seulgi lee, mohammad shamsuddin ahmed, vinod mathew, yang-kook sun, jang-yeon hwang, jaekook kim "in situ oriented mn deficient znmn2o4@c nanoarchitecture for durable rechargeable aqueous zinc-ion batteries"
Advanced Science, 2021
[Ref No.: 5263]

miao zhang, jacky wai keung, yan xiao, md alamgir kabir "evaluating the effects of similar-class combination on class integration test order generation"
Information and Software Technology, 2021
[Ref No.: 5272]

zhen yang, jacky keung, md alamgir kabir, xiao yu, yutian tang, miao zhang, shuo feng "acomnn: attention enhanced compound neural network for financial time-series forecasting with cross-regional features"
Applied Soft Computing, 2021
[Ref No.: 5273]

s. m. a. hakim siddiki, md. nurnobi rashed, abeda sultana touchy, md. a. r. jamil, yuan jing, takashi toyao, zen maeno and ken-ichi shimizu "hydrolysis of amides to carboxylic acids catalyzed by nb2o5"
Catalysis Science & Technology, 2021
Keywords: Sustainable production and Consumption [Ref No.: 5309]

elsayed elbayoumy, yuting wang, md. a. r. jamil, claudio trombini, masayoshi bando, zhiyi song, mostafa a. diab, farid sh. mohamed, naofumi naga and tamaki nakano "pd nanoparticles-loaded vinyl polymer gels: preparation, structure and catalysis"
Catalysts, 2021
[Ref No.: 5310]

md sajid bin-faisal" investigation of security challenges from the perspective of stakeholders in iot"
AJSE, 2021
[Ref No.: 5279]

m. s. hossain , laveet kumar , and afroza nahar" a comparative performance analysis between serpentine-flow solar water heater and photovoltaic thermal collector under malaysian climate conditions"
International Journal of Photoenergy, 2021
[Ref No.: 5324]

dr. afroza nahar" leach-s2: a brief approach on a proposal of an energy efficient leach routing"
International Journal of Advanced Networking and Applications, 2021
[Ref No.: 5503]

ahmed, s.; saif, a.f.m.s.; hanif, m.i.; shakil, m.m.n.; jaman, m.m.; haque, m.m.u.; shawkat, s.b.; hasan, j.; sonok, b.s.; rahman, f.; sabbir, h.m. "att-bil-sl: attention-based bi-lstm and sequential lstm for describing video in the textual formation"
Applied Sciences, 2021
Keywords: Deep Learning,Video Analysis [Ref No.: 5497]

s a m manzur hossain khan, nurakmal ahmad mustaffa, md. mamun habib "online education in heis in bangladesh moderated by covid-19: modified utaut2"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5465]

s a m manzur hossain khan, nurakmal ahmad mustaffa, md. mamun habib "users acceptance of mobile finance service in bangladesh and the impact of covid-19: extended utaut2"
AIUB Journal of Science and Engineering (AJSE), 2021
[Ref No.: 5467]

s a m manzur hossain khan, nurakmal ahmad mustaffa, md. mamun habib "the effect of ict & digital supply chain (dsc) in higher education institutions"
International Journal of Supply Chain Management (IJSCM), 2021
[Ref No.: 5468]

dr. kamal uddin sarker" monolithic ontological methodology (mom): an effective software project management approach"
Journal of Engineering Research (JER)., 2021
[Ref No.: 5453]

2. sohrab khan, faheemullah shaikh, mokhi maan siddiqui, tanweer hussain, laveet kumar, and afroza nahar" hourly forecasting of solar photovoltaic power in pakistan using recurrent neural networks"
International Journal of Photoenergy, 2021
[Ref No.: 5505]

m. f. mridha, abu quwsar ohi, md. abdul hamid, muhammad mostafa monowar" a study on the challenges and opportunities of speech recognition for bengali language"
Artificial Intelligence Review, 2021
[Ref No.: 5528]

m. f. mridha, m. a. h. wadud, m. a. hamid, m. m. monowar, m. abdullah-al-wadud and a. alamri" l-boost: identifying offensive texts from social media post in bengali"
IEEE Access, 2021
[Ref No.: 5530]

m. f. mridha, abu quwsar ohi, j. shin, muhammad m. kabir, md. abdul hamid, muhammad mostafa monowar" a thresholded gabor-cnn based writer identification system for indic scripts"
IEEE Access, 2021
[Ref No.: 5536]

m. f. mridha, abu quwsar ohi, muhammad mostafa monowar, md. abdul hamid, md rashedul islam *, yutaka watanobe" u-vectors: generating clusterable speaker embedding from unlabeled data"
Applied Sciences, 2021
[Ref No.: 5537]

mridha, m. f., sujoy c. das, muhammad m. kabir, aklima a. lima, md. r. islam, and yutaka watanobe" brain-computer interface: advancement and challenges"
Sensors, 2021
[Ref No.: 5538]

faris a kateb, muhammad mostafa monowar *, md. abdul hamid, m. f. mridha" fruitdet: attentive feature aggregation for real-time fruit detection in orchards"
Agronomy, 2021
[Ref No.: 5539]

m. m. kabir, m. f. mridha, j. shin, i. jahan and a. q. ohi" a survey of speaker recognition: fundamental theories, recognition methods and opportunities"
IEEE Access, 2021
[Ref No.: 5540]

a. q. ohi, m. f. mridha, m. a. hamid, m. m. monowar and f. a. kateb" fabricnet: a fiber recognition architecture using ensemble convnets"
IEEE Access, 2021
[Ref No.: 5541]

a. q. ohi, m. f. mridha, m. a. hamid and m. m. monowar" deep speaker recognition: process, progress, and challenges"
IEEE Access, 2021
[Ref No.: 5542]

m. f. mridha, aklima akter lima, kamruddin nur, sujoy chandra das, mahmud hasan, and muhammad mohsin kabir "a survey of automatic text summarization: progress, process and challenges"
IEEE Access, 2021
Keywords: Natural Language Processing [Ref No.: 5563]

md anwar hussen wadud, firoz mridha, and kamruddin nur "covid-19: risk analysis in south asia with respect to europe and north america"
AIUB Journal of Science and Engineering (AJSE), 2021
Keywords: Artificial Intelligence [Ref No.: 5564]

m. f. mridha, md. abdul hamid, muhammad mostafa monowar, ashfia jannat keya, abu quwsar ohi, md rashedul islam, jong-myon kim" a comprehensive survey on deep learning based breast cancer diagnosis"
Cancers, 2021
[Ref No.: 5532]

m. f. mridha, aklima akter lima, kamruddin nur, sujoy chandra das, mahmud hasan, and md. mohsin kabir" automatic text summarization: fundamental theories, algorithms, and challenges"
IEEE Access, 2021
[Ref No.: 5533]

m. f. mridha, ashfia jannat keya, md. abdul hamid, muhammad mostafa monowar, md. saifur rahman" a comprehensive review on fake news detection with deep learning"
IEEE Access, 2021
[Ref No.: 5534]

md junayed hasan, m. m. manjurul islam, jong-myon kim "bearing fault diagnosis using multidomain fusion-based vibration imaging and multitask learning"
Sensors, 2021
Keywords: Deep Learning [Ref No.: 5545]

m. f. mridha, abu quwsar ohi, m. ameer ali, mazedul islam emon, muhammad mohsin kabir" banglawriting: a multi-purpose offline bangla handwriting dataset"
Data in Brief, 2021
[Ref No.: 5546]

md. abdul hamid, marjia akter, m. f. mridha, muhammad mostafa monowar and madini o. alassafi" a comprehensive study on intrusion and extrusion phenomena"
International Journal of Advanced Computer Science and Applications(IJACSA), 2021
[Ref No.: 5547]

wadud m. a. h., mridha d. f., and nur d. k" covid-19: risk analysis in south asia with respect to europe and north america"
AIUB Journal of Science and Engineering [AJSE], 2021
[Ref No.: 5553]

s. oh, y. kim, m. f. mridha" optimizing energy consumption prediction models using genetic algorithms"
The Journal of Contents Computing, 2021
[Ref No.: 5554]

dr. mahfuza khatun" a new distribution-free adaptive sample size control chart for a finite production horizon and its application in monitoring fill volume of soft drink beverage bottles"
Applied Stochastic Models in Business and Industry, 2021
[Ref No.: 4426]

dipta justin gomes" discovering rules for nursery students using apriori algorithm"
Bulletin of Electrical Engineering and Informatics, 2020
[Ref No.: 4757]

aneem al ahsan rupai" discovering rules for nursery students using apriori algorithm"
Bulletin of Electrical Engineering and Informatics, 2020
[Ref No.: 4845]

md. mortuza ahmmed "depression and associated factors among undergraduate students of private universities in bangladesh: a cross-sectional study"
International Journal of Psychosocial Rehabilitation, 2020
[Ref No.: 4846]

md. masud parvez" synthesis of bismuth feraites nanoparticles by modified pechini sol-gel method"
International Journal of Science and Engineering Investigations (IJSEI), 9(101), 35-38., 2020
[Ref No.: 4878]

ohi, abu quwsar, m. f. mridha, md. abdul hamid, muhammad mostafa monowar, dongsu lee" a lightweight speaker recognition system using timbre properties"
The Journal of Contents Computing, 2020
[Ref No.: 5555]

ohi, abu quwsar, mf mridha, md. abdul hamid, muhammad mostafa monowar, md ferdous mridha" full dynamic transmission model and threat analysis of covid-19"
The Journal of Contents Computing, 2020
[Ref No.: 5556]

m. a. h. wadud, m. a. jafor, m. f. mridha, m. m. rahman" similarity measurement technique for measuring the performance of page rank algorithm based on hadoop"
International Journal of Recent Technology and Engineering (IJRTE), 2020
[Ref No.: 5557]

abu quwsar ohi, m. f. mridha, muhammad mostafa monowar, md. abdul hamid" optimal control of epidemic spread using reinforcement learning"
Scientific Reports – Nature, 2020
[Ref No.: 5535]

amena ferdousi, m. mostafizur rahman, sajjadul bari and ayesha siddiqua" assessment of heavy metals and water quality parameters of buriganga river of dhaka, bangladesh: a review"
Journal of Research in Environmental and Earth Sciences, 2020
[Ref No.: 5580]

dhiraj kumar rana, vivek mehta, shovan kumar kundu, soumen basu "development of organic-inorganic flexible pvdf-lafeo3 nanocomposites for the enhancement of electrical, ferroelectric and magnetic properties"
Materials Chemistry and Physics, 2020
Keywords: Natural Sciences,Nanotechnology,Polymer and Nano Materials [Ref No.: 5527]

rakib ul haque, m. f. mridha, md. abdul hamid, m. abdullah-al-wadud and md.saiful islam" bengali stop word and phrase detection mechanism"
Arabian Journal for Science and Engineering, 2020
[Ref No.: 5543]

abu quwsar ohi, m. f. mridha, farisa benta safir, md. abdul hamid, muhammad mostafa monowar" autoembedder: a semi-supervised dnn embedding system for clustering"
Knowledge-Based Systems, 2020
[Ref No.: 5531]

dr. md. rayhan uddin" interactive image segmentation of mars datasets using bag of features"
IEEE, 2020
[Ref No.: 5426]

dr. kamal uddin sarker" sq-framework for improving sustainability and quality into software product and process"
International Journal of Advanced Computer Science and Applications(IJACSA), 2020
[Ref No.: 5454]

dr. kamal uddin sarker" explicit specification framework to manage software project effectively."
Indian Journal of Science and Technology, 2020
[Ref No.: 5455]

dr. kamal uddin sarker" predicting student performance in higher educational institutions using video learning analytics and data mining techniques."
Applied Science, 2020
[Ref No.: 5456]

dr. kamal uddin sarker" ontological practice for software quality control"
International Journal of Business Information Systems, 2020
[Ref No.: 5457]

rubyet hossain, debashish sarker, sumya sultana meem, khondoker shahrina, md al-amin" analysis of centralized payment eco-system: a systematic review on e-payments"
International Journal of Advanced Science and Technology, 2020
[Ref No.: 5498]

shuo feng, jacky keung, xiao yu, yan xiao, kwabena ebo bennin, md alamgir kabir, miao zhang "coste: complexity-based oversampling technique to alleviate the class imbalance problem in software defect prediction"
Information and Software Technology, 2020
[Ref No.: 5271]

md. a. r. jamil, abeda sultana touchy, sharmin sultana poly, md. nurnobi rashed, s. m. a. hakim siddiki, takashi toyao, zen maeno, and ken-ichi shimizu "high-silica hβ zeolite catalyzed methanolysis of triglycerides to form fatty acid methyl esters (fames)"
Fuel Processing Technology (FPT), 2020
[Ref No.: 5317]

m. a. hossaina, s. m. a. hakim siddikib, m. eliasa, m. m. rahman and md. a. r. jamil "highly β-selective glycosylation reactions for the synthesis of ω-functionalized alkyl β-maltoside as a co-crystallizing detergent"
Russian Journal of Organic Chemistry, 2020
[Ref No.: 5311]

dimas yuniantoputroa1muhammad hilmyalfaruqiab1saifulislamaseokhunkimasohyunparkaseulgileeajang-yeonhwangayang-kooksuncjaekookkima "quasi-solid-state zinc-ion battery based on α-mno2 cathode with husk-like morphology"
Electrochimica Acta, 2020
[Ref No.: 5299]

vinod mathewvinod mathew department of materials science and engineering, chonnam national university, gwangju 500-757, republic of korea more by vinod mathew , balaji sambandam, seokhun kim, sungjin kim, sohyun park, seulgi lee, muhammad hilmy alfaruqi, vaiyapuri soundharrajan, saiful islam, dimas yunianto putro, jang-yeon hwang, yang-kook sun, and jaekook kim* "manganese and vanadium oxide cathodes for aqueous rechargeable zinc-ion batteries: a focused view on performance, mechanism, and developments"
ACS Energy Letter, 2020
[Ref No.: 5300]

vaiyapurisoundharrajan, balaji sambandam, sungjin kim,saiful islam, jeonggeunjoaseokhunkimavinodmathewayang-kooksunbjaekookkima "the dominant role of mn2+ additive on the electrochemical reaction in znmn2o4 cathode for aqueous zinc-ion batteries"
Energy Storage Materials, 2020
[Ref No.: 5301]

anjir ahmed chowdhury, sabrina kashem chowdhury, md hanif, sadia noor nosheen, md. saniat rahman zishan "yolo-based enhancement of public safety on roads and transportation in bangladesh"
AIUB Journal of Science and Engineering, 2020
Keywords: Deep Learning,Artificial Intelligence,Computer Vision [Ref No.: 5261]

s. a. tarek, s. b. faruque, s. m. sharafuddin, h. ara, y. hoque "uv-visible absorption spectroscopy and z-scan analysis along with corresponding molecular electronic structure analysis at dft level for l-tyrosine"
IOSR Journal of Applied Chemistry, 2020
[Ref No.: 5397]

md. asiful islam" precision agriculture in bangladesh: need and opportunities"
International Journal of Advanced Science and Technology, 2020
[Ref No.: 5243]

shahrin chowdhury" sha-256 in parallel blockchain technology: storing land related documents"
International Journal of Computer Applications (IJCA), 2020
[Ref No.: 5239]

md. masud parvez , md. ehasanul haque , munaly akter , humayra ferdous "synthesis of bismuth ferrite nanoparticles by modified pechini sol-gel method"
International Journal of Science and Engineering Investigations (IJSEI), 2020
[Ref No.: 5222]

munaly akter , md. masud parvez , md. ehasanul haque, humayra ferdous, md. abdul matin "fabrication of carbon nanotube (cnt) by chemical vapor deposition and investigate the second harmonic response from cnt/peptide and si/sio2/peptide interfaces."
International Journal of Science and Engineering Investigations (IJSEI), 2020
[Ref No.: 5223]

dr. mohammad mahbub rabbani" electrochemical and structural characterization of polyacrylonitrile (pan)–based gel polymer electrolytes blended with tetrabutylammonium iodide for possible application in dye-sensitized solar cells"
Ionics, 2020
[Ref No.: 5235]

dr. mohammad mahbub rabbani" silicone-enriched surface of immersed polyurethane-poss antifouling coating"
International Journal of Polymer Analysis and Characterization, 2020
[Ref No.: 5236]

dr. mohammad mahbub rabbani" effect on human health by residues of commonly used pesticides in vegetables cultivation"
AIUB Journal of Science and Engineering (AJSE), 2020
[Ref No.: 5237]

sajib hasan" finding gaps between human intentions and actions"
International Journal of Innovative Science and Research Technology, 2020
[Ref No.: 5230]

sajib hasan" a model of interactive traffic management system and traffic data analysis"
International Journal of Innovative Science and Research Technology, 2020
[Ref No.: 5231]

md. anwarul kabir" an innovative program management"
ICCA, 2020, AIUB, 2020
[Ref No.: 5219]

rifat tasnim anannya" mitigating cyber-threat in the financial industry of bangladesh using biometric based public key infrastructure (pki) with the help of digital certification"
International Journal of Engineering and Management Research., 2020
[Ref No.: 5215]

rifat tasnim anannya" plant health monitoring system using iot"
: International Journal of Computer Applications, 2020
[Ref No.: 5216]

dr. s. mosaddeq ahmed" michael 1:1 adducts by acid catalyzed reaction during synthesis of spiro and spiroketal compounds"
Bangladesh Journal of Scientific and Industrial Research, 2020
[Ref No.: 5210]

dr. md. razib hayat khan" comprehending relation between contribution and career development"
International Journal of Advanced Trends in Computer Science and Engineering, 2020
[Ref No.: 5211]

a.g.m. zaman" experimental comparison of mutation testing tools for c sharp language"
International Journal of Education and Management Engineering (IJEME), 2020
[Ref No.: 5208]

dr. kamrun nahar mukta" evoked response activity eigenmode analysis in a convoluted cortex via neural field theory"
Physical Review E, 2020
[Ref No.: 5202]

sajjadul bari" comparative analysis of heavy metals and water attribute constraints of buriganga and turag river of dhaka, bangladesh-reassess"
Journal of Environmental Sciences, 2020
[Ref No.: 5193]

sajjadul bari" exactness: a generalized approach to solve 1st order 1st degree ordinary differential equations"
Journal of Applied Mathematics and Statistical Analysis, 2020
[Ref No.: 5194]

dr. md. sohidul islam" fundamental capacity analysis for identically independently distributed nakagami-q fading wireless communication"
International Journal of Advanced Computer Science and Applications, 2020
[Ref No.: 5176]

dr. md. sohidul islam" design and analysis of a highly sensitive octagonal hollow core photonic crystal fiber for chemical sensing"
Journal of Nanophotonics, 2020
[Ref No.: 5177]

dr. md. sohidul islam" data rate limit in low and high snr regime for nakagami-q fading wireless channel"
International Journal of Advanced Computer Science and Applications, 2020
[Ref No.: 5178]

sajjadul bari" on gradient descent and co-ordinate descent methods and its variants."
AIUB Journal of Science and Engineering (AJSE), 2020
[Ref No.: 5180]

sajjadul bari" assessment of heavy metals and water quality parameters of buriganga river of dhaka, bangladesh: a review"
Journal of Research in Environmental and earth sciences, 2020
[Ref No.: 5181]

sajjadul bari" effluence, deposit transport and dredging of the karnaphuli river – a review"
International Journal of Progressive Sciences and Technologies (IJPSAT), 2020
[Ref No.: 5182]

dr. debajyoti karmaker" budgerigars adopt robust, but idiosyncratic flight paths"
Nature, Scientific reports, 2020
[Ref No.: 5183]

md. mehedi hassan onik" major challenges in combating epidemics like covid-19 in the developing countries"
International Journal of Medical Science in Clinical Research and Review, 2020
[Ref No.: 5173]

prof. dr. kh. abdul maleque" similarity requirements for mixed convective boundary layer flow over vertical curvilinear porous surfaces with heat generation/absorption"
International Journal of Aerospace Engineering, 2020
[Ref No.: 5126]

kumari, r., uddin, a., lee, b.-h., choi, k. "analyzing the factors influencing the waiting time to first citation and long-term impact of publications"
Journal of Scientometric Research, 2020
[Ref No.: 5127]

dr. ashraf uddin "major challenges in combating epidemics like covid-19 in the developing countries"
International Journal of Medical Science in Clinical Research and Review, 2020
[Ref No.: 5128]

farzana khalil, maliyat tarannum maruf, mohammad tariqul islam, mohammad mahbub rabbani, s. mosaddeq ahmed" effect on human health by residues of commonly used pesticides in vegetables cultivation"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2020
[Ref No.: 5119]

dr. hossain md. shakhawat" automatic quality evaluation of whole slide images for the practical use of whole slide imaging scanner"
ITE Trans. on MTA, 2020
[Ref No.: 5112]

roushanara begum" numerical computation of natural ventilation system at the top floor of a multistory building in dhaka city"
Journal of Bangladesh Academy of Science, 2020
[Ref No.: 5116]

dr. mohammad tariqul islam" effect on human health by residues of commonly used pesticides in vegetables cultivation"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2020
[Ref No.: 5117]

juena ahmed noshin" automated detection of diabetic retinopathy using deep residual learning"
International Journal of Computer Applications, 2020
[Ref No.: 5091]

dr. s. a. m. manzur h. khan" change management for information system in public service"
the International Supply Chain Technology Journal, 2020
[Ref No.: 5092]

dipta justin gomes" a comprehensive study of real-time vacant parking space detection towards the need of a robust model"
AIUB Journal of Science and Engineering (AJSE), 2020
[Ref No.: 5096]

dr. mohammed jashim uddin" numerical study of self-similar natural convection mass transfer from a rotating cone in anisotropic porous media with stefan blowing and navier slip. 8"
Indian Journal of Physics,, 2020
[Ref No.: 5072]

dr. mohammed jashim uddin" numerical investigation of von karman swirling bioconvective nanofluid transport from a rotating disk in a porous medium with stefan blowing and anisotropic slip effects."
Journal of Mechanical Engineering Science (2020)., 2020
[Ref No.: 5066]

dr. mohammed jashim uddin" magnetohydrodynamic bio-nano-convective slip flow with stefan blowing effects over a rotating disc"
. Journal of Nanomaterials, Nanoengineering and Nanosystems, 2020
[Ref No.: 5067]

md. siyamul islam" major challenges in combating epidemics like covid-19 in the developing countries"
International Journal of Medical Science in Clinical Research and Review, 2020
[Ref No.: 5068]

dr. mohammed jashim uddin" non-similar solution of g-jitter induced unsteady magnetohydrodynamic radiative slip flow of nanoflud"
Applied Sciences, 2020
[Ref No.: 5069]

dr. s. m. hasan mahmud" risk-based test case prioritization by correlating system methods and their associated risks"
Arabian Journal for Science and Engineering, 2020
[Ref No.: 5034]

dr. mohammed jashim uddin" boundary layer flow of a nanofluid past a horizontal flat plate in a darcy porous medium: a lie group approach"
Journal of Mechanical Engineering Science, 2020
[Ref No.: 5061]

prattoy majumder , a. r. m. fahim , nusrat haque supti , md. manzurul hasan "criminal behavior analysis for questionable vehicle detection"
Proceedings of the ICCA2020, ACM Digital Library, 2020
[Ref No.: 5018]

mohaimen-bin-noor , md. manzurul hasan "antimagic labelling of any perfect binary tree"
Proceedings of the ICCA2020, ACM Digital Library, 2020
[Ref No.: 5019]

authors: anika tahsin , md. manzurul hasan "a descriptive research on big data evolution and a proposed combined platform by integrating r and python on hadoop for big data analytics and visualization"
Proceedings of the ICCA 2020, ACM Digital Library, 2020
[Ref No.: 5020]

dr. md. asraf ali" the future of electronic voting system using blockchain"
International Journal of Scientific & Technology Research, 2020
[Ref No.: 4986]

md. mortuza ahmmed "disparities in maternal and newborn health interventions in bangladesh: evidence from the latest demographic and health survey"
ANNALS OF TROPICAL MEDICINE AND HEALTH, 2020
[Ref No.: 4990]

sifat rahman ahona" efficient positioning of data aggregation point for wireless sensor network"
International Journal of Computer Applications, 2020
[Ref No.: 5009]

md. masud parvez" fabrication of carbon nanotube (cnt) by chemical vapor deposition and investigate the second harmonic response from cnt/peptide and si/sio2/peptide interfaces."
International Journal of Science and Engineering Investigations (IJSEI), 9(101), 39-45., 2020
[Ref No.: 5010]

md. masud parvez" synthesis of carbon nanotube by chemical vapor deposition (cvd) method"
Scientific Research Journal (Scirj), 2020
[Ref No.: 5011]

dr. md. manzurul hasan "major challenges in combating epidemics like covid-19 in the developing countries"
International Journal of Medical Science in Clinical Research and Review, 2020
[Ref No.: 5016]

dr. s. m. hasan mahmud" spatial division networks for weakly supervised detection"
Neural Computing and Applications, 2020
[Ref No.: 5032]

dr. s. m. hasan mahmud" prediction of drug-target interaction based on protein features using undersampling and feature selection techniques with boosting"
analytical biochemistry, 2020
[Ref No.: 5028]

dr. s. m. hasan mahmud" detection of molecular signatures and pathways shared in inflammatory bowel disease and colorectal cancer: a bioinformatics and systems biology approach"
Genomics, 2020
[Ref No.: 5029]

dr. s. m. hasan mahmud" deepaction: a deep learning-based method for predicting novel drug-target interactions"
analytical biochemistry, 2020
[Ref No.: 5030]

dr. s. m. hasan mahmud" network-based identification genetic effect of sars-cov-2 infections to idiopathic pulmonary fibrosis (ipf) patients"
Briefings in Bioinformatics, 2020
[Ref No.: 5036]

md. mazid-ul-haque and md. sohidul islam "data rate limit in low and high snr regime for nakagami-q fading wireless channel"
International Journal of Advanced Computer Science and Applications(IJACSA), 2020
Keywords: Wireless/ Mobile Communication [Ref No.: 5024]

siam bin shawkat, md. mazid-ul-haque, md. sohidul islam and borshan sarker "fundamental capacity analysis for identically independently distributed nakagami-q fading wireless communication"
International Journal of Advanced Computer Science and Applications(IJACSA), 2020
Keywords: Wireless/ Mobile Communication [Ref No.: 5025]

sifat rahman ahona" a prediction algorithm for cloud integrated smart parking system to search vacant parking spot using internet of things"
International Journal of Computer Applications, 2020
[Ref No.: 4927]

sifat rahman ahona" mitigating cyber-threat in the financial industry of bangladesh using biometric based public key infrastructure (pki) with the help of digital certification"
International Journal of Engineering and Management Research, 2020
[Ref No.: 4928]

dr. md. abdullah - al - jubair" a concept: classifying student’s feedback electronically for improving academics"
ACM Digital Library, 2020
[Ref No.: 4934]

md. mortuza ahmmed "a brief overview of the classical transportation problem"
JOURNAL OF XI'AN UNIVERSITY OF ARCHITECTURE & TECHNOLOGY, 2020
[Ref No.: 4935]

dr. md. abdullah - al - jubair" extracting relevant information using handheld augmented reality"
ACM Digital Library, 2020
[Ref No.: 4937]

dr. md. abdullah - al - jubair" electronic opinion analysis system for library (e-oasl)"
ACM Digital Library, 2020
[Ref No.: 4938]

mohaimen- bin- noor" iot (internet of things) - based smart garbage management system: a proposal for major cities of bangladesh"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2020
[Ref No.: 4947]

dr. s. mosaddeq ahmed" soil organic carbon pool and its storage in arial beel wetland soils of bangladesh"
American Journal of Environmental Sciences, 2020
[Ref No.: 4948]

dr. s. mosaddeq ahmed" one pot synthesis of biginelli 3,4-dihydro-1h-pyrimidin-2-ones and 1,2,3,4-tetrahydro pyrimidines, bangladesh j. sci. ind. res. 2020, 55(3), 173-180."
Bangladesh Journal of Scientific and Industrial Research, 2020
[Ref No.: 4949]

dr. s. mosaddeq ahmed" effect on human health by residues of commonly used pesticides in vegetables cultivation"
AIUB Journal of Science and Engineering (AJSE), 2020
[Ref No.: 4950]

dr. md. sakir hossain" healthcare informatics and analytics in big data"
Expert Systems with Applications (Wiley), 2020
[Ref No.: 4996]

dr. md. sakir hossain" privacy preserving big data analytics: a critical analysis of state‐of‐the‐art"
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discov, 2020
[Ref No.: 4997]

dr. md. mozahar ali" physical properties of a novel boron-based ternary compound ti2inb2"
Materials Today Communications, 2020
[Ref No.: 5667]

dr. md. mozahar ali" dft investigations into the physical properties of a mab phase cr4alb4"
Journal of Alloys and Compound, 2020
[Ref No.: 5668]

rifath mahmud, a. f. m. saifuddin saif, dipta gomes "a comprehensive study of real-time vacant parking space detection towards the need of a robust model"
AIUB Journal of Science and Engineering (AJSE), 2020
Keywords: Smart Cities,Image Processing [Ref No.: 5727]

amena ferdosui, m. mostafizur rahman, sajjadul bari" exactness: a generalized approach to solve 1st order 1st degree ordinary differential equations"
Journal of Applied Mathematics and Statistical Analysis, 2020
[Ref No.: 5623]

amena ferdousi, m. mostafizur rahman, sajjadul bari, ayesha siddiqua" assessment of heavy metals and water quality parameters of buriganga river of dhaka, bangladesh: a review"
Journal of Research in Environmental and Earth Sciences, 2020
[Ref No.: 5624]

amena ferdousi, m mostafizur rahman, mohammad abdur rob, muhammad mahfuz hasan "researches in effluence and environmental flow of turag river–a review"
AIUB Journal of Science and Engineering (AJSE), 2020
[Ref No.: 5625]

gollam rabby, saiful azad, mufti mahmud, kamal z zamli, mohammed mostafizur rahman "teket: a tree-based unsupervised keyphrase extraction technique"
Cognitive Computation, 2020
[Ref No.: 5626]

12) abhijit bhowmik, md saef ullah miah, mohaimen-bin-noor "analysis iot (internet of things) - based smart garbage management system: a proposal for major cities of bangladesh"
AIUB Journal of Science and Engineering, 2020
[Ref No.: 5637]

dr. md. rabiul auwul" comparative study of k-means, partitioning around medoids, agglomerative hierarchical, and diana clustering algorithms by using cancer datasets"
Biomedical Statistics and Informatics, 2020
[Ref No.: 5664]

abhishek bagchi, suman sarka, sandip bysakh, chandra sekhar tiwary, md sarowar hossain, susenjit sarkar, p.k. mukhopadhyay "microstructural evolution and its outcome on the photo induced micro actuation effect and mechanical properties of copper doped co-ni-al fsma"
Journal of Alloys and Compounds, 2020
[Ref No.: 6035]

dr. md. saef ullah miah" demography of startup software companies: an empirical investigation on the success and failure"
International Journal of Computer Applications, 2020
[Ref No.: 6232]

dr. md. saef ullah miah" iot (internet of things) - based smart garbage management system: a proposal for major cities of bangladesh"
AIUB Journal of Science and Engineering (AJSE), 2020
[Ref No.: 6233]

5. ayesha, u., islam, m. n., hossain, m. r tasmia, s. a. and hossain, m. g. "a statistical study on initial breastfeeding among mothers in patuakhali district, bangladesh"
International Journal of Statistical Sciences, 2020
Keywords: Public health Awareness [Ref No.: 6167]

gour chandra paul, sukumar senthilkumar, hafijur rahman "on the implementation of novel rkarms(4,4) algorithm to study the structures of initial extrasolar giant protoplanets"
Heliyon, 2020
[Ref No.: 6194]

md. rakibul islam, jahida binte islam, mai furukawa, tateishi, hideyuki katsumata, satoshi kaneco" photocatalytic degradation of a systemic herbicide: picloram from aqueous solution using titanium oxide (tio2) under sunlight"
ChemEngineering, 2020
[Ref No.: 6614]

moushumi zaman bonny, mohammad shorif uddin" a technique for panorama-creation using multiple images"
International Journal of Advanced Computer Science and Applications (IJACSA), 2020
[Ref No.: 6617]

dr. moushumi zaman bonny" a hybrid-binarization approach for degraded document enhancement"
Journal of Computer and Communications, 2020
[Ref No.: 6618]

prof. dr. md. rafiqul islam" an efficient method for extraction and recognition of bangla characters from vehicle license plates,"
Multimedia Tools and Applications, 2020
[Ref No.: 6589]

dr. jahida binte islam "formic acid motivated photocatalytic reduction of cr(vi) to cr(iii) with znfe2o4 nanoparticles under uv irradiation"
Environmental Technology, 2020
[Ref No.: 6610]

dr. jahida binte islam "photocatalytic degradation of a typical neonicotinoid insecticide: nitenpyrum by zno nanoparticles under solar irradiation"
Environmental Science and Pollution Research, 2020
[Ref No.: 6611]

jahida binte islam, mai furukawa, ikki tateishi, hideyuki katsumata, satoshi kaneco "photocatalytic degradation of a typical agricultural chemical: metalaxyl in water using tio2 under solar irradiation"
SN Applied Sciences, 2020
[Ref No.: 6612]

prof. dr. md. rafiqul islam" optimization of protein folding using chemical reaction optimization in hp cubic lattice model,"
Neural Computing and Applications, 2020
[Ref No.: 6586]

dr. samia mahjabin" perceiving of defect tolerance in perovskite absorber layer for efficient perovskite solar cell"
IEEE Access, 2020
[Ref No.: 6719]

s. jahan, a. mannan n. a. chowdhury, and a. a. mamun "dust-acoustic rogue waves in four-component plasmas"
Plasma Physics Reports, 2020
Keywords: Other [Ref No.: 6724]

prof. dr. md. rafiqul islam" an enhanced mser pruning algorithm for detection and localization of bangla texts from scene images"
The International Arab Journal of Information Technology (IAJIT), 2020
[Ref No.: 6557]

prof. dr. md. rafiqul islam" rna secondary structure prediction with pseudoknots using chemical reaction optimization algorithm"
IEEE/ACM Transactions on Computational Biology and Bioinformatic, 2020
[Ref No.: 6558]

samira salam, md. abul kalam azad, md. abdus salam, mohammad m. islam" rural to urban migration and realization of expected better life in bangladesh: an empirical study in rajshahi city corporation"
International Journal of Asian Social Science, 2020
[Ref No.: 6561]

samira salam, rehena parveen, s.m. nasim azad, md. abdus salam "understanding the performance of domestic biodigesters in bangladesh: a study from household level survey"
Business and Management Studies, 2020
[Ref No.: 6562]

samira salam , rehana parvin , md. abdus salam , s. m. nasim azad "feasibility study for biogas generation from household digesters in bangladesh: evidence from a household level survey"
International Journal of Energy Economics and Policy, 2020
[Ref No.: 6563]

samira salam, bipasha aktar "child marriage in rural bangladesh and its consequences on reproductive and maternal health: an empirical study"
European Journal of Medical and Health Sciences, 2020
[Ref No.: 6564]

murshed ahmed ovi, tajnin rahman, md kamruzzaman "pressure gradient effects on fluid flow through a rotating straight square duct under magnetic field"
Journal of Multidisciplinary Engineering Science and Technology (JMEST), 2020
Keywords: Other [Ref No.: 6504]

shahnaj parvin, md. ezharul islam, liton jude rozario "nighttime vehicle detection methods based on brake light/taillight features: a review"
International Journal of Computer Science and Information Security (IJCSIS), 2020
[Ref No.: 6421]

md. fayz-al- asad" effect of fin length and location on natural convection heat transfer in a wavy cavity"
International Journal of Thermofluid Science and Technology, 2020
[Ref No.: 6412]

tarikul islam, nazma parveen, md. fayz-al-asad" hydromagnetic natural convection heat transfer of copper- water nanofluid within a right-angled triangular cavity"
International Journal of Thermofluid Science and Technology, 2020
[Ref No.: 6413]

md. fayz-al- asad" numerical study of magnetohydrodynamic natural convection heat transfer and fluid flow of nanofluid in a skewed cavity"
Journal of Engineering Mathematics & Statistics, 2020
[Ref No.: 6414]

md. fayz-al-asad, m.m.a. sarker, m.j.h. munshi" numerical investigation of natural convection flow in a hexagonal enclosure having vertical fin"
Journal of Scientific Research, 2019
[Ref No.: 6409]

md. fayz-al-asad, m.m.a. sarker, m.j.h. munshi, r.k. bhowmik" mhd free convection heat transfer having vertical fin in a square wavy cavity"
International Journal of Statistics and Applied Mathematics, 2019
[Ref No.: 6410]

r.k. bhowmik, md. fayz-al-asad, m.r. karim" soliton solution of korteweg-de vries equation"
International Journal of Statistics and Applied Mathematics, 2019
[Ref No.: 6411]

angkita mistry tama,subrata das, sagar dutta, m. d. i. bhuyana, m. n. islam and m. a. basith "mos2 nanosheet incorporated α-fe2o3/zno nanocomposite with enhanced photocatalytic dye degradation and hydrogen production ability"
RSC Advances, 2019
Keywords: Nanotechnology and Fabrication [Ref No.: 6285]

▪ subrata das, angkita mistry tama, sagar dutta, md. shahjahan ali, mohammed abdul basith "facile high-yield synthesis of mos2 nanosheets with enhanced photocatalytic performance using ultrasound driven exfoliation technique"
Materials Research Express, 2019
Keywords: Nanotechnology and Fabrication [Ref No.: 6286]

dr. razuan karim "bangladeshi license plate recognition using adaboost classifier"
Joint 8th International Conference on Informatics, Electronics & Vision (ICIEV), 2019
Keywords: Internet of Things [Ref No.: 6531]

prof. dr. md. rafiqul islam" chemical reaction optimization for rna structure prediction"
Applied Intelligence, 2019
[Ref No.: 6536]

prof. dr. md. rafiqul islam" generalized vertex cover using chemical reaction optimization"
Applied Intelligence, 2019
[Ref No.: 6549]

prof. dr. md. rafiqul islam" transportation scheduling optimization by a collaborative strategy in supply chain management with tpl using chemical reaction optimization,"
Neural Computing and Applications, 2019
[Ref No.: 6550]

prof. dr. md. rafiqul islam" chemical reaction optimization: survey on variants"
Evolutionary Intelligence, 2019
[Ref No.: 6551]

s. jahan,∗ n. a. chowdhury, a. mannan, and a. a. mamun "modulated dust-acoustic wave packets in an opposite polarity dusty plasma system"
Communications in Theoretical Physics (CTP), 2019
Keywords: Other [Ref No.: 6723]

jahidabinte islam, mai furukawa, ikki tateishi, hideyuki katsumata, satoshi. kaneco "photocatalytic reduction of hexavalent chromium with nanosized tio2 in presence of formic acid"
Chemengineering, 2019
[Ref No.: 6608]

dr. jahida binte islam" enhanced photocatalytic reduction of toxic cr (vi) with cu modified zno nanoparticles in presence of edta under uv illumination"
SN Applied Sciences, 2019
[Ref No.: 6609]

n.c. roy, s. parvin "laminar boundary layer flow of a combustible gas over a semi-infinite porous surface"
SN Applied Sciences, 2019
[Ref No.: 6584]

n.c. roy, t. rahman, s. parvin "boundary-layer separations of mixed convection flow past an isothermal circular cylinder"
Int. J. Appl. Comput. Math., 2019
[Ref No.: 6585]

akash mamon sarkar, akml rahman, abdus samad, arjun chandra bhowmick, jahida binte islam "surface and ground water pollution in bangladesh: a review"
Asian Review of Environmental and Earth Sciences, 2019
[Ref No.: 6606]

md. sarowar hossain, tanmoy ghosh, bhoguju rajini kanth, pratip k. mukhopadhyay" effect of annealing on the structural and magnetic properties of conial fsma"
Crystal Research and Technology, 2019
[Ref No.: 6019]

md. sarowar hossain, gokul p, barnana pal and p k mukhopadhyay "correlation of dynamic elastic properties of a heat treated conial alloy system with its microstructural changes"
Shape Memory and Superelasticity journal, 2019
[Ref No.: 6029]

tumian mohammad rabiul islam∗, imad fakhri al-shaikhli, rizal mohd nor and afidalina "neural network and principal component analysis based numerical data analysis for stock market prediction with machine learning techniques."
Journal of Computational and Theoretical Nanoscience, 2019
Keywords: Machine to Machine Data Analytics [Ref No.: 6000]

md. anwarul kabir" introducing refined agile model (ram) in the context of bangladesh's software development environment concentrating on the improvement of requirement engineering process"
International Journal of Software Engineering & Applications (IJSEA),, 2019
Keywords: Software processes and methodologies [Ref No.: 5994]

dr. md. mozahar ali" first−principles study: structural, mechanical, electronic and thermodynamic properties of simple−cubic−perovskite (ba0.62k0.38) (bi0.92mg0.08)o3"
Solid State Communications, 2019
[Ref No.: 5669]

ayesha siddiqua" heatline analysis for mixed convection flow of nanofluid in a two sided lid-driven cavity with a heat generating block: effect of reynolds number"
AIP Conference Proceedings, 2019
[Ref No.: 5004]

dr. md. asraf ali" a review on crosstalk in myographic signals. a review on crosstalk in myographic signals"
European Journal of Applied Physiology, 2019
[Ref No.: 4985]

dr. dilruba yasmin" analysis of dynamic interactions in a bubble-particle system in presence of an acoustic field"
Minerals Engineering, 2019
[Ref No.: 4923]

dr. md. saiful islam" oblique propagation of ion-acoustic solitary wave in a magnetized plasma with electrons following a generalized distribution function"
Physics of Plasmas, 2019
[Ref No.: 4904]

md mehedi hasan and sungoh kwon "cluster-based load balancing algorithm for ultra-dense heterogeneous networks"
IEEE Access, 2019
Keywords: Networking,Wireless/ Mobile Communication,5G Networks [Ref No.: 4908]

dr. s. m. hasan mahmud" idti-cssmoteb: identification of drug{target interaction based on drug chemical structure and protein sequence using xgboost with over-sampling technique smote"
IEEE Access, 2019
[Ref No.: 5027]

fatema t. zohra, mohammed j. uddin, ahamd i. m. ismail "magnetohydrodynamic bio-nanoconvective naiver slip flow of micropolar fluid in a stretchable horizontal channel"
Heat Transfer-Asian Research, 2019
Keywords: Nanotechnology and Fabrication [Ref No.: 4994]

5. f tuz zohra, mj uddin, mf basir, aim ismail. "magnetohydrodynamic bio-nano-convective slip flow with stefan blowing effects over a rotating disc"
Proc. Inst. Mech. Eng. Part N J. Nanomater. Nanoeng. Nanosyst, 2019
[Ref No.: 4995]

dr. s. m. hasan mahmud" cpn-based test case generation approach for testing bpel-based web services composition"
Journal of Engineering and Applied Sciences, 2019
[Ref No.: 5037]

dr. s. m. hasan mahmud" version specific test case prioritization approach based on artificial neural network"
Journal of Intelligent & Fuzzy Systems, 2019
[Ref No.: 5033]

dr. mohammed jashim uddin" influence of variable viscosity and thermal conductivity, hydrodynamic, and thermal slips on magnetohydrodynamic micropolar flow: a numerical study"
Heat Transfer—Asian Research, 2019
[Ref No.: 5062]

dr. mohammed jashim uddin" magnetohydrodynamic bio‐nanoconvective naiver slip flow of micropolar fluid in a stretchable horizontal channel."
Heat Transfer—Asian Research,, 2019
[Ref No.: 5063]

dr. mohammed jashim uddin" numerical solution of bio-nano-convection transport from a horizontal plate with blowing and multiple slip effects"
Journal of Mechanical Engineering Science, 2019
[Ref No.: 5065]

dr. s. m. hasan mahmud" an efficient deep learning model to infer user demographic information from ratings"
IEEE Access, 2019
[Ref No.: 5035]

dr. mohammed jashim uddin" stefan blowing and slip effects on unsteady nanofluid transport past a shrinking sheet: multiple solutions."
Heat Transfer—Asian Research 48, no. 6 (2019):, 2019
[Ref No.: 5058]

dr. mohammed jashim uddin" unsteady mhd bio-nanoconvective anistropic slip flow past a vertical rotating cone."
Thermal Science, 2019
[Ref No.: 5059]

dr. m m manjurul islam" an improved algorithm for selecting imf components in ensemble empirical mode decomposition for domain of rub-impact fault diagnosis"
IEEE Access, 2019
[Ref No.: 5076]

dr. m m manjurul islam" vision-based autonomous crack detection of concrete structures using a fully convolutional encoder–decoder network"
Sensors, 2019
[Ref No.: 5077]

dr. m m manjurul islam" electricity theft detection in smart grid systems: a cnn-lstm based approach"
Engergies, 2019
[Ref No.: 5078]

dr. m m manjurul islam" acoustic spectral imaging and transfer learning for reliable bearing fault diagnosis under variable speed conditions"
Measurement, 2019
[Ref No.: 5079]

dr. m m manjurul islam" automated bearing fault diagnosis scheme using 2d representation of wavelet packet transform and deep convolutional neural network"
Computers in Industry, 2019
[Ref No.: 5080]

dr. m m manjurul islam" leakage detection of a spherical water storage tank in a chemical industry using acoustic emissions"
Applied Sciences, 2019
[Ref No.: 5081]

dr. hossain md. shakhawat" automatic quantification of her2 gene amplification in invasive breast cancer from chromogenic in situ hybridization whole slide images"
Journal of Medical Imaging, 2019
[Ref No.: 5111]

salahuddin haowlader , humayra ferdous and shahidul islam" quality of physics teaching up to higher secondary level in bangladesh—from the undergraduate students’ perspective."
Bangladesh Journal of Physics, 2019
[Ref No.: 5220]

nadia akter mokta, md shakilur rahman, tanjim siddiqua, santunu purohit, md kawchar ahmed patwary, akm moinul haque meaze1 and humayra ferdous "effective point of measurement (epom) of some ionization chambers for high energy photon beam dosimetry used in radiotherapy for the treatment of cancer patient."
Biomedical Journal for Scientific and Technical Research, 2019
[Ref No.: 5221]

farzana khalil" dichlorodiphenyltrichloroethane in environmental samples and human blood of chittagong chemical complex area and pesticide residues in some vegetable samples"
Dhaka University Institutional Repository, 2019
[Ref No.: 5354]

dr. saiful islam "k+ intercalated v2o5 nanorods with exposed facets as advanced cathodes for high energy and high rate zinc-ion batteries†"
JMC-A, 2019
[Ref No.: 5264]

saiful islam, orcid logo a muhammad hilmy alfaruqi, orcid logo ab balaji sambandam,a dimas yunianto putro,a sungjin kim,a jeonggeun jo,a seokhun kim,a vinod mathewa and jaekook kim orcid logo *a "a new rechargeable battery based on a zinc anode and a nav6o15 nanorod cathode†"
Chemcom, 2019
[Ref No.: 5265]

muhammad hilmy alfaruqi, orcid logo ab saiful islam,a jun lee,a jeonggeun jo,a vinod mathewa and jaekook kim orcid logo *a "first principles calculations study of α-mno2 as a potential cathode for al-ion battery application"
Journal of Materials Chemistry-A, 2019
[Ref No.: 5302]

sharmin sultana poly, md. a. r. jamil, abeda s. touchy, shunsaku yasumura, s. m. a. hakim siddiki, takashi toyao, zen maeno, and ken-ichi shimizu "acetalization of glycerol with ketones and aldehydes catalyzed by high silica hβ zeolite"
Molecular Catalysis, 2019, 479,110608, 2019
[Ref No.: 5312]

md. nurnobi rashed, s.m.a.hakim siddiki, abeda s. touchy, md. a. r. jamil, sharmin s. poly, takashi toyao, zen maeno, ken-ichi shimizu "direct phenolysis reactions of unactivated amides into phenolic esters promoted by a heterogeneous ceo2 catalyst"
Chem. Eur. J., 2019, 25, 10594 – 10605, 2019
[Ref No.: 5313]

md. a. r. jamil, s.m.a. hakim siddiki, abeda s. touchy, md. nurnobi rashed, sharmin s. poly, yuan jing, kah wei ting, takashi toyao, zen maeno, ken-ichi shimizu "selective transformations of triglycerides into fatty amines, amides, and nitriles using heterogeneous catalysts"
ChemSusChem, 2019, 12, 3115 – 3125, 2019
[Ref No.: 5314]

md. a. r. jamil, abeda s touchy, md. numobi rashed, kah wei ting, s.m.a. hakim siddiki, takashi toyao, zen maeno, ken-ichi shimizu "n-methylation of amines and nitroarenes with methanol using heterogeneous platinum catalysts"
Journal of Catalysis, 2019
[Ref No.: 5315]

dr. kamal uddin sarker" enhancing the teaching and learning process using video streaming servers and forecasting techniques"
Sustainability, 2019
[Ref No.: 5458]

dr. kamal uddin sarker" ontological practice for big data management"
International Journal of Computing and Digital Systems, 2019
[Ref No.: 5459]

dr. md. rayhan uddin" mars pre-clinical imaging: the benefits of small pixels and good energy data"
SPIE Optical Engineering + Applications, 2019
[Ref No.: 5428]

dr. md. rayhan uddin" assessment of metal implant induced artefacts using photon counting spectral ct"
SPIE Optical Engineering + Applications, 2019
[Ref No.: 5429]

dr. md. rayhan uddin" mars pulmonary spectral molecular imaging: potential for locating tuberculosis involvement"
IEEE Xplore, 2019
[Ref No.: 5433]

dr. md. rayhan uddin" first human imaging with mars photon-counting ct"
IEEE Nuclear Science Symposium and Medical Imaging Conference Proceedings (NSS/MIC), 2019
[Ref No.: 5434]

m. f. mridha, md. abdul hamid, shaon hossain sani, akramkhan rony, seungmin oh, jinsul kim" evaluate and predict concentration of particulate matter (pm10) using machine learning approach"
The Journal of Contents Computing, 2019
[Ref No.: 5558]

shahadat hossain" environmental radioactivity monitoring and assessment of excess lifetime cancer risk to people in demra thana, dhaka, bangladesh"
ABC Research Alert, 2019
[Ref No.: 4879]

md. mortuza ahmmed "maternal and child health in bangladesh over the years: evidence from demographic and health surveys"
National University Journal of Science, 2019
[Ref No.: 4876]

k. n. mukta, xiao gao, and p. a. robinson "neural field theory of evoked response potentials in a spherical brain geometry"
Physical Review E, 2019
[Ref No.: 4870]

dr. kamrun nahar mukta" nonlinear propagation of dust-ion-acoustic shock waves in a degenerate multi-species plasma"
International Journal of Cosmology, Astronomy and Astrophysics, 2019
[Ref No.: 4872]

md. mehedi hassan onik" modifiable public blockchains using truncated hashing and sidechains."
IEEE Access, 2019
[Ref No.: 4829]

md. mehedi hassan onik" personal information classification on aggregated android application’s permissions"
Applied Sciences, 2019
[Ref No.: 4830]

md. mehedi hassan onik" proof-familiarity: a privacy-preserved blockchain scheme for collaborative medical decision-making"
Applied Sciences, 2019
[Ref No.: 4831]

md. mehedi hassan onik" privacy-aware blockchain for personal data sharing and tracking"
Open Computer Science, 2019
[Ref No.: 4832]

dr. mahjabin taskin" ultrasound propagation in two-layer gas flow"
International Journal of Hydrogen Energy, 2019
[Ref No.: 4795]

dr. mahjabin taskin" observation of ultrasonic signal and measurement of h2 concentration from the exterior of a metal pipe"
International Journal of Hydrogen Energy, 2019
[Ref No.: 4796]

dr. mahjabin taskin" instant gas concentration measurement using ultrasound from exterior of a pipe"
IEEE Sensors Journal, 2019
[Ref No.: 4797]

shovan kumar kundu, dhiraj kumar rana, laxmikanta karmakar, debajyoti das & soumen basu "enhanced multiferroic, magnetodielectric and electrical properties of sm doped lanthanum ferrite nanoparticles"
Journal of Materials Science: Materials in Electronics, 2019
Keywords: Natural Sciences,Nanotechnology [Ref No.: 4808]

shovan kumar kundu, dhiraj kumar rana, amit banerjee, debajyoti das, and soumen basu "influence of manganese on multiferroic and electrical properties of lanthanum ferrite nanoparticles"
Materials Research Express, 2019
Keywords: Natural Sciences,Nanotechnology [Ref No.: 4809]

dhiraj kumar rana,a suresh kumar singh,a shovan kumar kundu, subir roy, s. angappane, and soumen basu "electrical and room temperature multiferroic properties of polyvinylidene fluoride nanocomposites doped with nickel ferrite nanoparticles"
New Journal of Chemistry, 2019
Keywords: Natural Sciences,Nanotechnology,Polymer and Nano Materials [Ref No.: 4810]

dhiraj kumar rana, shovan kumar kundu, ram janay choudhary, and soumen basu "enhancement of electrical and magnetodielectric properties of bifeo3 incorporated pvdf flexible nanocomposite films"
Materials Research Express, 2019
Keywords: Natural Sciences,Nanotechnology,Polymer and Nano Materials [Ref No.: 4812]

shovan kumar kundu, dhiraj kumar rana and soumen basu "observation of room temperature multiferroic and electrical properties in gadolinium ferrite nanoparticles"
Modern Physics Letters B, 2019
Keywords: Natural Sciences,Nanotechnology [Ref No.: 4813]

md. ismail hossen" smartphone-based drivers context recognition"
Intelligent Decision Technologies, 2019
[Ref No.: 4780]

md. ismail hossen" an automated driver’s context recognition approach using smartphone embedded sensors"
Lecture Notes in Electrical Engineering, 2019
[Ref No.: 4781]

md. ismail hossen" smartphone-based context flow recognition for outdoor parking system with machine"
Electronics, 2019
[Ref No.: 4782]

md. mortuza ahmmed" green supply chain management practices by superstores in bangladesh: a case study in dhaka"
European Journal of Business and Management, 2019
[Ref No.: 4740]

md. mortuza ahmmed "the impact of internet on the youth leadership"
Business Ethics and Leadership, 2019
[Ref No.: 4752]

abhijit bhowmik" genre of bangla music: a machine classification learning approach"
AIUB JOURNAL OF SCIENCE AND ENGINEERING, 2019
[Ref No.: 4753]

dr. a. f. m. saifuddin saif" data analysis and visualization of continental cancer situation by twitter scraping"
International Journal of Modern Education and Computer Science (IJMECS), 2019
[Ref No.: 4619]

tanzia zerin khan; salma parvin "effects of lewis number on two phase natural convection flow of nanofluid inside a square cavity with an adiabatic obstacle"
AIP Conference Proceedings, 2019
[Ref No.: 4700]

md. siyamul islam" siat: a distributed video analytics framework for intelligent video surveillance"
Symmetry, 2019
[Ref No.: 4718]

raihan uddin ahmed" new algorithm for detection of spinal cord tumor using opencv"
Global Journal of Computer Science and Technology (GJCST), 2019
[Ref No.: 4719]

dr. mahfuza khatun" one-sided control charts for monitoring the multivariate coefficient of variation in short production runs"
Transactions of the Institute of Measurement and Control., 2019
[Ref No.: 4423]

dr. mahfuza khatun" a side-sensitive modified group runs control chart with auxiliary information to detect process mean shifts"
Pertanika Journal of Science and Technology, 2019
[Ref No.: 4424]

jenita jahangir" electromagnetics in terms of differential form"
The Dhaka University Journal of Science, 2019
[Ref No.: 4434]

jenita jahangir" fluid flow of a rotating rectangular straight duct in darcian porous medium"
Journal of Multidisciplinary Engineering Science and Technology, 2019
[Ref No.: 4440]

prodip kumar ghose" fluid flow of a rotating rectangular straight duct in darcian porous medium."
Journal of Multidisciplinary Engineering Science and Technology (JMEST), 2019
[Ref No.: 4487]

md. navid bin anwar" comparative study of cryptography algorithms and its’ applications"
International Journal of Computer Networks and Communications Security, 2019
[Ref No.: 4274]

bithi paul" significant reduction of defect states and surface tailoring in zno nanoparticles via nano-bio interaction with glucose for bio-applications"
IEEE Transactions on NanoBioscience, 2019
[Ref No.: 4275]

m. mahmudul hasan, george kousiouris, dimosthenis anagnostopoulos, teta stamati, peri loucopoulos, mara nikolaidou "an ontology based framework for e-government regulatory requirements compliance"
International Journal of E-Services and Mobile Applications (IJESMA), 2019
[Ref No.: 4321]

md. manzurul hasan & md. saidur rahman "no-bend orthogonal drawings and no-bend orthogonally convex drawings of planar graphs (extended abstract)"
Computing and Combinatorics (COCOON 2019), 2019
Keywords: Algorithms [Ref No.: 4342]

dr. a. f. m. saifuddin saif" a review based on brain computer interaction using eeg headset for physically handicapped people"
International Journal of Education and Management Engineering (IJEME), 2019
[Ref No.: 4352]

dr. a. f. m. saifuddin saif" efficient method to improve human brain activities using neuroheadset device embedded with sensors: a comprehensive study"
International Journal of Software Engineering and Computer Systems, 2019
[Ref No.: 4353]

dr. a. f. m. saifuddin saif" category specific prediction modules for visual relation recognition"
International Journal of Mathematical Sciences and Computing(IJMSC), 2019
[Ref No.: 4354]

dr. a. f. m. saifuddin saif" aggressive action estimation: a comprehensive review on neural network based human segmentation and action recognition"
International Journal of Education and Management Engineering(IJEME), 2019
[Ref No.: 3850]

prof. dr. dip nandi" an empirical comparison of missing value imputation techniques on aps failure prediction"
International Journal of Information Technology and Computer Science (IJITCS), 2019
[Ref No.: 3887]

dr. md. sohidul islam" topas based low loss and dispersion flatten decagonal porous core photonic crystal fiber for terahertz communication"
INTERNATIONAL JOURNAL OF MICROWAVE AND OPTICAL TECHNOLOGY [ ISI (request submitted), SCOPUS], 2019
[Ref No.: 3778]

bithi paul" fabrication and ferromagnetic resonance study of bzt-bct/lsmo heterostructure films on lao and pt"
Journal of Magnetism and Magnetic Materials, 2019
[Ref No.: 3801]

md. masuduzzaman" li-fi technology: increasing the range of li-fi by using mirror"
International Journal of Information Technology and Computer Science, 2019
[Ref No.: 3810]

dr. afroza nahar" effect of nanofluid properties and mass-flow rate on heat transfer of parabolic-trough concentrating solar system"
Journal of Naval Architecture and Marine Engineering, 2019
[Ref No.: 3819]

dr. mohammed jashim uddin" unsteady mhd bio-nanoconvective anistropic slip flow past a vertical rotating cone"
Thermal Science, 2019
[Ref No.: 3824]

dr. mohammed jashim uddin" mhd boundary layer bionanoconvective non‐newtonian flow past a needle with stefan blowing"
HEAT TRANSFER ASIAN RESEARCH, 2019
[Ref No.: 3845]

dr. a. f. m. saifuddin saif" anomaly detection in crowded scene by pedestrians behaviour extraction using long short term method: a comprehensive study"
International Journal of Education and Management Engineering(IJEME), 2019
[Ref No.: 3846]

dr. a. f. m. saifuddin saif" online trial room based on human body shape detection"
International Journal of Image, Graphics and Signal Processing, 2019
[Ref No.: 3843]

dr. afroza nahar" numerical investigation on the effect of different parameters in enhancing heat transfer performance of photovoltaic thermal systems"
Renewable Energy, 2019
[Ref No.: 3672]

asad abbas, anders avdic, peng xiao, m. mahmudulhasan, wan ming "university-government collaboration for the generation and commercialisation of new knowledge for use in industry"
Journal of Innovation & Knowledge - JIK (Elsevier Journal), 2019
[Ref No.: 3668]

dr. md. mozahar ali " first− principles study: structural, mechanical, electronic and thermodynamic properties of simple− cubic− perovskite (ba0. 62k0. 38)(bi0. 92mg0. 08) o3"
Solid State Communications, 2019
[Ref No.: 4002]

md. masuduzzaman" energy efficiency analysis by fine grained modification in link state routing protocol"
International Journal of Information Technology and Computer Science, 2019
[Ref No.: 4010]

dr. mohammed jashim uddin" three-dimensional bioconvection nanofluid flow from a bi-axial stretching sheet with anisotropic slip, thermal jump and concentration slip effects"
SAINS MALASIANA, 2019
[Ref No.: 4226]

dr. mohammed jashim uddin" computation of melting dissipative magnetohydrodynamic nanofluid bioconvection with second order slip and variable thermophysical properties"
APPLIED SCIENCE, 2019
[Ref No.: 4227]

dr. s. mosaddeq ahmed" synthesis of 1-phenyl-3,4-dihydropyrimidine-2(1h)-ones derivatives under solvent free condition and study of their antimicrobial activity."
Bangladesh Journal Scientific and Industrial Research, 2019
[Ref No.: 4228]

dr. md. razib hayat khan" a smart and cost-effective fire detection system for developing country: an iot based approach"
International Jornal of Information Engineering and Electronic Business, 2019
[Ref No.: 4229]

dr. mohammed jashim uddin" unsteady three-dimensional stagnation point magnetohydrodynamic flow of bionanofluid with variable properties"
Journal of Nanomaterials, Nanoengineering and Nanosystems, 2018
[Ref No.: 4225]

dr. m. mostafizur rahman" an analysis on vulnerabilities of password retrying"
Advanced Science Letters, 2018
[Ref No.: 3971]

dr. m. mostafizur rahman" a highly accurate pdf-to-text conversion system for academic papers using natural language processing approach"
Advanced Science Letters, 2018
[Ref No.: 3972]

dr. m. mostafizur rahman" a flexible key-phrase extraction technique for academic literature"
Procedia Computer Science, 2018
[Ref No.: 3973]

dr. a. f. m. saifuddin saif" speech to text conversion for bengali language with labyrinth and resolution: a review"
International Journal of Advances in Electronics and Computer Science, 2018
[Ref No.: 3974]

dr. a. f. m. saifuddin saif" 3d painting using inertial system and monocular vision for localization of handheld controller in virtual reality"
International Journal of Advances in Electronics and Computer Science, 2018
[Ref No.: 3975]

dr. a. f. m. saifuddin saif" an analysis on position estimation, drifting and accumulated error accuracy during 3d tracking in electronic handheld devices"
Journal of Computer and Communications, 2018
[Ref No.: 3976]

dr. a. f. m. saifuddin saif" moving object segmentation using various features from aerial images: a review"
Advanced Science Letters, 2018
[Ref No.: 3977]

dr. a. f. m. saifuddin saif" measurement of unique pupillary distance using modified circle algorithm"
International Journal of Computer Applications, 2018
[Ref No.: 3978]

umme marzia haque" wildlife monitoring using aodv routing protocol in wireless sensor network"
Wildlife Monitoring using AODV Routing Protocol in Wireless Sensor Network, 2018
[Ref No.: 3983]

dr. m. mostafizur rahman" a brain-inspired trust management model to assure security in a cloud based iot framework for neuroscience applications"
Cognitive Computation, 2018
[Ref No.: 3941]

rifat tasnim anannya" master-slave clustering technique for high density traffic in urban vanet scenario"
International Journal of Computer Science and Information Security(IJCSIS), 2018
[Ref No.: 3953]

khadiza akter mitu1 , md. motaleb hossain2*, md. sazzad hossain3 , kazuhisa a. chikita4 "development of rainfall-runoff model for northeast region of bangladesh"
International Journal of Geology Agriculture and Environmental Science, 2018
Keywords: Geographic Information Systems [Ref No.: 3724]

azm ehtesham chowdhury" scrumfall: a hybrid software process model"
International Journal of Information Technology and Computer Science(IJITCS), 2018
[Ref No.: 3734]

bithi paul" structural, electronic, and magnetic analysis and device characterization of ferroelectric–ferromagnetic heterostructure (bzt–bct/lsmo/lao) devices for multiferroic applications"
IEEE Transactions on Magnetics, 2018
[Ref No.: 3742]

kaniz fatema" optimizing contemporary application and processes in open source software"
Demography of Open Source Software Prediction Models and Techniques, 2018
[Ref No.: 3669]

azm ehtesham chowdhury" a survey of software quality assurance and testing practices and challenges in bangladesh"
International Journal of Computer Applications, 2018
[Ref No.: 3661]

juena ahmed noshin" teaching programming to non-programmers at undergraduate level"
International Journal of Engineering and Management Research (IJEMR), 2018
[Ref No.: 3662]

jannatul maowa" vgtool: web tool for visualizing and determining the class of gracefully labeled tree"
International Journal of Computer Applications, 2018
[Ref No.: 3663]

s.m. abdur bhuiyan rouf" a survey of software quality assurance and testing practices and challenges in bangladesh"
International Journal of Computer Applications, 2018
[Ref No.: 3664]

kawser irom rushee" improvised priority based round robin cpu scheduling"
International Journal of Computer Applications (IJCA), 2018
[Ref No.: 3665]

md. navid bin anwar" wildlife monitoring using aodv routing protocol in wireless sensor network"
International Journal of Computer Networks and Communications Security, 2018
[Ref No.: 3631]

dr. mohammed jashim uddin" chebyshev collocation computation of magneto-bioconvection nanofluid flow over a wedge with multiple slips and magnetic induction,"
Journal of Nanomaterials and Nanoengineering, 2018
[Ref No.: 3838]

dr. mohammed jashim uddin" anisotropic slip magneto-bioconvection flow from a rotating cone to a nanofluid with stefan blowing effects"
Chinese Journal Of Physics, 2018
[Ref No.: 3829]

dr. mohammed jashim uddin" bioconvective electromagnetic nanofluid transport from a wedge geometry: simulation of smart electro‐conductive bio‐nanopolymer processing."
Heat Transfer—Asian Research, 2018
[Ref No.: 3832]

dr. mohammed jashim uddin" melting and second order slip effect on convective flow of nanofluid past a radiating stretching/shrinking sheet"
Propulsion and Power Research, 2018
[Ref No.: 3833]

dr. mohammed jashim uddin" modeling and simulation of nanofluid transport via bio-elastic sheets"
Biomedical Engineering, Nanoengineering, 2018
[Ref No.: 3834]

azm ehtesham chowdhury" a study on bangladeshi it freelancers: a survey"
International Journal of Computer Applications, 2018
[Ref No.: 3809]

dr. s. mosaddeq ahmed" solid waste disposal and its impact on surrounding environment of matuail landfill site, dhaka, bangladesh"
American Journal of Environmental Sciences, 2018
[Ref No.: 3818]

md. masuduzzaman" intelligent tour planning system using crowd sourced data"
International Journal of Education and Management Engineering, 2018
[Ref No.: 3811]

md. mortuza ahmmed "determinants of academic performance of undergraduate students in private universities in bangladesh: a case study"
Global Journal of HUMAN-SOCIAL SCIENCE, 2018
[Ref No.: 3803]

md. mortuza ahmmed "discriminating patients suffering from non-communicable diseases: a case study among bangladeshi adults"
Biomedical Journal of Scientific & Technical Research, 2018
[Ref No.: 3804]

md. mortuza ahmmed" trends in climate change and some of its determinants in bangladesh"
Research and Science Today (RST), 2018
[Ref No.: 3805]

md. mortuza ahmmed" a study on identification of socioeconomic variables associated with non-communicable diseases among bangladeshi adults"
American Journal of Biomedical Science and Engineering, 2018
[Ref No.: 3806]

dr. md. sakir hossain" spectrally efficient dsi-based ofdm papr reduction by subcarrier group modulation"
IEEE Transactions on Broadcasting, 2018
[Ref No.: 3799]

prof. dr. dip nandi" comparative study of parallel implementation for searching algorithms with openmp"
Journal of Theoretical and Applied Information Technology, 2018
[Ref No.: 3888]

prof. dr. dip nandi" traffic sign detection based on color segmentation of obscure image candidates: a comprehensive study"
International Journal of Modern Education and Computer Science, 2018
[Ref No.: 3883]

prof. dr. dip nandi" an efficient hybrid architecture for visual behavior recognition using convolutional neural network"
International Journal of Computer Applications, 2018
[Ref No.: 3886]

dr. a. f. m. saifuddin saif" real time bangla vehicle plate recognition towards the need of efficient model - a comprehensive study"
International Journal of Image, Graphics and Signal Processing(IJIGSP), 2018
[Ref No.: 3851]

dr. a. f. m. saifuddin saif" bangla digital number plate recognition using template matching for higher accuracy and less time complexity"
International Journal of Computer Applications, 2018
[Ref No.: 3855]

dr. a. f. m. saifuddin saif" efficient framework using morphological modeling for frequent iris movement investigation towards questionable observer detection"
International Journal of Image, Graphics and Signal Processing(IJIGSP), 2018
[Ref No.: 3857]

dr. a. f. m. saifuddin saif" an efficient hybrid architecture for visual behavior recognition using convolutional neural network"
International Journal of Computer Applications, 2018
[Ref No.: 3861]

dr. a. f. m. saifuddin saif" fast and effective motion model for moving object detection using aerial images"
International Journal of Computer Vision and Signal Processing, 2018
[Ref No.: 3870]

dr. a. f. m. saifuddin saif" traffic sign detection based on color segmentation of obscure image candidates: a comprehensive study"
International Journal of Modern Education and Computer Science, 2018
[Ref No.: 3872]

dr. a. f. m. saifuddin saif" efficient mathematical procedural model for brain signal improvement from human brain sensor activities"
International Journal of Image, Graphics and Signal Processing(IJIGSP), 2018
[Ref No.: 3864]

dr. a. f. m. saifuddin saif" a study of activity recognition and questionable observer detection"
International Journal of Computer Applications, 2018
[Ref No.: 3866]

prof. dr. dip nandi" scrumfall: a hybrid software process model"
International Journal of Information Technology and Computer Science (IJITCS), 2018
[Ref No.: 3881]

dr. khandaker tabin hasan" measurement of unique pupillary distance using modified circle algorithm"
International Journal of Computer Applications, 2018
[Ref No.: 4384]

dr. mahfuza khatun" adaptive multivariate double sampling and variable sampling interval hotelling’s t^2 charts"
Quality and Reliability Engineering International, 2018
[Ref No.: 4419]

dr. mahfuza khatun" variable sampling interval run-sum x (over bar) chart with estimated parameters"
The 4th International Conference on Engineering, Applied Science and Technology, 2018
[Ref No.: 4420]

sajib hasan" adaptive fitts for adaptive interface"
AIUB Journal of Science and Engineering, 2018
[Ref No.: 4341]

mohammad arifur rahman" investigating students’ adoption and usage behavior of educational technology(edutech) at tertiary level (pls-sem approach)"
AIUB Journal of Science and Engineering, 2018
[Ref No.: 4494]

md. manirul islam" master-slave clustering technique for high density traffic in urban vanet scenario"
International Journal of Computer Science and Information Security (IJCSIS), 2018
[Ref No.: 4496]

shahrin chowdhury" wildlife monitoring using aodv routing protocol in wireless sensor network"
International Journal of Computer Networks and Communications Security, 2018
[Ref No.: 4533]

md. hasibul hasan" a survey of software quality assurance and testing practices and challenges in bangladesh"
International Journal of Computer Applications, 2018
[Ref No.: 4510]

md mehedi hasan, sungoh kwon, and jee-hyeon na "adaptive mobility load balancing algorithm for lte small-cell networks"
IEEE Transactions on Wireless Communications, 2018
Keywords: Networking,Wireless/ Mobile Communication,5G Networks [Ref No.: 4730]

md mehedi hasan, sungoh kwon, and sangchul oh "frequent-handover mitigation in ultra-dense heterogeneous networks"
IEEE Transactions on Vehicular Technology, 2018
Keywords: Networking,Wireless/ Mobile Communication,5G Networks [Ref No.: 4731]

md. masum billah" using archived comments on learning videos as a resource for question answering"
International Journal of Scientific and Research Publications, 2018
[Ref No.: 4716]

dipta justin gomes" performance evaluation of extended latency time algorithm in different linux based operating systems"
International Journal of New Technology and Research (IJNTR), 2018
[Ref No.: 4712]

dr. shohag barman" a boolean network inference from time-series gene expression data using a genetic algorithm"
Bioinformatics, 2018
[Ref No.: 4690]

md. ismail hossen" a review on outdoor parking systems using feasibility of mobile sensors"
. Lecture Notes in Electrical Engineering, 2018
[Ref No.: 4779]

dr. md. tarek hossain" inner relationship among rapidity, velocity and geometric approach to the wigner rotation"
International Journal of Applied Physics, 2018
[Ref No.: 4820]

dhiraj kumar rana, suresh kumar singh, shovan kumar kundu, ram janay choudhary, & soumen basu "electrical and magnetic properties of polyvinyl alcohol-cobalt ferrite nanocomposite films"
Bulletin of Materials Science, 2018
Keywords: Natural Sciences,Nanotechnology,Polymer and Nano Materials [Ref No.: 4814]

shovan kumar kundu, dhiraj kumar rana, ayan mukherjee, amit banerjee, debajyoti das, soumen basu "structural, magnetic and optical properties of lanthanum ferrite nanoparticles with application perspective"
Advanced Science Letters, 2018
Keywords: Natural Sciences,Nanotechnology [Ref No.: 4815]

dr. mahjabin taskin" flowing h2 gas concentration measurement using ultrasound from exterior of the pipe"
IEEE Xplore, 2018
[Ref No.: 4798]

dr. md. tarek hossain" study of dynamic behavior of a three story model frame"
American Journal of Construction and Building Materials, 2018
[Ref No.: 4825]

md. mehedi hassan onik" a novel approach to identify the best practices of quality management in smes based on critical success factors using interpretive structural modeling (ism)"
International Journal of Engineering & Technology, 2018
[Ref No.: 4833]

md. mehedi hassan onik" a novel approach for network attack classification based on sequential questions"
Annals of Emerging Technologies in Computing, 2018
[Ref No.: 4834]

md. mehedi hassan onik" muxer—a new equipment for energy saving in ethernet"
Technologies, 2018
[Ref No.: 4835]

nazia hossain" emotion detection from voice based classified frame-energy signal using k-means clustering"
International Journal of Software Engineering & Applications (IJSEA), 2018
[Ref No.: 4836]

dr. kamrun nahar mukta" neural field theory of perceptual echo and implications for estimating brain connectivity"
Physical Review E, 2018
[Ref No.: 4894]

dr. kamrun nahar mukta" properties of electron-ion acoustic solitary waves in a four component degenerate quantum plasma"
International Journal of Current Research, 2018
[Ref No.: 4895]

dr. md. saddam mukta hossain" temporal modeling of basic human values from social network usage."
Journal of the Association for Information Science and Technology, Wiley, 2018
[Ref No.: 2909]

dr. md. sohidul islam" topas based high birefringent and low loss single mode hybrid core porous fiber for broand band applications"
Indian Journal of Pure and Applied Physics, [ ISI index], 2018
[Ref No.: 3574]

dr. md. sohidul islam" secrecy mutual information of the independent and identically distributed nakagami-q fading simo channel"
IETE Journal of Research, Taylor and Francis [ISI indexed], 2018
[Ref No.: 3576]

dr. md. abdullah - al - jubair" electronic opinion analysis in organizational culture audit"
Advanced Science Letters (ASL), American Scientific Publishers (CPCI-S Indexed), 2018
[Ref No.: 3595]

dr. md. abdullah - al - jubair" organizational culture automated audit system framework (ocaas): a concept"
Journal of Economic and Management Perspectives, 2018
[Ref No.: 3596]

farzana sabeth, rahima khatun, md. serajul islam, toshifumi iimori, nobuhiro ohta "reversible photocurrent switching in ionic and superionic conductors of polycrystalline silver iodide"
Journal of Physical Chemistry C, 2018
Keywords: Electrodes,Ions,Irradiation,Photonics,Power conversion efficiency [Ref No.: 5509]

dr. md. rayhan uddin" distinguishing iron and calcium using mars spectral ct"
IEEE, 2018
[Ref No.: 5430]

dr. md. rayhan uddin" medipix3rx neutron camera for ambient radiation measurements in the cms cavern"
IEEE, 2018
[Ref No.: 5431]

dr. md. rayhan uddin" cancer imaging with nanoparticles using mars spectral scanner"
IEEE, 2018
[Ref No.: 5432]

s. m. a. hakim siddiki , abeda s. touchy, md. a. r. jamil, takashi toyao, and ken-ichi shimizu "c-methylation of alcohols, ketones, and indoles with methanol using heterogeneous platinum catalysts"
ACS Catalysis, 2018
[Ref No.: 5316]

vaiyapuri soundharrajanvaiyapuri soundharrajan department of materials science and engineering, chonnam national university, gwangju 500-757, south korea more by vaiyapuri soundharrajan , balaji sambandam, sungjin kim, vinod mathew, jeonggeun jo, seokhun kim, jun lee, saiful islam, kwangho kim, yang-kook sun, and jaekook kim* "aqueous magnesium zinc hybrid battery: an advanced high-voltage and high-energy mgmn2o4 cathode"
ACS Energy Letter, 2018
[Ref No.: 5303]

muhammad hilmyalfaruqiabsaifulislamadimas yuniantoputroavinodmathewasungjinkimajeonggeunjoaseokhunkimayang-kooksunckwanghokimdejaekookkima "structural transformation and electrochemical study of layered mno2 in rechargeable aqueous zinc-ion battery"
Electrochimica Acta, 2018
[Ref No.: 5304]

saiful islam, muhammad hilmy alfaruqi, dimas yunianto putro, dr. vinod mathew, sungjin kim, jeonggeun jo, seokhun kim, prof. yang-kook sun, prof. kwangho kim, prof. jaekook kim "pyrosynthesis of na3v2(po4)3@c cathodes for safe and low-cost aqueous hybrid batteries"
Chemsuschem, 2018
[Ref No.: 5266]

dr. debajyoti karmaker" an inverse differential game approach to modelling bird mid-air collision avoidance behaviours"
IFAC-PapersOnLine, 2018
[Ref No.: 5184]

dr. m m manjurul islam" crack classification of a pressure vessel using feature selection and deep learning methods"
Sensors, 2018
[Ref No.: 5082]

dr. m m manjurul islam" rub-impact fault diagnosis using an effective imf selection technique in ensemble empirical mode decomposition and hybrid feature models"
Sensors, 2018
[Ref No.: 5083]

dr. m m manjurul islam" reliable multiple combined fault diagnosis of bearings using heterogeneous feature models and multiclass support vector machines"
Reliability Engineering & System Safety, 2018
[Ref No.: 5084]

dr. m m manjurul islam" a reliable technique for remaining useful life estimation of rolling element bearings using dynamic regression models"
Reliability Engineering & System Safety, 2018
[Ref No.: 5085]

dr. s. m. hasan mahmud" prmt: predicting risk factor of obesity among middle-aged people using data mining techniques"
Procedia Computer Science, 2018
[Ref No.: 5038]

dr. s. m. hasan mahmud" csv2rdf: generating rdf data from csv file using semantic web technologies"
Journal of Theoretical and Applied Information Technology, 2018
[Ref No.: 5039]

8. ft tuz zohra, m jashim uddin, ai md. ismail, o anwar bég. "bioconvective electromagnetic nanofluid transport froma wedge geometry: simulation of smart electro-conductive bio-nanopolymer processing"
Heat Transfer-Asian Research, 2018
[Ref No.: 4992]

7. ft zohra, mj uddin, aim ismail, oa bég, a kadir. "anisotropic slip magneto-bioconvection flow from a rotating cone to a nanofluid with stefan blowing effects"
Chinese Journal of Physics, 2018
[Ref No.: 4993]

dr. md. saiful islam" modulated heavy nucleus-acoustic waves and associated rogue waves in a degenerate relativistic quantum plasma system."
Physics of Plasmas, 2018
[Ref No.: 4905]

dr. md. asraf ali" fuzzy logic-based improved ventilation system for the pharmaceutical industry"
International Journal of Engineering & Technology, 2018
[Ref No.: 4980]

dr. md. asraf ali" electromyography-a reliable technique for muscle activity assessment"
Journal of Telecommunication, Electronic and Computer Engineering (JTEC), 2018
[Ref No.: 4981]

dr. md. asraf ali" a literature review on nosql database for big data processing"
International Journal of Engineering & Technology, 2018
[Ref No.: 4982]

dr. md. asraf ali" a systematic review on fatigue analysis in triceps brachii using surface electromyography"
Biomedical Signal Processing and Control, 2018
[Ref No.: 4983]

dr. md. asraf ali" significance of electromyography in the assessment of diabetic neuropathy"
Journal of Mechanics in Medicine and Biology, 2018
[Ref No.: 4984]

dr. abdus salam" authorship attribution for bengali language using the fusion of n-gram and naive bayes algorithms"
International Journal of Information Technology and Computer Science(IJITCS), 2018
[Ref No.: 5887]

jannatul maowa, sharifa rania mahmud "vgtool: web tool for visualizing and determining the class of gracefully labeled tree"
International Journal of Computer Applications, 2018
[Ref No.: 5783]

dr. md. rabiul auwul" impact of micro-credit on poor households in kurigram district"
Applied Economics and Finance, 2018
[Ref No.: 5665]

muhammad rabiul. islam 1*, i.f.t. al-shaikhli2 , a. abdulkadir1 "a scientific review of soft-computing techniques and methods for stock market prediction"
International Journal of Engineering & Technology, 2018
Keywords: Big Data,Deep Learning,Machine to Machine Data Analytics [Ref No.: 6001]

mohammad rabiul islam1 , imad fakhri al-shaikhli2 , rizal bin mohd nor3 , vijayakumar varadarajan4 "technical approach in text mining for stock market prediction: a systematic review"
Indonesian Journal of Electrical Engineering and Computer Science, 2018
Keywords: Big Data,Deep Learning,Machine to Machine Data Analytics [Ref No.: 6003]

dr. md. saef ullah miah" intelligent tour planning system using crowd sourced data"
International Journal of Education and Management Engineering(IJEME), 2018
[Ref No.: 6231]

md sarowar hossain, barnana pal and p. k. mukhopadhyay "ultrasonic characterization of newtonian and non-newtonian fluids"
Universal Journal of Physics and Application, 2018
Keywords: Viscous Medium, Ultrasonic Velocity, Sound Attenuation, Adiabatic Compressibility, Non-newtonian Fluids [Ref No.: 6032]

md abdullah al mamun, manifa noor, a k m atique ullah, md. sarowar hossain, matin abdul, fakhrul islam and m a hakim "effect of cepo4 on structural, magnetic and optical properties of ceria nanoparticles"
Material Research Express, 2018
[Ref No.: 6054]

dr. moushumi zaman bonny" image stitching algorithm: an optimization between correlation-based and feature-based method"
International Journal of Computer Science and Information Security (IJCSIS), 2018
[Ref No.: 6619]

jahida binte islam, s akter, ac bhowmick, mn uddin, m sarkar" hydro-environmental pollution of turag river in bangladesh"
Bangladesh Journal of Scientific and Industrial Research, 2018
[Ref No.: 6605]

md zainal abedin, kazy noor e alam siddiquee, ms bhuyan, razuan karim, mohammad shahadat hossain, karl andersson "performance analysis of anomaly based network intrusion detection systems"
43rd Annual IEEE Conference on Local Computer Networks, 2018
Keywords: Computer Network [Ref No.: 6532]

prof. dr. md. rafiqul islam" a component based unified architecture for utility service in cloud,"
Future Generation Computer Systems, 2018
[Ref No.: 6518]

prof. dr. md. rafiqul islam" chemical reaction optimization for solving longest common subsequence problem for multiple string"
Soft computing, 2018
[Ref No.: 6519]

dr. razuan karim "an interoperable ip based wsn for smart irrigation systems"
14th Annual IEEE Consumer Communications & Networking Conference, 2017
Keywords: Wireless Sensor Networks [Ref No.: 6533]

m. a. basith, areef billah, m. a. jalil, nilufar yesmin, mashnoon alam sakib, emran khan ashik, s.m.enamul hoque yousuf, sayeed shafayet chowdhury, md. sarowar hossain, shakhawat h. firoz, bashir ahmmad "the 10% gd and ti co-doped bifeo3: a promising multiferroic material"
Journal of Alloys and Compounds, 2017
[Ref No.: 6055]

md sarowar hossain, b. rajini kanth and p. k. mukhopadhyay "effect of annealing on elastic moduli of a fsma"
Shape Memory and Superelasticity, 2017
[Ref No.: 6030]

md. sarowar hossain, m. a. hakim and p. k. mukhopadhyay "interesting low temperature magneto-elastic behavior of a finemet metglass"
AIP Advances, 2017
[Ref No.: 6031]

pritam khan boni" smartphone based heart attack risk prediction system with statistical analysis and data mining approaches"
Advances in Science, Technology and Engineering Systems Journal, 2017
[Ref No.: 6026]

m. a. basith, m. a. islam, bashir ahmmad, md. sarowar hossain and k mølhave "preparation of high crystalline nanoparticles of rare-earth based complex pervoskites and comparison of their structural and magnetic properties with bulk counterparts"
Materials Research Express, 2017
[Ref No.: 6036]

anwarul kabir" cyber-crimes against womenfolk on social networks: bangladesh context"
International Journal of Computer Applications, 2017
[Ref No.: 5995]

dr. md. mozahar ali" hydrothermal synthesis, structure, and superconductivity of simple cubic perovskite (ba0.62k0.38)(bi0.92mg0.08)o3 with tc ∼ 30 k"
Inorganic Chemistry, 2017
[Ref No.: 5670]

dr. abdus salam" text-to-3d-scene generation using semantic parsing and spatial knowledge with rule based system"
International Journal of Computer Science Issues (IJCSI), 2017
[Ref No.: 5888]

dr. md. saiful islam" envelope solitons in three-component degenerate relativistic quantum plasmas."
Physics of Plasmas, 2017
[Ref No.: 4906]

dr. md. saiful islam" ultra-low frequency shock dynamics in degenerate relativistic plasmas"
Physics of Plasmas, 2017
[Ref No.: 4907]

dr. m m manjurul islam" time–frequency envelope analysis-based sub-band selection and probabilistic support vector machines for multi-fault diagnosis of low-speed bearings"
Journal of Ambient Intelligence and Humanized Computing, 2017
[Ref No.: 5086]

dr. m m manjurul islam" reliable bearing fault diagnosis using bayesian inference-based multi-class support vector machines"
The Journal of the Acoustical Society of America, 2017
[Ref No.: 5087]

prof. dr. kh. abdul maleque" temperature dependent suction/injuction and variable properties on non-newtonian casson mixed convective mhd laminar fluid flow with viscous dissipation and thermal radiation"
American Journal of heat and Mass transfer (AJHMT), 2017
[Ref No.: 5125]

dr. akinul islam jony" ict in higher education: wiki-based reflection to promote deeper thinking levels"
International Journal of Modern Education and Computer Science, 2017
[Ref No.: 5113]

dr. khandaker tabin hasan" identifying human personalized sentiment with streaming data"
International Journal of Computer Applications, 2017
[Ref No.: 5204]

saiful islam,‡a muhammad hilmy alfaruqi, orcid logo ‡a vinod mathew,a jinju song,a sungjin kim,a seokhun kim,a jeonggeun jo,a joseph paul baboo,a duong tung pham,a dimas yunianto putro,a yang-kook sunb and jaekook kim "facile synthesis and the exploration of the zinc storage mechanism of β-mno2 nanorods with exposed (101) planes as a novel cathode material for high performance eco-friendly zinc-ion batteries†"
JMC-A, 2017
[Ref No.: 5267]

saifulislammuhammad hilmyalfaruqijinjusongsungjinkimduong tungphamjeonggeunjoseokhunkimvinodmathewjoseph paulbaboozhiliangxiujaekookkim "carbon-coated manganese dioxide nanoparticles and their enhanced electrochemical properties for zinc-ion battery applications"
Journal of energy chemistry, 2017
[Ref No.: 5268]

muhammad hilmyalfaruqi1saifulislam1vinodmathewjinjusongsungjinkimduong phamtungjeonggeunjoseokhunkimjoseph paulbaboozhiliangxiujaekookkim "ambient redox synthesis of vanadium-doped manganese dioxide nanoparticles and their enhanced zinc storage properties"
Applied Surface Science, 2017
[Ref No.: 5269]

muhammad hilmyalfaruqi1saifulislam1jinjusongsungjinkimduong tungphamjeonggeunjoseokhunkimjoseph paulbaboodimas yuniantoputrovinodmathewjaekookkim "carbon-coated rhombohedral li2nav2(po4)3 nanoflake cathode for li-ion battery with excellent cycleability and rate capability"
Chemical Physics Letters, 2017
[Ref No.: 5270]

muhammad h. alfaruqi†‡, vinod mathew†‡, jinju song†, sungjin kim†, saiful islam†, duong tung pham†, jeonggeun jo†, seokhun kim†, joseph paul baboo†, zhiliang xiu†, kug-seung lee§, yang-kook sun∥orcid, and jaekook kim*†orcid "electrochemical zinc intercalation in lithium vanadium oxide: a high-capacity zinc-ion battery cathode"
Chemistry of Materials, 2017
[Ref No.: 5307]

dr. md. rayhan uddin" quality control of intensity modulated radiation therapy (imrt)"
Universal Journal of Physics and Application, 2017
[Ref No.: 5427]

m. f. mridha, kamruddin nur, aloke kumar saha, md. akhtaruzzaman adnan" a new approach to enhance internet banking security"
International Journal of Computer Applications, 2017
[Ref No.: 5559]

m. f. mridha, kamruddin nur, aloke kumar saha, and md akhtaruzzaman adnan "a new approach to enhance internet banking security"
International Journal of Computer Applications (IJCA), 2017
Keywords: Security in Smart Environments [Ref No.: 5565]

sabbir ahmed" cyber-crimes against womenfolk on social networks: bangladesh context"
International Journal of Computer Applications, 2017
[Ref No.: 3552]

victor stany rozario, a.z.m. ehtesham chowdhury, muhammad sarwar jahan morshed" community detection in social network using temporal data"
AIUB Journal of Science and Engineering (AJSE), 2017
Keywords: Algorithms,Expert Systems [Ref No.: 3561]

azm ehtesham chowdhury" analysis of the veracities of industry used software development life cycle methodologies"
AIUB Journal of Science and Engineering (AJSE), 2017
[Ref No.: 3562]

azm ehtesham chowdhury" community detection in social network using temporal data"
AIUB Journal of Science and Engineering (AJSE), 2017
[Ref No.: 3563]

azm ehtesham chowdhury" issue starvation in software development: a case study on the redmine issue tracking system dataset"
Journal of Telecommunication, Electronic and Computer Engineering, 2017
[Ref No.: 3564]

azm ehtesham chowdhury" software engineering practices and challenges in bangladesh: a preliminary survey"
Journal of Telecommunication, Electronic and Computer Engineering, 2017
[Ref No.: 3565]

dr. afroza nahar" numerical and experimental investigation on the performance of a photovoltaic thermal collector with parallel plate flow channel under different operating conditions in malaysia."
Solar Energy, 2017
[Ref No.: 3530]

dr. afroza nahar" a three-dimensional comprehensive numerical investigation of different operating parameters on the performance of a photovoltaic thermal system with pancake collector."
Journal of Solar Energy Engineering, 2017
[Ref No.: 3531]

roushanara begum" difficulties of computing natural convection flow in an open cavity"
Universal Journal of Applied Mathematics, 2017
[Ref No.: 3538]

dr. md. kamruzzaman" on the normalized dissipationc_epsilon parameter in decaying turbulence"
Journal of Fluid Mechanics, 2017
[Ref No.: 3545]

fahad ahmed" investigating factors that influence rice yields of bangladesh using data warehousing, machine learning, and visualization"
International Journal of Modern Education and Computer Science (IJMECS), 2017
[Ref No.: 3549]

prof. dr. dip nandi" investigating factors that influence rice yields of bangladesh using data warehousing, machine learning, and visualization"
International Journal of Modern Education and Computer Science, 2017
[Ref No.: 3437]

md. jamsher ali" wang’s premium principle: overview and comparison with classical principles."
ASTIN BULLETIN, 2017
[Ref No.: 3475]

azm ehtesham chowdhury" mining industrial engineered data of apparel industry: a proposed methodology"
International Journal of Computer Applications, 2017
[Ref No.: 3509]

dr. kamrun nahar mukta" theory of corticothalamic brain activity on spherical geometry: spectra, coherence, and correlation"
Physical Review E, 2017
[Ref No.: 4896]

dr. md. tarek hossain" numerical calculations of the wigner rotation"
International Journal of Physics and Research, 2017
[Ref No.: 4821]

dr. md. tarek hossain" pressure induced structural phase transition and valence change"
American Journal of Condensed Matter Physics, 2017
[Ref No.: 4822]

israt kabir" temperature dependency of the swelling of biopolymer gel"
UITS Journal of Science and Technology (www.uits.edu.bd), 2017
[Ref No.: 4614]

dr. shohag barman" a novel mutual information-based boolean network inference method from time-series gene expression data"
PloS one, 2017
[Ref No.: 4691]

md. hasibul hasan" analysis of the veracities of industry used software development life cycle methodologies"
AIUB Journal of Science and Engineering, 2017
[Ref No.: 4509]

md. hasibul hasan" software engineering practices and challenges in bangladesh: a preliminary survey"
Journal of Telecommunication, Electronic and Computer Engineering, 2017
[Ref No.: 4507]

dr. mohammad mahbub rabbani" incorporation of sorghum extract into electrospun zein nanofibers and their characterization"
Journal of Nanoscience and Nanotechnology, 2017
[Ref No.: 4501]

md. mahfuzur rhaman" parametric studies and reliability of near-wall turbulence modeling for large eddy simulation of incompressible flows"
Journal of Mechanical Engineering, 2017
[Ref No.: 4524]

dr. mahfuza khatun" awareness of health hazard of tobacco consumption among students of universities- a meta-analysis approach"
JU Journal of Statistical Studies, 2017
[Ref No.: 4418]

dr. khandaker tabin hasan" investigating factors that influence rice yields of bangladesh using data warehousing, machine learning, and visualization"
International Journal of Modern Education and Computer Science, 2017
[Ref No.: 4294]

dr. kamruddin md. nur" a new approach to enhance internet banking security"
International Journal of Computer Applications, 2017
[Ref No.: 4288]

prof. dr. kh. abdul maleque" effect of hall current on mhd non-newtonian unsteady casson fluid porous rotating disk flow with a uniform electric field"
Journal The Aiub Journal of Science and Engineering, 2017
[Ref No.: 3876]

prof. dr. dip nandi" issue starvation in software development: a case study on the redmine issue tracking system dataset"
Journal of Telecommunication, Electronic and Computer Engineering, 2017
[Ref No.: 3879]

dr. mohammed jashim uddin" numerical study of slip effects on unsteady aysmmetric bioconvective nanofluid flow in a porous microchannel with an expanding/contracting upper wall using bbuongiorno’s model. ,"
Journal of Mechanics in Medicine and Biolog, 2017
[Ref No.: 3733]

md. mortuza ahmmed" factors associated with safe delivery practice in bangladesh"
International Journal of Health Preference Research (IJHPR), 2017
[Ref No.: 3807]

md. mortuza ahmmed "socioeconomic factors associated with overweight and obesity: a case study among adult people of bangladesh"
AIUB Journal of Science and Engineering (AJSE), 2017
[Ref No.: 3808]

dr. s. mosaddeq ahmed" one step cyclocondensation of (thio)barbituric acid with chalcones in glacial acetic acid and phosphorous pentoxide, part-ii"
Bangladesh Journal Scientific and Industrial Research, 2017
[Ref No.: 3817]

dr. mohammed jashim uddin" electromagnetoconvective stagnation point flow of bionanofluid with melting heat transfer and stefan blowing"
Thermal Science, 2017
[Ref No.: 3825]

dr. mohammed jashim uddin" unsteady magnetoconvective flow of bionanofluid with zero mass flux boundary condition"
Sains Malaysiana, 2017
[Ref No.: 3826]

dr. mohammed jashim uddin" numerical solution of mhd slip flow of a nanofluid past a radiating plate with newtonian heating: a lie group approach."
Alaxandaria J of Engineering,, 2017
[Ref No.: 3827]

dr. mohammed jashim uddin" numerical study of slip effects on unsteady asymmetric bioconvective nanofluid flow in a porous microchannel with an expanding/contracting upper wall using buongiorno’s model"
Journal of Mechanics in Medicine and Biology, 2017
[Ref No.: 3828]

dr. mohammed jashim uddin" bioconvection nanofluid slip flow past a wavy surface with applications in nano-biofuel cells."
Chinese Journal of Physics, 2017
[Ref No.: 3830]

dr. mohammed jashim uddin" slip effects on mhd hiemenz stagnation point nanofluid flow and heat transfer along a nonlinearly shrinking sheet with induced magnetic field: multiple solutions"
Journal of the Brazilian Society of Mechanical Sciences, 2017
[Ref No.: 3823]

dr. md. sakir hossain" papr reduction for ofdm systems using pilot derived phase factors"
IEICE Communication Express, 2017
[Ref No.: 3641]

dr. md. sakir hossain" enhanced ofdm performancewith pilot-aided reduced peak-to-average power ratio"
RISP Journal of Signal Processing, 2017
[Ref No.: 3642]

dr. mohammad ferdows" md. ghulam murtaza; efstratios em. tzirtzilakis and m. ferdows , effect of electrical conductivity and magnetization on the biomagnetic fluid over a stretching sheet,"
ZAMP, 2017
[Ref No.: 3630]

dr. mohammad marufuzzaman" location based sequence prediction algorithm for determining next activity in smart home."
Journal of Engineering Science and Technology Review, 2017
[Ref No.: 3624]

shahadat hossain" measurement of indooor terrestrial gamma radiation dose and evaluation of annual effective dose at aecd campus, dhaka , bangladesh"
International Journal of Scientific Research and Management, 2017
[Ref No.: 3608]

dr. md. atikur rahman khan" disclosure risk reduction for generalized linear model output in a remote analysis system"
Data & Knowledge Engineering, 2017
[Ref No.: 3600]

dr. md. atikur rahman khan" forecasting stochastic processes using singular spectrum analysis: aspects of the theory and application"
International Journal of Forecasting, 2017
[Ref No.: 3601]

dr. md. atikur rahman khan" perturbed robust linear estimating equations for confidentiality protection in remote analysis"
Statistics and Computing, 2017
[Ref No.: 3602]

mohammad mobarak hossen " dust-acoustic shock excitations in κ-nonthermal electron depleted dusty plasmas"
Springer EPJ D, 2017
[Ref No.: 3649]

mohammad mobarak hossen " electrostaticshockwavesinanonthermaldustyplasmawithoppositelychargeddust"
Elsevier High Energy Density Physics, 2017
[Ref No.: 3650]

dr. md. mozahar ali " hydrothermal synthesis, structure, and superconductivity of simple cubic perovskite (ba0.62k0.38)(bi0.92mg0.08)o3 with tc ∼ 30 k"
Inorganic Chemistry, 2017
[Ref No.: 3651]

ayesha siddiqua" effect of reynold’s number for mixed convection flow of nanofluid in a double lid driven cavity with heat generating obstacle."
Heat and Mass Transfer Research Journal (HMTRJ), 2017
[Ref No.: 3714]

atika farzana urmi" discriminating students of public and private universities in respect of some social characters"
Journal of Statistical studies, 2017
[Ref No.: 3690]

abhijit bhowmik" analysis of the veracities of industry used software development life cycle methodologies"
AIUB Journal of Science and Engineering, 2017
[Ref No.: 3936]

dr. a. f. m. saifuddin saif" an algorithm to find out risk free share to invest in stock market"
International Journal of Engineering Trends and Technology (IJETT), 2017
[Ref No.: 3979]

dr. a. f. m. saifuddin saif" a study of pupil orientation and detection of pupil using circle algorithm: a review"
International Journal of Engineering Trends and Technology (IJETT), 2017
[Ref No.: 3980]

dr. a. f. m. saifuddin saif" performance comparison of min-max normalization on frontal face detection using haar classifiers"
Pertanika Journal of Science & Technology (JST), 2017
[Ref No.: 3981]

dr. s. a. m. manzur h. khan" ict integration in management for public educational institutions in bangladesh"
Open Journal of Advances in Business & Management (OJABM), 2016
[Ref No.: 4043]

dr. mohammad tariqul islam" swelling and absorption properties of polyvinyl alcohol (pva) and acrylic acid blend hydrogels: effect of γ-irradiation"
Chemical Technology: An Indian Journal (IF:0.34), 2016
[Ref No.: 3940]

dr. mohammad tariqul islam" studies on swelling and absorption properties of the γ–irradiated polyvinyl alcohol (pva)/kappa-carrageenan blend hydrogels"
Journal of Advanced Chemical Engineering, 2016
[Ref No.: 3942]

dr. md. saddam mukta hossain" identifying and validating personality traits-based homophilies for an egocentric network"
Social Network Analysis and Mining, Springer, 2016
[Ref No.: 3683]

dr. mohammed jashim uddin" nanofluid slip flow over a stretching cylinder with schmidt and péclet number effects"
AIP Advances, 2016
[Ref No.: 3729]

dr. mohammed jashim uddin" multiple slips and variable transport property effect onmagnetohydromagnetic dissipative thermosolutal convection in a porous medium"
Journal of Aerospace Engineering, 2016
[Ref No.: 3730]

dr. mohammed jashim uddin" two parameter scaling group for unsteady convective magnetohydrodynamic flow."
Alexandria Engineering Journal, 2016
[Ref No.: 3731]

dr. mohammed jashim uddin" a.a. afify and m.j uddin, lie symmetries analysis of double-diffusive free convective slip flow with convective boundary conition past a radiating vertical surface embedded in porous medium"
Journal of Applied Mechanics and Technical Physics,, 2016
[Ref No.: 3732]

dr. mahadeb kumar das" numerical study on unsteady mhd free convection and mass transfer flow past a vertical flat plate in porous medium, chemical reaction and soret effects"
Elixir Applied Mathematics, 2016
[Ref No.: 3751]

dr. mohammed jashim uddin" group analysis and numerical solution of slip flow of a nanofluid in porous media with heat transfer."
Progress in Computational Fluid Dynamics, an International Journal, 2016
[Ref No.: 3735]

dr. mohammed jashim uddin" two-component modeling for non-newtonian nanofluid slip flow and heat transfer over sheet: lie group approach"
Applied Mathematics and Mechanics,, 2016
[Ref No.: 3736]

dr. mohammed jashim uddin" numerical simulation of self-similar thermal convection from a spinning cone in anisotropic porous medium."
Journal of Hydrodynamics, Ser. B,, 2016
[Ref No.: 3737]

dr. mohammed jashim uddin" stefan blowing, navier slip, and radiation effects on thermo-solutal convection from a spinning cone in an anisotropic porous medium.."
Journal of Porous Media,, 2016
[Ref No.: 3738]

dr. mohammed jashim uddin" symmetry group and numerical study of non-newtonian nanofluid transport in a porous medium with multiple convective boundary and nonlinear radiation."
International Journal of Numerical Methods for Heat & Fluid Flow., 2016
[Ref No.: 3739]

dr. mohammed jashim uddin" effect of variable properties, navier slip and convective heating on hydromagnetic transport phenomena."
Indian Journal of Physics, 2016
[Ref No.: 3740]

dr. mohammed jashim uddin" numerical solutions for gyrotactic bioconvection in nanofluid-saturated porous media with stefan blowing and multiple slip effects."
Computers & Mathematics with Applications, 2016
[Ref No.: 3741]

uddin, a., bhoosreddy, j., marisha tiwari, singh, v.k. "a sciento-text framework to characterize research strength of institutions at fine-grained thematic area level"
Scientometrics, 2016
[Ref No.: 3677]

solanki, t., uddin, a., singh, v.k. "research competitiveness of indian institutes of science education and research"
Current Science, 2016
[Ref No.: 3678]

rupika, uddin, a., singh, v.k. "measuring the university–industry– government collaboration in indian research output"
Current Science, 2016
[Ref No.: 3679]

dr. md. mozahar ali " floating zone growth and characterization of (ca1-xndx)12al14o33+6x (x  0.001) single crystals"
ACS Omega, 2016
[Ref No.: 3652]

dr. md. mozahar ali " determination of solubility limits and distribution coefficients of rare earth ln3+ ions (ln = y, ho, eu or nd) in ca12al14o33 crystals using floating zone growth"
Journal of Flux Growth, 2016
[Ref No.: 3653]

dr. md. mozahar ali " hydrothermal synthesis, crystal structure, and superconductivity of a double-perovskite bi oxide"
Chemistry of Materials, 2016
[Ref No.: 3654]

dr. mohammad mahmudul hasan" regulatory requirements compliance in requirements engineering: a systematic classification and analysis"
International Journal of Systems and Service-Oriented Engineering (IJSSOE), 2016
[Ref No.: 3635]

mohammad mobarak hossen " oblique propagation of low frequency nonlinear waves in an electron depleted magnetized plasma with positive and negative dust"
AIP Physics of Plasmas, 2016
[Ref No.: 3647]

mohammad mobarak hossen " low frequency nonlinear waves in electron depleted magnetized nonthermal plasmas"
Springer EPJ D, 2016
[Ref No.: 3648]

dr. md. atikur rahman khan" signal identification in singular spectrum analysis"
Australian & New Zealand Journal of Statistics, 2016
[Ref No.: 3603]

dr. md. sakir hossain" low complexity null subcarrier-assisted ofdm papr reduction with improved ber"
IEEE Communication Letters, 2016
[Ref No.: 3643]

prof. dr. kh. abdul maleque" mhd non-newtonian casson fluid heat and mass transfer flow with exothermic/endothermic binary chemical reaction and activation energy"
Journal American Journal of Heat and Mass Transfer, 2016
[Ref No.: 3849]

dr. mohammed jashim uddin" computational study of three-dimensional stagnation point nanofluid bioconvection flow on a moving surface with anisotropic slip and thermal jump effect"
ASME Journal of Heat Transfer, 2016
[Ref No.: 3820]

dr. mohammed jashim uddin" computational investigation of stefan blowing and multiple slips effect on buoyancy-driven bioconvection nanofluid flow with microorganisms,"
International Journal of Heat and Mass Transfer, 2016
[Ref No.: 3821]

dr. mohammed jashim uddin" energy conversion under conjugate conduction, magneto-convection, diffusion and nonlinear radiation over a non-linearly stretching sheet with slip and multiple convective boundary conditions"
Energy,, 2016
[Ref No.: 3822]

dr. s. mosaddeq ahmed" one step cyclocondensation of (thio)barbituric acid with chalcones in glacial acetic acid and phosphorous pentoxide, part-i"
Bangladesh Journal Scientific and Industrial Research, 2016
[Ref No.: 3816]

md. ezazul islam" an approach to security for unstructured big data"
The Review of Socionetwork Strategies, 2016
[Ref No.: 3802]

prof. dr. kh. abdul maleque" mhd free-convective and mass transfer flow past a continuously moving semi-infinite vertical porous plate with thermal diffusion"
American Journal of Heat and Mass Transfer, 2016
[Ref No.: 3853]

prof. dr. kh. abdul maleque" unsteady mhd non-newtonian casson fluid flow due to a porous rotating disk with uniform electric field."
Journal Fluid Mechanics: Open Access, 2016
[Ref No.: 3862]

prof. dr. kh. abdul maleque" temperature dependent variable properties on mixed convective unsteady mhd laminar incompressible fluid flow with heat transfer and viscous dissipation"
Journal Fluid Mechanics: Open Access, 2016
[Ref No.: 3868]

dr. mahfuza khatun" discriminating the students of universities by their smoking habit"
AIUB Journal of Science and Engineering, 2016
[Ref No.: 4399]

md. hasibul hasan" a learning dataset aimed at predicting the feedbacks for bengali blogs"
AIUB Journal of Science and Engineering, 2016
[Ref No.: 4512]

dr. mohammad mahbub rabbani" optimum conditions for the fabrication of zein/ag composite nanoparticles from ethanol/h2o co-solvents using electrospinning"
Nanomaterials, 2016
[Ref No.: 4500]

shohag barman, hiralal gope, m m manjurul islam, md mehedi hasan, and umme salma "clustering techniques for software engineering"
Indonesian Journal of Electrical Engineering and Computer Science, 2016
Keywords: Software engineering for Contemporary Software Systems [Ref No.: 4732]

dr. shohag barman" clustering techniques for software engineering"
Indonesian Journal of Electrical Engineering and Computer Science, 2016
[Ref No.: 4692]

dr. shohag barman" fire detection in still image using color mode"
Indonesian Journal of Electrical Engineering and Computer Science, 2016
[Ref No.: 4693]

dr. md. tarek hossain" transformation of orbital angular momentum and spin angular momentum"
American Journal of Mathematics and Statistics, 2016
[Ref No.: 4823]

tasnim rahman" seqdev: an algorithm for constructing genetic elements using comparative assembly"
Plant Tissue Culture and Biotechnology, 2016
[Ref No.: 4794]

dr. mohammed jashim uddin" numerical simulation of self-similar thermal convection from a spinning cone in anisotropic porous medium"
Journal of Hydrodynamics, Ser. B,, 2016
[Ref No.: 3104]

dr. mohammed jashim uddin" lie group analysis and numerical solutions for magnetoconvective slip flow along a moving chemically reacting radiating plate in porous media with variable mass diffusivity"
Heat Transfer Asian Research, 2016
[Ref No.: 3102]

dr. mohammed jashim uddin" numerical study of free convective flow of a nanofluid over a chemically reactive porous flat vertical plate with second order slip model"
Journal of Aerospace Engineering, 2016
[Ref No.: 3135]

dr. mohammed jashim uddin" boundary layer flow over a moving vertical flat plate with convective thermal boundary condition"
Bulletin of the Malaysian Mathematical Sciences Society, 2016
[Ref No.: 3121]

dr. mohammed jashim uddin" group analysis and numerical solution of slip flow of a nanofluid in porous media with heat transfe"
Progress in Computational Fluid Dynamics, 2016
[Ref No.: 3124]

dr. mohammad mahbub rabbani" characterization of pullulan/chitosan oligosaccharide/ montmorillonite nanofibers prepared by electrospinning technique"
Journal of Nanoscience and Nanotechnology, 2016
[Ref No.: 2998]

md. mahfuzur rhaman" numerical simulation and analysis of incompressible newtonian fluid flows using freefem++"
Journal of Advanced Research in Fluid Mechanics and Thermal Sciences, 2016
[Ref No.: 3495]

md. jamsher ali" analysis of numerical methods for differential-algebraic equations. the one step methods"
International Journal of Fuzzy Mathematical Archive, 2016
[Ref No.: 3473]

prof. dr. dip nandi" test case prioritization based on fault dependency"
International Journal of Modern Education and Computer Science., 2016
[Ref No.: 3436]

shovra das" a learning dataset aimed at predicting the feedbacks for bengali blogs"
The AIUB Journal of Science and Engineering (AJSE), 2016
[Ref No.: 3432]

riashat islam" active learning with image data"
Neural Information Processing Systems, 2016
[Ref No.: 3433]

ayesha siddiqua" heat line analysis for mhd mixed convection flow of nanofluid within a driven cavity containing heat generating block."
AIP Conference Proceedings, 2016
[Ref No.: 3550]

dr. md. kamruzzaman" self-preservation in a zero pressure gradient rough wall turbulent boundary layer"
Journal of Fluid Mechanics, 2016
[Ref No.: 3544]

rahman mohammod hafizur" a learning dataset aimed at predicting the feedbacks for bengali blogs"
The AIUB Journal of Science and Engineering (AJSE), 2016
[Ref No.: 3514]

humaira haroon" j/psi momentum spectrum in the decay of b –meson in parton model"
The AIUB Journal of Science and Engineering (AJSE), 2016
[Ref No.: 3560]

md. fahad monir" a study on wireless sensor network deployment and lifetime maximization of wireless sensor nodes in natural gas pipeline monitoring system"
Journal of Communication Engineering & Systems., 2016
[Ref No.: 3580]

md. fahad monir" review for deployment of femtocells in soho"
Journal of Mobile Computing, Communications & Mobile Networks, 2016
[Ref No.: 3573]

dr. md. abdul hamid" supervisory routing control for dynamic load balancing in low data rate wireless sensor networks"
Wireless Networks, 2016
[Ref No.: 3295]

md habib ullah, chang-sik ha "in situ prepared polypyrrole–ag nanocomposites: optical properties and morphology"
Journal of Materials Science, 2016
[Ref No.: 3383]

dr. akinul islam jony" applications of real-time big data analytics"
International Journal of Computer Applications, 2016
[Ref No.: 3401]

dr. akinul islam jony" real time social network data analysis for community detection"
International Journal of Computer Applications, 2016
[Ref No.: 3402]

roushanara begum" effects of different boundary conditions at the surfaces of the extended computational domain in computing the natural convection flow in an open cavity."
The Dhaka University Journal of Science, 2016
[Ref No.: 3407]

dr. s. n. m. azizul hoque" adapting the nequick 2 model to gps derived tec data at a given location"
The AIUB Journal of Science and Engineering (AJSE), 2016
[Ref No.: 3412]

sharfuddin mahmood" test case prioritization based on fault dependency"
International Journal of Modern Education and Computer Science, 2016
[Ref No.: 3420]

dr. mohammad mahbub rabbani" dyeing of electrospun nylon 6 nanofibers with reactive dyes using electron beam irradiation"
Journal of Industrial and Engineering Chemistry, 2016
[Ref No.: 3428]

dr. saiful islam "a high surface area tunnel-type α-mno2 nanorod cathode by a simple solvent-free synthesis for rechargeable aqueous zinc-ion batteries"
Chemical Physics Letters, 2016
[Ref No.: 5319]

md. saidul islam,mohammad razaul karim,saiful islam,jaekook kim,nurun nahar rabin,ryo ohtani,masaaki nakamura,michio koinuma,shinya hayami, "in situ generation of silicon oxycarbide phases on reduced graphene oxide for li–ion battery anode"
Chemistryselect, 2016
[Ref No.: 5320]

dr. md alamgir kabir "an improved usability evaluation model for point-of-sale systems"
International Journal of Smart Home, 2016
[Ref No.: 5274]

israt jahan mouri" traffic control management and road safety using vehicle to vehicle data transmission based on li-fi technology"
International Journal of Computer Science, Engineering and Information Technology (IJCSEIT), 2016
[Ref No.: 5368]

dr. mahfuza khatun" title of report: socioeconomic factors responsible for diabetes among urban and rural people of bangladesh: a factor analysis approach. b. name of journal"
Global Journal of Quantitative Science, 2016
[Ref No.: 5175]

dr. md. sohidul islam" low loss topas based porous-core single-mode photonic crystal fiber for thz communications"
Indian Journal of Pure and Applied Physics, 2016
[Ref No.: 5179]

9. mj uddin, wa khan, ft zohra, aim ismail "blasius and sakiadis slip flows of nanofluid with radiation effects"
Journal of Aerospace Engineering, 2016
[Ref No.: 4991]

dr. s. m. hasan mahmud" an agent-based meta-search engine architecture for open government datasets search"
Communications on Applied Electronics, 2016
[Ref No.: 5040]

dr. dilruba yasmin" visco-elastic fluid flow on mhd free convection and mass transfer flow with thermal and mass diffusion"
International Journal of Engineering-Annals of the Faculty of Engineering Hunedoara, 2016
[Ref No.: 4925]

dr. md. taimur ahad" exploring the usage of the mobile phones by smes in the achievement of vision2020 goals"
Journal of Mobile Technologies, Knowledge, and Society, 2016
[Ref No.: 4945]

dr. md. asraf ali" semg activities of the three heads of the triceps brachii muscle during cricket bowling"
Journal of Mechanics in Medicine and Biology, 2016
[Ref No.: 4978]

dr. abdus salam" save time for public transport users in a developing country"
International Journal of Education and Management Engineering (IJEME), 2016
[Ref No.: 5889]

dr. md. mozahar ali" floating zone growth and characterization of (ca1–xndx)12al14o33+6x (x ∼ 0.001) single crystals"
ACS omega, 2016
[Ref No.: 5671]

dr. md. mozahar ali" determination of solubility limits and distribution coefficients of rare earth ln3+ ions (ln= y, ho, eu or nd) in ca12al14o33 crystals using floating zone growth"
J. Flux Growth, 2016
[Ref No.: 5672]

dr. md. mozahar ali" hydrothermal synthesis, crystal structure, and superconductivity of a double-perovskite bi oxide"
Chemistry of Materials, 2016
[Ref No.: 5673]

mehedi hasan, m. a. hakim, m. a. basith, md. sarowar hossain, bashir ahmmad, m. a. zubair, a. hussain, and md. fakhrul islam "size dependent magnetic and electrical properties of ba-doped nanocrystalline bifeo3"
AIP Advances, 2016
[Ref No.: 6050]

mehedi hasan, m.a. basith, m.a. zubair, md. sarowar hossain, rubayyat mahbub, m.a. hakim, md. fakhrul islam "saturation magnetization and band gap tuning in bifeo3 nanoparticles via co-substitution of gd and mn"
Journal of Alloys and Compounds, 2016
[Ref No.: 6051]

mehedi hasan, md. fakhrul islam, rubayyat mahbub, md. sarowar hossain, m.a. hakim "a soft chemical route to the synthesis of bifeo3 nanoparticles with enhanced magnetization"
Materials Research Bulletin, 2016
[Ref No.: 6053]

md iftekharul mobin, md abid-ar-rafi, md neamul islam and md rifat hasan" an intelligent fire detection and mitigation system safe from fire (sff)"
International Journal of Computer Applications, 2016
[Ref No.: 6011]

rajarshi roy chowdhury "a proportional study of nearest neighbour and simulated annealing algorithms by using symmetric tsp"
North East University Bangladesh Journal, 2016
[Ref No.: 6757]

rajarshi roy chowdhury, sushanta acharjee "a proportional study on ip address"
Sylhet International University Studies (SIU Studies), 2016
[Ref No.: 6758]

m sarkar, jb islam, s akter" pollution and ecological risk assessment for the environmentally impacted turag river, bangladesh"
Journal of Materials and Environmental Science, 2016
[Ref No.: 6603]

ks ahmed, akml rahman, m sarkar, jb islam, ia jahan, m moniruzzaman, b saha, nc bhoumik" assessment on the level of contamination of turag river at tongi area in dhaka"
Bangladesh Journal of Scientific and Industrial Research, 2016
[Ref No.: 6604]

mohammad shahadat hossain, ahmed afif monrat, mamun hasan, razuan karim, tanveer ahmed bhuiyan, md saifuddin khalid "a belief rule-based expert system to assess mental disorder under uncertainty"
5th International Conference on Informatics, Electronics and Vision (ICIEV), 2016
Keywords: Expert Systems [Ref No.: 6534]

razuan karim, karl andersson, mohammad shahadat hossain, md jasim uddin, md perveg meah "a belief rule based expert system to assess clinical bronchopneumonia suspicion"
Proceedings of Future Technologies Conference 2016 (FTC 2016), 2016
Keywords: Expert Systems [Ref No.: 6535]

mohammad shahadat hossain, mohammad a. haque, rashed mustafa, razuan karim, hirak chandra dey, md. yusuf" an expert system to assist the diagnosis of ischemic heart disease"
International Journal for Integrated Care (ICIC), 2016
Keywords: Expert Systems [Ref No.: 6520]

md. ezazul islam" an approach to security for unstructured big data"
The Review of Socionetwork Strategies, 2016
[Ref No.: 6515]

prof. dr. md. rafiqul islam" a new approach to access control in cloud"
The Arabian Journal of Science and Engineering, 2016
[Ref No.: 6516]

prof. dr. md. rafiqul islam" chemical reaction optimization for solving shortest common supersequence problem,"
Computational Biology and Chemistr, 2016
[Ref No.: 6517]

r. karim, m. s. hossain, m. s. khalid, r. mustafa, t. a. bhuiyan "a belief rule based expert system to assess bronchiolitis suspicion from signs and symptoms under uncertainty"
Proceedings of SAI Intelligent Systems Conference (IntelliSys), 2016
Keywords: Expert Systems [Ref No.: 6530]

a. a. nahid, m. m. hossain, mahfuzur rahman* "effect of some metal ions on the photocatalytic oxidation of remazol black b in aqueous solution under uv irradiation"
Journal of Advanced Oxidation Technologies, 2016
[Ref No.: 6490]

s.h. naqib, m. afsana azam, m. borhan uddin "a simple model for normal state in- and out-of-plane resistivities of hole doped cuprates"
Physica C: Superconductivity and its applications, 2016
Keywords: Materials and Processing [Ref No.: 6492]

jahida b islam, mamon sarkar, akm lutfor rahman, k shahin ahmed "quantitative assessment of toxicity in the shitalakkhya river, bangladesh"
The Egyptian Journal of Aquatic Research, 2015
[Ref No.: 6424]

m sarkar, jb islam, ks ahmed, a rahman, ba begum" evaluation of transboundary impact on air pollution in a rural area shyamnagar, bangladesh"
Mesopotamia Environmental Journal, 2015
[Ref No.: 6425]

m sarkar, akml rahman, jb islam, ks ahmed" study of hydrochemistry and pollution status of the buriganga river, bangladesh"
Bangladesh Journal of Scientific and Industrial Research, 2015
[Ref No.: 6426]

dr. mahadeb kumar das" to determine the best wavelet by the compression of an image (fingerprint) using two types of wavelets base on wavelet and wavelet-packet"
Elixir Journal of Applied Mathematics, 2015
[Ref No.: 6538]

bilkis a begum, k shahin ahmed, m sarkar, jb islam, akm lutfor rahman" status of ambient particulate matter and black carbon concentrations in rajshahi air, bangladesh"
Journal of Bangladesh Academy of Sciences, 2015
[Ref No.: 6602]

s jahan, m n h liton, m k r khan and m mozibur rahman "effect of aluminum doping on the properties of spray deposited copper sulfide (cu2s) thin films"
International Journal of Advanced Engineering Technology, 2015
Keywords: Natural Sciences [Ref No.: 6732]

dr. md. mozahar ali" hydrothermal synthesis of a new bi-based (ba0. 82k0. 18)(bi0. 53pb0. 47) o3 superconductor"
Journal of Alloys and Compounds, 2015
[Ref No.: 5674]

dr. md. asraf ali" muscle fatigue in the three heads of the triceps brachii during a controlled forceful hand grip task with full elbow extension using surface electromyography"
Journal of Human Kinetics, 2015
[Ref No.: 4976]

dr. md. asraf ali" analysis of crosstalk in the mechanomyographic signals generated by forearm muscles during different wrist postures"
Muscle & Nerve, 2015
[Ref No.: 4977]

dr. debajyoti karmaker" an extended research on the blood donor community as a mobile application"
IJ Wireless and Microwave Technologies, 2015
[Ref No.: 5185]

dr. debajyoti karmaker" an automated music selector derived from weather condition and its impact on human psychology"
GSTF Journal on Computing (JoC), Global Science and Technology Forum, 2015
[Ref No.: 5186]

dr. debajyoti karmaker" face recognition using eigenfaces"
International Journal of Computer Applications, 2015
[Ref No.: 5187]

dr. debajyoti karmaker" simple approach to traffic update system"
International Journal of Computer Applications, 2015
[Ref No.: 5188]

dr. khandaker tabin hasan" automated person identification system using walking pattern biometrics"
International Journal of Scientific & Engineering Research, 2015
[Ref No.: 5203]

rutaba jania" x-rays and other associated techniques in identifying organic compounds for the production of synthetic graphite"
The AIUB Journal Of Science and Engineering (AJSE), 2015
[Ref No.: 5137]

israt jahan mouri" a smart, location based time and attendance tracking system using android application"
International Journal of Computer Science, Engineering and Information Technology (IJCSEIT), 2015
[Ref No.: 5367]

kamruddin nur, marc morenza-cinos, anna carreras, and rafael pous "projection of rfid-obtained product information on a retail stores indoor panoramas"
IEEE Intelligent Systems, 2015
Keywords: Internet of Things,Computer Vision,Robotics [Ref No.: 5566]

m. f. mridha, molla rashied hussein, md. musfiqur rahaman, jugal krishna das" a proficient autonomous bangla semantic parser for natural language processing"
ARPN Journal of Engineering and Applied Sciences, 2015
[Ref No.: 5549]

21. m. f. mridha, aloke kumar saha, md. akhtaruzzaman adnan, molla rashied hussain and jugal krishna das" design and implementation of an efficient enconverter for bangla language"
ARPN Journal of Engineering and Applied Sciences, 2015
[Ref No.: 5550]

dr. a. f. m. saifuddin saif" moment feature based fast feature extraction algorithm for moving object detection using aerial images"
PLoS ONE, 2015
[Ref No.: 3379]

dr. md. kamruzzaman" spectroscopic study of the interaction between adenosine disodium triphosphate and gatifloxacin-al3+ complex and its analytical application"
Luminescence, The Journal of Biological and Chemical Luminescence, 2015
[Ref No.: 3334]

dr. md. kamruzzaman" effects of temperature in electrodepostion of znte thin films"
Journal of Materials Science: Materials in Electronics, 2015
[Ref No.: 3335]

prof. dr. dip nandi" investigation of participation and quality of online interaction."
International Journal of Modern Education and Computer Science., 2015
[Ref No.: 3303]

prof. dr. dip nandi" what factors impact student–content interaction in fully online courses?"
International Journal of Modern Education and Computer Science., 2015
[Ref No.: 3304]

prof. dr. dip nandi" a proposed modification of k-means algorithm"
International Journal of Modern Education and Computer Science., 2015
[Ref No.: 3305]

prof. dr. dip nandi" a high-throughput routing metric for multi-hop underwater acoustic networks"
Computers & Electrical Engineering, 2015
[Ref No.: 3306]

a. m. anisul huq" a compact routing based mapping system for the locator/id separation protocol (lisp)"
International Journal of Computer Applications (IJCA), 2015
[Ref No.: 3252]

a. m. anisul huq" a reputation based system to overcome malicious behavior in peer-to-peer networks"
International Journal of Computer Applications, 2015
[Ref No.: 3253]

a. m. anisul huq" a review: performance measurements of transport protocols"
International Journal of Advanced Research in Computer and Communication Engineering (IJARCCE), 2015
[Ref No.: 3254]

dr. md. alamgir badsha" broadband epsilon-near-zero perfect absorption in the near-infrared"
Scientific Reports, 2015
[Ref No.: 3264]

dr. md. abdul hamid" qos and trust-aware coalition formation game in data-intensive cloud federations"
Concurrency and Computation: Practice and Experience, 2015
[Ref No.: 3266]

md. masud parvez" experimental studies on the nonlinear optical properties of linbo3 crystal."
AMERICAN JOURNAL OF SCIENTIFIC AND INDUSTRIAL RESEARCH, 2015
[Ref No.: 3591]

dr. md. sohidul islam" average secrecy mutual information of the non-identically independently distributed hoyt fading wireless channels"
International Journal of Electrical, Computer, Energetic, Electronic and Communication Engineering, 2015
[Ref No.: 3572]

rahman mohammod hafizur" simple approach to traffic update system"
International Journal of Computer Applications, Foundation of Computer Science (IJCA), 2015
[Ref No.: 3512]

rahman mohammod hafizur" face recognition using eigenfaces"
International Journal of Computer Applications (IJCA), 2015
[Ref No.: 3513]

dr. afroza nahar" global prospects, progress, policies, and environmental impact of solar photovoltaic power generation."
Renewable and Sustainable Energy Reviews, 2015
[Ref No.: 3533]

dr. md. kamruzzaman" drag of a turbulent boundary layer with trans- verse 2d circular rods on the wall"
Experiments in Fluids, 2015
[Ref No.: 3540]

dr. md. kamruzzaman" scale by scale energy budget in a turbulent boundary layer over a rough wall"
International Journal of Heat and fluid flow, 2015
[Ref No.: 3542]

dr. md. kamruzzaman" power-law exponent in the transition period of decay in grid turbulence"
Journal of Fluid Mechanics, 2015
[Ref No.: 3543]

dr. md. saef ullah miah" simple approach to traffic update system"
International Journal of Computer Applications, Foundation of Computer Science (IJCIA), 2015
[Ref No.: 3488]

dr. md. saef ullah miah" face recognition using eigenfaces"
International Journal of Computer Applications, Foundation of Computer Science (IJCIA), 2015
[Ref No.: 3489]

dr. md. saef ullah miah" determining the best agile sdlc for bangladesh’s software industry"
Asian Transactions on Computers, 2015
[Ref No.: 3490]

dr. mohammad mahbub rabbani" novel preparation and characterization of human hair-based nanofibers using electrospinning process"
International Journal of Biological Macromolecules, 2015
[Ref No.: 2999]

mohammad samawat ullah" optimization of wireless ad-hoc networks using an adjacent collaborative directional mac (acdm) protocol"
International Journal of Computer Applications, 2015
[Ref No.: 2981]

mohammad samawat ullah" tea leaf diseases recognition using neural network ensemble"
International Journal of Computer Applications, 2015
[Ref No.: 2982]

4) d karmaker, m s u miah, m a imran, h rahman and a bhowmik "simple approach to traffic update system"
International Journal of Computer Applications, Foundation of Computer Science (IJCIA), 2015
[Ref No.: 2995]

5) m a imran, m s u miah, h rahman, a bhowmik and d karmaker "face recognition using eigenfaces"
International Journal of Computer Applications, Foundation of Computer Science (IJCIA), 2015
[Ref No.: 2996]

6) m islam, d karmaker,m a imran, m s u miah and a bhowmik "determining the best agile sdlc for bangladesh’s software industry"
Asian Transactions on Computers, 2015
[Ref No.: 2997]

dr. mohammad mahmudul hasan" e-government service research development: a literature review"
International Journal of E-Services and Mobile Applications (IJESMA), 2015
[Ref No.: 3004]

sabeth, farzana, islam, md. serajul, endo, tadashi, ohta, nobuhiro "time-resolved photoexcitation dynamics of the electrical conductivity of the magnetic organic superconductor -(bets)2fe0.45ga0.55cl4"
Rapid Communication in Photoscience (RCP), 2015
[Ref No.: 3010]

dr. kazi a. kalpoma" asian dust detection method and time series analysis of 2010, 2013 and 2014 events using aqua modis satellite images (preparing manuscript for the submission by 29th dec))"
International Journal of Remote Sensing, 2015
[Ref No.: 2921]

dr. mohammad tariqul islam" self-assembly of a liquid crystal aba triblock copolymer in a b-selective organic solvent"
Polymer, Elsevier, Impact Factor 4.23, 2015
[Ref No.: 2945]

dr. mohammed jashim uddin" effect of newtonian heating and thermal radiation on heat and mass transfer of nanofluids over a stretching sheet in porous media"
Heat Transfer Asian Research, 2015
[Ref No.: 3101]

dr. mohammed jashim uddin" effect of multiple slips and dissipation on boundary layer flow of nanofluid flow over a flat plate in a darcian porous media"
Journal of Porous Media, 2015
[Ref No.: 3123]

dr. mohammed jashim uddin" bioconvective non-newtonian nanofluid transport over a vertical plate in a porous medium containing micro-organisms in a moving free stream ."
Journal of Porous Media, 2015
[Ref No.: 3127]

dr. mohammed jashim uddin" bioconvective non-newtonian nanofluid transport in porous media containing micro-organisms in a moving free stream"
Journal of Mechanics in Medicine and Biology, 2015
[Ref No.: 3128]

dr. mohammed jashim uddin" radiative convective nanofluid flow past a stretching/shrinking sheet with slip boundary conditions"
AIAA Journal of Thermophysics AND Heat Transfer, 2015
[Ref No.: 3129]

dr. mohammed jashim uddin" group analysis of free convection flow of a magnetic nanofluid with chemical reaction"
Mathematical Problems in Engineering, 2015
[Ref No.: 3130]

dr. mohammed jashim uddin" multiple slip effects on unsteady magnetohydrodynamic mixed convective rear stagnation point flow of nanofluid in a darcian porous medium"
Journal of Porous Media, 2015
[Ref No.: 3131]

dr. mohammed jashim uddin" non-similar solution of free convectiveflow of power law nanofluids in porous medium along a vertical cone/plate with thermal and mass convective boundary conditions"
Canadian J of Physics, 2015
[Ref No.: 3132]

dr. mohammed jashim uddin" g-jitter induced magnetohydrodynamics flow of nanofluid with constant convective thermal and solutal boundary conditions."
PLoS ONE, 2015
[Ref No.: 3133]

dr. mohammed jashim uddin" lie group analysis and numerical solutions for magneto-convective slip flow of nanofluid over a moving plate with newtonian heating boundary condition"
Canadian Journal of Physics, 2015
[Ref No.: 3134]

dr. mohammed jashim uddin" symmetry group and numerical study of non-newtonian nanofluid transport in a porous medium with multiple convective boundary and nonlinear radiation"
International Journal of Numerical Methods for Heat and Fluid Flow, 2015
[Ref No.: 3103]

dr. mohammed jashim uddin" new similarity solution of boundary layer flow along a continuously moving convectively heated horizontal plate by deductive group method."
Thermal Science, 2015
[Ref No.: 3115]

dr. mohammed jashim uddin" computational investigation of hydromagnetic thermo-solutal nanofluid slip flow in darcian porous medium with zero mass flux boundary condition using stretching group transformations"
J Porous Media, 2015
[Ref No.: 3105]

dr. mohammed jashim uddin" lie group analysis and numerical solution of magnetohydrodynamic free convective slip flow of micropolarfluid over a moving plate with heat transfer"
Computers and Mathematics with Applications, 2015
[Ref No.: 3106]

dr. afroza shelley" yrast states and electromagnetic reduced transition properties of 122t e by means of interacting boson model-1"
Problems of atomic science and technology, 2015
[Ref No.: 3091]

dr. mohammed jashim uddin" optimal homotopy asymptotic method for mhd slips flow over a radiating stretching sheet with heat transfer"
Far East Journal of Applied Mathematics, 2015
[Ref No.: 3095]

dr. mohammed jashim uddin" similarity solution of double diffusive free convective flow over a moving vertical flat plate with convective boundary condition"
Ain Shams Journal of Engineering, 2015
[Ref No.: 3097]

dr. mohammed jashim uddin" free convective flow of pseudo plastic and newtonian fluid past a convectively heated vertical plate in a darcian porous medium with heat generation/absorption"
Heat Transfer—Asian Research, 2015
[Ref No.: 3098]

7) a bhowmik, n a nabila,m a imran, m a u rahman and d karmaker "an extended research on the blood donor community as a mobile application"
International Journal of Wireless and Microwave Technologies, 2015
[Ref No.: 3234]

dr. kazi a. kalpoma" logo-recognition-using-surf-features-and-knn-search-tree"
The International Journal of Scientific and Engineering Research (IJSER), 2015
[Ref No.: 3235]

dr. kazi a. kalpoma" automated-person-identification-system-using-walking-pattern-biometrics"
The International Journal of Scientific and Engineering Research (IJSER), 2015
[Ref No.: 3236]

bayzid ashik hossain" otr: a transparent database approach for using ontology in information systems"
The AIUB Journal of Science and Engineering (AJSE), 2015
[Ref No.: 3175]

sharfuddin mahmood" a proposed modification of k-means algorithm"
International Journal of Modern Education and Computer Science, 2015
[Ref No.: 3194]

sharfuddin mahmood" investigation of participation and quality of online interaction"
International Journal of Modern Education and Computer Science, 2015
[Ref No.: 3195]

dr. kamrun nahar mukta" compressive and rarefactive dust ion-acoustic solitary waves with degenerate electron–positron–ion plasma"
Journal of Plasma Physics, 2015
[Ref No.: 4897]

dr. md. tarek hossain" effect of pressure on the valency of cerium in cerium monochalcogenides and cerium monopnictides"
J.Natn.Sci.Foundation Sri Lanka, 2015
[Ref No.: 4824]

raihan uddin ahmed" jonaki - an mlearning tool to reduce illeteracy in bangladesh"
International Journal of Computer Applications (IJCA), 2015
[Ref No.: 4720]

raihan uddin ahmed" a zigzag approach to cascading menu"
Journal of Computer Sciences and Applications, 2015
[Ref No.: 4721]

prodip kumar ghose" mathematical analysis of an hiv/aids epidemic model."
American Journal of Mathematics and Statistics(AJMS), 2015
[Ref No.: 4481]

md. manirul islam" a novel signature-based traffic classification engine to reduce false alarms in intrusion detection systems"
International Journal of Computer Networks & Communications (IJCNC), 2015
[Ref No.: 4495]

prodip kumar ghose" non-newtonian casson fluid heat and mass transfer flow and viscous dissipation with a binary chemical reaction."
The AIUB Journal of Science and Engineering (AJSE), 2015
[Ref No.: 4478]

dr. khandaker tabin hasan" a high-throughput routing metric for multi-hop underwater acoustic networks"
Computers & Electrical Engineering, 2015
[Ref No.: 4292]

abhijit bhowmik" a heuristic approach to course scheduling problem"
The Second IEEE International Conference on Education Technologies and Computers (ICETC), 2015, 2015
[Ref No.: 3934]

prof. dr. kh. abdul maleque" non-newtonian casson fluid heat and mass transfer flow and viscous dissipation with a binary chemical reaction"
The AIUB Journal of Science and Engineering (AJSE), 2015
[Ref No.: 3848]

dr. md. sakir hossain" enhancing cell edge performance using multi-layer soft frequencyreuse scheme"
IET Electronics Letters, 2015
[Ref No.: 3644]

dr. md. sakir hossain" the tropospheric scintillation prediction based on measured data for earth-to-satellite link for bangladeshi climatic condition"
Serbian Journal of Electrical Engineering, 2015
[Ref No.: 3645]

dr. mohammad marufuzzaman" a time series based sequence prediction algorithm to detect activities of daily living in smart home"
Methods of Information in Medicine, 2015
[Ref No.: 3625]

dr. mohammad marufuzzaman" triple data encryption standard encryption engine: a hardware approach"
Indian Journal of Science and Technology, 2015
[Ref No.: 3626]

dr. mohammad marufuzzaman" design perspective of low power, high efficiency shift registers"
Journal of Theoretical and Applied Information Technology, 2015
[Ref No.: 3627]

dr. mohammad mahmudul hasan" implication of requirements engineering in ict4d project development"
International Journal of Information Communication Technologies and Human Development (IJICTHD), 2015
[Ref No.: 3634]

dr. kamruddin md. nur" projection of rfid-obtained product information on a retail store’s indoor panoramas"
IEEE Intelligent Systems, 2015
[Ref No.: 3614]

m. n. u. al mahmud, farzana khalil, md. musfiqur rahman, m. i. r. mamun, mohammad shoeb, a. m. abd el-aty, jong-hyouk park, ho-chul shin, nilufar nahar & jae-han shim" analysis of ddt and its metabolites in soil and water samples obtained in the vicinity of a closed-down factory in bangladesh using various extraction methods"
Environ Monit Assess, 2015
[Ref No.: 3636]

dr. mahadeb kumar das" analytical study on unsteady mhd free convection and mass transfer flow past a vertical porous plate"
American Journal of Applied Mathematics, 2015
[Ref No.: 3752]

dr. mahadeb kumar das" numerical solution of mhd flow in presence of induced magnetic field and hall current effect over an infinite rotating vertical porous plate through porous medium"
American Journal of Engineering Research (AJER), 2015
[Ref No.: 3753]

dr. mahadeb kumar das" effect of porous medium on unsteady heat & mass transfer flow of fluid"
International Journal of Modern Embedded System (IJMES), 2015
[Ref No.: 3754]

tashmiah tamzid anannya" impact of heuristics in clustering large biological networks"
Computational Biology and Chemistry: CBAC (Elsevier), 2015
[Ref No.: 3705]

uddin, a., singh, v.k. "a quantity–quality composite ranking of indian institutions in cs research"
IETE Technical Review, 2015
[Ref No.: 3682]

singh, v.k., uddin, a., pinto, d. "computer science research: the top 100 institutions in india and in the world"
Scientometrics, 2015
[Ref No.: 3698]

uddin, a., singh, v.k., pinto, d., olmos, i. "scientometric mapping of computer science research in mexico"
Scientometrics, 2015
[Ref No.: 3699]

singh, v.k., banshal, s.k., singhal, k., uddin, a. "scientometric mapping of research on “big data”"
Scientometrics, 2015
[Ref No.: 3700]

umme marzia haque" logo_recognition_using_surf_features_and_knn_search_tree"
International Journal of Scientific & Engineering Research, 2015
[Ref No.: 3982]

dr. md. razib hayat khan" software performance evaluation utilizing uml specification and srn model and their formal representation"
Journal of Software, 2014
[Ref No.: 4230]

uddin, a., singh, v.k. "measuring research output and collaboration in south asian countries"
Current Science, 2014
[Ref No.: 3701]

dr. ashraf uddin "the information technology knowledge infrastructure and research in south asia"
Journal of Scientometric Research, 2014
[Ref No.: 3702]

dr. md. mozahar ali " hydrothermal synthesis of a new bi-based (ba 0.82 k 0.18)(bi 0.53 pb 0.47) o 3 superconductor"
Journal of Alloys and Compounds, 2014
[Ref No.: 3655]

dr. md. mozahar ali " new superconductor (na0.25k0.45) ba3bi4o12: a first-principles study"
Physica C, 2014
[Ref No.: 3656]

dr. md. mozahar ali " superconducting double perovskite bismuth oxide prepared by a low‐temperature hydrothermal reaction"
Angewandte Chemie International Edition, 2014
[Ref No.: 3657]

uddin, a., singh, v.k. "mapping the computer science research in saarc countries"
IETE Technical Review, 2014
[Ref No.: 3680]

dr. md. atikur rahman khan" on the theory and practice of singular spectrum analysis forecasting"
EBS Working Paper, Monash University, 2014
[Ref No.: 3604]

jannatul maowa" a new failure detector to detect failures in a distributed system"
International Journal of Scientific & Engineering Research, 2014
[Ref No.: 3632]

dr. mohammad marufuzzaman" high-speed current dq pi controller for vector controlled pmsm drive"
The Scientific World Journal, 2014
[Ref No.: 3628]

dr. mohammad marufuzzaman" fpga based precise and high speed current dq pi controller for foc pmsm drive"
Current Nanoscience, 2014
[Ref No.: 3629]

dr. md. sakir hossain" rain attenuation prediction for terrestrial microwave link in bangladesh"
Journal of Electrical and Electronics Engineering, Romania, 2014
[Ref No.: 3646]

abhijit bhowmik" pbct: a modified polyharmonic broadcasting scheme with seamless channel transition"
9th International Forum on Strategic Technology (IFOST), 2014
[Ref No.: 3932]

dr. mahjabin taskin" dielectric properties of pure and cobalt doped zinc oxide thin films prepared by spray pyrolysis"
Applied Science Reports, 2014
[Ref No.: 4799]

dr. mahjabin taskin" study the effect of molar concentration on the optical and surface properties of zno thin films prepared by spray pyrolysis"
Applied Science Reports, 2014
[Ref No.: 4800]

dr. mahjabin taskin" structural, optical and electrical properties of pure and co-doped zno nano fiber thin films prepared by spray pyrolysis"
Applied Science Reports, 2014
[Ref No.: 4801]

dr. md. tarek hossain" modified single folded potentials for the elastic scattering"
Bangladesh Journal of Physics, 2014
[Ref No.: 4826]

nazia hossain" a comparative analysis on routing protocols of mobile ad hoc network"
International Journal of Computer Science, Engineering and Information Technology (IJCSEIT), 2014
[Ref No.: 4837]

nazia hossain" instant bangla speech to text conversion"
International Journal of Science and Research (IJSR), 2014
[Ref No.: 4838]

s. sultana, s. islam, a. a. mamun "envelope solitons and their modulational instability in dusty plasmas with two-temperature superthermal electrons"
Astrophysics and Space Science, 2014
Keywords: Natural Sciences [Ref No.: 2862]

shahrin chowdhury" a sign language recognition approach for human-robot symbiosis"
International Journal of Computer Science, Engineering and Information Technology, 2014
[Ref No.: 2779]

md. mahfuzur rhaman" numerical analysis and cfd simulations of two dimensional steady flow within square cavity"
Southeast university Journal of Science and Engineering, 2014
[Ref No.: 681]

md. manirul islam" a practical approach to asses fatal attacks in enterprise network to identify effective mitigation techniques"
International Journal of Computer Networks and Communications Security (IJCNCS), 2014
[Ref No.: 701]

prof. dr. kh. abdul maleque" variable electro-conductivity on mhd convective flow past vertical porous plate with heat absorption"
The AIUB Journal of Science and Engineering (AJSE), 2014
[Ref No.: 371]

prof. dr. kh. abdul maleque" binary chemical reaction on boundary layer flow with activation energy and heat absorption"
The Latin American Applied Research Journal (LAAR), 2014
[Ref No.: 379]

a.g.m. zaman" generation of poly-line road network from map data for traffic simulator"
The AIUB Journal of Science and Engineering (AJSE), 2014
[Ref No.: 436]

md. mahfuzur rhaman" numerical simulations of unsteady navier-stokes equations for incompressible newtonian fluids using freefem++ based on finite element method."
Annals of Pure and Applied Mathematics, 2014
[Ref No.: 446]

dr. keshab chandra bhuyan" awareness of health hazard of tobacco consumption among students of american international university - bangladesh"
AJSE, 2014
[Ref No.: 447]

prof. dr. md. rafiqul islam" recognition of bangla numerals using double layered feed forward neural network"
The AIUB Journal of Science and Engineering (AJSE), 2014
[Ref No.: 466]

prof. dr. md. rafiqul islam" data intensive dynamic scheduling model and algorithm for cloud computing security"
Journal of Computers (JCP), Academy Publisher, UK, 2014
[Ref No.: 459]

dr. mahfuza khatun" awareness of health hazard of tobacco consumption among students of american international university- bangladesh"
AIUB Journal of Science and Engineering (AJSE), 2014
[Ref No.: 488]

prof. dr. dip nandi" does learning environment affect the students in introductory programming courses?"
International Journal of advanced studies in Computer Science and Engineering IJASCSE, 2014
[Ref No.: 501]

dr. s. a. m. manzur h. khan" prospect of itescm model based on ict application"
International Journal of Business and Economics Research, 2014
[Ref No.: 11]

ayesha siddiqua" effect of variable..... moving semi-infinite vertical porous plate with heat absorption"
The AIUB Journal of Science and Engineering, 2014
[Ref No.: 70]

dr. mohammad tariqul islam" controlled radical polymerization of vinyl acetate in supercritical co2 catalyzed by cubr/terpyridine"
Korean Journal of Chemical Engineering, Springer, IF: 2.69, 2014
[Ref No.: 3238]

dr. mohammed jashim uddin" effects of melting and thermal dispersion on unsteady mixed convection with heat and mass transfer in non-darcy porous medium."
Journal of Porous Media, 2014
[Ref No.: 3116]

dr. mohammed jashim uddin" combined similarity-numerical solutions of mhd boundary layer slip flow of non-newtonian power-law nanofluids over a radiating moving plate"
Sains Malaysiana, 2014
[Ref No.: 3117]

dr. mohammed jashim uddin" double-diffusive radiative magnetic mixed convective slip flow with biot and richardson number effects"
Journal of Engineering Thermophysics, 2014
[Ref No.: 3118]

dr. mohammed jashim uddin" mathematical modelling of radiative hydromagnetic thermosolutal nanofluid convection slip flow in saturated porous media"
Mathematical Problems in Engineering, 2014
[Ref No.: 3119]

dr. mohammed jashim uddin" scaling transformation for free convection flow of a micropolar fluid along a moving vertical plate in a porous medium with velocity and thermal slip boundary conditions"
Sains Malaysiana, 2014
[Ref No.: 3120]

dr. mohammed jashim uddin" scaling group transformation for mhd boundary layer flow over a permeable stretching sheet in the presence of slip flow with newtonian heating effects ."
Journal of Applied Mathematics and Mechanics, 2014
[Ref No.: 3122]

dr. mohammed jashim uddin" hydromagnetic transport phenomena from a stretching or shrinking nonlinear nanomaterial sheet with navier slip and convective heating: a model for bio-nano-materials processing"
Journal of Magnetism and Magnetic Materials, 2014
[Ref No.: 3125]

dr. mohammed jashim uddin" g-jitter mixed convective slip flow of nanofluid past a permeable stretching sheet embedded in a darcian porous media with variable viscosity"
PloS One, 2014
[Ref No.: 3126]

dr. mohammad tariqul islam" liquid crystal based biosensors using a strong polyelectrolyte-containing block copolymer, poly(4-cyanobiphenyl- 4’-oxyundecylacrylate)-b-poly(sodium styrene sulfonate)"
Macromolecular Research, Springer, IF: 2.047, 2014
[Ref No.: 2946]

dr. mohammad tariqul islam" self-assembly of a liquid crystal aba triblock copolymer in a nematic liquid crystal solvent"
Polymer, Elsevier, Impact Factor 4.23, 2014
[Ref No.: 2947]

f j pettersen, h ferdous, h kalvøy, ø g martinsen and j o høgetveit "comparison of four different fim configurations-a simulation study"
Physiological Measurement, 2014
[Ref No.: 2937]

afsah sharmin" design of a wireless data transmission protocol for underwater acoustic networks"
American Academic & Scholarly Research Journal, 2014
[Ref No.: 2912]

dr. preetom nag" local-heterogeneous responses and transient dynamics of cage breaking and formation in colloidal fluids"
Journal of Chemical Physics, 2014
[Ref No.: 3049]

dr. mohammad mahbub rabbani" poly (vinyl alcohol)/pullulan blend nanofibres prepared from aqueous solutions using electrospinning method"
Polymers & Polymer composites, 2014
[Ref No.: 3014]

dr. mohammad mahbub rabbani" electrochemical characterization of multilayered cdte/pss films prepared by electrostatic self-assembly method"
Transactions on Electrical and Electronic Materials, 2014
[Ref No.: 3015]

dr. mohammad mahbub rabbani" effect of tio2 content and process parameters on electrospun poly(acrylonitrile)/tio2 nanofibers"
Polymers & Polymer composites, 2014
[Ref No.: 3016]

dr. m. m. mahbubul syeed" prediction models and techniques in open source software projects"
International Journal of Open Source Software and Processes (IJOSSP), 2014
[Ref No.: 3469]

dr. m. m. mahbubul syeed" socio-technical dependencies in forked oss projects: revealing evidence from bsd family"
Journal of Software, 2014
[Ref No.: 3470]

dr. md. kamruzzaman" magnetic field effect on fluid flow through a rotating rectangular st raight duct with large aspect ratio"
Progress in Computational Fluid Dynamics An International Journal, 2014
[Ref No.: 3548]

dr. afroza nahar" global renewable energy based electricity generation and smart grid system for energy security”, the scientific world journal, vol. 2014, article id 197136, page 13."
The Scientific World Journal,, 2014
[Ref No.: 3534]

dr. afroza nahar" the effect of pv cell materials on pv system performance."
Advanced Materials Research Journal, 2014
[Ref No.: 3532]

mehnaz seraj" seraj mehnaz, atsuo inomata, kazutoshi fujikawa: "a context aware routing metric for reliable route discovery in manet using fuzzy logic","
IEICE ITS Research Society Proceedings,, Dec, 2014, 2014
[Ref No.: 3518]

dr. md. mahbub chowdhury mishu" a review on pressure ulcer: aetiology, cost, detection and prevention systems"
International Journal of Engineering Sciences & Research Technology, 2014
[Ref No.: 3567]

dr. md. mahbub chowdhury mishu" mathematical modelling of different types of body support surface for pressure ulcer prevention"
International Journal of Biomedical and Biological Engineering, 2014
[Ref No.: 3568]

dr. md. sohidul islam" capacity of a simo system over hoyt fading wireless channels"
DUET Journal, 2014
[Ref No.: 3570]

dr. md. alamgir badsha" admittance matching analysis of perfect absorption in unpatterned thin films"
Optics Communications, 2014
[Ref No.: 3263]

dr. md. abdul hamid" thermal-aware multiconstrained intrabody qos routing for wireless body area networks"
International Journal of Distributed Sensor Networks, 2014
[Ref No.: 3296]

dr. md. abdul hamid" a fault-tolerant structural health monitoring protocol using wireless sensor networks"
Annals of Telecommunications, 2014
[Ref No.: 3297]

jannatul maowa" a new class of graceful tree"
International Journal of Scientific & Engineering Research, 2014
[Ref No.: 3336]

dr. a. f. m. saifuddin saif" moving object detection using dynamic motion modeling from uav aerial images"
Scientific World Journal, 2014
[Ref No.: 3380]

md. shamsur rahim" model of automated system to prevent road crashes due to drunk & drowsy driving"
International Journal of Advanced Research in Computer and Communication Engineering, 2014
[Ref No.: 3317]

dr. a. f. m. saifuddin saif" a conceptual framework: dynamic path planning system for simultaneous localization and mapping multirotor uav"
Advanced Science Letters, 2014
[Ref No.: 3385]

muhammad f. mridha, aloke kumar saha, mahadi hasan and jugal krishna das" solving semantic problem of phrases in nlp using universal networking language (unl)"
International Journal of Advanced Computer Science and Applications(IJACSA), 2014
[Ref No.: 5551]

aloke kumar saha, muhammad f. mridha and jugal krishna das" analysis of bangla root word for universal networking language (unl)"
International Journal of Computer Applications, 2014
[Ref No.: 5560]

gregory l. newman, jamil m. a. rahman, josef b. g. gluyas, dmitry s. yufit, judith a. k. howard, paul j. low "alkynyl–phosphine substituted fe2s2 clusters: synthesis, structure and spectroelectrochemical characterization of a cluster with a class iii mixed–valence [fefe]3+ core"
Journal of Cluster Science, 2014
[Ref No.: 5318]

dr. dilruba yasmin" ionized micropolar fluid flow through a vertical plate"
Advances in Materials Science and Engineering, 2014
[Ref No.: 4926]

dr. dilruba yasmin" diffusion-thermo and thermal-diffusion effects on mhd visco-elastic fluid flow over a vertical plate"
Journal of Applied Fluid Mechanics, 2014
[Ref No.: 4924]

dr. md. asraf ali" significance of the electromyographic analysis of the upper limb muscles of cricket bowlers: recommendations from studies of overhead-throwing athletes"
Journal of Mechanics in Medicine and Biology, 2014
[Ref No.: 4968]

dr. md. asraf ali" longitudinal, lateral and transverse axes of forearm muscles influence the crosstalk in the mechanomyographic signals during isometric wrist postures"
PLoS ONE, 2014
[Ref No.: 4969]

dr. md. asraf ali" surface electromyographic analysis of the biceps brachii muscle of cricket bowlers during bowling"
Australasian Physical & Engineering Sciences in Medicine, 2014
[Ref No.: 4970]

dr. md. asraf ali" crosstalk in mechanomyographic signals from the forearm muscles during sub-maximal to maximal isometric grip force"
PLoS One, 2014
[Ref No.: 4971]

dr. md. asraf ali" emg-force relationship during static contraction: effects on sensor placement locations on biceps brachii muscle"
Technology and Health Care, 2014
[Ref No.: 4972]

dr. md. asraf ali" evaluation of triceps brachii muscle strength during grip force exercise through surface electromyography"
Biomedical Research-India, 2014
[Ref No.: 4973]

dr. md. asraf ali" evaluation of repetitive isometric contractions on the heads of triceps brachii muscle during grip force exercise,"
Technology and Health Care, 2014
[Ref No.: 4974]

dr. md. asraf ali" recent observations in surface electromyography recording of triceps brachii muscle in patients and athletes"
Applied Bionics and Biomechanics, 2014
[Ref No.: 4975]

dr. s. m. hasan mahmud" efficiency of scrum the most widely adopted method for agile software development"
IOSR Journal of Computer Engineering, 2014
[Ref No.: 5041]

sharifa rania mahmud, marzia sultana, nazia majadi, lazima ansari "computational geometry based remote networking"
ACEEE International Journal on Recent Trends in Engineering & Technology, 2014
[Ref No.: 5784]

dr. md. mozahar ali" new superconductor (na0. 25k0. 45) ba3bi4o12: a first-principles study"
Physica C: Superconductivity and its Applications, 2014
[Ref No.: 5675]

dr. md. mozahar ali" superconducting double perovskite bismuth oxide prepared by a low‐temperature hydrothermal reaction"
Angewandte Chemie, 2014
[Ref No.: 5676]

shamim ripon, sumaya mahbub, km intiaz-ud-din "verification of a security adaptive protocol suite using spin"
International Journal of Engineering and Technology (IJET), 2014
[Ref No.: 5607]

k. m. imtiaz-ud-din, touhid bhuiyan, shamim ripon "circle of trust: one-hop-trust-based security paradigm for resource-constraint manet"
Intelligent Computing, Networking, and Informatics. Advances in Intelligent Systems and Computing, 2014
[Ref No.: 5608]

shamim h ripon, syed fahin ahmed, afroza yasmin, yeaminar rashid, km imtiaz-ud-din" formal analysis of a ranked neighbour manet protocol suite"
International Journal of Future Computer and Communication, 2014
[Ref No.: 5609]

azizul azhar ramli, mohammad rabiul islam, mohd farhan md. fudzee, mohamad aizi salamat & shahreen kasim "a practical weather forecasting for air traffic control system using fuzzy hierarchical technique"
Recent Advances on Soft Computing and Data Mining, 2014
[Ref No.: 6004]

hira lal gope, md mehedi hasan, shohag barman, and nihad karim chowdhury "find real time passenger information using intelligent transportation system (its)"
International Journal of Innovation and Scientific Research (IJISR), 2014
Keywords: Smart Cities [Ref No.: 6625]

rajarshi roy chowdhury "security in cloud computing"
International Journal of Computer Applications, 2014
[Ref No.: 6759]

md. abdul awal ansary, rajarshi roy chowdhury, md. jakir mia" a survey of software development practices in sylhet metropolitan software firms, bangladesh"
International Journal of Engineering and Innovative Technology, 2014
[Ref No.: 6760]

rajarshi roy chowdhury, md. abdul awal ansary" a secured mutual authentication protocol for rfid system"
International Journal of Scientific & Technology Research, 2014
[Ref No.: 6761]

sohrab hossain, farhana islam, razuan karim, kn siddique" a critical comparison between distributed database approach and data warehousing approach"
International Journal of Scientific and Engineering Research (IJSER), 2014
Keywords: Distributed and parallel systems [Ref No.: 6521]

sohrab hossain, razuan karim, dhiman sarma" designing a task management system for a banking system by combining relational model with use case diagram"
International Journal of Computer Applications (IJCA), 2014
Keywords: Distributed and parallel systems [Ref No.: 6522]

dr. jahida binte islam" particulate matter and black carbon concentration in ambient air of an urban-traffic influenced site at farm gate, dhaka, bangladesh"
Jagannath University Journal of Science, 2014
[Ref No.: 6423]

m m hassan, m borhan uddin "performance evaluation of contention resolution schemes in optical burst switching"
International Journal of Engineering Research & Technology (IJERT), 2014
Keywords: Wireless/ Mobile Communication [Ref No.: 6493]

mushfiq ahmad, k. asraful islam, m. borhan uddin "reciprocal symmetry and classical discrete oscillator incorporating hall-integral energy levels"
International Journal of Theoretical and Mathematical Physics, 2014
Keywords: Photonics [Ref No.: 6494]

maa nahid, mm hossain, mahfuzur rahman "removal of bractive t blue by photodegradation and adsorption using zno"
Smart Science, 2014
Keywords: Digital Transformation [Ref No.: 6491]

kawser wazed nafi, tonny shekha kar, md. amjad hossain, m. m. a. hashem "e-commerce model based on fuzzy based certain trust model"
Global Journal of Computer Science and Technology, 2013
Keywords: Network Security,Fuzzy Logic,Cloud Computing [Ref No.: 6468]

kn siddiquee and r karim" operational failures: a general issue in government organizations in bangladesh and possible solutions using information technology"
University of Science & Technology Annual (USTA), 2013
Keywords: ICT [Ref No.: 6524]

saeeda sharmeen rahman" component based method for usability testing of a website"
Advanced Materials Research, 2013
[Ref No.: 6027]

sharifa rania mahmud "survey on convex drawing of planar graph"
IOSR Journal of Computer Engineering (IOSRJCE), 2013
[Ref No.: 5785]

sharifa rania mahmud "a simple information retrieval technique"
ACEEE International Journal of Recent Trends in Engineering and Technology (IJRTET), 2013
[Ref No.: 5786]

nazia majadi, sharifa rania mahmud, marzia sultana "uniform distribution technique of cluster heads in leach protocol"
ACEEE International Journal of Recent Trends in Engineering and Technology (IJRTET), 2013
[Ref No.: 5787]

dr. md. asraf ali" markerless tracking of the complex articulated motion in golf swings"
Journal of Bodywork and Movement Therapies, 2013
[Ref No.: 4961]

dr. md. asraf ali" rehabilitation systems for physically disabled patients: a brief review of sensor-based computerised signal-monitoring systems"
Biomedical Research-India, 2013
[Ref No.: 4962]

dr. md. asraf ali" mechanomyography sensor development, related signal processing and applications: a systematic review"
IEEE Sensors Journal, 2013
[Ref No.: 4963]

dr. md. asraf ali" coherence in muscle activity of the biceps brachii at middle, proximal and distal tendon region among the arm wrestling contestants"
Biomedical Research-India, 2013
[Ref No.: 4964]

dr. md. asraf ali" surface electromyography assessment on biceps brachii muscle between endplate region and distal tendon insertion: comparison in terms of gender, dominant arm and contractions"
Journal of Physical Therapy Science, 2013
[Ref No.: 4965]

dr. md. asraf ali" effects of anthropometric variables and electrode placement on the semg activity of the biceps brachii muscle during submaximal isometric contraction in arm wrestling"
Biomedical Engineering/Biomedizinische Technik, 2013
[Ref No.: 4966]

dr. md. asraf ali" surface electromyography for assessing triceps brachii muscle activities: a literature review"
Biocybernetics and Biomedical Engineering, 2013
[Ref No.: 4967]

md. nizamuddinabsayed ul alamshiblyarasimovalicsaiful islamamd. motiur rahamanmazumderamd. saidulislamam. jasimuddindeoguzgulserencermanbengub "an experimental and first-principles study of the effect of b/n doping in tio2 thin films for visible light photo-catalysis"
Journal of Photochemistry and Photobiology A: Chemistry, 2013
[Ref No.: 5308]

md alamgir kabir, md mijanur rahman" a survey on security requirements elicitation and presentation in requirements engineering phase"
American Journal of Engineering Research (AJER), 2013
[Ref No.: 5275]

md alamgir kabir, md. mijanur rahman and md. ismail jabiullah" model for identifying the security of a system: a case study of point of sale system"
IOSR Journal of Computer Engineering (IOSR-JCE), 2013
[Ref No.: 5276]

aloke kumar saha, muhammad f. mridha, shammi akhtar and jugal krishna das" attribute analysis for bangla words for universal networking language(unl)"
International Journal of Advanced Computer Science and Applications(IJACSA), 2013
[Ref No.: 5552]

dr. a. f. m. saifuddin saif" adaptive long term motion pattern analysis for moving object detection using uav aerial images"
International Journal of Information System and Engineering (IJISE2013), 2013
[Ref No.: 3384]

khaza newaz muhammad" energy demand & prospect of geothermal energy as the solution of energy crisis of bangladesh – an approach to green energy solution"
International Journal of Sustainable and Green Energy, 2013
[Ref No.: 3376]

dr. a. f. m. saifuddin saif" vision-based human face recognition using extended principal component analysis"
International Journal of Mobile Computing and Multimedia Communications, 2013
[Ref No.: 3381]

dr. a. f. m. saifuddin saif" a review of machine vision based on moving objects: object detection from uav aerial images"
International Journal of Advancements in Computing Technology(IJACT), 2013
[Ref No.: 3382]

dr. md. kamruzzaman" chemiluminescence determination of moxifloxacin based on its enhancing effect of luminol-ferricyanide system using a microfluidic chip"
Luminescence, The Journal of Biological and Chemical Luminescence, 2013
[Ref No.: 3337]

dr. md. kamruzzaman" chemiluminescence microfluidic system on a chip to determine vitamin b1 using a platinum nanoparticle triggered luminol-agno3 reaction"
Sensor and Actuator B: Chemical, 2013
[Ref No.: 3340]

dr. md. kamruzzaman" chemiluminecence microfluidic system of gold nanoparticles enhanced luminol-silver nitrate for the determination of vitamin b12"
Biomedical Microdevices, 2013
[Ref No.: 3342]

dr. md. abdul hamid" reliable data approximation in wireless sensor network"
Ad Hoc Networks, 2013
[Ref No.: 3298]

dr. md. abdullah - al - jubair" interactive based secured online organizational culture audit system"
Procedia - Social and Behavioral Sciences, Elsevier, 2013
[Ref No.: 3597]

dr. md. abdullah - al - jubair" graphics, audio-visuals and interaction (gai) based handheld augmented reality system"
Procedia - Social and Behavioral Sciences, Elsevier, 2013
[Ref No.: 3598]

dr. md. kamruzzaman" behaviours of energy spect rum at low reynolds number in grid turbulence"
International Journal of Mechanical, Industrial Science and Engineering, 2013
[Ref No.: 3539]

dr. md. kamruzzaman" numerical solution of fluid flow through a rotating rectangular straight duct with magnetic field"
Internatioanl Journal of Mechanical Engineering, 2013
[Ref No.: 3546]

dr. md. kamruzzaman" magnetic effect on direct numerical simulations of fluid flow through a rotating rectangular straight duct"
International Journal of Applied Electromagnetics and Mechanic, 2013
[Ref No.: 3547]

mohammad imrul jubair" an approach to extract features from document image for character recognition"
Global Journal of Computer Science and Technology, 2013
[Ref No.: 3452]

dr. m. m. mahbubul syeed" the evolution of open source software projects: a systematic literature review"
Journal of Software, 2013
[Ref No.: 3471]

md. manzurul hasan, md. saidur rahman & md. rezaul karim "box-rectangular drawings of planar graphs (extended abstract)"
WALCOM: Algorithms and Computation - 2013, 2013
[Ref No.: 3000]

md. manzurul hasan, md. saidur rahman & md. rezaul karim "box-rectangular drawings of planar graphs"
Journal of Graph Algorithms and Applications (Brown University, USA), 2013
[Ref No.: 3001]

dr. mohammad mahbub rabbani" electrospinning fabrication of poly(vinyl alcohol)/tio2 nanofibers"
Textile Coloration and Finishing (J. Korean Soc. Dye. and Finish.), 2013
[Ref No.: 3017]

dr. mohammad mahbub rabbani" photocatalytic activity of electrospun pan/tio2 nanofibers in dye photodecomposition."
Textile Coloration and Finishing (J. Korean Soc. Dye. and Finish.), 2013
[Ref No.: 3018]

dr. mohammad mahbub rabbani" effect of co-solvent ratios and solution concentrations on morphologies of electrospun zein nanomaterials"
Current Research on Agriculture and Life Sciences, 2013
[Ref No.: 3019]

dr. mohammad mahbub rabbani" characterization of au/cdte nanocomposites prepared by electrostatic interaction."
Transactions of Nonferrous Metals Society of China,, 2013
[Ref No.: 3020]

dr. preetom nag" hydro-magnetic convection heat transfer in a micropolar fluid over a vertical plate"
Journal of Applied Fluid Mechanics, 2013
[Ref No.: 3048]

bodrunnesa " preparation and characterization of porous scaffold composite films by blending chitosan and gelatin solutions for skin tissue engineering"
Polymer International, 2013
[Ref No.: 2934]

bodrunnesa " effect of γ-irradiation on the thermomechanical and morphological properties of chitosan obtained from prawn shell: evaluation of potential for irradiated chitosan as plant growth stimulator for malabar spinach."
Radiation Physics and Chemistry, 2013
[Ref No.: 2935]

humayra ferdous , tanvir noor baig and k. siddique-e rabbani "thorax mapping for localised lung impedance change using focused impedance measurement (fim): a pilot study"
Journal of Electrical Bioimpedance, 2013
[Ref No.: 2940]

dr. mohammed jashim uddin" mhd forced convection laminar boundary layer flow from a convectively heated permeable moving vertical plate with radiation effect"
PloS One, 2013
[Ref No.: 3107]

dr. mohammed jashim uddin" lie group analysis and numerical solutions of boundary layer flow of non-newtonian nanofluids along a horizontal plate in porous medium with internal heat generation"
Physica Scripta, 2013
[Ref No.: 3108]

dr. mohammed jashim uddin" hydrodynamic and thermal slip effect on double-diffusive free convective boundary layer flow of a nanofluid past a flat vertical plate in the moving free stream"
PLoS One, 2013
[Ref No.: 3109]

dr. mohammed jashim uddin" free convective flow of a non-newtonian nanofluid past a horizontal flat plate in porous media with nanoparticles and gyrotactic microorganisms"
Journal of Thermophysics and Heat Transfer, 2013
[Ref No.: 3110]

dr. mohammed jashim uddin" heat transfer analysis for falkner-skan boundary layer flow past a wedge with slip condition considering temperature-dependent thermal conductivity"
Sains Malaysiana, 2013
[Ref No.: 3111]

dr. mohammed jashim uddin" numerical analysis of mixed convection over horizontal moving porous flat plate by the method of one parameter continuous group theory"
International Journal of Numerical Methods for Heat and Fluid Flow, 2013
[Ref No.: 3112]

dr. mohammed jashim uddin" scaling group transformation for mhd boundary layer free convective heat and mass transfer flow past a convectively heated nonlinear radiating stretching sheet"
International Journal of Heat and Mass Transfer, 2013
[Ref No.: 3113]

dr. mohammed jashim uddin" double diffusion, slips and variable diffusivity effects on combined heat mass transfer with variable viscosity via a point transformation"
Progress in Computation in Fluid Dynamics, 2013
[Ref No.: 3114]

dr. mohammed jashim uddin" effect of dissipation on free convective flow of a non-newtonian nanofluid in a porous medium with gyrotactic microorganisms"
Journal of Nanosytem and Nanoengineering, 2013
[Ref No.: 3099]

dr. mohammed jashim uddin" effects of radiation on blasius slip flow of oxide nanofluids with merkin boundary condition"
Journal of Nanosytem and Nanoengineering, 2013
[Ref No.: 3100]

dr. mohammed jashim uddin" group analysis and numerical computation of magneto-convective non-newtonian nanofluid slip flow from a permeable stretching sheet"
Appl Nanosci, (SPRINGER), 2013
[Ref No.: 3096]

dr. s. mosaddeq ahmed" studies on the conversion of ketones of heterocyclic spiro compounds having barbituric acid..."
Bangladesh Journal Scientific and Industrial Research, 2013
[Ref No.: 96]

dr. s. mosaddeq ahmed" a one pot synth. of 5, 7-diaryl-1,5-dihydro (or 1, 2, 3, 5-tetrahydro)- pyrano[2, 3-d] pyrimidin..."
Dhaka University Journal of Science, 2013
[Ref No.: 97]

dr. s. mosaddeq ahmed" an efficient synth. of chromene derivatives through a tandem michael addition-cyclization reactn."
Journal of Bangladesh Chemical Society, 2013
[Ref No.: 98]

syed ishteaque ahmed" application of dynamic approach to aiub course scheduling problem"
The AIUB Journal or Science and Engineering, 2013
[Ref No.: 41]

dr. s. a. m. manzur h. khan" a novel framework of e-commerce payment via cell phone"
International Journal of Business & Information Technology, 2013
[Ref No.: 12]

dr. s. a. m. manzur h. khan" impact of uisc: a case study"
International Journal of Business & Information Technology, 2013
[Ref No.: 13]

prof. dr. kh. abdul maleque" binary chemical reactions with arrhenius activation energy on free convection and mass transfer flow"
The Aiub Journal of Science and Engineering (AJSE), 2013
[Ref No.: 181]

prof. dr. kh. abdul maleque" exothermic/endothermic chemical reactions with arrhenius activation energy on mhd thermal radiation"
Journal of Thermodynamics,, 2013
[Ref No.: 190]

prof. dr. kh. abdul maleque" binary chemical reaction and activation energy on mhd boundary layer with viscous dissipation"
ISRN Thermodynamics,, 2013
[Ref No.: 207]

prof. dr. kh. abdul maleque" heat and mass transfer flow with exothermic chemical reactions"
Journal of Pure and Applied Mathematics, 2013
[Ref No.: 208]

prof. dr. kh. abdul maleque" natural convection boundary layer flow with mass transfer and a binary chemical reaction"
British Journal of Applied Science and Technology Technology (Sciencedomain International, 2013
[Ref No.: 318]

sabbir ahmed" application of dynamic approach to aiub course scheduling problem"
The AIUB Journal of Science and Engineering (AJSE), 2013
[Ref No.: 481]

prof. dr. md. rafiqul islam" a version of watershed algorithm for color image segmentation"
The AIUB Journal of Science and Engineering (AJSE), 2013
[Ref No.: 467]

dr. kazi a. kalpoma" ikonos image fusion process using steepest descent method with bi-linear interpolation"
International Journal of Remote Sensing, 2013
[Ref No.: 394]

rezwan ahmed" context enabled query and minimalist metadata visualization: a context bound approach for user and content"
IJCA, 2013
[Ref No.: 593]

mashiour rahman" application of dynamic approach to aiub course scheduling problem"
AIUB Journal of Science and Engineering (AJSE), 2013
[Ref No.: 2729]

md. manirul islam" assessing the tangible and intangible impacts of the convergence of e-learning and knowledge management"
International Journal of Information Sciences and Techniques (IJIST), 2013
[Ref No.: 702]

dr. m. mostafizur rahman" : mhd natural convection flow of fluid with variable viscosity from a porous vertical plate"
Researches and Applications in Mechanical Engineering, 2013
[Ref No.: 672]

dr. m. mostafizur rahman" the effect of radiation on natural convection flow of fluid with variable viscosity from a porous vertical plate"
International Journal of Advanced mathematical sciences, 2013
[Ref No.: 673]

dr. m. mostafizur rahman" effect of radiation on mhd natural convection flow from a porous vertical plate"
International Journal of Scientific Research Engineering &Technology, 2013
[Ref No.: 674]

dr. m. mostafizur rahman" free convection flow of fluid with variable viscosity from a porous vertical plate in presence of heat generation"
Applied Mathematics, 2013
[Ref No.: 661]

dr. m. mostafizur rahman" effect of radiation on natural convection flow from a porous vertical plate in presence of heat generation"
International Journal of Engineering and Applied Sciences, 2013
[Ref No.: 662]

dr. m. mostafizur rahman" deciphering brain functionality through brain modeling: a review on single neuron modeling"
Jahangirnagar University Journal of Information Technology, 2013
[Ref No.: 653]

dr. m. mostafizur rahman" the effect of radiation on mhd natural convection flow of fluid with variable viscosity from a porous vertical plate in presence of heat generation"
Applied and computational mathematics, 2013
[Ref No.: 657]

rezwan ahmed" the history of temporal data visualization and a proposed event centric timeline visualization model"
IJCA, 2013
[Ref No.: 558]

shahrin chowdhury" a security engineering towards building a secure software"
International Journal of Computer Applications (IJCA), 2013
[Ref No.: 2781]

debasis kumar" effect of radiation on free convection flow of non-newtonian power-law fluids along a power-law stretching sheet"
Dhaka University Journal of Science, 2013
[Ref No.: 2783]

dr. kamrun nahar mukta" dust ion-acoustic k-dv and modified k-dv solitons in a dusty degenerate dense plasma"
Physical Review & Research International, 2013
[Ref No.: 4898]

dr. kamrun nahar mukta" nonplanar waves with electronegative dusty plasma"
Physics of Plasmas, 2013
[Ref No.: 4899]

dr. kamrun nahar mukta" the roles of dust grains on electrostatic ia shocks in highly nonlinear dense plasma with degenerate electrons"
IEEE Transactions on Plasma Sciences, 2013
[Ref No.: 4900]

dr. kamrun nahar mukta" sws and dls in ia solitary waves in e-p-i degenerate dense plasma"
The International Journal of Scientific and Engineering Research (IJSER), 2013
[Ref No.: 4901]

dr. kamrun nahar mukta" k-dv and burgers’ equations on da waves with strongly coupled dusty plasma"
Astrophysics and Space Science, 2013
[Ref No.: 4902]

dr. md. abdullah - al - jubair" multimedia based mobile ar system"
International Journal of Interactive Digital Media (IJIDM), 2013
[Ref No.: 4766]

dr. t. m. shahriar sazzad" automatic detection of human body parts especially human hands considering gamma correction and template matching on noisy images"
International Journal of Video&Image Processing and Network Security IJVIPNS-IJENS, 2013
[Ref No.: 4552]

dr. khandaker tabin hasan" the history of temporal data visualization and a proposed event centric timeline visualization model"
International Journal of Computer Applications, 2013
[Ref No.: 4289]

dr. t. m. shahriar sazzad" establishment of an efficient color model from existing models for better gamma encoding in image processing. international journal of image processing"
International Journal of Image Processing (IJIP), 2013
[Ref No.: 4318]

dr. t. m. shahriar sazzad" use of gamma encoder on hsl color model improves human visualization in the field of image processing"
International Journal of Computer Science Engineering (IJCSE), 2013
[Ref No.: 4319]

dr. khandaker tabin hasan" context enabled query and minimalist metadata visualization: a context bound approach for user and content"
International Journal of Computer Applications, 2013
[Ref No.: 4379]

dr. md. atikur rahman khan" moment tests for window length selection in singular spectrum analysis of short- and long-memory processes"
Journal of Time Series Analysis, 2013
[Ref No.: 3605]

dr. md. atikur rahman khan" a note on window length selection in singular spectrum analysis"
Australian & New Zealand Journal of Statistics, 2013
[Ref No.: 3606]

dr. ashraf uddin "computational exploration of theme-based blog data using topic modeling, nerc and sentiment classifier combine"
AASRI Procedia, 2013
[Ref No.: 3703]
"""

# Function to extract author lists and titles
def extract_authors_and_titles(data):
    # Regex pattern to match author list and publication title
    pattern = r'^(.*?)"(.+?)"$'
    matches = re.findall(pattern, data, re.MULTILINE)
    return matches

# Extract data
extracted_data = extract_authors_and_titles(text)

# Define the output CSV file path
output_csv = "aiub_authors.csv"

# Write the extracted data to a CSV file
with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Authors", "Title"])  # Header row
    for authors, title in extracted_data:
        writer.writerow([authors.strip(), title.strip()])

print(f"Data successfully saved to {output_csv}.")
