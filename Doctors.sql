CREATE TABLE DoctorDetails{
doc_ID VARCHAR2(10) NOT NULL,
doc_name VARCHAR2(50),
doc_contact VARCHAR2(10),
doc_pwd VARCHAR2(200),
doc_add VARCHAR2(100),
doc_sex CHAR,
spec VARCHAR2(20),
in_time TIME,
hours INT,
PRIMARY KEY (ID)
};

INSERT INTO DoctorDetails ('EDO_994639', 'Edogawa Con', '9945132639', '1122', 'M-291, Safaa Apts, Chennnai', 'M', 'PHYSICIAN', 10:00:00, 5);
INSERT INTO DoctorDetails ('VEN_994640', 'Venkat R', '9945132640', 'L-101, Safaa Apts, Chennnai', 'ADD', 'M', 'PSYCHIATRIST', 10:00:00, 5);
INSERT INTO DoctorDetails ('GAU_994641', 'Gaurav Singh', '9945132641', '1144', 'K-45, Safaa Apts, Chennnai', 'M', 'CARDIOLOGIST', 10:00:00, 5);
INSERT INTO DoctorDetails ('PRA_994642', 'Pragati Sharma', '9945132642', '1155', 'T-19, Safaa Apts, Chennnai', 'F', 'GYNECOLOGIST', 10:00:00, 5);
INSERT INTO DoctorDetails ('BRA_994643', 'Brandon Tan', '9945132643', '1166', 'Q-87, Safaa Apts, Chennnai', 'M', 'NEUROLOGIST', 10:00:00, 5);
INSERT INTO DoctorDetails ('ROH_994644', 'Rohit Batra', '9945132644', '1177', 'P-393, Safaa Apts, Chennnai', 'M', 'SURGEON', 10:00:00, 5);

