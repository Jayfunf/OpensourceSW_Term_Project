horizen_t = 0 #
MN = 0 #
H = 0 #
R = 0 #

pi = 3.1416
rate_hv = 1.414
horizen_actual = 297 #mm
vertical_t = rate_hv*horizen_t
rate_actual = horizen_actual/horizen_t
cos = MN/vertical_t
sin = (1-cos^2)^(1/2)
h_t = H/sin
H_actual = h_t*rate_actual
R_actual = R*rate_actual
volume = R_actual^2 * pi * H_actual