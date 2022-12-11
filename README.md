## Predicting Student Success on the California ELPAC Summative Assessment

This project is a part of the ADS-599B course in the Applied Data Science Program at the University of San Diego.

## Partners/Contributors:
### Team 3 Members:
- Emma Oo
- Luke Awino
- Oscar Gil

--Project Status:[Active]

## Installation:
To use this project, first clone the repo on your device using the command below:

git init

git clone https://github.com/OscarG-DataSci/ADS-599B.git

Please note, the 1_Deidentify.ipynb script was used to produce the master file Deidentified/elpac.csv. This file is unnecessary to run after you clone the repository.

## Background
The ELPAC test, given to students whose primary language is not English, is used to measure proficiency of the English language from kindergarten (K) to Grade 12 (California Department of Educa-tion, 2022). There are initial ELPAC and summative ELPAC assessments. Initial ELPAC identifies whether students are English learners or ones fluent in English. The summative ELPAC assesses the progress of English learners in listening, speaking, writing, and reading in English. English learner students are given the ELPAC test every year. The test scores are classified into Level 1, 2, 3, and 4. Once the students score Level 4, they are reclassified as fluent English proficient (California Department of Education, 2022). The levels are broken down as:

Level 4: Well developed

Level 3: Moderately developed

Level 2: Somewhat developed

Level 1: Minimally developed

## Project Intro/Objective
With the hypothesis that students with poor attendance are less likely to do well on ELPAC summative assessment, the main purpose of this project is to predict the student ELPAC level for a school district in California.

In addition, we intend to create an application for end users to enter data so that our machine learning model produces a predictive result.

## Technologies:
- Python
- SQL
- Streamlit

## Methodology 
- Data Acquisition 
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Modeling - Machine Learning Algorithms


## Data Acquisition
The file used for this project, elpac.csv, was created from several different sources which include: 
* Attendance information which came from the California Longitudinal Pupil Achievement Data System (CALPADS), Student Attendance Summary (STAS) files, 
for five school years, 2017-2018, through 2021-2022.
*Five years of ELPAC Assessment data was obtained from the California Assessment of Student Performance and Progress (CAASPP).
* Student demographic and Teacher information, was obtained from CALPADS reports 8.1 and 4.4.
* Student and School data is de-identified, per request of the school district that gave us permission to use their data.

## EDA
![Screen Shot 2022-12-10 at 10 13 43 PM](https://user-images.githubusercontent.com/87887191/206889257-caee3fd8-c219-4c66-9d6c-63c8c17ad3b7.png)![Screen Shot 2022-12-10 at 10 10 22 PM](https://user-images.githubusercontent.com/87887191/206889163-aa4f28ad-8d4f-4b59-95cd-18e55a224615.png)

## Feature Engineering
The following features were engineered.
* TestDayName, TestAge, AttendedPct, EnrolledPct, GradeEnrolledPct, GradeAttendedPct, OverallScoreStd, TotalAssessments, TestInstance, and Growth. 
* Label-encoding: Laben-encoding was performed for the categorical variables, StudentGender, StudentEthnicity, Special_Education, Homeless, SocioEconomically, TestDayName, TeacherGender, and TeacherEthnicity.

## Modeling
After the data set was balanced with upsamling, the following algorithms were trained on 70% train dataset and tested on 30% test dataset.
* Several Logistic Regression 
  * Nonstandardized and Standardized dataset
  * Penalized L2 Ridge Logistic Regression 
  * Hypertuned Logistic Regression
* Decision Tree Model
* Random Forest Model
* k-Nearest Neighbors Model
* Graident Boost Classifier (with full varialbes & partial variables)
* Histogram Gradient Boost Model (with full varialbes & partial variables)

## Results

![Screen Shot 2022-12-10 at 10 21 48 PM](https://user-images.githubusercontent.com/87887191/206889481-3c9de8f9-54b7-46cd-8884-ee8d0d6d99fd.png)

![Screen Shot 2022-12-10 at 10 22 03 PM](https://user-images.githubusercontent.com/87887191/206889485-122af046-ad30-4868-9d52-dfb06b47c7d3.png)

Histogram Graident Boost classifer outperformed all other model with accuracy of 97.46% with highest F1 scores. 

## Discussion & Findings

The original hypothesis considered that students with poor attendance are likely not to do well on the ELPAC Summative Assessment, scoring a low OverallLevel. The original hypothesis stands true regarding the importance of attendance, but our final model introduces other supporting features such as the school of attendance weighs in on the OverallLevel even though all schools within a district have standardized teaching practices across all schools, In addition, the day of the week the student takes the ELPAC Assessment also factored in with Monday being the best day to see more Level 4 than Level 1. 

Our final model's results include identifiers from the features for lowincome identification, whether a student is homeless, participates in special education, and socioeconomic status, as mentioned in our problem statement. Most students in the district in our model are low-income; however, the school of attendance is where actionable insight opportunities lie. In addition, a school ID played an important role in prediction of ELPAC levels. Therefore, the school district can compare ELPAC results across grade levels and schools to determine where best practices lie to then apply those practices throughout the school district.

## Recommend Next Steps/Future Studies

Future recommendation include: 
* Pedagogical measures can be carried out to improve the school’s ELPAC passing scores by replicating the academic curriculum and attendance policy from the schools with higher classification rates. 
* Exploring the relationship of ethnicities between teachers and students to determine if there is a correlation between student’s success and having a teacher with a similar background.
* To take our model further depends on whether the model will include data for one school district or a collection of school districts. If there’s a collection of school districts, we recommend creating a feature for the school district such as District_deID. 
* Adding a feature to represent the percentage of English Learners in each school district would help the model in terms of bias as not all school districts have the same percentage of English Learners. Finally, additional analysis of results based on the growth feature may reveal that certain teachers succeed more than others in producing students who score Overall Level 4.

## Streamlit Webapp 
For end user application for prediction
 of ELPAC
 score level, the Streamlit webapp can be accessed at the following link:

<a target="_blank" rel="noopener noreferrer" href="https://oscarg-datasci-ads-599b-streamlitelpac-app-obqftk.streamlit.app/">Prediction of ELPAC Levels App<a>

## ACKNOWLEDGMENTS
We want to acknowledge the following organizations and websites for providing us the resources for the success of our project: 
California Assessment of Student Performance and Progress (CAASPP)
California Longitudinal Pupil Achievement Data System (CALPADS)
Streamlit

## References:
Brownlee, J. (2019, June 20). Classification accuracy is not enough: More performance measures you can use. Machine Learning Mastery. https://machinelearningmastery.com/classification-accuracy-is-not-enough-more-performance-measures-you-can-use/

Brownlee, J. (2021, April 26). Histogram-based gradient boosting ensembles in Python. Machine Learning Mastery. https://machinelearningmastery.com/histogram-based-gradient-boosting-ensembles/

Costa-Mendes, R., Oliveira, T., Castelli, M., & Cruz-Jesus, F. (2021). A machine learning approximation of the 2015 Portuguese high school student grades: A hybrid approach. Education and Information Technologies, 26(2), 1527–1547. https://doi.org/10.1007/s10639-020-10316-y

California Department of Education. (2022, November 30). English language proficiency assessments for California (ELPAC). https://www.cde.ca.gov/ta/tg/ep/

U.S. Department of Education. (n.d.). Every student succeeds act (ESSA). https://www.ed.gov/essa?src=rn

Kuhn, M., & Johnson, K. (2019). Applied predictive modeling. Springer.

Naicker, N., Adeliyi, T., & Wing, J. (2020). Linear support vector machines for prediction of student performance in school-based education. Mathematical Problems in Engineering, 2020, Article 4761468. https://doi.org/10.1155/2020/4761468

Rajuladevi, Aditya, "A Machine Learning Approach to Predict First-Year Student Retention Rates at University Of Nevada, Las Vegas" (2018). UNLV Theses, Dissertations, Professional Papers, and Capstones. 3315. http://dx.doi.org/10.34917/13568702

El-Keiey, S., ElMenshawy, D., & Hassanein, E. (2022). Student’s performance prediction based on personality traits and intelligence quotient using machine learning. International Journal of Advanced Computer Science and Applications (IJACSA), 13(9). http://dx.doi.org/10.14569/IJACSA.2022.0130934 

U.S. Department of Education. (2018, January 24). English learner tool kit (OELA). Retrieved November 5, 2022, from https://www2.ed.gov/about/offices/list/oela/educationandemployment.pdf

U.S. Department of Education. (2019, January 2). Non-regulatory guidance: English learners and Title III of the Elementary and Secondary Education Act (ESEA), as amended by the Every Student Succeeds Act (ESSA). https://www2.ed.gov/policy/elsec/leg/essa/essatitleiiiguidenglishlearners10219.pdf

Xu, J., Moon, K. H., & Van Der Schaar, M. (2017). A machine learning approach for tracking and predicting student performance in degree programs. IEEE Journal of Selected Topics in Signal Processing, 11(5), 742-753. https://doi.org/10.1109/JSTSP.2017.2692560
