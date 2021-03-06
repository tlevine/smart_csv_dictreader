import os
import nose.tools as n
n.assert_dict_equal.__self__.maxDiff = None

from smart_csv_dictreader import DictReader

def test_dictreader():
    expected_header = [
        'code_insee', 'code_postal', 'commune', 'wgs84', 'federation', 'licences_en_2011',
        'moins_de_20_ans', 'entre_20_et_60_ans', 'plus_de_60_ans',
        'femmes', 'femmes_moins_de_20_ans', 'femmes_de_20_a_60_ans', 'femmes_plus_de_60_ans',
        'licences_en_zone_urbaine_sensible_zus', 'population_totale_2010', 'population_femme',
        'population_femmes_de_moins_de_20_ans', 'population_femme_de_20_a_60_ans', 'population_femme_de_plus_de_60_ans',
        'population_de_moins_de_20_ans', 'population_de_20_a_60_ans', 'population_de_plus_de_60_ans'
    ]
    expected_firstrow_values = [
        '92050', '92000', 'NANTERRE', '48.8924273, 2.2071267', 'FF de badminton', '166', '54', '112',
        '', '58', '18', '40', '', '30', '89185', '44739', '12377', '25998', '6365', '25125', '51879', '12182',
    ]

    with open(os.path.join('smart_csv_dictreader','test','fixtures','carte-des-licencies-sportifs-dans-les-hauts-de-seine.csv')) as fp:
        reader = DictReader(fp, delimiter = ';')
        firstrow = next(reader)
    n.assert_dict_equal(firstrow, dict(zip(expected_header, expected_firstrow_values)))
