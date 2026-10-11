# Maya runs an ice cream truck and wants to build a simple computer program to help her make decisions 
# on Saturday morning.

# She is tracking two things:
# Predicting whether today will be "Busy" or "Slow" so she knows how many helpers to hire.
# Predicting the exact number of scoops she will sell (e.g., 215 scoops, 410 scoops) so she knows how 
# much ice cream to pack.
# She also sets up a simple scoring rule to decide if a day will be "Busy":
# Every Saturday starts with a baseline score of 0 points.
# If the temperature is above 30°C: +4 points
# If there is a football match in town: +3 points
# If it is raining: -5 points
# Decision Rule:
# If the final score is 2 or higher, the program predicts "Busy". Otherwise, it predicts "Slow".

def predict_day(temperature, football_match, raining):
    score = 0

    if temperature > 30:
        score += 4

    if football_match:
        score+= 3

    if raining:
        score -=5

    if score >= 2:
        prediction = "Busy"
    else:
        prediction = "Slow"

    return prediction, score

temp = 26
football = False
rain = True

day_prediction, final_score = predict_day(temp, football, rain)

print(f"The final score: {final_score}")
print(f"The prediction will be: {day_prediction}")


# A bank uses a scoring rule to decide whether to Approve or Reject a small loan:
# Baseline Score (Bias): +10 points
# Monthly Income > ₹50,000: +15 points
# Missed a bill payment in the last year: -20 points
# Employed at the current job for over 2 years: +10 points
# Decision Rule:
# If the final score is 20 or higher, the loan is Approved. Otherwise, it is Rejected.
# Applicant Profile (Aman):
# Earns ₹65,000 per month
# Missed a credit card payment last month
# Has worked at his current company for 3 years
# What is Aman's final calculated score?
# Is his loan Approved or Rejected?

def loan_approval(monthly_income, missed_bill_payment, years_employed):
    score = 10

    if monthly_income > 50000:
        score += 15

    if missed_bill_payment:
        score -= 20

    if years_employed > 2:
        score += 10

    if score >= 20:
        decision = "Approved"
    else:
        decision = "Rejected"

    return score, decision

aman_monthly_salary = 65000
aman_missed_bill_payment = True
aman_years_employed = 3

final_score, loan_status = loan_approval(
    monthly_income=aman_monthly_salary,
    missed_bill_payment=aman_missed_bill_payment,
    years_employed=aman_years_employed
)

print(f"Final Score: {final_score}")
print(f"The loan status is: {loan_status}")


# A clinic builds a computer tool that calculates a "Sickness Score" from 0 to 10 based 
# on patient symptoms.
# Right now, the clinic uses this rule:
# Score  7: Run an emergency diagnostic test.
# Score < 7: Send the patient home to rest.
# The Problem:
# The head doctor notices that several patients with a score of 5 or 6 were sent home, but 
# their conditions worsened because an early infection was missed.
# To make the clinic safer and catch more sick patients before they leave:
# Should the doctor raise the threshold (e.g., to 8 or 9), or lower the threshold (e.g., to 4 or 5)? Why?

def evaluate_patient(sickness_score, threshold=5):

    if sickness_score > threshold:
        return "Run an emeergency diagnostic test"
    else:
        return "Send the patient home to rest"

test_patients = [5, 6, 7]

print(f"Evaluating patients within the threshold: ")
for score in test_patients:
    action = evaluate_patient(score, threshold=5)
    print(f"Patient score: {score}")
    print(f"The action for the patient is: {action}")