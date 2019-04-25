CREATE TABLE Patient(
  Patient_ID VARCHAR(10) NOT NULL,
  Patient_ph VARCHAR(10),
  Patient_pwd VARCHAR(200),
  Patient_name VARCHAR(50),
  Patient_bg VARCHAR(3),
  Patient_address VARCHAR(60),
  Patient_age INTEGER(110),
  Patient_sex CHAR,
  PRIMARY KEY (Patient_ID)
);

INSERT INTO Patient VALUES ('tom_123123','1230123123','this is a Patient_pwd','Tom Hanks','O+','B-491 , Triton Apts , Gudvancherry Chennai',20,'M');

INSERT INTO Patient VALUES ('joe_456123','4560123123','this is a Patient_pwd','Joe Bill','B+','BD-221, SaltLake Valley, Delhi',25,'M');

INSERT INTO Patient VALUES ('ros_567123','5670123123','this is a Patient_pwd','Rose Mary Marlo','AB+','C-7/3, BCT Avenue, Gurgaon Sector 2',27,'F');

INSERT INTO Patient VALUES ('ros_678123','6780123123','this is a Patient_pwd','Roslina Ronald','AB-','P-99, Sarvanah Apts, Chennnai',18,'F');

INSERT INTO Patient VALUES ('rob_911119','9119211119','this is a Patient_pwd','Robert Stark','A-','P-101, Sarvanah Apts, Chennnai',48,'M');

INSERT INTO Patient VALUES ('ary_911111','9111009111','this is a Patient_pwd','Arya Stark','B+','P-111, Sarvanah Apts, Chennnai',21,'F');
