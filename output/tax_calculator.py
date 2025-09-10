class Tax:
    def __init__(self):
        self.name = None
        self.sin = None
        self.employment_income = 0.0
        self.employment_tax_deducted = 0.0
        self.self_employment_income = 0.0
        self.rrsp_deduction = 0.0
        self.donation_deduction = 0.0
        self.total_income = 0.0
        self.net_income = 0.0
        self.taxable_income = 0.0
        self.federal_tax = 0.0
        self.provincial_tax = 0.0
        self.total_tax_payable = 0.0
        self.final_refund_or_owing = 0.0

    def input_personal_information(self, name: str, sin: str) -> None:
        self._validate_sin(sin)
        self.name = name
        self.sin = sin

    def add_employment_income(self, income: float, tax_deducted: float) -> None:
        self._validate_financial_entry(income)
        self._validate_financial_entry(tax_deducted)
        self.employment_income += income
        self.employment_tax_deducted += tax_deducted

    def add_self_employment_income(self, income: float) -> None:
        self._validate_financial_entry(income)
        self.self_employment_income += income

    def add_deduction(self, rrsp: float = 0, donation: float = 0) -> None:
        if rrsp:
            self._validate_financial_entry(rrsp)
            self.rrsp_deduction += rrsp
        if donation:
            self._validate_financial_entry(donation)
            self.donation_deduction += donation

    def calculate_taxes(self) -> None:
        self.total_income = self.employment_income + self.self_employment_income
        self.net_income = self.total_income - (self.rrsp_deduction + self.donation_deduction)
        self.taxable_income = max(0, self.net_income)

        self.federal_tax = self._calculate_federal_tax(self.taxable_income)
        self.provincial_tax = self._calculate_provincial_tax(self.taxable_income)

        self.total_tax_payable = self.federal_tax + self.provincial_tax
        self.final_refund_or_owing = self.employment_tax_deducted - self.total_tax_payable

    def _calculate_federal_tax(self, taxable_income: float) -> float:
        brackets = [55867, 111733, 173205]
        rates = [0.15, 0.205, 0.26, 0.29]
        
        tax = 0.0
        if taxable_income <= brackets[0]:
            tax = taxable_income * rates[0]
        elif taxable_income <= brackets[1]:
            tax = (brackets[0] * rates[0]) + ((taxable_income - brackets[0]) * rates[1])
        elif taxable_income <= brackets[2]:
            tax = ((brackets[0] * rates[0]) + ((brackets[1] - brackets[0]) * rates[1]) + 
                   ((taxable_income - brackets[1]) * rates[2]))
        else:
            tax = ((brackets[0] * rates[0]) + ((brackets[1] - brackets[0]) * rates[1]) + 
                   ((brackets[2] - brackets[1]) * rates[2]) + ((taxable_income - brackets[2]) * rates[3]))
        return tax

    def _calculate_provincial_tax(self, taxable_income: float) -> float:
        brackets = [51446, 102894, 150000]
        rates = [0.0505, 0.0915, 0.1116, 0.1216]
        
        tax = 0.0
        if taxable_income <= brackets[0]:
            tax = taxable_income * rates[0]
        elif taxable_income <= brackets[1]:
            tax = (brackets[0] * rates[0]) + ((taxable_income - brackets[0]) * rates[1])
        elif taxable_income <= brackets[2]:
            tax = ((brackets[0] * rates[0]) + ((brackets[1] - brackets[0]) * rates[1]) + 
                   ((taxable_income - brackets[1]) * rates[2]))
        else:
            tax = ((brackets[0] * rates[0]) + ((brackets[1] - brackets[0]) * rates[1]) + 
                   ((brackets[2] - brackets[1]) * rates[2]) + ((taxable_income - brackets[2]) * rates[3]))
        return tax

    def get_tax_summary(self) -> dict:
        return {
            "name": self.name,
            "total_income": self.total_income,
            "net_income": self.net_income,
            "taxable_income": self.taxable_income,
            "federal_tax": self.federal_tax,
            "provincial_tax": self.provincial_tax,
            "total_tax_payable": self.total_tax_payable,
            "final_refund_or_owing": self.final_refund_or_owing
        }

    def list_income_entries(self) -> list:
        return [
            {"employment_income": self.employment_income, "tax_deducted": self.employment_tax_deducted},
            {"self_employment_income": self.self_employment_income}
        ]

    def list_deduction_entries(self) -> list:
        return [
            {"rrsp_deduction": self.rrsp_deduction},
            {"donation_deduction": self.donation_deduction}
        ]

    def generate_tax_report(self) -> str:
        return f"""
        Tax Summary Report for {self.name}
        -----------------------------------
        Total Income: ${self.total_income:.2f}
        Net Income: ${self.net_income:.2f}
        Taxable Income: ${self.taxable_income:.2f}
        Federal Tax: ${self.federal_tax:.2f}
        Provincial Tax: ${self.provincial_tax:.2f}
        Total Tax Payable: ${self.total_tax_payable:.2f}
        Final Refund or Balance Owing: ${self.final_refund_or_owing:.2f}
        """

    def _validate_financial_entry(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"Invalid financial entry: {value}. Must be a non-negative number.")

    def _validate_sin(self, sin: str) -> None:
        if len(sin) != 11 or not all(part.isdigit() for part in sin.split('-')):
            raise ValueError(f"Invalid SIN: {sin}. Format should be 'XXX-XXX-XXX'.")

# Example usage
if __name__ == "__main__":
    tax_instance = Tax()
    tax_instance.input_personal_information("John Doe", "123-456-789")
    tax_instance.add_employment_income(55000, 5000)
    tax_instance.add_self_employment_income(20000)
    tax_instance.add_deduction(rrsp=2000, donation=500)
    tax_instance.calculate_taxes()
    print(tax_instance.get_tax_summary())
    print(tax_instance.generate_tax_report())