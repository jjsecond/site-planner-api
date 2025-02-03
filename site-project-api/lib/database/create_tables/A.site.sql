CREATE TABLE IF NOT EXISTS sites (
    id SERIAL PRIMARY KEY,
    manager VARCHAR(80),
    site_name VARCHAR(100) NOT NULL,
    address VARCHAR(300) NOT NULL,
    site_contact_num VARCHAR(40) NOT NULL,
    site_plan_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);