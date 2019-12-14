#! /usr/bin/env bash

# GIVEN

# SB001 has both fear and happy
mkdir -p SB001/T4/model/tgng
echo "1.234" > SB001/T4/model/tgng/happy_lev1_mod1.feat
echo "0.138" > SB001/T4/model/tgng/fear_lev1_mod1.feat

# SB002 has only fear
mkdir -p SB002/T4/model/tgng
echo "0.789" > SB002/T4/model/tgng/fear_lev1_mod1.feat

# SB003 has only happy
mkdir -p SB003/T4/model/tgng
echo "0.456" > SB003/T4/model/tgng/happy_lev1_mod1.feat

# SB004 has neither
mkdir -p SB004/T4/model/tgng

# expected
echo -e "ID,Happy,Fear\nSB001,1.234,0.138\nSB002,N/A,0.789\nSB003,0.456,N/A\nSB004,N/A,N/A" > expected.csv

# WHEN
python main.py > actual.csv

# THEN
diff -w actual.csv expected.csv
