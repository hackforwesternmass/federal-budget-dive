"""
Simple aggregators for downloaded CSV files
This script assumes it can find CSV files like
2012_USDA_Contracts_Full_20130518.csv
where USDA is the agency, and Contracts is the spending type

You should set the prog_src_code, Agency_Id, cfda_key to values
you want.

If use_treas is True, it uses the treasury based progsrc_acnt_code to
aggregate the budgetary data by spending types

If use_treas is False, it uses the cfda_program_num to aggregate the
budgetary data by spending types
"""

import csv
import numpy
prog_src_code = '0162'
Agency_ID = 'HUD'
cfda_key = '14.862'
use_treas = False

spending_type = ('Grants', 'Contracts', 'Loans',
                 'DirectPayments', 'Insurance', 'Others')

obligated_amount = {}
for spt in spending_type:
    print "opening %s" % spt
    reader = csv.DictReader(open('2012_%s_%s_Full_20130518.csv' % (Agency_ID, spt), 'rb'))
    if spt == 'Contracts':
        ffa_amt_key = 'obligatedamount'
        prg_src_key = 'progsourceaccount'
        cfda_program_key = 'cfda_program_num'
    else:
        ffa_amt_key = 'fed_funding_amount'
        prg_src_key = 'progsrc_acnt_code'
        cfda_program_key = 'cfda_program_num'
    ffa = []
    for row in reader:
        if use_treas:
            if row[prg_src_key] == prog_src_code:
                ffa.append(float(row[ffa_amt_key]))
        else:
            try:
                if row[cfda_program_key] == cfda_key:
                    ffa.append(float(row[ffa_amt_key]))
            except:
                pass
    ffa = numpy.array(ffa)
    obligated_amount[spt] = ffa

for spt in spending_type:
    print spt, obligated_amount[spt].sum()/1e6

total = 0.0
for spt in spending_type:
    total += obligated_amount[spt].sum()/1e6

print total

