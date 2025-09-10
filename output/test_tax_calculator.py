import unittest
from tax_calculator import Tax

class TestTax(unittest.TestCase):

    def test_input_personal_information(self):
        tax = Tax()
        tax.input_personal_information('Jane Doe', '123-456-789')
        self.assertEqual(tax.name, 'Jane Doe')
        self.assertEqual(tax.sin, '123-456-789')

    def test_input_personal_information_invalid_sin(self):
        tax = Tax()
        with self.assertRaises(ValueError):
            tax.input_personal_information('Jane Doe', '123456789')

    def test_add_employment_income(self):
        tax = Tax()
        tax.add_employment_income(100000, 15000)
        self.assertEqual(tax.employment_income, 100000)
        self.assertEqual(tax.employment_tax_deducted, 15000)

    def test_add_self_employment_income(self):
        tax = Tax()
        tax.add_self_employment_income(50000)
        self.assertEqual(tax.self_employment_income, 50000)

    def test_add_deduction(self):
        tax = Tax()
        tax.add_deduction(rrsp=5000, donation=2000)
        self.assertEqual(tax.rrsp_deduction, 5000)
        self.assertEqual(tax.donation_deduction, 2000)

    def test_calculate_taxes(self):
        tax = Tax()
        tax.input_personal_information('John Smith', '234-567-890')
        tax.add_employment_income(60000, 10000)
        tax.add_self_employment_income(30000)
        tax.add_deduction(rrsp=0, donation=0)
        tax.calculate_taxes()
        self.assertAlmostEqual(tax.federal_tax, 12382.2, places=1)
        self.assertAlmostEqual(tax.provincial_tax, 6234.35, places=1)
        self.assertAlmostEqual(tax.final_refund_or_owing, 21416.85, places=1)

    def test_get_tax_summary(self):
        tax = Tax()
        tax.input_personal_information('Alice Johnson', '345-678-901')
        tax.add_employment_income(70000, 20000)
        tax.add_self_employment_income(20000)
        tax.add_deduction(rrsp=5000, donation=1000)
        tax.calculate_taxes()
        summary = tax.get_tax_summary()
        self.assertEqual(summary['name'], 'Alice Johnson')
        self.assertAlmostEqual(summary['total_income'], 90000, places=1)
        self.assertAlmostEqual(summary['net_income'], 84000, places=1)

if __name__ == '__main__':
    unittest.main()