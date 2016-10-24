import unittest

from etl import extract_xls_html as etl
from fixtures import TEST_CONTRIBUTIONS_LIST, TEST_BUSINESS_LICENSE_LIST


class TestExtractHtmlData(unittest.TestCase):

    def test_extracts_headers(self):

        data = etl.extract_data_from_html(TEST_CONTRIBUTIONS_LIST)

        self.assertEqual(
            data.headers,
            ['Contribution Date',
             'Contributor Name',
             'Contributor Address']
        )

    def test_extracts_data_to_py_objs(self):

        data = etl.extract_data_from_html(TEST_CONTRIBUTIONS_LIST)

        self.assertEqual(
            list(data),
            [
                {
                    'Contribution Date': '2/2/2004',
                    'Contributor Name': 'Inc, Caldera   Management',
                    'Contributor Address': '4260 Hwy 1, Rehoboth, DE 19971'
                },
                {
                    'Contribution Date': '9/22/2004',
                    'Contributor Name': 'Conset-vancy/LLC, Rehoboth   Bay',
                    'Contributor Address': '1207 Delaware AveWilinin too/DE 19806, DE',

                },
                {
                    'Contribution Date': '9/17/2004',
                    'Contributor Name': 'lingua, James.A',
                    'Contributor Address': '28 The Circle.Georgetown/DE 19947, DE',

                }
            ]
        )

    def test_extracts_business_list_headers(self):
        headers = [
            'Business name',
            'Trade name',
            'Category',
            'From',
            'To',
         ]

        data = etl.extract_data_from_html(
            TEST_BUSINESS_LICENSE_LIST, headers=headers)

        self.assertEqual(data.headers, headers)

    def test_extracts_business_list_data_to_py_objs(self):

        headers = [
            'Business name',
            'Trade name',
            'Category',
            'Current License Valid From',
            'Current License Valid To',
            'Address 1',
            'Address 2',
            'City',
            'State',
            'Zip',
            'Country',
            'License number'
        ]

        expected = [
            {
                'Business name': u'000 CHOICE MANAGEMENT INC',
                'Trade name': u' ',
                'Category': u'PROFESSIONAL AND/OR PRSL SRVCS-UNCLASSIFIED',
                'Current License Valid From': u'1/1/05',
                'Current License Valid To': u'12/31/07',
                'Address 1': u' ',
                'Address 2': u'7904 COASTAL HWY #5',
                'City': u'OCEAN CITY',
                'State': u'MD',
                'Zip': u'21842-6707',
                'Country': u' ',
                'License number': u'1999202399',
            },
        ]

        data = etl.extract_data_from_html(
            TEST_BUSINESS_LICENSE_LIST, headers=headers, skip_rows=2)

        self.maxDiff = None
        for got, expect in zip(list(data), expected):
            self.assertEqual(got, expect)


if __name__ == '__main__':
    unittest.main()
