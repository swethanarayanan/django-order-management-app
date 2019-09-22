--Add Items not in a warehouse
insert into stock
select all_item_warehouse.w_id, all_item_warehouse.i_id, 0 as s_qty 
from
(
	select i.i_id, w.w_id
	from item i, warehouse w
) all_item_warehouse
left join
( 	
	select i_id, w_id
 	from stock s
) item_warehouse_with_quantity 
on all_item_warehouse.i_id = item_warehouse_with_quantity.i_id
and all_item_warehouse.w_id = item_warehouse_with_quantity.w_id
where item_warehouse_with_quantity.i_id is null
