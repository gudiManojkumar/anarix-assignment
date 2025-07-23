CREATE TABLE ad_sales (
    date TEXT,
    item_id TEXT,
    ad_sales REAL,
    impressions INTEGER,
    ad_spend REAL,
    clicks INTEGER,
    units_sold INTEGER
);

CREATE TABLE total_sales (
    date TEXT,
    item_id TEXT,
    total_sales REAL,
    total_units_ordered INTEGER
);


CREATE TABLE eligibility (
    eligibility_datetime_utc TEXT,
    item_id TEXT,
    eligibility TEXT,
    message TEXT
);
