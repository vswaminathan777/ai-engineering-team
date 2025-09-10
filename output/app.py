# app.py

import gradio as gr
from tax_calculator import Tax

def process_tax(name, sin, emp_income, emp_tax_deducted, self_emp_income, rrsp, donation):
    """
    Processes all inputs from the Gradio UI and returns a tax report or an error message.
    """
    try:
        # Sanitize financial inputs by removing common formatting characters.
        emp_income_val = float(emp_income.replace(",", "").replace("$", "").replace(" ", "") or 0)
        emp_tax_deducted_val = float(emp_tax_deducted.replace(",", "").replace("$", "").replace(" ", "") or 0)
        self_emp_income_val = float(self_emp_income.replace(",", "").replace("$", "").replace(" ", "") or 0)
        rrsp_val = float(rrsp.replace(",", "").replace("$", "").replace(" ", "") or 0)
        donation_val = float(donation.replace(",", "").replace("$", "").replace(" ", "") or 0)

        # Create an instance of the tax calculator and process the data
        tax_instance = Tax()
        tax_instance.input_personal_information(name, sin)
        tax_instance.add_employment_income(emp_income_val, emp_tax_deducted_val)
        tax_instance.add_self_employment_income(self_emp_income_val)
        tax_instance.add_deduction(rrsp=rrsp_val, donation=donation_val)
        tax_instance.calculate_taxes()
        report = tax_instance.generate_tax_report()
        
        return report

    except ValueError as e:
        # Catches validation errors (e.g., bad SIN) and numeric conversion errors.
        # Displays the specific error message from the Tax class directly to the user.
        return f"Input Error: {e}"
    except Exception as e:
        # Catches any other unexpected errors.
        return f"An unexpected error occurred: {e}"

# --- Gradio Interface Definition ---
title = "Canadian Tax Calculator (2024)"
description = "Enter your personal and financial details to calculate your estimated tax. This is a simulation for a resident of Ontario."

iface = gr.Interface(
    fn=process_tax,
    inputs=[
        gr.Textbox(label="Full Name", placeholder="e.g., Jane Doe"),
        gr.Textbox(label="Social Insurance Number", placeholder="e.g., 123-456-789"),
        gr.Textbox(label="Total Employment Income", value="0"),
        gr.Textbox(label="Income Tax Deducted at Source", value="0"),
        gr.Textbox(label="Total Self-Employment Income", value="0"),
        gr.Textbox(label="RRSP Contributions", value="0"),
        gr.Textbox(label="Charitable Donations", value="0")
    ],
    outputs=gr.Textbox(label="Tax Summary Report", interactive=False, lines=15),
    title=title,
    description=description,
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch()