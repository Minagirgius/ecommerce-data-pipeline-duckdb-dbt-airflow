select *
from {{ ref('fact_orders') }}
where total_amount_usd < 0