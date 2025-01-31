INSERT INTO task (site_id, plot_id, company_id, task_name, task_type, trade)
VALUES 
-- site one all companies
(1, 1, 1, 'Build foundations', 'ground_works', 'ground workers'),
-- bricklayers
(1, 1, 2, 'Build walls', 'first_fix', 'bricklayers'),
-- plumbers
(1, 1, 3, 'Install pipes', 'first_fix', 'plumbers'),
(1, 1, 3, 'Install bathrooms', 'second_fix', 'plumbers'),
(1, 1, 3, 'Install radiators', 'second_fix', 'plumbers'),
(1, 1, 3, 'Install boiler', 'second_fix', 'plumbers'),
-- roofers
(1, 1, 4, 'Tile roof', 'first_fix', 'roofers'),
(1, 1, 4, 'Install guttering', 'first_fix', 'roofers'),
-- carpenters
(1, 1, 5, 'Build walls', 'first_fix', 'carpenters'),
(1, 1, 5, 'Fit stairs', 'first_fix', 'carpenters'),
(1, 1, 5, 'Fit roof', 'first_fix', 'carpenters'),
(1, 1, 5, 'Fit doors, frames, skirting, architrave', 'second_fix', 'carpenters'),
(1, 1, 5, 'Fit kitchen', 'second_fix', 'carpenters'),
(1, 1, 5, 'Fit ironmongery', 'third_fix', 'carpenters'),
-- electricians
(1, 1, 6, 'Lay cables', 'first_fix', 'electricians'),
(1, 1, 6, 'fit faces', 'second_fix', 'electricians'),
-- painters
(1, 1, 7, 'Paint internals', 'second_fix', 'painters'),
(1, 1, 7, 'Touch ups', 'third_fix', 'painters'),
-- surveys
(1, 1, 8, 'utility survey', 'surveys', 'surveyors'),
(1, 1, 9, 'NHBC survey', 'surveys', 'surveyors');