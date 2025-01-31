CREATE TABLE IF NOT EXISTS certificate (
    id SERIAL PRIMARY KEY,
    site_id INTEGER NOT NULL REFERENCES site(id) ON DELETE CASCADE,
    plot_id INTEGER NOT NULL REFERENCES plot(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    cert_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);