# Given the name of a US state or territory, return its postal abbreviation. All states,
# federal districts and inhabited territories will be tested, according to the linked wikipedia page.
#
# Notes:
#
# to spark your creativity, the size of your code is limited to 500 characters
# the list of states and their respective abbreviations are listed below
# import, exec, eval and "__" are forbidden
# Examples
# "Alabama"               -->  "AL"
# "District of Columbia"  -->  "DC"
# "U.S. Virgin Islands"   -->  "VI"
# List of states and abbreviations
# Alabama, AL
# Alaska, AK
# Arizona, AZ
# Arkansas, AR
# California, CA
# Colorado, CO
# Connecticut, CT
# Delaware, DE
# Florida, FL
# Georgia, GA
# Hawaii, HI
# Idaho, ID
# Illinois, IL
# Indiana, IN
# Iowa, IA
# Kansas, KS
# Kentucky, KY
# Louisiana, LA
# Maine, ME
# Maryland, MD
# Massachusetts, MA
# Michigan, MI
# Minnesota, MN
# Mississippi, MS
# Missouri, MO
# Montana, MT
# Nebraska, NE
# Nevada, NV
# New Hampshire, NH
# New Jersey, NJ
# New Mexico, NM
# New York, NY
# North Carolina, NC
# North Dakota, ND
# Ohio, OH
# Oklahoma, OK
# Oregon, OR
# Pennsylvania, PA
# Rhode Island, RI
# South Carolina, SC
# South Dakota, SD
# Tennessee, TN
# Texas, TX
# Utah, UT
# Vermont, VT
# Virginia, VA
# Washington, WA
# West Virginia, WV
# Wisconsin, WI
# Wyoming, WY
# District of Columbia, DC
# American Samoa, AS
# Guam, GU
# Northern Mariana Islands, MP
# Puerto Rico, PR
# U.S. Virgin Islands, VI
# My other katas
# If you enjoyed this kata then please try my other katas! :-)
#
# Translations are welcome!

STATES = "Ama Aka Ana Aas Cia Cdo Cut Dre Fda Gia Hii Iho Iis Ina Iwa Kas Kky Lna Mne Mnd Mts Man Mta Mpi Mri Mna Nka Nda Nre Ney Nco Nrk Nna Nta Oio Oma Oon Pia Rnd Sna Sta Tee Tas Uah Vnt Via Won Wia Win Wng Dia Aoa Gam Nds Pco Uds".split()
CODES  = "AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC AS GU MP PR VI".split()

def abbr(s):
    return CODES[STATES.index(s[0] + s[-2:])]