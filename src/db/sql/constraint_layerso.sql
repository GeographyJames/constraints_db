--
-- PostgreSQL database dump
--

-- Dumped from database version 14.10
-- Dumped by pg_dump version 15.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: constraints_layers_register; Type: TABLE DATA; Schema: constraints_metadata; Owner: edfreweb
--

INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (139, 'national_scenic_areas_scotland', 51, 2, 4, 2, 'https://www.data.gov.uk/dataset/8d9d285a-985d-4524-90a0-3238bca9f8f8/national-scenic-areas', 1, '', '2023-02-03', '2022-06-30', NULL, '2023-02-03 16:59:34.002032+00', NULL, 1, 'edfreweb', '');
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (141, 'gdl_scotland', 52, 2, 4, 2, 'https://www.data.gov.uk/dataset/8d9d285a-985d-4524-90a0-3238bca9f8f8/national-scenic-areas', 1, '', '2023-02-03', '2019-09-19', NULL, '2023-02-03 17:29:21.772971+00', NULL, 1, 'edfreweb', '');
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (142, 'green_belt_england', 50, 2, 2, 50, 'https://www.data.gov.uk/dataset/ccb505e0-67a8-4ace-b294-19a3cbff4861/english-local-authority-green-belt-dataset', 50, '', '2023-02-03', '2023-01-10', NULL, '2023-02-03 17:49:48.279794+00', NULL, 1, 'edfreweb', '');
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (143, 'national_forest_inventory_woodland_map_gb2020', 53, 1, 1, 51, 'https://data-forestry.opendata.arcgis.com/datasets/eb05bd0be3b449459b9ad0692a8fc203_0/explore', 1, '', '2023-06-12', '2022-06-30', NULL, '2023-06-12 08:15:22.666817+00', NULL, 1, 'edfreweb', '');
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (144, 'alc_grade_1', 54, 2, 2, 4, 'https://naturalengland-defra.opendata.arcgis.com/datasets/5d2477d8d04b41d4bbc9a8742f858f4d', 1, '', '2023-07-11', '2019-04-01', NULL, '2023-07-11 13:14:36.222564+00', NULL, 1, 'edfreweb', '');
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (3, 'sssi_england', 5, 2, 2, 4, 'naturalengland-defra.opendata.arcgis.com/datasets/Defra::sites-of-special-scientific-interest-england/about', 1, NULL, '2022-04-13', '2022-03-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (21, 'wild_land_scotland', 17, 2, 4, 1, 'cagmap.snh.gov.uk/natural-spaces/', 1, NULL, '2022-03-15', '2014-06-24', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (1, 'sac_scotland', 1, 2, 4, 1, 'cagmap.snh.gov.uk/natural-spaces/', 1, NULL, '2022-03-15', '2019-07-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (2, 'spa_england', 2, 2, 2, 4, 'naturalengland-defra.opendata.arcgis.com/datasets/special-protection-areas-england/explore?location=52.798326%2C3.451415%2C6.35', 1, NULL, '2022-04-13', '2021-06-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (4, 'nnr_england', 7, 2, 2, 4, 'naturalengland-defra.opendata.arcgis.com/datasets/Defra::national-nature-reserves-england/about', 1, NULL, '2022-04-13', '2022-01-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (5, 'lnr_england', 8, 2, 2, 4, 'naturalengland-defra.opendata.arcgis.com/datasets/Defra::local-nature-reserves-england/about', 1, NULL, '2022-04-13', '2022-03-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (6, 'national_parks_england', 11, 2, 2, 4, 'naturalengland-defra.opendata.arcgis.com/datasets/national-parks-england/explore', 1, NULL, '2022-04-14', '2022-04-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (7, 'esa_england', 3, 2, 2, 4, 'naturalengland-defra.opendata.arcgis.com/datasets/environmentally-sensitive-areas-england/explore?location=54.527649%2C-0.574842%2C6.04', 1, NULL, '2022-04-14', '2018-07-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (8, 'ancient_woodland_england', 4, 2, 2, 4, 'naturalengland-defra.opendata.arcgis.com/datasets/ancient-woodland-england/explore?location=54.525484%2C-1.121450%2C12.24', 1, NULL, '2022-04-14', '2022-03-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (10, 'aonb_england', 10, 2, 2, 4, 'naturalengland-defra.opendata.arcgis.com/datasets/6f2ad07d91304ad79cdecd52489d5046_0/explore', 1, NULL, '2022-04-14', '2020-08-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (11, 'sac_england', 1, 2, 2, 4, 'https://naturalengland-defra.opendata.arcgis.com/datasets/special-areas-of-conservation-england/explore?location=52.665096%2C-1.762599%2C6.89', 1, NULL, '2022-06-25', '2022-01-28', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (12, 'ramsar_england', 6, 2, 2, 4, 'https://naturalengland-defra.opendata.arcgis.com/datasets/13b5f06edc88471db479b49b4ac04a43_0/explore?location=52.621532%2C-2.520138%2C7.06', 1, NULL, '2022-06-25', '2020-10-02', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (13, 'country_parks_england', 12, 2, 2, 4, 'https://naturalengland-defra.opendata.arcgis.com/datasets/country-parks-england/explore?location=54.606936%2C-1.479326%2C11.55', 1, NULL, '2022-04-14', '2018-07-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (14, 'world_heritage_sites_england', 13, 2, 2, 6, 'https://historicengland.org.uk/listing/the-list/data-downloads', 1, NULL, '2022-04-14', '2021-08-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (16, 'spa_scotland', 2, 2, 4, 1, 'https://cagmap.snh.gov.uk/natural-spaces/dataset.jsp?code=SPA', 1, NULL, '2022-03-15', '2020-12-03', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (17, 'sssi_scotland', 5, 2, 4, 1, 'https://cagmap.snh.gov.uk/natural-spaces/dataset.jsp?code=SSSI', 1, NULL, '2022-03-15', '2020-12-09', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (18, 'parks_and_gardens_england', 15, 2, 2, 6, 'https://historicengland.org.uk/listing/the-list/data-downloads', 1, NULL, '2022-04-14', '2022-01-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (19, 'register_of_historic_battlefields_england', 16, 2, 2, 6, 'https://historicengland.org.uk/listing/the-list/data-downloads', 1, NULL, '2022-04-14', '2021-08-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (20, 'ramsar_scotland', 6, 2, 4, 1, 'cagmap.snh.gov.uk/natural-spaces/', 1, NULL, '2022-03-15', '2018-12-20', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (23, 'nnr_scotland', 7, 2, 4, 1, 'cagmap.snh.gov.uk/natural-spaces/', 1, NULL, '2022-03-15', '2018-05-21', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (24, 'lnr_scotland', 8, 2, 4, 1, 'cagmap.snh.gov.uk/natural-spaces/', 1, NULL, '2022-03-15', '2018-06-28', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (25, 'ancient_woodland_scotland', 4, 2, 4, 1, 'cagmap.snh.gov.uk/natural-spaces/', 1, NULL, '2022-03-15', '2012-04-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (26, 'scheduled_monuments_scotland', 14, 2, 4, 7, 'portal.historicenvironment.scot/downloads', 1, NULL, '2022-03-15', '2020-08-19', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (27, 'world_heritage_sites_scotland', 13, 2, 4, 7, 'portal.historicenvironment.scot/downloads', 1, NULL, '2022-03-15', '2015-11-04', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (28, 'battlefields_inventory_scotland', 16, 2, 4, 7, 'https://portal.historicenvironment.scot/downloads/battlefields', 1, NULL, '2022-07-21', '2016-09-28', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (29, 'biosphere_reserves_scotland', 18, 2, 4, 1, 'cagmap.snh.gov.uk/natural-spaces/', 1, NULL, '2022-03-15', '2015-06-15', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (30, 'nco_scotland', 19, 2, 4, 1, 'cagmap.snh.gov.uk/natural-spaces/', 1, NULL, '2022-03-15', '2017-11-21', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', 'Currently missing the SKY NCO');
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (31, 'naturescot_nature_reserve_scotland', 20, 2, 4, 1, 'cagmap.snh.gov.uk/natural-spaces/', 1, NULL, '2022-03-15', '2021-07-28', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (32, 'country_parks_scotland', 12, 2, 4, 1, 'cagmap.snh.gov.uk/natural-spaces/', 1, NULL, '2022-03-15', '2012-04-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (15, 'scheduled_monuments_england', 14, 2, 2, 6, 'https://historicengland.org.uk/listing/the-list/data-downloads', 1, NULL, '2022-04-14', '2022-04-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (22, 'national_parks_scotland', 11, 2, 4, 2, 'SpatialData.gov.scot', 1, NULL, '2022-03-16', NULL, NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);
INSERT INTO constraints_metadata.constraints_layers_register (id, name, development_constraint_id, admin_level_id, geographical_area_id, data_publisher_id, data_source, data_license_id, update_cycle, date_accessed_or_created, date_last_updated, date_next_updated, date_time_added_to_register, date_data_expires, user_id, database_user, notes) VALUES (9, 'heritage_coast_england', 9, 2, 2, 4, 'naturalengland-defra.opendata.arcgis.com/datasets/heritage-coasts-england/explore', 1, NULL, '2022-04-14', '2017-02-01', NULL, '2023-01-26 10:36:59.004745+00', NULL, NULL, 'postgres', NULL);


--
-- Name: constraints_layers_register_id_seq; Type: SEQUENCE SET; Schema: constraints_metadata; Owner: edfreweb
--

SELECT pg_catalog.setval('constraints_metadata.constraints_layers_register_id_seq', 144, true);


--
-- PostgreSQL database dump complete
--
