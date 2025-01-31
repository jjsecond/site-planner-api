DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'task_status_type') THEN
        CREATE TYPE task_status_type AS ENUM ('pending', 'in_progress', 'completed', 'canceled');
    END IF;
    
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'task_type') THEN
        CREATE TYPE task_type AS ENUM ('ground_works', 'first_fix', 'second_fix', 'third_fix', 'final_fix', 'surveys');
    END IF;
END $$;

CREATE TABLE IF NOT EXISTS task (
    id SERIAL PRIMARY KEY,
    site_id INTEGER NOT NULL REFERENCES site(id) ON DELETE CASCADE,
    plot_id INTEGER NOT NULL REFERENCES plot(id) ON DELETE CASCADE,
    company_id INTEGER NOT NULL REFERENCES company(id) ON DELETE CASCADE,
    task_name VARCHAR(100) NOT NULL,
    task_type task_type NOT NULL DEFAULT 'first_fix', 
    trade VARCHAR(50),
    status task_status_type NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);