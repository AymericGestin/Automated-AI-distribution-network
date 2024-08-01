(define (problem disnet68n) (:domain disnet)
(:objects
	P69 P70 - Primary
	S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 S15 S16 S17 S18 S19 S20 S21 S22 S23 S24 S25 S26 S27 S28 S29 S30 S31 S32 S33 S34 S35 S36 S37 S38 S39 S40 S41 S42 S43 S44 S45 S46 S47 S48 S49 S50 S51 S52 S53 S54 S55 S56 S57 S58 S59 S60 S61 S62 S63 S64 S65 S66 S67 S68 - Secondary
	)
(:init
	(is-primary P69)
	(is-primary P70)
	(connected P70 S1)(connected S1 P70)
	(feed S1 P70)
	(closed P70 S1)(closed S1 P70)
	(connected S1 S2) (connected S2 S1)
	(feed S2 S1)
	(closed S1 S2) (closed S2 S1)
	(connected S2 S3) (connected S3 S2)
	(feed S3 S2)
	(closed S2 S3) (closed S3 S2)
	(connected S3 S4) (connected S4 S3)
	(feed S4 S3)
	(closed S3 S4) (closed S4 S3)
	(connected S4 S5) (connected S5 S4)
	(feed S5 S4)
	(closed S4 S5) (closed S5 S4)
	(connected S5 S6) (connected S6 S5)
	(feed S6 S5)
	(closed S5 S6) (closed S6 S5)
	(connected S6 S7) (connected S7 S6)
	(feed S7 S6)
	(closed S6 S7) (closed S7 S6)
	(connected S7 S8) (connected S8 S7)
	(feed S8 S7)
	(closed S7 S8) (closed S8 S7)
	(connected S3 S9) (connected S9 S3)
	(feed S9 S3)
	(closed S3 S9) (closed S9 S3)
	(connected S9 S10) (connected S10 S9)
	(feed S10 S9)
	(closed S9 S10) (closed S10 S9)
	(connected S10 S11) (connected S11 S10)
	(feed S11 S10)
	(closed S10 S11) (closed S11 S10)
	(connected S11 S12) (connected S12 S11)
	(feed S12 S11)
	(closed S11 S12) (closed S12 S11)
	(connected S12 S13) (connected S13 S12)
	(feed S13 S12)
	(closed S12 S13) (closed S13 S12)
	(connected S13 S14) (connected S14 S13)
	(feed S14 S13)
	(closed S13 S14) (closed S14 S13)
	(connected S6 S67) (connected S67 S6)
	(feed S67 S6)
	(closed S6 S67) (closed S67 S6)
	(connected S67 S68) (connected S68 S67)
	(feed S68 S67)
	(closed S67 S68) (closed S68 S67)
	(connected P70 S15)(connected S15 P70)
	(feed S15 P70)
	(closed P70 S15)(closed S15 P70)
	(connected S15 S16) (connected S16 S15)
	(feed S16 S15)
	(closed S15 S16) (closed S16 S15)
	(connected S16 S17) (connected S17 S16)
	(feed S17 S16)
	(closed S16 S17) (closed S17 S16)
	(connected S17 S18) (connected S18 S17)
	(feed S18 S17)
	(closed S17 S18) (closed S18 S17)
	(connected S18 S19) (connected S19 S18)
	(feed S19 S18)
	(closed S18 S19) (closed S19 S18)
	(connected S19 S20) (connected S20 S19)
	(feed S20 S19)
	(closed S19 S20) (closed S20 S19)
	(connected S20 S21) (connected S21 S20)
	(feed S21 S20)
	(closed S20 S21) (closed S21 S20)
	(connected S16 S22) (connected S22 S16)
	(feed S22 S16)
	(closed S16 S22) (closed S22 S16)
	(connected S22 S23) (connected S23 S22)
	(feed S23 S22)
	(closed S22 S23) (closed S23 S22)
	(connected S23 S24) (connected S24 S23)
	(feed S24 S23)
	(closed S23 S24) (closed S24 S23)
	(connected S24 S25) (connected S25 S24)
	(feed S25 S24)
	(closed S24 S25) (closed S25 S24)
	(connected S25 S26) (connected S26 S25)
	(feed S26 S25)
	(closed S25 S26) (closed S26 S25)
	(connected S26 S27) (connected S27 S26)
	(feed S27 S26)
	(closed S26 S27) (closed S27 S26)
	(connected S27 S28) (connected S28 S27)
	(feed S28 S27)
	(closed S27 S28) (closed S28 S27)
	(connected P69 S29)(connected S29 P69)
	(feed S29 P69)
	(closed P69 S29)(closed S29 P69)
	(connected S29 S30) (connected S30 S29)
	(feed S30 S29)
	(closed S29 S30) (closed S30 S29)
	(connected S30 S31) (connected S31 S30)
	(feed S31 S30)
	(closed S30 S31) (closed S31 S30)
	(connected S31 S32) (connected S32 S31)
	(feed S32 S31)
	(closed S31 S32) (closed S32 S31)
	(connected S32 S33) (connected S33 S32)
	(feed S33 S32)
	(closed S32 S33) (closed S33 S32)
	(connected S33 S34) (connected S34 S33)
	(feed S34 S33)
	(closed S33 S34) (closed S34 S33)
	(connected S34 S35) (connected S35 S34)
	(feed S35 S34)
	(closed S34 S35) (closed S35 S34)
	(connected S35 S36) (connected S36 S35)
	(feed S36 S35)
	(closed S35 S36) (closed S36 S35)
	(connected S36 S37) (connected S37 S36)
	(feed S37 S36)
	(closed S36 S37) (closed S37 S36)
	(connected S39 S38) (connected S38 S39)
	(feed S38 S39)
	(closed S39 S38) (closed S38 S39)
	(connected S38 S40) (connected S40 S38)
	(feed S40 S38)
	(closed S38 S40) (closed S40 S38)
	(connected S40 S41) (connected S41 S40)
	(feed S41 S40)
	(closed S40 S41) (closed S41 S40)
	(connected S41 S42) (connected S42 S41)
	(feed S42 S41)
	(closed S41 S42) (closed S42 S41)
	(connected S43 S39) (connected S39 S43)
	(feed S39 S43)
	(closed S43 S39) (closed S39 S43)
	(connected S44 S43) (connected S43 S44)
	(feed S43 S44)
	(closed S44 S43) (closed S43 S44)
	(connected S41 S45) (connected S45 S41)
	(feed S45 S41)
	(closed S41 S45) (closed S45 S41)
	(connected S34 S46) (connected S46 S34)
	(feed S46 S34)
	(closed S34 S46) (closed S46 S34)
	(connected S46 S47) (connected S47 S46)
	(feed S47 S46)
	(closed S46 S47) (closed S47 S46)
	(connected S47 S48) (connected S48 S47)
	(feed S48 S47)
	(closed S47 S48) (closed S48 S47)
	(connected S48 S49) (connected S49 S48)
	(feed S49 S48)
	(closed S48 S49) (closed S49 S48)
	(connected P69 S50)(connected S50 P69)
	(feed S50 P69)
	(closed P69 S50)(closed S50 P69)
	(connected S50 S51) (connected S51 S50)
	(feed S51 S50)
	(closed S50 S51) (closed S51 S50)
	(connected S51 S52) (connected S52 S51)
	(feed S52 S51)
	(closed S51 S52) (closed S52 S51)
	(connected S52 S53) (connected S53 S52)
	(feed S53 S52)
	(closed S52 S53) (closed S53 S52)
	(connected S53 S54) (connected S54 S53)
	(feed S54 S53)
	(closed S53 S54) (closed S54 S53)
	(connected S54 S55) (connected S55 S54)
	(feed S55 S54)
	(closed S54 S55) (closed S55 S54)
	(connected S51 S56) (connected S56 S51)
	(feed S56 S51)
	(closed S51 S56) (closed S56 S51)
	(connected S56 S57) (connected S57 S56)
	(feed S57 S56)
	(closed S56 S57) (closed S57 S56)
	(connected S57 S58) (connected S58 S57)
	(feed S58 S57)
	(closed S57 S58) (closed S58 S57)
	(connected S58 S59) (connected S59 S58)
	(feed S59 S58)
	(closed S58 S59) (closed S59 S58)
	(connected S55 S60) (connected S60 S55)
	(feed S60 S55)
	(closed S55 S60) (closed S60 S55)
	(connected S60 S61) (connected S61 S60)
	(feed S61 S60)
	(closed S60 S61) (closed S61 S60)
	(connected S61 S62) (connected S62 S61)
	(feed S62 S61)
	(closed S61 S62) (closed S62 S61)
	(connected S62 S63) (connected S63 S62)
	(feed S63 S62)
	(closed S62 S63) (closed S63 S62)
	(connected S61 S64) (connected S64 S61)
	(feed S64 S61)
	(closed S61 S64) (closed S64 S61)
	(connected S64 S65) (connected S65 S64)
	(feed S65 S64)
	(closed S64 S65) (closed S65 S64)
	(connected S65 S66) (connected S66 S65)
	(feed S66 S65)
	(closed S65 S66) (closed S66 S65)
	(connected S8 S49) (connected S49 S8)
	(feed S49 S8)
	(open_line S8 S49) (open_line S49 S8)
	(connected S8 S37) (connected S37 S8)
	(feed S37 S8)
	(open_line S8 S37) (open_line S37 S8)
	(connected S14 S45) (connected S45 S14)
	(feed S45 S14)
	(open_line S14 S45) (open_line S45 S14)
	(connected S21 S66) (connected S66 S21)
	(feed S66 S21)
	(open_line S21 S66) (open_line S66 S21)
	(connected S28 S63) (connected S63 S28)
	(feed S63 S28)
	(open_line S28 S63) (open_line S63 S28)
	(connected S59 S44) (connected S44 S59)
	(feed S44 S59)
	(closed S59 S44) (closed S44 S59)
	(connected S42 S37) (connected S37 S42)
	(feed S37 S42)
	(open_line S42 S37) (open_line S37 S42)
	(connected S58 S38) (connected S38 S58)
	(feed S38 S58)
	(open_line S58 S38) (open_line S38 S58)
	(connected S20 S26) (connected S26 S20)
	(feed S26 S20)
	(open_line S20 S26) (open_line S26 S20)
	(connected S68 S49) (connected S49 S68)
	(feed S49 S68)
	(open_line S68 S49) (open_line S49 S68)
	(connected S66 S14) (connected S14 S66)
	(feed S14 S66)
	(open_line S66 S14) (open_line S14 S66)
	(feed P69 P69)
	(feed P70 P70)
	(available P69)
	(available P70)
	(available S1)
	(available S2)
	(full S3)
	(available S4)
	(available S5)
	(full S6)
	(available S7)
	(full S8)
	(available S9)
	(available S10)
	(available S11)
	(available S12)
	(available S13)
	(full S14)
	(available S15)
	(full S16)
	(available S17)
	(available S18)
	(available S19)
	(full S20)
	(available S21)
	(available S22)
	(available S23)
	(available S24)
	(available S25)
	(full S26)
	(available S27)
	(available S28)
	(available S29)
	(available S30)
	(available S31)
	(available S32)
	(available S33)
	(full S34)
	(available S35)
	(available S36)
	(full S37)
	(full S38)
	(available S39)
	(available S40)
	(full S41)
	(available S42)
	(available S43)
	(available S44)
	(available S45)
	(available S46)
	(available S47)
	(available S48)
	(full S49)
	(available S50)
	(full S51)
	(available S52)
	(available S53)
	(available S54)
	(available S55)
	(available S56)
	(available S57)
	(full S58)
	(available S59)
	(available S60)
	(full S61)
	(available S62)
	(available S63)
	(available S64)
	(available S65)
	(full S66)
	(available S67)
	(available S68)
	(buildable S22 S15)
	(buildable S15 S22)
	(buildable S52 S28)
	(buildable S28 S52)
	(buildable S56 S50)
	(buildable S50 S56)
	(buildable S59 S56)
	(buildable S56 S59)
	(buildable S57 S59)
	(buildable S59 S57)
	(buildable P69 S57)
	(buildable S57 P69)
	(buildable S16 P70)
	(buildable P70 S16)
	(buildable S63 S21)
	(buildable S21 S63)
	(buildable S55 S62)
	(buildable S62 S55)
	(buildable S60 S53)
	(buildable S53 S60)
	(buildable S45 S66)
	(buildable S66 S45)
	(buildable S44 S45)
	(buildable S45 S44)
	(buildable P69 S44)
	(buildable S44 P69)
	(buildable S10 P70)
	(buildable P70 S10)
	(buildable S37 S14)
	(buildable S14 S37)
	(buildable S46 S35)
	(buildable S35 S46)
	(buildable S42 S33)
	(buildable S33 S42)
	(buildable S43 S40)
	(buildable S40 S43)
	(buildable P69 S58)
	(buildable S58 P69)
	(buildable S4 S9)
	(buildable S9 S4)
	(buildable S67 S7)
	(buildable S7 S67)
	(buildable S8 S67)
	(buildable S67 S8)
	(buildable S68 S8)
	(buildable S8 S68)
	(buildable S32 S47)
	(buildable S47 S32)
	(mutable S22)
	(mutable S15)
	(mutable S52)
	(mutable S28)
	(mutable S56)
	(mutable S50)
	(mutable S59)
	(mutable S57)
	(mutable P69)
	(mutable S16)
	(mutable P70)
	(mutable S63)
	(mutable S21)
	(mutable S55)
	(mutable S62)
	(mutable S60)
	(mutable S53)
	(mutable S64)
	(mutable S61)
	(mutable S45)
	(mutable S66)
	(mutable S44)
	(mutable S10)
	(mutable S37)
	(mutable S14)
	(mutable S46)
	(mutable S35)
	(mutable S42)
	(mutable S33)
	(mutable S40)
	(mutable S41)
	(mutable S43)
	(mutable S58)
	(mutable S38)
	(mutable S4)
	(mutable S9)
	(mutable S67)
	(mutable S7)
	(mutable S8)
	(mutable S68)
	(mutable S32)
	(mutable S47)
	(mutable S3)
	(mutable S6)
	(mutable S34)
	(mutable S51)
	(mutable S49)
	(mutable S26)
	(mutable S20)
	)
(:goal (and
	(connected P70 S15)(connected S15 P70)
	(closed P70 S15)(closed S15 P70)
	(connected S15 S22) (connected S22 S15)
	(closed S15 S22) (closed S22 S15)
	(connected S22 S23) (connected S23 S22)
	(closed S22 S23) (closed S23 S22)
	(connected S23 S24) (connected S24 S23)
	(closed S23 S24) (closed S24 S23)
	(connected S24 S25) (connected S25 S24)
	(closed S24 S25) (closed S25 S24)
	(connected S25 S26) (connected S26 S25)
	(closed S25 S26) (closed S26 S25)
	(connected S26 S27) (connected S27 S26)
	(closed S26 S27) (closed S27 S26)
	(connected S27 S28) (connected S28 S27)
	(closed S27 S28) (closed S28 S27)
	(connected S28 S52) (connected S52 S28)
	(open_line S28 S52) (open_line S52 S28)
	(connected S51 S52) (connected S52 S51)
	(closed S51 S52) (closed S52 S51)
	(connected S51 S50) (connected S50 S51)
	(closed S51 S50) (closed S50 S51)
	(connected S50 S56) (connected S56 S50)
	(closed S50 S56) (closed S56 S50)
	(connected S56 S59) (connected S59 S56)
	(closed S56 S59) (closed S59 S56)
	(connected S59 S57) (connected S57 S59)
	(closed S59 S57) (closed S57 S59)
	(connected S57 P69)(connected P69 S57)
	(closed S57 P69)(closed P69 S57)
	(connected P70 S16)(connected S16 P70)
	(closed P70 S16)(closed S16 P70)
	(connected S16 S17) (connected S17 S16)
	(closed S16 S17) (closed S17 S16)
	(connected S17 S18) (connected S18 S17)
	(closed S17 S18) (closed S18 S17)
	(connected S18 S19) (connected S19 S18)
	(closed S18 S19) (closed S19 S18)
	(connected S19 S20) (connected S20 S19)
	(closed S19 S20) (closed S20 S19)
	(connected S20 S21) (connected S21 S20)
	(closed S20 S21) (closed S21 S20)
	(connected S21 S63) (connected S63 S21)
	(closed S21 S63) (closed S63 S21)
	(connected S63 S62) (connected S62 S63)
	(closed S63 S62) (closed S62 S63)
	(connected S62 S55) (connected S55 S62)
	(closed S62 S55) (closed S55 S62)
	(connected S55 S54) (connected S54 S55)
	(closed S55 S54) (closed S54 S55)
	(connected S54 S53) (connected S53 S54)
	(closed S54 S53) (closed S53 S54)
	(connected S53 S60) (connected S60 S53)
	(closed S53 S60) (closed S60 S53)
	(connected S60 S61) (connected S61 S60)
	(closed S60 S61) (closed S61 S60)
	(connected S61 S64) (connected S64 S61)
	(open_line S61 S64) (open_line S64 S61)
	(connected S64 S65) (connected S65 S64)
	(closed S64 S65) (closed S65 S64)
	(connected S65 S66) (connected S66 S65)
	(closed S65 S66) (closed S66 S65)
	(connected S66 S45) (connected S45 S66)
	(closed S66 S45) (closed S45 S66)
	(connected S45 S44) (connected S44 S45)
	(closed S45 S44) (closed S44 S45)
	(connected S44 P69)(connected P69 S44)
	(closed S44 P69)(closed P69 S44)
	(connected P70 S10)(connected S10 P70)
	(closed P70 S10)(closed S10 P70)
	(connected S10 S11) (connected S11 S10)
	(closed S10 S11) (closed S11 S10)
	(connected S11 S12) (connected S12 S11)
	(closed S11 S12) (closed S12 S11)
	(connected S12 S13) (connected S13 S12)
	(closed S12 S13) (closed S13 S12)
	(connected S13 S14) (connected S14 S13)
	(closed S13 S14) (closed S14 S13)
	(connected S14 S37) (connected S37 S14)
	(closed S14 S37) (closed S37 S14)
	(connected S37 S36) (connected S36 S37)
	(closed S37 S36) (closed S36 S37)
	(connected S36 S35) (connected S35 S36)
	(closed S36 S35) (closed S35 S36)
	(connected S35 S46) (connected S46 S35)
	(closed S35 S46) (closed S46 S35)
	(connected S46 S34) (connected S34 S46)
	(closed S46 S34) (closed S34 S46)
	(connected S34 S33) (connected S33 S34)
	(closed S34 S33) (closed S33 S34)
	(connected S33 S42) (connected S42 S33)
	(closed S33 S42) (closed S42 S33)
	(connected S42 S41) (connected S41 S42)
	(closed S42 S41) (closed S41 S42)
	(connected S41 S40) (connected S40 S41)
	(open_line S41 S40) (open_line S40 S41)
	(connected S40 S43) (connected S43 S40)
	(closed S40 S43) (closed S43 S40)
	(connected S43 S39) (connected S39 S43)
	(closed S43 S39) (closed S39 S43)
	(connected S39 S38) (connected S38 S39)
	(closed S39 S38) (closed S38 S39)
	(connected S38 S58) (connected S58 S38)
	(closed S38 S58) (closed S58 S38)
	(connected S58 P69)(connected P69 S58)
	(closed S58 P69)(closed P69 S58)
	(connected P70 S1)(connected S1 P70)
	(closed P70 S1)(closed S1 P70)
	(connected S1 S2) (connected S2 S1)
	(closed S1 S2) (closed S2 S1)
	(connected S2 S3) (connected S3 S2)
	(closed S2 S3) (closed S3 S2)
	(connected S3 S9) (connected S9 S3)
	(closed S3 S9) (closed S9 S3)
	(connected S9 S4) (connected S4 S9)
	(closed S9 S4) (closed S4 S9)
	(connected S4 S5) (connected S5 S4)
	(closed S4 S5) (closed S5 S4)
	(connected S5 S6) (connected S6 S5)
	(closed S5 S6) (closed S6 S5)
	(connected S6 S7) (connected S7 S6)
	(closed S6 S7) (closed S7 S6)
	(connected S7 S67) (connected S67 S7)
	(closed S7 S67) (closed S67 S7)
	(connected S67 S8) (connected S8 S67)
	(closed S67 S8) (closed S8 S67)
	(connected S8 S68) (connected S68 S8)
	(closed S8 S68) (closed S68 S8)
	(connected S68 S49) (connected S49 S68)
	(open_line S68 S49) (open_line S49 S68)
	(connected S49 S48) (connected S48 S49)
	(closed S49 S48) (closed S48 S49)
	(connected S48 S47) (connected S47 S48)
	(closed S48 S47) (closed S47 S48)
	(connected S47 S32) (connected S32 S47)
	(closed S47 S32) (closed S32 S47)
	(connected S32 S31) (connected S31 S32)
	(closed S32 S31) (closed S31 S32)
	(connected S31 S30) (connected S30 S31)
	(closed S31 S30) (closed S30 S31)
	(connected S30 S29) (connected S29 S30)
	(closed S30 S29) (closed S29 S30)
	(connected S29 P69)(connected P69 S29)
	(closed S29 P69)(closed P69 S29)
	(removed S4 S3)
	(removed S3 S4)
	(removed S8 S7)
	(removed S7 S8)
	(removed S10 S9)
	(removed S9 S10)
	(removed S67 S6)
	(removed S6 S67)
	(removed S68 S67)
	(removed S67 S68)
	(removed S16 S15)
	(removed S15 S16)
	(removed S22 S16)
	(removed S16 S22)
	(removed S33 S32)
	(removed S32 S33)
	(removed S35 S34)
	(removed S34 S35)
	(removed S40 S38)
	(removed S38 S40)
	(removed S43 S44)
	(removed S44 S43)
	(removed S45 S41)
	(removed S41 S45)
	(removed S47 S46)
	(removed S46 S47)
	(removed S50 P69)
	(removed P69 S50)
	(removed S53 S52)
	(removed S52 S53)
	(removed S56 S51)
	(removed S51 S56)
	(removed S57 S56)
	(removed S56 S57)
	(removed S58 S57)
	(removed S57 S58)
	(removed S59 S58)
	(removed S58 S59)
	(removed S60 S55)
	(removed S55 S60)
	(removed S62 S61)
	(removed S61 S62)
	(removed S49 S8)
	(removed S8 S49)
	(removed S37 S8)
	(removed S8 S37)
	(removed S45 S14)
	(removed S14 S45)
	(removed S66 S21)
	(removed S21 S66)
	(removed S63 S28)
	(removed S28 S63)
	(removed S44 S59)
	(removed S59 S44)
	(removed S37 S42)
	(removed S42 S37)
	(removed S26 S20)
	(removed S20 S26)
	(removed S14 S66)
	(removed S66 S14)
	)
)
)