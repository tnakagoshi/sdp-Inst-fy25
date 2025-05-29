-- database: ../sdp-Eteam-fy25/suppliesproject/db.sqlite3

SELECT * FROM supplies_supplies;
insert into supplies_supplies (
    id, title, description, category, user_id, current_value,threshold)
     values (1, 'Laptop', 'Dell XPS 13', 'other',1, 999, 3);
     
INSERT INTO `db_rental` (`borrowed_value`, `end_date`, `status`, `supplies_id`, `user_id`, `start_date`)
VALUES (5, '2025-05-30', true, 1, 1, '2025-05-28');
