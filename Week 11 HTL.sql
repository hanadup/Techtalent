SELECT * FROM uni.student Where EmailAddress = 'val.bolger@example.com';
SELECT * FROM uni.student Where courseID >1;
SELECT * FROM uni.module Where Subject = 'Economics';
SELECT * FROM uni.schedule Where CDate < '2020-09-21'
SELECT * FROM uni.module;
INSERT INTO module (Subject) Values ('Deep-Space Radar Telemetry');
INSERT INTO module (ModuleID, ModuleName, Subject, Level, Credits) Values ('114', 'String Theory', 'Quantum Physics', '6', '20'), ('115', 'Exotic Matter', 'Quantum Physics', '6', '20'), ('116', 'Harnessing the Einstein-Rosen Bridge', 'Quantum Physics', '6', '20'), ('117', 'Supercollision and miniature Black Holes', 'Quantum Physics', '6', '20');
