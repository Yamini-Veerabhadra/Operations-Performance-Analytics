-- PostgreSQL reporting views (run AFTER scripts/load_postgres.py).
-- Consistent grain: one row per order. Avoid multiplying item/payment rows.
CREATE OR REPLACE VIEW vw_order_facts AS
WITH item_totals AS (
 SELECT order_id, COUNT(*) AS item_count, SUM(price) AS items_value,
        SUM(freight_value) AS freight_value, COUNT(DISTINCT seller_id) AS seller_count
 FROM olist_items GROUP BY order_id
), payment_totals AS (
 SELECT order_id, SUM(payment_value) AS payment_total FROM olist_payments GROUP BY order_id
)
SELECT o.order_id, o.customer_id, c.customer_state, c.customer_city,
 o.order_status, o.order_purchase_timestamp, o.order_approved_at,
 o.order_delivered_carrier_date, o.order_delivered_customer_date,
 o.order_estimated_delivery_date, i.item_count, i.items_value, i.freight_value,
 i.seller_count, p.payment_total,
 (o.order_status='delivered' AND o.order_delivered_customer_date IS NOT NULL
   AND o.order_estimated_delivery_date IS NOT NULL) AS eligible,
 (o.order_status='delivered' AND o.order_delivered_customer_date IS NOT NULL
   AND o.order_estimated_delivery_date IS NOT NULL
   AND o.order_delivered_customer_date > o.order_estimated_delivery_date) AS late,
 CASE WHEN o.order_delivered_carrier_date IS NOT NULL AND o.order_delivered_customer_date >= o.order_delivered_carrier_date
 THEN ROUND((EXTRACT(EPOCH FROM(o.order_delivered_customer_date-o.order_delivered_carrier_date))/86400)::numeric,2)
 ELSE NULL END AS shipping_days
FROM olist_orders o
LEFT JOIN olist_customers c ON c.customer_id=o.customer_id
LEFT JOIN item_totals i ON i.order_id=o.order_id
LEFT JOIN payment_totals p ON p.order_id=o.order_id;

CREATE OR REPLACE VIEW vw_monthly_performance AS
SELECT DATE_TRUNC('month',order_purchase_timestamp)::date AS purchase_month,
 COUNT(*) AS orders, COUNT(*) FILTER(WHERE eligible) AS eligible_deliveries,
 COUNT(*) FILTER(WHERE late) AS late_deliveries,
 ROUND(100.0*COUNT(*) FILTER(WHERE late)/NULLIF(COUNT(*) FILTER(WHERE eligible),0),2) AS late_rate,
 ROUND(AVG(shipping_days),2) AS avg_shipping_days
FROM vw_order_facts GROUP BY 1;

CREATE OR REPLACE VIEW vw_state_performance AS
SELECT customer_state, COUNT(*) AS orders,
 COUNT(*) FILTER(WHERE eligible) AS eligible_deliveries,
 COUNT(*) FILTER(WHERE late) AS late_deliveries,
 ROUND(100.0*COUNT(*) FILTER(WHERE late)/NULLIF(COUNT(*) FILTER(WHERE eligible),0),2) AS late_rate
FROM vw_order_facts GROUP BY customer_state;

-- Window functions and CTE example for trend reporting
WITH monthly AS (SELECT * FROM vw_monthly_performance)
SELECT purchase_month, orders, late_rate,
 LAG(orders) OVER (ORDER BY purchase_month) AS previous_month_orders,
 ROUND(AVG(orders) OVER (ORDER BY purchase_month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW),1) AS trailing_3_month_avg
FROM monthly ORDER BY purchase_month;
