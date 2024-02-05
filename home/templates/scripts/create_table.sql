CREATE TABLE home_lostitem(
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    lost_loc VARCHAR(25) NOT NULL,
    lost_latitude INT(11) NOT NULL,
    lost_longetude INT(11) NOT NULL,
    lost_item VARCHAR(30) NOT NULL,
    item_desc VARCHAR(255) NOT NULL,
    circle_radio INT(4),
    lost_date DATETIME NOT NULL,
    lost_fk_id INT NOT NULL,
    FOREIGN KEY (lost_fk_id) REFERENCES auth_user (id),
    item_status BOOLEAN DEFAULT FALSE NOT NULL
);