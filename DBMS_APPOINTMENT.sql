CREATE TABLE Appointment (
	Patient_ID VARCHAR(10),
	Doctor_ID VARCHAR(10),
	Hospital_ID VARCHAR(50),
	Appointment_Date_Time DATETIME,
	Appointment_Token INT,
	FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
	FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID),
	FOREIGN KEY (Hospital_ID) REFERENCES Hospital(Hospital_ID)
);

INSERT INTO Appointment VALUES ('tom_123123', 'edo_994639', 'ste_ing', '01-01-2018 10:00:00', 1);
INSERT INTO Appointment VALUES ('joe_456123', 'ven_994640', 'app_llo', '01-01-2018 10:30:00', 2);
INSERT INTO Appointment VALUES ('ros_567123', 'gau_994641', 'for_tis', '01-01-2018 12:30:00', 3);
INSERT INTO Appointment VALUES ('ros_678123', 'pra_994642', 'for_tis', '01-01-2018 03:00:00', 4);
INSERT INTO Appointment VALUES ('rob_911119', 'bra_994643', 'ste_ing', '01-01-2018 05:00:00', 5);
