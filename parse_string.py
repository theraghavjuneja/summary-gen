input_string = "1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 332, 333, 334, 335, 336, 337, 449, 450, 451, 452, 453, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 624, 625, 626, 627, 628, 629, 643, 644, 645, 646, 647, 648, 649, 665, 666, 667, 668, 669, 670, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 836, 837, 838, 839, 840, 846, 847, 848, 849, 850, 927, 928, 929, 930, 931, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1022, 1023, 1024, 1025, 1026, 1246, 1247, 1248, 1249, 1250, 1261, 1262, 1263, 1264, 1265"
numbers = list(map(int, input_string.split(', ')))
dataset = [
    [1, "AICTE", "SIH1458", "Software", 40481, 50869, "DYNAMIC DUDES@", "BHAVYA GROVER", 145546, "MODERN INSTITUTE OF TECHNOLOGY & RESEARCH CENTRE,ALWAR,RAJASTHAN,ALWAR", "SELECTED", "O P Jindal University, Raigarh,Chhattisgarh,Raigarh", "AI Based - Designing of Assistive portal for Stakeholders in Approval Process", "Miscellaneous"],
    [2, "AICTE", "SIH1458", "Software", 27179, 50141, "Swasthya Sahayak", "PRAVEEN KUSHWAHA", 158737, "AJAY KUMAR GARG ENGINEERING COLLEGE, GHAZIABAD,UTTAR PRADESH,GHAZIABAD", "SELECTED", "O P Jindal University, Raigarh,Chhattisgarh,Raigarh", "AI Based - Designing of Assistive portal for Stakeholders in Approval Process", "Miscellaneous"],
    [3, "AICTE", "SIH1458", "Software", 28982, 48836, "FusionX!", "SANKALP SRIVASTAVA", 103531, "GALGOTIAS UNIVERSITY,UTTAR PRADESH,GAUTAM BUDDHA NAGAR", "SELECTED", "O P Jindal University, Raigarh,Chhattisgarh,Raigarh", "AI Based - Designing of Assistive portal for Stakeholders in Approval Process", "Miscellaneous"],
    [4, "AICTE", "SIH1458", "Software", 3934, 39712, "Binks' Crew", "SOHAM SAWANT", 102748, "INDIAN INSTITUTE OF INFORMATION TECHNOLOGY, VADODARA,GUJARAT,VADODARA", "SELECTED", "O P Jindal University, Raigarh,Chhattisgarh,Raigarh", "AI Based - Designing of Assistive portal for Stakeholders in Approval Process", "Miscellaneous"],
    [5, "AICTE", "SIH1458", "Software", 3103, 47678, "Elk Cloners", "HITHENDRA B M", 131047, "VIDYA VARDHAKA COLLEGE OF ENGINEERING, MYSORE,KARNATAKA,MYSURU", "SELECTED", "O P Jindal University, Raigarh,Chhattisgarh,Raigarh", "AI Based - Designing of Assistive portal for Stakeholders in Approval Process", "Miscellaneous"]
]
for entry in dataset:
    if entry[0] in numbers:
        team_name = entry[6]
        team_leader = entry[7]
        college_name = entry[9]
        problem_statement_title = entry[12]
        domain_bucket = entry[13]
        print(f"Team name is {team_name}, whereas team leader is {team_leader}, They belong to college {college_name} and they have worked on problem statement {problem_statement_title} which falls in domain {domain_bucket}.")
