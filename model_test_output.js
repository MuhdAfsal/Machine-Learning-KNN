
✅ Dataset loaded — 159,541 rows × 89 columns
=== Dataset Info ===
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 159541 entries, 0 to 159540
Data columns (total 89 columns):
 #   Column               Non-Null Count   Dtype 
---  ------               --------------   ----- 
 0   UID                  159541 non-null  int64 
 1   Name                 159541 non-null  object
 2   NationID             159541 non-null  int64 
 3   Born                 159541 non-null  object
 4   Age                  159541 non-null  int64 
 5   IntCaps              159541 non-null  int64 
 6   IntGoals             159541 non-null  int64 
 7   U21Caps              159541 non-null  int64 
 8   U21Goals             159541 non-null  int64 
 9   Height               159541 non-null  int64 
 10  Weight               159541 non-null  int64 
 11  AerialAbility        159541 non-null  int64 
 12  CommandOfArea        159541 non-null  int64 
 13  Communication        159541 non-null  int64 
 14  Eccentricity         159541 non-null  int64 
 15  Handling             159541 non-null  int64 
 16  Kicking              159541 non-null  int64 
 17  OneOnOnes            159541 non-null  int64 
 18  Reflexes             159541 non-null  int64 
 19  RushingOut           159541 non-null  int64 
 20  TendencyToPunch      159541 non-null  int64 
 21  Throwing             159541 non-null  int64 
 22  Corners              159541 non-null  int64 
 23  Crossing             159541 non-null  int64 
 24  Dribbling            159541 non-null  int64 
 25  Finishing            159541 non-null  int64 
 26  FirstTouch           159541 non-null  int64 
 27  Freekicks            159541 non-null  int64 
 28  Heading              159541 non-null  int64 
 29  LongShots            159541 non-null  int64 
 30  Longthrows           159541 non-null  int64 
 31  Marking              159541 non-null  int64 
 32  Passing              159541 non-null  int64 
 33  PenaltyTaking        159541 non-null  int64 
 34  Tackling             159541 non-null  int64 
 35  Technique            159541 non-null  int64 
 36  Aggression           159541 non-null  int64 
 37  Anticipation         159541 non-null  int64 
 38  Bravery              159541 non-null  int64 
 39  Composure            159541 non-null  int64 
 40  Concentration        159541 non-null  int64 
 41  Vision               159541 non-null  int64 
 42  Decisions            159541 non-null  int64 
 43  Determination        159541 non-null  int64 
 44  Flair                159541 non-null  int64 
 45  Leadership           159541 non-null  int64 
 46  OffTheBall           159541 non-null  int64 
 47  Positioning          159541 non-null  int64 
 48  Teamwork             159541 non-null  int64 
 49  Workrate             159541 non-null  int64 
 50  Acceleration         159541 non-null  int64 
 51  Agility              159541 non-null  int64 
 52  Balance              159541 non-null  int64 
 53  Jumping              159541 non-null  int64 
 54  LeftFoot             159541 non-null  int64 
 55  NaturalFitness       159541 non-null  int64 
 56  Pace                 159541 non-null  int64 
 57  RightFoot            159541 non-null  int64 
 58  Stamina              159541 non-null  int64 
 59  Strength             159541 non-null  int64 
 60  Consistency          159541 non-null  int64 
 61  Dirtiness            159541 non-null  int64 
 62  ImportantMatches     159541 non-null  int64 
 63  InjuryProness        159541 non-null  int64 
 64  Versatility          159541 non-null  int64 
 65  Adaptability         159541 non-null  int64 
 66  Ambition             159541 non-null  int64 
 67  Loyalty              159541 non-null  int64 
 68  Pressure             159541 non-null  int64 
 69  Professional         159541 non-null  int64 
 70  Sportsmanship        159541 non-null  int64 
 71  Temperament          159541 non-null  int64 
 72  Controversy          159541 non-null  int64 
 73  PositionsDesc        159509 non-null  object
 74  Goalkeeper           159541 non-null  int64 
 75  Sweeper              159541 non-null  int64 
 76  Striker              159541 non-null  int64 
 77  AttackingMidCentral  159541 non-null  int64 
 78  AttackingMidLeft     159541 non-null  int64 
 79  AttackingMidRight    159541 non-null  int64 
 80  DefenderCentral      159541 non-null  int64 
 81  DefenderLeft         159541 non-null  int64 
 82  DefenderRight        159541 non-null  int64 
 83  DefensiveMidfielder  159541 non-null  int64 
 84  MidfielderCentral    159541 non-null  int64 
 85  MidfielderLeft       159541 non-null  int64 
 86  MidfielderRight      159541 non-null  int64 
 87  WingBackLeft         159541 non-null  int64 
 88  WingBackRight        159541 non-null  int64 
dtypes: int64(86), object(3)
memory usage: 108.3+ MB
None

=== Null Values ===
PositionsDesc    32
dtype: int64

=== Basic Stats (numeric) ===
                UID      NationID            Age        IntCaps  \
count  1.595410e+05  1.595410e+05  159541.000000  159541.000000   
mean   1.368157e+08  7.621294e+04      23.578033       0.988987   
std    3.492948e+08  2.051496e+06       5.640172       6.642102   
min    5.100000e+02  5.000000e+00      14.000000       0.000000   
25%    1.902265e+07  7.610000e+02      19.000000       0.000000   
50%    4.104476e+07  7.760000e+02      23.000000       0.000000   
75%    6.723302e+07  7.990000e+02      27.000000       0.000000   
max    1.394674e+09  6.200213e+07      54.000000     166.000000   

            IntGoals        U21Caps       U21Goals         Height  \
count  159541.000000  159541.000000  159541.000000  159541.000000   
mean        0.108148       0.507424       0.065883     180.025097   
std         1.269210       2.535295       0.591362       7.218558   
min         0.000000       0.000000       0.000000     149.000000   
25%         0.000000       0.000000       0.000000     175.000000   
50%         0.000000       0.000000       0.000000     180.000000   
75%         0.000000       0.000000       0.000000     185.000000   
max        65.000000      62.000000      37.000000     210.000000   

              Weight  AerialAbility  ...  AttackingMidRight  DefenderCentral  \
count  159541.000000  159541.000000  ...      159541.000000    159541.000000   
mean       45.874922       2.991613  ...           4.156649         5.233984   
std        36.340693       2.901983  ...           6.225964         7.552120   
min         0.000000       1.000000  ...           1.000000         1.000000   
25%         0.000000       1.000000  ...           1.000000         1.000000   
50%        68.000000       2.000000  ...           1.000000         1.000000   
75%        75.000000       3.000000  ...           1.000000         4.000000   
max       118.000000      20.000000  ...          20.000000        20.000000   

        DefenderLeft  DefenderRight  DefensiveMidfielder  MidfielderCentral  \
count  159541.000000  159541.000000        159541.000000      159541.000000   
mean        3.443848       3.665854             4.031534           5.729750   
std         5.806511       6.027779             6.273162           7.436234   
min         1.000000       1.000000             1.000000           1.000000   
25%         1.000000       1.000000             1.000000           1.000000   
50%         1.000000       1.000000             1.000000           1.000000   
75%         1.000000       1.000000             1.000000          12.000000   
max        20.000000      20.000000            20.000000          20.000000   

       MidfielderLeft  MidfielderRight   WingBackLeft  WingBackRight  
count   159541.000000    159541.000000  159541.000000  159541.000000  
mean         3.588626         3.726798       2.332165       2.345993  
std          5.536178         5.673648       4.055871       4.056001  
min          1.000000         1.000000       1.000000       1.000000  
25%          1.000000         1.000000       1.000000       1.000000  
50%          1.000000         1.000000       1.000000       1.000000  
75%          1.000000         1.000000       1.000000       1.000000  
max         20.000000        20.000000      20.000000      20.000000  

[8 rows x 86 columns]
Position distribution:
PrimaryPosition
DefenderCentral        27218
Striker                26616
MidfielderCentral      18217
Goalkeeper             17130
AttackingMidCentral    11668
DefensiveMidfielder    11357
DefenderRight          11145
DefenderLeft           10535
AttackingMidRight       8010
AttackingMidLeft        7584
MidfielderRight         4474
MidfielderLeft          4246
WingBackLeft             661
WingBackRight            426
Sweeper                  254
Name: count, dtype: int64

Broad role distribution:
Role
Defender         49152
Midfielder       38294
Attacking Mid    27262
Striker          26616
Goalkeeper       17130
Wing Back         1087
Name: count, dtype: int64
Using 69 features: ['Age', 'IntCaps', 'IntGoals', 'U21Caps', 'U21Goals', 'Height', 'Weight', 'AerialAbility', 'CommandOfArea', 'Communication', 'Eccentricity', 'Handling', 'Kicking', 'OneOnOnes', 'Reflexes', 'RushingOut', 'TendencyToPunch', 'Throwing', 'Corners', 'Crossing', 'Dribbling', 'Finishing', 'FirstTouch', 'Freekicks', 'Heading', 'LongShots', 'Longthrows', 'Marking', 'Passing', 'PenaltyTaking', 'Tackling', 'Technique', 'Aggression', 'Anticipation', 'Bravery', 'Composure', 'Concentration', 'Vision', 'Decisions', 'Determination', 'Flair', 'Leadership', 'OffTheBall', 'Positioning', 'Teamwork', 'Workrate', 'Acceleration', 'Agility', 'Balance', 'Jumping', 'LeftFoot', 'NaturalFitness', 'Pace', 'RightFoot', 'Stamina', 'Strength', 'Consistency', 'Dirtiness', 'ImportantMatches', 'InjuryProness', 'Versatility', 'Adaptability', 'Ambition', 'Loyalty', 'Pressure', 'Professional', 'Sportsmanship', 'Temperament', 'Controversy']

Feature matrix shape : (159541, 69)
Target shape         : (159541,)
Classes              : ['Attacking Mid', 'Defender', 'Goalkeeper', 'Midfielder', 'Striker', 'Wing Back']
Training samples : 127,632
Test samples     : 31,909
✅ KNN model trained!
  k= 1 → CV Accuracy: 0.7441 ± 0.0025
  k= 3 → CV Accuracy: 0.7767 ± 0.0015
  k= 5 → CV Accuracy: 0.7940 ± 0.0013
  k= 7 → CV Accuracy: 0.8035 ± 0.0013
  k= 9 → CV Accuracy: 0.8098 ± 0.0014
  k=11 → CV Accuracy: 0.8131 ± 0.0014
  k=13 → CV Accuracy: 0.8161 ± 0.0015
  k=15 → CV Accuracy: 0.8179 ± 0.0020
  k=17 → CV Accuracy: 0.8194 ± 0.0018
  k=19 → CV Accuracy: 0.8205 ± 0.0020
  k=21 → CV Accuracy: 0.8213 ± 0.0021
  k=23 → CV Accuracy: 0.8220 ± 0.0015
  k=25 → CV Accuracy: 0.8228 ± 0.0013

🏆 Best k = 25 (CV Accuracy = 0.8228)
📊 Elbow curve saved as elbow_curve.png
✅ Model retrained with k=25
Test Accuracy : 0.8263

=== Classification Report ===
               precision    recall  f1-score   support

Attacking Mid       0.65      0.73      0.69      5453
     Defender       0.88      0.93      0.91      9831
   Goalkeeper       1.00      1.00      1.00      3426
   Midfielder       0.76      0.69      0.72      7659
      Striker       0.90      0.85      0.87      5323
    Wing Back       0.00      0.00      0.00       217

     accuracy                           0.83     31909
    macro avg       0.70      0.70      0.70     31909
 weighted avg       0.82      0.83      0.82     31909

📊 Confusion matrix saved as confusion_matrix.png
✅ Model saved to knn_football_position.pkl
=== Sample Predictions ===
  Actual Role Predicted Role Confidence (%)
Attacking Mid     Midfielder           68.0
   Midfielder       Defender           64.1
   Midfielder       Defender           55.9
   Midfielder       Defender           59.5
     Defender       Defender           64.0

🔍 Custom player predicted role : Striker  (confidence: 100.0%)

✅ All done! Your KNN model is trained, evaluated, and ready to use.
