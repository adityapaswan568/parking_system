-- ============================================================
--  PARKING MANAGEMENT SYSTEM - DATABASE SETUP
--  Run this in MySQL before launching parking.py
-- ============================================================

-- Create database
CREATE DATABASE IF NOT EXISTS parking;
USE parking;

-- ── TABLE: parkmaster12 ──────────────────────────────────────
CREATE TABLE IF NOT EXISTS parkmaster12 (
    pid         INT             PRIMARY KEY,
    pnm         VARCHAR(50)     NOT NULL,
    level       VARCHAR(10)     NOT NULL,
    freespace   VARCHAR(3)      NOT NULL,   -- YES / NO
    vehicleno   VARCHAR(20)     NOT NULL,
    nod         INT             NOT NULL,   -- number of days
    payment     DECIMAL(10,2)   NOT NULL
);

-- ── TABLE: vehicle ───────────────────────────────────────────
CREATE TABLE IF NOT EXISTS vehicle (
    vid         INT             AUTO_INCREMENT PRIMARY KEY,
    pid         INT             NOT NULL,
    vnm         VARCHAR(50)     NOT NULL,
    dateofpur   DATE            NOT NULL,
    FOREIGN KEY (pid) REFERENCES parkmaster12(pid)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- ── SAMPLE DATA (optional, for testing) ──────────────────────
INSERT IGNORE INTO parkmaster12 VALUES
    (101, 'Slot A1', 'Ground', 'NO',  'DL01AB1234', 2, 40.00),
    (102, 'Slot B2', 'Level1', 'YES', 'UP32CD5678', 1, 20.00),
    (103, 'Slot C3', 'Level2', 'NO',  'MH12EF9012', 3, 60.00);

INSERT IGNORE INTO vehicle (pid, vnm, dateofpur) VALUES
    (101, 'Honda City',    '2019-06-15'),
    (102, 'Maruti Swift',  '2021-03-10'),
    (103, 'Hyundai i20',   '2020-11-22');

-- ── VERIFY ───────────────────────────────────────────────────
SELECT 'parkmaster12' AS table_name, COUNT(*) AS rows FROM parkmaster12
UNION ALL
SELECT 'vehicle',                    COUNT(*)          FROM vehicle;
