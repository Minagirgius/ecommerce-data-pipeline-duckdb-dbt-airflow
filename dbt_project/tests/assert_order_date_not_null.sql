select *
from {{ ref('stg_orders') }}
where order_date is null