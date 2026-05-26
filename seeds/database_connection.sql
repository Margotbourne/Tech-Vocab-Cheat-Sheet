-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, drop tables if they already exist so we start fresh every time we seed
DROP TABLE IF EXISTS tech_terms;

-- Create our new cheat sheet flashcards table
CREATE TABLE tech_terms (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(255),
    concept_name VARCHAR(255),
    analogy TEXT,
    key_notes TEXT
);

-- Let's seed it with one starter row just to test our connection later
INSERT INTO tech_terms (topic, concept_name, analogy, key_notes) VALUES 
('Backend', 'API', 'A waiter in a restaurant taking your order to the kitchen and bringing back food.', 'Application Programming Interface. Connects separate code components or interfaces.'),
('Database', 'Relational (SQL) vs. NoSQL', 'SQL is a neat Excel spreadsheet with locked rows. NoSQL is a folder of random mixed sticky notes.', 'SQL handles highly structured tables with relations (PostgreSQL). NoSQL handles loose unstructured document stores (MongoDB).'),
('Frontend', 'The DOM', 'The architectural blueprint framework of a house. JavaScript uses it to dynamically repaint walls or move furniture.', 'Document Object Model. The structural representation of HTML objects that browsers read and interact with.'),
('DevOps', 'CI/CD Pipeline', 'An automated car assembly line that runs continuous safety checks and paints cars automatically before rolling them onto the lot.', 'Continuous Integration / Continuous Deployment. Automates code testing, building, and live server updates.');