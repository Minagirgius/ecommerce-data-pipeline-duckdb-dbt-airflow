select *
from {{ ref('stg_payments') }}
where amount_usd < 0