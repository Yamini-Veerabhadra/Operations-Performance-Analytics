# Project notes, evidence and limits

- Primary order source: Olist historical Brazilian e-commerce data, approximately 2016–2018.
- Previous analysis (user-supplied SQL results): 99,441 orders; 96,478 delivered; 96,470 eligible for timing; 88,644 on-time; 7,826 late; late rate 8.11%.
- User-supplied SQL findings: March 2018 purchase cohort had 7,003 eligible delivered orders and 1,496 late (21.36%). In RJ, March 2018 had 864 eligible deliveries and 319 late (36.92%).
- For RJ March 2018: users found late orders with average carrier-to-customer transit 35.38 days versus 12.71 for on-time, and approval-to-carrier averages 3.06 versus 2.81 days. These are associations, not causal identification.
- Data quality: 8 delivered orders missing customer delivery timestamps; 2 delivered missing carrier timestamps; 23 with delivery before carrier handover.
- The 32 excluded rows reported for prior clean shipping view reflect the union of relevant missing/invalid fields, not necessarily the sum of disjoint defects.
- Historical data are **not real-time**, and in-sample Isolation Forest results are **not production alert accuracy**.
- This is a portfolio study, not proof of a reduction in operational costs or delays.
- `data/reference` contains exports from the initial starter run; new CSV exports can differ when settings or analysis logic change.
