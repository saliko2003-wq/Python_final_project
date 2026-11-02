# Min-Max normalization function
def normalize(value, min_value, max_value):
    normalized = (value - min_value) / (max_value - min_value)
    return normalized * 100
    
# cvs function
def calculate_cvs(pf_normalized, ss_normalized, lpa_normalized):
    cvs = (pf_normalized+ss_normalized+lpa_normalized) / 3
    return cvs

# Assigning a customer segment based on their CVS:
q1 = 38.43124108896529
q3 = 62.59451489843179

def assign_segment(cvs, q1=q1, q3=q3):
    if cvs <= q1:
        return "Low CVS"
    elif cvs <= q3:
        return "Medium CVS"
    else:
        return "High CVS"

#Loyalty function
def calculate_loyalty(pf_normalized, my_normalized):
    ls = (pf_normalized+my_normalized) / 2
    return ls

# Assigning a customer segment based on their loyalty score:
l1 = 35.005669
l3 = 66.638322

def assign_segment_loyalty(ls, l1=l1, l3=l3):
    if ls <= l1:
        return "Low loyalty"
    elif ls <= l3:
        return "Medium loyalty"
    else:
        return "High loyalty"