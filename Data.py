
def ApplicantIncomeStandard(x):
    ApplicantIncomeMean = 5403.459283387622
    ApplicantIncomeStd = 6109.041673387178
    y = (x - ApplicantIncomeMean) / ApplicantIncomeStd
    return y

def CoapplicantIncomeStandard(x):
    CoapplicantIncomeMean = 1621.2457980271008 
    CoapplicantIncomeStd = 2926.2483692241885
    y = (x - CoapplicantIncomeMean) / CoapplicantIncomeStd
    return y

def LoanAmountStandard(x):
    LoanAmountMean = 145.75244299674267 
    LoanAmountStd = 84.10723338042614
    y = (x - LoanAmountMean)/ LoanAmountStd
    return y

def Loan_Amount_TermStandard(x):
    Loan_Amount_TermMean = 342.4104234527687 
    Loan_Amount_TermStd = 64.42862906767307
    y = (x - Loan_Amount_TermMean) / Loan_Amount_TermStd
    return y
