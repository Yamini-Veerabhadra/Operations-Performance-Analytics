-- Run after importing olist_orders_dataset into a PostgreSQL table named olist_orders.
-- Use one row per order; excludes non-delivered orders from on-time denominator.
SELECT
  DATE_TRUNC('day', order_purchase_timestamp)::date AS purchase_day,
  COUNT(DISTINCT order_id) AS orders,
  COUNT(*) FILTER (WHERE order_status = 'delivered') AS delivered_orders,
  COUNT(*) FILTER (WHERE order_status = 'delivered' AND order_delivered_customer_date IS NOT NULL AND order_estimated_delivery_date IS NOT NULL) AS delivery_eligible,
  COUNT(*) FILTER (WHERE order_status = 'delivered' AND order_delivered_customer_date <= order_estimated_delivery_date AND order_delivered_customer_date IS NOT NULL) AS on_time_orders
FROM olist_orders
GROUP BY 1 ORDER BY 1;
