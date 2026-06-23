def generate_case_summary(case):

    summary = f"""
Complaint ID: {case['id']}

Victim: {case['name']}

Category: {case['category']}

Risk Score: {case['risk_score']}

Priority: {case['priority']}

Status: {case['status']}

Assigned Officer: {case['officer_name']}

Investigation Notes:
{case['investigation_notes']}

AI Assessment:
This complaint appears to be related to {case['category']}.
The reported risk score is {case['risk_score']}.

Recommended Action:
Review evidence, verify victim claims,
and continue investigation according
to cybercrime procedures.
"""

    return summary