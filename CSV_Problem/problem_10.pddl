(define (problem disnet10n) (:domain disnet)
(:objects
	P11 P12 - Primary
	S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 - Secondary
	)
(:init
	(is-primary P11)
	(is-primary P12)
	(connected P11 S10)(connected S10 P11)
	(feed S10 P11)
	(closed P11 S10)(closed S10 P11)
	(connected S10 S5) (connected S5 S10)
	(feed S5 S10)
	(closed S10 S5) (closed S5 S10)
	(connected S5 S2) (connected S2 S5)
	(feed S2 S5)
	(closed S5 S2) (closed S2 S5)
	(connected S2 S9) (connected S9 S2)
	(feed S9 S2)
	(open_line S2 S9) (open_line S9 S2)
	(connected S9 S6) (connected S6 S9)
	(feed S6 S9)
	(closed S9 S6) (closed S6 S9)
	(connected S6 S8) (connected S8 S6)
	(feed S8 S6)
	(closed S6 S8) (closed S8 S6)
	(connected S8 S7) (connected S7 S8)
	(feed S7 S8)
	(closed S8 S7) (closed S7 S8)
	(connected S7 S3) (connected S3 S7)
	(feed S3 S7)
	(closed S7 S3) (closed S3 S7)
	(connected S3 P12)(connected P12 S3)
	(feed P12 S3)
	(closed S3 P12)(closed P12 S3)
	(connected P11 S1)(connected S1 P11)
	(feed S1 P11)
	(closed P11 S1)(closed S1 P11)
	(connected S1 S4) (connected S4 S1)
	(feed S4 S1)
	(open_line S1 S4) (open_line S4 S1)
	(connected S4 P12)(connected P12 S4)
	(feed P12 S4)
	(closed S4 P12)(closed P12 S4)
	(feed P11 P11)
	(feed P12 P12)
	(available P11)
	(available P12)
	(available S1)
	(available S2)
	(available S3)
	(available S4)
	(available S5)
	(available S6)
	(available S7)
	(available S8)
	(available S9)
	(available S10)
	(buildable S5 P11)
	(buildable P11 S5)
	(buildable S9 S5)
	(buildable S5 S9)
	(buildable S2 P11)
	(buildable P11 S2)
	(buildable S10 S2)
	(buildable S2 S10)
	(buildable S4 S10)
	(buildable S10 S4)
	(buildable P12 S1)
	(buildable S1 P12)
	(mutable S5)
	(mutable P11)
	(mutable S9)
	(mutable S8)
	(mutable S6)
	(mutable S2)
	(mutable S10)
	(mutable S4)
	(mutable S1)
	(mutable P12)
	)
(:goal (and
	(connected P11 S5)(connected S5 P11)
	(closed P11 S5)(closed S5 P11)
	(connected S5 S9) (connected S9 S5)
	(closed S5 S9) (closed S9 S5)
	(connected S9 S6) (connected S6 S9)
	(closed S9 S6) (closed S6 S9)
	(connected S6 S8) (connected S8 S6)
	(open_line S6 S8) (open_line S8 S6)
	(connected S8 S7) (connected S7 S8)
	(closed S8 S7) (closed S7 S8)
	(connected S7 S3) (connected S3 S7)
	(closed S7 S3) (closed S3 S7)
	(connected S3 P12)(connected P12 S3)
	(closed S3 P12)(closed P12 S3)
	(connected P11 S2)(connected S2 P11)
	(closed P11 S2)(closed S2 P11)
	(connected S2 S10) (connected S10 S2)
	(open_line S2 S10) (open_line S10 S2)
	(connected S10 S4) (connected S4 S10)
	(closed S10 S4) (closed S4 S10)
	(connected S4 S1) (connected S1 S4)
	(closed S4 S1) (closed S1 S4)
	(connected S1 P12)(connected P12 S1)
	(closed S1 P12)(closed P12 S1)
	(removed S10 P11)
	(removed P11 S10)
	(removed S5 S10)
	(removed S10 S5)
	(removed S2 S5)
	(removed S5 S2)
	(removed S9 S2)
	(removed S2 S9)
	(removed S1 P11)
	(removed P11 S1)
	(removed P12 S4)
	(removed S4 P12)
	)
)
)