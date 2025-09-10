#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from ai_engineering_team.crew import AIEngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
The system should allow users to enter their personal information and financial details for a tax year.
The system should allow a user to input their personal information (e.g., name, Social Insurance Number).
The system should allow a user to add various sources of income, specifically employment income (from a T4 slip, including income tax deducted) and self-employment income.
The system should allow a user to enter common deductions, such as RRSP (Registered Retirement Savings Plan) contributions and charitable donations.
The system should perform all necessary calculations to determine the final tax outcome.
The system must calculate the user's total income, net income, and taxable income.
The system must calculate the federal tax and provincial (Ontario) tax payable by applying the provided progressive tax brackets to the taxable income.
The system must calculate the final tax refund or balance owing by comparing the total tax payable to the income tax already deducted.
The system should be able to report the user's tax summary.
The system should be able to generate a clear tax summary report showing the breakdown of income, deductions, credits, taxes payable, and the final refund or balance owing.
The system should be able to list all individual income and deduction entries the user has made.
The system should include basic validation.
The system should prevent the user from entering non-numeric values for financial amounts.
The system should ensure that required information, such as a Social Insurance Number, is entered before performing a final calculation.
The system has access to pre-defined data structures or functions that provide the 2024 tax brackets. Include a test implementation with the following federal and Ontario tax brackets:
Federal Tax Brackets (2024)
15% on the first $55,867
20.5% on the portion of income over $55,867 up to $111,733
26% on the portion of income over $111,733 up to $173,205
29% on the portion of income over $173,205
Ontario Provincial Tax Brackets (2024)
5.05% on the first $51,446
9.15% on the portion of income over $51,446 up to $102,894
11.16% on the portion of income over $102,894 up to $150,000
12.16% on the portion of income over $150,000
"""
module_name = "tax_calculator.py"
class_name = "tax"


def run():
    """
    Run the research crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = AIEngineeringTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()